# Translation Quality Checker Guide
# 翻訳品質チェッカー使用ガイド

## 概要

翻訳品質チェッカーは、日本語翻訳の品質を自動的にチェックし、問題を検出・修正するツールです。

### 解決する問題

1. **未翻訳コンテンツの検出**
   - msgstrが空または未記入のエントリーを自動検出
   - 部分的に翻訳されたコンテンツの識別

2. **RST構文エラーの検出**
   - 日本語は書いているのにHTMLに反映されない問題を発見
   - インラインマークアップのスペーシング問題を自動修正
   - マークアップの不一致を警告

従来は、ビルド後のHTMLを目視でチェックするしかなかった問題を、**ビルド前に自動的に検出できる**ようになります。

## インストール

### 必要なパッケージ

```bash
pip install polib
```

### オプション: LLM機能を使う場合

```bash
# Ollamaをインストール（システム依存）
# https://ollama.ai/

# モデルをダウンロード
ollama pull qwen2.5:7b-instruct-q5_K_M

# Pythonパッケージをインストール
pip install ollama
```

## 基本的な使い方

### 1. 翻訳品質をチェック

翻訳作業後、まず品質チェックを実行します：

```bash
python tools/quality/translation_quality_checker.py --check
```

**出力例:**
```
============================================================
翻訳品質チェック結果
============================================================
チェック済みファイル: 256
チェック済みエントリー: 8130
検出された問題: 1837
  - 未翻訳: 272
  - 構文エラー: 1378
  - 警告: 187
自動修正可能: 1376
============================================================
```

### 2. 自動修正を実行

スペーシング問題など、自動修正可能な問題を修正します：

```bash
python tools/quality/translation_quality_checker.py --fix
```

これにより、以下のような問題が自動的に修正されます：
- `** 太字 **` → `**太字**`
- `* イタリック *` → `*イタリック*`
- `` ` コード ` `` → `` `コード` ``

### 3. 詳細レポートを確認

HTMLレポートを生成して、問題の詳細を確認します：

```bash
python tools/quality/translation_quality_checker.py --report
```

レポートは `data/quality_reports/` に保存されます。

## レポートの見方

### HTMLレポート

生成されたHTMLレポートには以下の情報が含まれます：

#### 統計情報
- チェック済みファイル数
- チェック済みエントリー数
- 検出された問題数（種類別）
- 自動修正可能な問題数

#### フィルター機能
- **すべて**: 全ての問題を表示
- **エラーのみ**: 構文エラーのみ表示
- **警告のみ**: 警告のみ表示
- **自動修正可能のみ**: 自動修正可能な問題のみ表示

#### 問題の詳細
各問題について以下が表示されます：
- 問題の種類と深刻度
- 元の英語テキスト
- 現在の日本語翻訳
- 修正案（あれば）
- ファイル名と行番号

### JSONレポート

プログラムで処理する場合はJSONレポートを使用できます：

```bash
python tools/quality/translation_quality_checker.py --report
# JSONレポート: data/quality_reports/quality_report_YYYYMMDD_HHMMSS.json
```

## 推奨ワークフロー

### 翻訳作業後のチェック

```bash
# 1. 品質チェック
python tools/quality/translation_quality_checker.py --check

# 2. 自動修正
python tools/quality/translation_quality_checker.py --fix

# 3. 再チェック
python tools/quality/translation_quality_checker.py --check

# 4. 詳細レポート生成（問題が残っている場合）
python tools/quality/translation_quality_checker.py --report
```

### ビルド前のチェック

```bash
# ビルド前に品質チェック
python tools/quality/pre_build_check.py

# 自動修正してからビルド
python tools/quality/pre_build_check.py --auto-fix

# Strictモード（エラーがあれば中断）
python tools/quality/pre_build_check.py --strict
```

### 定期的なチェック

週次や月次で実行して、翻訳品質を維持：

```bash
# レポート生成
python tools/quality/translation_quality_checker.py --report

# 結果をエクスポート（JSONファイルを保存）
cp data/quality_reports/quality_report_latest.json reports/weekly/
```

## 検出される問題の種類

### 1. 未翻訳エントリー（Warning）

**問題:**
```po
msgid "This is English text"
msgstr ""
```

**対処法:**
- 手動で翻訳を追加
- 自動翻訳ツールを使用: `python tools/translation/batch_translate.py`

### 2. 太字マークアップのスペーシングエラー（Error）

**問題:**
```po
msgid "This is **bold** text"
msgstr "これは ** 太字 ** テキストです"
```

**修正案:**
```po
msgstr "これは**太字**テキストです"
```

**対処法:**
- 自動修正: `--fix` オプションを使用
- 手動修正: POファイルを直接編集

### 3. イタリック体マークアップのスペーシングエラー（Error）

**問題:**
```po
msgid "This is *italic* text"
msgstr "これは * イタリック * テキストです"
```

**修正案:**
```po
msgstr "これは*イタリック*テキストです"
```

### 4. コードマークアップのスペーシングエラー（Error）

**問題:**
```po
msgid "Use ``code`` here"
msgstr "ここで `` コード `` を使用"
```

**修正案:**
```po
msgstr "ここで``コード``を使用"
```

### 5. マークアップの不一致（Warning）

**問題:**
```po
msgid "This has **bold** and ``code``"
msgstr "これは太字とコードです"  # マークアップが消えている
```

**対処法:**
- 手動でマークアップを追加
- 英語版を参考に適切な位置にマークアップを配置

### 6. マークアップの数の不一致（Error）

**問題:**
```po
msgid "This has **bold text"
msgstr "これは**太字テキスト"  # 閉じ**がない
```

**対処法:**
- 手動でマークアップを修正
- 開始と終了のマークアップが対になっているか確認

## 高度な使い方

### LLMを使った修正案の提案

ローカルLLM（Ollama）を使用して、複雑な問題の修正案を提案できます：

```bash
python tools/quality/translation_quality_checker.py --report --use-llm
```

**注意:**
- VRAM 8GB以上を推奨
- Ollamaと `qwen2.5:7b-instruct-q5_K_M` モデルが必要
- 処理時間が長くなります

### 特定のファイルのみチェック

```bash
# スクリプトを修正してファイルパスを指定
# 現在の実装では全ファイルをチェックしますが、
# 必要に応じてスクリプトを編集してフィルタリング可能
```

### CI/CDパイプラインへの統合

```yaml
# .github/workflows/translation-quality.yml
name: Translation Quality Check

on:
  pull_request:
    paths:
      - 'locales/**/*.po'

jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: pip install polib
      - name: Run quality check
        run: python tools/quality/pre_build_check.py --strict
```

## トラブルシューティング

### 問題: polib がインストールされていない

```bash
pip install polib
```

### 問題: 大量のエラーが検出される

1. まず自動修正を試す:
   ```bash
   python tools/quality/translation_quality_checker.py --fix
   ```

2. レポートを生成して優先度を確認:
   ```bash
   python tools/quality/translation_quality_checker.py --report
   ```

3. エラーから修正（警告は後回し）

### 問題: LLM機能が動作しない

- Ollamaが起動しているか確認:
  ```bash
  ollama list
  ```

- モデルがダウンロードされているか確認:
  ```bash
  ollama list | grep qwen2.5
  ```

- LLMなしでも基本機能は使用可能:
  ```bash
  python tools/quality/translation_quality_checker.py --check
  ```

## ベストプラクティス

### 1. 定期的なチェック

- **毎日**: 翻訳作業後に `--check` を実行
- **週次**: 詳細レポートを生成して確認
- **リリース前**: `--strict` モードで検証

### 2. 自動修正の活用

- 自動修正可能な問題は積極的に `--fix` を使用
- ただし、修正後は必ず目視確認を行う

### 3. レポートの活用

- HTMLレポートをチームで共有
- 問題の傾向を分析して翻訳ガイドラインに反映

### 4. ビルド前の検証

- ビルド前に必ず `pre_build_check.py` を実行
- 重大なエラーがある場合はビルドを中止

## 参考資料

- [tools/quality/README.md](README.md) - 詳細なツール説明
- [RST構文ガイド](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html)
- [PO構文修正ガイド](../../guides/PO_SYNTAX_FIX_GUIDE.md)
