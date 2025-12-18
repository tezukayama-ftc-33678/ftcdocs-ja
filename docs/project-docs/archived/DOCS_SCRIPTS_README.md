# PO翻訳ファイル自動検証・修正ツール

このディレクトリには、Sphinx日本語翻訳ビルドの品質を保証するための自動化スクリプトが含まれています。

## スクリプト概要

### 1. `check_and_fix_po.py` - PO検証ツール

**用途**: 翻訳ファイル(.po)の問題を自動検出します。

**検出する問題**:
- `missing_doc_ref` (error): msgidに`:doc:`参照があるのにmsgstrに欠落
- `emphasis_mismatch` (warning): `**...**`などの強調記法のペア不一致
- `inconsistent_ref` (warning): 外部リンク(http://...)の欠落

**使い方**:
```powershell
# 基本スキャン（全POファイル）
cd h:\ftcdocs-ja\docs
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES

# 結果をJSONに出力
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues.json

# 詳細表示付き
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues.json --verbose
```

**出力例**:
```
🔍 Scanning 256 PO files...
  index.po: 11 issues found
  imu.po: 68 issues found
  ...

📊 Total issues found: 1622
  emphasis_mismatch: 1044
  inconsistent_ref: 433
  missing_doc_ref: 145

✅ Results written to ../po_issues.json
```

### 2. `fix_po_issues.py` - PO自動修正ツール

**用途**: 検出された問題を自動修正します（現在は報告のみ）。

**使い方**:
```powershell
# dry-runモード（変更なし、修正内容をプレビュー）
cd h:\ftcdocs-ja\docs
python scripts/fix_po_issues.py --issues ../po_issues.json --dry-run

# 実際に修正を適用（実装中）
python scripts/fix_po_issues.py --issues ../po_issues.json --type missing_doc_ref

# 全タイプ修正
python scripts/fix_po_issues.py --issues ../po_issues.json --type all
```

**オプション**:
- `--issues FILE`: 問題定義JSONファイル（check_and_fix_po.pyの出力）
- `--type TYPE`: 修正対象タイプ（missing_doc_ref | emphasis_mismatch | inconsistent_ref | all）
- `--dry-run`: 実際には変更せず、修正内容を表示のみ

### 3. `validate_build.py` - ビルド＆検証ラッパー

**用途**: ビルド実行と同時にPO検証を行います。

**使い方**:
```powershell
cd h:\ftcdocs-ja
python docs/scripts/validate_build.py
```

このスクリプトは自動的に以下を実行します:
1. `make html-ja` でSphinxビルド
2. ビルドログを `sphinx_build.log` に保存
3. `check_and_fix_po.py` でPO検証
4. 結果を `po_issues.json` に出力

## 推奨ワークフロー

### 1. 翻訳後の品質チェック
```powershell
# 1. POファイルをスキャン
cd h:\ftcdocs-ja\docs
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues.json --verbose

# 2. 重要度の高い問題を確認
# po_issues.json の "severity": "error" をチェック

# 3. ビルド実行
cd ..
make -C docs html-ja

# 4. 警告数を確認
# 出力に "ビルド 成功, XX 警告" が表示される
```

### 2. 問題の手動修正
```powershell
# po_issues.json を確認して該当POファイルを編集
# 例: locales/ja/LC_MESSAGES/index.po の行145を修正

# 修正後、再スキャンで確認
python docs/scripts/check_and_fix_po.py --po-dir locales/ja/LC_MESSAGES --output po_issues_fixed.json
```

### 3. ビルド前の自動チェック（CI/CD組み込み想定）
```powershell
# 検証スクリプト実行→問題があれば終了コード1
python docs/scripts/check_and_fix_po.py --po-dir locales/ja/LC_MESSAGES
if ($LASTEXITCODE -ne 0) {
    Write-Host "PO validation failed"
    exit 1
}

# ビルド実行
make -C docs clean
make -C docs html-ja
```

## 問題タイプ別の対処方法

### `missing_doc_ref` (最優先)
- **原因**: 翻訳時に`:doc:`ガイド`のような参照が削除された
- **影響**: Sphinx警告「inconsistent term references」が発生
- **修正**: msgid内の`:doc:`をmsgstrにも含める
- **例**:
  ```po
  # 間違い
  msgid "See the :doc:`Installation Guide </install/guide>` for details."
  msgstr "詳細はインストールガイドを参照してください。"
  
  # 正しい
  msgid "See the :doc:`Installation Guide </install/guide>` for details."
  msgstr "詳細は :doc:`インストールガイド </install/guide>` を参照してください。"
  ```

### `emphasis_mismatch` (警告)
- **原因**: `**強調**`のペアが不一致（開始マーカーのみ、終了マーカーのみなど）
- **影響**: レンダリング時に強調が正しく表示されない、または警告発生
- **修正**: msgidの`**`ペアをmsgstrでも維持
- **例**:
  ```po
  # 間違い
  msgid "This is **important** text."
  msgstr "これは重要なテキストです。"  # ** がない
  
  # 正しい
  msgid "This is **important** text."
  msgstr "これは **重要** なテキストです。"
  ```

### `inconsistent_ref` (情報)
- **原因**: 外部リンク(http://...)が翻訳時に削除された
- **影響**: ユーザーがリンクにアクセスできない
- **修正**: URLをmsgstrにも含める（通常URLは変更不要）

## トラブルシューティング

### エラー: "TypeError: unsupported operand type(s) for +=: 'NoneType' and 'str'"
- **原因**: PO構文解析エラー
- **対処**: 該当POファイルの構文をチェック（msgid/msgstrペア、引用符の閉じ忘れ）

### 警告: "File not found"
- **原因**: 相対パス解決の問題
- **対処**: スクリプト実行ディレクトリを確認（`h:\ftcdocs-ja\docs`から実行すること）

### 修正が反映されない
- **対処**: 
  1. `make clean` でビルドキャッシュをクリア
  2. `make html-ja` で再ビルド
  3. ブラウザのキャッシュもクリア（Ctrl+Shift+R）

## 今後の拡張

- [ ] `fix_po_issues.py` での実際の自動修正機能実装
- [ ] GitHub Actions CI統合（PR時に自動チェック）
- [ ] HTMLレンダリング結果の視覚的差分チェック
- [ ] 翻訳率カバレッジレポート生成
- [ ] 用語統一チェック（glossary.md連携）

## 関連ドキュメント

- [BUILD_JA.md](../../BUILD_JA.md) - 日本語ビルド手順
- [TRANSLATION_GUIDE.md](../../TRANSLATION_GUIDE.md) - 翻訳ガイドライン
- [Sphinx i18n documentation](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
