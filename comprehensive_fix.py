#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
包括的修正ツール：正規化 + LLM修正の統合実行
- ステップ1: 正規化（改行・空白・文末クリーンアップ）
- ステップ2: LLM修正（反復実行：最大3ラウンド）
- ステップ3: 品質チェック（ラウンド毎）
"""

import subprocess
import sys
import json
from pathlib import Path

def run(cmd, cwd=None, desc=""):
    """コマンド実行"""
    if desc:
        print(f"\n{'='*60}\n{desc}\n{'='*60}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode == 0

def get_issue_count(json_file):
    """問題件数を取得"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            issues = json.load(f)
            return len(issues), issues
    except:
        return 0, []

def main():
    repo = Path(__file__).parent
    docs = repo / "docs"
    
    print("\n" + "="*60)
    print("包括的修正ツール：正規化 + LLM 反復修正")
    print("="*60)
    
    # ステップ1: 正規化実行
    run([sys.executable, "scripts/normalize_po_whitespace.py", "--po-dir", "../locales/ja/LC_MESSAGES"],
        cwd=docs, desc="[1/4] ステップ1: 正規化（改行・空白削除）")
    
    # 初回品質チェック
    run([sys.executable, "scripts/check_and_fix_po.py", 
         "--po-dir", "../locales/ja/LC_MESSAGES", 
         "--output", "../po_issues_round0.json", "--verbose"],
        cwd=docs, desc="[QA] 初回品質チェック")
    
    initial_count, _ = get_issue_count(repo / "po_issues_round0.json")
    print(f"\n初回問題数: {initial_count} 件")
    
    # LLM修正を最大3ラウンド
    for round_num in range(1, 4):
        prev_file = repo / f"po_issues_round{round_num-1}.json"
        curr_file = repo / f"po_issues_round{round_num}.json"
        
        prev_count, issues = get_issue_count(prev_file)
        if prev_count == 0:
            print(f"\n[OK] ラウンド{round_num}: 問題ゼロ！修正完了")
            break
        
        print(f"\n{'='*60}")
        print(f"[LLM] ラウンド{round_num}: LLM修正開始（{prev_count} 件）")
        print(f"{'='*60}")
        
        # 各タイプ別に処理
        types_to_fix = []
        type_counts = {}
        for issue in issues:
            t = issue['type']
            type_counts[t] = type_counts.get(t, 0) + 1
        
        # 優先度順（missing_doc_ref → inconsistent_ref → emphasis_mismatch）
        priority_order = ['missing_doc_ref', 'inconsistent_ref', 'emphasis_mismatch']
        for t in priority_order:
            if t in type_counts:
                types_to_fix.append(t)
        
        print(f"対象タイプ: {', '.join(types_to_fix)}")
        for t in types_to_fix:
            print(f"  - {t}: {type_counts[t]} 件")
        
        # LLM修正実行
        limit = min(prev_count, 500)  # 1ラウンド最大500件
        run([sys.executable, "scripts/fix_po_with_llm.py",
             "--issues", str(prev_file),
             "--types"] + types_to_fix + [
             "--limit", str(limit)],
            cwd=docs)
        
        # 正規化を再度実行（LLM出力をクリーンアップ）
        run([sys.executable, "scripts/normalize_po_whitespace.py", "--po-dir", "../locales/ja/LC_MESSAGES"],
            cwd=docs, desc=f"[CLEAN] ラウンド{round_num}後: 正規化")
        
        # 品質チェック
        run([sys.executable, "scripts/check_and_fix_po.py",
             "--po-dir", "../locales/ja/LC_MESSAGES",
             "--output", str(curr_file), "--verbose"],
            cwd=docs, desc=f"[QA] ラウンド{round_num}後: 品質チェック")
        
        curr_count, _ = get_issue_count(curr_file)
        improvement = prev_count - curr_count
        
        print(f"\n{'='*60}")
        print(f"[結果] ラウンド{round_num}")
        print(f"{'='*60}")
        print(f"  修正前: {prev_count:>4} 件")
        print(f"  修正後: {curr_count:>4} 件")
        print(f"  削減数: {improvement:>4} 件 ({100*improvement/prev_count if prev_count > 0 else 0:.1f}%)")
        print(f"{'='*60}")
        
        # 改善が10件未満なら終了
        if improvement < 10:
            print(f"[WARN] 改善が少ないため、ラウンド{round_num}で終了")
            break
    
    # 最終ビルド
    print(f"\n{'='*60}")
    print("[BUILD] 最終ビルド開始")
    print(f"{'='*60}")
    run(["make", "clean"], cwd=docs)
    run(["make", "html"], cwd=docs)
    run(["make", "html-ja"], cwd=docs)
    
    # 構造比較
    run([sys.executable, "scripts/compare_build_structures.py"],
        cwd=docs, desc="[DIFF] 構造比較")
    
    # 最終サマリー
    final_count, _ = get_issue_count(repo / f"po_issues_round{round_num}.json")
    print(f"""
{'='*60}
[完了] 包括的修正完了
{'='*60}
  初回問題数: {initial_count:>4} 件
  最終問題数: {final_count:>4} 件
  総削減数  : {initial_count - final_count:>4} 件 ({100*(initial_count-final_count)/initial_count if initial_count > 0 else 0:.1f}%)
{'='*60}
  出力:
    - docs/build/html-ja/       (日本語HTML)
    - po_issues_round*.json    (各ラウンドの問題)
    - build_structure_diff.txt (構造差分)
{'='*60}
    """)

if __name__ == "__main__":
    main()
