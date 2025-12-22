# 翻訳未反映問題の検出・修正ガイド

このガイドでは、日本語翻訳が存在するのにHTMLに反映されていない問題を検出・修正する方法を説明します。

## 📋 目次

1. [問題の概要](#問題の概要)
2. [検出ツールの使用方法](#検出ツールの使用方法)
3. [問題の種類と修正方法](#問題の種類と修正方法)
4. [自動修正の可能性](#自動修正の可能性)

---

## 問題の概要

日本語翻訳プロジェクトでは、以下の2種類の「未反映」問題が発生します：

### 1. 翻訳データがない場合
- **原因**: POファイルの`msgstr`が空、または部分的に未翻訳
- **症状**: 英語のままHTML に表示される
- **解決**: 翻訳を追加する（自動翻訳ツールが利用可能）

### 2. 翻訳データがあるのに反映されない場合 ⚠️
- **原因**: RST構文エラー、Sphinxの仕様/バグ
- **症状**: 日本語翻訳を書いているのに英語のまま表示される
- **解決**: このガイドで扱う問題

**このガイドは後者の問題を検出・修正するためのものです。**

---

## 検出ツールの使用方法

### ステップ1: ビルドと警告の収集

まず、日本語版をビルドして警告を確認します：

```bash
cd docs
make clean && make html-ja 2>&1 | tee build.log
```

現在の警告数を確認：
```bash
grep "build succeeded" build.log
```

**重要**: 修正前の警告数をメモしておき、修正後に増えていないことを確認してください。

### ステップ2: 翻訳問題の分析

新しい分析ツールを使用して、問題を特定します：

```bash
# コンソールに結果を表示
python tools/analysis/analyze_translation_issues.py build.log

# HTMLレポートを生成（推奨）
python tools/analysis/analyze_translation_issues.py build.log --html-report report.html

# JSON形式でエクスポート
python tools/analysis/analyze_translation_issues.py build.log --json issues.json
```

### ステップ3: HTMLレポートの確認

生成された`report.html`をブラウザで開くと、以下の情報が表示されます：

- **統計情報**: 総警告数、重大度別の数
- **最重要問題**: 日本語ラベル/ドキュメントパス参照の問題
- **警告タイプ別**: どの種類の問題が多いか
- **ファイル別**: どのファイルに問題が集中しているか

---

## 問題の種類と修正方法

### 🔴 最重要: 日本語ラベル参照の問題

**症状**: `undefined label: 'programming_resources/shared/myblocks/index:カスタムブロック（myblocks）'`

**原因**: ラベル名が日本語に翻訳されているため、参照が壊れている

**修正方法**:
```rst
# ❌ 間違い（ラベル名も翻訳されている）
:ref:`カスタムブロック <programming_resources/shared/myblocks/index:カスタムブロック（myblocks）>`

# ✅ 正しい（ラベル名は英語のまま、表示テキストのみ日本語）
:ref:`カスタムブロック <programming_resources/shared/myblocks/index:custom blocks (myblocks)>`
```

**重大度**: CRITICAL - これらは日本語が表示されない直接的な原因です

**該当POファイルを特定**:
1. HTMLレポートの「日本語ラベル参照の問題」セクションを確認
2. ファイル名と行番号をメモ
3. 該当POファイルを開いて修正

### 🔴 最重要: 日本語ドキュメントパスの問題

**症状**: `unknown document: 'ハードウェアとソフトウェア設定/構成/index'`

**原因**: ドキュメントパスが日本語に翻訳されている

**修正方法**:
```rst
# ❌ 間違い
:doc:`ハードウェアとソフトウェア設定/構成/index`

# ✅ 正しい（パスは英語のまま、表示テキストのみ日本語）
:doc:`ハードウェアとソフトウェア設定 <hardware_and_software_configuration/configuring/index>`
```

**重大度**: CRITICAL

### 🟠 高優先度: 不整合な参照

**症状**: `inconsistent term references` または `inconsistent references`

**原因**: 原文と翻訳で参照の数や順序が一致していない

**例**:
```rst
# 原文: 2つの参照
[':doc:`Guide 1 <path1>`', ':doc:`Guide 2 <path2>`']

# 翻訳: 1つしかない（間違い）
[':doc:`ガイド1 <path1>`']
```

**修正方法**:
1. 原文の参照をすべて確認
2. 翻訳にも同じ数だけ参照を含める
3. 順序を保つ

**重大度**: HIGH

### 🟡 中優先度: インラインマークアップの問題

**症状**: 
- `Inline interpreted text or phrase reference start-string without end-string`
- `Inline emphasis start-string without end-string`
- `Inline literal start-string without end-string`

**原因**: マークアップ記号（`:ref:`, `*`, `` ` ``）の開始と終了が対応していない

**例**:
```rst
# ❌ 間違い（バッククォートが不足）
:ref:`リンクテキスト <path:label>

# ✅ 正しい
:ref:`リンクテキスト <path:label>`
```

**注意**: 
- 問題文の指示により、「end-string」関連の単純な問題は優先度を下げてください
- 表示に大きな問題はなく、スクリプトで対処可能な場合が多い

**重大度**: MEDIUM

---

## 自動修正の可能性

### ローカルLLMを使用した修正

VRAM 8GBのローカルLLMを使用して、段階的に修正できます：

```bash
# Ollamaがインストールされている場合
ollama pull qwen2.5:7b-instruct-q5_K_M

# LLMによる修正（慎重に、少量ずつ）
python tools/po-fixing/fix_po_with_llm.py \
  --issues translation_issues.json \
  --types undefined_label \
  --limit 10
```

**注意事項**:
- LLMは完璧ではないため、少量（10-20件）ずつ修正
- 各修正後にビルドして警告が増えていないか確認
- 悪化した場合は中止してロールバック

### 手動修正推奨のケース

以下の場合は手動修正を推奨します：

1. **日本語ラベル参照の問題** (CRITICAL)
   - 数が少ない（43件程度）
   - パターンが明確
   - 手動で確実に修正できる

2. **日本語ドキュメントパスの問題** (CRITICAL)
   - 数が非常に少ない（8件程度）
   - 手動で確実に修正すべき

3. **複雑な不整合** (HIGH)
   - コンテキストを理解する必要がある
   - LLMでは対処が難しい

---

## 修正ワークフロー

### 推奨手順

1. **警告のベースライン確認**
   ```bash
   cd docs
   make clean && make html-ja 2>&1 | tee build_before.log
   grep "build succeeded" build_before.log
   # 例: "build succeeded, 256 warnings."
   ```

2. **問題を分析**
   ```bash
   python tools/analysis/analyze_translation_issues.py build_before.log --html-report report.html
   # ブラウザでreport.htmlを開く
   ```

3. **最重要問題から修正** (CRITICAL優先)
   - 日本語ラベル参照の問題（43件）
   - 日本語ドキュメントパスの問題（8件）
   
   該当するPOファイルを開いて手動修正

4. **ビルドして確認**
   ```bash
   make clean && make html-ja 2>&1 | tee build_after.log
   grep "build succeeded" build_after.log
   ```

5. **警告数が減っているか確認**
   ```bash
   # 警告数の差分を確認
   python tools/analysis/analyze_translation_issues.py build_after.log
   ```

6. **HTMLで実際の表示を確認**
   ```bash
   # ローカルサーバーで確認
   cd build/html-ja
   python -m http.server 8000
   # ブラウザで http://localhost:8000 を開く
   ```

7. **コミット**
   ```bash
   git add locales/ja/LC_MESSAGES/*.po
   git commit -m "Fix critical translation reflection issues"
   ```

### 段階的修正（大量の問題がある場合）

```bash
# ラウンド1: CRITICAL問題のみ（手動）
# → 日本語ラベル、ドキュメントパスを修正
# → ビルド確認 → コミット

# ラウンド2: HIGH問題（手動またはLLM）
# → 不整合な参照を修正
# → ビルド確認 → コミット

# ラウンド3: MEDIUM問題（スクリプトまたはLLM）
# → インラインマークアップを修正
# → ビルド確認 → コミット
```

---

## トラブルシューティング

### Q: 修正したのに警告が減らない

A: 以下を確認してください：
1. `make clean`を実行したか
2. 正しいPOファイルを修正したか
3. POファイルの構文エラーがないか（`msgfmt --check-format file.po`）
4. ビルドログで具体的なエラーメッセージを確認

### Q: 警告が増えてしまった

A: 直前のコミットにロールバック：
```bash
git checkout -- locales/ja/LC_MESSAGES/*.po
```

### Q: HTMLで表示を確認する最良の方法は？

A: 
1. `make html-ja`でビルド
2. `build/html-ja`ディレクトリでローカルサーバーを起動
3. ブラウザで該当ページを開いて確認
4. 特に問題が報告されたファイルを重点的にチェック

### Q: どの問題を優先すべき？

A: 重大度順：
1. CRITICAL: 日本語ラベル、ドキュメントパス（翻訳が表示されない）
2. HIGH: 不整合な参照（リンクが壊れる）
3. MEDIUM: インラインマークアップ（表示は概ね問題なし）
4. LOW: その他（無視してもよい場合が多い）

---

## 関連ドキュメント

- [ERROR_FIX_GUIDE.md](ERROR_FIX_GUIDE.md) - 一般的なエラー修正ガイド
- [PO_SYNTAX_FIX_GUIDE.md](PO_SYNTAX_FIX_GUIDE.md) - PO構文エラーの修正
- [TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md) - 翻訳ガイドライン
- [AUTO_TRANSLATE.md](AUTO_TRANSLATE.md) - 自動翻訳の使い方

---

## ツール一覧

### 新規追加ツール

1. **`tools/analysis/analyze_translation_issues.py`** ⭐ NEW
   - ビルド警告を分析して翻訳問題を特定
   - 重大度別、タイプ別の統計
   - HTMLレポート生成
   - JSON形式でエクスポート

2. **`tools/analysis/detect_translation_not_reflected.py`** ⭐ NEW
   - POファイルとHTMLを比較
   - 翻訳があるのに反映されていない箇所を検出

### 既存ツール

- **`tools/analysis/detect_untranslated.py`**
  - 英語のまま残っているテキストを検出

- **`tools/analysis/compare_build_structures.py`**
  - 英語版と日本語版のビルド構造を比較

---

**作成日**: 2024-12-22
**対象**: 翻訳メンテナー、翻訳レビュアー
