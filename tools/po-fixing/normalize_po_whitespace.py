#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
POファイルの改行・空白正規化ツール
- 余分な改行(3行以上)を2行に圧縮
- 行末の余分な空白を除去
- 文末の改行を常に除去（モデルが末尾に\nを挿入する癖の対策）
- 単一行のmsgidに対して、全体trim
- 誤挿入されたコードフェンス(``` )を除去（msgidに無い場合）
"""

import os
import re
import sys
from pathlib import Path
import polib


def normalize_msgstr(msgid: str, msgstr: str) -> str:
    s = msgstr.replace('\r\n', '\n')
    # 行末空白除去
    s = '\n'.join(line.rstrip() for line in s.split('\n'))
    # 3行以上の連続改行を2行へ
    s = re.sub(r'\n{3,}', '\n\n', s)
    # 文末改行を常に除去（内部の段落改行は保持）
    s = s.rstrip('\n')
    # msgidに改行がない場合は末尾の改行を削除し、全体をtrim
    if '\n' not in msgid:
        s = s.strip()
    # 誤ったコードフェンスの除去（msgidに無ければ削除）
    if '```' not in msgid and '```' in s:
        s = s.replace('```', '')
    return s


def process_po_file(po_path: Path) -> int:
    try:
        po = polib.pofile(str(po_path), encoding='utf-8')
    except Exception as e:
        # パース不能なPOはスキップ（後続のチェック/ビルドで検出される）
        print(f"  ⚠ 解析不可のためスキップ: {po_path} ({e})")
        return 0
    changes = 0
    for entry in po:
        if entry.msgstr:
            new_str = normalize_msgstr(entry.msgid, entry.msgstr)
            if new_str != entry.msgstr:
                entry.msgstr = new_str
                changes += 1
    if changes:
        po.save()
    return changes


def main():
    import argparse
    parser = argparse.ArgumentParser(description='PO改行・空白正規化')
    parser.add_argument('--po-dir', required=True, help='POディレクトリ (例: ../locales/ja/LC_MESSAGES)')
    args = parser.parse_args()

    base = Path(args.po_dir)
    if not base.exists():
        print(f'✗ ディレクトリが見つかりません: {base}', file=sys.stderr)
        sys.exit(1)

    po_files = list(base.rglob('*.po'))
    if not po_files:
        print(f'⚠ POファイルが見つかりません: {base}')
        sys.exit(0)

    total_changes = 0
    for po in po_files:
        changes = process_po_file(po)
        total_changes += changes
        if changes:
            print(f'  ✓ 正規化: {po} （{changes}エントリ）')
    print(f'合計修正エントリ数: {total_changes}')

if __name__ == '__main__':
    main()
