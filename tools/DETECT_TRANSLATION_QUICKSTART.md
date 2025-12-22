# 翻訳未反映問題の検出ツール - クイックスタート

日本語翻訳を書いたのに、ビルドしたHTMLに反映されていない問題を自動検出するツールです。

## 🚀 クイックスタート（3ステップ）

### ステップ1: ビルドして警告を収集

```bash
cd docs
make clean && make html-ja 2>&1 | tee build.log
```

### ステップ2: 問題を分析

```bash
cd ..
python tools/analysis/analyze_translation_issues.py \
  docs/build.log \
  --html-report report.html
```

### ステップ3: レポートを確認

ブラウザで `report.html` を開いて、問題を確認します。

## 📊 レポートの見方

レポートには以下の情報が表示されます：

### 重大度レベル

- 🔴 **CRITICAL**: 翻訳が表示されない直接的な原因（最優先）
  - 日本語ラベル参照の問題
  - 日本語ドキュメントパスの問題
  
- 🟠 **HIGH**: リンクが壊れる問題（高優先）
  - 不整合な参照
  
- 🟡 **MEDIUM**: 表示に影響するが致命的ではない
  - インラインマークアップの問題
  
- ⚪ **LOW**: 表示に大きな影響なし
  - その他の軽微な問題

## 🔧 修正の進め方

### 1. CRITICAL問題を優先的に修正

最も影響が大きい問題から修正します：

```bash
# レポートから CRITICAL 問題を確認
# 該当するPOファイルを開いて修正
```

**修正例**:
```rst
# ❌ 間違い（ラベル名も翻訳されている）
:ref:`カスタムブロック <programming_resources/shared/myblocks/index:カスタムブロック（myblocks）>`

# ✅ 正しい（ラベル名は英語のまま）
:ref:`カスタムブロック <programming_resources/shared/myblocks/index:custom blocks (myblocks)>`
```

### 2. 修正後にビルドして確認

```bash
cd docs
make clean && make html-ja 2>&1 | tee build_after.log

# 警告が減っているか確認
grep "build succeeded" build_after.log
```

### 3. HTMLで実際の表示を確認

```bash
cd build/html-ja
python -m http.server 8000
# ブラウザで http://localhost:8000 を開く
```

## 🔍 その他のツール

### 未翻訳箇所の検出

英語のまま残っているテキストを検出:

```bash
python tools/analysis/detect_untranslated.py --check
```

### PO/HTML比較

POファイルに翻訳があるのに反映されていない箇所を検出:

```bash
python tools/analysis/detect_translation_not_reflected.py --check
```

## 📚 詳細なガイド

詳しい使い方や修正方法は以下のドキュメントを参照してください：

- **[guides/TRANSLATION_REFLECTION_FIX.md](../guides/TRANSLATION_REFLECTION_FIX.md)** - 完全な修正ガイド
- **[guides/ERROR_FIX_GUIDE.md](../guides/ERROR_FIX_GUIDE.md)** - 一般的なエラー修正
- **[tools/README.md](README.md)** - 全ツールの説明

## 🎯 デモスクリプト

全ステップを自動実行するデモスクリプトも用意されています：

```bash
./tools/demo_detect_translation_issues.sh
```

このスクリプトは以下を実行します：
1. 日本語版をビルド
2. 警告を分析
3. HTMLレポートを生成
4. サマリーを表示

## ⚠️ 注意事項

### 修正前の確認

```bash
# 修正前の警告数を必ずメモ
cd docs
make clean && make html-ja 2>&1 | grep "build succeeded"
# 例: "build succeeded, 256 warnings."
```

### 修正後の確認

修正後に警告数が**増えていない**ことを確認してください。

### LLMによる自動修正

VRAM 8GBのローカルLLMを使用する場合は慎重に：
- 少量（10-20件）ずつ修正
- 各修正後にビルドして確認
- 悪化した場合はロールバック

## 🆘 トラブルシューティング

### Q: モジュールが見つからないエラー

```bash
pip install polib beautifulsoup4 lxml
```

### Q: ビルドディレクトリが見つからない

```bash
# 先に日本語版をビルド
cd docs
make html-ja
```

### Q: レポートが開けない

レポートファイルのパスを確認してください：
```bash
ls -la report.html
# または
ls -la reports/translation_issues.html
```

---

**作成日**: 2024-12-22
**対象バージョン**: FTC Docs 日本語版
