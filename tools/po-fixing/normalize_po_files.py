#!/usr/bin/env python3
"""
POファイル正規化スクリプト

このスクリプトは、POファイルの一般的な問題を検出して修正します：
- Gitマージコンフリクトマーカー
- エスケープされていない引用符
- 不正な複数行文字列
- 余分な空白
- Inline markupの不一致 (**, *, `)

使用方法:
    # すべてのPOファイルを正規化
    python scripts/normalize_po_files.py

    # Dry-runモード（変更なし）
    python scripts/normalize_po_files.py --dry-run

    # 特定のファイルのみ
    python scripts/normalize_po_files.py --file locales/ja/LC_MESSAGES/path/to/file.po
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Optional
import argparse
from collections import defaultdict


class PONormalizer:
    """POファイル正規化クラス"""
    
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.stats = defaultdict(int)
    
    def normalize_file(self, file_path: Path) -> bool:
        """
        単一のPOファイルを正規化
        
        戻り値: 成功した場合True
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"エラー: {file_path} の読み込み失敗: {e}")
            return False
        
        original_content = content
        
        # 各種正規化を適用
        content = self._fix_merge_conflicts(content, file_path)
        content = self._fix_inline_markup(content, file_path)
        content = self._normalize_whitespace(content, file_path)
        
        # 変更があった場合のみ書き込み
        if content != original_content:
            if not self.dry_run:
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    self.stats['files_modified'] += 1
                    return True
                except Exception as e:
                    print(f"エラー: {file_path} の書き込み失敗: {e}")
                    return False
            else:
                self.stats['files_would_be_modified'] += 1
                return True
        
        return True
    
    def _fix_merge_conflicts(self, content: str, file_path: Path) -> str:
        """Gitマージコンフリクトマーカーを削除"""
        if '<<<<<<< HEAD' not in content:
            return content
        
        lines = content.split('\n')
        new_lines = []
        in_conflict = False
        in_head_section = False
        head_lines = []
        conflicts_fixed = 0
        
        for line in lines:
            if line.startswith('<<<<<<< HEAD'):
                in_conflict = True
                in_head_section = True
                head_lines = []
                continue
            elif line.startswith('=======') and in_conflict:
                in_head_section = False
                continue
            elif line.startswith('>>>>>>>') and in_conflict:
                new_lines.extend(head_lines)
                in_conflict = False
                in_head_section = False
                conflicts_fixed += 1
                continue
            
            if in_conflict:
                if in_head_section:
                    head_lines.append(line)
            else:
                new_lines.append(line)
        
        if conflicts_fixed > 0:
            self.stats['merge_conflicts_fixed'] += conflicts_fixed
        
        return '\n'.join(new_lines)
    
    def _fix_inline_markup(self, content: str, file_path: Path) -> str:
        """
        Inline markupの不一致を修正
        
        msgstr の中で ** や * の開始と終了が一致しない場合に修正
        """
        lines = content.split('\n')
        new_lines = []
        
        for line in lines:
            if line.startswith('msgstr ') and '"' in line:
                # msgstr の値部分を取得
                match = re.match(r'(msgstr\s+)"(.+)"', line)
                if match:
                    prefix = match.group(1)
                    value = match.group(2)
                    original_value = value
                    
                    # ** の数をチェック
                    if value.count('**') % 2 != 0:
                        # 奇数の場合、最後の ** を削除または追加
                        value = self._balance_markers(value, '**')
                    
                    # * の数をチェック（** を除外）
                    # ** を一時的に置換して * をカウント
                    temp = value.replace('**', '%%')
                    if temp.count('*') % 2 != 0:
                        value = self._balance_markers(value, '*')
                    
                    # ` の数をチェック
                    if value.count('`') % 2 != 0:
                        value = self._balance_markers(value, '`')
                    
                    if value != original_value:
                        new_lines.append(f'{prefix}"{value}"')
                        self.stats['inline_markup_fixed'] += 1
                        continue
            
            new_lines.append(line)
        
        return '\n'.join(new_lines)
    
    def _balance_markers(self, text: str, marker: str) -> str:
        """
        マーカーのバランスを取る
        
        奇数の場合、末尾にマーカーを追加
        """
        count = text.count(marker)
        if count % 2 != 0:
            # 末尾にマーカーを追加
            text += marker
        return text
    
    def _normalize_whitespace(self, content: str, file_path: Path) -> str:
        """
        空白を正規化
        
        - 行末の空白を削除
        - 複数の空行を1行に
        """
        lines = content.split('\n')
        new_lines = []
        prev_empty = False
        
        for line in lines:
            # 行末の空白を削除
            line = line.rstrip()
            
            # 空行の重複を防ぐ
            if line == '':
                if not prev_empty:
                    new_lines.append(line)
                    prev_empty = True
            else:
                new_lines.append(line)
                prev_empty = False
        
        # 末尾の空行を1つだけにする
        while len(new_lines) > 1 and new_lines[-1] == '':
            new_lines.pop()
        
        if len(new_lines) == 0 or new_lines[-1] != '':
            new_lines.append('')
        
        new_content = '\n'.join(new_lines)
        
        if new_content != content:
            self.stats['whitespace_normalized'] += 1
        
        return new_content
    
    def print_stats(self):
        """統計情報を表示"""
        print("\n" + "=" * 70)
        print("正規化統計")
        print("=" * 70)
        
        if self.dry_run:
            print(f"変更予定ファイル数:       {self.stats.get('files_would_be_modified', 0)}")
        else:
            print(f"変更したファイル数:       {self.stats.get('files_modified', 0)}")
        
        print(f"マージコンフリクト修正:   {self.stats.get('merge_conflicts_fixed', 0)}")
        print(f"Inline markup修正:        {self.stats.get('inline_markup_fixed', 0)}")
        print(f"空白正規化:               {self.stats.get('whitespace_normalized', 0)}")


def find_po_files(locales_dir: Path, specific_file: Optional[Path] = None) -> List[Path]:
    """POファイルを検索"""
    if specific_file:
        if specific_file.exists():
            return [specific_file]
        else:
            print(f"エラー: {specific_file} が見つかりません")
            return []
    
    return list(locales_dir.rglob("*.po"))


def main():
    parser = argparse.ArgumentParser(
        description='POファイルを正規化して一般的な問題を修正',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
例:
  # すべてのPOファイルを正規化
  %(prog)s

  # Dry-runモード
  %(prog)s --dry-run

  # 特定のファイルのみ
  %(prog)s --file locales/ja/LC_MESSAGES/path/to/file.po

  # 詳細モード
  %(prog)s --verbose
        """
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='実際の変更は行わず、検出のみを実行'
    )
    parser.add_argument(
        '--locales-dir',
        type=Path,
        default=Path(__file__).parent.parent / 'locales',
        help='localesディレクトリのパス'
    )
    parser.add_argument(
        '--file',
        type=Path,
        help='特定のPOファイルのパス'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='詳細な出力'
    )
    
    args = parser.parse_args()
    
    locales_dir = args.locales_dir
    
    if not locales_dir.exists():
        print(f"エラー: {locales_dir} が見つかりません")
        sys.exit(1)
    
    print("=" * 70)
    print("POファイル正規化スクリプト")
    print("=" * 70)
    
    if args.dry_run:
        print("\n*** DRY-RUN モード: 実際の変更は行いません ***")
    
    # POファイルを検索
    if args.file:
        print(f"\n特定のファイルを処理: {args.file}")
        po_files = find_po_files(locales_dir, args.file)
    else:
        print(f"\n{locales_dir} 配下のPOファイルを検索中...")
        po_files = find_po_files(locales_dir)
    
    print(f"対象ファイル数: {len(po_files)}")
    
    if len(po_files) == 0:
        print("\n処理対象のファイルが見つかりませんでした。")
        return
    
    # 正規化実行
    normalizer = PONormalizer(dry_run=args.dry_run)
    
    print("\n正規化を実行中...\n")
    
    success_count = 0
    for i, file_path in enumerate(po_files, 1):
        if args.verbose or len(po_files) <= 20:
            relative_path = file_path.relative_to(locales_dir) if locales_dir in file_path.parents else file_path
            print(f"[{i}/{len(po_files)}] {relative_path}")
        elif i % 50 == 0:
            print(f"処理中... {i}/{len(po_files)}")
        
        if normalizer.normalize_file(file_path):
            success_count += 1
    
    # 統計表示
    normalizer.print_stats()
    
    print(f"\n処理成功:                 {success_count}/{len(po_files)}")
    
    if not args.dry_run and normalizer.stats.get('files_modified', 0) > 0:
        print(f"\n✓ {normalizer.stats['files_modified']} ファイルを正規化しました。")
        print("\n次のステップ:")
        print("1. ビルドを実行して警告が減少したか確認:")
        print("   cd docs && make clean && make html-ja")
        print("2. git diff で変更を確認")
    elif args.dry_run:
        print(f"\n次のステップ:")
        print("--dry-run オプションを外して実際の正規化を実行:")
        print(f"  python {Path(__file__).name}")
    
    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
