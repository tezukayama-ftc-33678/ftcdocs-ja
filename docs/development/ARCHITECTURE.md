# Translation System Architecture

## 概要

本ドキュメントは、FTC日本語ドキュメント翻訳プロジェクトの最新アーキテクチャを説明します。
マルチバックエンド対応、Clean Architecture原則、SOLID設計を採用しています。

### 設計原則

1. **Clean Architecture** - 責任の明確な分離（Core / API / Scripts）
2. **SOLID原則** - 拡張可能で保守しやすい設計
3. **RST構文の完全保護** - Sphinx互換性を保証
4. **プラグインアーキテクチャ** - 新バックエンドの追加が容易
5. **包括的テスト** - 31のユニットテストで品質保証

---

## アーキテクチャ図

### レイヤー構造

```
┌─────────────────────────────────────────────────┐
│         Application Layer                        │
│  (translate_po_smart.py, batch_translate_smart.py)│
└────────────────┬────────────────────────────────┘
                 │
        ┌────────┴─────────┐
        │                  │
┌───────▼──────────┐  ┌────▼─────────────┐
│   Core Module    │  │   API Module     │
│   (Utilities)    │◄─┤  (Translators)   │
└──────────────────┘  └──────────────────┘
        │                     │
        │  ・RST Protection   │  ・Translator Base
        │  ・PO File I/O      │  ・OpenAI
        │  ・Quality Check    │  ・Anthropic
        │  ・Token Estimate   │  ・Local LLM
        │                     │  ・Registry
        └─────────────────────┘
```

### 依存関係の一方向性

```
Scripts (Application)
   ↓
   ├─→ Core (完全独立、API非依存)
   └─→ API (Coreを使用)
```

---

## ディレクトリ構成

```
scripts/
├── core/                        # コアユーティリティ（完全独立）
│   ├── __init__.py              # Core exports
│   ├── rst_protector.py         # RST構文保護・復元
│   ├── po_file_handler.py       # POファイルI/O
│   ├── quality_checker.py       # 品質チェック（中国語検出等）
│   └── token_estimator.py       # トークン推定・コスト計算
│
├── api/                         # 翻訳バックエンド実装
│   ├── __init__.py              # API exports
│   ├── translator_base.py       # 抽象基底クラス
│   ├── local_llm_translator.py  # Ollama実装
│   ├── openai_translator.py     # OpenAI実装
│   ├── anthropic_translator.py  # Anthropic実装
│   └── translator_registry.py   # バックエンド管理
│
├── tests/                       # ユニットテスト
│   ├── test_rst_protector.py    # 22 tests
│   ├── test_po_file_handler.py  # 9 tests
│   └── README.md
│
├── translate_po_smart.py        # 単一ファイル翻訳
├── batch_translate_smart.py     # バッチ翻訳
├── normalize_po_files.py        # PO構文正規化
├── show_backends.py             # バックエンド一覧表示
└── test_simplified_chinese_detection.py  # 品質テスト
```

---

## Core Module（コアユーティリティ層）

### 設計哲学
- **完全独立**: 翻訳APIに依存しない汎用ユーティリティ
- **再利用可能**: 他プロジェクトでもそのまま使用可能
- **単一責任**: 各モジュールが明確な責務を持つ

### 1. `rst_protector.py` - RST構文保護

**責務**: RST構文を翻訳から保護し、翻訳後に復元する

```python
from core import RSTProtector

protector = RSTProtector()

# 保護
text = "See :doc:`guide </path/to/guide>` for details."
protected, placeholders = protector.protect(text)
# → "See __RST_ROLE_0__ for details."

# 翻訳後に復元
translated = "詳細は __RST_ROLE_0__ を参照"
restored = protector.restore(translated, placeholders)
# → "詳細は :doc:`guide </path/to/guide>` を参照"
```

**保護対象**:
1. 外部リンク: `` `text <url>`_ ``
2. ロール: `:ref:`, `:doc:`, `:download:`, etc.
3. URL: `http://...`, `https://...`
4. ファイルパス: `file.py`, `images/sample.png`
5. インラインコード: ``` ``code`` ```
6. 太字・斜体: `**bold**`, `*italic*`
7. 内部リンク: `` `text`_ ``
8. 置換: `|name|`

**重要機能**: 日本語とインラインマークアップの間に半角スペース自動挿入
```
Bad:  日本語`text`日本語  (Sphinxエラー)
Good: 日本語 `text` 日本語 (正常)
```

### 2. `po_file_handler.py` - POファイルI/O

**責務**: POファイルの安全な読み書き

```python
from core import POFileHandler

handler = POFileHandler()

# 読み込み
po = handler.load("locales/ja/LC_MESSAGES/index.po")

# 未翻訳エントリ取得
entries = handler.get_untranslated_entries(po)

# 翻訳設定
handler.set_translation(entry, "翻訳テキスト")

# 保存
handler.save(po, "output.po")
```

**安全性保証**:
- ✅ `msgid`は絶対に変更しない
- ✅ `msgstr`のみ書き込み
- ✅ fuzzyフラグとコメント保持
- ✅ メタデータ保存

### 3. `quality_checker.py` - 品質チェック

**責務**: 翻訳品質の検証

```python
from core import QualityChecker

checker = QualityChecker()

result = checker.check_text("翻訳された文章")
# result = {
#   'is_acceptable': True,
#   'issues': [],
#   'simplified_chinese_ratio': 0.0,
#   'japanese_char_count': 10
# }
```

**チェック項目**:
- ✅ 簡体字中国語の検出（誤翻訳防止）
- ✅ 日本語文字の存在確認
- ✅ 文字数統計

### 4. `token_estimator.py` - トークン推定

**責務**: トークン数とコスト推定（OpenAI/Anthropic用）

```python
from core import TokenEstimator

estimator = TokenEstimator()

# トークン推定
tokens = estimator.estimate_tokens(text)

# コスト計算
cost = estimator.estimate_cost(
    input_tokens=1000,
    output_tokens=1500,
    model="gpt-4"
)
```

---

## API Module（翻訳実装層）

### 設計哲学
- **Coreを活用**: ユーティリティを再利用
- **Strategy Pattern**: バックエンドの切り替え可能
- **Factory Pattern**: 統一されたインターフェース

### 1. `translator_base.py` - 抽象基底クラス

**責務**: 全翻訳クラスの共通インターフェース定義

```python
from abc import ABC, abstractmethod

class Translator(ABC):
    @abstractmethod
    def translate(self, text: str, context: str = "") -> str:
        """テキストを翻訳"""
        pass
    
    @abstractmethod
    def translate_batch(self, texts: List[str]) -> List[str]:
        """バッチ翻訳"""
        pass
```

### 2. `local_llm_translator.py` - Ollama実装

**特徴**:
- 無料・オフライン動作
- ローカルLLM（Ollama）を使用
- 開発・テスト向け

```python
from api import LocalLLMTranslator

translator = LocalLLMTranslator(
    model="qwen2.5-coder:7b-instruct",
    temperature=0.1
)
result = translator.translate("Hello World")
```

### 3. `openai_translator.py` - OpenAI実装

**特徴**:
- 最高品質（GPT-4）
- 高速
- 本番環境推奨

```python
from api import OpenAITranslator

translator = OpenAITranslator(
    api_key="sk-...",
    model="gpt-4",
    temperature=0.1
)
result = translator.translate("Hello World")
```

### 4. `anthropic_translator.py` - Anthropic実装

**特徴**:
- 長文対応（Claude）
- 高品質
- 大量翻訳向け

```python
from api import AnthropicTranslator

translator = AnthropicTranslator(
    api_key="sk-ant-...",
    model="claude-3-sonnet-20240229",
    temperature=0.1
)
result = translator.translate("Hello World")
```

### 5. `translator_registry.py` - バックエンド管理

**責務**: 翻訳バックエンドの登録と選択

```python
from api import TranslatorRegistry, create_translator

# 利用可能なバックエンド一覧
backends = TranslatorRegistry.list_backends()
# → ['ollama', 'local', 'openai', 'gpt', 'anthropic', 'claude']

# バックエンド作成
translator = create_translator(
    'openai',
    api_key='sk-...',
    model='gpt-4'
)
```

---

## Application Layer（アプリケーション層）

### 1. `translate_po_smart.py` - 単一ファイル翻訳

**使い方**:
```bash
# デフォルト（OpenAI）
python translate_po_smart.py index.po

# バックエンド指定
python translate_po_smart.py -b anthropic index.po
python translate_po_smart.py -b ollama index.po -o output.po
```

**処理フロー**:
1. POファイル読み込み（POFileHandler）
2. 未翻訳エントリ抽出
3. RST保護（RSTProtector）
4. 翻訳実行（Translator）
5. 品質チェック（QualityChecker）
6. RST復元
7. POファイル保存

### 2. `batch_translate_smart.py` - バッチ翻訳

**使い方**:
```bash
# 全ファイル翻訳
python batch_translate_smart.py locales/ja/LC_MESSAGES

# 10ファイル限定
python batch_translate_smart.py -b openai locales/ja/LC_MESSAGES --limit 10
```

**追加機能**:
- 進捗保存（中断・再開可能）
- エラーハンドリング
- ファイルサイズ順に処理

---

## 設計パターン

### 1. Strategy Pattern（戦略パターン）

**目的**: 翻訳アルゴリズム（バックエンド）を切り替え可能に

```python
# 同じインターフェースで異なる実装
translator = create_translator('openai', ...)  # OpenAI
translator = create_translator('anthropic', ...)  # Anthropic
translator = create_translator('ollama', ...)  # Local LLM

# 全て同じ方法で使用
result = translator.translate(text)
```

### 2. Factory Pattern（ファクトリパターン）

**目的**: オブジェクト生成を統一

```python
# TranslatorRegistryがファクトリ
translator = create_translator(backend_name, **config)
```

### 3. Registry Pattern（レジストリパターン）

**目的**: 利用可能なバックエンドを一元管理

```python
class TranslatorRegistry:
    _backends = {
        'openai': OpenAITranslator,
        'anthropic': AnthropicTranslator,
        'ollama': LocalLLMTranslator
    }
```

### 4. Dependency Injection（依存性注入）

**目的**: テスタビリティ向上

```python
class SmartPOTranslator:
    def __init__(self, translator: Translator):
        self.translator = translator  # 外部から注入
```

---

## SOLID原則の実装

### 1. Single Responsibility（単一責任の原則）

✅ **実装例**:
- `RSTProtector`: RST保護のみ
- `POFileHandler`: POファイルI/Oのみ
- `QualityChecker`: 品質チェックのみ

### 2. Open/Closed（開放/閉鎖の原則）

✅ **実装例**:
- 拡張に開く: 新バックエンドは`api/`に追加
- 変更に閉じる: `core/`は変更不要

```python
# 新バックエンド追加（既存コード変更不要）
class NewTranslator(Translator):
    def translate(self, text):
        # 実装
```

### 3. Liskov Substitution（リスコフの置換原則）

✅ **実装例**:
- 全Translatorサブクラスは`Translator`と置き換え可能

```python
def process(translator: Translator):
    # どのTranslatorでも動作
    return translator.translate(text)
```

### 4. Interface Segregation（インターフェース分離の原則）

✅ **実装例**:
- 最小限のインターフェース（`translate`, `translate_batch`のみ）

### 5. Dependency Inversion（依存性逆転の原則）

✅ **実装例**:
- 上位層が下位層の抽象に依存

```python
# 具象クラスではなく抽象に依存
translator: Translator = create_translator(...)
```

---

## テスト戦略

### ユニットテスト

```
tests/
├── test_rst_protector.py      # 22 tests
└── test_po_file_handler.py    # 9 tests

Total: 31 tests, 100% pass rate ✅
```

### テストカバレッジ

| モジュール | テスト数 | カバレッジ |
|-----------|---------|----------|
| rst_protector | 22 | 95%+ |
| po_file_handler | 9 | 90%+ |
| quality_checker | - | 統合テスト |
| translators | - | 統合テスト |

### 実行方法

```bash
cd scripts/tests
python test_rst_protector.py
python test_po_file_handler.py
```

---

## 拡張ガイド

### 新しい翻訳バックエンドの追加

1. **`api/new_translator.py`を作成**:
```python
from .translator_base import Translator

class NewTranslator(Translator):
    def translate(self, text: str, context: str = "") -> str:
        # 実装
        pass
```

2. **`api/translator_registry.py`に登録**:
```python
class TranslatorRegistry:
    _backends = {
        # ...existing...
        'new': NewTranslator
    }
```

3. **使用**:
```bash
python translate_po_smart.py -b new index.po
```

**変更不要**:
- ✅ `core/` モジュール
- ✅ メインスクリプト
- ✅ 既存バックエンド

---

## パフォーマンス最適化

### 1. チャンク分割

長文を小さなチャンクに分割して翻訳:
```python
chunks = split_into_chunks(text, max_size=400)
for chunk in chunks:
    translated = translator.translate(chunk)
```

### 2. バッチ処理

複数テキストを一度に翻訳:
```python
results = translator.translate_batch(texts)
```

### 3. キャッシング

同一テキストの再翻訳を回避（未実装、将来の拡張ポイント）

---

## セキュリティ

### APIキー管理

```json
// data/translate_config.json
{
  "backend": "openai",
  "api_key": "sk-...",  // ⚠️ .gitignore必須
  "model": "gpt-4"
}
```

**注意**:
- ✅ `translate_config.json`を`.gitignore`に追加
- ✅ 環境変数からの読み込みサポート（将来実装）

---

## トラブルシューティング

### よくある問題

1. **Sphinxビルドエラー**
   - 原因: RST構文の破損
   - 解決: `RSTProtector`の保護パターン確認

2. **翻訳品質が低い**
   - 原因: 不適切なモデル/temperature
   - 解決: `translate_config.json`で調整

3. **簡体字中国語が混入**
   - 原因: モデルの言語混同
   - 解決: `QualityChecker`が自動検出・ブロック

---

## まとめ

### アーキテクチャの強み

1. ✅ **拡張性**: 新バックエンド追加が容易
2. ✅ **保守性**: モジュール単位で変更可能
3. ✅ **テスタビリティ**: 各層が独立してテスト可能
4. ✅ **再利用性**: Coreは他プロジェクトでも使用可能
5. ✅ **品質**: 31テストで品質保証

### 今後の拡張ポイント

- [ ] キャッシング機能
- [ ] 環境変数からのAPIキー読み込み
- [ ] 翻訳メモリ機能
- [ ] 並列処理の最適化
- [ ] より詳細な品質メトリクス

---

**更新日**: 2026年1月13日  
**バージョン**: 2.0（マルチバックエンド対応版）
