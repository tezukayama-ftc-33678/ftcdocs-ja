#!/usr/bin/env python3
"""
POファイルの:ref:参照の不整合を修正するスクリプト

原文に:ref:参照があるのに翻訳で削除されているケースを検出し、
原文の参照構造を維持しつつ日本語部分を保持します。
"""

import polib
import re
from pathlib import Path
from typing import List, Tuple, Optional
from tqdm import tqdm
from colorama import init, Fore, Style

init(autoreset=True)


class RefInconsistencyFixer:
    """POファイルの:ref:参照不整合を修正"""
    
    def __init__(self, locales_dir: str = "locales/ja/LC_MESSAGES"):
        self.locales_dir = Path(locales_dir)
        self.stats = {
            'total_files': 0,
            'modified': 0,
            'unchanged': 0,
            'failed': 0,
            'refs_restored': 0
        }
    
    def find_refs(self, text: str) -> List[Tuple[str, str, str]]:
        """
        テキストから:ref:参照を抽出
        
        Returns:
            List[(全体, 表示テキスト, パス)] のリスト
        """
        # 改行を削除してから処理（POファイルでは\nが改行として含まれる）
        text_normalized = text.replace('\n', ' ')
        
        # :ref:`表示テキスト<パス:アンカー>` のパターン
        pattern = r':ref:`([^<>`]+)<([^<>`]+)>`'
        
        # (全体, 表示テキスト, パス) を返す
        refs = []
        for match in re.finditer(pattern, text_normalized):
            full = match.group(0)
            display = match.group(1).strip()
            path = match.group(2).strip()
            refs.append((full, display, path))
        
        return refs
    
    def restore_refs(self, msgid: str, msgstr: str) -> Optional[str]:
        """
        msgidの:ref:参照をmsgstrに復元
        
        Args:
            msgid: 原文
            msgstr: 翻訳文
        
        Returns:
            修正後の翻訳文、または変更なしの場合None
        """
        if not msgstr:
            return None
        
        msgid_refs = self.find_refs(msgid)
        msgstr_refs = self.find_refs(msgstr)
        
        # 参照数が同じなら問題なし
        if len(msgid_refs) == len(msgstr_refs):
            return None
        
        # msgidに参照があるのにmsgstrにない場合
        if len(msgid_refs) > len(msgstr_refs):
            # msgstrの既存参照のパスを収集
            existing_paths = {path for _, _, path in msgstr_refs}
            
            # 欠けている参照を追加
            new_msgstr = msgstr
            for full_ref, display, path in msgid_refs:
                if path not in existing_paths:
                    # 原文の参照をそのまま追加（表示テキストも英語のまま）
                    # 翻訳文の末尾に追加
                    if not new_msgstr.endswith(' '):
                        new_msgstr += ' '
                    new_msgstr += full_ref
                    self.stats['refs_restored'] += 1
            
            return new_msgstr if new_msgstr != msgstr else None
        
        return None
    
    def fix_po_file(self, po_path: Path) -> bool:
        """
        POファイルの:ref:参照不整合を修正
        
        Args:
            po_path: POファイルのパス
        
        Returns:
            成功した場合True
        """
        try:
            po = polib.pofile(str(po_path))
            modified = False
            
            for entry in po:
                if not entry.msgstr:
                    continue
                
                # :ref:参照の不整合を修正
                fixed_msgstr = self.restore_refs(entry.msgid, entry.msgstr)
                if fixed_msgstr:
                    entry.msgstr = fixed_msgstr
                    modified = True
            
            if modified:
                po.save()
                self.stats['modified'] += 1
                return True
            else:
                self.stats['unchanged'] += 1
                return False
        
        except Exception as e:
            print(f"{Fore.RED}Error processing {po_path}: {e}")
            self.stats['failed'] += 1
            return False
    
    def fix_all(self):
        """全POファイルを修正"""
        po_files = list(self.locales_dir.rglob("*.po"))
        self.stats['total_files'] = len(po_files)
        
        print(f"Found {len(po_files)} PO files\n")
        
        for po_file in tqdm(po_files, desc="Fixing refs", unit="file"):
            self.fix_po_file(po_file)
        
        self.print_summary()
    
    def print_summary(self):
        """処理結果のサマリを表示"""
        print("\n" + "=" * 60)
        print("Ref Inconsistency Fix Complete")
        print("=" * 60)
        print(f"Total files: {self.stats['total_files']}")
        print(f"{Fore.GREEN}Modified: {self.stats['modified']}")
        print(f"Unchanged: {self.stats['unchanged']}")
        print(f"{Fore.RED}Failed: {self.stats['failed']}")
        print(f"{Fore.CYAN}Refs restored: {self.stats['refs_restored']}")
        print("=" * 60)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Fix :ref: reference inconsistencies in PO files'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Process all PO files'
    )
    parser.add_argument(
        'files',
        nargs='*',
        help='Specific PO files to process'
    )
    
    args = parser.parse_args()
    
    fixer = RefInconsistencyFixer()
    
    if args.all:
        fixer.fix_all()
    elif args.files:
        for file_path in args.files:
            po_path = Path(file_path)
            if po_path.exists():
                fixer.fix_po_file(po_path)
            else:
                print(f"{Fore.RED}File not found: {file_path}")
        fixer.print_summary()
    else:
        print("Please specify --all or provide file paths")
        parser.print_help()


if __name__ == '__main__':
    main()
