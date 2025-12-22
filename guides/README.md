# ガイド一覧

このディレクトリには、FTC日本語ドキュメントプロジェクトに関する各種ガイドが含まれています。

## 📖 公開・ライセンス関連

### 🚀 [PUBLISHING.md](../PUBLISHING.md)
**Read the Docsでの公開手順**
- Read the Docsプロジェクトの設定方法
- ビルド設定の詳細
- カスタムドメインの設定
- トラブルシューティング

👉 **Read the Docsで公開したい方は、まずこちらをご覧ください！**

### 📜 [LICENSE_AND_LOGO_GUIDE.md](LICENSE_AND_LOGO_GUIDE.md)
**ライセンスとロゴ使用に関するFAQ**
- 法的に問題ないか？
- FIRSTのロゴは使えるか？
- 記事内の権利表記はどうする？
- 商標表記は必要か？

👉 **ライセンスやロゴについて疑問がある方は、まずこちらをご覧ください！**

### 📄 [LICENSE-JA.md](../LICENSE-JA.md)
**翻訳版のライセンスと免責事項**
- 原文のライセンス情報
- 翻訳版の位置づけ
- 重要な注意事項
- 使用条件

## 🤖 翻訳関連

### ⚡ [AUTO_TRANSLATE.md](AUTO_TRANSLATE.md)
**ローカルLLMによる自動翻訳**
- Ollamaを使った自動翻訳の詳細手順
- モデルの選択とインストール
- バッチ翻訳の実行方法

### 🚀 [AUTO_TRANSLATE_QUICKSTART.md](AUTO_TRANSLATE_QUICKSTART.md)
**自動翻訳クイックスタート**
- 3ステップで始める自動翻訳
- 最小限の手順で翻訳を開始

### 📝 [TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md)
**翻訳ガイドライン**
- 翻訳の基本方針
- 用語の統一
- 品質管理

### 📚 [GLOSSARY.md](GLOSSARY.md)
**用語集**
- FTC用語の日本語訳
- 技術用語の対訳表
- 統一すべき表記

### 🔄 [TRANSLATION_APPROACH.md](TRANSLATION_APPROACH.md)
**翻訳アプローチの説明**
- POファイル翻訳とRST直接翻訳の使い分け
- ハイブリッド翻訳戦略

## 🔧 修正・メンテナンス関連

### 🔍 [TRANSLATION_REFLECTION_FIX.md](TRANSLATION_REFLECTION_FIX.md) ⭐ NEW
**翻訳未反映問題の検出・修正**
- 日本語翻訳があるのに表示されない問題の特定
- ビルド警告の分析と優先順位付け
- 日本語ラベル/パス参照の修正方法
- 自動修正ツールの使用方法

👉 **日本語を書いたのに反映されていない場合は、まずこちらをご覧ください！**

### 🛠️ [ERROR_FIX_GUIDE.md](ERROR_FIX_GUIDE.md)
**エラー修正ガイド**
- Sphinxビルドエラーの修正方法
- よくあるエラーと解決策

### 📝 [PO_SYNTAX_FIX_GUIDE.md](PO_SYNTAX_FIX_GUIDE.md)
**PO構文修正ガイド**
- POファイルの構文エラー修正
- 自動修正ツールの使い方

### ⚡ [QUICK_FIX_GUIDE.md](QUICK_FIX_GUIDE.md)
**クイック修正ガイド**
- よくある問題の素早い解決方法
- チートシート形式

### 🔍 [FIX_CHINESE_ERRORS.md](FIX_CHINESE_ERRORS.md)
**中国語文字エラーの修正**
- 誤った中国語文字の検出と修正
- 自動修正スクリプト

## 🏗️ ビルド関連

### 🔨 [BUILD_JA.md](BUILD_JA.md)
**日本語版ビルドガイド**
- ローカルでのビルド方法
- 必要な依存関係
- ビルドコマンド

### 🚀 [EXECUTE_GUIDE.md](EXECUTE_GUIDE.md)
**実行ガイド**
- 各種スクリプトの実行方法
- ツールの使い方

## 🔧 環境構築

### 🖥️ [LOCAL_LLM_SETUP.md](LOCAL_LLM_SETUP.md)
**ローカルLLM環境のセットアップ**
- Ollamaのインストール
- LLMモデルのダウンロード
- トラブルシューティング

## 📊 使い方の流れ

### 初めて翻訳に取り組む方

```
1. [QUICKSTART.md](../QUICKSTART.md) を読む
2. [AUTO_TRANSLATE_QUICKSTART.md](AUTO_TRANSLATE_QUICKSTART.md) で自動翻訳を試す
3. [TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md) で翻訳方針を理解
4. [BUILD_JA.md](BUILD_JA.md) でローカルビルドを確認
```

### 翻訳を改善したい方

```
1. [GLOSSARY.md](GLOSSARY.md) で用語を確認
2. [TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md) でガイドラインを確認
3. POファイルを編集
4. [BUILD_JA.md](BUILD_JA.md) でビルドして確認
```

### エラーを修正したい方

```
1. [ERROR_FIX_GUIDE.md](ERROR_FIX_GUIDE.md) でエラータイプを確認
2. [PO_SYNTAX_FIX_GUIDE.md](PO_SYNTAX_FIX_GUIDE.md) でPOエラーを修正
3. [QUICK_FIX_GUIDE.md](QUICK_FIX_GUIDE.md) で素早く解決
```

### Read the Docsで公開したい方

```
1. [LICENSE_AND_LOGO_GUIDE.md](LICENSE_AND_LOGO_GUIDE.md) でライセンスを確認 ⭐
2. [PUBLISHING.md](../PUBLISHING.md) で公開手順を実施 ⭐
3. Read the Docsでビルドを確認
```

## 📚 その他のドキュメント

### プロジェクトルート
- [README.md](../README.md) - プロジェクト概要
- [QUICKSTART.md](../QUICKSTART.md) - 5分で始めるクイックスタート
- [LICENSE](../LICENSE) - 原文のBSD 3-Clause License
- [LICENSE-JA.md](../LICENSE-JA.md) - 翻訳版のライセンス説明
- [PUBLISHING.md](../PUBLISHING.md) - Read the Docs公開手順

### ツール
- [tools/README.md](../tools/README.md) - 各種ツールの説明
- [tools/translation/](../tools/translation/) - 自動翻訳ツール
- [tools/po-fixing/](../tools/po-fixing/) - PO修正ツール
- [tools/analysis/](../tools/analysis/) - 分析ツール

## 💡 Tips

### ドキュメントの検索

特定の情報を探すときは：
```bash
# guides内を検索
grep -r "キーワード" guides/

# プロジェクト全体を検索
grep -r "キーワード" .
```

### よくある質問

**Q: どのガイドから読めば良い？**
- **初めての方**: QUICKSTART.md → AUTO_TRANSLATE_QUICKSTART.md
- **公開したい方**: LICENSE_AND_LOGO_GUIDE.md → PUBLISHING.md
- **エラー修正**: ERROR_FIX_GUIDE.md

**Q: ガイドが多すぎて迷う**
- **最優先**: README.md、QUICKSTART.md
- **公開関連**: PUBLISHING.md、LICENSE_AND_LOGO_GUIDE.md
- **翻訳関連**: AUTO_TRANSLATE.md、TRANSLATION_GUIDE.md
- **困ったとき**: ERROR_FIX_GUIDE.md、QUICK_FIX_GUIDE.md

**Q: ガイドに載っていない情報を知りたい**
- GitHubのIssuesで質問
- ツールのREADMEを確認
- プロジェクトドキュメント (docs/project-docs/) を参照

## 🤝 貢献

ガイドの改善提案やバグ報告は、GitHubのIssuesやPull Requestsでお願いします。

---

**目的別クイックリンク:**
- 🚀 **すぐに始めたい** → [QUICKSTART.md](../QUICKSTART.md)
- 📖 **公開したい** → [PUBLISHING.md](../PUBLISHING.md) ⭐
- 📜 **ライセンスが心配** → [LICENSE_AND_LOGO_GUIDE.md](LICENSE_AND_LOGO_GUIDE.md) ⭐
- 🤖 **自動翻訳したい** → [AUTO_TRANSLATE.md](AUTO_TRANSLATE.md)
- 🛠️ **エラーを直したい** → [ERROR_FIX_GUIDE.md](ERROR_FIX_GUIDE.md)
