#!/usr/bin/env python3
"""
構文保護型 PO ファイル翻訳スクリプト

前回の反省:
1. ファイル全体を渡すとRST構文が崩れる（VRAM 8GB）
2. 日本語ではマークアップ前後に空白が必要だがLLMは消しがち

対策:
1. msgid を段落単位（小チャンク）で翻訳
2. RST マークアップを事前抽出・保護
3. 翻訳後に空白を保証して復元
4. 構文に強いモデル（Qwen2.5-Coder）を推奨
"""

import os
import sys
import json
import argparse
import time
from pathlib import Path
from typing import Dict, List, Optional
import re

try:
    import polib
    import ollama
    from tqdm import tqdm
    from colorama import init, Fore, Style
except ImportError as e:
    print(f"Error: Required package not found: {e}")
    print("\nPlease install required packages:")
    print("  pip install polib ollama tqdm colorama")
    sys.exit(1)

# 同じディレクトリのユーティリティをインポート
sys.path.insert(0, str(Path(__file__).parent))
try:
    from rst_markup_extractor import RSTMarkupProtector, split_into_chunks, should_skip_translation
except ImportError:
    print("Error: rst_markup_extractor.py not found in the same directory")
    sys.exit(1)

init(autoreset=True)  # colorama初期化


class SimplifiedChineseDetector:
    """簡体字中国語検出クラス"""
    
    def __init__(self):
        # 簡体字にのみ特有の文字（日本語では絶対に使われない）
        # 日本語でも使う漢字は除外
        self.simplified_only = set(
            '为应该'    # 簡体字「为应该」（日本語では「為」など異なる） ※「了」は日本語でも使う
            '更多的'    # 簡体字「更多的」（日本語では「より多くの」など）
            '这样'      # 簡体字「这样」（日本語では「この様」など）
            '已经'      # 簡体字「已经」（日本語では「既に」など）
            '获发'      # 簡体字「获発」（日本語では「獲得」「発」など）
            '变'        # 簡体字「变」
            '删'        # 簡体字「删」（日本語の「削」とは異なる）
            '检'        # 簡体字「检」（日本語の「検」とは異なる）
            '验'        # 簡体字「验」（日本語の「験」とは異なる）
            '设'        # 簡体字「设」（日本語の「設」とは異なる）
            '这'        # 簡体字「这」
        )
    
    def has_simplified_chinese(self, text: str, threshold: float = 0.3) -> bool:
        """
        簡体字が含まれているか判定（簡体字特有の字のみを検出）
        
        Args:
            text: チェック対象テキスト
            threshold: 未使用（後方互換性のため保持）
        
        Returns:
            簡体字特定字が1個以上含まれている場合True
        """
        if not text:
            return False
        
        # 簡体字特定字が1つ以上あれば簡体字と判定
        simplified_count = sum(1 for c in text if c in self.simplified_only)
        return simplified_count >= 1


detector = SimplifiedChineseDetector()  # グローバルインスタンス


class SmartPOTranslator:
    """構文保護型POファイル翻訳クラス"""
    
    def __init__(self, config_path: str = "data/translate_config.json"):
        """
        Args:
            config_path: 設定ファイルのパス
        """
        self.config = self._load_config(config_path)
        self.protector = RSTMarkupProtector()
        self.glossary = self._load_glossary()
        self.blocked_entries = []  # 簡体字検出でブロックされたエントリを記録
        
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
            "model": "qwen2.5-coder:7b-instruct",  # 構文に強いモデル
            "temperature": 0.1,  # 低温で正確な翻訳
            "max_retries": 3,
            "chunk_size": 400,  # 小さめのチャンク
            "context_window": 2048,
        }
        
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
                default_config.update(user_config)
        
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
    
    def _clean_translation(self, text: str) -> str:
        """
        LLM出力をクリーニング: 余計な説明や改行を削除
        
        Args:
            text: 翻訳テキスト
            
        Returns:
            クリーニングされたテキスト
        """
        # パターン1: "(Translation: ...)" を削除
        text = re.sub(r'\s*\(Translation:.*?\)', '', text, flags=re.DOTALL)
        
        # パターン2: "![...](...)" (Markdownイメージ)を削除
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text, flags=re.DOTALL)
        
        # パターン3: LLMが付け足したリスト形式の説明を削除
        # 「- X軸: 前後」のような行が複数ある場合は削除
        text = re.sub(r'(：|。)\n(- .*?\n)+', r'\1\n', text)
        
        # パターン4: 句読点の後の説明文を削除（複数行の場合）
        # 「〜です。\nこれらの〜」というパターン
        text = re.sub(r'(。)\n([こここれ].*?。)', r'\1', text, flags=re.DOTALL)
        
        # パターン5: 複数の改行を1つに統合
        text = re.sub(r'\n\n+', '\n', text)
        
        # パターン6: 行単位で不要な行を削除
        lines = text.split('\n')
        cleaned_lines = []
        skip_next = False
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            if not stripped:
                continue
            
            # 記号のみの行は削除
            if re.match(r'^[\*\_]+$', stripped):
                continue
            
            # リスト項目「- 」で始まる行を削除
            if stripped.startswith('- '):
                continue
            
            # 「これは」「ここに」などで始まる説明文
            if re.match(r'^(これは|ここに|この|その|あの)', stripped):
                # ただし最初の文字列の場合は許容
                if cleaned_lines and cleaned_lines[-1].endswith(('。', '：')):
                    skip_next = True
                    continue
            
            cleaned_lines.append(line)
        
        text = '\n'.join(cleaned_lines).strip()
        
        return text
    
    def _fix_untranslated_markup(self, text: str, placeholders: Dict[str, str]) -> str:
        """
        マークアップ内容が英語のまま残っていないか確認し、簡単な翻訳を試みる
        
        例: **help new teams** （英語のまま） → **新しいチームを支援する** （翻訳）
        
        Args:
            text: 復元されたテキスト
            placeholders: 元のプレースホルダーと内容のマッピング
        
        Returns:
            修正されたテキスト
        """
        import re
        
        # **english text** パターンを検出
        # 日本語以外（英数字）が**で囲まれている場合
        pattern = r'\*\*([a-zA-Z0-9\s]+)\*\*'
        matches = re.finditer(pattern, text)
        
        for match in matches:
            english_phrase = match.group(1)
            
            # 辞書から翻訳を探す
            jp_translation = self.glossary.get(english_phrase.lower(), None)
            
            if jp_translation:
                # 翻訳があれば置き換え
                text = text.replace(f'** {english_phrase} **', f'** {jp_translation} **', 1)
                text = text.replace(f'**{english_phrase}**', f'**{jp_translation}**', 1)
        
        return text
    
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
        
        # 翻訳プロンプト作成
        prompt = self._create_prompt(protected_text, placeholders, context)
        
        # メインモデルで翻訳試行
        models_to_try = [self.config['model']]
        
        # フォールバックモデルを追加
        if self.config['model'] != 'qwen2.5-coder:7b-instruct':
            models_to_try.append('qwen2.5-coder:7b-instruct')
        
        for model in models_to_try:
            for attempt in range(self.config['max_retries']):
                try:
                    response = ollama.generate(
                        model=model,
                        prompt=prompt,
                        options={
                            'temperature': self.config['temperature'],
                            'num_predict': len(text) * 3,  # 日本語は長くなる
                        }
                    )
                    
                    translated = response['response'].strip()
                    
                    # LLM出力をクリーニング: 改行や説明文を削除
                    translated = self._clean_translation(translated)
                    
                    # 簡体字中国語が出力されていないか確認
                    if detector.has_simplified_chinese(translated):
                        if model != models_to_try[-1]:  # 最後のモデルでない場合
                            print(f"{Fore.YELLOW}[WARNING] Simplified Chinese detected with {model} => trying fallback model")
                            break  # 次のモデルを試す
                        else:
                            print(f"{Fore.YELLOW}[WARNING] Simplified Chinese detected in output (attempt {attempt+1}/{self.config['max_retries']})")
                            if attempt < self.config['max_retries'] - 1:
                                time.sleep(2 ** attempt)  # リトライ
                                continue
                            else:
                                print(f"{Fore.RED}[ERROR] Translation rejected: Simplified Chinese found with all models")
                                # ブロックされたエントリを記録
                                self.blocked_entries.append({
                                    'original': text,
                                    'attempted_translation': translated,
                                    'simplified_chars': [c for c in translated if c in detector.simplified_only],
                                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                                })
                                return None
                    
                    # プレースホルダーを復元（空白も追加）
                    restored = self.protector.restore(translated, placeholders)
                    
                    if model != models_to_try[0]:
                        print(f"{Fore.GREEN}[OK] Successfully translated with fallback model: {model}")
                    
                    return restored
                    
                except Exception as e:
                    if attempt < self.config['max_retries'] - 1:
                        time.sleep(2 ** attempt)  # 指数バックオフ
                        continue
                    else:
                        if model != models_to_try[-1]:
                            print(f"{Fore.YELLOW}[WARNING] {model} failed => trying fallback model")
                            break  # 次のモデルを試す
                        else:
                            print(f"{Fore.RED}[ERROR] Translation failed after {self.config['max_retries']} attempts with all models: {e}")
                            return None
        
        return None
    
    def _create_prompt(self, text: str, placeholders: Dict[str, str], context: str) -> str:
        """翻訳プロンプトを作成"""
        glossary_text = "\n".join([f"- {en} → {ja}" for en, ja in list(self.glossary.items())[:20]])
        
        placeholder_list = "\n".join([f"- {ph}: {orig}" for ph, orig in placeholders.items()])
        
        prompt = f"""You are a technical translator specializing in reStructuredText (RST) documentation for FTC (FIRST Tech Challenge).

Your task: Translate English technical documentation to Japanese. Write ONLY in Japanese.

🚨 ABSOLUTELY CRITICAL:
1. **Write ONLY in Japanese** - Use ONLY Hiragana (ひらがな), Katakana (カタカナ), and Japanese Kanji
2. **DO NOT write any Chinese** - Avoid these characters: 为了应该这处理方式设置获取发送接收检查验证搜索结果查找从事进行
3. **DO NOT use Simplified Chinese characters** - These are WRONG: 为(should be ため), 了(should be た), 应该(should be すべき), 这(should be この)
4. Your output must be grammatically correct Japanese using Japanese grammar and vocabulary
5. Preserve ALL placeholders exactly as shown (e.g., __RST_ROLE_0__, __RST_LITERAL_1__)
6. DO NOT translate placeholder CONTENT - keep markup content exactly as is
7. Use です・ます form (polite, formal Japanese)
8. Keep technical terms in English when specified in glossary
9. Ensure proper spacing around placeholders

GLOSSARY (preserve these terms EXACTLY in English):
{glossary_text}

PLACEHOLDERS (keep EXACTLY as shown - do NOT translate the content inside):
{placeholder_list}

{f"CONTEXT: {context}" if context else ""}

TEXT TO TRANSLATE:
{text}

TRANSLATE TO JAPANESE (ONLY Japanese, NO Chinese characters):"""
        
        return prompt
    
    def translate_po_file(self, po_path: str, output_path: Optional[str] = None):
        """
        POファイル全体を翻訳
        
        Args:
            po_path: 入力POファイルのパス
            output_path: 出力POファイルのパス（Noneの場合は上書き）
        """
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}Translating: {po_path}")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        # POファイルを読み込む
        try:
            po = polib.pofile(po_path)
        except Exception as e:
            print(f"{Fore.RED}Error loading PO file: {e}")
            return
        
        # 翻訳が必要なエントリを抽出
        entries_to_translate = [e for e in po if not e.msgstr and not e.obsolete]
        
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
                chunks = split_into_chunks(msgid, self.config['chunk_size'])
                
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
                    entry.msgstr = '\n\n'.join(translated_chunks)
                    self.stats['translated'] += 1
                
                pbar.update(1)
                
                # 定期保存（50エントリごと）
                if self.stats['translated'] % 50 == 0:
                    po.save(output_path or po_path)
        
        # 最終保存
        po.save(output_path or po_path)
        
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
        """簡体字検出でブロックされたエントリをレポート保存"""
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
        
        print(f"{Fore.YELLOW}⚠️  {len(self.blocked_entries)} entries blocked by Simplified Chinese detection")
        print(f"{Fore.YELLOW}📄 See: {report_file}")
        print(f"{Fore.YELLOW}💡 Check if detection is correct:\n")


def main():
    parser = argparse.ArgumentParser(
        description="Smart PO file translator with RST markup protection"
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
        "--test",
        action="store_true",
        help="Test mode: translate only first 5 entries"
    )
    
    args = parser.parse_args()
    
    # ファイル存在確認
    if not os.path.exists(args.po_file):
        print(f"{Fore.RED}Error: PO file not found: {args.po_file}")
        sys.exit(1)
    
    # 翻訳実行
    translator = SmartPOTranslator(args.config)
    
    if args.test:
        print(f"{Fore.YELLOW}Running in TEST mode (first 5 entries only)\n")
        # テストモード実装は省略
    
    translator.translate_po_file(args.po_file, args.output)


if __name__ == '__main__':
    main()
