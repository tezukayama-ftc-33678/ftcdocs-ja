# FIRST Tech Challenge ドキュメントプロジェクト（日本語翻訳版）

本リポジトリは、**FIRST Tech Challenge 公式ドキュメント**の非公式日本語翻訳プロジェクトです。
AIを活用した自動翻訳システムにより、高品質な日本語ドキュメントを提供しています。

**📖 公開サイト**: https://ftcdocs-ja.readthedocs.io/ja/latest/index.html

---

## ⚠️ 非公式な翻訳と免責事項（重要）

**本プロジェクトは、FIRST Tech Challenge (FIRST®) の公式ドキュメントではありません。**

* この日本語翻訳は、日本のFTCコミュニティのために **Team 33678 Tezukayama** が自主的に運営・提供しているものです。
* 翻訳の正確性には努めていますが、**公式な情報源としては必ず英語のオリジナルドキュメントを参照してください。**
* 本翻訳の使用により生じたいかなる損害についても、本プロジェクトの貢献者および運営者は一切の責任を負いません。

**公式ウェブサイト（英語原文）**: https://ftc-docs.firstinspires.org

---

## 🚀 クイックスタート

### 必要な環境

```bash
# Python 3.8以上
python --version

# 必須パッケージのインストール
pip install polib tqdm colorama

# OpenAI/Anthropicを使う場合（推奨）
pip install openai anthropic

# ローカルLLMを使う場合
pip install ollama
ollama pull qwen2.5-coder:7b-instruct
```

### 翻訳の実行

```bash
# OpenAI GPT-4で翻訳（デフォルト）
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po

# バックエンドを指定して翻訳
python scripts/translate_po_smart.py -b anthropic index.po
python scripts/translate_po_smart.py -b ollama index.po

# バッチ翻訳
python scripts/batch_translate_smart.py -b openai locales/ja/LC_MESSAGES

# 利用可能なバックエンド一覧
python scripts/show_backends.py
```

### ドキュメントのビルド

```bash
cd docs
make html      # 英語版
make html-ja   # 日本語版
```

---

## 🤖 サポートされる翻訳バックエンド

| バックエンド | 特徴 | コスト | 推奨用途 |
|------------|------|--------|---------|
| **OpenAI gpt-4o-mini** | 最速、低コスト | ¥最安 | 本番翻訳 ✅ |
| **OpenAI gpt-4.1-mini** | 高速、バランス | ¥低 | 本番翻訳 |
| **OpenAI gpt-5-mini** | 高品質 | ¥中 | 大量翻訳 |
| **Anthropic Claude** | 長文対応 | ¥中 | 長文翻訳 |
| **Ollama (ローカル)** | 無料、オフライン | ¥0 | テスト・開発 |

**Daily Limit**: 2.5M トークン/日（全mini modelで共有）

### 設定ファイル (data/translate_config.json)

```json
{
  "backend": "openai",
  "model": "gpt-4o-mini",
  "api_key": "sk-...",
  "temperature": 0.1,
  "max_retries": 3
}
```

---

## 📁 プロジェクト構成

```
ftcdocs-ja/
├── docs/                      # Sphinxドキュメント
│   ├── source/                # RSTソースファイル
│   └── build/html-ja/         # ビルド済み日本語版
├── locales/ja/LC_MESSAGES/    # 翻訳ファイル (PO)
├── scripts/                   # 翻訳スクリプト
│   ├── core/                  # コアユーティリティ
│   │   ├── rst_protector.py   # RST構文保護
│   │   ├── po_file_handler.py # POファイルI/O
│   │   ├── quality_checker.py # 品質チェック
│   │   └── token_estimator.py # トークン推定
│   ├── api/                   # 翻訳バックエンド
│   │   ├── translator_base.py # 抽象基底クラス
│   │   ├── openai_translator.py
│   │   ├── anthropic_translator.py
│   │   ├── local_llm_translator.py
│   │   └── translator_registry.py
│   ├── tests/                 # ユニットテスト
│   ├── translate_po_smart.py  # メイン翻訳スクリプト
│   ├── batch_translate_smart.py
│   ├── normalize_po_files.py
│   └── show_backends.py
├── data/                      # 設定・データ
│   ├── translate_config.json  # 翻訳設定
│   ├── translation_progress.json
│   └── mistranslation_corrections.json
├── guides/                    # ドキュメント
│   ├── GLOSSARY.md            # 用語集
│   ├── LOCAL_LLM_SETUP.md     # LLM環境構築
│   └── LICENSE_AND_LOGO_GUIDE.md
└── legacy/                    # 旧バージョン
```

---

## 📚 ドキュメント

### メインドキュメント
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - システムアーキテクチャの詳細
- **[WORKFLOW.md](WORKFLOW.md)** - 翻訳ワークフロー完全ガイド
- **[guides/GLOSSARY.md](guides/GLOSSARY.md)** - FTC用語集

### セットアップガイド
- **[guides/LOCAL_LLM_SETUP.md](guides/LOCAL_LLM_SETUP.md)** - Ollama環境構築
- **[guides/LICENSE_AND_LOGO_GUIDE.md](guides/LICENSE_AND_LOGO_GUIDE.md)** - ライセンスとロゴ使用

### 開発履歴
- **[PHASE5_MULTI_BACKEND_INTEGRATION.md](PHASE5_MULTI_BACKEND_INTEGRATION.md)** - マルチバックエンド統合
- **[API_CORE_SEPARATION_FINAL.md](API_CORE_SEPARATION_FINAL.md)** - API/Core分離設計
- **[PROJECT_STRUCTURE_V2.md](PROJECT_STRUCTURE_V2.md)** - プロジェクト構造詳細

---

## 🛠️ 主要スクリプト

### 翻訳スクリプト

```bash
# 単一ファイル翻訳
python scripts/translate_po_smart.py [OPTIONS] <po_file>
  -b, --backend   翻訳バックエンド (openai|anthropic|ollama)
  -o, --output    出力ファイルパス
  -c, --config    設定ファイルパス

# バッチ翻訳
python scripts/batch_translate_smart.py [OPTIONS] <po_dir>
  -b, --backend   翻訳バックエンド
  -l, --limit     翻訳ファイル数制限
  --reset         進捗をリセット
```

### ユーティリティ

```bash
# 利用可能なバックエンド一覧
python scripts/show_backends.py

# PO構文エラー修正
python scripts/normalize_po_files.py

# 品質テスト
python scripts/test_simplified_chinese_detection.py
```

---

## 🏗️ アーキテクチャ

### モジュール構成

```
┌─────────────────────────────────┐
│      Translation Scripts        │  (translate_po_smart.py)
└────────────┬────────────────────┘
             │
    ┌────────┴─────────┐
    │                  │
┌───▼──────┐    ┌──────▼────┐
│   Core   │◄───┤    API    │
│ Utilities│    │ Backends  │
└──────────┘    └───────────┘
```

### 設計原則
- ✅ **Clean Architecture** - 明確な責任分離
- ✅ **SOLID原則** - 拡張可能で保守しやすい設計
- ✅ **プラグインアーキテクチャ** - 新バックエンドの追加が容易
- ✅ **包括的テスト** - 31のユニットテスト（100%通過）

---

## 🤝 コントリビューション

誤訳や改善案を見つけた場合は、GitHubのIssueやPull Requestをお気軽にお送りください！

### 貢献方法
1. このリポジトリをフォーク
2. feature ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. Pull Request を作成

---

## 📜 ライセンス

本プロジェクトのコードは[MITライセンス](LICENSE)の下で公開されています。
翻訳コンテンツは元の[FIRST® ライセンス](LICENSE-JA.md)に従います。

---

**🌟 Star this repository if you find it useful!**
