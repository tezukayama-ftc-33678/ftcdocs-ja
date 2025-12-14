# AI翻訳指示書

**このドキュメントは移動しました。**

---

## 🆕 新しい .po 翻訳システムをご利用ください

このプロジェクトは **標準的な .po ベースの翻訳システム** に移行しました。

### AI翻訳向けの新しいガイド

👉 **[po-translation/guides/AI_TRANSLATION_GUIDE.md](po-translation/guides/AI_TRANSLATION_GUIDE.md)**

**新しいガイドの内容:**
- ✅ .poファイル専用のAI翻訳指示プロンプト
- ✅ DeepL、ChatGPT、Claude等のAPI対応
- ✅ 翻訳ルールとベストプラクティス
- ✅ 自動化スクリプトの使い方
- ✅ 品質チェック方法

### なぜ .po 翻訳なのか？

| 項目 | RST直接翻訳 | .po翻訳 |
|-----|------------|--------|
| AI翻訳 | 困難（RST構文の維持が必要） | **容易（翻訳単位が明確）** |
| 上流との同期 | 手動マージ（困難） | **自動更新** |
| RST構文知識 | 必須 | **不要** |
| 翻訳単位 | ファイル全体 | **メッセージ単位** |

---

## 📖 クイックスタート

### 1. 環境セットアップ

```bash
cd docs
pip install -r requirements.txt
```

### 2. 翻訳可能文字列を抽出

```bash
make gettext
make ja-update
```

### 3. .poファイルを翻訳

```bash
# AIツールに以下のプロンプトを与える:
# "docs/locale/ja/LC_MESSAGES/index.po の msgstr フィールドを日本語に翻訳してください"
# 詳細なプロンプトは po-translation/guides/AI_TRANSLATION_GUIDE.md を参照

# または、自動化スクリプトを使用:
python po-translation/scripts/ai_translate_po.py \
  docs/locale/ja/LC_MESSAGES/index.po \
  --dry-run
```

### 4. ビルドして確認

```bash
make ja-build
python -m http.server 8000 --directory build/html/ja
```

---

## 📚 完全なドキュメント

### 新しい .po 翻訳システム

- **[po-translation/README.md](po-translation/README.md)** - システム概要
- **[po-translation/guides/QUICK_START.md](po-translation/guides/QUICK_START.md)** - 15分で始める
- **[po-translation/guides/AI_TRANSLATION_GUIDE.md](po-translation/guides/AI_TRANSLATION_GUIDE.md)** - AI翻訳ガイド
- **[po-translation/guides/WORKFLOW.md](po-translation/guides/WORKFLOW.md)** - 日常的なワークフロー

### リファレンス

- **[po-translation/reference/GLOSSARY.md](po-translation/reference/GLOSSARY.md)** - 用語集
- **[po-translation/reference/COMMANDS.md](po-translation/reference/COMMANDS.md)** - コマンドリファレンス
- **[po-translation/reference/PO_FORMAT.md](po-translation/reference/PO_FORMAT.md)** - .poファイル形式

---

## 🔧 従来の RST 直接翻訳（非推奨）

従来のRST直接翻訳システムのドキュメントは、以下に移動しました：

- **[legacy-rst-translation/README.md](legacy-rst-translation/README.md)** - 従来システムの説明
- **[docs-ja/guides/AI_TRANSLATION_GUIDE.md](docs-ja/guides/AI_TRANSLATION_GUIDE.md)** - RST用AIガイド（参考用）

⚠️ **新規翻訳には .po システムを使用してください。**

---

## 📖 ナビゲーションガイド

すべてのドキュメントへのナビゲーションは:

👉 **[DOCUMENTATION_GUIDE.md](DOCUMENTATION_GUIDE.md)**
