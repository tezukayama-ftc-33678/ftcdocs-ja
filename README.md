# FIRST Tech Challenge ドキュメントプロジェクト（日本語翻訳版）
=====================================================

![ビルド](https://readthedocs.com/projects/first-tech-challenge-ftcdocs/badge/?version=latest) ![リンクチェック](https://github.com/FIRST-Tech-Challenge/ftcdocs/actions/workflows/link-check.yaml/badge.svg)

本リポジトリは、 **FIRST Tech Challenge 公式ドキュメント**の非公式日本語翻訳プロジェクトです。

---

## ⚠️ 非公式な翻訳と免責事項（重要）

**本プロジェクトは、FIRST Tech Challenge (FIRST®) の公式ドキュメントではありません。**

* この日本語翻訳は、日本のFTCコミュニティのために **[Team 33678 Tezukayama]** が自主的に運営・提供しているものです。
* 翻訳の正確性には努めていますが、**公式な情報源としては必ず英語のオリジナルドキュメントを参照してください。**
* 本翻訳の使用により生じたいかなる損害についても、本プロジェクトの貢献者および運営者は一切の責任を負いません。

公式ウェブサイト（英語原文）：
https://ftc-docs.firstinspires.org

---

## 貢献について

私たちは、FTC Docs の改善にご協力いただける方を常に求めています。

貢献に関する詳細情報については、公式 FTC Docs の [貢献セクション](https://ftc-docs.firstinspires.org/contrib/index.html) を参照してください。
（この翻訳プロジェクトへの貢献方法については、別途[CONTRIBUTING.mdなどのリンク]を参照してください。）

---

## 📚 翻訳システム

このプロジェクトは **標準的な .po ベースの翻訳システム** を使用しています。

---

## 🚀 翻訳を始める

### 📖 新規翻訳者向け（推奨）

翻訳作業のすべてのドキュメントは **[po-translation/](po-translation/)** ディレクトリに整理されています。

**🎯 最初に読むべきドキュメント:**

1. **[po-translation/README.md](po-translation/README.md)** - .po翻訳システムの概要
2. **[po-translation/guides/QUICK_START.md](po-translation/guides/QUICK_START.md)** - 15分で始める
3. **[po-translation/guides/AI_TRANSLATION_GUIDE.md](po-translation/guides/AI_TRANSLATION_GUIDE.md)** - AI翻訳の活用

### ⚡ クイックスタート

```bash
# 1. 依存関係をインストール
cd docs
pip install -r requirements.txt

# 2. 翻訳可能文字列を抽出
make gettext

# 3. 日本語.poファイルを生成/更新
make ja-update

# 4. .poファイルを編集して翻訳
vim locale/ja/LC_MESSAGES/index.po

# 5. 日本語版をビルド
make ja-build

# 6. プレビュー
python -m http.server 8000 --directory build/html/ja
```

詳細は [po-translation/guides/QUICK_START.md](po-translation/guides/QUICK_START.md) を参照。

---

## 📁 ディレクトリ構成

```
ftcdocs-ja/
├── po-translation/              # .po翻訳システム（現行）
│   ├── README.md               # システム概要
│   ├── guides/                 # 翻訳ガイド
│   │   ├── QUICK_START.md     # クイックスタート
│   │   ├── AI_TRANSLATION_GUIDE.md  # AI翻訳ガイド
│   │   └── WORKFLOW.md        # 日常的なワークフロー
│   ├── scripts/                # 翻訳支援スクリプト
│   │   ├── ai_translate_po.py # AI翻訳支援ツール
│   │   └── check_po_quality.py # 品質チェックツール
│   └── reference/              # リファレンス
│       ├── GLOSSARY.md        # 用語集
│       └── COMMANDS.md        # コマンドリファレンス
│
├── docs/                        # Sphinxドキュメント
│   ├── source/                 # 英語RST（上流と同期）
│   ├── locale/ja/LC_MESSAGES/  # 日本語.poファイル
│   └── scripts/                # ビルド支援スクリプト
│
├── docs-ja/                     # 従来のドキュメント（参考用）
├── legacy-rst-translation/      # 従来のRST翻訳（非推奨）
└── README.md                    # このファイル
```

---

## 🤖 AI翻訳支援

このプロジェクトは、AI翻訳ツールとの統合を前提に設計されています。

### 対応ツール

- DeepL API
- OpenAI API (ChatGPT/GPT-4)
- Anthropic API (Claude)
- ローカルLLM (Ollama等)

### AI翻訳スクリプト

```bash
# 未翻訳エントリをAIで翻訳
python po-translation/scripts/ai_translate_po.py \
  docs/locale/ja/LC_MESSAGES/index.po \
  --dry-run

# 翻訳品質をチェック
python po-translation/scripts/check_po_quality.py \
  docs/locale/ja/LC_MESSAGES/
```

詳細は [po-translation/guides/AI_TRANSLATION_GUIDE.md](po-translation/guides/AI_TRANSLATION_GUIDE.md) を参照。

---

## 📖 主要ドキュメント

### 翻訳ガイド

- **[po-translation/guides/QUICK_START.md](po-translation/guides/QUICK_START.md)** - 15分で始める.po翻訳
- **[po-translation/guides/AI_TRANSLATION_GUIDE.md](po-translation/guides/AI_TRANSLATION_GUIDE.md)** - AI翻訳の完全ガイド
- **[po-translation/guides/WORKFLOW.md](po-translation/guides/WORKFLOW.md)** - 日常的な翻訳ワークフロー

### リファレンス

- **[po-translation/reference/GLOSSARY.md](po-translation/reference/GLOSSARY.md)** - 用語集（92語）
- **[po-translation/reference/COMMANDS.md](po-translation/reference/COMMANDS.md)** - コマンドリファレンス
- **[docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md](docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md)** - RSTエラー解決ガイド

### 移行関連（参考）

- **[legacy-rst-translation/README.md](legacy-rst-translation/README.md)** - 従来システムについて
- **[legacy-rst-translation/archive/](legacy-rst-translation/archive/)** - 移行ドキュメント

---

## 📊 翻訳進捗

```bash
# 翻訳統計を表示
cd docs
make ja-stats

# 詳細な品質レポートを生成
python ../po-translation/scripts/check_po_quality.py \
  locale/ja/LC_MESSAGES/ \
  --report quality_report.md
```

---

## 🛠️ 翻訳支援ツール

### .po翻訳用（推奨）

```bash
# AI翻訳支援
python po-translation/scripts/ai_translate_po.py FILE.po

# 品質チェック
python po-translation/scripts/check_po_quality.py DIRECTORY/
```

### RST検証用（ビルドエラー解決に使用）

```bash
# RST構文検証
python docs/scripts/validate_rst_syntax.py

# インラインマークアップ自動修正
python docs/scripts/fix_rst_inline_markup.py

# ビルド警告解析
python docs/scripts/check_build_warnings.py
```
