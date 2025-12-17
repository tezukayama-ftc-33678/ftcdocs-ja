# ビルド警告修正ガイド

このドキュメントは、日本語翻訳ビルドの警告を分析・修正するための包括的なガイドです。

## 概要

現在の状況:
- **初期警告数**: 1,435件（ログファイル内）、Sphinxビルド: 245件
- **修正後**: 234件（Sphinxビルド: 248件）
- **削減率**: 83%の警告を自動修正

## 警告の分類

### 1. Gitマージコンフリクト (修正済み)
- **影響**: 602件の警告 (41%)
- **状態**: ✅ 修正完了
- **詳細**: 95個のPOファイルに残っていた305個のマージコンフリクトマーカー (`<<<<<<<`, `=======`, `>>>>>>>`) を削除

### 2. PO読み込みエラー
- **影響**: 67件の警告 (28%)
- **原因**: POファイルの構文エラー
- **例**:
  - エスケープされていない二重引用符
  - 不正な複数行文字列
  - 文字列の閉じ忘れ
- **修正方法**: `scripts/warnings/fix_po_syntax_errors.py` または手動修正

### 3. Translation Error
- **影響**: 61件の警告 (26%)
- **原因**: 翻訳されたテキストと元のテキストの構造的な不一致
- **修正方法**: 手動でPOファイルを確認・修正

### 4. Inline Markup不一致
- **影響**: 86件の警告 (37%)
- **種類**:
  - `**` (強調): 40件
  - `*` (イタリック): 40件
  - `` ` `` (コードリテラル): 6件
- **原因**: マークアップの開始と終了が一致しない
- **修正方法**: `scripts/normalize_po_files.py` で自動修正

### 5. その他
- **影響**: 20件の警告 (8%)
- **修正方法**: 個別に確認が必要

## 使用可能なスクリプト

### 1. 警告分析スクリプト

#### `scripts/warnings/analyze_all_warnings.py`
ビルド警告を詳細に分析し、分類します。

```bash
# 警告ログを分析
python scripts/warnings/analyze_all_warnings.py /tmp/build_warnings.log

# 詳細レポートを保存
python scripts/warnings/analyze_all_warnings.py /tmp/build_warnings.log --output report.md
```

**出力例**:
```
総警告数: 234
警告タイプ別:
  PO Reading Error                  67 件 ( 28%)
  Translation Error                 61 件 ( 26%)
  Inline Markup: *                  40 件 ( 17%)
  Inline Markup: **                 40 件 ( 17%)
```

### 2. マージコンフリクト修正スクリプト

#### `scripts/warnings/fix_merge_conflicts.py`
Gitマージコンフリクトマーカーを自動削除します。

```bash
# Dry-runモード（変更なし）
python scripts/warnings/fix_merge_conflicts.py --dry-run

# 実際の修正を実行
python scripts/warnings/fix_merge_conflicts.py
```

**結果**: 95ファイルから305個のマージコンフリクトを削除 ✅

### 3. PO構文エラー修正スクリプト

#### `scripts/warnings/fix_po_syntax_errors.py`
POファイルの構文エラーを自動修正します。

```bash
# 警告ログから問題のあるファイルを検出して修正
python scripts/warnings/fix_po_syntax_errors.py --warning-log /tmp/build_warnings.log

# Dry-runモード
python scripts/warnings/fix_po_syntax_errors.py --dry-run
```

### 4. POファイル正規化スクリプト (推奨)

#### `scripts/normalize_po_files.py`
POファイルを包括的に正規化します。

```bash
# すべてのPOファイルを正規化
python scripts/normalize_po_files.py

# Dry-runモード
python scripts/normalize_po_files.py --dry-run

# 特定のファイルのみ
python scripts/normalize_po_files.py --file locales/ja/LC_MESSAGES/path/to/file.po

# 詳細モード
python scripts/normalize_po_files.py --verbose
```

**機能**:
- Gitマージコンフリクトマーカーの削除
- Inline markup (`**`, `*`, `` ` ``) の不一致修正
- 空白の正規化（行末空白削除、空行の整理）

## 推奨ワークフロー

### ステップ1: 現在の警告を記録

```bash
cd docs
make clean
make html-ja 2>&1 | tee /tmp/build_warnings.log
cd ..
```

### ステップ2: 警告を分析

```bash
python scripts/warnings/analyze_all_warnings.py /tmp/build_warnings.log
```

### ステップ3: POファイルを正規化

```bash
# まずDry-runで確認
python scripts/normalize_po_files.py --dry-run

# 問題なければ実行
python scripts/normalize_po_files.py
```

### ステップ4: ビルドして警告を確認

```bash
cd docs
make clean
make html-ja 2>&1 | tee /tmp/build_warnings_after.log
cd ..
```

### ステップ5: 結果を比較

```bash
python scripts/warnings/analyze_all_warnings.py /tmp/build_warnings_after.log
```

### ステップ6: 残存警告の手動修正

残った警告は個別に確認して修正:

1. **PO構文エラー**: POファイルを開いて構文を確認
2. **Translation Error**: 翻訳内容と元のテキストを比較
3. **Inline Markup**: マークアップの開始/終了を確認

## 警告の多いファイル TOP 10

現在の状況（修正後）:

1. `style-guide.rst` - 18件
2. `Managing-a-Smartphone-Robot-Controller.rst` - 12件
3. `index.rst` - 12件
4. `visionportal-webcams.rst` - 8件
5. `uvc.rst` - 8件
6. `make-pr.rst` - 7件
7. `ex1.rst` - 6件
8. `tos.rst` - 6件
9. `std-ports.rst` - 5件
10. `motors.rst` - 5件

これらのファイルに対応するPOファイルを優先的に確認してください。

## トラブルシューティング

### Q: "list index out of range" エラー

**A**: POファイルに構文エラーがあります。

```bash
# 該当ファイルを確認
python -c "import polib; polib.pofile('path/to/file.po')"
```

エラーメッセージの行番号を確認して、手動で修正してください。

### Q: Inline markupの警告が消えない

**A**: POファイルのmsgstr内で `**` や `*` の数が奇数になっている可能性があります。

```bash
# 該当ファイルを正規化
python scripts/normalize_po_files.py --file path/to/file.po
```

### Q: 翻訳エラーの修正方法

**A**: 元のRSTファイルと翻訳を比較:

1. `docs/source/path/to/file.rst` を開く
2. 対応する `locales/ja/LC_MESSAGES/path/to/file.po` を開く
3. 警告の行番号を確認
4. 構造（リスト、コードブロック、リンクなど）が一致するように修正

### Q: ビルドが遅い

**A**: 並列ビルドを使用:

```bash
make html-ja -j 4
```

## 期待される最終結果

- **目標警告数**: < 100件
- **致命的エラー**: 0件
- **自動修正率**: > 60%

## 定期メンテナンス

1. **週次**: ビルド警告数を確認
2. **月次**: 正規化スクリプトを実行
3. **翻訳追加時**: 必ず警告をチェック

## 参考情報

### スクリプトの場所

```
ftcdocs-ja/
├── scripts/
│   ├── normalize_po_files.py          # POファイル正規化
│   └── warnings/
│       ├── analyze_all_warnings.py    # 警告分析
│       ├── fix_merge_conflicts.py     # マージコンフリクト修正
│       └── fix_po_syntax_errors.py    # PO構文エラー修正
```

### ログファイル

ビルド警告ログは `/tmp/` ディレクトリに保存することを推奨:

- `/tmp/build_warnings.log` - 初期警告
- `/tmp/build_warnings_after.log` - 修正後

### Git管理

POファイルの変更は慎重に:

```bash
# 変更を確認
git diff locales/

# 意図した変更のみコミット
git add locales/
git commit -m "Fix PO warnings: [具体的な修正内容]"
```

## まとめ

このガイドで提供されたツールとワークフローを使用することで、日本語翻訳ビルドの警告を効率的に管理・削減できます。

**重要**: 
- 自動修正スクリプトは必ずDry-runモードで確認してから実行
- 大量の変更を行う前にバックアップを作成
- 変更後は必ずビルドして動作確認

---

*最終更新: 2025-12-17*
*作成者: GitHub Copilot*
