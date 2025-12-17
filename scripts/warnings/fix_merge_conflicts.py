#!/usr/bin/env python3
"""
Git merge conflict markers を自動的に削除するスクリプト

このスクリプトは、POファイルに残っているGitのマージコンフリクトマーカー
(<<<<<<<, =======, >>>>>>>) を検出して自動的に削除します。
マージコンフリクトの "HEAD" 側（上部）のコンテンツを保持します。
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple
import argparse


def find_po_files_with_conflicts(locales_dir: Path) -> List[Path]:
    """
    マージコンフリクトマーカーを含むPOファイルを検索
    """
    conflict_files = []
    
    for po_file in locales_dir.rglob("*.po"):
        try:
            with open(po_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if '<<<<<<< HEAD' in content or '=======' in content or '>>>>>>>' in content:
                    conflict_files.append(po_file)
        except Exception as e:
            print(f"警告: {po_file} の読み込みエラー: {e}")
    
    return conflict_files


def fix_merge_conflicts(file_path: Path, dry_run: bool = False) -> Tuple[bool, int, int]:
    """
    単一のPOファイルのマージコンフリクトを修正
    
    戻り値: (success, conflicts_found, conflicts_fixed)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"エラー: {file_path} の読み込み失敗: {e}")
        return False, 0, 0
    
    # マージコンフリクトマーカーを検出
    conflicts_found = 0
    conflicts_fixed = 0
    new_lines = []
    in_conflict = False
    in_head_section = False
    conflict_start_line = -1
    head_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # マージコンフリクトの開始
        if line.startswith('<<<<<<< HEAD'):
            in_conflict = True
            in_head_section = True
            conflict_start_line = i
            head_lines = []
            conflicts_found += 1
            i += 1
            continue
        
        # マージコンフリクトの中間（HEAD側終了、incoming側開始）
        elif line.startswith('=======') and in_conflict:
            in_head_section = False
            i += 1
            continue
        
        # マージコンフリクトの終了
        elif line.startswith('>>>>>>>') and in_conflict:
            # HEAD側のコンテンツを保持
            new_lines.extend(head_lines)
            in_conflict = False
            in_head_section = False
            conflicts_fixed += 1
            i += 1
            continue
        
        # 通常の行処理
        if in_conflict:
            if in_head_section:
                # HEAD側の内容を保存
                head_lines.append(line)
            # else: incoming側は無視
        else:
            # コンフリクト外の通常行
            new_lines.append(line)
        
        i += 1
    
    # ファイルに書き込み
    if conflicts_fixed > 0 and not dry_run:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            return True, conflicts_found, conflicts_fixed
        except Exception as e:
            print(f"エラー: {file_path} の書き込み失敗: {e}")
            return False, conflicts_found, 0
    
    return True, conflicts_found, conflicts_fixed


def main():
    parser = argparse.ArgumentParser(
        description='POファイルのGitマージコンフリクトマーカーを自動削除'
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
        help='localesディレクトリのパス (デフォルト: ../../locales)'
    )
    
    args = parser.parse_args()
    
    locales_dir = args.locales_dir
    
    if not locales_dir.exists():
        print(f"エラー: {locales_dir} が見つかりません")
        sys.exit(1)
    
    print("=" * 70)
    print("Git マージコンフリクト修正スクリプト")
    print("=" * 70)
    
    if args.dry_run:
        print("\n*** DRY-RUN モード: 実際の変更は行いません ***\n")
    
    # マージコンフリクトを含むファイルを検索
    print(f"\n{locales_dir} 配下のPOファイルを検索中...")
    conflict_files = find_po_files_with_conflicts(locales_dir)
    
    print(f"\nマージコンフリクトが見つかったファイル: {len(conflict_files)} 件")
    
    if len(conflict_files) == 0:
        print("\n✓ マージコンフリクトは見つかりませんでした。")
        return
    
    # 各ファイルを修正
    total_conflicts = 0
    total_fixed = 0
    failed_files = []
    
    print("\n修正を実行中...\n")
    
    for i, file_path in enumerate(conflict_files, 1):
        relative_path = file_path.relative_to(locales_dir)
        print(f"[{i}/{len(conflict_files)}] {relative_path}")
        
        success, found, fixed = fix_merge_conflicts(file_path, args.dry_run)
        
        if success:
            total_conflicts += found
            total_fixed += fixed
            print(f"  → コンフリクト検出: {found} 件, 修正: {fixed} 件")
        else:
            failed_files.append(file_path)
            print(f"  → 失敗")
    
    # サマリー
    print("\n" + "=" * 70)
    print("修正結果サマリー")
    print("=" * 70)
    print(f"処理ファイル数:      {len(conflict_files)}")
    print(f"検出コンフリクト数:  {total_conflicts}")
    print(f"修正コンフリクト数:  {total_fixed}")
    print(f"失敗ファイル数:      {len(failed_files)}")
    
    if failed_files:
        print("\n失敗したファイル:")
        for f in failed_files:
            print(f"  - {f.relative_to(locales_dir)}")
    
    if not args.dry_run and total_fixed > 0:
        print(f"\n✓ {total_fixed} 件のマージコンフリクトを修正しました。")
        print("\n次のステップ:")
        print("1. ビルドを実行して警告が減少したか確認:")
        print("   cd docs && make clean && make html-ja")
        print("2. git diff で変更を確認")
        print("3. 問題がなければコミット")
    elif args.dry_run:
        print(f"\n次のステップ:")
        print("--dry-run オプションを外して実際の修正を実行:")
        print(f"  python {Path(__file__).name}")
    
    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
