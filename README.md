# FIRST Tech Challenge ドキュメントプロジェクト（日本語翻訳版）


本リポジトリは、**FIRST Tech Challenge 公式ドキュメント**の非公式日本語翻訳プロジェクトです。
現在日本語を自然にしていく作業をしています。
我々だけでは限界があるので、誤字脱字を見つけたらGitHubのIssueやPRを投げて頂けると幸いです。

Read the docsで公開中： https://ftcdocs-ja.readthedocs.io/ja/latest/index.html

**📖 自動翻訳の始め方**: [WORKFLOW.md](WORKFLOW.md) をご覧ください！

---

## ⚠️ 非公式な翻訳と免責事項（重要）

**本プロジェクトは、FIRST Tech Challenge (FIRST®) の公式ドキュメントではありません。**

* この日本語翻訳は、日本のFTCコミュニティのために **[Team 33678 Tezukayama]** が自主的に運営・提供しているものです。
* 翻訳の正確性には努めていますが、**公式な情報源としては必ず英語のオリジナルドキュメントを参照してください。**
* 本翻訳の使用により生じたいかなる損害についても、本プロジェクトの貢献者および運営者は一切の責任を負いません。

公式ウェブサイト（英語原文）：https://ftc-docs.firstinspires.org

---



## 🚀 自動翻訳クイックスタート

### 1. ローカルLLM環境のセットアップ

```powershell
# Ollamaインストール後、モデルをダウンロード
ollama pull qwen2.5-coder:7b-instruct

# 依存パッケージをインストール
pip install polib ollama tqdm colorama
```

### 2. POファイルの翻訳

```powershell
# 単一ファイルを翻訳
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po

# 全ファイルをバッチ翻訳
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

### 3. 日本語版のビルド

```bash
cd docs
make html-ja
```

詳しくは **[WORKFLOW.md](WORKFLOW.md)** をご覧ください。

---

## 📚 メインドキュメント

- **[WORKFLOW.md](WORKFLOW.md)** - 翻訳ワークフローの完全ガイド
- **[guides/GLOSSARY.md](guides/GLOSSARY.md)** - 用語集
- **[guides/LICENSE_AND_LOGO_GUIDE.md](guides/LICENSE_AND_LOGO_GUIDE.md)** - ライセンスとロゴの使用
- **[guides/LOCAL_LLM_SETUP.md](guides/LOCAL_LLM_SETUP.md)** - LLM環境構築の詳細

---

## 🔧 メインスクリプト（3つ）

| スクリプト | 用途 |
|-----------|------|
| `scripts/translate_po_smart.py` | POファイルの翻訳 |
| `scripts/test_simplified_chinese_detection.py` | 翻訳品質テスト |
| `scripts/normalize_po_files.py` | 構文エラー自動修正 |

---

## 📂 ディレクトリ構成

```
ftcdocs-ja/
├── docs/                    # Sphinxドキュメント
│   └── source/              # ソースファイル（RST）
├── locales/ja/LC_MESSAGES/  # 翻訳ファイル（PO）
├── scripts/                 # メインスクリプト
├── data/                    # 設定ファイル
├── guides/                  # ガイドドキュメント
└── legacy/                  # 古いスクリプト・ガイド
```
