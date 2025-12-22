#!/usr/bin/env python3
"""
日本語翻訳が反映されていない箇所を検出するツール

POファイルにmsgstr（日本語翻訳）があるのに、HTMLビルドで反映されていない箇所を検出します。
これはRST構文エラーやSphinxの問題により発生する可能性があります。

使い方:
    python detect_translation_not_reflected.py --check
    python detect_translation_not_reflected.py --report output.json
    python detect_translation_not_reflected.py --html-report report.html
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from bs4 import BeautifulSoup
from typing import Dict, List, Tuple, Set, Optional
import polib
from collections import defaultdict

# プロジェクトルート
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
DOCS_ROOT = PROJECT_ROOT / "docs"

# ディレクトリ
HTML_EN = DOCS_ROOT / "build" / "html"
HTML_JA = DOCS_ROOT / "build" / "html-ja"
SOURCE_DIR = DOCS_ROOT / "source"
LOCALES_DIR = PROJECT_ROOT / "locales" / "ja" / "LC_MESSAGES"

# スキップするHTMLクラス（コードブロック等）
SKIP_CLASSES = {
    'highlight', 'code', 'literal', 'download', 'reference',
    'headerlink', 'viewcode-link', 'pre', 'sig', 'guilabel'
}

# スキップするタグ
SKIP_TAGS = {'script', 'style', 'code', 'pre', 'kbd', 'samp', 'var'}


class TranslationReflectionDetector:
    """翻訳が反映されているかを検出"""
    
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.issues = []
        self.stats = {
            'po_files_checked': 0,
            'translations_checked': 0,
            'not_reflected': 0,
            'reflected': 0,
            'po_entries_with_translation': 0,
        }
        self.po_cache = {}  # POファイルキャッシュ
        
    def log(self, message):
        """ログ出力"""
        if self.verbose:
            print(message)
    
    def load_po_file(self, po_path: Path) -> Optional[polib.POFile]:
        """POファイルを読み込み"""
        if po_path in self.po_cache:
            return self.po_cache[po_path]
        
        if not po_path.exists():
            return None
        
        try:
            po = polib.pofile(str(po_path))
            self.po_cache[po_path] = po
            return po
        except Exception as e:
            self.log(f"❌ POファイル読み込みエラー: {po_path}: {e}")
            return None
    
    def extract_text_from_html(self, soup, skip_technical=True) -> Set[str]:
        """HTMLからテキストを抽出（技術用語などをスキップ）"""
        texts = set()
        
        def extract_from_element(element):
            """再帰的にテキストを抽出"""
            if not hasattr(element, 'name') or element.name is None:
                return
            
            if element.name in SKIP_TAGS:
                return
            
            elem_classes = element.get('class', [])
            if any(cls in SKIP_CLASSES for cls in elem_classes):
                return
            
            # テキストノードを取得
            if element.string and len(element.string.strip()) > 2:
                text = element.string.strip()
                # 技術用語などをスキップする場合
                if not skip_technical or self.is_meaningful_text(text):
                    texts.add(text)
            
            # 子要素を再帰的に処理
            for child in element.children:
                if hasattr(child, 'name') and child.name:
                    extract_from_element(child)
        
        # メインコンテンツから抽出
        main_content = soup.find('div', {'role': 'main'}) or soup.find('main') or soup.body
        if main_content:
            extract_from_element(main_content)
        
        return texts
    
    def is_meaningful_text(self, text: str) -> bool:
        """意味のあるテキスト（日本語を含む）かチェック"""
        if len(text) < 3:
            return False
        
        # 日本語文字が含まれているか
        has_japanese = any('\u3040' <= c <= '\u309F' or  # ひらがな
                          '\u30A0' <= c <= '\u30FF' or  # カタカナ
                          '\u4E00' <= c <= '\u9FFF'     # 漢字
                          for c in text)
        
        return has_japanese
    
    def normalize_text(self, text: str) -> str:
        """テキストを正規化（比較用）"""
        # 空白を正規化
        text = re.sub(r'\s+', ' ', text)
        # 前後の空白を削除
        text = text.strip()
        # 句読点を削除
        text = re.sub(r'[、。，．,\.]', '', text)
        return text
    
    def check_translation_reflected(self, po_path: Path, html_ja_path: Path) -> List[Dict]:
        """POファイルの翻訳がHTMLに反映されているかチェック"""
        issues = []
        
        # POファイルを読み込み
        po = self.load_po_file(po_path)
        if not po:
            return issues
        
        self.stats['po_files_checked'] += 1
        
        # HTMLを読み込み
        if not html_ja_path.exists():
            return issues
        
        try:
            with open(html_ja_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
        except Exception as e:
            self.log(f"❌ HTML読み込みエラー: {html_ja_path}: {e}")
            return issues
        
        # HTMLからテキストを抽出
        html_texts = self.extract_text_from_html(soup)
        html_texts_normalized = {self.normalize_text(t) for t in html_texts}
        
        # POエントリをチェック
        for entry in po:
            # 翻訳が存在するエントリのみチェック
            if not entry.msgstr or entry.obsolete or entry.fuzzy:
                continue
            
            self.stats['translations_checked'] += 1
            self.stats['po_entries_with_translation'] += 1
            
            msgid = entry.msgid
            msgstr = entry.msgstr
            
            # msgstrが意味のあるテキスト（日本語）でない場合はスキップ
            if not self.is_meaningful_text(msgstr):
                continue
            
            # 正規化
            msgstr_normalized = self.normalize_text(msgstr)
            
            # HTMLに反映されているかチェック
            # 部分一致もチェック（長い文の一部が表示されることもあるため）
            is_reflected = False
            
            # 完全一致
            if msgstr in html_texts or msgstr_normalized in html_texts_normalized:
                is_reflected = True
            else:
                # 部分一致（msgstrの50%以上が含まれている）
                msgstr_words = msgstr_normalized.split()
                if len(msgstr_words) > 3:
                    for html_text in html_texts_normalized:
                        # msgstrの主要部分がHTMLに含まれているか
                        match_count = sum(1 for word in msgstr_words if word in html_text)
                        if match_count >= len(msgstr_words) * 0.5:
                            is_reflected = True
                            break  # 早期終了
            
            if is_reflected:
                self.stats['reflected'] += 1
            else:
                self.stats['not_reflected'] += 1
                issues.append({
                    'po_file': str(po_path.relative_to(PROJECT_ROOT)),
                    'html_file': str(html_ja_path.relative_to(HTML_JA)),
                    'msgid': msgid[:100] + '...' if len(msgid) > 100 else msgid,
                    'msgstr': msgstr[:100] + '...' if len(msgstr) > 100 else msgstr,
                    'line': entry.linenum,
                    'type': 'translation_not_reflected',
                })
        
        return issues
    
    def scan_all(self):
        """すべてのPOファイルとHTMLをスキャン"""
        if not LOCALES_DIR.exists():
            print(f"❌ POディレクトリが見つかりません: {LOCALES_DIR}")
            return
        
        if not HTML_JA.exists():
            print(f"❌ 日本語HTMLビルドが見つかりません: {HTML_JA}")
            print("   先に 'cd docs && make html-ja' を実行してください。")
            return
        
        print(f"[INFO] スキャン中...")
        print(f"  POディレクトリ: {LOCALES_DIR}")
        print(f"  HTMLディレクトリ: {HTML_JA}")
        print()
        
        # POファイルを走査
        po_files = list(LOCALES_DIR.rglob("*.po"))
        print(f"[INFO] POファイル数: {len(po_files)}")
        
        for po_path in po_files:
            # 対応するHTMLファイルのパスを推定
            rel_path = po_path.relative_to(LOCALES_DIR)
            # .po -> .html
            html_rel_path = rel_path.with_suffix('.html')
            html_ja_path = HTML_JA / html_rel_path
            
            # HTMLファイルが存在しない場合、親ディレクトリのindex.htmlを試す
            if not html_ja_path.exists():
                html_ja_path = HTML_JA / rel_path.parent / "index.html"
            
            if not html_ja_path.exists():
                continue
            
            file_issues = self.check_translation_reflected(po_path, html_ja_path)
            
            if file_issues:
                self.issues.extend(file_issues)
                print(f"📄 {rel_path}")
                print(f"   対応HTML: {html_ja_path.relative_to(HTML_JA)}")
                print(f"   未反映の翻訳: {len(file_issues)}件")
                for issue in file_issues[:3]:  # 最初の3件のみ表示
                    print(f"   - 行{issue['line']}: {issue['msgstr'][:60]}...")
                if len(file_issues) > 3:
                    print(f"   ... 他{len(file_issues) - 3}件")
                print()
    
    def generate_report(self, output_path: Path):
        """JSON形式のレポートを生成"""
        report = {
            'stats': self.stats,
            'issues': self.issues,
            'issues_by_file': {},
        }
        
        # ファイル別に集計
        for issue in self.issues:
            file = issue['html_file']
            if file not in report['issues_by_file']:
                report['issues_by_file'][file] = []
            report['issues_by_file'][file].append(issue)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"✅ レポート生成完了: {output_path}")
    
    def generate_html_report(self, output_path: Path):
        """HTML形式の詳細レポートを生成"""
        html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>翻訳反映状況レポート</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stat-card h3 {{
            margin: 0 0 10px 0;
            color: #7f8c8d;
            font-size: 14px;
        }}
        .stat-card .value {{
            font-size: 28px;
            font-weight: bold;
            color: #2c3e50;
        }}
        .issue-card {{
            background: white;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 4px solid #e74c3c;
        }}
        .issue-card h3 {{
            margin: 0 0 10px 0;
            color: #2c3e50;
        }}
        .issue-details {{
            font-family: monospace;
            background: #f8f9fa;
            padding: 10px;
            border-radius: 4px;
            margin: 5px 0;
        }}
        .msgid {{
            color: #7f8c8d;
            margin-bottom: 5px;
        }}
        .msgstr {{
            color: #e74c3c;
            font-weight: bold;
        }}
        .tag {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 12px;
            margin-right: 5px;
        }}
        .tag-file {{
            background: #3498db;
            color: white;
        }}
        .tag-line {{
            background: #95a5a6;
            color: white;
        }}
    </style>
</head>
<body>
    <h1>📊 翻訳反映状況レポート</h1>
    
    <div class="stats">
        <div class="stat-card">
            <h3>POファイル数</h3>
            <div class="value">{self.stats['po_files_checked']}</div>
        </div>
        <div class="stat-card">
            <h3>チェックした翻訳</h3>
            <div class="value">{self.stats['translations_checked']}</div>
        </div>
        <div class="stat-card">
            <h3>反映済み</h3>
            <div class="value" style="color: #27ae60;">{self.stats['reflected']}</div>
        </div>
        <div class="stat-card">
            <h3>未反映</h3>
            <div class="value" style="color: #e74c3c;">{self.stats['not_reflected']}</div>
        </div>
    </div>
    
    <h2>🔍 未反映の翻訳（{len(self.issues)}件）</h2>
"""
        
        # ファイル別に問題を表示
        issues_by_file = defaultdict(list)
        for issue in self.issues:
            issues_by_file[issue['html_file']].append(issue)
        
        for html_file, file_issues in sorted(issues_by_file.items()):
            html_content += f"""
    <div class="issue-card">
        <h3>📄 {html_file}</h3>
        <span class="tag tag-file">{file_issues[0]['po_file']}</span>
        <span class="tag tag-line">未反映: {len(file_issues)}件</span>
"""
            for issue in file_issues[:10]:  # 最初の10件のみ表示
                html_content += f"""
        <div class="issue-details">
            <div class="msgid">原文: {issue['msgid']}</div>
            <div class="msgstr">翻訳: {issue['msgstr']}</div>
            <div style="color: #7f8c8d; font-size: 12px; margin-top: 5px;">
                行 {issue['line']}
            </div>
        </div>
"""
            
            if len(file_issues) > 10:
                html_content += f"""
        <p style="color: #7f8c8d; font-style: italic;">... 他{len(file_issues) - 10}件</p>
"""
            
            html_content += """
    </div>
"""
        
        html_content += """
</body>
</html>
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTMLレポート生成完了: {output_path}")
    
    def print_summary(self):
        """サマリーを表示"""
        print("=" * 70)
        print("📊 スキャン結果サマリー")
        print("=" * 70)
        print(f"POファイル数: {self.stats['po_files_checked']}")
        print(f"翻訳エントリ数: {self.stats['po_entries_with_translation']}")
        print(f"チェックした翻訳: {self.stats['translations_checked']}")
        print(f"反映済み: {self.stats['reflected']}")
        print(f"未反映: {self.stats['not_reflected']}")
        print()
        
        if self.stats['not_reflected'] > 0:
            reflection_rate = (self.stats['reflected'] / 
                             (self.stats['reflected'] + self.stats['not_reflected']) * 100)
            print(f"反映率: {reflection_rate:.1f}%")
            print()
            print("⚠️  翻訳が反映されていない箇所が見つかりました。")
            print("   これらはRST構文エラーやSphinxの問題が原因の可能性があります。")
        else:
            print("✅ すべての翻訳が正しく反映されています！")


def main():
    parser = argparse.ArgumentParser(
        description='POファイルの翻訳がHTMLに反映されているかをチェック'
    )
    parser.add_argument('--check', action='store_true',
                       help='チェックのみ実行（結果を表示）')
    parser.add_argument('--report', type=str,
                       help='JSON形式のレポートを指定したファイルに出力')
    parser.add_argument('--html-report', type=str,
                       help='HTML形式のレポートを指定したファイルに出力')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='詳細ログを表示')
    
    args = parser.parse_args()
    
    if not any([args.check, args.report, args.html_report]):
        parser.print_help()
        sys.exit(1)
    
    detector = TranslationReflectionDetector(verbose=args.verbose)
    detector.scan_all()
    detector.print_summary()
    
    if args.report:
        detector.generate_report(Path(args.report))
    
    if args.html_report:
        detector.generate_html_report(Path(args.html_report))


if __name__ == '__main__':
    main()
