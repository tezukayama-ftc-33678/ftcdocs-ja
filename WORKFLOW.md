# FTC日本語ドキュメント 翻訳ワークフロー

このドキュメントでは、FTC公式ドキュメントの日本語翻訳プロジェクトにおける基本的なワークフローを説明します。

---

## 📋 目次

1. [必要なツール](#必要なツール)
2. [メインスクリプト（3つ）](#メインスクリプト3つ)
3. [上流更新への追従](#上流更新への追従)
4. [新規ドキュメントの翻訳](#新規ドキュメントの翻訳)
5. [翻訳の確認とビルド](#翻訳の確認とビルド)

---

## 必要なツール

### 1. ローカルLLMのセットアップ

```powershell
# Ollamaをインストール（https://ollama.ai/）
# インストール後、翻訳用モデルをダウンロード
ollama pull qwen2.5-coder:7b-instruct
```

詳細は [guides/LOCAL_LLM_SETUP.md](guides/LOCAL_LLM_SETUP.md) を参照。

### 2. Pythonパッケージ

```powershell
pip install polib ollama tqdm colorama
```

### 3. Sphinx（ビルド用）

```powershell
pip install -r docs/requirements.txt
```

---

## メインスクリプト（3つ）

プロジェクトのメインスクリプトは以下の3つです：

### 1️⃣ **翻訳スクリプト**: `scripts/translate_po_smart.py`

POファイルを翻訳するメインスクリプト。RST構文を保護しながら高品質な翻訳を実行します。

```powershell
# 単一ファイルを翻訳
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po

# バッチ翻訳（全ファイル）
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

**設定ファイル**: `data/translate_config.json`

### 2️⃣ **翻訳テスト**: `scripts/test_simplified_chinese_detection.py`

簡体字中国語の誤混入を検出するテストスクリプト。

```powershell
python scripts/test_simplified_chinese_detection.py
```

翻訳品質を確認し、中国語が混入していないかチェックします。

### 3️⃣ **構文エラー自動修正**: `scripts/normalize_po_files.py`

POファイルの構文エラーや誤訳を自動修正します。

```powershell
# 単一ファイルを修正
python scripts/normalize_po_files.py locales/ja/LC_MESSAGES/index.po

# 全ファイルを修正
python scripts/normalize_po_files.py locales/ja/LC_MESSAGES
```

**設定ファイル**: `data/mistranslation_corrections.json`

---

## 上流更新への追従

FTC公式ドキュメントが更新された際の追従手順：

### ステップ1: 上流の変更を取り込む

```bash
# 上流リポジトリを追加（初回のみ）
git remote add upstream https://github.com/FIRST-Tech-Challenge/ftcdocs.git

# 上流の最新版を取得
git fetch upstream

# 上流の変更をマージ
git merge upstream/main
```

### ステップ2: POファイルを再生成

```bash
cd docs

# 既存の翻訳を保持しながらPOファイルを更新
make gettext
sphinx-intl update -p build/gettext -l ja
```

これにより、新しい原文が追加され、既存の翻訳は保持されます。

### ステップ3: 未翻訳部分を翻訳

```powershell
# 未翻訳部分のみを翻訳（既翻訳はスキップされる）
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

### ステップ4: ビルドして確認

```bash
cd docs
make html-ja

# ブラウザで確認
# Windows: start build/html-ja/index.html
# Mac/Linux: open build/html-ja/index.html
```

---

## 新規ドキュメントの翻訳

完全に新しいドキュメントページが追加された場合：

### ステップ1: POファイルの生成

```bash
cd docs

# 新しい原文からPOファイルを生成
make gettext
sphinx-intl update -p build/gettext -l ja
```

新しい `.po` ファイルが `locales/ja/LC_MESSAGES/` 以下に作成されます。

### ステップ2: 翻訳実行

```powershell
# 特定のファイルを翻訳
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/<新しいファイル>.po

# または全ファイルをバッチ翻訳
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

### ステップ3: 構文エラーの修正

```powershell
# 翻訳後の構文チェックと修正
python scripts/normalize_po_files.py locales/ja/LC_MESSAGES/<新しいファイル>.po
```

### ステップ4: ビルドして確認

```bash
cd docs
make html-ja
```

---

## 翻訳の確認とビルド

### ローカルビルド

```bash
cd docs

# 日本語版をビルド
make html-ja

# ブラウザで確認
# Windows
start build/html-ja/index.html

# Mac/Linux
open build/html-ja/index.html
```

### ビルドエラーの確認

```bash
# ビルド時の警告を確認
make html-ja 2>&1 | grep WARNING

# クリーンビルド（キャッシュをクリア）
make clean
make html-ja
```

### 翻訳品質のチェック

```powershell
# 簡体字中国語の混入チェック
python scripts/test_simplified_chinese_detection.py

# 構文エラーのチェックと修正
python scripts/normalize_po_files.py locales/ja/LC_MESSAGES
```

---

## 📚 参考資料

- **用語集**: [guides/GLOSSARY.md](guides/GLOSSARY.md) - FTC用語の統一表記
- **ライセンス**: [guides/LICENSE_AND_LOGO_GUIDE.md](guides/LICENSE_AND_LOGO_GUIDE.md) - ライセンスとロゴの使用
- **LLMセットアップ**: [guides/LOCAL_LLM_SETUP.md](guides/LOCAL_LLM_SETUP.md) - ローカルLLM環境の構築

---

## 🎯 Tips

### 効率的な翻訳

```powershell
# 重要なファイルから翻訳
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/overview/overview.po

# その後、残りをバッチ処理
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

### 進捗の確認

```powershell
# 翻訳進捗を確認
python -c "import polib; print(f'{sum(1 for e in polib.pofile(\"locales/ja/LC_MESSAGES/index.po\") if e.msgstr)} translated')"
```

### トラブルシューティング

- **モデルが見つからない**: `ollama list` で確認、`ollama pull qwen2.5-coder:7b-instruct` で再ダウンロード
- **VRAM不足**: 軽量モデル `qwen2.5-coder:7b-instruct-q4_K_M` を使用
- **翻訳品質が低い**: `data/translate_config.json` の `temperature` を下げる（0.05など）

---

## 🤝 質問・サポート

問題が発生した場合は、GitHubのIssuesで質問してください。

**旧ドキュメント**: 古いガイドやスクリプトは `legacy/` フォルダに保存されています。
