# 翻訳ファイルラベル機能 ガイド

## 概要

翻訳ファイルラベル機能は、特定のファイルに対して特別な状態やステータスを示すラベルを付ける仕組みです。これにより、以下のようなケースに対応できます：

- 意図的に英語を残すファイル（引用文や技術文書）
- AI翻訳が困難で人間のレビューが必要なファイル
- 英語が残っていても解決済みとみなすファイル

## ラベルの種類

### `intentional_english`
**用途**: 意図的に英語を残すファイル

**使用例**:
- 原文の引用文を含むファイル（例：gracious_professionalism/gp.rst）
- 技術文書で英語が必要な箇所
- RSTコメントブロック内の英語

### `ai_difficult`
**用途**: AI翻訳が困難なファイル

**使用例**:
- 複雑な技術説明が含まれるファイル
- 専門用語が多く、コンテキスト理解が必要なファイル
- スタイルガイドなど、細かいニュアンスが重要なファイル

### `resolved`
**用途**: 英語が残っていても解決済みとみなすファイル

**効果**: このラベルを付けたファイルは、英語の問題があっても「翻訳完了」として扱われます

**使用例**:
- 意図的に英語を残すファイルで、これ以上の翻訳作業が不要な場合
- 技術的な理由で英語を残す必要があり、レビュー済みのファイル

### `needs_human_review`
**用途**: 完了前に人間のレビューが必要なファイル

**使用例**:
- AI翻訳の品質確認が必要なファイル
- 重要な文書で、人間による最終確認が必要な場合

## ラベルの設定方法

### 1. YAML設定ファイルの編集

`TRANSLATION_FILE_LABELS.yaml` ファイルを編集してラベルを追加します：

```yaml
ファイルパス:
  labels:
    - ラベル名1
    - ラベル名2
  reason: "このラベルを付ける理由の説明"
  date_added: "YYYY-MM-DD"
```

### 2. 実際の例

```yaml
gracious_professionalism/gp.rst:
  labels:
    - intentional_english
    - resolved
  reason: "Contains Dr. Woodie Flowers' original English quote which should be preserved alongside Japanese translation"
  date_added: "2025-12-11"

contrib/style_guide/image-and-figure-details.rst:
  labels:
    - ai_difficult
    - needs_human_review
  reason: "Large style guide with complex technical explanations, option descriptions, and accessibility guidelines that require careful human review"
  date_added: "2025-12-11"
```

## ラベルの確認方法

翻訳進捗チェッカーを実行すると、ラベル付きファイルが別セクションに表示されます：

```bash
python docs/scripts/check_translation_progress.py
```

生成される `TRANSLATION_PROGRESS.md` で以下が確認できます：

1. **翻訳完了ファイル** セクション内の「🏷️ ラベル付きファイル」サブセクション
2. **部分的に翻訳されているファイル** セクションで、各ファイル名の横にラベルが表示
3. ラベル理由の説明

## ワークフロー例

### 例1: 意図的な英語を含むファイルの処理

1. ファイルを翻訳中に、原文の引用文など意図的に残すべき英語を発見
2. `TRANSLATION_FILE_LABELS.yaml` に以下を追加：

```yaml
example/file.rst:
  labels:
    - intentional_english
    - resolved
  reason: "Contains original English quotes from important sources"
  date_added: "2025-12-11"
```

3. 翻訳チェッカーを実行して確認
4. ファイルは「翻訳完了」として扱われる

### 例2: AI翻訳が困難なファイルの処理

1. 複雑な技術文書を発見
2. `TRANSLATION_FILE_LABELS.yaml` に以下を追加：

```yaml
complex/technical_doc.rst:
  labels:
    - ai_difficult
    - needs_human_review
  reason: "Complex accessibility guidelines requiring expert knowledge"
  date_added: "2025-12-11"
```

3. 人間の翻訳者にレビューを依頼
4. レビュー完了後、必要に応じて `resolved` ラベルを追加

## ベストプラクティス

### ラベルを付けるタイミング
- AI翻訳で対応できない箇所を発見したとき
- 意図的に英語を残す必要があるとき
- 人間のレビューが必要と判断したとき

### reason フィールドの記述
- **具体的に**: なぜそのラベルが必要なのかを明確に記述
- **英語で記述**: 国際的な協力者も理解できるように
- **簡潔に**: 1-2文で要点をまとめる

### ラベルの組み合わせ
よく使われる組み合わせ：
- `intentional_english` + `resolved`: 意図的な英語で解決済み
- `ai_difficult` + `needs_human_review`: 人間のレビュー待ち
- `resolved` のみ: その他の理由で解決済み

## トラブルシューティング

### Q: ラベルを付けたのに反映されない
**A**: 以下を確認してください：
- ファイルパスが正しいか（`docs/source/` からの相対パス）
- YAML構文が正しいか（インデントなど）
- 翻訳チェッカーを再実行したか

### Q: 複数のファイルに同じラベルを付けたい
**A**: 各ファイルごとに設定を追加してください。現時点ではワイルドカード指定は非対応です。

### Q: ラベルを削除したい
**A**: `TRANSLATION_FILE_LABELS.yaml` から該当エントリを削除し、翻訳チェッカーを再実行してください。

## まとめ

ラベル機能を活用することで、以下のメリットがあります：

1. **明確な分類**: ファイルの翻訳状態を細かく管理できる
2. **作業効率化**: AI対応可能なファイルと人間対応が必要なファイルを区別
3. **進捗管理**: 意図的な英語を含むファイルを「完了」として扱える
4. **チーム協力**: ラベルと理由を共有することで、チーム全体で状況を把握

ラベル機能を効果的に使用して、翻訳プロジェクトをスムーズに進めましょう！
