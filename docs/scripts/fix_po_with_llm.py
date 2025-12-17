#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LLM連携によるPO問題自動修正ツール
- 入力: po_issues.json（check_and_fix_po.py の出力）
- 各issueに対し、該当POのmsgid/msgstrを抽出してLLMで修正案を生成
- ルール: :doc:, :ref:, 外部リンク、**強調**等を保持、sphinx-designのリンク部は変更しない
- 可能ならその場で品質チェック（簡易）を行い、通過した場合のみ書き戻す
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Optional, Tuple

try:
    import ollama
except Exception:
    ollama = None

# 簡易品質チェック（translate_po.py に合わせたルール）
def basic_quality_check(msgid: str, msgstr: str) -> bool:
    if not msgstr or len(msgstr) < 1:
        return False
    # :doc:
    doc_refs_id = len(re.findall(r':doc:`[^`]+`', msgid))
    doc_refs_str = len(re.findall(r':doc:`[^`]+`', msgstr))
    if doc_refs_id != doc_refs_str:
        return False
    # :ref:
    ref_refs_id = len(re.findall(r':ref:`[^`]+`', msgid))
    ref_refs_str = len(re.findall(r':ref:`[^`]+`', msgstr))
    if ref_refs_id != ref_refs_str:
        return False
    # ** 強調
    strong_id = msgid.count('**')
    strong_str = msgstr.count('**')
    if strong_id != strong_str:
        return False
    # 外部リンク
    links_id = len(re.findall(r'<https?://[^>]+>__?', msgid))
    links_str = len(re.findall(r'<https?://[^>]+>__?', msgstr))
    if links_id != links_str:
        return False
    return True

SYSTEM_PROMPT = (
    "あなたはSphinxドキュメントのPO翻訳修正者です。以下を厳守して修正してください:\n"
    "- msgidに含まれる :doc:`...`、:ref:`...`、外部リンク、**強調** を msgstrでも必ず保持\n"
    "- sphinx-designのbutton/cardはラベルのみ翻訳し、リンク部分は変更しない\n"
    "- 改行とインデントは極力維持し、不要な空行は削減\n"
    "- 専門用語・固有名詞は原文尊重\n"
    "- 出力は修正済みの msgstr のみ（引用符不要、説明不要）\n"
)

USER_TEMPLATE = (
    "修正対象のmsgidと現msgstrは以下です。msgstrを規則に従って正しく修正してください。\n\n"
    "msgid:\n\"\"\"\n{msgid}\n\"\"\"\n\n"
    "current msgstr:\n\"\"\"\n{msgstr}\n\"\"\"\n"
)


def load_model() -> str:
    cfg = Path('translate_config.json')
    if cfg.exists():
        data = json.loads(cfg.read_text(encoding='utf-8'))
        return data.get('model', 'qwen2.5:7b-instruct-q5_K_M')
    return 'qwen2.5:7b-instruct-q5_K_M'


def extract_entry_by_line(po_path: Path, line_num: int) -> Optional[Tuple[str, str, int, int]]:
    """対象行付近の msgid/msgstr ブロックを抽出（テキストベース）"""
    lines = po_path.read_text(encoding='utf-8').splitlines()
    idx = max(0, min(len(lines) - 1, line_num))
    # 直前の msgid を探す
    start = idx
    while start >= 0 and not lines[start].startswith('msgid'):
        start -= 1
    if start < 0:
        return None
    # msgid 収集
    msgid = ''
    i = start
    m = re.match(r'msgid\s+"(.*)"', lines[i])
    msgid += (m.group(1) if m else '')
    i += 1
    while i < len(lines) and lines[i].strip().startswith('"'):
        msgid += re.match(r'^"(.*)"', lines[i]).group(1)
        i += 1
    # 次の msgstr
    if i >= len(lines) or not lines[i].startswith('msgstr'):
        return None
    msgstr_start = i
    m = re.match(r'msgstr\s+"(.*)"', lines[i])
    msgstr = (m.group(1) if m else '')
    i += 1
    while i < len(lines) and lines[i].strip().startswith('"'):
        msgstr += re.match(r'^"(.*)"', lines[i]).group(1)
        i += 1
    msgstr_end = i - 1
    return msgid, msgstr, msgstr_start, msgstr_end


def replace_msgstr_in_file(po_path: Path, new_msgstr: str, msgstr_start: int, msgstr_end: int):
    """msgstrブロックを1行形式に置換"""
    content = po_path.read_text(encoding='utf-8').splitlines()
    # エスケープ
    esc = new_msgstr.replace('"', '\\"')
    # 1行のmsgstrに再構築
    content[msgstr_start] = f'msgstr "{esc}"'
    # 既存の継続行は削除
    del content[msgstr_start + 1: msgstr_end + 1]
    po_path.write_text('\n'.join(content) + '\n', encoding='utf-8')


def llm_fix(msgid: str, msgstr: str) -> Optional[str]:
    if ollama is None:
        print('✗ ollama が未インストールのためLLM修正はスキップします')
        return None
    model = load_model()
    prompt = USER_TEMPLATE.format(msgid=msgid, msgstr=msgstr)
    res = ollama.chat(
        model=model,
        messages=[{'role': 'system', 'content': SYSTEM_PROMPT}, {'role': 'user', 'content': prompt}],
        options={'temperature': 0.2, 'num_predict': 1024}
    )
    out = (res['message']['content'] or '').strip()
    # 引用符/コードフェンス等のノイズ除去
    out = out.strip('"')
    out = out.replace('```', '')
    # 3行以上の改行は2行へ
    out = re.sub(r'\n{3,}', '\n\n', out)
    # 行末空白除去
    out = '\n'.join(line.rstrip() for line in out.split('\n'))
    return out


def main():
    import argparse
    p = argparse.ArgumentParser(description='LLM連携PO自動修正')
    p.add_argument('--issues', default='po_issues.json', help='問題JSONファイル')
    p.add_argument('--limit', type=int, default=0, help='処理する最大件数(0は全件)')
    p.add_argument('--types', nargs='*', help='対象issue type絞り込み (例: emphasis_mismatch missing_doc_ref)')
    p.add_argument('--dry-run', action='store_true', help='書き込みせず候補のみ出力')
    args = p.parse_args()

    issues_path = Path(args.issues)
    if not issues_path.exists():
        print(f'✗ issuesファイルが見つかりません: {issues_path}', file=sys.stderr)
        sys.exit(1)

    try:
        issues = json.loads(issues_path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f'✗ JSON読み込みエラー: {e}', file=sys.stderr)
        sys.exit(1)

    count = 0
    fixed = 0
    skipped = 0
    for it in issues:
        issue_type = it.get('type') or it.get('issue_type')
        po_file = it.get('file') or it.get('po_file')
        line = it.get('line') or it.get('line_num')
        if args.types and issue_type not in args.types:
            continue
        if not po_file or line is None:
            skipped += 1
            continue
        po_path = Path(po_file)
        if not po_path.exists():
            # ルート相対の場合
            rel = Path(str(po_file).replace('..\\', '').replace('..//', ''))
            if rel.exists():
                po_path = rel
            else:
                print(f'  ⚠ ファイル未検出: {po_file}')
                skipped += 1
                continue
        # エントリ抽出
        entry = extract_entry_by_line(po_path, int(line))
        if not entry:
            print(f'  ⚠ エントリ抽出失敗: {po_path}#L{line}')
            skipped += 1
            continue
        msgid, msgstr, msgstr_start, msgstr_end = entry
        # LLM修正
        new_msgstr = llm_fix(msgid, msgstr)
        if not new_msgstr:
            skipped += 1
            continue
        # 品質チェック
        if not basic_quality_check(msgid, new_msgstr):
            print(f'  ⚠ 品質チェック不合格: {po_path}#L{line}')
            skipped += 1
            continue
        # 書き戻し
        if not args.dry_run:
            replace_msgstr_in_file(po_path, new_msgstr, msgstr_start, msgstr_end)
            fixed += 1
        count += 1
        if args.limit and fixed >= args.limit:
            break
    print(f'処理: {count} / 修正: {fixed} / スキップ: {skipped}')

if __name__ == '__main__':
    main()
