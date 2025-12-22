# Translation Quality Tools
# 翻訳品質ツール

日本語翻訳の品質をチェックし、問題を自動的に検出・修正するツール群

## 🎯 主な機能

### translation_quality_checker.py

日本語翻訳の品質を包括的にチェックするツール

**検出できる問題:**

1. **未翻訳エントリー** - msgstrが空または未記入
2. **RST構文エラー**
   - 太字マークアップ (`**`) のスペーシング問題
   - イタリック体マークアップ (`*`) のスペーシング問題
   - コードマークアップ (` `` `) のスペーシング問題
   - マークアップの不一致（開始と終了の数が合わない）
3. **インラインマークアップ不一致** - 英語版にあるマークアップが日本語版にない
4. **LLM支援修正** - ローカルLLM (Ollama) を使用した修正案の提案

## 🚀 使用方法

### 基本的な使い方

#### 1. チェックのみ実行

```bash
python tools/quality/translation_quality_checker.py --check
```

全てのPOファイルをチェックし、問題をリストアップします。

#### 2. 自動修正を実行

```bash
python tools/quality/translation_quality_checker.py --fix
```

自動修正可能な問題（スペーシングエラー等）を自動的に修正します。

#### 3. ドライラン（修正内容確認のみ）

```bash
python tools/quality/translation_quality_checker.py --fix --dry-run
```

修正内容を表示しますが、実際には適用しません。

#### 4. 詳細レポート生成

```bash
python tools/quality/translation_quality_checker.py --report
```

HTML形式とJSON形式で詳細レポートを生成します。

### 高度な使い方

#### LLMを使用した修正案提案

```bash
python tools/quality/translation_quality_checker.py --report --use-llm
```

ローカルLLM (Ollama) を使用して、複雑な問題の修正案を提案します。

**前提条件:**
- Ollamaがインストールされていること
- `qwen2.5:7b-instruct-q5_K_M` モデルがダウンロードされていること

```bash
# モデルのダウンロード
ollama pull qwen2.5:7b-instruct-q5_K_M

# 必要なパッケージのインストール
pip install ollama polib
```

#### 詳細な出力を表示

```bash
python tools/quality/translation_quality_checker.py --check --verbose
```

チェック中の詳細情報を表示します。

## 📊 レポートの見方

### HTMLレポート

レポート生成後、以下の場所に保存されます:
```
data/quality_reports/quality_report_YYYYMMDD_HHMMSS.html
```

**レポートの内容:**
- 統計情報（総ファイル数、エントリー数、問題数）
- ファイルごとの問題リスト
- 各問題の詳細（元の英語、現在の日本語、修正案）
- フィルター機能（エラーのみ、警告のみ、自動修正可能のみ）

### JSONレポート

プログラムで処理しやすいJSON形式のレポート:
```
data/quality_reports/quality_report_YYYYMMDD_HHMMSS.json
```

**データ構造:**
```json
{
  "timestamp": "2025-12-22T10:00:00",
  "stats": {
    "total_files": 100,
    "total_entries": 5000,
    "empty_entries": 50,
    "syntax_errors": 30,
    "warnings": 20,
    "auto_fixable": 25
  },
  "issues": [
    {
      "po_file": "locales/ja/LC_MESSAGES/path/to/file.po",
      "msgid": "Original English text",
      "msgstr": "現在の日本語翻訳",
      "issue_type": "rst_syntax",
      "severity": "error",
      "description": "太字マークアップ（**）の前後に不要なスペースがあります",
      "line_number": 42,
      "suggested_fix": "修正後の日本語翻訳",
      "auto_fixable": true
    }
  ]
}
```

## 🔧 ワークフロー例

### 1. 翻訳後の品質チェック

```bash
# 1. チェック実行
python tools/quality/translation_quality_checker.py --check

# 2. レポート生成
python tools/quality/translation_quality_checker.py --report

# 3. HTMLレポートを開いて問題を確認
# ブラウザで data/quality_reports/quality_report_*.html を開く

# 4. 自動修正可能な問題を修正
python tools/quality/translation_quality_checker.py --fix

# 5. 再度チェック
python tools/quality/translation_quality_checker.py --check
```

### 2. LLMを使用した高度な修正

```bash
# 1. LLMを使用してレポート生成
python tools/quality/translation_quality_checker.py --report --use-llm

# 2. レポートを確認してLLMの修正案を確認

# 3. 手動で修正が必要な箇所を修正

# 4. 最終チェック
python tools/quality/translation_quality_checker.py --check
```

## 🐛 トラブルシューティング

### polib がインストールされていない

```bash
pip install polib
```

### Ollama が利用できない

LLM機能を使わない場合は、`--use-llm` オプションを外してください:

```bash
python tools/quality/translation_quality_checker.py --report
```

### レポートが生成されない

`data/quality_reports` ディレクトリは自動的に作成されますが、権限エラーが発生する場合は手動で作成してください:

```bash
mkdir -p data/quality_reports
```

## 📝 検出される問題の例

### 1. 未翻訳エントリー

```po
msgid "This is English text"
msgstr ""
```

→ 警告: msgstrが空です（未翻訳）

### 2. 太字マークアップのスペーシングエラー

```po
msgid "This is **bold** text"
msgstr "これは ** 太字 ** テキストです"
```

→ エラー: 太字マークアップ（**）の前後に不要なスペースがあります
→ 修正案: "これは**太字**テキストです"
→ 自動修正可能

### 3. コードマークアップのスペーシングエラー

```po
msgid "Use ``code`` here"
msgstr "ここで `` コード `` を使用"
```

→ エラー: コードマークアップ（``）の前後に不要なスペースがあります
→ 修正案: "ここで``コード``を使用"
→ 自動修正可能

### 4. マークアップの不一致

```po
msgid "This has **bold** text"
msgstr "これは太字テキストです"
```

→ 警告: 英語版にある太字マークアップが日本語版にありません

## 🔗 関連ツール

- **tools/translation/** - 自動翻訳ツール
- **tools/po-fixing/** - PO構文修正ツール
- **tools/analysis/** - ビルド警告分析ツール

## 📚 関連ドキュメント

- [QUICKSTART.md](../../QUICKSTART.md) - プロジェクト全体のクイックスタート
- [AUTO_TRANSLATE.md](../../guides/AUTO_TRANSLATE.md) - 自動翻訳ガイド
- [PO_SYNTAX_FIX_GUIDE.md](../../guides/PO_SYNTAX_FIX_GUIDE.md) - PO構文修正ガイド
