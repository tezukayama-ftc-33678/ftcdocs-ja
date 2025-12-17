#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PO自動修正ツール - 未翻訳箇所を自動的に修正

GLOSSARY.mdの用語集と連携して、POファイル内の未翻訳箇所を自動修正します。
"""

import sys
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Windows環境でUnicode出力を有効化
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# プロジェクトルート
SCRIPT_DIR = Path(__file__).parent
DOCS_ROOT = SCRIPT_DIR.parent
PROJECT_ROOT = DOCS_ROOT.parent
LOCALES_DIR = PROJECT_ROOT / "locales" / "ja" / "LC_MESSAGES"
GLOSSARY_PATH = PROJECT_ROOT / "GLOSSARY.md"


class GlossaryLoader:
    """GLOSSARY.mdから用語集を読み込む"""
    
    def __init__(self, glossary_path: Path):
        self.glossary_path = glossary_path
        self.keep_english = set()  # 英語のまま保持する用語
        self.translations = {}      # 翻訳マッピング
        self.load_glossary()
    
    def load_glossary(self):
        """GLOSSARY.mdを解析"""
        if not self.glossary_path.exists():
            print(f"[WARN] GLOSSARY.mdが見つかりません: {self.glossary_path}")
            return
        
        with open(self.glossary_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # すべてのMarkdownテーブルを抽出
        # テーブル形式: | 英語 | 表記/統一訳語 | 備考 |
        table_pattern = r'\|([^|]+)\|([^|]+)\|[^|]*\|'
        
        for match in re.finditer(table_pattern, content):
            col1 = match.group(1).strip()
            col2 = match.group(2).strip()
            
            # ヘッダー行や区切り行をスキップ
            if col1 in ['英語', '---', ''] or col2 in ['表記', '統一訳語', '統一訳語/カタカナ語', '---', '']:
                continue
            
            # col1が英語用語、col2が表記/訳語
            self.translations[col1] = col2
            
            # 英語のまま保持する場合（col1 == col2）
            if col1 == col2:
                self.keep_english.add(col1)
        
        print(f"[INFO] GLOSSARY.md読み込み完了")
        print(f"  - 英語保持用語: {len(self.keep_english)}件")
        print(f"  - 翻訳マッピング: {len(self.translations)}件")
    
    def translate_text(self, text: str) -> str:
        """テキストを用語集に基づいて翻訳"""
        # 英語保持用語の場合はそのまま返す
        if text in self.keep_english:
            return text
        
        result = text
        placeholders = {}
        placeholder_counter = 0
        
        # ステップ1: 英語保持用語を一時的なプレースホルダーに置換
        for keep_term in sorted(self.keep_english, key=len, reverse=True):
            if keep_term in result:
                placeholder = f"__KEEP_{placeholder_counter}__"
                placeholders[placeholder] = keep_term
                result = result.replace(keep_term, placeholder)
                placeholder_counter += 1
        
        # ステップ2: 通常の翻訳を適用（長いフレーズから順に）
        for english, japanese in sorted(
            self.translations.items(),
            key=lambda x: len(x[0]),
            reverse=True
        ):
            # 英語保持用語は翻訳しない
            if english in self.keep_english:
                continue
            
            if english in result:
                result = result.replace(english, japanese)
        
        # ステップ3: プレースホルダーを元に戻す
        for placeholder, keep_term in placeholders.items():
            result = result.replace(placeholder, keep_term)
        
        return result
    
    def should_keep_english(self, text: str) -> bool:
        """テキストが英語のまま保持すべきか判定"""
        # 完全一致チェック
        if text in self.keep_english:
            return True
        
        # 部分一致チェック
        text_lower = text.lower()
        for term in self.keep_english:
            if term.lower() in text_lower:
                return True
        return False


class POEntry:
    """POエントリの表現"""
    def __init__(self, msgid: str, msgstr: str, start_line: int, end_line: int):
        self.msgid = msgid
        self.msgstr = msgstr
        self.start_line = start_line
        self.end_line = end_line


class POAutoFixer:
    """POファイルの自動修正（正規表現ベース）"""
    
    def __init__(self, glossary: GlossaryLoader):
        self.glossary = glossary
        self.stats = {
            'files_checked': 0,
            'files_modified': 0,
            'entries_fixed': 0,
        }
    
    def parse_po_file(self, po_path: Path) -> List[POEntry]:
        """POファイルを正規表現で解析"""
        with open(po_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        entries = []
        # msgid と msgstr のペアを抽出
        pattern = r'msgid\s+"([^"]*(?:"[^"]*")*)"\s+msgstr\s+"([^"]*(?:"[^"]*")*)"'
        
        for match in re.finditer(pattern, content, re.MULTILINE | re.DOTALL):
            msgid = match.group(1)
            msgstr = match.group(2)
            
            # 複数行の場合、結合
            msgid = re.sub(r'"\s*"', '', msgid)
            msgstr = re.sub(r'"\s*"', '', msgstr)
            
            entries.append(POEntry(msgid, msgstr, match.start(), match.end()))
        
        return entries
    
    def is_untranslated(self, entry: POEntry) -> bool:
        """エントリが未翻訳か判定"""
        # msgstrが空
        if not entry.msgstr:
            return True
        
        # msgidと同じ（翻訳されていない）
        if entry.msgstr == entry.msgid:
            return True
        
        # 英語のままの可能性が高い
        if self._is_mostly_english(entry.msgstr) and not self.glossary.should_keep_english(entry.msgstr):
            return True
        
        return False
    
    def _is_mostly_english(self, text: str) -> bool:
        """テキストが主に英語か判定"""
        if not text or len(text) < 10:
            return False
        
        alpha_chars = sum(1 for c in text if c.isalpha())
        if alpha_chars == 0:
            return False
        
        ascii_alpha = sum(1 for c in text if c.isascii() and c.isalpha())
        return (ascii_alpha / alpha_chars) > 0.7
    
    def suggest_translation(self, msgid: str) -> Optional[str]:
        """翻訳候補を提案"""
        # 用語集ベースの翻訳
        translated = self.glossary.translate_text(msgid)
        
        # 変化があれば候補として返す
        if translated != msgid:
            return translated
        
        # 簡単なパターンマッチング
        common_patterns = {
            r'^New Teams?$': '新規チーム',
            r'^Returning Teams?$': '既存チーム',
            r'^Veteran Teams?$': '既存チーム',
            r'^Rookie Teams?$': '新規チーム',
            r'^Programming Resources?$': 'プログラミングリソース',
            r'^CAD Resources?$': 'CADリソース',
            r'^Team Management$': 'チーム管理',
            r'^Competition Manual$': '競技マニュアル',
            r'^Game Manual$': '競技マニュアル',
            r'^Frequently Asked Questions?$': 'よくある質問',
            r'^FAQ$': 'よくある質問',
            r'^Download(s)?$': 'ダウンロード',
            r'^Next$': '次へ',
            r'^Previous$': '前へ',
            r'^Home$': 'ホーム',
            r'^Search$': '検索',
            r'^Table of Contents$': '目次',
            r'^Note$': '注記',
            r'^Warning$': '警告',
            r'^Important$': '重要',
            r'^Tip$': 'ヒント',
            r'^See also$': '参照',
            r'^Required Item\(s\)$': '必要なアイテム',
        }
        
        for pattern, translation in common_patterns.items():
            if re.match(pattern, msgid, re.IGNORECASE):
                return translation
        
        return None
    
    def fix_po_file(self, po_path: Path, dry_run: bool = False) -> int:
        """POファイルを修正"""
        try:
            with open(po_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"[ERROR] {po_path}: {e}")
            return 0
        
        entries = self.parse_po_file(po_path)
        fixed_count = 0
        replacements = []
        
        for entry in entries:
            if self.is_untranslated(entry):
                suggestion = self.suggest_translation(entry.msgid)
                
                if suggestion:
                    # 置換情報を記録
                    replacements.append((entry, suggestion))
                    fixed_count += 1
                    print(f"  [FIX] '{entry.msgid[:60]}' -> '{suggestion[:60]}'")
        
        # 実際にファイルを更新
        if fixed_count > 0 and not dry_run:
            new_content = content
            
            # 後ろから置換（位置がずれないように）
            for entry, suggestion in reversed(replacements):
                # msgstr部分を正規表現で検索
                pattern = re.compile(
                    rf'(msgid\s+"{re.escape(entry.msgid)}"\s+msgstr\s+")([^"]*)(")',
                    re.MULTILINE | re.DOTALL
                )
                new_content = pattern.sub(rf'\1{suggestion}\3', new_content, count=1)
            
            with open(po_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            self.stats['files_modified'] += 1
        
        self.stats['entries_fixed'] += fixed_count
        return fixed_count
    
    def scan_and_fix(self, dry_run: bool = False):
        """全POファイルをスキャンして修正"""
        if not LOCALES_DIR.exists():
            print(f"[ERROR] ロケールディレクトリが見つかりません: {LOCALES_DIR}")
            return
        
        print("=" * 70)
        print("PO自動修正ツール")
        print("=" * 70)
        if dry_run:
            print("[INFO] ドライランモード（実際の修正は行いません）")
        print(f"対象: {LOCALES_DIR}")
        print()
        
        po_files = list(LOCALES_DIR.rglob("*.po"))
        
        for po_path in po_files:
            self.stats['files_checked'] += 1
            
            rel_path = po_path.relative_to(LOCALES_DIR)
            fixed = self.fix_po_file(po_path, dry_run=dry_run)
            
            if fixed > 0:
                print(f"\n[FILE] {rel_path}")
                print(f"  修正候補: {fixed}件")
        
        # サマリー
        print()
        print("=" * 70)
        print("[STATS] 修正結果")
        print("=" * 70)
        print(f"チェックしたファイル数: {self.stats['files_checked']}")
        print(f"修正したファイル数: {self.stats['files_modified']}")
        print(f"修正したエントリ数: {self.stats['entries_fixed']}")
        
        if not dry_run and self.stats['entries_fixed'] > 0:
            print()
            print("[INFO] 修正後は必ず内容を確認してください")
            print("       fuzzyフラグが付与されたエントリは要レビューです")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='POファイルの未翻訳箇所を自動修正',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # ドライラン（修正内容のプレビュー）
  python fix_po_auto.py --dry-run
  
  # 実際に修正を適用
  python fix_po_auto.py
  
  # 特定のファイルのみ修正
  python fix_po_auto.py --file persona_pages/rookie_teams/rookie_teams.po
        """
    )
    
    parser.add_argument('--dry-run', action='store_true',
                        help='修正内容をプレビューのみ（実際の変更は行わない）')
    parser.add_argument('--file', type=str,
                        help='特定のPOファイルのみ処理（相対パス）')
    
    args = parser.parse_args()
    
    # GLOSSARY読み込み
    glossary = GlossaryLoader(GLOSSARY_PATH)
    
    # 自動修正実行
    fixer = POAutoFixer(glossary)
    
    if args.file:
        # 特定ファイルのみ
        po_path = LOCALES_DIR / args.file
        if not po_path.exists():
            print(f"[ERROR] ファイルが見つかりません: {po_path}")
            return 1
        
        print(f"[INFO] 単一ファイル処理: {po_path.relative_to(LOCALES_DIR)}")
        fixer.fix_po_file(po_path, dry_run=args.dry_run)
    else:
        # 全ファイル
        fixer.scan_and_fix(dry_run=args.dry_run)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
