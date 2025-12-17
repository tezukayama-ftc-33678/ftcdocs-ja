# 翻訳アプローチの説明

## 概要

このプロジェクトでは、FTC Docs の日本語翻訳に2つの異なるアプローチを組み合わせています：

1. **自動翻訳 (.po ファイル)**: ほとんどのページ
2. **手動翻訳 (RST ファイル直接編集)**: トップページと主要ペルソナページ

## なぜ2つのアプローチを使うのか？

ローカルLLMによる自動翻訳は効率的ですが、以下の問題が発生する可能性があります：

- 翻訳の不正確さ
- 構造の崩れ（特に複雑なRSTディレクティブ）
- ビルドエラー

そのため、**構造が重要なページ**については、RSTファイルを直接翻訳することで、
構造の完全性を保証しています。

## 手動翻訳されているページ

以下のページは RST ファイルを直接翻訳しており、.po ファイルは使用していません：

### 1. トップページ
- **ファイル**: `docs/source/index.rst`
- **理由**: サイト全体の入り口であり、構造が最も重要
- **特徴**: 
  - 警告ノート（非公式翻訳であることの明示）
  - 複雑なグリッドレイアウトとボタン
  - 多数の toctree ディレクティブ

### 2. ペルソナページ
- **新規チーム**: `docs/source/persona_pages/rookie_teams/rookie_teams.rst`
- **既存チーム**: `docs/source/persona_pages/veteran_teams/veteran_teams.rst`
- **コーチ**: `docs/source/persona_pages/coach_admin/coach_admin.rst`
- **メンター**: `docs/source/persona_pages/mentor_tech/mentor_tech.rst`

**理由**: 
- 複雑なグリッドレイアウトとボタンディレクティブ
- ユーザーの最初の接点となる重要なページ
- 構造の崩れが UX に直接影響

## 技術的な実装

### .po ファイルの無効化

手動翻訳されているページの .po ファイルは、ヘッダーのみで msgid/msgstr ペアを含まない
空のファイルになっています。これにより：

1. Sphinx はこれらのページの翻訳を .po ファイルから取得しようとしない
2. 代わりに、RST ファイルの内容がそのまま使用される

### バックアップファイル

オリジナルの英語版は `.en.rst` という拡張子でバックアップされています：

- `index.en.rst`
- `rookie_teams.en.rst`
- `veteran_teams.en.rst`
- `coach_admin.en.rst`
- `mentor_tech.en.rst`

これにより、必要に応じて元の内容を参照できます。

## ビルドプロセス

### 日本語ビルド

```bash
cd docs
make html-ja
```

このコマンドは：
1. Sphinx に `language=ja` を設定
2. 手動翻訳されているページは RST から直接ビルド
3. その他のページは .po ファイルから翻訳を適用

### 自動ビルド（開発用）

```bash
cd docs
make autobuild-ja
```

ファイルの変更を監視し、自動的に再ビルドします。

## 警告ノートについて

トップページ（`index.rst`）の先頭に以下の警告が表示されます：

```rst
.. warning::
   **⚠️ 重要な注意事項**
   
   このドキュメントは **非公式の日本語翻訳** です。
   
   * 本翻訳は有志による非公式なものであり、FIRST® の公式ドキュメントではありません
   * AI翻訳（ローカルLLM）を使用しているため、不正確な翻訳や構造の崩れがある可能性があります
   * 現在、順次修正を進めています
   * **正確な情報については、必ず英語の公式ドキュメントをご確認ください**: https://ftc-docs.firstinspires.org
   
   翻訳の改善にご協力いただける方は、GitHubリポジトリまでお問い合わせください。
```

この警告は：
- ユーザーに非公式翻訳であることを明確に伝える
- AI翻訳の使用を透明化
- 公式ドキュメントへの参照を促す

## 翻訳問題トラッカー

手動での問題修正を支援するため、ブラウザベースの問題トラッカーを提供しています。

### 使用方法

1. ビルドしたドキュメントの `_static/issue_tracker.html` を開く
2. ドキュメントを読みながら、問題を記録
3. JSON または Markdown 形式でエクスポート

詳細は `ISSUE_TRACKER_GUIDE.md` を参照してください。

## 今後の作業

### 手動翻訳ページの改善

手動翻訳されているページについて：
- [ ] 翻訳の品質をさらに向上
- [ ] リンクの動作確認
- [ ] スタイルの統一

### .po ファイル翻訳の改善

その他のページについて：
- [ ] 問題トラッカーで収集した問題を修正
- [ ] 重要なページから順次手動レビュー
- [ ] 必要に応じて追加のページを手動翻訳に移行

## トラブルシューティング

### ビルドエラーが発生する

1. 依存関係をインストール: `cd docs && pip install -r requirements.txt`
2. クリーンビルド: `make clean && make html-ja`

### 翻訳が反映されない

1. .mo ファイルを削除: `find locales -name "*.mo" -delete`
2. 再ビルド: `make html-ja`

### 手動翻訳ページを元に戻したい

1. `.en.rst` ファイルから `.rst` ファイルにコピー
2. 対応する .po ファイルを復元（元のバックアップから）

## 貢献ガイドライン

### 手動翻訳ページの編集

1. 該当する `.rst` ファイルを直接編集
2. RST 構造を崩さないよう注意
3. ローカルでビルドして確認: `make html-ja`
4. プルリクエストを作成

### .po ファイルの編集

1. `locales/ja/LC_MESSAGES/` 以下の該当する .po ファイルを編集
2. Poedit などのツールを使用することを推奨
3. `sphinx-intl build` で .mo ファイルを生成（またはビルド時に自動生成）
4. `make html-ja` でビルド確認
5. プルリクエストを作成

## 参考資料

- [Sphinx 国際化ドキュメント](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx-intl ドキュメント](https://sphinx-intl.readthedocs.io/)
- [reStructuredText 記法](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

## ライセンス

このドキュメントは FTC Docs 日本語版プロジェクトの一部として提供されます。
