#!/usr/bin/env python3
"""
POファイルの構文エラーを高度に修正するスクリプト

機能:
1. エスケープされていない二重引用符の修正
2. 複数行文字列の修正
3. 不正な改行の修正
4. バックアップの自動作成
"""

import re
import sys
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Tuple


class AdvancedPOSyntaxFixer:
    def __init__(self, locales_dir: Path, dry_run: bool = False):
        self.locales_dir = locales_dir
        self.dry_run = dry_run
        self.stats = {
            'files_checked': 0,
            'files_with_errors': 0,
            'files_fixed': 0,
            'quotes_escaped': 0,
            'lines_modified': 0
        }
        
    def backup_file(self, file_path: Path) -> bool:
        """
        ファイルのバックアップを作成
        """
        try:
            backup_path = file_path.with_suffix('.po.bak')
            shutil.copy2(file_path, backup_path)
            return True
        except Exception as e:
            print(f"警告: バックアップ作成失敗 {file_path}: {e}")
            return False
    
    def is_po_syntax_valid(self, file_path: Path) -> Tuple[bool, str]:
        """
        POファイルの構文をチェック
        """
        try:
            import polib
            polib.pofile(str(file_path))
            return True, ""
        except Exception as e:
            return False, str(e)
    
    def fix_unescaped_quotes_in_msgstr(self, content: str) -> Tuple[str, int]:
        """
        msgstr内のエスケープされていない引用符を修正
        
        ロジック:
        1. msgstr "..." の範囲を特定
        2. 範囲内の " を検査
        3. \ でエスケープされていない " を \" に置換
        4. ただし、行末の " は除外
        """
        lines = content.split('\n')
        fixed_lines = []
        in_msgstr = False
        fixes = 0
        
        for i, line in enumerate(lines):
            original_line = line
            
            # msgstr の開始を検出
            if line.strip().startswith('msgstr "'):
                in_msgstr = True
                # msgstr "text" の形式の場合、1行で完結
                if line.strip().endswith('"') and line.count('"') >= 2:
                    # この行内の引用符をチェック
                    line, line_fixes = self._fix_quotes_in_line(line, is_msgstr_start=True)
                    fixes += line_fixes
                    in_msgstr = False
            
            # msgstr の継続行
            elif in_msgstr:
                # 空行または次のエントリ開始で msgstr 終了
                if not line.strip() or line.strip().startswith(('msgid', '#')):
                    in_msgstr = False
                else:
                    # 継続行を修正
                    line, line_fixes = self._fix_quotes_in_line(line, is_msgstr_start=False)
                    fixes += line_fixes
            
            fixed_lines.append(line)
            
            if line != original_line:
                self.stats['lines_modified'] += 1
        
        return '\n'.join(fixed_lines), fixes
    
    def _fix_quotes_in_line(self, line: str, is_msgstr_start: bool) -> Tuple[str, int]:
        """
        1行内のエスケープされていない引用符を修正
        """
        # msgstr "..." の場合
        if is_msgstr_start:
            match = re.match(r'^(\s*msgstr\s+")(.*?)("\s*)$', line)
            if not match:
                return line, 0
            
            prefix = match.group(1)
            content = match.group(2)
            suffix = match.group(3)
            
            fixed_content, fixes = self._escape_quotes(content)
            
            if fixes > 0:
                return prefix + fixed_content + suffix, fixes
            return line, 0
        
        # 継続行 "..." の場合
        else:
            match = re.match(r'^(\s*")(.*?)("\s*)$', line)
            if not match:
                return line, 0
            
            prefix = match.group(1)
            content = match.group(2)
            suffix = match.group(3)
            
            fixed_content, fixes = self._escape_quotes(content)
            
            if fixes > 0:
                return prefix + fixed_content + suffix, fixes
            return line, 0
    
    def _escape_quotes(self, text: str) -> Tuple[str, int]:
        r"""
        テキスト内のエスケープされていない " を \" に変換
        """
        if not text:
            return text, 0
        
        result = []
        fixes = 0
        i = 0
        
        while i < len(text):
            if text[i] == '"':
                # 前の文字が \ かチェック
                if i > 0 and text[i-1] == '\\':
                    # 既にエスケープされている
                    result.append('"')
                else:
                    # エスケープされていない → 修正
                    result.append('\\"')
                    fixes += 1
            else:
                result.append(text[i])
            
            i += 1
        
        return ''.join(result), fixes
    
    def fix_multiline_strings(self, content: str) -> Tuple[str, int]:
        """
        不正な複数行文字列を修正
        """
        # 実装は複雑なので、基本的な修正のみ
        # polib のエラーメッセージに基づいて改善
        
        # 例: 行末に " がない場合
        lines = content.split('\n')
        fixed_lines = []
        fixes = 0
        
        for i, line in enumerate(lines):
            # msgstr や msgid の継続行で " が欠けている場合
            if i > 0 and lines[i-1].strip().startswith(('msgstr', 'msgid', '"')):
                if line.strip() and not line.strip().startswith('"') and not line.strip().startswith('#'):
                    # この行は引用符で囲むべき
                    fixed_lines.append(f'"{line}"')
                    fixes += 1
                    continue
            
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines), fixes
    
    def fix_file(self, file_path: Path) -> bool:
        """
        1つのPOファイルを修正
        """
        try:
            # 構文チェック
            is_valid, error_msg = self.is_po_syntax_valid(file_path)
            
            if is_valid:
                return False  # 修正不要
            
            self.stats['files_with_errors'] += 1
            
            if self.dry_run:
                print(f"[DRY RUN] 修正対象: {file_path.relative_to(self.locales_dir)}")
                print(f"  エラー: {error_msg}")
                return False
            
            # バックアップ
            if not self.backup_file(file_path):
                return False
            
            # ファイルを読み込み
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 修正適用
            content, quote_fixes = self.fix_unescaped_quotes_in_msgstr(content)
            self.stats['quotes_escaped'] += quote_fixes
            
            content, multiline_fixes = self.fix_multiline_strings(content)
            
            # 修正内容を書き込み
            with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(content)
            
            # 再度検証
            is_valid_after, error_after = self.is_po_syntax_valid(file_path)
            
            if is_valid_after:
                self.stats['files_fixed'] += 1
                print(f"[OK] 修正成功: {file_path.relative_to(self.locales_dir)}")
                print(f"  引用符エスケープ: {quote_fixes}件")
                return True
            else:
                print(f"[FAIL] 修正失敗: {file_path.relative_to(self.locales_dir)}")
                print(f"  エラー (修正後): {error_after}")
                # バックアップから復元
                backup_path = file_path.with_suffix('.po.bak')
                if backup_path.exists():
                    shutil.copy2(backup_path, file_path)
                    print(f"  バックアップから復元しました")
                return False
                
        except Exception as e:
            print(f"エラー: {file_path} の処理中に例外: {e}")
            return False
    
    def fix_all_files(self):
        """
        すべてのPOファイルを処理
        """
        po_files = list(self.locales_dir.glob('**/*.po'))
        
        print(f"{'='*70}")
        print(f"PO構文エラー高度修正スクリプト")
        if self.dry_run:
            print("[DRY RUN MODE - 実際の修正は行いません]")
        print(f"{'='*70}")
        print(f"\n処理対象: {len(po_files)} 個のPOファイル\n")
        
        for i, po_file in enumerate(po_files, 1):
            self.stats['files_checked'] += 1
            
            if i % 10 == 0:
                print(f"進行中: {i}/{len(po_files)} ({i*100//len(po_files)}%)", end='\r')
            
            self.fix_file(po_file)
        
        print()  # 改行
    
    def print_stats(self):
        """
        統計情報を表示
        """
        print(f"\n{'='*70}")
        print("修正結果:")
        print(f"{'='*70}")
        print(f"チェックしたファイル:   {self.stats['files_checked']:4} 個")
        print(f"エラーのあったファイル: {self.stats['files_with_errors']:4} 個")
        print(f"修正に成功したファイル: {self.stats['files_fixed']:4} 個")
        print(f"修正に失敗したファイル: {self.stats['files_with_errors'] - self.stats['files_fixed']:4} 個")
        print(f"\nエスケープした引用符:   {self.stats['quotes_escaped']:4} 箇所")
        print(f"修正した行数:           {self.stats['lines_modified']:4} 行")
        print(f"{'='*70}")


def main():
    """
    メイン処理
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='POファイルの構文エラーを高度に修正')
    parser.add_argument('--dry-run', action='store_true', help='実際の修正は行わず、修正対象のみ表示')
    args = parser.parse_args()
    
    script_dir = Path(__file__).parent
    locales_dir = script_dir / 'locales' / 'ja' / 'LC_MESSAGES'
    
    if not locales_dir.exists():
        print(f"エラー: ディレクトリが見つかりません: {locales_dir}")
        sys.exit(1)
    
    fixer = AdvancedPOSyntaxFixer(locales_dir, dry_run=args.dry_run)
    fixer.fix_all_files()
    fixer.print_stats()
    
    if not args.dry_run:
        print("\n次のステップ:")
        print("1. ビルドを実行: cd docs && make clean && make html-ja")
        print("2. 警告数を確認: python summarize_warnings.py")
        print("3. 必要に応じて Phase 2 を実行: python fix_build_warnings.py")


if __name__ == '__main__':
    main()
