# プロジェクト概要

**ftcdocs-ja** - FIRST Tech Challenge 公式ドキュメントの日本語翻訳プロジェクト

## 📊 プロジェクト情報

| 項目 | 内容 |
|------|------|
| **プロジェクト名** | ftcdocs-ja |
| **目的** | FTC公式ドキュメントの高品質日本語翻訳 |
| **翻訳方式** | AI自動翻訳（マルチバックエンド対応） |
| **公開URL** | https://ftcdocs-ja.readthedocs.io/ja/latest/ |
| **運営** | Team 33678 Tezukayama |
| **ライセンス** | MITライセンス（コード）、FIRST®ライセンス（コンテンツ） |

---

## 🎯 プロジェクトの特徴

### 1. マルチバックエンド翻訳システム

複数の翻訳エンジンをサポート:

| バックエンド | 特徴 | 用途 |
|------------|------|------|
| **OpenAI GPT-4** | 最高品質 | 本番翻訳 ✅ |
| **Anthropic Claude** | 長文対応 | 大量翻訳 |
| **Ollama (Local)** | 無料・オフライン | 開発・テスト |

### 2. Clean Architecture設計

```
Scripts (Application)
   ↓
   ├─→ Core (ユーティリティ - 完全独立)
   └─→ API (翻訳実装 - Coreを活用)
```

- ✅ 明確な責任分離
- ✅ 高い拡張性
- ✅ 優れた保守性
- ✅ 完全なテストカバレッジ

### 3. RST構文の完全保護

Sphinx互換性を100%維持:
- RST構文を自動検出・保護
- 翻訳後に正確に復元
- 日本語との間に適切なスペース挿入

### 4. 品質保証

- 31のユニットテスト（100%通過）
- 簡体字中国語の自動検出・ブロック
- 翻訳品質チェック

---

## 📁 プロジェクト構成

```
ftcdocs-ja/
├── docs/                      # Sphinxドキュメント
│   ├── source/                # RSTソース
│   └── build/html-ja/         # ビルド済み日本語版
│
├── locales/ja/LC_MESSAGES/    # POファイル（翻訳データ）
│
├── scripts/                   # 翻訳システム
│   ├── core/                  # コアユーティリティ
│   │   ├── rst_protector.py   # RST構文保護
│   │   ├── po_file_handler.py # POファイルI/O
│   │   ├── quality_checker.py # 品質チェック
│   │   └── token_estimator.py # トークン推定
│   │
│   ├── api/                   # 翻訳バックエンド
│   │   ├── translator_base.py
│   │   ├── openai_translator.py
│   │   ├── anthropic_translator.py
│   │   ├── local_llm_translator.py
│   │   └── translator_registry.py
│   │
│   ├── tests/                 # ユニットテスト
│   ├── translate_po_smart.py  # メイン翻訳スクリプト
│   ├── batch_translate_smart.py
│   └── show_backends.py
│
├── data/                      # 設定・データ
│   ├── translate_config.json  # 翻訳設定
│   └── translation_progress.json
│
├── guides/                    # ドキュメント
│   ├── GLOSSARY.md
│   ├── LOCAL_LLM_SETUP.md
│   └── LICENSE_AND_LOGO_GUIDE.md
│
├── legacy/                    # 旧バージョン
│
├── README.md                  # プロジェクト概要
├── ARCHITECTURE.md            # アーキテクチャ詳細
├── WORKFLOW.md                # 翻訳ワークフロー
└── PROJECT_STRUCTURE_V2.md    # 構造詳細
```

---

## 🚀 クイックスタート

### セットアップ

```bash
# 依存パッケージ
pip install polib tqdm colorama openai anthropic

# OpenAI APIキーを設定
# data/translate_config.json に api_key を設定
```

### 翻訳の実行

```bash
# 単一ファイル翻訳（OpenAI）
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po

# バックエンド指定
python scripts/translate_po_smart.py -b anthropic index.po

# バッチ翻訳
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

### ドキュメントビルド

```bash
cd docs
make html-ja
```

---

## 📚 主要ドキュメント

### ユーザー向け

1. **[README.md](README.md)** - プロジェクト概要（このファイル）
2. **[WORKFLOW.md](WORKFLOW.md)** - 翻訳ワークフロー完全ガイド
3. **[guides/GLOSSARY.md](guides/GLOSSARY.md)** - FTC用語集
4. **[guides/LOCAL_LLM_SETUP.md](guides/LOCAL_LLM_SETUP.md)** - Ollama環境構築

### 開発者向け

1. **[ARCHITECTURE.md](ARCHITECTURE.md)** - システムアーキテクチャ詳細
2. **[PROJECT_STRUCTURE_V2.md](PROJECT_STRUCTURE_V2.md)** - プロジェクト構造
3. **[scripts/README.md](scripts/README.md)** - スクリプト使用方法

### 開発履歴

1. **[PHASE5_MULTI_BACKEND_INTEGRATION.md](PHASE5_MULTI_BACKEND_INTEGRATION.md)** - Phase 5: マルチバックエンド統合
2. **[API_CORE_SEPARATION_FINAL.md](API_CORE_SEPARATION_FINAL.md)** - Phase 4.5: API/Core分離
3. **[PHASE4_COMPLETION.md](PHASE4_COMPLETION.md)** - Phase 4: バックエンド実装

---

## 🛠️ 技術スタック

### コア技術
- **Python 3.8+** - プログラミング言語
- **Sphinx** - ドキュメントビルドシステム
- **polib** - POファイル処理
- **gettext** - 翻訳インフラ

### AI/翻訳
- **OpenAI GPT-4** - メイン翻訳エンジン
- **Anthropic Claude** - サブ翻訳エンジン
- **Ollama** - ローカルLLM

### 開発ツール
- **pytest** - テストフレームワーク
- **Git** - バージョン管理
- **VS Code** - 開発環境

---

## 📊 統計情報

### コード規模

| カテゴリ | ファイル数 | 行数 |
|---------|----------|------|
| Core モジュール | 4 | ~1,000 |
| API モジュール | 5 | ~1,500 |
| メインスクリプト | 3 | ~1,000 |
| テスト | 2 | ~500 |
| **合計** | **14** | **~4,000** |

### 翻訳進捗

| 言語 | 翻訳率 | ファイル数 |
|------|--------|----------|
| 日本語 (ja) | 進行中 | 100+ POファイル |

### テストカバレッジ

- **ユニットテスト**: 31テスト（100%通過）
- **統合テスト**: 品質チェック、バックエンド切り替え
- **カバレッジ**: Core 90%+、API 統合テスト

---

## 🏗️ 設計原則

### 1. SOLID原則

- ✅ **S**ingle Responsibility - 単一責任
- ✅ **O**pen/Closed - 開放/閉鎖
- ✅ **L**iskov Substitution - リスコフの置換
- ✅ **I**nterface Segregation - インターフェース分離
- ✅ **D**ependency Inversion - 依存性逆転

### 2. Clean Architecture

- **Core**: ビジネスロジック（完全独立）
- **API**: 外部サービス統合
- **Scripts**: アプリケーション層

### 3. デザインパターン

- **Strategy Pattern** - バックエンド切り替え
- **Factory Pattern** - オブジェクト生成
- **Registry Pattern** - バックエンド管理
- **Dependency Injection** - 依存性注入

---

## 🔄 開発フロー

### ブランチ戦略

```
main (default)
  └── docs-ja-v2 (current)
```

### リリースプロセス

1. 機能開発（feature branch）
2. テスト実行
3. docs-ja-v2にマージ
4. ドキュメントビルド
5. Read the Docsに自動デプロイ

---

## 🤝 コントリビューション

### 貢献方法

1. リポジトリをフォーク
2. feature ブランチ作成
3. 変更を実装
4. テスト実行
5. Pull Request作成

### コーディング規約

- **PEP 8** - Pythonスタイルガイド遵守
- **型ヒント** - 可能な限り使用
- **ドキュメント文字列** - 全関数に記載
- **テスト** - 新機能には必ずテスト追加

---

## 📜 ライセンス

### コード
本プロジェクトのPythonコードは**MITライセンス**の下で公開されています。

### 翻訳コンテンツ
翻訳されたドキュメントは、元の**FIRST® ライセンス**に従います。

詳細は[LICENSE](LICENSE)と[LICENSE-JA.md](LICENSE-JA.md)を参照してください。

---

## 🙏 謝辞

- **FIRST®** - 素晴らしいFTCプログラムとドキュメント
- **Team 33678 Tezukayama** - プロジェクト運営
- **日本FTCコミュニティ** - フィードバックとサポート
- **OpenAI / Anthropic / Ollama** - AI翻訳技術
- **オープンソースコミュニティ** - 使用ツール・ライブラリ

---

## 📞 連絡先

- **GitHub Issues**: バグ報告・機能要望
- **Pull Requests**: コード貢献
- **Email**: （チーム連絡先があれば記載）

---

## 🗺️ ロードマップ

### 完了 ✅
- Phase 1: 既存コード分析
- Phase 2: モジュール化
- Phase 3: ユニットテスト
- Phase 4: マルチバックエンド実装
- Phase 4.5: API/Core分離
- Phase 5: マルチバックエンド統合

### 進行中 🚧
- 翻訳の継続実行
- 品質改善
- ドキュメント整備

### 今後の予定 📅
- キャッシング機能
- 翻訳メモリ
- 並列処理最適化
- CI/CD統合
- より詳細な品質メトリクス

---

**最終更新**: 2026年1月13日  
**バージョン**: 2.0（マルチバックエンド対応版）
