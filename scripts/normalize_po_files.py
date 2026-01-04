#!/usr/bin/env python3
"""
POファイルの誤訳置換スクリプト

"""

import json
import polib
import re
from pathlib import Path
from typing import Dict, List
import argparse
import sys
from tqdm import tqdm


class PONormalizer:
    """POファイルの誤訳置換のみを行うクラス"""

    def __init__(self, corrections_file: str = 'data/mistranslation_corrections.json'):
        self.corrections_file = Path(corrections_file)
        self.corrections = self._load_corrections()

    def _load_corrections(self) -> List[Dict]:
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
            po = polib.pofile(po_path)
            modified = False
            for entry in po:
                if not entry.msgstr:
                    continue
                original_msgstr = entry.msgstr
                for correction in self.corrections:
                    mistrans = correction['mistranslation']
                    correct = correction['correct']
                    if mistrans in entry.msgstr:
                        entry.msgstr = entry.msgstr.replace(mistrans, correct)
                        modified = True
                if entry.msgstr != original_msgstr:
                    pass
            if modified:
                po.save(po_path)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error processing {po_path}: {e}")
            return False

    def replace_all_po_files(self, po_dir: str = 'locales/ja/LC_MESSAGES') -> None:
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
