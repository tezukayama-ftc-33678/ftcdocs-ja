#!/usr/bin/env python3
"""
構文保護型 PO ファイル翻訳スクリプト（マルチバックエンド対応版）

Core モジュールと API モジュールを使用した翻訳パイプライン。
RST マークアップを完全に保護し、品質チェックを行いながら翻訳します。

サポートされるバックエンド:
- ollama/local: Ollama ローカルLLM（詳細プロンプト）
- openai/gpt: OpenAI GPT-3.5/4（簡潔プロンプト・トークン最適化）
- anthropic/claude: Anthropic Claude 2/3（簡潔プロンプト・トークン最適化）

トークン最適化（2026-01-14実装）:
- バックエンド別プロンプト: 商用APIには簡潔版、ローカルLLMには詳細版
- 用語集の条件付き送信: テキストに含まれる項目のみ（最大10件）
- コンテキスト削減: 最初の80-100文字のみ使用
- プレースホルダー簡潔化: 存在時のみ短い注記
→ トークン消費量を約60-70%削減（互換性完全維持）

Usage:
    # デフォルトバックエンド（設定ファイルまたはollama）
    python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po
    
    # バックエンドを指定
    python scripts/translate_po_smart.py -b openai locales/ja/LC_MESSAGES/index.po
    python scripts/translate_po_smart.py --backend anthropic locales/ja/LC_MESSAGES/index.po -o output.po
    
    # 利用可能なバックエンド一覧
    python scripts/show_backends.py
"""

import os
import sys
import json
import argparse
import time
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, but that's okay - can use environment variables directly
    pass
from typing import Dict, List, Optional

try:
    from tqdm import tqdm
    from colorama import init, Fore, Style
except ImportError as e:
    print(f"Error: Required package not found: {e}")
    print("\nPlease install required packages:")
    print("  pip install polib ollama tqdm colorama")
    sys.exit(1)

# Core & API モジュールをインポート
sys.path.insert(0, str(Path(__file__).parent))
try:
    from core.po_file_handler import POFileHandler
    from core.rst_protector import RSTProtector, split_into_chunks, should_skip_translation
    from core.quality_checker import QualityChecker
    from api.translator_registry import TranslatorRegistry, create_translator
    from api.translator_base import TranslationError
except ImportError as e:
    print(f"Error: Failed to import core modules: {e}")
    print("Make sure core/ and api/ modules are present in scripts/ directory")
    sys.exit(1)

init(autoreset=True)  # colorama初期化


class SmartPOTranslator:
    """
    構文保護型POファイル翻訳クラス
    
    Core モジュールを使用した翻訳パイプライン。
    RST マークアップを完全に保護し、品質チェックを行いながら翻訳します。
    """
    
    def __init__(self, config_path: str = "data/translate_config.json", backend: Optional[str] = None):
        """
        Args:
            config_path: 設定ファイルのパス
            backend: 翻訳バックエンド名（None=設定ファイルから読み込み）
        """
        self.config = self._load_config(config_path)
        self.po_handler = POFileHandler()
        self.protector = RSTProtector()
        self.quality_checker = QualityChecker()
        
        # バックエンドを選択（引数 > 設定ファイル > デフォルト）
        backend_name = backend or self.config.get('backend', 'openai')
        
        # TranslatorRegistryを使用して翻訳クラスを作成
        try:
            # バックエンド固有のパラメータを準備
            translator_kwargs = {
                'model': self.config.get('model', 'qwen2.5-coder:7b-instruct'),
                'temperature': self.config.get('temperature', 0.1),
                'max_retries': self.config.get('max_retries', 3),
                'glossary': self._load_glossary(),
                'api_key': os.getenv('OPENAI_API_KEY')  # Environment variable only
            }
            
            # fallback_modelはLocalLLMTranslator専用
            if backend_name.lower() in ['ollama', 'local']:
                translator_kwargs['fallback_model'] = self.config.get('fallback_model')
            
            self.translator = create_translator(backend_name, **translator_kwargs)
            print(f"{Fore.GREEN}✓ Using backend: {backend_name}")
        except ValueError as e:
            print(f"{Fore.RED}Error: {e}")
            print(f"\n{Fore.YELLOW}Available backends:")
            for name in TranslatorRegistry.list_backends():
                print(f"  - {name}")
            sys.exit(1)
        
        self.blocked_entries = []  # 品質チェックでブロックされたエントリ
        
        # 統計情報
        self.stats = {
            'total': 0,
            'translated': 0,
            'skipped': 0,
            'failed': 0,
        }
    
    def _load_config(self, config_path: str) -> Dict:
        """設定を読み込む"""
        default_config = {
            "backend": "openai",
            "model": "gpt-4",
            "temperature": 0.1,
            "max_retries": 3,
            "chunk_size": 400,
            "context_window": 2048,
        }
        
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                    default_config.update(user_config)
            except Exception as e:
                print(f"Warning: Failed to load config: {e}")
        
        return default_config
    
    def _load_glossary(self) -> Dict[str, str]:
        """用語集を読み込む"""
        glossary = {}
        glossary_path = Path(__file__).parent.parent / "guides" / "GLOSSARY.md"
        
        if not glossary_path.exists():
            return glossary
        
        try:
            with open(glossary_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # テーブルから用語を抽出（簡易版）
                for line in content.split('\n'):
                    if '|' in line and not line.startswith('|---'):
                        parts = [p.strip() for p in line.split('|')]
                        if len(parts) >= 3 and parts[1] and parts[2]:
                            # 英語 -> 日本語
                            glossary[parts[1]] = parts[2]
        except Exception as e:
            print(f"Warning: Failed to load glossary: {e}")
        
        return glossary
    
    def translate_chunk(self, text: str, context: str = "") -> Optional[str]:
        """
        小さなテキストチャンクを翻訳
        
        Args:
            text: 翻訳するテキスト
            context: コンテキスト情報（前後の文脈）
        
        Returns:
            翻訳されたテキスト、失敗時はNone
        """
        # スキップ判定
        if should_skip_translation(text):
            return text
        
        # マークアップを保護
        protected_text, placeholders = self.protector.protect(text)
        
        # 翻訳
        try:
            translated = self.translator.translate(protected_text, context)
        except TranslationError as e:
            print(f"{Fore.RED}[ERROR] Translation failed: {e.message}")
            return None
        
        # 品質チェック（OpenAIは信頼できるので、空でないかのみ確認）
        is_valid, errors = self.quality_checker.check_translation(text, translated)
        if not is_valid:
            print(f"{Fore.RED}[WARNING] Quality check failed:")
            for error in errors:
                print(f"  - {error}")
            self.blocked_entries.append({
                'original': text,
                'attempted_translation': translated,
                'issues': errors,
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            })
            return None
        
        # プレースホルダーを復元
        restored = self.protector.restore(translated, placeholders)
        
        return restored
    
    def translate_po_file(self, po_path: str, output_path: Optional[str] = None, retranslate: bool = False):
        """
        POファイル全体を翻訳
        
        Args:
            po_path: 入力POファイルのパス
            output_path: 出力POファイルのパス（Noneの場合は上書き）
            retranslate: Trueの場合、既存訳文を破棄して全エントリを再翻訳
        """
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}Translating: {po_path}")
        if retranslate:
            print(f"{Fore.YELLOW}(retranslate mode: discarding existing translations)")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        # POファイルを読み込む
        try:
            po = self.po_handler.load(po_path)
        except Exception as e:
            print(f"{Fore.RED}Error loading PO file: {e}")
            return
        
        # 翻訳が必要なエントリを抽出
        if retranslate:
            # 既存訳文を破棄して全エントリを対象にする
            entries_to_translate = [entry for entry in po if entry.msgid and not entry.obsolete and 'fuzzy' not in entry.flags]
        else:
            # 訳文がないエントリのみ
            entries_to_translate = self.po_handler.get_untranslated_entries(po)
        
        if not entries_to_translate:
            print(f"{Fore.GREEN}✓ All entries already translated")
            return
        
        print(f"Found {len(entries_to_translate)} entries to translate\n")
        
        # 進捗バー
        with tqdm(total=len(entries_to_translate), desc="Translating", unit="entry") as pbar:
            for entry in entries_to_translate:
                self.stats['total'] += 1
                
                # msgid を取得
                msgid = entry.msgid
                if not msgid:
                    self.stats['skipped'] += 1
                    pbar.update(1)
                    continue
                
                # 小さなチャンクに分割
                chunks = split_into_chunks(msgid, self.config.get('chunk_size', 400))
                
                translated_chunks = []
                failed = False
                
                for i, chunk in enumerate(chunks):
                    # コンテキスト（前のチャンク）
                    context = translated_chunks[-1] if translated_chunks else ""
                    
                    # 翻訳
                    translated_chunk = self.translate_chunk(chunk, context)
                    
                    if translated_chunk is None:
                        print(f"{Fore.RED}✗ Failed to translate chunk {i+1}/{len(chunks)}")
                        failed = True
                        break
                    
                    translated_chunks.append(translated_chunk)
                
                if failed:
                    self.stats['failed'] += 1
                else:
                    # チャンクを結合
                    translation = '\n\n'.join(translated_chunks)
                    self.po_handler.set_translation(entry, translation)
                    self.stats['translated'] += 1
                
                pbar.update(1)
                
                # 定期保存（50エントリごと）
                if self.stats['translated'] % 50 == 0:
                    self.po_handler.save(po, output_path or po_path)
        
        # 最終保存
        self.po_handler.save(po, output_path or po_path)
        
        # 統計を表示
        self._print_stats()
    
    def _print_stats(self):
        """統計情報を表示"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}Translation Statistics")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"Total entries:      {self.stats['total']}")
        print(f"Translated:         {Fore.GREEN}{self.stats['translated']}")
        print(f"Skipped:            {Fore.YELLOW}{self.stats['skipped']}")
        print(f"Failed:             {Fore.RED}{self.stats['failed']}")
        success_rate = (self.stats['translated'] / self.stats['total'] * 100) if self.stats['total'] > 0 else 0
        print(f"Success rate:       {success_rate:.1f}%")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        # ブロックされたエントリをレポートに保存
        if self.blocked_entries:
            self._save_blocked_entries_report()
    
    def _save_blocked_entries_report(self):
        """品質チェックでブロックされたエントリをレポート保存"""
        report_file = "data/simplified_chinese_blocked_entries.json"
        
        # 既存データを読み込み
        existing_data = []
        if os.path.exists(report_file):
            try:
                with open(report_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            except:
                existing_data = []
        
        # 新しいエントリを追加
        existing_data.extend(self.blocked_entries)
        
        # ファイルに保存
        os.makedirs(os.path.dirname(report_file), exist_ok=True)
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)
        
        print(f"{Fore.YELLOW}⚠️  {len(self.blocked_entries)} entries blocked by quality check")
        print(f"{Fore.YELLOW}📄 See: {report_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Smart PO file translator with RST markup protection (Multi-backend support)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Supported backends:
  ollama, local     - Ollama local LLM
  openai, gpt       - OpenAI GPT-3.5/4 (requires API key in config)
  anthropic, claude - Anthropic Claude 2/3 (requires API key in config)

Examples:
  # Use default backend (from config or ollama)
  %(prog)s locales/ja/LC_MESSAGES/index.po
  
  # Specify backend
  %(prog)s -b openai locales/ja/LC_MESSAGES/index.po
  %(prog)s --backend anthropic locales/ja/LC_MESSAGES/index.po -o output.po
  
  # List available backends
  python scripts/show_backends.py
        """
    )
    parser.add_argument(
        "po_file",
        help="Path to the PO file to translate"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output PO file path (default: overwrite input)"
    )
    parser.add_argument(
        "-c", "--config",
        default="data/translate_config.json",
        help="Config file path (default: data/translate_config.json)"
    )
    parser.add_argument(
        "-b", "--backend",
        help="Translation backend (ollama|openai|anthropic) - overrides config file"
    )
    
    args = parser.parse_args()
    
    # ファイル存在確認
    if not os.path.exists(args.po_file):
        print(f"{Fore.RED}Error: PO file not found: {args.po_file}")
        sys.exit(1)
    
    # 翻訳実行
    translator = SmartPOTranslator(args.config, backend=args.backend)
    translator.translate_po_file(args.po_file, args.output)


if __name__ == '__main__':
    main()
