#!/usr/bin/env python3
"""
POファイル正規化スクリプト

msgstr内の誤訳を一括置換します。
使用可能な correction パターンは data/mistranslation_corrections.json で定義します。

Usage:
    python scripts/normalize_po_files.py --all                          # すべてのPOファイル
    python scripts/normalize_po_files.py --file locales/ja/LC_MESSAGES/index.po
"""

import json
import sys
from pathlib import Path
from typing import Dict, List
import argparse
from tqdm import tqdm

# Import from core modules
from core.po_file_handler import POFileHandler


class PONormalizer:
    """
    POファイルの誤訳置換を行うクラス。
    
    core/po_file_handler.py を使用して安全な PO ファイル処理を実現します。
    msgstr のみを変更し、msgid は決して変更しません。
    """

    def __init__(self, corrections_file: str = 'data/mistranslation_corrections.json'):
        """
        Args:
            corrections_file: 誤訳修正設定ファイルのパス
        """
        self.corrections_file = Path(corrections_file)
        self.corrections = self._load_corrections()
        self.handler = POFileHandler()

    def _load_corrections(self) -> List[Dict]:
        """誤訳修正パターンを読み込む"""
        if not self.corrections_file.exists():
            print(f"Warning: {self.corrections_file} not found")
            return []
        try:
            with open(self.corrections_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data.get('corrections', [])
        except Exception as e:
            print(f"Error loading corrections: {e}")
            return []

    def replace_mistranslations(self, po_path: str) -> bool:
        """
        POファイルのmsgstr内の誤訳を一括置換
        
        Args:
            po_path: POファイルのパス
        
        Returns:
            変更があった場合True
        """
        try:
            # PO ファイルを読み込む（安全な I/O）
            po = self.handler.load(po_path)
            modified = False
            
            for entry in po:
                # msgstr が空の場合はスキップ
                if not entry.msgstr:
                    continue
                
                original_msgstr = entry.msgstr
                
                # 各修正パターンを適用
                for correction in self.corrections:
                    mistrans = correction['mistranslation']
                    correct = correction['correct']
                    if mistrans in entry.msgstr:
                        entry.msgstr = entry.msgstr.replace(mistrans, correct)
                        modified = True
            
            # 変更があった場合のみ保存
            if modified:
                self.handler.save(po, po_path)
                return True
            else:
                return False
                
        except Exception as e:
            print(f"Error processing {po_path}: {e}")
            return False

    def replace_all_po_files(self, po_dir: str = 'locales/ja/LC_MESSAGES') -> None:
        """すべての PO ファイル内の誤訳を置換"""
        po_dir = Path(po_dir)
        po_files = list(po_dir.glob('**/*.po'))
        print(f"Found {len(po_files)} PO files")
        
        modified = 0
        unchanged = 0
        
        for po_file in tqdm(po_files, desc="Replacing", unit="file"):
            if self.replace_mistranslations(str(po_file)):
                modified += 1
            else:
                unchanged += 1
        
        print()
        print(f"Modified: {modified}")
        print(f"Unchanged: {unchanged}")

    def replace_single_file(self, po_path: str) -> None:
        """単一の PO ファイル内の誤訳を置換"""
        if not Path(po_path).exists():
            print(f"Error: {po_path} not found")
            sys.exit(1)
        
        print(f"Replacing mistranslations in: {po_path}")
        if self.replace_mistranslations(po_path):
            print(f"✓ Modified and saved")
        else:
            print(f"✓ No changes needed")




def main():
    parser = argparse.ArgumentParser(
        description="POファイルの誤訳置換"
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='すべてのPOファイルの誤訳を置換'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='特定のPOファイルの誤訳を置換'
    )
    parser.add_argument(
        '--corrections',
        type=str,
        default='data/mistranslation_corrections.json',
        help='誤訳修正設定ファイル（デフォルト: data/mistranslation_corrections.json）'
    )

    args = parser.parse_args()

    normalizer = PONormalizer(args.corrections)

    if args.all:
        normalizer.replace_all_po_files()
    elif args.file:
        normalizer.replace_single_file(args.file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
