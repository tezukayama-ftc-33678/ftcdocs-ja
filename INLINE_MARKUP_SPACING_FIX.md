# Inline Markup Spacing Fix Script 使用方法

## 概要

このスクリプトは、Sphinxビルド時に発生する「Inline literal/emphasis」警告を修正するためのツールです。
日本語テキストとインラインマークアップ（バッククォート `` ` `` やアスタリスク `*`）の間にスペースがないことが原因で発生する警告を自動的に修正します。

## 問題の背景

Sphinxでは、reStructuredTextのインラインマークアップ（`` ` ``、`*`、`**` など）を使用する際、マークアップ文字の前後にスペースが必要です。
日本語テキストの場合、このスペースが欠けていることが多く、以下のような警告が発生します：

```
WARNING: Inline literal start-string without end-string.
WARNING: Inline emphasis start-string without end-string.
```

### 具体例

**問題のある例：**
```
msgstr "これは`サンプル`です"
msgstr "これは*重要*な情報です"
```

**修正後：**
```
msgstr "これは `サンプル` です"
msgstr "これは *重要* な情報です"
```

## スクリプトの仕様

### 処理内容

1. **対象ファイル**: 指定したディレクトリ内のすべての `.po` ファイル
2. **対象行**: `msgstr "..."` の行のみ（`msgid` は絶対に書き換えません）
3. **置換ルール**:
   - バッククォート `` ` `` の前後に半角スペースを挿入
   - シングルアスタリスク `*` の前後に半角スペースを挿入
4. **除外条件**:
   - ダブルアスタリスク `**` は太字指定なので、そのまま（スペースを入れない）
   - エスケープされた `\*` や `` \` `` も対象外
5. **重複防止**: すでにスペースがある場合は、二重にスペースを入れません

### 処理アルゴリズム

```python
# 処理順序:
1. エスケープされた文字（\`、\*）を一時的に保護
2. バッククォートの前後にスペースを追加
3. **（太字）を一時的に保護
4. シングルアスタリスクの前後にスペースを追加
5. 保護した文字を元に戻す
```

## 使用方法

### 基本的な使用方法

#### 1. Dry-runモード（推奨：最初に実行）

実際にファイルを変更する前に、どのような変更が行われるかを確認します：

```bash
python fix_inline_markup_spacing.py --dry-run
```

#### 2. 通常実行（ファイルを実際に変更）

```bash
python fix_inline_markup_spacing.py
```

#### 3. 詳細ログ付きで実行

各ファイルの修正内容を詳しく表示します：

```bash
python fix_inline_markup_spacing.py --verbose
```

### オプション

| オプション | 説明 | デフォルト値 |
|----------|------|------------|
| `--po-dir` | 処理対象の.poファイルがあるディレクトリ | `locales/ja/LC_MESSAGES` |
| `--dry-run` | ファイルを変更せず、検出のみ実行 | 無効 |
| `--verbose` | 詳細なログを表示 | 無効 |

### カスタムディレクトリの指定

```bash
python fix_inline_markup_spacing.py --po-dir /path/to/custom/directory
```

## 実行例

### 例1: 初回実行（Dry-run → 本実行）

```bash
# ステップ1: Dry-runで確認
$ python fix_inline_markup_spacing.py --dry-run
================================================================================
Inline Markup Spacing Fix Script
バッククォート（`）とシングルアスタリスク（*）の前後にスペースを追加
================================================================================

処理対象ディレクトリ: locales/ja/LC_MESSAGES
検出された.poファイル数: 234

⚠️  DRY-RUN モード: ファイルは変更されません

処理開始...

✓ ai/innovation_corner/innovation-corner.po
✓ programming_resources/tutorial_specific/blocks/blocks-tutorial.po
...

================================================================================
処理完了
================================================================================
処理ファイル数:         234
変更されたファイル数:   45
...
```

```bash
# ステップ2: 問題なければ本実行
$ python fix_inline_markup_spacing.py
...
✓ ファイルの変更が完了しました

次のステップ:
1. ビルドを実行して警告が減少したか確認:
   cd docs && make clean && make html-ja
2. 変更内容をgitで確認:
   git diff locales/
```

### 例2: ビルド前後での警告数比較

```bash
# ビルド前の警告数を記録
cd docs
make clean
make html-ja 2>&1 | grep -c "WARNING" > /tmp/warnings_before.txt

# スクリプト実行
cd ..
python fix_inline_markup_spacing.py

# ビルド後の警告数を記録
cd docs
make clean
make html-ja 2>&1 | grep -c "WARNING" > /tmp/warnings_after.txt

# 比較
echo "修正前の警告数: $(cat /tmp/warnings_before.txt)"
echo "修正後の警告数: $(cat /tmp/warnings_after.txt)"
```

## 出力形式

### 通常モード

```
================================================================================
Inline Markup Spacing Fix Script
バッククォート（`）とシングルアスタリスク（*）の前後にスペースを追加
================================================================================

処理対象ディレクトリ: locales/ja/LC_MESSAGES
検出された.poファイル数: 234

処理開始...

✓ ai/innovation_corner/innovation-corner.po
✓ programming_resources/tutorial_specific/blocks/blocks-tutorial.po
...

================================================================================
処理完了
================================================================================
処理ファイル数:         234
変更されたファイル数:   45

修正内容:
  バッククォート前にスペース追加:     87 箇所
  バッククォート後にスペース追加:     92 箇所
  シングルアスタリスク前にスペース追加: 123 箇所
  シングルアスタリスク後にスペース追加: 118 箇所
  合計修正箇所:                        420 箇所

✓ ファイルの変更が完了しました

次のステップ:
1. ビルドを実行して警告が減少したか確認:
   cd docs && make clean && make html-ja
2. 変更内容をgitで確認:
   git diff locales/
```

### 詳細モード（--verbose）

```
✓ ai/innovation_corner/innovation-corner.po
  バッククォート前スペース追加: 3 箇所
  バッククォート後スペース追加: 3 箇所
  アスタリスク前スペース追加: 5 箇所
  アスタリスク後スペース追加: 5 箇所
```

## 検証方法

### 1. 正規表現での検証

修正前後で問題のあるパターンが減少しているか確認：

```bash
# 修正前
grep -rP 'msgstr.*[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]`' locales/ja/LC_MESSAGES/ | wc -l

# スクリプト実行
python fix_inline_markup_spacing.py

# 修正後（減少しているはず）
grep -rP 'msgstr.*[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]`' locales/ja/LC_MESSAGES/ | wc -l
```

### 2. Sphinxビルドでの検証

```bash
cd docs

# 修正前のビルド
make clean
make html-ja 2>&1 | tee /tmp/build_before.log

# スクリプト実行
cd ..
python fix_inline_markup_spacing.py

# 修正後のビルド
cd docs
make clean
make html-ja 2>&1 | tee /tmp/build_after.log

# 警告数の比較
echo "=== 修正前の警告数 ==="
grep -c "WARNING.*Inline" /tmp/build_before.log

echo "=== 修正後の警告数 ==="
grep -c "WARNING.*Inline" /tmp/build_after.log
```

### 3. Gitでの変更確認

```bash
# 変更されたファイルを確認
git status

# 差分を確認
git diff locales/ja/LC_MESSAGES/

# 特定のファイルの変更を詳細に確認
git diff locales/ja/LC_MESSAGES/ai/innovation_corner/innovation-corner.po
```

## トラブルシューティング

### Q1: スクリプトが実行できない

**A**: Python 3が必要です。以下を確認してください：

```bash
python --version  # Python 3.x が表示されることを確認
```

Python 2の場合は、明示的に `python3` を使用：

```bash
python3 fix_inline_markup_spacing.py
```

### Q2: ディレクトリが見つからないエラー

```
エラー: ディレクトリが存在しません: locales/ja/LC_MESSAGES
```

**A**: スクリプトをリポジトリのルートディレクトリで実行してください：

```bash
cd /path/to/ftcdocs-ja
python fix_inline_markup_spacing.py
```

または、`--po-dir` オプションで正しいパスを指定：

```bash
python fix_inline_markup_spacing.py --po-dir /path/to/locales/ja/LC_MESSAGES
```

### Q3: 変更が多すぎて不安

**A**: まずは `--dry-run` で確認し、さらに `--verbose` で詳細を確認してください：

```bash
python fix_inline_markup_spacing.py --dry-run --verbose
```

問題なければ、小さい範囲でテスト実行：

```bash
# 1つのファイルだけコピーしてテスト
cp locales/ja/LC_MESSAGES/ai/innovation_corner/innovation-corner.po /tmp/test.po
mkdir -p /tmp/test_locales/ja/LC_MESSAGES/ai/innovation_corner/
mv /tmp/test.po /tmp/test_locales/ja/LC_MESSAGES/ai/innovation_corner/
python fix_inline_markup_spacing.py --po-dir /tmp/test_locales/ja/LC_MESSAGES
```

### Q4: ダブルアスタリスク（**）にもスペースが入ってしまう

**A**: このスクリプトは `**` を保護するように設計されています。
もし問題が発生した場合は、以下を確認してください：

1. スクリプトが最新版であること
2. `**` の前後に既にスペースがある場合、それは元々のテキストです

### Q5: エスケープ文字が壊れた

**A**: スクリプトは `\*` と `` \` `` を保護しますが、万が一問題が発生した場合：

```bash
# 変更を取り消し
git checkout locales/

# もう一度実行
python fix_inline_markup_spacing.py
```

## 注意事項

1. **バックアップ**: 初回実行前に、必ずバックアップを取るか、gitでコミットしてください
2. **Dry-run推奨**: 必ず `--dry-run` で動作確認してから本実行してください
3. **msgidは変更されません**: スクリプトは `msgstr` のみを変更し、`msgid`（原文）には一切手を加えません
4. **手動確認**: 自動修正後も、一部のケースでは手動での確認・調整が必要な場合があります

## 関連スクリプト

このリポジトリには他にも警告修正スクリプトがあります：

- `fix_asterisk_spacing.py` - ダブルアスタリスク（**）の前後にスペースを追加
- `tools/fix_inline_markup.py` - インラインマークアップの不一致を修正

## ライセンス

このスクリプトは、ftcdocs-jaプロジェクトの一部として、同じライセンスの下で提供されます。

## 作成日

2025-12-19

## 更新履歴

- 2025-12-19: 初版作成
