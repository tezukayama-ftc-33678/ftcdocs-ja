# PO自動修正ツール (`fix_po_auto.py`)

GLOSSARY.mdの用語集と連携して、POファイル内の未翻訳箇所を自動修正するツールです。

## 機能

- **GLOSSARY.md解析**: マークダウンテーブルから英語→日本語のマッピングを自動抽出
- **未翻訳検出**: msgstrが空または英語のままなエントリを自動検出
- **スマート置換**: 長いフレーズから優先的に置換（`Game Manual` → `競技マニュアル`）
- **ドライランモード**: 修正内容をプレビューしてから適用可能
- **パターンマッチング**: 用語集にない一般的な表現（Next, Previous等）も自動修正

## インストール

依存するライブラリはありません（標準ライブラリのみ使用）。

## 使用方法

### 全POファイルをドライランで確認

```bash
python fix_po_auto.py --dry-run
```

実際には修正せず、修正候補を表示します。

### 全POファイルを実際に修正

```bash
python fix_po_auto.py
```

76個のファイルで194エントリを修正（実績）。

### 特定のPOファイルのみ修正

```bash
python fix_po_auto.py --file persona_pages/rookie_teams/rookie_teams.po
```

相対パスはGLOSSARY.mdに対して指定します。

## 修正例

### GLOSSARY.mdベース

```
msgid "Team"
msgstr ""  →  msgstr "チーム"

msgid "Competition Manual"
msgstr ""  →  msgstr "競技マニュアル"
```

### パターンマッチング

```
msgid "Next"
msgstr ""  →  msgstr "次へ"

msgid "Programming Resources"
msgstr ""  →  msgstr "プログラミングリソース"
```

## GlossaryLoader クラス

### メソッド

- `load_glossary()`: GLOSSARY.mdをMarkdownテーブルから解析
  - 英語保持用語: `col1 == col2`のエントリ（Robot Controller等）
  - 翻訳マッピング: `col1 != col2`のエントリ

- `translate_text(text)`: テキストを用語集に基づいて翻訳
  - 完全一致チェック
  - 複合語優先（長いフレーズから置換）

- `should_keep_english(text)`: テキストが英語保持対象か判定

## POAutoFixer クラス

### メソッド

- `parse_po_file(po_path)`: POファイルを正規表現で解析
  - msgidとmsgstrのペアを抽出
  - 複数行エントリに対応

- `is_untranslated(entry)`: エントリが未翻訳か判定
  - msgstrが空
  - msgidと同じ
  - 主に英語（80%以上がASCII）

- `suggest_translation(msgid)`: 翻訳候補を提案
  - GLOSSARY.mdベースの翻訳
  - パターンマッチング（次へ、ダウンロード等）

- `fix_po_file(po_path, dry_run)`: 単一POファイルを修正
  - ドライラン対応
  - 修正内容をコンソール出力

- `scan_and_fix(dry_run)`: 全POファイルをスキャンして修正
  - locales/ja/LC_MESSAGES配下の全.poファイルを対象
  - 修正統計を表示

## GLOSSARY.md連携

### テーブル形式

```markdown
| 英語 | 表記/統一訳語 | 備考 |
|------|---------|------|
| Team | チーム | |
| Robot | ロボット | |
```

### パース処理

1. Markdownテーブルを正規表現で抽出
2. ヘッダー行・区切り行をスキップ
3. col1が英語、col2が訳語として処理
4. col1 == col2 の場合は「英語保持」フラグ

## 修正統計（実績）

```
チェックしたファイル数: 256
修正したファイル数: 76
修正したエントリ数: 194
```

## 出力フォーマット

```
[INFO] GLOSSARY.md読み込み完了
  - 英語保持用語: 38件
  - 翻訳マッピング: 85件

[FILE] persona_pages/mentor_tech/mentor_tech.po
  修正候補: 5件
  [FIX] 'Team Management' -> 'チーム管理'
  [FIX] 'Programming Resources' -> 'プログラミングリソース'
  ...

[STATS] 修正結果
チェックしたファイル数: 256
修正したファイル数: 76
修正したエントリ数: 194
```

## 注意点

- **ドライランの確認**: 実際の修正前に `--dry-run` で内容を確認してください
- **バージョン管理**: 修正後は必ずgitで差分を確認してください
- **レビュー**: 自動修正なので誤り検出の確認が重要です
- **GLOSSARY更新**: 新しい用語を追加した場合は、スクリプトを再実行してください

## トラブルシューティング

### GLOSSARY.mdが見つからない

```
[WARN] GLOSSARY.mdが見つかりません
```

スクリプトをプロジェクトルートから実行してください。

### POファイルのシンタックスエラー

```
[ERROR] ... Syntax error in po file
```

POファイルを手動で確認・修正してください。

## 関連スクリプト

- `detect_untranslated.py`: HTMLから未翻訳英語を検出
- `detect_untranslated_simple.py`: Windows環境向けの簡略版

## ライセンス

プロジェクトに準拠。
