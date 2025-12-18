#!/usr/bin/env python3
"""
簡体字・中国語が混入している日本語.poファイルを検出するスクリプト

日本語の翻訳ファイル(.po)に誤って含まれている簡体字や中国語表現を検出します。
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple
import polib

# 簡体字特有の文字（日本語では使われない、または日本語とは異なる形の簡体字のみ）
# 日本語の常用漢字と重複するものは除外
SIMPLIFIED_CHINESE_CHARS = set([
    '为', '拥', '态', '估', '镜', '头', '厅', '览', '购', '谁', '块', '际', 
    '习', '远', '让', '边', '务', '验', '压', '担', '处', '团', '阶', '员',
    '调', '导', '测', '协', '围', '确', '阳', '养', '层', '双', '医', '审',
    '护', '坏', '优', '获', '临', '预', '规', '织', '奖', '随', '扩', '杂',
    '输', '维', '缺', '另', '评', '错', '须', '怀', '产', '业', '们', '发',
    '经', '应', '对', '时', '进', '实', '现', '动', '过', '问', '题', '两',
    '这', '关', '开', '间', '样', '级', '义', '变', '观', '认', '识', '议',
    '标', '环', '节', '农', '门', '战', '较', '续', '选', '传', '带', '广',
    '术', '极', '备', '组', '队', '费', '况', '质', '达', '资', '显', '响',
    '专', '旧', '尽'
])

# 中国語特有の文法パターンと表現
# 明らかに中国語の文章パターンのみを検出
CHINESE_PATTERNS = [
    r'为了',           # ~のために（中国語特有）
    r'对于',           # ~について（中国語特有）
    r'的话',           # ~の場合（中国語特有）
    r'通过.{0,5}来',   # ~を通じて~する（中国語特有）
    r'拥有',           # 持つ（中国語）
    r'姿态',           # 姿勢（中国語簡体字）
    r'估计',           # 推定（中国語簡体字）
    r'镜头',           # レンズ（中国語簡体字）
    r'校准',           # キャリブレーション（中国語）
    r'内在参数',       # 内部パラメータ（中国語）
    r'分辨率',         # 解像度（中国語）
    r'都需要',         # すべて必要（中国語特有）
    r'可以通过',       # ~を通じて（中国語特有）
    r'甚至可以',       # さらに~できる（中国語特有）
    r'只有.*才',       # ~でなければ（中国語特有）
    r'无论.*都',       # ~に関わらず（中国語特有）
    r'不仅.*而且',     # ~だけでなく（中国語特有）
    r'虽然.*但是',     # ~だけれども（中国語特有）
    r'因为.*所以',     # ~だから（中国語特有）
    r'如果.*就',       # もし~ならば（中国語特有）
    r'乃至',           # ないし（中国語）
    r'亦即',           # すなわち（中国語）
    r'即可',           # ~すればよい（中国語）
    r'企图',           # たくらむ（中国語）
    r'左侧|右侧',      # 左側/右側（中国語）
]


def detect_chinese_in_text(text: str) -> List[Tuple[str, int, str]]:
    """
    テキスト内の簡体字や中国語パターンを検出
    
    Returns:
        List of (issue_type, position, matched_text) tuples
    """
    issues = []
    
    # 簡体字の検出
    for i, char in enumerate(text):
        if char in SIMPLIFIED_CHINESE_CHARS:
            # 前後の文脈を取得（最大20文字）
            start = max(0, i - 10)
            end = min(len(text), i + 10)
            context = text[start:end]
            issues.append(('simplified_char', i, f'{char} (context: {context})'))
    
    # 中国語パターンの検出
    for pattern in CHINESE_PATTERNS:
        for match in re.finditer(pattern, text):
            start = max(0, match.start() - 10)
            end = min(len(text), match.end() + 10)
            context = text[start:end]
            issues.append(('chinese_pattern', match.start(), f'{match.group()} (context: {context})'))
    
    # 重複を除去（同じ位置の検出を避ける）
    seen_positions = set()
    unique_issues = []
    for issue_type, pos, text in issues:
        if pos not in seen_positions:
            unique_issues.append((issue_type, pos, text))
            seen_positions.add(pos)
    
    return unique_issues


def scan_po_file(po_path: Path) -> Dict:
    """
    単一の.poファイルをスキャンして中国語を検出
    
    Returns:
        Dict with file info and detected issues
    """
    try:
        po = polib.pofile(str(po_path))
    except Exception as e:
        return {
            'file': str(po_path),
            'error': f'Failed to parse: {str(e)}',
            'issues': []
        }
    
    issues = []
    
    for entry in po:
        # msgstr（翻訳された文字列）をチェック
        if entry.msgstr:
            chinese_issues = detect_chinese_in_text(entry.msgstr)
            if chinese_issues:
                issues.append({
                    'msgid': entry.msgid[:100],  # 最初の100文字
                    'msgstr': entry.msgstr[:200],  # 最初の200文字
                    'line': entry.linenum,
                    'chinese_found': chinese_issues
                })
    
    if issues:
        return {
            'file': str(po_path),
            'issue_count': len(issues),
            'issues': issues
        }
    
    return None


def scan_all_po_files(base_dir: Path) -> List[Dict]:
    """
    locales/ja/LC_MESSAGES配下の全.poファイルをスキャン
    """
    ja_messages_dir = base_dir / 'locales' / 'ja' / 'LC_MESSAGES'
    
    if not ja_messages_dir.exists():
        print(f"Error: Directory not found: {ja_messages_dir}")
        return []
    
    po_files = list(ja_messages_dir.rglob('*.po'))
    print(f"Found {len(po_files)} .po files to scan...")
    
    problematic_files = []
    
    for i, po_file in enumerate(po_files, 1):
        print(f"[{i}/{len(po_files)}] Scanning: {po_file.relative_to(base_dir)}")
        result = scan_po_file(po_file)
        if result:
            problematic_files.append(result)
    
    return problematic_files


def generate_report(results: List[Dict], output_file: Path):
    """
    検出結果のレポートを生成
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 簡体字・中国語混入検出レポート\n\n")
        f.write(f"検出日時: {Path(__file__).stat().st_mtime}\n\n")
        f.write(f"## サマリー\n\n")
        f.write(f"- 問題のあるファイル数: {len(results)}\n")
        
        total_issues = sum(r['issue_count'] for r in results)
        f.write(f"- 検出された問題箇所: {total_issues}\n\n")
        
        f.write("## 問題ファイル一覧\n\n")
        
        for result in results:
            if 'error' in result:
                f.write(f"### {result['file']}\n\n")
                f.write(f"**エラー**: {result['error']}\n\n")
                continue
            
            f.write(f"### {result['file']}\n\n")
            f.write(f"問題箇所: {result['issue_count']}件\n\n")
            
            for issue in result['issues'][:10]:  # 最初の10件のみ表示
                f.write(f"#### Line {issue['line']}\n\n")
                f.write(f"**原文 (msgid)**: {issue['msgid']}\n\n")
                f.write(f"**翻訳 (msgstr)**: {issue['msgstr']}\n\n")
                f.write("**検出された中国語**:\n")
                for issue_type, pos, text in issue['chinese_found']:
                    f.write(f"- [{issue_type}] 位置 {pos}: {text}\n")
                f.write("\n")
            
            if result['issue_count'] > 10:
                f.write(f"... 他 {result['issue_count'] - 10} 件\n\n")
            
            f.write("---\n\n")


def main():
    # スクリプトの場所からワークスペースルートを推定
    script_dir = Path(__file__).resolve().parent
    workspace_root = script_dir.parent.parent
    
    print(f"Workspace root: {workspace_root}")
    print("=" * 60)
    
    # スキャン実行
    results = scan_all_po_files(workspace_root)
    
    # 結果を表示
    print("\n" + "=" * 60)
    print(f"スキャン完了: {len(results)} ファイルに問題が見つかりました")
    
    if results:
        print("\n問題のあるファイル:")
        for result in results:
            if 'error' in result:
                print(f"  - {result['file']} (エラー)")
            else:
                print(f"  - {result['file']} ({result['issue_count']}件)")
        
        # レポート生成
        report_file = workspace_root / 'chinese_chars_report.md'
        generate_report(results, report_file)
        print(f"\n詳細レポートを生成しました: {report_file}")
    else:
        print("\n問題は見つかりませんでした！")


if __name__ == '__main__':
    main()
