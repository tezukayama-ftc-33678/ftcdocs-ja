#!/usr/bin/env python3
"""
ビルド警告を簡単に集計するスクリプト
"""

import re
from pathlib import Path
from collections import Counter

def main():
    log_path = Path('build_warnings.log')
    
    if not log_path.exists():
        print(f"エラー: {log_path} が見つかりません")
        return
    
    print("="*70)
    print("ビルド警告サマリー")
    print("="*70)
    
    # UTF-16 LE エンコーディングで読み込み (PowerShell Tee-Objectが出力)
    try:
        with open(log_path, 'r', encoding='utf-16-le') as f:
            content = f.read()
    except UnicodeError:
        # UTF-16 LEで読めない場合はUTF-8を試す
        with open(log_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    
    # すべての警告行を抽出
    warning_lines = [line for line in content.split('\n') if 'WARNING:' in line]
    
    print(f"\n総警告数: {len(warning_lines)}")
    
    if len(warning_lines) == 0:
        print("警告が見つかりませんでした。")
        return
    
    # 警告タイプを分類
    inline_strong = len([l for l in warning_lines if 'Inline strong start-string' in l])
    inline_emphasis = len([l for l in warning_lines if 'Inline emphasis start-string' in l])
    inline_literal = len([l for l in warning_lines if 'Inline literal start-string' in l])
    start_of_line = len([l for l in warning_lines if 'Start of line didn\'t match' in l])
    translated_ref = len([l for l in warning_lines if '翻訳されたメッセージの参照が矛盾' in l])
    
    print("\n警告タイプ別:")
    print("-"*70)
    print(f"  Start of line didn't match:      {start_of_line:4} 件 ({start_of_line*100//len(warning_lines):2}%)")
    print(f"  Inline strong (**不一致):        {inline_strong:4} 件 ({inline_strong*100//len(warning_lines):2}%)")
    print(f"  Inline emphasis (*不一致):       {inline_emphasis:4} 件 ({inline_emphasis*100//len(warning_lines):2}%)")
    print(f"  Inline literal (`不一致):        {inline_literal:4} 件 ({inline_literal*100//len(warning_lines):2}%)")
    print(f"  翻訳メッセージ参照矛盾:          {translated_ref:4} 件 ({translated_ref*100//len(warning_lines) if len(warning_lines) > 0 else 0:2}%)")
    print(f"  その他:                          {len(warning_lines)-(start_of_line+inline_strong+inline_emphasis+inline_literal+translated_ref):4} 件")
    
    # ファイル別集計
    file_pattern = re.compile(r'([^:]+\.rst):\d+:<translated>')
    files = []
    for line in warning_lines:
        match = file_pattern.search(line)
        if match:
            files.append(Path(match.group(1)).name)
    
    if files:
        print("\n警告の多いファイルTOP 15:")
        print("-"*70)
        file_counts = Counter(files).most_common(15)
        for filename, count in file_counts:
            print(f"  {filename:50} {count:3} 件")
    
    # 特定の警告パターンのサンプル
    print("\nInline markup警告サンプル:")
    print("-"*70)
    inline_samples = [l for l in warning_lines if 'Inline' in l and '<translated>' in l][:10]
    for sample in inline_samples[:5]:
        # ファイル名と行番号を抽出
        match = re.search(r'([^\\/:]+\.rst):(\d+):', sample)
        if match:
            print(f"  {match.group(1)}:{match.group(2)}")
    
    print("\n" + "="*70)
    print("修正アプローチ:")
    print("="*70)
    print("""
1. Inline markup修正 (**, *, ` の不一致):
   - fix_build_warnings.py を実行
   - 自動で ** や * の閉じ忘れを修正

2. "Start of line didn't match" 修正:
   - これはPOファイルの翻訳文に問題がある
   - check_and_fix_po.py で検出される問題と関連
   - LLMで手動修正が必要な場合が多い

3. 参照矛盾:
   - normalize_po_whitespace.py で修正可能
    """)

if __name__ == '__main__':
    main()
