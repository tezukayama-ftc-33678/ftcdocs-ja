# FTC日本語翻訳プロジェクト - ドキュメントガイド

このドキュメントは、プロジェクト内のすべてのドキュメントへのナビゲーションガイドです。

---

## 🎯 目的別ガイド

### 翻訳を始めたい

👉 **[po-translation/guides/QUICK_START.md](po-translation/guides/QUICK_START.md)**

15分で.po翻訳を始められます。

### AI翻訳を使いたい

👉 **[po-translation/guides/AI_TRANSLATION_GUIDE.md](po-translation/guides/AI_TRANSLATION_GUIDE.md)**

DeepL、ChatGPT、Claude等のAI翻訳ツールの使い方。

### 実践的な翻訳作業を始めたい

👉 **[TRANSLATION_WORKFLOW.md](TRANSLATION_WORKFLOW.md)**

残りの未翻訳エントリを効率的に翻訳する実践的ワークフロー。

### 日常的な翻訳作業をしたい

👉 **[po-translation/guides/WORKFLOW.md](po-translation/guides/WORKFLOW.md)**

上流の変更取り込み、翻訳追加、ビルドまでの完全なワークフロー。

### コマンドを調べたい

👉 **[po-translation/reference/COMMANDS.md](po-translation/reference/COMMANDS.md)**

make、msgfmt、git等のコマンドリファレンス。

### .poファイルの形式を知りたい

👉 **[po-translation/reference/PO_FORMAT.md](po-translation/reference/PO_FORMAT.md)**

.poファイルの構造と仕様の詳細説明。

### 用語の翻訳を統一したい

👉 **[po-translation/reference/GLOSSARY.md](po-translation/reference/GLOSSARY.md)**

技術用語、製品名等の統一リスト（92語）。

### RSTのエラーを解決したい

👉 **[docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md](docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md)**

RSTビルドエラーの解決方法。

### 従来システムについて知りたい

👉 **[legacy-rst-translation/README.md](legacy-rst-translation/README.md)**

RST直接翻訳システム（非推奨）の説明。

---

## 📁 ディレクトリ構造

```
ftcdocs-ja/
│
├── README.md                    # プロジェクト全体の概要
├── DOCUMENTATION_GUIDE.md       # このファイル（ドキュメントナビゲーション）
├── TRANSLATION_WORKFLOW.md      # 実践的な翻訳ワークフロー
│
├── po-translation/              # 【推奨】.po翻訳システム
│   ├── README.md               # システム概要
│   ├── guides/                 # 翻訳ガイド
│   │   ├── QUICK_START.md     # 15分で始める
│   │   ├── AI_TRANSLATION_GUIDE.md  # AI翻訳ガイド
│   │   └── WORKFLOW.md        # 日常的なワークフロー
│   ├── scripts/                # 翻訳支援スクリプト
│   │   ├── ai_translate_po.py # AI翻訳支援
│   │   └── check_po_quality.py # 品質チェック
│   └── reference/              # リファレンス
│       ├── GLOSSARY.md        # 用語集
│       ├── COMMANDS.md        # コマンドリファレンス
│       └── PO_FORMAT.md       # .poファイル形式
│
├── docs/                        # Sphinxドキュメント
│   ├── source/                 # 英語RSTファイル
│   ├── locale/ja/LC_MESSAGES/  # 日本語.poファイル
│   ├── scripts/                # ビルド支援スクリプト
│   ├── Makefile                # ビルドコマンド
│   └── requirements.txt        # Python依存関係
│
├── docs-ja/                     # 従来のドキュメント（参考用）
│   ├── README.md
│   ├── guides/                 # 翻訳ガイド
│   ├── reference/              # リファレンス
│   └── archive/                # 過去の作業記録
│
└── legacy-rst-translation/      # 【非推奨】従来システム
    ├── README.md               # 非推奨システムの説明
    └── archive/                # 移行関連ドキュメント
```

---

## 📚 ドキュメント一覧

### po-translation/ （現行システム）

#### ガイド (guides/)

| ファイル | 説明 | 対象 |
|---------|------|------|
| **QUICK_START.md** | 15分で始める.po翻訳 | 初心者 |
| **AI_TRANSLATION_GUIDE.md** | AI翻訳の完全ガイド | AI使用者 |
| **WORKFLOW.md** | 日常的な翻訳ワークフロー | 全員 |

#### リファレンス (reference/)

| ファイル | 説明 | 用途 |
|---------|------|------|
| **GLOSSARY.md** | 用語集（92語） | 翻訳時の参照 |
| **COMMANDS.md** | コマンドリファレンス | コマンド確認 |
| **PO_FORMAT.md** | .poファイル形式の詳細 | 高度な編集 |

#### スクリプト (scripts/)

| ファイル | 説明 | 使い方 |
|---------|------|--------|
| **ai_translate_po.py** | AI翻訳支援ツール | `python ai_translate_po.py FILE.po --dry-run` |
| **check_po_quality.py** | 品質チェックツール | `python check_po_quality.py DIR/` |

---

### docs-ja/ （参考用）

#### リファレンス (reference/)

| ファイル | 説明 | 用途 |
|---------|------|------|
| **RST_TROUBLESHOOTING_GUIDE.md** | RSTエラー解決ガイド | ビルドエラー対応 |
| **TRANSLATION_ROADMAP.md** | 翻訳ロードマップ | 進捗管理 |
| **TRANSLATION_PROGRESS.md** | 翻訳進捗状況 | 進捗確認 |

---

### docs/scripts/ （ビルド支援）

| ファイル | 説明 | 使い方 |
|---------|------|--------|
| **validate_rst_syntax.py** | RST構文検証 | `python validate_rst_syntax.py` |
| **fix_rst_inline_markup.py** | インラインマークアップ修正 | `python fix_rst_inline_markup.py` |
| **check_build_warnings.py** | ビルド警告解析 | `python check_build_warnings.py` |
| **populate_po_translations.py** | 既存翻訳を.poに投入 | `python populate_po_translations.py` |

---

### legacy-rst-translation/ （非推奨）

| ファイル | 説明 |
|---------|------|
| **README.md** | 従来システムの説明と移行案内 |
| **archive/** | 移行関連ドキュメント |

---

## 🚀 よくある作業フロー

### 1. 初めて翻訳する

```
1. po-translation/guides/QUICK_START.md を読む
2. 環境セットアップ (pip install -r docs/requirements.txt)
3. make gettext && make ja-update
4. .poファイルを編集
5. make ja-build
```

### 2. AI翻訳を使う

```
1. po-translation/guides/AI_TRANSLATION_GUIDE.md を読む
2. python po-translation/scripts/ai_translate_po.py FILE.po --dry-run
3. （必要に応じてAPI設定）
4. 翻訳結果をレビュー
5. make ja-build
```

### 3. 翻訳を更新する

```
1. git fetch upstream && git merge upstream/main
2. po-translation/guides/WORKFLOW.md の手順に従う
3. make gettext && make ja-update
4. fuzzyエントリを確認・修正
5. make ja-build
```

### 4. エラーを解決する

```
1. エラーメッセージを確認
2. docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md を参照
3. 必要に応じて docs/scripts/ のツールを使用
4. make clean && make ja-build
```

### 5. 品質をチェックする

```
1. python po-translation/scripts/check_po_quality.py docs/locale/ja/LC_MESSAGES/
2. レポートを確認
3. 問題箇所を修正
4. 再度チェック
```

---

## 💡 Tips

### 翻訳の一貫性を保つ

- **用語集を参照:** po-translation/reference/GLOSSARY.md
- **過去の翻訳を検索:**
  ```bash
  grep -r "OpMode" docs/locale/ja/LC_MESSAGES/*.po | grep msgstr
  ```

### 効率的に作業する

- **エイリアスを設定:** po-translation/reference/COMMANDS.md の「便利なエイリアス」セクション
- **スクリプトを活用:** po-translation/scripts/ のツール
- **Poeditを使用:** 初心者におすすめのGUIツール

### ドキュメントを活用する

- **迷ったら:** QUICK_START.md から始める
- **コマンドを忘れた:** COMMANDS.md を参照
- **エラーが出た:** RST_TROUBLESHOOTING_GUIDE.md を確認

---

## 🔗 外部リンク

### 公式ドキュメント

- [FIRST Tech Challenge 公式](https://www.firstinspires.org/robotics/ftc)
- [FTC Docs（英語版）](https://ftc-docs.firstinspires.org/)

### 技術リソース

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [sphinx-intl](https://sphinx-intl.readthedocs.io/)
- [GNU gettext](https://www.gnu.org/software/gettext/manual/)
- [Poedit](https://poedit.net/)

---

## 📞 サポート

### 質問がある場合

1. **このガイドで目的のドキュメントを探す**
2. **該当するガイドを読む**
3. **それでも解決しない場合は GitHub Issues で質問**

### バグを見つけた場合

- GitHub Issues で報告してください

### 改善提案がある場合

- Pull Request または Issue で提案してください

---

**このガイドをブックマークして、翻訳作業の参考にしてください！**
