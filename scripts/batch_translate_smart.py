#!/usr/bin/env python3
"""
構文保護型バッチ翻訳スクリプト

複数のPOファイルを順次翻訳し、進捗を保存する。
"""

import os
import sys
import json
import argparse
import time
from pathlib import Path
from typing import List, Dict

try:
    from colorama import init, Fore, Style
except ImportError:
    print("Error: colorama not found. Install with: pip install colorama")
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).parent))
try:
    from translate_po_smart import SmartPOTranslator
except ImportError:
    print("Error: translate_po_smart.py not found")
    sys.exit(1)

init(autoreset=True)


class BatchTranslator:
    """バッチ翻訳管理クラス"""
    
    def __init__(self, po_dir: str, config_path: str, progress_file: str = "data/translation_progress.json"):
        self.po_dir = Path(po_dir)
        self.config_path = config_path
        self.progress_file = progress_file
        self.progress = self._load_progress()
        self.translator = SmartPOTranslator(config_path)
    
    def _load_progress(self) -> Dict:
        """進捗ファイルを読み込む"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # 新形式と旧形式の両対応
                if 'completed_files' in data:
                    return {
                        'completed': data.get('completed_files', []),
                        'failed': data.get('failed_files', []),
                        'skipped': [],
                        'last_updated': data.get('last_updated')
                    }
                return data
        return {
            'completed': [],
            'failed': [],
            'skipped': [],
            'last_updated': None
        }
    
    def _save_progress(self):
        """進捗を保存"""
        self.progress['last_updated'] = time.strftime('%Y-%m-%d %H:%M:%S')
        os.makedirs(os.path.dirname(self.progress_file), exist_ok=True)
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, indent=2, ensure_ascii=False)
    
    def find_po_files(self) -> List[Path]:
        """POファイルを検索"""
        po_files = []
        for po_file in self.po_dir.rglob('*.po'):
            # 既に翻訳済みはスキップ
            if str(po_file.relative_to(self.po_dir)) not in self.progress['completed']:
                po_files.append(po_file)
        
        # 優先順位でソート（ファイルサイズの小さい順）
        po_files.sort(key=lambda p: p.stat().st_size)
        
        return po_files
    
    def translate_all(self, limit: int = None):
        """全POファイルを翻訳"""
        po_files = self.find_po_files()
        
        if not po_files:
            print(f"{Fore.GREEN}✓ All PO files already translated!")
            return
        
        total = min(len(po_files), limit) if limit else len(po_files)
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}Batch Translation Started")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"Total files to translate: {total}")
        print(f"Already completed: {len(self.progress['completed'])}")
        print(f"Failed: {len(self.progress['failed'])}")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        for i, po_file in enumerate(po_files[:total] if limit else po_files, 1):
            rel_path = str(po_file.relative_to(self.po_dir))
            
            print(f"\n{Fore.YELLOW}[{i}/{total}] {rel_path}")
            
            try:
                self.translator.translate_po_file(str(po_file))
                self.progress['completed'].append(rel_path)
                print(f"{Fore.GREEN}✓ Completed: {rel_path}")
                
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}⚠ Interrupted by user")
                self._save_progress()
                sys.exit(0)
                
            except Exception as e:
                print(f"{Fore.RED}✗ Failed: {rel_path}")
                print(f"{Fore.RED}  Error: {e}")
                self.progress['failed'].append({
                    'file': rel_path,
                    'error': str(e),
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                })
            
            # 進捗を保存
            self._save_progress()
            
            # 少し休憩（LLMに優しい）
            time.sleep(1)
        
        # 最終統計
        self._print_final_stats()
    
    def _print_final_stats(self):
        """最終統計を表示"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}Batch Translation Completed")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"Completed:  {Fore.GREEN}{len(self.progress['completed'])} files")
        print(f"Failed:     {Fore.RED}{len(self.progress['failed'])} files")
        
        if self.progress['failed']:
            print(f"\n{Fore.RED}Failed files:")
            failed_items = self.progress['failed'][-5:] if self.progress['failed'] else []
            for item in failed_items:
                # failedが文字列またはディクショナリの両方に対応
                if isinstance(item, dict):
                    print(f"  - {item.get('file', 'unknown')}: {item.get('error', 'unknown error')}")
                else:
                    print(f"  - {item}")
        
        print(f"{Fore.CYAN}{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Batch translate PO files with RST markup protection"
    )
    parser.add_argument(
        "po_dir",
        help="Directory containing PO files"
    )
    parser.add_argument(
        "-c", "--config",
        default="data/translate_config.json",
        help="Config file path"
    )
    parser.add_argument(
        "-p", "--progress",
        default="data/translation_progress.json",
        help="Progress file path"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Limit number of files to translate"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset progress and start from scratch"
    )
    
    args = parser.parse_args()
    
    # ディレクトリ存在確認
    if not os.path.exists(args.po_dir):
        print(f"{Fore.RED}Error: Directory not found: {args.po_dir}")
        sys.exit(1)
    
    # 進捗リセット
    if args.reset:
        if os.path.exists(args.progress):
            os.remove(args.progress)
            print(f"{Fore.YELLOW}Progress reset")
    
    # バッチ翻訳実行
    batch = BatchTranslator(args.po_dir, args.config, args.progress)
    batch.translate_all(args.limit)


if __name__ == '__main__':
    main()
