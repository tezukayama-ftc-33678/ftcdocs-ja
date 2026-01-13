# プロジェクト構造 (更新版)

## 📁 ディレクトリ構造

```
ftcdocs-ja/
├── scripts/                   # 翻訳スクリプト
│   ├── core/                  # コアユーティリティ (完全独立)
│   │   ├── __init__.py
│   │   ├── rst_protector.py
│   │   ├── po_file_handler.py
│   │   ├── quality_checker.py
│   │   └── token_estimator.py
│   │
│   ├── api/                   # 翻訳API実装
│   │   ├── __init__.py
│   │   ├── translator_base.py
│   │   ├── local_llm_translator.py
│   │   ├── openai_translator.py
│   │   ├── anthropic_translator.py
│   │   └── translator_registry.py
│   │
│   ├── tests/                 # ユニットテスト
│   │   ├── __init__.py
│   │   ├── test_rst_protector.py
│   │   ├── test_po_file_handler.py
│   │   ├── test_quality_checker.py
│   │   ├── test_token_estimator.py
│   │   ├── run_tests.py
│   │   └── README.md
│   │
│   ├── translate_po_smart.py      # メイン翻訳スクリプト
│   ├── batch_translate_smart.py   # バッチ翻訳
│   ├── normalize_po_files.py      # PO正規化
│   └── show_backends.py           # バックエンド管理
│
├── data/                      # 設定・データ
│   ├── translate_config.json
│   ├── translation_progress.json
│   ├── mistranslation_corrections.json
│   └── simplified_chinese_blocked_entries.json
│
├── locales/ja/LC_MESSAGES/    # 翻訳ファイル
│   ├── index.po
│   ├── programming_resources/
│   └── ...
│
├── docs/                      # Sphinxドキュメント
│   ├── source/
│   ├── build/
│   └── Makefile
│
├── ARCHITECTURE.md            # アーキテクチャ設計書
├── LEGACY.md                  # レガシーコード文書
├── REFACTORING_SUMMARY.md     # リファクタリング概要
├── PROJECT_STRUCTURE.md       # プロジェクト構造
├── PHASE4_COMPLETION.md       # Phase 4完了報告
├── API_CORE_SEPARATION.md     # API/Core分離報告
└── README.md                  # プロジェクトREADME
```

## 🏗️ モジュール構成

### Core Module (scripts/core/)
**役割**: バックエンド非依存のユーティリティ機能

| ファイル | 責務 | 依存関係 |
|---------|------|---------|
| `rst_protector.py` | RSTマークアップ保護/復元 | なし |
| `po_file_handler.py` | POファイル安全I/O | polib |
| `quality_checker.py` | 翻訳品質検証 | なし |
| `token_estimator.py` | トークン数・コスト推定 | なし |

### API Module (scripts/api/)
**役割**: 翻訳バックエンド実装

| ファイル | 責務 | 依存関係 |
|---------|------|---------|
| `translator_base.py` | 抽象基底クラス | なし |
| `local_llm_translator.py` | Ollama実装 | core, ollama |
| `openai_translator.py` | OpenAI実装 | openai |
| `anthropic_translator.py` | Anthropic実装 | anthropic |
| `translator_registry.py` | バックエンド管理 | api modules |

### Tests Module (scripts/tests/)
**役割**: ユニットテスト

| ファイル | テスト対象 | テスト数 |
|---------|----------|---------|
| `test_rst_protector.py` | RST保護 | 22 |
| `test_po_file_handler.py` | POファイルI/O | 9 |
| `run_tests.py` | テストランナー | - |

## 🔄 依存関係

```
┌──────────────────────────────────┐
│      Main Scripts Layer          │
│  (translate_po_smart.py, etc.)   │
└───────────┬──────────────────────┘
            │
            ├─────────────┬─────────────┐
            │             │             │
      ┌─────▼─────┐ ┌────▼────┐  ┌────▼────┐
      │   core    │ │   api   │  │  tests  │
      │           │ │         │  │         │
      │ - RST     │ │ - Base  │  │ - Test  │
      │ - PO I/O  │ │ - Ollama│  │   Cases │
      │ - Quality │ │ - OpenAI│  │         │
      │ - Tokens  │ │ - Claude│  │         │
      └───────────┘ └────┬────┘  └─────────┘
                         │
                         │ (uses)
                         │
                    ┌────▼────┐
                    │  core   │
                    └─────────┘
```

## 📦 パッケージ詳細

### `core` パッケージ

```python
from core import (
    # RST Protection
    RSTProtector,
    split_into_chunks,
    should_skip_translation,
    
    # PO File Handling
    POFileHandler,
    POBatchHandler,
    
    # Quality & Estimation
    QualityChecker,
    TokenEstimator
)
```

**特徴:**
- 完全に独立（他モジュールに依存しない）
- 再利用可能（他プロジェクトでも使用可能）
- テストしやすい

### `api` パッケージ

```python
from api import (
    # Base
    Translator,
    TranslationError,
    
    # Implementations
    LocalLLMTranslator,
    OpenAITranslator,        # Optional
    AnthropicTranslator,     # Optional
    
    # Registry
    TranslatorRegistry,
    create_translator
)
```

**特徴:**
- 統一インターフェース（Translator基底クラス）
- プラグイン型アーキテクチャ
- オプション依存（未インストールでも動作）

## 🎯 設計原則

### 1. Separation of Concerns (関心の分離)
- `core`: データ処理とユーティリティ
- `api`: 外部APIとの通信

### 2. Dependency Inversion (依存性の逆転)
- 上位モジュール（scripts）→ 下位モジュール（core, api）
- `api` → `core`（一方向依存）

### 3. Single Responsibility (単一責任)
- 各モジュールは1つの明確な責務

### 4. Open/Closed Principle (開放/閉鎖)
- 拡張に開いている（新バックエンド追加容易）
- 変更に閉じている（既存コードの変更不要）

## 🚀 使用例

### 基本的な使い方

```python
# 1. コアユーティリティ
from core import RSTProtector, POFileHandler

protector = RSTProtector()
handler = POFileHandler()

# RST保護
protected, placeholders = protector.protect("Use ``code`` here")

# POファイル読み込み
po = handler.load("locales/ja/LC_MESSAGES/index.po")

# 2. 翻訳API
from api import create_translator

# 設定から作成
translator = create_translator(config_path="data/translate_config.json")

# 直接指定
translator = create_translator("openai", model="gpt-4")

# 翻訳実行
result = translator.translate("Hello, world!")
```

### バックエンド選択

```bash
# Ollama (デフォルト)
python translate_po_smart.py file.po

# OpenAI
python translate_po_smart.py file.po --backend openai

# Anthropic
python translate_po_smart.py file.po --backend anthropic

# バックエンド一覧
python show_backends.py
```

## 📊 メトリクス

### コード行数
- **core**: ~1,500行（ユーティリティ）
- **api**: ~1,500行（翻訳実装）
- **tests**: ~800行（テスト）
- **scripts**: ~600行（メインスクリプト）
- **合計**: ~4,400行

### モジュール数
- **core**: 4モジュール
- **api**: 5モジュール
- **tests**: 4テストファイル
- **scripts**: 4メインスクリプト

### テストカバレッジ
- **RST Protector**: 22テスト ✅
- **PO File Handler**: 9テスト ✅
- **成功率**: 100%

## 🔧 開発ワークフロー

### 新機能追加
1. `core`に新ユーティリティ追加（必要な場合）
2. `api`に新バックエンド追加（必要な場合）
3. `tests`にテスト追加
4. メインスクリプト更新

### バグ修正
1. 該当モジュールを特定
2. テストで再現
3. 修正
4. テスト実行

### リファクタリング
1. テスト実行（現状確認）
2. コード変更
3. テスト実行（変更検証）

## 📚 関連ドキュメント

- [ARCHITECTURE.md](ARCHITECTURE.md) - 詳細なアーキテクチャ設計
- [API_CORE_SEPARATION.md](API_CORE_SEPARATION.md) - 分離の詳細
- [PHASE4_COMPLETION.md](PHASE4_COMPLETION.md) - Phase 4完了報告
- [REFACTORING_SUMMARY.md](REFACTORING_SUMMARY.md) - リファクタリング概要
- [LEGACY.md](LEGACY.md) - レガシーコード文書

## 🎉 まとめ

この構造により:
1. ✅ **明確な責任分担** - 各モジュールの役割が明確
2. ✅ **高い保守性** - 変更の影響範囲が限定的
3. ✅ **優れた拡張性** - 新機能追加が容易
4. ✅ **テスト容易性** - モジュール単位でテスト可能
5. ✅ **再利用性** - coreモジュールは他でも使用可能

クリーンで保守しやすいコードベースを実現しました！
