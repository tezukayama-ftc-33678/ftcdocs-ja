# クイックスタートガイド

## 🚀 5分で始める FTC Docs 日本語版

### 1. ビルド環境のセットアップ

```bash
# リポジトリをクローン
git clone https://github.com/tezukayama-ftc-33678/ftcdocs-ja.git
cd ftcdocs-ja

# 依存パッケージをインストール
cd docs
pip install -r requirements.txt
```

### 2. 日本語ドキュメントをビルド

```bash
# ワンコマンドでビルド
make html-ja
```

成功すると、`docs/build/html-ja/` にドキュメントが生成されます。

### 3. ドキュメントを開く

```bash
# ブラウザで開く（Mac/Linux）
open docs/build/html-ja/index.html

# Windows の場合
start docs/build/html-ja/index.html
```

### 4. 問題トラッカーを使う

```bash
# 問題トラッカーを開く
open docs/build/html-ja/_static/issue_tracker.html
```

ドキュメントを読みながら、おかしい箇所を記録していきましょう！

## 📝 翻訳を編集する

### 手動翻訳ページ（重要なページ）

以下のページは RST ファイルを直接編集します：

```bash
# 編集
vim docs/source/index.rst
vim docs/source/persona_pages/rookie_teams/rookie_teams.rst
# ... など

# ビルドして確認
cd docs
make html-ja
```

### .po ファイルで翻訳（その他のページ）

```bash
# Poedit などのツールで編集
poedit locales/ja/LC_MESSAGES/path/to/file.po

# またはテキストエディタで直接編集
vim locales/ja/LC_MESSAGES/path/to/file.po

# ビルドして確認
cd docs
make html-ja
```

## 🔄 自動ビルド（開発用）

ファイルの変更を監視して、自動的に再ビルド：

```bash
cd docs
make autobuild-ja

# ブラウザが自動で開き、http://localhost:7351 でアクセス可能
# ファイルを編集すると自動的にリロードされます
```

## 🐛 よくある問題

### ビルドエラーが出る

```bash
# 依存パッケージを再インストール
cd docs
pip install -r requirements.txt --upgrade

# クリーンビルド
make clean
make html-ja
```

### 翻訳が反映されない

```bash
# .mo ファイルを削除して再ビルド
find locales -name "*.mo" -delete
cd docs
make html-ja
```

### 問題トラッカーでデータが消えた

- ブラウザのプライベートモードを使っていませんか？
  → 通常モードで開いてください
  
- ブラウザのキャッシュをクリアしましたか？
  → 定期的にエクスポートしてバックアップしてください

## 📚 詳細ドキュメント

さらに詳しい情報は以下のドキュメントを参照してください：

- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - 実装の完全な説明
- **[TRANSLATION_APPROACH.md](TRANSLATION_APPROACH.md)** - 翻訳方法の詳細
- **[ISSUE_TRACKER_GUIDE.md](ISSUE_TRACKER_GUIDE.md)** - 問題トラッカーの使い方

## 💡 ヒント

### 効率的な翻訳ワークフロー

1. **ドキュメントを読む**: まず全体を通して読む
2. **問題を記録**: 問題トラッカーで気づいた問題を記録
3. **優先順位付け**: 重要度の高い問題から修正
4. **修正と確認**: 修正してビルドで確認
5. **エクスポート**: 定期的に問題リストをエクスポート

### Git ワークフロー

```bash
# 新しいブランチを作成
git checkout -b fix/translation-improvements

# 変更をコミット
git add .
git commit -m "翻訳の改善: トップページの誤字を修正"

# プッシュ
git push origin fix/translation-improvements
```

## 🆘 サポート

問題が解決しない場合：

1. GitHub の Issue を検索
2. 該当する Issue がなければ新規作成
3. エラーメッセージやスクリーンショットを添付

---

Happy Translating! 🎉
