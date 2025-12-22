# LLM統合ツール

このディレクトリには、ローカルLLM（Ollama）を使用して翻訳問題を自動修正するための統合ツールが含まれています。

## 📦 ツール

### fix_issues_with_llm.py ⭐

`analyze_translation_issues.py`の出力を使用して、検出された翻訳問題をローカルLLMで自動修正します。

## 🚀 使い方

### ステップ1: 事前準備

```bash
# Ollamaをインストール（まだの場合）
# https://ollama.ai/

# 推奨モデルをダウンロード
ollama pull qwen2.5:7b-instruct-q5_K_M

# 必要なPythonパッケージをインストール
pip install ollama polib
```

### ステップ2: 問題を分析

```bash
# ビルドして警告を収集
cd docs
make clean && make html-ja 2>&1 | tee build.log

# 問題を分析してJSON出力
cd ..
python tools/analysis/analyze_translation_issues.py docs/build.log --json issues.json
```

### ステップ3: LLMで自動修正

```bash
# まずドライランで確認（推奨）
python tools/integration/fix_issues_with_llm.py issues.json --limit 10 --dry-run

# 実際に10件修正
python tools/integration/fix_issues_with_llm.py issues.json --limit 10

# ビルドして結果を確認
cd docs && make clean && make html-ja 2>&1 | grep "build succeeded"
```

### ステップ4: 結果確認とコミット

```bash
# HTMLで表示を確認
cd docs/build/html-ja
python -m http.server 8000
# ブラウザで http://localhost:8000 を開く

# 警告が減っていればコミット
cd ../../../
git add locales/ja/LC_MESSAGES/*.po
git commit -m "Fix CRITICAL translation issues with LLM"
```

## 📋 オプション

### fix_issues_with_llm.py

```bash
python tools/integration/fix_issues_with_llm.py issues.json [オプション]

オプション:
  --severity {critical,high}
                        修正する問題の重大度（デフォルト: critical）
  --limit N             修正する問題の最大数（推奨: 10-20件ずつ）
  --dry-run             実際の修正を行わず、対象のみ表示
```

### 使用例

```bash
# CRITICAL問題を10件だけ修正（推奨）
python tools/integration/fix_issues_with_llm.py issues.json --limit 10

# HIGH優先度も含めて20件修正
python tools/integration/fix_issues_with_llm.py issues.json --severity critical high --limit 20

# すべてのCRITICAL問題を修正（慎重に）
python tools/integration/fix_issues_with_llm.py issues.json
```

## 💡 推奨ワークフロー

### 段階的修正

```bash
# ラウンド1: CRITICAL 10件
python tools/integration/fix_issues_with_llm.py issues.json --limit 10
cd docs && make clean && make html-ja 2>&1 | grep "build succeeded"
cd ..

# 警告が減っていれば次へ

# ラウンド2: さらに10件
python tools/integration/fix_issues_with_llm.py issues.json --limit 20
cd docs && make clean && make html-ja 2>&1 | grep "build succeeded"
cd ..

# 以下繰り返し...
```

### 問題が発生した場合

```bash
# 変更をロールバック
git checkout -- locales/ja/LC_MESSAGES/*.po

# limitを小さくして再試行
python tools/integration/fix_issues_with_llm.py issues.json --limit 5
```

## 🎯 対応する問題タイプ

### CRITICAL（最優先）

1. **日本語ラベル参照の問題** (43件)
   - 症状: `undefined label`
   - 原因: `:ref:`内のラベル名が日本語
   - 修正: ラベル名を英語のまま保持

2. **日本語ドキュメントパスの問題** (8件)
   - 症状: `unknown document`
   - 原因: `:doc:`内のパスが日本語
   - 修正: パスを英語のまま保持

### HIGH（高優先度）

3. **不整合な参照** (49件)
   - 症状: `inconsistent references`
   - 原因: 原文と翻訳で参照の数が異なる
   - 修正: すべての参照を保持

## ⚠️ 注意事項

1. **少量ずつ修正**: --limit 10-20 を推奨
2. **各修正後にビルド**: 警告が増えていないか確認
3. **ドライランで確認**: 初回は必ず --dry-run で確認
4. **バックアップ**: 重要な変更の前に git commit
5. **LLMの限界**: 完璧ではないため、手動確認が必要な場合もある

## 🔧 トラブルシューティング

### Ollamaに接続できない

```bash
# Ollamaが起動しているか確認
ollama list

# 起動していない場合
ollama serve
```

### モデルが見つからない

```bash
# モデルをダウンロード
ollama pull qwen2.5:7b-instruct-q5_K_M

# 利用可能なモデルを確認
ollama list
```

### 修正が失敗する

1. POファイルのパスが正しいか確認
2. エントリの行番号が正しいか確認
3. 少量（--limit 5）で試す
4. 手動修正に切り替える

## 📚 関連ドキュメント

- [TRANSLATION_REFLECTION_FIX.md](../../guides/TRANSLATION_REFLECTION_FIX.md) - 完全な修正ガイド
- [DETECT_TRANSLATION_QUICKSTART.md](../DETECT_TRANSLATION_QUICKSTART.md) - クイックスタート
- [AUTO_TRANSLATE.md](../../guides/AUTO_TRANSLATE.md) - 自動翻訳ガイド

---

**作成日**: 2024-12-22
**対象**: ローカルLLMを使用した自動修正
