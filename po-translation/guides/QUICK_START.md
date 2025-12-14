# .po 翻訳クイックスタート

**15分で始める .po ベース翻訳システム**

## 🎯 このガイドの目的

- .po 翻訳の基本を理解する
- 最初の翻訳を完成させる
- 日常的なワークフローを習得する

## 📚 .po翻訳とは？

**.po (Portable Object)** は、ソフトウェア国際化の標準的な翻訳形式です。

### 従来のRST直接翻訳との違い

| 項目 | RST直接翻訳 | .po翻訳 |
|-----|------------|--------|
| 編集対象 | RSTファイル全体 | メッセージ単位 |
| 上流との同期 | 手動マージ（困難） | 自動更新 |
| RST構文の知識 | 必須 | 不要 |
| AI翻訳 | 困難 | 容易 |

### メリット

- ✅ **上流との同期が簡単** - 英語の変更を自動で取り込める
- ✅ **翻訳に集中できる** - RST構文を気にする必要がない
- ✅ **AI翻訳に最適** - 翻訳単位が明確
- ✅ **標準ツールが使える** - Poedit、Weblate等

## ⚡ 環境セットアップ（5分）

### 前提条件

```bash
# Python 3.7以上が必要
python --version

# Gitリポジトリをクローン済みであること
cd /path/to/ftcdocs-ja
```

### 依存関係のインストール

```bash
# docsディレクトリに移動
cd docs

# 必要なPythonパッケージをインストール
pip install -r requirements.txt

# インストールされたことを確認
sphinx-intl --version
```

### 上流リポジトリの設定（初回のみ）

```bash
# ルートディレクトリに戻る
cd ..

# 上流（英語版）をリモートとして追加
git remote add upstream https://github.com/FIRST-Tech-Challenge/ftcdocs.git

# 上流の変更を取得
git fetch upstream
```

## 🚀 最初の翻訳（10分）

### ステップ1: .pot/.poファイルの生成

```bash
cd docs

# 英語RSTから翻訳可能文字列を抽出
make gettext

# 日本語.poファイルを生成/更新
make ja-update
```

**何が起きた？**
- `build/gettext/*.pot` - 翻訳テンプレートファイルが生成された
- `locale/ja/LC_MESSAGES/*.po` - 日本語翻訳ファイルが生成/更新された

### ステップ2: .poファイルの編集

.poファイルを開いてみましょう：

```bash
# エディタで開く（例: vim、nano、VS Code等）
vim locale/ja/LC_MESSAGES/index.po
```

**ファイルの構造:**

```po
# コメント: ファイルの場所と行番号
#: ../../source/index.rst:5
msgid "Welcome to FIRST Tech Challenge"
msgstr ""

# ↑ msgstr に翻訳を入力
#: ../../source/index.rst:5
msgid "Welcome to FIRST Tech Challenge"
msgstr "FIRST Tech Challenge へようこそ"
```

### ステップ3: 翻訳の入力

最初のいくつかのエントリを翻訳してみましょう：

```po
#: ../../source/index.rst:5
msgid "Welcome to FIRST Tech Challenge"
msgstr "FIRST Tech Challenge へようこそ"

#: ../../source/index.rst:10
msgid "This documentation provides information about programming and configuring robots."
msgstr "このドキュメントでは、ロボットのプログラミングと設定に関する情報を提供します。"
```

**翻訳のルール:**
- 技術用語は太字の英語で残す: `**OpMode**`
- コードは翻訳しない: `` `code` ``
- RSTマークアップを保持: `:doc:`リンク <path>`

詳細は [AI_TRANSLATION_GUIDE.md](AI_TRANSLATION_GUIDE.md) を参照。

### ステップ4: ビルドとプレビュー

```bash
# 日本語版をビルド
make ja-build

# ビルド成功を確認
ls build/html/ja/index.html

# プレビュー
python -m http.server 8000 --directory build/html/ja
```

ブラウザで `http://localhost:8000` を開いて、翻訳を確認してください。

### ステップ5: 進捗確認

```bash
# 全体の翻訳統計を表示
make ja-stats

# 特定ファイルの統計
msgfmt --statistics locale/ja/LC_MESSAGES/index.po
```

## 🔄 日常的なワークフロー

### 上流の変更を取り込む

```bash
# 1. 上流の変更を取得してマージ
git fetch upstream
git merge upstream/main

# 2. 新しい翻訳可能文字列を抽出
cd docs
make gettext

# 3. .poファイルを更新
make ja-update

# 4. 変更を確認
make ja-stats
```

**何が起きる？**
- 新しい文字列 → `msgstr ""` として追加される
- 変更された文字列 → `#, fuzzy` フラグが付く
- 削除された文字列 → `#~` でコメントアウトされる

### 新しい/変更された翻訳を追加

```bash
# 1. fuzzyまたは空のmsgstrを探す
grep -n "fuzzy" locale/ja/LC_MESSAGES/index.po
grep -n 'msgstr ""' locale/ja/LC_MESSAGES/index.po

# 2. .poファイルを編集して翻訳

# 3. ビルドして確認
make ja-build
python -m http.server 8000 --directory build/html/ja

# 4. コミット
cd ..
git add docs/locale/ja/
git commit -m "翻訳: indexページを更新"
git push
```

## 🛠️ 便利なツール

### Poedit（GUIエディタ）

初心者に最もおすすめ：

```
ダウンロード: https://poedit.net/
機能: 翻訳メモリ、検証、統計表示
使い方: .poファイルを開いて編集するだけ
```

### VS Code（開発者向け）

```bash
# i18n Ally拡張機能をインストール
code --install-extension lokalise.i18n-ally

# .poファイルを開くと、インライン翻訳エディタが使える
```

### コマンドライン

```bash
# 未翻訳を探す
grep -r 'msgstr ""' locale/ja/LC_MESSAGES/

# fuzzyを探す
grep -r "fuzzy" locale/ja/LC_MESSAGES/

# 統計
msgfmt --statistics locale/ja/LC_MESSAGES/*.po

# 検証
msgfmt -c locale/ja/LC_MESSAGES/index.po
```

## 📖 .poファイルの構造

### 基本形式

```po
# ファイルヘッダー（メタデータ）
msgid ""
msgstr ""
"Language: ja\n"
"Content-Type: text/plain; charset=UTF-8\n"

# 翻訳エントリ
#: ../../source/file.rst:10
msgid "English text"
msgstr "日本語テキスト"
```

### エントリの状態

```po
# 未翻訳（翻訳が必要）
msgid "New feature"
msgstr ""

# 翻訳済み（OK）
msgid "Documentation"
msgstr "ドキュメント"

# Fuzzy（確認が必要）
#, fuzzy
msgid "Changed text"
msgstr "古い翻訳"

# 削除済み（無視してOK）
#~ msgid "Removed text"
#~ msgstr "削除された翻訳"
```

### 複数行

```po
# 長いテキストは複数行に分割できる
msgid ""
"This is a very long text that "
"spans multiple lines."
msgstr ""
"これは複数行にわたる "
"非常に長いテキストです。"
```

## 🎯 翻訳のコツ

### 1. 技術用語は英語のまま

```po
msgid "Create a new OpMode"
msgstr "新しい **OpMode** を作成します"
```

### 2. RSTマークアップを保持

```po
msgid "See :doc:`introduction <intro>` for details"
msgstr "詳細は :doc:`入門 <intro>` を参照してください"
```

### 3. コードは翻訳しない

```po
msgid "Use the ``init()`` method"
msgstr "``init()`` メソッドを使用します"
```

### 4. 文体を統一

- 「です・ます」調で統一
- 句読点は全角（、。）

## 🆘 トラブルシューティング

### ビルドエラー

```bash
# クリーンビルド
make clean
make gettext
make ja-build
```

### .poファイルの構文エラー

```bash
# 検証
msgfmt -c -v locale/ja/LC_MESSAGES/index.po

# エラーメッセージに従って修正
```

### 翻訳が反映されない

1. `make clean && make ja-build` でクリーンビルド
2. ブラウザのキャッシュをクリア
3. `msgstr` が空でないか確認

## 📚 次のステップ

基本を理解したら、以下のガイドを読んでください：

1. **[AI_TRANSLATION_GUIDE.md](AI_TRANSLATION_GUIDE.md)** - AI翻訳の活用方法
2. **[WORKFLOW.md](WORKFLOW.md)** - 詳細なワークフロー
3. **[../reference/GLOSSARY.md](../reference/GLOSSARY.md)** - 用語集

## 📝 まとめ

### 覚えておくべきコマンド

```bash
# 基本ワークフロー
make gettext      # 翻訳可能文字列を抽出
make ja-update    # .poファイルを更新
# [.poファイルを編集]
make ja-build     # 日本語版をビルド
make ja-stats     # 進捗確認
```

### .poファイルの編集

- `msgstr ""` → 翻訳を追加
- `#, fuzzy` → 確認して更新
- 技術用語は `**英語**`
- RSTマークアップを保持

---

**🎉 これで .po 翻訳の基本をマスターしました！**

次は [AI_TRANSLATION_GUIDE.md](AI_TRANSLATION_GUIDE.md) を読んで、AI翻訳を活用しましょう。
