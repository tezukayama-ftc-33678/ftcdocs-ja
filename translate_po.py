#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PO翻訳自動化スクリプト - Ollama版
VRAM 8GB対応のローカルLLMを使用してPOファイルを自動翻訳
"""

import json
import os
import re
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import ollama
    import polib
    from tqdm import tqdm
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError as e:
    print(f"必要なパッケージがインストールされていません: {e}")
    print("以下のコマンドでインストールしてください:")
    print("pip install ollama polib tqdm colorama")
    exit(1)


class POTranslator:
    """POファイルの自動翻訳クラス"""
    
    def __init__(self, config_path: str = "translate_config.json"):
        """初期化"""
        self.load_config(config_path)
        self.stats = {
            "total": 0,
            "translated": 0,
            "skipped": 0,
            "errors": 0,
            "retries": 0
        }
        
    def load_config(self, config_path: str):
        """設定ファイルの読み込み"""
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        else:
            config = {
                "model": "qwen2.5:7b-instruct-q5_K_M",
                "temperature": 0.3,
                "max_retries": 3,
                "batch_size": 10,
                "skip_translated": True
            }
        
        self.model = config.get("model", "qwen2.5:7b-instruct-q5_K_M")
        self.temperature = config.get("temperature", 0.3)
        self.max_retries = config.get("max_retries", 3)
        self.batch_size = config.get("batch_size", 10)
        self.skip_translated = config.get("skip_translated", True)
        
        print(f"{Fore.GREEN}✓ 設定読み込み完了")
        print(f"  モデル: {self.model}")
        print(f"  温度: {self.temperature}")
        
    def create_translation_prompt(self, msgid: str, context: str = "") -> str:
        """翻訳プロンプトの生成"""
        system_instruction = """あなたはFIRST Tech Challenge (FTC)ドキュメントの専門翻訳者です。
Sphinx POファイルのmsgidを日本語に翻訳してください。

【厳守事項】
1. reStructuredText形式を保持:
   - :doc:`path/to/file` 参照を必ず保持
   - :ref:`label` 参照を必ず保持
   - 外部リンク <URL>__ や `text <URL>`__ を保持
   - **強調** や *イタリック* のマーカーペアを完全に保持

2. Sphinx-Design記法を保持:
   - button-ref, button-link はラベルのみ翻訳、リンク部分は変更しない
   - grid, card のラベルのみ翻訳
   - :opticon:`icon-name` は変更しない

3. 構造保持:
   - 改行位置を保持
   - インデントを保持
   - 空白行を保持

4. 専門用語:
   - FIRST, FTC, REV, goBILDA などの固有名詞は訳さない
   - 技術用語は原文のまま（例: Driver Station, Robot Controller）
   - ボタン名は「〇〇」で囲む（例: 「INIT」「START」）

5. 出力形式:
   - msgstr翻訳文のみを出力
   - 説明や注釈は不要
   - 空のmsgstrを返さない（翻訳不要な場合は原文をそのまま返す）

【翻訳スタイル】
- 丁寧語（です・ます調）
- 自然な日本語
- 技術文書として正確
"""
        
        user_message = f"""以下のmsgidを翻訳してください:

msgid:
\"\"\"
{msgid}
\"\"\"
"""
        
        if context:
            user_message += f"\n# コンテキスト: {context}\n"
        
        return system_instruction + "\n" + user_message
    
    def translate_with_llm(self, msgid: str, context: str = "") -> Optional[str]:
        """LLMで翻訳を実行"""
        if not msgid or not msgid.strip():
            return ""
        
        prompt = self.create_translation_prompt(msgid, context)
        
        for attempt in range(self.max_retries):
            try:
                response = ollama.chat(
                    model=self.model,
                    messages=[
                        {
                            'role': 'user',
                            'content': prompt
                        }
                    ],
                    options={
                        'temperature': self.temperature,
                        'num_predict': 2048
                    }
                )
                
                msgstr = response['message']['content'].strip()
                
                # msgstrのクリーンアップ
                msgstr = self.clean_msgstr(msgstr)
                
                # 基本的な品質チェック
                if self.basic_quality_check(msgid, msgstr):
                    return msgstr
                else:
                    print(f"{Fore.YELLOW}⚠ 品質チェック失敗 (試行 {attempt + 1}/{self.max_retries})")
                    self.stats["retries"] += 1
                    time.sleep(1)
                    
            except Exception as e:
                print(f"{Fore.RED}✗ LLMエラー (試行 {attempt + 1}/{self.max_retries}): {e}")
                self.stats["retries"] += 1
                time.sleep(2)
        
        return None
    
    def clean_msgstr(self, msgstr: str) -> str:
        """msgstrのクリーンアップ"""
        # msgstr開始マーカーの削除
        msgstr = re.sub(r'^msgstr[:\s]*["\']*', '', msgstr, flags=re.MULTILINE)
        
        # 説明文の削除
        lines = msgstr.split('\n')
        cleaned_lines = []
        for line in lines:
            # コメント行をスキップ
            if line.strip().startswith('#'):
                continue
            # 説明的な前置きをスキップ
            if '翻訳:' in line or '訳:' in line:
                continue
            cleaned_lines.append(line)
        
        msgstr = '\n'.join(cleaned_lines).strip()
        
        # 前後の引用符を削除
        msgstr = msgstr.strip('"\'')
        
        # 余分な空行を圧縮（3行以上の連続改行を2行に）
        msgstr = re.sub(r'\n{3,}', '\n\n', msgstr)
        
        # 行末の余分な空白を除去
        msgstr = '\n'.join(line.rstrip() for line in msgstr.splitlines())
        
        return msgstr
    
    def basic_quality_check(self, msgid: str, msgstr: str) -> bool:
        """基本的な品質チェック"""
        if not msgstr or len(msgstr) < 2:
            return False
        
        # :doc: 参照の数が一致するか
        doc_refs_id = len(re.findall(r':doc:`[^`]+`', msgid))
        doc_refs_str = len(re.findall(r':doc:`[^`]+`', msgstr))
        if doc_refs_id != doc_refs_str:
            return False
        
        # :ref: 参照の数が一致するか
        ref_refs_id = len(re.findall(r':ref:`[^`]+`', msgid))
        ref_refs_str = len(re.findall(r':ref:`[^`]+`', msgstr))
        if ref_refs_id != ref_refs_str:
            return False
        
        # ** 強調の数が一致するか（ペアで数える）
        strong_id = msgid.count('**')
        strong_str = msgstr.count('**')
        if strong_id != strong_str:
            return False
        
        # 外部リンクの数が一致するか
        links_id = len(re.findall(r'<https?://[^>]+>__?', msgid))
        links_str = len(re.findall(r'<https?://[^>]+>__?', msgstr))
        if links_id != links_str:
            return False
        
        return True
    
    def translate_po_file(self, po_path: str, output_path: Optional[str] = None) -> bool:
        """POファイル全体を翻訳"""
        try:
            po = polib.pofile(po_path, encoding='utf-8')
            
            if output_path is None:
                output_path = po_path
            
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"{Fore.CYAN}翻訳開始: {os.path.basename(po_path)}")
            print(f"{Fore.CYAN}{'='*60}")
            
            entries_to_translate = []
            for entry in po:
                if entry.msgid and not entry.obsolete:
                    if self.skip_translated and entry.msgstr:
                        self.stats["skipped"] += 1
                    else:
                        entries_to_translate.append(entry)
            
            self.stats["total"] += len(entries_to_translate)
            
            if not entries_to_translate:
                print(f"{Fore.GREEN}✓ 翻訳対象なし（全て翻訳済み）")
                return True
            
            print(f"翻訳対象: {len(entries_to_translate)} エントリ")
            
            # 進捗バーを表示して翻訳
            for entry in tqdm(entries_to_translate, desc="翻訳中", unit="entry"):
                context = entry.msgctxt if hasattr(entry, 'msgctxt') else ""
                
                msgstr = self.translate_with_llm(entry.msgid, context)
                
                if msgstr:
                    entry.msgstr = msgstr
                    self.stats["translated"] += 1
                else:
                    print(f"{Fore.RED}✗ 翻訳失敗: {entry.msgid[:50]}...")
                    self.stats["errors"] += 1
                
                # バッチごとに保存
                if self.stats["translated"] % self.batch_size == 0:
                    po.save(output_path)
            
            # 最終保存
            po.save(output_path)
            
            print(f"{Fore.GREEN}✓ 翻訳完了: {output_path}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}✗ ファイル処理エラー: {e}")
            self.stats["errors"] += 1
            return False
    
    def print_stats(self):
        """統計情報の表示"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}翻訳統計")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"総エントリ数:   {self.stats['total']}")
        print(f"{Fore.GREEN}翻訳成功:       {self.stats['translated']}")
        print(f"{Fore.YELLOW}スキップ:       {self.stats['skipped']}")
        print(f"{Fore.RED}エラー:         {self.stats['errors']}")
        print(f"{Fore.BLUE}リトライ回数:   {self.stats['retries']}")
        
        if self.stats['total'] > 0:
            success_rate = (self.stats['translated'] / self.stats['total']) * 100
            print(f"\n成功率: {success_rate:.1f}%")


def main():
    """メイン関数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Ollamaを使用したPOファイル自動翻訳"
    )
    parser.add_argument(
        "po_file",
        help="翻訳するPOファイルのパス"
    )
    parser.add_argument(
        "-o", "--output",
        help="出力先POファイルのパス（デフォルト: 入力ファイルを上書き）"
    )
    parser.add_argument(
        "-c", "--config",
        default="translate_config.json",
        help="設定ファイルのパス（デフォルト: translate_config.json）"
    )
    parser.add_argument(
        "--no-skip",
        action="store_true",
        help="既に翻訳済みのエントリも再翻訳する"
    )
    
    args = parser.parse_args()
    
    # 翻訳実行
    translator = POTranslator(args.config)
    
    if args.no_skip:
        translator.skip_translated = False
    
    success = translator.translate_po_file(args.po_file, args.output)
    
    # 統計表示
    translator.print_stats()
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
