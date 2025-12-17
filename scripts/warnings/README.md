# 警告修正スクリプト

このディレクトリには、日本語翻訳ビルドの警告を分析・修正するためのスクリプトが含まれています。

## スクリプト一覧

### 1. analyze_all_warnings.py
**用途**: ビルド警告を詳細に分析

**機能**:
- 警告をタイプ別に分類
- ファイル別の警告数を集計
- 修正推奨事項を生成
- 詳細レポートをMarkdown形式で保存

**使用方法**:
```bash
# 基本的な分析
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
```

### 2. fix_merge_conflicts.py
**用途**: Gitマージコンフリクトマーカーを自動削除

**機能**:
- POファイル内の `<<<<<<<`, `=======`, `>>>>>>>` マーカーを検出
- HEAD側のコンテンツを保持して競合を解決
- Dry-runモード対応

**使用方法**:
```bash
# Dry-run（変更なし）
python scripts/warnings/fix_merge_conflicts.py --dry-run

# 実際の修正を実行
python scripts/warnings/fix_merge_conflicts.py

# 特定のディレクトリを指定
python scripts/warnings/fix_merge_conflicts.py --locales-dir path/to/locales
```

**実績**: 95ファイルから305個のマージコンフリクトを削除

### 3. fix_po_syntax_errors.py
**用途**: POファイルの構文エラーを自動修正

**機能**:
- エスケープされていない二重引用符を修正
- 不正な複数行文字列を修正
- 警告ログから問題のあるファイルを自動検出

**使用方法**:
```bash
# 警告ログから自動検出して修正
python scripts/warnings/fix_po_syntax_errors.py --warning-log /tmp/build_warnings.log

# Dry-run
python scripts/warnings/fix_po_syntax_errors.py --dry-run --warning-log /tmp/build_warnings.log
```

### 4. fix_po_newlines.py
**用途**: POファイルの改行エラーを修正

**機能**:
- msgid/msgstrの後に改行が欠けている場合を修正
- 警告ログから問題のあるファイルを検出

**使用方法**:
```bash
# 警告ログから自動検出して修正
python scripts/warnings/fix_po_newlines.py --warning-log /tmp/build_warnings.log

# Dry-run
python scripts/warnings/fix_po_newlines.py --dry-run
```

### 5. summarize_warnings.py (既存)
**用途**: 警告の簡単な集計

**機能**:
- 警告数を集計
- タイプ別の統計を表示
- UTF-16 LEエンコーディング対応

**使用方法**:
```bash
python scripts/warnings/summarize_warnings.py
```

**注**: このスクリプトは `build_warnings.log` を現在のディレクトリで探します。

## 推奨ワークフロー

### 初回セットアップ

```bash
# 1. 現在の警告を記録
cd docs
make clean
make html-ja 2>&1 | tee /tmp/build_warnings.log
cd ..

# 2. 警告を分析
python scripts/warnings/analyze_all_warnings.py /tmp/build_warnings.log
```

### 警告修正

```bash
# 3. マージコンフリクトを修正（最優先）
python scripts/warnings/fix_merge_conflicts.py

# 4. POファイルを正規化（推奨）
python scripts/normalize_po_files.py

# 5. 改行エラーを修正
python scripts/warnings/fix_po_newlines.py --warning-log /tmp/build_warnings.log

# 6. ビルドして結果を確認
cd docs
make clean
make html-ja 2>&1 | tee /tmp/build_warnings_after.log
cd ..

# 7. 改善を確認
python scripts/warnings/analyze_all_warnings.py /tmp/build_warnings_after.log
```

## スクリプトの依存関係

### 必須
- Python 3.7以上
- polib (`pip install polib`)

### オプション
- なし（標準ライブラリのみ使用）

## トラブルシューティング

### Q: "ModuleNotFoundError: No module named 'polib'"

**A**: polibをインストール:
```bash
pip install polib
```

### Q: スクリプトが警告ログを見つけられない

**A**: 明示的にパスを指定:
```bash
python scripts/warnings/analyze_all_warnings.py /path/to/build_warnings.log
```

### Q: Dry-runで動作確認したい

**A**: すべてのスクリプトは `--dry-run` オプションに対応:
```bash
python scripts/warnings/fix_merge_conflicts.py --dry-run
python scripts/normalize_po_files.py --dry-run
```

### Q: 特定のファイルだけ処理したい

**A**: `--file` オプションを使用（対応しているスクリプトのみ）:
```bash
python scripts/normalize_po_files.py --file path/to/file.po
```

## 警告タイプの説明

### Git Merge Conflict
- **原因**: マージ時のコンフリクトマーカーが残存
- **修正**: `fix_merge_conflicts.py`で自動削除

### PO Reading Error
- **原因**: POファイルの構文エラー
- **修正**: `fix_po_syntax_errors.py`または手動修正

### Line Start Mismatch
- **原因**: POファイルの行頭が期待されるキーワードと一致しない
- **修正**: 通常、マージコンフリクト削除で解決

### Translation Error
- **原因**: 翻訳と元のテキストの構造的な不一致
- **修正**: 手動でPOファイルを確認・修正

### Inline Markup
- **原因**: `**`, `*`, `` ` `` の開始と終了が一致しない
- **修正**: `normalize_po_files.py`で自動修正

## 統計

### 実績（初回実行）

- **初期警告数**: 1,435件
- **修正後**: 234件
- **削減率**: 83%

### 修正内訳

| 修正タイプ | 件数 | スクリプト |
|-----------|------|-----------|
| マージコンフリクト | 602 | fix_merge_conflicts.py |
| Inline markup | 13 | normalize_po_files.py |
| 空白正規化 | 22 | normalize_po_files.py |

## 関連ドキュメント

- [BUILD_WARNINGS_REPORT.md](../../BUILD_WARNINGS_REPORT.md) - 包括的なレポート
- [WARNING_FIX_GUIDE.md](../../docs/WARNING_FIX_GUIDE.md) - 詳細ガイド
- [BUILD_WARNINGS_SUMMARY.md](../../guides/BUILD_WARNINGS_SUMMARY.md) - 既存サマリー

## コントリビューション

新しいスクリプトを追加する場合:

1. このREADMEを更新
2. `--dry-run` オプションを実装
3. `--help` で使用方法を表示
4. エラーハンドリングを実装

## ライセンス

プロジェクトのライセンスに従います。

---

*最終更新: 2025-12-17*
