#!/usr/bin/env python3
"""
POファイルの正規化と誤訳置換スクリプト

機能：
1. msgstr内の\n（改行文字列）を削除
2. 設定ファイルベースの誤訳を一括置換
3. RSTマークアップ前後のスペース調整（日本語文字とマークアップの間）
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
    """POファイルの正規化と置換を行うクラス"""
    
    def __init__(self, corrections_file: str = 'data/mistranslation_corrections.json'):
        """
        Args:
            corrections_file: 誤訳修正設定ファイルのパス
        """
        self.corrections_file = Path(corrections_file)
        self.corrections = self._load_corrections()
    
    def _load_corrections(self) -> List[Dict]:
        """誤訳修正設定を読み込む"""
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
    
    def _fix_markup_spacing(self, text: str) -> str:
        """
        RSTマークアップ前後のスペースを修正
        
        日本語文字とマークアップの間にスペースを挿入
        """
        if not text:
            return text
        
        # 日本語文字の範囲
        jp_chars = r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]'
        
        # 1. 日本語の後にマークアップ開始: 「文字*markup」→「文字 *markup」
        # **太字**, *強調*
        text = re.sub(rf'({jp_chars})(\*\*)', r'\1 \2', text)
        text = re.sub(rf'({jp_chars})(\*(?!\*))', r'\1 \2', text)
        
        # ``リテラル``
        text = re.sub(rf'({jp_chars})(``)', r'\1 \2', text)
        
        # :role:`text` 形式（:ref:, :doc:, :term: など）
        text = re.sub(rf'({jp_chars})(:\w+:`)', r'\1 \2', text)
        
        # `text`_ (参照)
        text = re.sub(rf'({jp_chars})(`[^`]+`_)', r'\1 \2', text)
        
        # 2. マークアップ終了の直後に日本語: 「markup*文字」→「markup* 文字」
        # **太字**, *強調*
        text = re.sub(rf'(\*\*)({jp_chars})', r'\1 \2', text)
        text = re.sub(rf'(\*(?!\*))({jp_chars})', r'\1 \2', text)
        
        # ``リテラル``
        text = re.sub(rf'(``)({jp_chars})', r'\1 \2', text)
        
        # :role:`text` の終了
        text = re.sub(rf'(`)({jp_chars})', r'\1 \2', text)
        
        # 3. 特殊ケース: *FIRST* のような英語の固有名詞を囲むマークアップ
        # 「です。*FIRST*の」→「です。 *FIRST* の」
        text = re.sub(rf'({jp_chars})(\*[A-Z][A-Za-z0-9]*\*)', r'\1 \2', text)
        text = re.sub(rf'(\*[A-Z][A-Za-z0-9]*\*)({jp_chars})', r'\1 \2', text)
        
        # 4. 既にスペースがある場合は重複スペースを削除
        text = re.sub(r'  +', ' ', text)
        
        # 5. 行頭・行末の余分なスペースを削除
        text = '\n'.join(line.strip() for line in text.split('\n'))
        
        return text
    
    def normalize_po_file(self, po_path: str) -> bool:
        """
        POファイルを正規化・修正
        
        Args:
            po_path: POファイルのパス
        
        Returns:
            成功した場合True
        """
        try:
            po = polib.pofile(po_path)
            modified = False
            
            for entry in po:
                if not entry.msgstr:
                    continue
                
                original_msgstr = entry.msgstr
                
                # 1. \n（改行文字列）を削除
                if '\\n' in entry.msgstr:
                    # msgstr内の\nを空白に置換（文を繋ぎ直す）
                    # ただし、段落分けは保持する必要がある場合は改行を挿入
                    entry.msgstr = entry.msgstr.replace('\\n', ' ')
                    modified = True
                
                # 2. マークアップ前後のスペースを修正
                fixed_spacing = self._fix_markup_spacing(entry.msgstr)
                if fixed_spacing != entry.msgstr:
                    entry.msgstr = fixed_spacing
                    modified = True
                
                # 3. 誤訳を修正
                for correction in self.corrections:
                    mistrans = correction['mistranslation']
                    correct = correction['correct']
                    
                    if mistrans in entry.msgstr:
                        entry.msgstr = entry.msgstr.replace(mistrans, correct)
                        modified = True
                
                # 修正内容をログ（必要に応じて）
                if entry.msgstr != original_msgstr:
                    pass  # 修正されたが、詳細は実行時に表示
            
            if modified:
                po.save(po_path)
                return True
            else:
                return False
        
        except Exception as e:
            print(f"Error processing {po_path}: {e}")
            return False
    
    def normalize_all_po_files(self, po_dir: str = 'locales/ja/LC_MESSAGES') -> Dict:
        """
        すべてのPOファイルを正規化
        
        Args:
            po_dir: POファイルディレクトリ
        
        Returns:
            処理結果の統計
        """
        po_dir = Path(po_dir)
        po_files = list(po_dir.glob('**/*.po'))
        
        print(f"Found {len(po_files)} PO files")
        print()
        
        stats = {
            'total': len(po_files),
            'modified': 0,
            'unchanged': 0,
            'failed': 0
        }
        
        with tqdm(total=len(po_files), desc="Normalizing", unit="file") as pbar:
            for po_file in po_files:
                if self.normalize_po_file(str(po_file)):
                    stats['modified'] += 1
                else:
                    stats['unchanged'] += 1
                pbar.update(1)
        
        print()
        print("=" * 60)
        print("Normalization Complete")
        print("=" * 60)
        print(f"Total files: {stats['total']}")
        print(f"Modified: {stats['modified']}")
        print(f"Unchanged: {stats['unchanged']}")
        print(f"Failed: {stats['failed']}")
        print("=" * 60)
        
        return stats
    
    def normalize_single_file(self, po_path: str) -> None:
        """単一のPOファイルを正規化・修正"""
        if not Path(po_path).exists():
            print(f"Error: {po_path} not found")
            sys.exit(1)
        
        print(f"Normalizing: {po_path}")
        
        if self.normalize_po_file(po_path):
            print(f"✓ Modified and saved")
        else:
            print(f"✓ Already normalized")


def main():
    parser = argparse.ArgumentParser(
        description="POファイルの正規化と誤訳置換"
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='すべてのPOファイルを正規化'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='特定のPOファイルを正規化'
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
        normalizer.normalize_all_po_files()
    elif args.file:
        normalizer.normalize_single_file(args.file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
