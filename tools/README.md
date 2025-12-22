# FTC Docs 日本語版 - ツール集

このディレクトリには、FTC Docs日本語翻訳プロジェクトで使用するツール群が整理されています。

## 📁 ディレクトリ構成

### `integration/` - LLM統合ツール ⭐ NEW
ローカルLLM（Ollama）を使用した自動修正ツール

**主要スクリプト:**
- **`fix_issues_with_llm.py`** - 翻訳問題をLLMで自動修正
  - `analyze_translation_issues.py`の出力を使用
  - CRITICAL/HIGH問題を段階的に修正
  - ドライラン機能で安全に確認

**使い方:**
```bash
# 問題を分析
python tools/analysis/analyze_translation_issues.py docs/build.log --json issues.json

# LLMで自動修正（10件ずつ推奨）
python tools/integration/fix_issues_with_llm.py issues.json --limit 10 --dry-run
python tools/integration/fix_issues_with_llm.py issues.json --limit 10
```

詳細は [integration/README.md](integration/README.md) を参照してください。

### `translation/` - 翻訳ツール
自動翻訳とLLMベースの翻訳支援ツール

**主要スクリプト:**
- **`batch_translate.py`** - 全POファイル一括自動翻訳（メインツール）
- **`translate_po.py`** - 単一POファイル翻訳
- **`translate_helper.py`** - 翻訳支援ユーティリティ
- **`test_translation_env.py`** - 翻訳環境テスト

**使い方:**
```bash
# 環境テスト
python tools/translation/test_translation_env.py

# 全POファイルを自動翻訳
python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

詳細は [guides/AUTO_TRANSLATE.md](../guides/AUTO_TRANSLATE.md) を参照してください。

### `po-fixing/` - PO修正ツール
POファイルの構文エラーや品質問題を修正するツール

**主要スクリプト:**
- **`fix_po_syntax_advanced.py`** - 高度な構文エラー修正
- **`fix_po_syntax_errors.py`** - 基本的な構文エラー修正
- **`normalize_po_whitespace.py`** - 改行・空白の正規化
- **`normalize_po_files.py`** - POファイル全体の正規化
- **`fix_po_with_llm.py`** - LLMによる自動修正
- **`fix_po_auto.py`** - 自動修正ツール
- **`check_and_fix_po.py`** - PO検証と修正
- **`comprehensive_fix.py`** - 包括的修正（正規化 + LLM修正統合）
- **`run_fix_workflow.py`** - 修正ワークフロー実行

**使い方:**
```bash
# POファイル正規化
python tools/po-fixing/normalize_po_files.py

# 構文エラー修正
python tools/po-fixing/fix_po_syntax_advanced.py

# LLMによる包括的修正
python tools/po-fixing/comprehensive_fix.py
```

詳細は [guides/PO_SYNTAX_FIX_GUIDE.md](../guides/PO_SYNTAX_FIX_GUIDE.md) を参照してください。

### `analysis/` - 分析ツール
ビルド警告や翻訳品質の分析ツール

**主要スクリプト:**
- **`analyze_translation_issues.py`** ⭐ NEW - 翻訳問題の分析と優先順位付け
  - ビルド警告から翻訳が反映されない原因を特定
  - 重大度別、タイプ別の統計
  - HTMLレポート生成で視覚的に問題を把握
- **`detect_translation_not_reflected.py`** ⭐ NEW - POファイルとHTML比較
  - 翻訳があるのに反映されていない箇所を検出
- **`detect_untranslated.py`** - 未翻訳箇所検出（英語のまま残っているテキスト）
- **`analyze_warnings.py`** - ビルド警告の詳細分析
- **`analyze_all_warnings.py`** - 全警告の分類
- **`summarize_warnings.py`** - 警告サマリー生成
- **`validate_build.py`** - ビルド検証
- **`compare_build_structures.py`** - 英語版/日本語版の構造比較
- **`analyze_build_diff_with_llm.py`** - 差分のLLM分析
- **`detect_untranslated_simple.py`** - 未翻訳箇所検出（簡易版）

**使い方:**
```bash
# ビルドして警告を収集
cd docs && make clean && make html-ja 2>&1 | tee build.log

# 翻訳問題を分析（推奨）
python tools/analysis/analyze_translation_issues.py build.log --html-report report.html

# 未翻訳箇所を検出
python tools/analysis/detect_untranslated.py --check

# PO/HTML比較
python tools/analysis/detect_translation_not_reflected.py --check
```

### `archived/` - アーカイブ
過去に使用したが現在は非推奨または不要になったツール

## 🚀 クイックスタート

### 1. 自動翻訳を実行
```bash
python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

### 2. POファイルを修正
```bash
python tools/po-fixing/normalize_po_files.py
```

### 3. ビルド警告を分析
```bash
python tools/analysis/analyze_warnings.py
```

## 📚 関連ドキュメント

- [クイックスタート](../QUICKSTART.md) - プロジェクト全体のクイックスタート
- [自動翻訳ガイド](../guides/AUTO_TRANSLATE.md) - 自動翻訳の詳細手順
- [PO修正ガイド](../guides/PO_SYNTAX_FIX_GUIDE.md) - PO修正の詳細手順
- [エラー修正ガイド](../guides/ERROR_FIX_GUIDE.md) - エラー対処方法

## ⚙️ 前提条件

### 翻訳ツール使用時
- Python 3.8+
- Ollama（ローカルLLM）
- 必要なパッケージ: `ollama`, `polib`, `tqdm`, `colorama`

```bash
pip install ollama polib tqdm colorama
```

### PO修正ツール使用時
- Python 3.8+
- 必要なパッケージ: `polib`, `babel`

```bash
pip install polib babel
```

## 🔧 メンテナンス

### ツールの追加
新しいツールを追加する場合は、適切なカテゴリのディレクトリに配置し、このREADMEを更新してください。

### 非推奨ツールの処理
使用されなくなったツールは `archived/` に移動し、理由をコミットメッセージに記載してください。
