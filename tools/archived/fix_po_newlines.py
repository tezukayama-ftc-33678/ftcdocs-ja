#!/usr/bin/env python3
"""
POファイルの改行エラーを修正するスクリプト

msgstr や msgid の後に改行がない場合などの構文エラーを修正します。
"""

import sys
import re
from pathlib import Path
from typing import List
import argparse


def fix_missing_newlines(content: str) -> tuple[str, int]:
    """
    msgstr または msgid の後に改行が欠けている場合を修正
    
    例:
    msgstr "..."msgstr "..." → msgstr "..."\nmsgstr "..."
    msgstr ""msgstr "" → msgstr ""\nmsgstr ""
    """
    fixes = 0
    
    # msgid/msgstr の後に別のmsgid/msgstrが直接続いている場合
    patterns = [
        (r'(msgstr\s+"[^"]*")"(msgstr)', r'\1"\n\n\2'),  # msgstr "text"msgstr
        (r'(msgstr\s+"")"(msgstr)', r'\1"\n\n\2'),       # msgstr ""msgstr
        (r'(msgid\s+"[^"]*")"(msgid)', r'\1"\n\n\2'),    # msgid "text"msgid
        (r'(msgid\s+"")"(msgid)', r'\1"\n\n\2'),         # msgid ""msgid
        (r'(msgstr\s+"[^"]*")"(msgid)', r'\1"\n\n\2'),   # msgstr "text"msgid
        (r'(msgstr\s+"")"(msgid)', r'\1"\n\n\2'),        # msgstr ""msgid
    ]
    
    original = content
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    if content != original:
        fixes = content.count('\n') - original.count('\n')
    
    return content, fixes


def fix_po_file(file_path: Path, dry_run: bool = False) -> tuple[bool, int]:
    """単一のPOファイルを修正"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original = f.read()
    except Exception as e:
        print(f"エラー: {file_path} の読み込み失敗: {e}")
        return False, 0
    
    content, fixes = fix_missing_newlines(original)
    
    if fixes > 0 and not dry_run:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, fixes
        except Exception as e:
            print(f"エラー: {file_path} の書き込み失敗: {e}")
            return False, 0
    
    return True, fixes


def find_problematic_files(warning_log: Path) -> List[Path]:
    """警告ログから問題のあるファイルを抽出"""
    if not warning_log.exists():
        return []
    
    files = []
    with open(warning_log, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # "reading error: path/to/file.po" のパターンを検索
    pattern = r'reading error: (.+?\.po),'
    matches = re.findall(pattern, content)
    
    for match in matches:
        if '../../locales/' in match:
            rel_path = match.split('../../locales/')[1]
            file_path = Path('locales') / rel_path
            if file_path.exists() and file_path not in files:
                files.append(file_path)
    
    return files


def main():
    parser = argparse.ArgumentParser(
        description='POファイルの改行エラーを修正'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='実際の変更は行わず、検出のみを実行'
    )
    parser.add_argument(
        '--warning-log',
        type=Path,
        default=Path('/tmp/build_warnings_final.log'),
        help='警告ログファイルのパス'
    )
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("PO改行エラー修正スクリプト")
    print("=" * 70)
    
    if args.dry_run:
        print("\n*** DRY-RUN モード: 実際の変更は行いません ***\n")
    
    # 問題のあるファイルを検索
    print(f"\n警告ログから問題のあるファイルを検索中...")
    files = find_problematic_files(args.warning_log)
    
    print(f"\n改行エラーの可能性があるファイル: {len(files)} 件")
    
    if len(files) == 0:
        print("\n対象ファイルが見つかりませんでした。")
        return
    
    # 各ファイルを処理
    total_fixes = 0
    success_count = 0
    
    print("\n修正を実行中...\n")
    
    for i, file_path in enumerate(files, 1):
        print(f"[{i}/{len(files)}] {file_path}")
        
        success, fixes = fix_po_file(file_path, args.dry_run)
        
        if success:
            success_count += 1
            if fixes > 0:
                total_fixes += fixes
                print(f"  → 修正: {fixes} 箇所")
            else:
                print(f"  → 修正不要")
        else:
            print(f"  → 失敗")
    
    # サマリー
    print("\n" + "=" * 70)
    print("修正結果サマリー")
    print("=" * 70)
    print(f"処理ファイル数:      {len(files)}")
    print(f"修正箇所数:          {total_fixes}")
    print(f"成功ファイル数:      {success_count}")
    
    if not args.dry_run and total_fixes > 0:
        print(f"\n✓ {total_fixes} 箇所を修正しました。")
        print("\n次のステップ:")
        print("1. ビルドを実行して警告が減少したか確認")
    elif args.dry_run:
        print(f"\n次のステップ:")
        print("--dry-run オプションを外して実際の修正を実行")
    
    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
