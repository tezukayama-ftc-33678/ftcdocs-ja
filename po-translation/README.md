# .po ベース翻訳システム

このディレクトリには、**標準的な .po ベースの翻訳システム**に関するすべてのドキュメントとツールが含まれています。

## 📁 ディレクトリ構成

```
po-translation/
├── README.md                 # このファイル
├── guides/                   # 翻訳ガイド
│   ├── QUICK_START.md       # クイックスタート
│   ├── AI_TRANSLATION_GUIDE.md  # AI翻訳ガイド（.po用）
│   └── WORKFLOW.md          # 日常的なワークフロー
├── scripts/                  # 翻訳支援スクリプト
│   ├── ai_translate_po.py   # AI翻訳支援ツール
│   └── check_po_quality.py  # 品質チェックツール
└── reference/                # リファレンス
    ├── PO_FORMAT.md         # .poファイル形式の説明
    ├── GLOSSARY.md          # 用語集
    └── COMMANDS.md          # コマンドリファレンス
```

## 🚀 はじめに

### 推奨する読む順序

1. **[QUICK_START.md](guides/QUICK_START.md)** - 最初に読む
   - 15分で理解できる .po 翻訳の基本
   - すぐに始められるコマンド集

2. **[AI_TRANSLATION_GUIDE.md](guides/AI_TRANSLATION_GUIDE.md)** - AI翻訳を使う場合
   - AI翻訳ツール（DeepL、ChatGPT、Claude等）向けの指示書
   - .po 形式での翻訳ルールとベストプラクティス

3. **[WORKFLOW.md](guides/WORKFLOW.md)** - 日常的な作業
   - 上流の変更を取り込む方法
   - 翻訳を追加・更新する方法
   - ビルドとプレビューの方法

## ⚡ クイックスタート

### 環境セットアップ

```bash
# 依存関係のインストール
cd docs
pip install -r requirements.txt
```

### 基本的なワークフロー

```bash
# 1. 翻訳可能な文字列を抽出（英語RSTから.potファイルを生成）
cd docs
make gettext

# 2. 日本語.poファイルを更新
make ja-update

# 3. .poファイルを編集して翻訳
#    エディタで docs/locale/ja/LC_MESSAGES/*.po を開く

# 4. 日本語版をビルド
make ja-build

# 5. プレビュー
python -m http.server 8000 --directory build/html/ja
# ブラウザで http://localhost:8000 を開く
```

### AI翻訳支援ツールを使う

```bash
# 未翻訳のエントリをAIで翻訳
python po-translation/scripts/ai_translate_po.py docs/locale/ja/LC_MESSAGES/index.po

# 翻訳品質をチェック
python po-translation/scripts/check_po_quality.py docs/locale/ja/LC_MESSAGES/
```

## 📚 主要コマンド

| コマンド | 説明 |
|---------|------|
| `make gettext` | 英語RSTから翻訳可能文字列を抽出 |
| `make ja-update` | .poファイルを最新の.potに基づいて更新 |
| `make ja-build` | 日本語版HTMLをビルド |
| `make ja-stats` | 翻訳進捗を表示 |

詳細は [reference/COMMANDS.md](reference/COMMANDS.md) を参照。

## 🤖 AI翻訳について

このシステムは、AI翻訳ツールとの統合を前提に設計されています：

### 対応ツール
- DeepL API
- OpenAI API (ChatGPT/GPT-4)
- Anthropic API (Claude)
- ローカルLLM (Ollama等)

### AI翻訳の利点
- **.po形式は翻訳単位が明確** - 各エントリが独立している
- **文脈を保持しやすい** - 元のRST構造を気にする必要がない
- **一貫性の維持** - 用語集とルールをAIに与えやすい
- **バッチ処理が可能** - 複数ファイルを効率的に処理

詳細は [guides/AI_TRANSLATION_GUIDE.md](guides/AI_TRANSLATION_GUIDE.md) を参照。

## 🔄 従来のRST直接翻訳からの移行

従来のRST直接翻訳システムから移行する場合は、`../legacy-rst-translation/` ディレクトリのドキュメントを参照してください。

**重要な違い:**

| 項目 | RST直接翻訳 | .po翻訳 |
|-----|------------|--------|
| 編集対象 | RSTファイル | .poファイル |
| 上流との同期 | 手動マージ（困難） | 自動更新 |
| 翻訳単位 | ファイル全体 | メッセージ単位 |
| ツール | テキストエディタ | Poedit/テキストエディタ |
| AI翻訳 | 困難（RST構文の維持が必要） | 容易（構造が明確） |

## 📖 詳細ドキュメント

### ガイド (guides/)
- **QUICK_START.md** - 15分で始める.po翻訳
- **AI_TRANSLATION_GUIDE.md** - AI翻訳の完全ガイド
- **WORKFLOW.md** - 日常的な翻訳ワークフロー

### リファレンス (reference/)
- **PO_FORMAT.md** - .poファイルの構造と仕様
- **GLOSSARY.md** - 翻訳用語集
- **COMMANDS.md** - makeコマンドとツールのリファレンス

### スクリプト (scripts/)
- **ai_translate_po.py** - AI翻訳支援ツール
- **check_po_quality.py** - 翻訳品質チェックツール

## 💡 よくある質問

**Q: 既存の翻訳はどうなりますか？**  
A: TRANSLATION_MAPPING.md に保存されており、`docs/scripts/populate_po_translations.py` で.poファイルに移行できます。

**Q: 全部を一度に移行する必要がありますか？**  
A: いいえ、段階的に移行できます。空の msgstr は英語のまま表示されます。

**Q: RSTの知識は必要ですか？**  
A: .poファイルの翻訳にはRSTの知識は不要です。ただし、ビルド時のエラー解決には役立ちます。

**Q: どのツールを使うべきですか？**  
A: 初心者には [Poedit](https://poedit.net/)、開発者にはVS Code + i18n Ally、AI自動翻訳には提供スクリプトを推奨します。

## 🆘 サポート

- 質問: GitHub Issues
- ドキュメント: このディレクトリ内の各ガイド
- 従来システム: `../legacy-rst-translation/` を参照

---

**このシステムは、標準的な gettext/.po フォーマットを使用しており、多くの翻訳ツールやワークフローと互換性があります。**
