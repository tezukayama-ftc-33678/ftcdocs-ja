# クイックスタートガイド - ビルド警告修正

## 最速で警告を削減する方法

### ステップ1: 現在の状態を確認（1分）

```bash
cd docs
make html-ja 2>&1 | grep "build succeeded"
cd ..
```

現在の警告数が表示されます（例: "build succeeded, 248 warnings."）

### ステップ2: 自動修正を実行（5分）

```bash
# POファイルを正規化（推奨）
python scripts/normalize_po_files.py

# または個別に実行
python scripts/warnings/fix_merge_conflicts.py
python scripts/warnings/fix_po_newlines.py
```

### ステップ3: 結果を確認（1分）

```bash
cd docs
make clean && make html-ja 2>&1 | grep "build succeeded"
cd ..
```

警告数が減少していることを確認

## コマンド一覧

### 基本コマンド

```bash
# ビルドして警告を記録
cd docs && make clean && make html-ja 2>&1 | tee /tmp/warnings.log && cd ..

# 警告を分析
python scripts/warnings/analyze_all_warnings.py /tmp/warnings.log

# POファイルを正規化（最も推奨）
python scripts/normalize_po_files.py

# マージコンフリクトを修正
python scripts/warnings/fix_merge_conflicts.py

# 改行エラーを修正
python scripts/warnings/fix_po_newlines.py
```

### Dry-runモード（変更なし）

```bash
# 変更内容を確認してから実行
python scripts/normalize_po_files.py --dry-run
python scripts/warnings/fix_merge_conflicts.py --dry-run
python scripts/warnings/fix_po_newlines.py --dry-run
```

### 詳細モード

```bash
# 詳細な出力
python scripts/normalize_po_files.py --verbose

# 詳細レポートを保存
python scripts/warnings/analyze_all_warnings.py /tmp/warnings.log --output report.md
```

## よくある質問

### Q: 何から始めればいい？

**A**: 以下の順番で実行してください：

1. `python scripts/normalize_po_files.py`
2. ビルドして確認
3. 必要に応じて手動修正

### Q: どのくらい警告が減る？

**A**: 自動修正で約80-90%の警告を削減できます。

- Gitマージコンフリクト: 100%削減（約600件）
- Inline markup: 約15%削減（約13件）
- 空白: 正規化（約22件）

### Q: エラーが出た場合は？

**A**: まず `--dry-run` で確認してください：

```bash
python scripts/normalize_po_files.py --dry-run
```

問題がある場合は、個別のスクリプトを実行：

```bash
python scripts/warnings/fix_merge_conflicts.py
python scripts/warnings/fix_po_newlines.py
```

### Q: 特定のファイルだけ修正したい

**A**: `--file` オプションを使用：

```bash
python scripts/normalize_po_files.py --file locales/ja/LC_MESSAGES/path/to/file.po
```

### Q: 手動で確認したいファイルは？

**A**: 警告分析で上位ファイルを確認：

```bash
python scripts/warnings/analyze_all_warnings.py /tmp/warnings.log
```

出力例：
```
警告の多いファイル TOP 20:
  style-guide.rst                    18 件
  Managing-a-Smartphone-Robot-Controller.rst  12 件
  index.rst                          12 件
```

これらのファイルに対応するPOファイルを優先的に確認してください。

## トラブルシューティング

### "ModuleNotFoundError: No module named 'polib'"

```bash
pip install polib
```

### ビルドが失敗する

```bash
cd docs
pip install -r requirements.txt
make clean
make html-ja
```

### 警告が減らない

1. `git status` で変更を確認
2. `git diff` で内容を確認
3. 必要に応じて `git add` してコミット

## 詳細ドキュメント

より詳しい情報は以下を参照：

- **[BUILD_WARNINGS_REPORT.md](BUILD_WARNINGS_REPORT.md)** - 包括的なレポート
- **[WARNING_FIX_GUIDE.md](docs/WARNING_FIX_GUIDE.md)** - 詳細ガイド
- **[scripts/warnings/README.md](scripts/warnings/README.md)** - スクリプトの使用方法

## 成果

このプロジェクトで達成したこと：

- ✅ **警告を83%削減**: 1,435件 → 234件
- ✅ **95個のPOファイル**から305個のマージコンフリクトを削除
- ✅ **5つの自動修正スクリプト**を作成
- ✅ **包括的なドキュメント**を作成

## サポート

問題や質問がある場合は、GitHubのIssuesで報告してください。

---

*最終更新: 2025-12-17*
