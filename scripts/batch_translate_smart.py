#!/usr/bin/env python3
"""
構文保護型バッチ翻訳スクリプト（マルチバックエンド対応）

複数のPOファイルを順次翻訳し、進捗を保存する。
モジュール化されたアーキテクチャを使用。

サポートされるバックエンド:
- ollama/local: Ollama ローカルLLM
- openai/gpt: OpenAI GPT-3.5/4
- anthropic/claude: Anthropic Claude 2/3
"""

import os
import sys
import json
import argparse
import time
from pathlib import Path
from typing import List, Dict, Optional

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, but that's okay - can use environment variables directly
    pass

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
    """バッチ翻訳管理クラス
    
    モジュール化されたSmartPOTranslatorを使用して、
    複数のPOファイルを効率的に翻訳する。
    """
    
    def __init__(
        self,
        po_dir: str,
        config_path: str,
        progress_file: str = "data/translation_progress.json",
        backend: Optional[str] = None
    ):
        """初期化
        
        Args:
            po_dir: POファイルが含まれるディレクトリ
            config_path: 翻訳設定ファイルパス
            progress_file: 進捗ファイルパス
            backend: 翻訳バックエンド名（None=設定ファイルから読み込み）
        """
        self.po_dir = Path(po_dir)
        self.config_path = config_path
        self.progress_file = progress_file
        self.progress = self._load_progress()
        self.translator = SmartPOTranslator(config_path, backend=backend)
    
    def _load_progress(self) -> Dict:
        """進捗ファイルを読み込む
        
        新形式と旧形式の両方に対応している。
        
        Returns:
            進捗情報（completed, failed, skipped, last_updated）
        """
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
    
    def _save_progress(self) -> None:
        """進捗を保存
        
        進捗情報をJSONファイルに保存し、
        最後の更新時刻を記録する。
        """
        self.progress['last_updated'] = time.strftime('%Y-%m-%d %H:%M:%S')
        os.makedirs(os.path.dirname(self.progress_file), exist_ok=True)
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, indent=2, ensure_ascii=False)
    
    def find_po_files(self) -> List[Path]:
        """POファイルを検索
        
        ディレクトリ内のすべてのPOファイルを再帰的に検索し、
        既に翻訳済みのファイルはスキップする。
        ファイルサイズの小さい順に優先度付けする。
        
        Returns:
            未翻訳のPOファイルパスのリスト（ファイルサイズ昇順）
        """
        po_files = []
        for po_file in self.po_dir.rglob('*.po'):
            # 既に翻訳済みはスキップ
            rel_path = str(po_file.relative_to(self.po_dir))
            if rel_path not in self.progress['completed']:
                po_files.append(po_file)
        
        # 優先順位でソート（ファイルサイズの小さい順）
        po_files.sort(key=lambda p: p.stat().st_size)
        
        return po_files
    
    def translate_all(self, limit: Optional[int] = None, retranslate: bool = False) -> None:
        """全POファイルを翻訳
        
        未翻訳のPOファイルを見つけて、順次翻訳する。
        エラーが発生してもファイルサイズ順に続行する。
        
        Args:
            limit: 翻訳する最大ファイル数（Noneの場合は全ファイル）
            retranslate: Trueの場合、既存訳文を破棄して再翻訳
        """
        po_files = self.find_po_files()
        
        if not po_files:
            print(f"{Fore.GREEN}✓ All PO files already translated!")
            return
        
        total = min(len(po_files), limit) if limit else len(po_files)
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}Batch Translation Started")
        if retranslate:
            print(f"{Fore.YELLOW}⚠ RETRANSLATE MODE - existing translations will be discarded")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"Total files to translate: {total}")
        print(f"Already completed: {len(self.progress['completed'])}")
        print(f"Failed: {len(self.progress['failed'])}")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        for i, po_file in enumerate(po_files[:total] if limit else po_files, 1):
            rel_path = str(po_file.relative_to(self.po_dir))
            
            print(f"\n{Fore.YELLOW}[{i}/{total}] {rel_path}")
            
            try:
                self.translator.translate_po_file(str(po_file), retranslate=retranslate)
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
    
    def _print_final_stats(self) -> None:
        """最終統計を表示
        
        翻訳完了時に、完了数、失敗数、失敗ファイル一覧を表示する。
        """
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
    """メイン関数
    
    コマンドライン引数をパースし、バッチ翻訳を実行する。
    """
    parser = argparse.ArgumentParser(
        description="Batch translate PO files with RST markup protection (Multi-backend support)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Supported backends:
  ollama, local     - Ollama local LLM
  openai, gpt       - OpenAI GPT-3.5/4 (requires API key in config)
  anthropic, claude - Anthropic Claude 2/3 (requires API key in config)

Examples:
  # Use default backend (from config or ollama)
  %(prog)s locales/ja/LC_MESSAGES
  
  # Specify backend
  %(prog)s -b openai locales/ja/LC_MESSAGES
  %(prog)s --backend anthropic locales/ja/LC_MESSAGES --limit 10
  
  # List available backends
  python scripts/show_backends.py
        """
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
        "-b", "--backend",
        help="Translation backend (ollama|openai|anthropic) - overrides config file"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset progress and start from scratch"
    )
    parser.add_argument(
        "--retranslate",
        action="store_true",
        help="Discard existing translations and retranslate all entries"
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
    batch = BatchTranslator(args.po_dir, args.config, args.progress, backend=args.backend)
    batch.translate_all(args.limit, retranslate=args.retranslate)


if __name__ == '__main__':
    main()
