#!/bin/bash
# 翻訳未反映問題の検出デモスクリプト
# 
# このスクリプトは、翻訳が反映されていない問題を検出し、
# レポートを生成する一連の流れをデモンストレーションします。

set -e  # エラーで停止

echo "=========================================="
echo "翻訳未反映問題検出デモ"
echo "=========================================="
echo ""

# カラー定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# プロジェクトルートに移動
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

echo -e "${BLUE}ステップ1: 日本語版をビルド${NC}"
echo "======================================"
cd docs

# クリーンビルド
echo "クリーンビルドを実行中..."
make clean > /dev/null 2>&1

# 日本語版ビルド
echo "日本語版ビルド中（数分かかる場合があります）..."
make html-ja > build.log 2>&1

# 警告数を取得
WARNING_COUNT=$(grep "build succeeded" build.log | grep -oP '\d+(?= warnings)' || echo "0")
echo -e "${GREEN}✓ ビルド完了${NC}"
echo -e "  警告数: ${YELLOW}${WARNING_COUNT}件${NC}"
echo ""

cd ..

echo -e "${BLUE}ステップ2: 翻訳問題を分析${NC}"
echo "======================================"
echo "ビルド警告を分析中..."

# ディレクトリ作成
mkdir -p reports

# 分析実行
python tools/analysis/analyze_translation_issues.py \
  docs/build.log \
  --html-report reports/translation_issues.html \
  --json reports/translation_issues.json \
  > reports/analysis_summary.txt 2>&1

echo -e "${GREEN}✓ 分析完了${NC}"
echo ""

# サマリーを表示
echo "【分析結果サマリー】"
grep -A 20 "📊 翻訳問題分析レポート" reports/analysis_summary.txt | head -25
echo ""

echo -e "${BLUE}ステップ3: 未翻訳箇所の検出${NC}"
echo "======================================"
echo "英語のまま残っているテキストを検出中..."

# 未翻訳検出
python tools/analysis/detect_untranslated.py --check > reports/untranslated_summary.txt 2>&1
echo -e "${GREEN}✓ 検出完了${NC}"
echo ""

echo "【未翻訳箇所サマリー】"
tail -10 reports/untranslated_summary.txt
echo ""

echo -e "${BLUE}ステップ4: レポート生成完了${NC}"
echo "======================================"
echo -e "${GREEN}以下のレポートが生成されました:${NC}"
echo ""
echo "  1. reports/translation_issues.html"
echo -e "     ${YELLOW}→ ブラウザで開いて視覚的に問題を確認${NC}"
echo ""
echo "  2. reports/translation_issues.json"
echo -e "     ${YELLOW}→ プログラムで処理可能なJSON形式${NC}"
echo ""
echo "  3. reports/analysis_summary.txt"
echo -e "     ${YELLOW}→ コンソール出力のテキスト版${NC}"
echo ""
echo "  4. reports/untranslated_summary.txt"
echo -e "     ${YELLOW}→ 未翻訳箇所のサマリー${NC}"
echo ""

echo -e "${BLUE}次のステップ${NC}"
echo "======================================"
echo "1. HTMLレポートをブラウザで開く:"
echo -e "   ${GREEN}xdg-open reports/translation_issues.html${NC}"
echo ""
echo "2. 最重要（CRITICAL）問題から修正を開始:"
echo "   - 日本語ラベル参照の問題"
echo "   - 日本語ドキュメントパスの問題"
echo ""
echo "3. 詳細な修正方法は以下のガイドを参照:"
echo -e "   ${GREEN}guides/TRANSLATION_REFLECTION_FIX.md${NC}"
echo ""

# 最重要問題の件数を表示
CRITICAL_COUNT=$(grep -c "🔴 CRITICAL:" reports/analysis_summary.txt || echo "0")
HIGH_COUNT=$(grep -c "🟠 HIGH:" reports/analysis_summary.txt || echo "0")

echo -e "${RED}⚠️  最優先で対処すべき問題:${NC}"
echo -e "   CRITICAL: ${RED}${CRITICAL_COUNT}件${NC}"
echo -e "   HIGH: ${YELLOW}${HIGH_COUNT}件${NC}"
echo ""

echo "=========================================="
echo -e "${GREEN}デモ完了！${NC}"
echo "=========================================="
