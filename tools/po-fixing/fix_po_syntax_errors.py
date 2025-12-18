#!/usr/bin/env python3
"""
POファイルの構文エラーを自動修正するスクリプト

このスクリプトは、POファイルのよくある構文エラーを検出して修正します：
- エスケープされていない二重引用符
- 不正な複数行文字列
- 文字列の閉じ忘れ
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Optional
import argparse


def find_problematic_po_files(locales_dir: Path, warning_log: Optional[Path] = None) -> List[Path]:
    """
    構文エラーのあるPOファイルを検索
    """
    problematic_files = []
    
    if warning_log and warning_log.exists():
        # 警告ログから問題のあるファイルを抽出
        with open(warning_log, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # "reading error" のパターンを検索
        pattern = r'reading error: (.+?\.po),'
        matches = re.findall(pattern, content)
        
        for match in matches:
            # 絶対パスから相対パスに変換
            if '../../locales/' in match:
                rel_path = match.split('../../locales/')[1]
                po_file = locales_dir / rel_path
                if po_file.exists() and po_file not in problematic_files:
                    problematic_files.append(po_file)
    
    return problematic_files


def fix_unescaped_quotes(content: str) -> Tuple[str, int]:
    """
    エスケープされていない二重引用符を修正
    
    msgstr "text with "quote" inside" を
    msgstr "text with \"quote\" inside" に修正
    """
    lines = content.split('\n')
    fixed_lines = []
    fixes = 0
    
    for i, line in enumerate(lines):
        # msgid や msgstr 行を処理
        if line.startswith('msgid ') or line.startswith('msgstr '):
            # 行の内容を解析
            if line.count('"') >= 2:
                # 最初と最後の引用符を特定
                first_quote = line.index('"')
                # 最初の引用符の後に他の引用符があるか確認
                remaining = line[first_quote + 1:]
                
                # 最後の引用符を探す（行末から）
                if remaining.endswith('"'):
                    # 中間の引用符をエスケープ
                    middle = remaining[:-1]  # 最後の " を除外
                    
                    # 既にエスケープされていない " を探してエスケープ
                    if '"' in middle and '\\"' not in middle:
                        # 単純な置換（既にエスケープされているものは除外）
                        middle_fixed = middle.replace('"', '\\"')
                        fixed_line = line[:first_quote + 1] + middle_fixed + '"'
                        
                        if fixed_line != line:
                            fixed_lines.append(fixed_line)
                            fixes += 1
                            continue
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), fixes


def fix_multiline_strings(content: str) -> Tuple[str, int]:
    """
    不正な複数行文字列を修正
    """
    lines = content.split('\n')
    fixed_lines = []
    fixes = 0
    in_msgstr = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # msgstr の開始
        if line.startswith('msgstr '):
            # msgstr "" で始まる複数行の場合
            if line.strip() == 'msgstr ""' or line.strip() == 'msgstr ""':
                in_msgstr = True
                fixed_lines.append(line)
            else:
                # 単一行のmsgstr
                in_msgstr = False
                fixed_lines.append(line)
        elif in_msgstr:
            # 複数行の続き
            if line.startswith('"') and line.endswith('"'):
                fixed_lines.append(line)
            elif line.strip() == '':
                # 空行で終了
                in_msgstr = False
                fixed_lines.append(line)
            else:
                # 不正な行
                if not line.startswith('"'):
                    # 引用符で囲む
                    fixed_lines.append(f'"{line}"')
                    fixes += 1
                else:
                    fixed_lines.append(line)
        else:
            fixed_lines.append(line)
        
        i += 1
    
    return '\n'.join(fixed_lines), fixes


def validate_po_file(file_path: Path) -> Optional[str]:
    """
    POファイルを検証してエラーメッセージを返す
    """
    try:
        import polib
        polib.pofile(str(file_path))
        return None
    except Exception as e:
        return str(e)


def fix_po_file(file_path: Path, dry_run: bool = False) -> Tuple[bool, int]:
    """
    単一のPOファイルを修正
    
    戻り値: (success, fixes_applied)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"エラー: {file_path} の読み込み失敗: {e}")
        return False, 0
    
    content = original_content
    total_fixes = 0
    
    # 各種修正を適用
    content, fixes = fix_unescaped_quotes(content)
    total_fixes += fixes
    
    content, fixes = fix_multiline_strings(content)
    total_fixes += fixes
    
    # 変更があった場合のみ書き込み
    if total_fixes > 0 and not dry_run:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, total_fixes
        except Exception as e:
            print(f"エラー: {file_path} の書き込み失敗: {e}")
            return False, 0
    
    return True, total_fixes


def main():
    parser = argparse.ArgumentParser(
        description='POファイルの構文エラーを自動修正'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='実際の変更は行わず、検出のみを実行'
    )
    parser.add_argument(
        '--locales-dir',
        type=Path,
        default=Path(__file__).parent.parent.parent / 'locales',
        help='localesディレクトリのパス'
    )
    parser.add_argument(
        '--warning-log',
        type=Path,
        default=Path('/tmp/build_warnings_after_merge_fix.log'),
        help='警告ログファイルのパス'
    )
    
    args = parser.parse_args()
    
    locales_dir = args.locales_dir
    
    if not locales_dir.exists():
        print(f"エラー: {locales_dir} が見つかりません")
        sys.exit(1)
    
    print("=" * 70)
    print("PO構文エラー修正スクリプト")
    print("=" * 70)
    
    if args.dry_run:
        print("\n*** DRY-RUN モード: 実際の変更は行いません ***\n")
    
    # 問題のあるファイルを検索
    print(f"\n警告ログから問題のあるファイルを検索中...")
    problematic_files = find_problematic_po_files(locales_dir, args.warning_log)
    
    print(f"\n構文エラーが見つかったファイル: {len(problematic_files)} 件")
    
    if len(problematic_files) == 0:
        print("\n✓ 構文エラーは見つかりませんでした。")
        return
    
    # 各ファイルを修正
    total_fixes = 0
    failed_files = []
    
    print("\n修正を実行中...\n")
    
    for i, file_path in enumerate(problematic_files, 1):
        relative_path = file_path.relative_to(locales_dir)
        print(f"[{i}/{len(problematic_files)}] {relative_path}")
        
        # 修正前のエラーを確認
        error_before = validate_po_file(file_path)
        if error_before:
            print(f"  エラー: {error_before[:100]}...")
        
        success, fixes = fix_po_file(file_path, args.dry_run)
        
        if success and fixes > 0:
            total_fixes += fixes
            print(f"  → 修正適用: {fixes} 件")
            
            # 修正後の検証
            if not args.dry_run:
                error_after = validate_po_file(file_path)
                if error_after:
                    print(f"  ⚠ まだエラーあり: {error_after[:100]}...")
                    failed_files.append(file_path)
                else:
                    print(f"  ✓ 修正完了")
        elif not success:
            failed_files.append(file_path)
            print(f"  → 失敗")
        else:
            print(f"  → 修正不要")
    
    # サマリー
    print("\n" + "=" * 70)
    print("修正結果サマリー")
    print("=" * 70)
    print(f"処理ファイル数:      {len(problematic_files)}")
    print(f"適用した修正数:      {total_fixes}")
    print(f"修正失敗ファイル数:  {len(failed_files)}")
    
    if failed_files:
        print("\n手動修正が必要なファイル:")
        for f in failed_files:
            print(f"  - {f.relative_to(locales_dir)}")
    
    if not args.dry_run and total_fixes > 0:
        print(f"\n✓ {total_fixes} 件の修正を適用しました。")
        print("\n次のステップ:")
        print("1. ビルドを実行して警告が減少したか確認")
        print("2. 手動修正が必要なファイルを確認")
    elif args.dry_run:
        print(f"\n次のステップ:")
        print("--dry-run オプションを外して実際の修正を実行")
    
    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
