# Scripts ディレクトリ

このディレクトリには、翻訳プロジェクトのメインスクリプトが含まれています。

---

## 📝 メインスクリプト（3つ）

### 1️⃣ `translate_po_smart.py` - 翻訳スクリプト

POファイルを翻訳するメインスクリプト。RST構文を保護しながら高品質な翻訳を実行します。

```powershell
# 単一ファイルを翻訳
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po

# バッチ翻訳用ラッパー
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

**設定ファイル**: `data/translate_config.json`

---

### 2️⃣ `test_simplified_chinese_detection.py` - 翻訳テスト

簡体字中国語の誤混入を検出するテストスクリプト。

```powershell
python scripts/test_simplified_chinese_detection.py
```

翻訳後に実行して、品質を確認します。

---

### 3️⃣ `normalize_po_files.py` - 構文エラー自動修正

POファイルの構文エラーや誤訳を自動修正します。

```powershell
# 単一ファイルを修正
python scripts/normalize_po_files.py locales/ja/LC_MESSAGES/index.po

# 全ファイルを修正
python scripts/normalize_po_files.py locales/ja/LC_MESSAGES
```

**設定ファイル**: `data/mistranslation_corrections.json`

---

## 🔧 サポートスクリプト

### `rst_markup_extractor.py`

`translate_po_smart.py` が使用する依存モジュール。RST構文の保護と復元を担当します。

### `batch_translate_smart.py`

複数のPOファイルを順次翻訳するラッパースクリプト。進捗を保存しながらバッチ処理を実行します。

---

## 📚 詳細なドキュメント

各スクリプトの詳細な使い方については、[../WORKFLOW.md](../WORKFLOW.md) を参照してください。
