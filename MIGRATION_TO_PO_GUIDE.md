# .po-based Translation System Migration Guide

## 概要 (Overview)

このドキュメントは、ftcdocs-jaプロジェクトを従来の「RST直接翻訳」方式から、より標準的な「.po (gettext)」ベースの翻訳システムへ移行する手順を説明します。

### なぜ.poベースの翻訳に移行するのか？

1. **上流の変更への追従性**: 公式リポジトリ（英語版）の変更を容易に取り込める
2. **翻訳管理の効率化**: 翻訳済み文字列の再利用、部分的な翻訳が可能
3. **業界標準**: gettextは国際化(i18n)の標準的な手法
4. **メンテナンス性**: 英語版と日本語版を分離して管理できる

## 新しいワークフロー

### 旧方式（従来）
```
英語版RST → 直接日本語に翻訳 → 日本語版RST
```

**問題点**: 
- 上流の変更をマージするのが困難
- どの部分が翻訳されたか追跡が難しい

### 新方式（.poベース）
```
英語版RST → .pot生成 → .po作成/更新 → Sphinxビルド → 日本語HTML
```

**利点**:
- 英語版RST は変更不要（上流と同期可能）
- 翻訳状態を.poファイルで管理
- 部分的な翻訳でもビルド可能
- 翻訳ツール（Poedit, Weblate等）が利用可能

## セットアップ手順

### 1. 必要なツールのインストール

```bash
# sphinx-intl のインストール
pip install sphinx-intl

# 確認
sphinx-intl --version
```

### 2. ディレクトリ構造

```
ftcdocs-ja/
├── docs/
│   ├── source/           # 英語版RST（上流と同期）
│   │   ├── index.rst
│   │   └── ...
│   ├── locale/           # 翻訳ファイル（新規作成）
│   │   └── ja/          # 日本語
│   │       └── LC_MESSAGES/
│   │           ├── index.po
│   │           └── ...
│   └── build/           # ビルド結果
└── docs-ja/             # 翻訳関連ドキュメント
```

### 3. .potファイルの生成（翻訳可能な文字列の抽出）

```bash
cd docs

# 翻訳可能な文字列を抽出
make gettext

# 結果: build/gettext/*.pot ファイルが生成される
```

### 4. .poファイルの作成（日本語翻訳ファイル）

```bash
# 日本語（ja）の.poファイルを生成
sphinx-intl update -p build/gettext -l ja

# 結果: locale/ja/LC_MESSAGES/*.po ファイルが生成される
```

### 5. 翻訳作業

.poファイルを編集して翻訳を追加します：

```po
# locale/ja/LC_MESSAGES/index.po
msgid "Welcome to FIRST Tech Challenge"
msgstr "FIRST Tech Challenge へようこそ"

msgid "This is the official documentation"
msgstr "これは公式ドキュメントです"
```

**編集方法**:
- テキストエディタで直接編集
- Poedit などの専用ツール
- Weblate などのオンライン翻訳プラットフォーム

### 6. 翻訳済みドキュメントのビルド

```bash
# 日本語版をビルド
make -e SPHINXOPTS="-D language='ja'" html

# または、より簡潔に
sphinx-build -D language=ja source build/html/ja
```

## 既存翻訳の移行

既に docs/source/*.rst に日本語翻訳がある場合の移行手順：

### 自動移行スクリプトの使用

```bash
# 移行スクリプトを実行
python scripts/migrate_translations_to_po.py

# オプション:
# --source-dir: 日本語RST のディレクトリ
# --pot-dir: .pot ファイルのディレクトリ
# --output-dir: 出力先.poファイルのディレクトリ
```

### 手動移行の手順

1. **英語版RST を復元**
   ```bash
   # 上流リポジトリから英語版を取得
   git remote add upstream https://github.com/FIRST-Tech-Challenge/ftcdocs.git
   git fetch upstream
   ```

2. **.potファイルを生成**
   ```bash
   make gettext
   ```

3. **.poファイルを作成**
   ```bash
   sphinx-intl update -p build/gettext -l ja
   ```

4. **既存の翻訳を.poファイルに手動コピー**
   - 日本語RST から翻訳済み文字列を抽出
   - 対応する.poファイルの msgstr に貼り付け

## 翻訳ワークフロー

### 日常的な翻訳作業

```bash
# 1. 上流の変更を取り込む
git fetch upstream
git merge upstream/main

# 2. 新しい/変更された文字列を抽出
cd docs
make gettext

# 3. .po ファイルを更新
sphinx-intl update -p build/gettext -l ja

# 4. 翻訳作業
# locale/ja/LC_MESSAGES/*.po を編集

# 5. ビルドして確認
make -e SPHINXOPTS="-D language='ja'" html

# 6. コミット
git add locale/
git commit -m "翻訳: [ファイル名] を更新"
```

### 翻訳状態の確認

```bash
# 翻訳進捗を確認
sphinx-intl stat

# または、個別のファイルを確認
msgfmt --statistics locale/ja/LC_MESSAGES/index.po
```

## 設定ファイル (conf.py)

必要な設定が docs/source/conf.py に含まれていることを確認：

```python
# Internationalization (i18n) 設定
language = 'en'  # デフォルト言語
locale_dirs = ['locale/']  # .po ファイルの場所
gettext_compact = False  # ファイルごとに個別の.po
```

## よくある質問

### Q1: 既存の日本語RST はどうなりますか？

A: 移行後は英語版RST に戻します。翻訳は全て.poファイルで管理されます。

### Q2: 部分的に翻訳されていない場合は？

A: .poファイルで msgstr が空の場合、自動的に英語（msgid）が表示されます。

### Q3: 技術用語（OpMode等）はどう扱いますか？

A: .poファイルでも同様に英語のまま残せます：
```po
msgid "Create a new OpMode"
msgstr "新しい **OpMode** を作成します"
```

### Q4: 上流の変更にはどう対応しますか？

A: sphinx-intl update を実行すると、新しい文字列は追加され、削除された文字列はマークされ、変更された文字列は "fuzzy" としてマークされます。

### Q5: 複数人で翻訳する場合は？

A: .poファイルをGitで管理し、通常のプルリクエストワークフローで進めます。Weblate等のツールを使えばさらに効率的です。

## トラブルシューティング

### ビルドエラー: "locale directory not found"

```bash
# locale ディレクトリを作成
mkdir -p docs/locale/ja/LC_MESSAGES
```

### msgid と msgstr が一致しない

```bash
# .po ファイルの構文をチェック
msgfmt -c locale/ja/LC_MESSAGES/index.po
```

### 翻訳が反映されない

```bash
# クリーンビルド
cd docs
make clean
make gettext
sphinx-intl update -p build/gettext -l ja
make -e SPHINXOPTS="-D language='ja'" html
```

## 参考資料

- [Sphinx Internationalization](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx-intl Documentation](https://sphinx-intl.readthedocs.io/)
- [GNU gettext Manual](https://www.gnu.org/software/gettext/manual/)
- [Poedit - .po editor](https://poedit.net/)
- [Weblate - Web-based translation](https://weblate.org/)

## まとめ

.poベースの翻訳システムへの移行により：

✅ 上流の変更を容易に追従できる  
✅ 翻訳状態を明確に管理できる  
✅ 標準的なツールとワークフローが使える  
✅ 複数人での翻訳作業が効率化される  
✅ 部分翻訳でもビルド可能  

この移行は一度の作業で完了し、その後のメンテナンスが大幅に改善されます。
