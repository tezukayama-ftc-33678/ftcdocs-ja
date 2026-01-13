# 進捗管理システム

## 概要

翻訳プロジェクトの進捗は `data/translation_progress.json` で一元管理されます。
複数ファイルのバッチ翻訳を中断・再開できる仕組みです。

---

## 進捗ファイルの構造

```json
{
  "completed": ["file1.po", "file2.po", ...],
  "failed": [
    {
      "file": "file3.po",
      "error": "エラーメッセージ",
      "timestamp": "2026-01-13 10:30:45"
    }
  ],
  "skipped": [],
  "last_updated": "2026-01-13 10:30:45"
}
```

### 各フィールドの説明

| フィールド | 説明 |
|----------|------|
| **completed** | 翻訳完了したファイル一覧 |
| **failed** | 翻訳失敗したファイル（詳細エラー記録） |
| **skipped** | スキップしたファイル |
| **last_updated** | 最終更新時刻 |

---

## 使用方法

### 1. バッチ翻訳を開始

```bash
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

- 初回実行時：新規の `translation_progress.json` が作成される
- 全POファイルを翻訳対象として開始

### 2. 途中で中断

```
[Ctrl+C] キー押下
```

- 現在のファイルまで完了した状態で終了
- 進捗は自動保存される
- 完了済みファイルは再翻訳されない

### 3. 中断後に再開

```bash
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

- 自動的に未完了ファイルのみを翻訳
- 既に完了したファイルはスキップ

### 4. 特定ファイル数だけ翻訳

```bash
# 10ファイルまで
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES --limit 10
```

---

## 進捗管理オプション

### 進捗をリセット

```bash
# 全進捗をリセットして最初からやり直す
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES --reset
```

**注意**: `translation_progress.json` が削除されます。既に翻訳済みのファイルが再翻訳されます。

### 進捗ファイルを手動確認

```bash
cat data/translation_progress.json
```

出力例：
```json
{
  "completed": [
    "index.po",
    "guides.po",
    "tutorials.po"
  ],
  "failed": [
    {
      "file": "advanced.po",
      "error": "Rate limit exceeded",
      "timestamp": "2026-01-13 09:30:00"
    }
  ],
  "last_updated": "2026-01-13 10:45:30"
}
```

---

## トークン使用状況の追跡

### 1. OpenAI Translator の統計情報

翻訳完了後、統計情報を取得できます：

```python
from api import create_translator

translator = create_translator('openai', api_key='sk-...')
# ... 翻訳実行 ...

stats = translator.get_stats()
print(stats)
# {
#   'total_tokens': 150000,
#   'prompt_tokens': 50000,
#   'completion_tokens': 100000,
#   'estimated_cost_usd': 0.1234,
#   'daily_limit_tokens': 2500000
# }
```

### 2. スクリプト実行後の確認

バッチ翻訳完了時に統計情報が表示されます：

```
✓ Completed: index.po
✓ Completed: guides.po

============================================================
Batch Translation Completed
============================================================
Completed:  2 files
Token usage: 150,000 / 2,500,000 daily limit
Estimated cost: $0.12
============================================================
```

### 3. 日次トークン制限

- **Daily Limit**: 2.5M トークン/日
- リセット時刻：毎日 UTC 深夜 (00:00 UTC)
- 複数のminiモデル（gpt-4o-mini, gpt-4.1-mini, gpt-5-mini）で共有

---

## 推奨される使い方

### シナリオ1: 定期的に少量翻訳

```bash
# 毎日5ファイル翻訳
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES --limit 5
```

**メリット**:
- 日次トークン制限内
- 進捗が可視化される
- エラー対応が容易

### シナリオ2: 大量一括翻訳

```bash
# 全ファイルを翻訳
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

**注意**:
- 2.5M トークン超過の可能性
- 予め日数を計画する
- `--limit` で分割推奨

### シナリオ3: 失敗ファイルの再試行

```bash
# failed ファイルを確認
cat data/translation_progress.json | grep -A 5 '"failed"'

# 特定ファイルのみを翻訳
python scripts/translate_po_smart.py path/to/failed_file.po

# または progress をリセットして再実行
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES --reset
```

---

## トラブルシューティング

### Q: 進捗ファイルが見当たらない

**A**: 未実行です。バッチ翻訳を一度実行すると自動作成されます。

```bash
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

### Q: 進捗ファイルを初期化したい

**A**: `--reset` オプションを使用

```bash
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES --reset
```

### Q: トークン超過が心配

**A**: `--limit` でファイル数制限

```bash
# 日次制限内に収める目安：1000トークン/ファイル × 2000ファイル
# → 数千ファイルで 2.5M トークン
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES --limit 1000
```

### Q: 進捗ファイルを手動編集したい

**A**: JSON形式を保持して編集可能

```json
{
  "completed": ["edited_files_here"],
  "failed": [],
  "last_updated": "2026-01-13 10:00:00"
}
```

---

## まとめ

### 進捗管理の特徴

✅ **自動保存** - 中断時も自動的に保存  
✅ **再開可能** - 中断後に続きから再開  
✅ **エラー記録** - 失敗ファイルの詳細記録  
✅ **トークン追跡** - 使用量と制限を可視化  
✅ **柔軟な制御** - リセット、制限数指定が可能  

---

**最終更新**: 2026年1月13日  
**バージョン**: 1.0（gpt-4o-mini対応版）
