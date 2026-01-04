# Data ディレクトリ

このディレクトリには、翻訳スクリプトで使用する設定ファイルとデータファイルが含まれています。

---

## 📝 設定ファイル

### `translate_config.json`

翻訳スクリプト（`scripts/translate_po_smart.py`）の設定ファイル。

**主な設定項目**:
- `model`: 使用するLLMモデル（例: `qwen2.5-coder:7b-instruct`）
- `temperature`: 翻訳の創造性（低いほど正確、例: `0.05`）
- `max_retries`: 失敗時のリトライ回数（例: `3`）
- `chunk_size`: テキスト分割サイズ（例: `400`）
- `context_window`: コンテキストウィンドウサイズ（例: `2048`）

### `mistranslation_corrections.json`

構文修正スクリプト（`scripts/normalize_po_files.py`）で使用する誤訳修正リスト。

よくある誤訳パターンを定義し、自動修正します。

---

## 📊 データファイル

### `translation_progress.json`

バッチ翻訳の進捗を記録するファイル。`scripts/batch_translate_smart.py` が自動的に更新します。

### `simplified_chinese_blocked_entries.json`

簡体字中国語が検出されてブロックされたエントリのログ。手動で確認し、必要に応じて修正します。

---

## 🗑️ 古いファイル

以前の分析結果やレポートファイルは `legacy/data/` に移動されています。

---

## ⚙️ カスタマイズ

### モデルの変更

より高速な翻訳が必要な場合：

```json
{
  "model": "llama3.1:8b-instruct-q5_K_M"
}
```

より正確な翻訳が必要な場合：

```json
{
  "temperature": 0.01
}
```

### 誤訳の追加

よくある誤訳を見つけた場合、`mistranslation_corrections.json` に追加してください：

```json
{
  "corrections": [
    {
      "mistranslation": "間違った訳語",
      "correct": "正しい訳語",
      "description": "説明"
    }
  ]
}
```
