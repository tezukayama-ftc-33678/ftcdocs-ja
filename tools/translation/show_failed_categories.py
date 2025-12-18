#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
失敗分析からカテゴリ別に抽出
"""

import json
import sys
import io

# Windows対応
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def main():
    with open('failed_analysis.json', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    print("=== 断片的な文 (前後の文脈が必要) ===\n")
    fragment_count = 0
    for file_info in data['files']:
        for fail in file_info['failures']:
            if fail.get('is_fragment'):
                fragment_count += 1
                print(f"File: {file_info['file']}")
                print(f"Line: {fail['line']}")
                print(f"English: {fail['msgid']}")
                print(f"Japanese: {fail['msgstr']}")
                print()
    
    print(f"\n=== 長文 (200文字以上、翻訳が難しい) ===\n")
    long_count = 0
    for file_info in data['files']:
        for fail in file_info['failures']:
            if fail.get('is_long_text'):
                long_count += 1
                print(f"File: {file_info['file']}")
                print(f"Line: {fail['line']}")
                print(f"English ({fail['msgid_length']} chars): {fail['msgid'][:150]}...")
                print(f"Japanese: {fail['msgstr'][:150]}...")
                print()
    
    print(f"\n=== 通常の文 (断片でも長文でもない) ===\n")
    normal_count = 0
    for file_info in data['files']:
        for fail in file_info['failures']:
            if not fail.get('is_fragment') and not fail.get('is_long_text') and 'msgid' in fail:
                normal_count += 1
                print(f"File: {file_info['file']}")
                print(f"Line: {fail['line']}")
                print(f"English: {fail['msgid'][:100]}")
                print(f"Japanese: {fail['msgstr'][:100]}")
                print()
    
    print("\n=== 統計 ===")
    print(f"断片的な文: {fragment_count}件")
    print(f"長文: {long_count}件")
    print(f"通常の文: {normal_count}件")
    print(f"エントリ未発見: {data['total_failures'] - fragment_count - long_count - normal_count}件")
    print(f"総計: {data['total_failures']}件")

if __name__ == '__main__':
    main()
