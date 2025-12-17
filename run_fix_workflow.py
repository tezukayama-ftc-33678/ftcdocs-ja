#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統合修正ワークフロー実行スクリプト
- LLM修正 → 品質確認 → ビルド を連続実行
"""

import subprocess
import sys
from pathlib import Path

def run_cmd(cmd: list, cwd=None, description=""):
    """コマンド実行とエラーハンドリング"""
    if description:
        print(f"\n{'='*60}")
        print(f"🚀 {description}")
        print(f"{'='*60}")
    try:
        result = subprocess.run(cmd, cwd=cwd, check=False)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ エラー: {e}")
        return False

def main():
    repo_root = Path(__file__).resolve().parent
    docs_dir = repo_root / "docs"

    print("""
╔════════════════════════════════════════════════════════════╗
║         FTCDocs 日本語翻訳 修正ワークフロー                 ║
║                                                            ║
║  手順:                                                     ║
║  1️⃣  LLM で msgstr を修正（強調・リンク・参照）            ║
║  2️⃣  品質チェック（修正前後を比較）                       ║
║  3️⃣  ビルド（make html + html-ja）                       ║
║  4️⃣  構造比較（html vs html-ja）                         ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    """)

    # ステップ 1: LLM 修正
    success = run_cmd(
        [
            sys.executable,
            "scripts/fix_po_with_llm.py",
            "--issues", "../po_issues.json",
            "--types", "emphasis_mismatch", "inconsistent_ref", "missing_doc_ref",
            "--limit", "1000"
        ],
        cwd=docs_dir,
        description="ステップ 1️⃣ : LLM で PO ファイル修正中..."
    )
    if not success:
        print("⚠️  LLM修正が完了またはスキップされました。続行します...")

    # ステップ 2: 品質チェック
    success = run_cmd(
        [
            sys.executable,
            "scripts/check_and_fix_po.py",
            "--po-dir", "../locales/ja/LC_MESSAGES",
            "--output", "../po_issues_after_fix.json",
            "--verbose"
        ],
        cwd=docs_dir,
        description="ステップ 2️⃣ : 品質チェック（修正後）中..."
    )
    if not success:
        print("⚠️  品質チェックでエラーが発生しました")

    # ステップ 3: ビルド
    print(f"\n{'='*60}")
    print("ステップ 3️⃣ : ビルド中... (clean → html → html-ja)")
    print(f"{'='*60}")
    
    run_cmd(["make", "clean"], cwd=docs_dir)
    run_cmd(["make", "html"], cwd=docs_dir)
    run_cmd(["make", "html-ja"], cwd=docs_dir)

    # ステップ 4: 構造比較
    success = run_cmd(
        [sys.executable, "scripts/compare_build_structures.py"],
        cwd=docs_dir,
        description="ステップ 4️⃣ : ビルド構造比較中..."
    )

    # 完了サマリー
    print(f"""
{'='*60}
✅ ワークフロー完了！

📊 確認事項：
  - po_issues_after_fix.json : 修正後の問題件数
  - build/html-ja/         : 日本語HTML出力
  - build/build_structure_diff.txt : 構造差分

次のステップ：
  1. po_issues_after_fix.json と po_issues.json を比較
  2. 警告が大幅に削減されているか確認
  3. 手動修正が必要な項目は po ファイルを直接編集
{'='*60}
    """)

if __name__ == "__main__":
    main()
