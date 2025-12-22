#!/usr/bin/env python3
"""
HTMLビルドの英語残存部分を検出・修正するスクリプト

使い方:
  python detect_untranslated.py --check    # 検出のみ
  python detect_untranslated.py --fix      # 検出と自動修正
  python detect_untranslated.py --report   # 詳細レポート生成
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from bs4 import BeautifulSoup
from typing import Dict, List, Tuple, Set
import difflib

# プロジェクトルート
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # tools/analysis -> tools -> project root
DOCS_ROOT = PROJECT_ROOT / "docs"

# ビルドディレクトリ
HTML_EN = DOCS_ROOT / "build" / "html"
HTML_JA = DOCS_ROOT / "build" / "html-ja"
SOURCE_DIR = DOCS_ROOT / "source"
LOCALES_DIR = PROJECT_ROOT / "locales" / "ja" / "LC_MESSAGES"

# 除外すべき英語（技術用語、固有名詞など）
ALLOWED_ENGLISH = {
    # 技術用語
    'FIRST', 'Tech', 'Challenge', 'FTC', 'SDK', 'API', 'USB', 'WiFi', 'Bluetooth',
    'Android', 'Studio', 'OnBot', 'Java', 'Blocks', 'OpMode', 'Autonomous', 'TeleOp',
    'REV', 'Control', 'Hub', 'Driver', 'Station', 'Robot', 'Controller',
    'AprilTag', 'CAD', 'Servo', 'Motor', 'Sensor', 'IMU', 'UVC', 'PTZ',
    'Autodesk', 'PTC', 'SolidWorks', 'Fusion', 'Onshape', 'Creo',
    'GitHub', 'Git', 'Codespaces', 'VS', 'Code', 'Jupyter', 'Sphinx',
    # 固有名詞・ブランド
    'Gracious', 'Professionalism', 'Coopertition', 'STEM',
    'REV', 'Robotics', 'Education', 'Competition',
    # プログラミング用語
    'public', 'private', 'class', 'void', 'int', 'double', 'boolean',
    'if', 'else', 'for', 'while', 'switch', 'case', 'return',
    'import', 'package', 'extends', 'implements', 'interface',
    # 単位・記号
    'mm', 'cm', 'kg', 'MHz', 'GHz', 'mA', 'V', 'W',
    'PDF', 'PNG', 'JPG', 'JPEG', 'GIF', 'SVG', 'MP4',
    # その他
    'OK', 'ID', 'URL', 'IP', 'DNS', 'HTTP', 'HTTPS',
}

# スキップするHTMLクラス（コードブロック等）
SKIP_CLASSES = {
    'highlight', 'code', 'literal', 'download', 'reference',
    'headerlink', 'viewcode-link', 'pre', 'sig', 'guilabel'
}

# スキップするタグ
SKIP_TAGS = {'script', 'style', 'code', 'pre', 'kbd', 'samp', 'var'}


class UntranslatedDetector:
    """未翻訳部分の検出器"""
    
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.issues = []
        self.stats = {
            'files_checked': 0,
            'issues_found': 0,
            'files_with_issues': 0,
        }
    
    def log(self, message):
        """ログ出力"""
        if self.verbose:
            print(message)
    
    def is_likely_english(self, text: str) -> bool:
        """テキストが英語である可能性が高いかチェック"""
        if not text or len(text.strip()) < 3:
            return False
        
        text = text.strip()
        
        # 許可された英語用語
        if text in ALLOWED_ENGLISH:
            return False
        
        # 数字のみ
        if text.replace('.', '').replace(',', '').replace(' ', '').isdigit():
            return False
        
        # URLやパス
        if re.match(r'^[\w\-./:\\]+\.(html|rst|py|java|js|css|png|jpg|pdf)$', text, re.IGNORECASE):
            return False
        
        # アルファベットの比率をチェック
        alpha_chars = sum(1 for c in text if c.isalpha())
        ascii_alpha = sum(1 for c in text if c.isascii() and c.isalpha())
        
        if alpha_chars == 0:
            return False
        
        # 80%以上がASCIIアルファベット = 英語の可能性
        if ascii_alpha / alpha_chars > 0.8 and len(text.split()) > 1:
            return True
        
        # 英語の一般的な単語をチェック
        english_words = {
            'the', 'and', 'for', 'are', 'with', 'this', 'that', 'from',
            'have', 'has', 'will', 'can', 'you', 'your', 'all', 'not',
            'but', 'our', 'out', 'what', 'which', 'when', 'where', 'how',
            'more', 'here', 'there', 'about', 'into', 'through', 'during',
        }
        
        words = re.findall(r'\b[a-z]+\b', text.lower())
        if len(words) >= 2:
            english_count = sum(1 for w in words if w in english_words)
            if english_count / len(words) > 0.3:
                return True
        
        return False
    
    def extract_text_from_element(self, element, parent_class='') -> List[Tuple[str, str]]:
        """要素からテキストを抽出（クラス情報付き）"""
        texts = []
        
        # NavigableStringの場合はスキップ
        if not hasattr(element, 'name') or element.name is None:
            return texts
        
        if element.name in SKIP_TAGS:
            return texts
        
        elem_classes = element.get('class', [])
        if any(cls in SKIP_CLASSES for cls in elem_classes):
            return texts
        
        if element.string and element.string.strip():
            text = element.string.strip()
            context = f"{element.name}.{'.'.join(elem_classes)}" if elem_classes else element.name
            texts.append((text, context))
        
        for child in element.children:
            if hasattr(child, 'name') and child.name:
                texts.extend(self.extract_text_from_element(child, parent_class))
        
        return texts
    
    def compare_html_files(self, en_path: Path, ja_path: Path) -> List[Dict]:
        """HTMLファイルを比較して未翻訳部分を検出"""
        issues = []
        
        if not ja_path.exists():
            self.log(f"⚠️  日本語版が存在しません: {ja_path.relative_to(HTML_JA)}")
            return issues
        
        try:
            with open(en_path, 'r', encoding='utf-8') as f:
                en_soup = BeautifulSoup(f, 'html.parser')
            
            with open(ja_path, 'r', encoding='utf-8') as f:
                ja_soup = BeautifulSoup(f, 'html.parser')
        except Exception as e:
            self.log(f"❌ ファイル読み込みエラー: {e}")
            return issues
        
        # メインコンテンツのみを比較
        en_main = en_soup.find('div', {'role': 'main'}) or en_soup.find('main') or en_soup.body
        ja_main = ja_soup.find('div', {'role': 'main'}) or ja_soup.find('main') or ja_soup.body
        
        if not en_main or not ja_main:
            return issues
        
        # テキストを抽出
        ja_texts = self.extract_text_from_element(ja_main)
        
        for text, context in ja_texts:
            if self.is_likely_english(text):
                issues.append({
                    'file': str(ja_path.relative_to(HTML_JA)),
                    'text': text,
                    'context': context,
                    'severity': 'high' if len(text.split()) > 3 else 'medium',
                })
        
        return issues
    
    def scan_directory(self):
        """ディレクトリをスキャン"""
        if not HTML_JA.exists():
            print(f"[ERROR] 日本語HTMLビルドが見つかりません: {HTML_JA}")
            print("   先に 'make html-ja' を実行してください。")
            return
        
        print(f"[INFO] スキャン中: {HTML_JA}")
        print()
        
        html_files = list(HTML_JA.rglob("*.html"))
        
        for ja_path in html_files:
            # ビルド生成ファイルをスキップ
            if any(x in str(ja_path) for x in ['genindex', 'search', '_static', '_sources']):
                continue
            
            self.stats['files_checked'] += 1
            
            # 対応する英語ファイルのパスを構築
            rel_path = ja_path.relative_to(HTML_JA)
            en_path = HTML_EN / rel_path
            
            if not en_path.exists():
                continue
            
            file_issues = self.compare_html_files(en_path, ja_path)
            
            if file_issues:
                self.stats['files_with_issues'] += 1
                self.stats['issues_found'] += len(file_issues)
                self.issues.extend(file_issues)
                
                print(f"📄 {rel_path}")
                for issue in file_issues:
                    severity_icon = "🔴" if issue['severity'] == 'high' else "🟡"
                    print(f"   {severity_icon} {issue['context']}: '{issue['text']}'")
                print()
    
    def generate_report(self, output_file: Path):
        """詳細レポートを生成"""
        report = {
            'timestamp': str(Path.ctime(Path(__file__))),
            'stats': self.stats,
            'issues': self.issues,
            'issues_by_file': {},
        }
        
        # ファイル別に集計
        for issue in self.issues:
            file = issue['file']
            if file not in report['issues_by_file']:
                report['issues_by_file'][file] = []
            report['issues_by_file'][file].append({
                'text': issue['text'],
                'context': issue['context'],
                'severity': issue['severity'],
            })
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"📊 レポート生成: {output_file}")
    
    def print_summary(self):
        """サマリーを表示"""
        print("=" * 70)
        print("📊 スキャン結果サマリー")
        print("=" * 70)
        print(f"チェックしたファイル数: {self.stats['files_checked']}")
        print(f"問題が見つかったファイル: {self.stats['files_with_issues']}")
        print(f"未翻訳の可能性がある箇所: {self.stats['issues_found']}")
        print()
        
        if self.stats['issues_found'] > 0:
            # 頻出する未翻訳テキスト
            text_count = {}
            for issue in self.issues:
                text = issue['text']
                text_count[text] = text_count.get(text, 0) + 1
            
            print("🔝 頻出する未翻訳テキスト (Top 10):")
            for text, count in sorted(text_count.items(), key=lambda x: x[1], reverse=True)[:10]:
                print(f"   {count}回: '{text}'")
            print()


class TranslationFixer:
    """翻訳の自動修正"""
    
    def __init__(self, detector: UntranslatedDetector):
        self.detector = detector
        self.fixes_applied = 0
    
    def find_po_file(self, html_file: str) -> Path:
        """HTMLファイルに対応するPOファイルを探す"""
        # HTMLパスからRSTパスを推測
        html_path = Path(html_file)
        rel_path = html_path.with_suffix('.rst')
        
        # POファイルのパスを構築
        po_path = LOCALES_DIR / rel_path.with_suffix('.po')
        
        if not po_path.exists():
            # ディレクトリ構造が違う場合の代替パス
            parts = list(rel_path.parts)
            if len(parts) > 1:
                po_path = LOCALES_DIR / Path(*parts[:-1]) / (parts[-1].replace('.rst', '.po'))
        
        return po_path if po_path.exists() else None
    
    def suggest_translation(self, english_text: str) -> str:
        """簡単な翻訳候補を提案（辞書ベース）"""
        # 基本的な翻訳辞書
        translations = {
            'New Teams': '新規チーム',
            'Returning Teams': '既存チーム',
            'Programming Resources': 'プログラミングリソース',
            'CAD Resources': 'CADリソース',
            'Competition Manual': '競技マニュアル',
            'Team Management': 'チーム管理',
            'Frequently Asked Questions': 'よくある質問',
            'Downloads': 'ダウンロード',
            'Next': '次へ',
            'Previous': '前へ',
            'Home': 'ホーム',
            'Search': '検索',
            'Table of Contents': '目次',
            'Note': '注記',
            'Warning': '警告',
            'Important': '重要',
            'Tip': 'ヒント',
            'See also': '参照',
        }
        
        return translations.get(english_text, f"[要翻訳: {english_text}]")
    
    def fix_issues(self):
        """問題を自動修正"""
        print("🔧 自動修正を実行中...")
        print()
        
        # ファイル別に問題をグループ化
        issues_by_file = {}
        for issue in self.detector.issues:
            file = issue['file']
            if file not in issues_by_file:
                issues_by_file[file] = []
            issues_by_file[file].append(issue)
        
        for file, issues in issues_by_file.items():
            print(f"📝 修正中: {file}")
            
            po_file = self.find_po_file(file)
            if not po_file:
                print(f"   ⚠️  対応するPOファイルが見つかりません")
                continue
            
            print(f"   📄 POファイル: {po_file.relative_to(PROJECT_ROOT)}")
            
            for issue in issues:
                suggestion = self.suggest_translation(issue['text'])
                print(f"   💡 '{issue['text']}' → '{suggestion}'")
                # 実際の修正はPOファイル編集が必要
            
            print()


def main():
    parser = argparse.ArgumentParser(
        description='HTMLビルドの英語残存部分を検出・修正',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 検出のみ（詳細表示）
  python detect_untranslated.py --check -v
  
  # レポート生成
  python detect_untranslated.py --report -o report.json
  
  # 自動修正（要確認）
  python detect_untranslated.py --fix
        """
    )
    
    parser.add_argument('--check', action='store_true',
                        help='未翻訳部分をチェック（デフォルト）')
    parser.add_argument('--fix', action='store_true',
                        help='自動修正を試みる')
    parser.add_argument('--report', action='store_true',
                        help='詳細レポートを生成')
    parser.add_argument('-o', '--output', default='untranslated_report.json',
                        help='レポート出力ファイル（デフォルト: untranslated_report.json）')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='詳細ログを表示')
    
    args = parser.parse_args()
    
    # デフォルトは --check
    if not (args.check or args.fix or args.report):
        args.check = True
    
    detector = UntranslatedDetector(verbose=args.verbose)
    detector.scan_directory()
    detector.print_summary()
    
    if args.report:
        output_path = Path(args.output)
        detector.generate_report(output_path)
    
    if args.fix:
        fixer = TranslationFixer(detector)
        fixer.fix_issues()
        print(f"✅ 修正候補を提示しました。実際の修正にはPOファイルの編集が必要です。")
    
    # 終了コード
    sys.exit(1 if detector.stats['issues_found'] > 0 else 0)


if __name__ == '__main__':
    main()
