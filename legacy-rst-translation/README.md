# 従来のRST直接翻訳システム（レガシー）

⚠️ **このディレクトリは従来のRST直接翻訳システムのドキュメントです。**

---

## 🚨 重要なお知らせ

このプロジェクトは **標準的な .po ベースの翻訳システム** に移行しました。

### 新しいシステムを使用してください

- **新規翻訳:** [../po-translation/](../po-translation/) を参照
- **クイックスタート:** [../po-translation/guides/QUICK_START.md](../po-translation/guides/QUICK_START.md)
- **AI翻訳:** [../po-translation/guides/AI_TRANSLATION_GUIDE.md](../po-translation/guides/AI_TRANSLATION_GUIDE.md)

---

## なぜ移行したのか？

### RST直接翻訳の問題点

1. **上流との同期が困難**
   - 英語版の変更を手動でマージする必要がある
   - コンフリクト解決が複雑

2. **RST構文の維持が必要**
   - 翻訳者がRST構文を理解する必要がある
   - 構文エラーが発生しやすい

3. **AI翻訳が困難**
   - ファイル全体を処理する必要がある
   - RST構文を保持しながら翻訳するのが難しい

### .po翻訳の利点

1. **上流との同期が簡単**
   - 変更が自動的に検出される
   - fuzzyフラグで確認が必要な箇所が明確

2. **翻訳に集中できる**
   - RST構文を気にする必要がない
   - 翻訳単位が明確

3. **AI翻訳に最適**
   - メッセージ単位で処理できる
   - 標準的なツールが使える

---

## このディレクトリの内容

### ドキュメント（参考用）

従来のRST直接翻訳に関するドキュメントは `docs-ja/` ディレクトリに残されています：

- **docs-ja/guides/AI_TRANSLATION_GUIDE.md** - RST翻訳用のAIガイド
- **docs-ja/reference/GLOSSARY.md** - 用語集（.po翻訳でも使用）
- **docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md** - RSTエラー解決ガイド

### スクリプト（従来のツール）

`docs/scripts/` には、従来のRST翻訳で使用されていたツールが残されています：

```bash
# RST構文チェック
python docs/scripts/validate_rst_syntax.py

# インラインマークアップ修正
python docs/scripts/fix_rst_inline_markup.py

# 翻訳進捗チェック（RST用）
python docs/scripts/check_translation_progress.py
```

これらのツールは、ビルドエラーの解決やRSTファイルのメンテナンスに引き続き使用できます。

---

## 移行ガイド

### 既存の翻訳データ

既存のRST翻訳は **TRANSLATION_MAPPING.md** に保存されています。

### .po形式への移行

既存の翻訳を.po形式に移行するには：

```bash
# 翻訳を.poファイルに投入
python docs/scripts/populate_po_translations.py

# 結果を確認
cd docs
make ja-stats
```

詳細は以下のドキュメントを参照：
- **MIGRATION_TO_PO_GUIDE.md** - 移行の技術的詳細
- **MIGRATION_NEXT_STEPS.md** - 移行の手順

---

## 従来システムの使用（非推奨）

⚠️ **新規翻訳には使用しないでください。**

従来のRST直接翻訳システムを使用する場合（メンテナンスのみ）：

### ワークフロー

```bash
# 1. RSTファイルを直接編集
vim docs/source/index.rst

# 2. ビルド
cd docs
make html

# 3. プレビュー
python -m http.server 8000 --directory build/html
```

### 問題点

- 上流の変更を手動でマージする必要がある
- RST構文エラーが発生しやすい
- AI翻訳が困難

---

## 新システムへの完全移行

プロジェクトは段階的に.po翻訳システムに移行しています。

### 移行状況

- ✅ .po翻訳システムのセットアップ完了
- ✅ 既存翻訳のスキャン完了
- ✅ 翻訳マッピングの抽出完了
- ✅ .poファイルへの初期投入完了（30.1%）
- ⏳ 残りの翻訳を段階的に追加中

### 今後の計画

1. **Phase 1:** 重要なページを優先的に.po翻訳
2. **Phase 2:** すべてのページを.po形式に移行
3. **Phase 3:** 従来のRST翻訳ドキュメントをアーカイブ

---

## サポート

### 新システムに関する質問

- **クイックスタート:** [../po-translation/guides/QUICK_START.md](../po-translation/guides/QUICK_START.md)
- **FAQ:** [../po-translation/README.md](../po-translation/README.md)
- **Issue:** GitHub Issues

### 従来システムに関する質問

- **docs-ja/README.md** - 従来システムの概要
- **docs-ja/guides/AI_TRANSLATION_GUIDE.md** - RST翻訳ガイド

---

## 関連ドキュメント

### 移行関連

- **MIGRATION_TO_PO_GUIDE.md** - .po移行の技術ガイド
- **MIGRATION_NEXT_STEPS.md** - 移行の次のステップ
- **WHY_PO_TRANSLATION.md** - なぜ移行するのか
- **COMPARISON_OLD_VS_NEW.md** - 新旧システムの比較

### 作業記録

- **MIGRATION_COMPLETION_SUMMARY.md** - 移行完了サマリー
- **PO_POPULATION_SUMMARY.md** - .po初期投入サマリー
- **TRANSLATION_MAPPING.md** - 既存翻訳のマッピング

---

## まとめ

- ⚠️ **このシステムは非推奨です**
- ✅ **新規翻訳には .po システムを使用してください**
- 📚 **移行ガイドを参照してください**

**[../po-translation/](../po-translation/) で新しい翻訳システムを始めましょう！**
