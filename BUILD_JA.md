# 日本語版ドキュメントのビルド方法

このドキュメントは、FIRST Tech Challenge Docs の日本語翻訳版をビルドする方法を説明します。

## 必要な環境

- Python 3.x
- Make (Windows の場合は `make` コマンドが利用可能であること)
- 必要なPythonパッケージ（`docs/requirements.txt` に記載）

## セットアップ

初回のみ、必要なパッケージをインストールします：

```bash
cd docs
make setup
```

または手動でインストール：

```bash
cd docs
pip install -r requirements.txt
```

## 日本語版のビルド

### 通常のHTMLビルド

日本語版のHTMLドキュメントをビルドする場合：

```bash
cd docs
make html-ja
```

ビルドされたHTMLファイルは `docs/build/html-ja/` ディレクトリに生成されます。

### 自動リビルド機能付きビルド（開発用）

翻訳作業中に自動的にリビルドとブラウザのライブリロードを行う場合：

```bash
cd docs
make autobuild-ja
```

このコマンドは以下の機能を提供します：

- **自動リビルド**: ソースファイルや翻訳ファイル（`locales/` フォルダ）の変更を検知して自動的にリビルド
- **ライブプレビュー**: http://localhost:7351 でプレビューが自動的に開きます
- **ブラウザ自動リロード**: ファイル変更時にブラウザが自動的にリロード

停止する場合は `Ctrl+C` を押します。

## 英語版（オリジナル）のビルド

英語版をビルドする場合：

```bash
cd docs
make html
```

ビルドされたファイルは `docs/build/html/` に生成されます。

## ビルドのクリーンアップ

ビルド成果物を削除する場合：

```bash
cd docs
make clean
```

## 翻訳ファイルの構成

翻訳ファイルは以下の場所にあります：

- `locales/ja/LC_MESSAGES/` - 日本語翻訳ファイル（.po/.mo ファイル）
- `docs/build/gettext/` - 翻訳テンプレートファイル（.pot ファイル）

## トラブルシューティング

### 警告が表示される場合

ビルド時に警告が表示されることがありますが、ビルド自体は成功します：

- **翻訳の不整合**: 一部のリンクや参照が翻訳されていない場合に表示されます
- **空の翻訳**: `msgstr` が空の場合、元の英語テキストが表示されます

### ビルドエラーの場合

1. `make clean` でビルド成果物をクリーンアップ
2. 再度 `make html-ja` を実行
3. エラーメッセージを確認し、該当する `.po` ファイルの構文をチェック

### POファイルの検証

POファイルのフォーマットが正しいか確認する場合：

```bash
msgfmt -c -v -o /dev/null locales/ja/LC_MESSAGES/<path>/<file>.po
```

## 利用可能なMakeターゲット

| コマンド | 説明 |
|---------|------|
| `make setup` | 必要なパッケージをインストール |
| `make html` | 英語版HTMLビルド |
| `make html-ja` | 日本語版HTMLビルド |
| `make autobuild` | 英語版の自動リビルド（ポート7350） |
| `make autobuild-ja` | 日本語版の自動リビルド（ポート7351） |
| `make clean` | ビルド成果物を削除 |
| `make latexpdf` | PDF版をビルド |

## 翻訳ワークフロー

1. `.pot` ファイルから `.po` ファイルを更新または作成
2. `.po` ファイルの `msgstr` に日本語訳を記入
3. `make html-ja` でビルドして確認
4. または `make autobuild-ja` で自動リビルドしながら翻訳作業

## 参考情報

- オリジナルリポジトリ: [FIRST-Tech-Challenge/ftcdocs](https://github.com/FIRST-Tech-Challenge/ftcdocs)
- Sphinx ドキュメント: https://www.sphinx-doc.org/
- Sphinx i18n: https://www.sphinx-doc.org/en/master/usage/advanced/intl.html
