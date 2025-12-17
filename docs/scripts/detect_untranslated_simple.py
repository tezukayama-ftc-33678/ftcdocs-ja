#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTMLビルドの英語残存部分を検出するスクリプト (Windows対応版)

使い方:
  python detect_untranslated_simple.py
"""

import sys
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Windows環境でUnicode出力を有効化
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# プロジェクトルート
SCRIPT_DIR = Path(__file__).parent
DOCS_ROOT = SCRIPT_DIR.parent
PROJECT_ROOT = DOCS_ROOT.parent

# ビルドディレクトリ
HTML_JA = DOCS_ROOT / "build" / "html-ja"

# スキップするタグとクラス
SKIP_TAGS = {'script', 'style', 'code', 'pre', 'kbd', 'samp', 'var'}
SKIP_CLASSES = {
    'highlight', 'code', 'literal', 'download', 'reference',
    'headerlink', 'viewcode-link', 'pre', 'sig', 'guilabel'
}

# 許可する英語（技術用語など）
ALLOWED_TERMS = {
    'FIRST', 'Tech', 'Challenge', 'FTC', 'SDK', 'API', 'USB', 'WiFi',
    'Android', 'Studio', 'OnBot', 'Java', 'Blocks', 'OpMode',
    'REV', 'Control', 'Hub', 'Driver', 'Station', 'Robot',
    'AprilTag', 'CAD', 'Servo', 'Motor', 'Sensor', 'IMU',
    'GitHub', 'Git', 'PDF', 'PNG', 'JPG', 'HTML', 'CSS',
}


def is_english_text(text):
    """テキストが英語かどうか判定"""
    if not text or len(text.strip()) < 3:
        return False
    
    text = text.strip()
    
    # 許可された用語
    if text in ALLOWED_TERMS:
        return False
    
    # 数字のみ
    if re.match(r'^[\d\s\.,]+$', text):
        return False
    
    # ファイル名やパス
    if re.match(r'^[\w\-./:\\]+\.(html|rst|py|java|js|css|png|jpg|pdf)$', text, re.I):
        return False
    
    # アルファベット比率チェック
    alpha = sum(1 for c in text if c.isalpha())
    if alpha == 0:
        return False
    
    ascii_alpha = sum(1 for c in text if c.isascii() and c.isalpha())
    
    # 80%以上がASCIIアルファベット = 英語の可能性
    if ascii_alpha / alpha > 0.75 and len(text.split()) > 1:
        return True
    
    return False


def extract_texts(element):
    """要素からテキストを抽出"""
    if not hasattr(element, 'name') or element.name is None:
        return []
    
    if element.name in SKIP_TAGS:
        return []
    
    classes = element.get('class', [])
    if any(c in SKIP_CLASSES for c in classes):
        return []
    
    texts = []
    
    # 直接のテキスト
    if element.string and element.string.strip():
        text = element.string.strip()
        if is_english_text(text):
            context = f"{element.name}"
            if classes:
                context += f".{'.'.join(classes)}"
            texts.append((text, context))
    
    # 子要素
    for child in element.children:
        texts.extend(extract_texts(child))
    
    return texts


def scan_html_file(html_path):
    """HTMLファイルをスキャン"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        # メインコンテンツ
        main = soup.find('div', {'role': 'main'}) or soup.find('main') or soup.body
        if not main:
            return []
        
        return extract_texts(main)
    
    except Exception as e:
        print(f"[ERROR] {html_path}: {e}")
        return []


def main():
    if not HTML_JA.exists():
        print("[ERROR] 日本語HTMLビルドが見つかりません")
        print(f"        パス: {HTML_JA}")
        print("        先に 'make html-ja' を実行してください")
        return
    
    print("=" * 70)
    print("日本語HTMLビルド 未翻訳検出ツール")
    print("=" * 70)
    print(f"スキャン対象: {HTML_JA}")
    print()
    
    issues = []
    files_checked = 0
    files_with_issues = 0
    
    # HTMLファイルをスキャン
    html_files = list(HTML_JA.rglob("*.html"))
    
    for html_path in html_files:
        # ビルド生成ファイルをスキップ
        if any(x in str(html_path) for x in ['genindex', 'search', '_static', '_sources']):
            continue
        
        files_checked += 1
        file_texts = scan_html_file(html_path)
        
        if file_texts:
            files_with_issues += 1
            rel_path = html_path.relative_to(HTML_JA)
            
            print(f"\n[FILE] {rel_path}")
            for text, context in file_texts[:10]:  # 最初の10件のみ表示
                severity = "[HIGH]" if len(text.split()) > 3 else "[MED] "
                issues.append({
                    'file': str(rel_path),
                    'text': text,
                    'context': context,
                })
                print(f"  {severity} {context}: '{text[:80]}'")
            
            if len(file_texts) > 10:
                print(f"  ... 他 {len(file_texts) - 10} 件")
    
    # サマリー
    print()
    print("=" * 70)
    print("[STATS] スキャン結果")
    print("=" * 70)
    print(f"チェックしたファイル数: {files_checked}")
    print(f"問題が見つかったファイル数: {files_with_issues}")
    print(f"未翻訳の可能性がある箇所: {len(issues)}")
    
    if issues:
        # 頻出テキスト
        text_count = {}
        for issue in issues:
            text = issue['text'][:50]  # 最初の50文字
            text_count[text] = text_count.get(text, 0) + 1
        
        print()
        print("[TOP] 頻出する未翻訳テキスト (Top 10):")
        for text, count in sorted(text_count.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {count}回: '{text}'")
    
    # JSONレポート出力
    report_path = DOCS_ROOT / "untranslated_report.json"
    report = {
        'stats': {
            'files_checked': files_checked,
            'files_with_issues': files_with_issues,
            'total_issues': len(issues),
        },
        'issues': issues[:100],  # 最初の100件
    }
    
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print()
    print(f"[OK] 詳細レポート: {report_path}")
    print()
    
    return 0 if len(issues) == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
