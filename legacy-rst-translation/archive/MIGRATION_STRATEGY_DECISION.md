# 移行戦略の決定: 推奨アプローチ

## 質問への回答

**現在のブランチでそのまま進めるべきか、mainブランチベースの新規ブランチで進めるべきか？**

## ✅ 推奨: mainブランチベースの新規ブランチで完全移行

### 理由

#### 1. mainブランチは既に英語版 🎯

確認結果:
```
main branch: docs/source/index.rst
- "Welcome to the *FIRST®* Tech Challenge Documentation!"
- 完全に英語のコンテンツ
```

**これは理想的な状態です！** mainブランチは既に上流（公式英語リポジトリ）と同期できる状態にあります。

#### 2. 現在のブランチ (copilot/migrate-to-standard-translation) の問題

- **日本語RSTが含まれている** (161ファイル、3,258ブロック)
- .poへの移行には、これらを英語に戻す必要がある
- 現在のブランチで進めると:
  - 161ファイル全てを英語に戻す作業が必要
  - 大量のファイル変更が発生
  - git historyが複雑になる

#### 3. mainブランチベースの利点

✅ **クリーンな開始**
- 既に英語版が揃っている
- 余計なファイル変更不要
- git historyがシンプル

✅ **作業が単純**
```bash
# mainから新規ブランチ作成
git checkout main
git checkout -b po-migration

# .pot生成
make gettext

# .po作成
make ja-update

# 翻訳を.poに移行
# (TRANSLATION_MAPPING.mdを参照)
```

✅ **レガシーブランチの保存**
- 現在のブランチ → `legacy/direct-translation`
- いつでも参照可能
- ロールバックも可能

## 📋 推奨手順

### ステップ1: レガシーブランチの保存

```bash
# 現在のブランチをlegacyとして保存
git branch legacy/direct-translation copilot/migrate-to-standard-translation
git push origin legacy/direct-translation
```

### ステップ2: mainベースの新規ブランチ作成

```bash
# mainブランチをチェックアウト
git fetch origin main
git checkout main

# 新規ブランチ作成
git checkout -b po-migration
```

### ステップ3: 移行インフラをmainにマージ

```bash
# 現在のPRの移行ツールとドキュメントをmainにマージ
git merge --no-ff copilot/migrate-to-standard-translation

# または、必要なファイルだけをチェリーピック
git checkout copilot/migrate-to-standard-translation -- \
  docs/Makefile \
  docs/requirements.txt \
  docs/scripts/migrate_translations_to_po.py \
  MIGRATION_*.md \
  PO_TRANSLATION_WORKFLOW.md \
  WHY_PO_TRANSLATION.md \
  QUICK_REFERENCE.md \
  PR_SUMMARY_FOR_USER.md \
  COMPARISON_OLD_VS_NEW.md \
  TRANSLATION_MAPPING.md
```

### ステップ4: .pot生成と.po作成

```bash
# docs/sourceは既に英語なので、そのまま.pot生成
cd docs
make gettext

# 日本語.po作成
make ja-update

# 確認
ls -la locale/ja/LC_MESSAGES/
```

### ステップ5: 翻訳の移行

```bash
# TRANSLATION_MAPPING.mdを参照しながら.poファイルに翻訳を追加
# ツールを使用: Poedit, VS Code, またはテキストエディタ

# 例: index.poの編集
vim locale/ja/LC_MESSAGES/index.po
```

### ステップ6: ビルドとテスト

```bash
# 日本語版をビルド
make ja-build

# 確認
python -m http.server 8000 --directory build/html/ja
```

### ステップ7: コミットとプッシュ

```bash
git add locale/ja/
git commit -m "翻訳: .poファイルに既存翻訳を移行"
git push origin po-migration
```

## 🔄 ブランチ構成（推奨）

```
origin
├── main                                  # 英語版（上流と同期）
├── po-migration                          # 新規: .po移行作業ブランチ
├── legacy/direct-translation             # レガシー: 日本語RST版
└── copilot/migrate-to-standard-translation # 現在のPR（マージ後削除）
```

## 📊 比較: 2つのアプローチ

### アプローチA: 現在のブランチで続行 ❌

```
現在のブランチ (日本語RST)
↓
161ファイルを英語に戻す (大量の変更)
↓
.pot生成
↓
.po作成
↓
翻訳移行
```

**デメリット:**
- 161ファイルの大量変更
- コミット履歴が複雑
- レビューが困難
- ロールバックが難しい

### アプローチB: mainベースの新規ブランチ ✅

```
main (既に英語)
↓
新規ブランチ作成 (po-migration)
↓
移行ツール追加 (小規模)
↓
.pot生成 (自動)
↓
.po作成 (自動)
↓
翻訳移行 (段階的)
```

**メリット:**
- ファイル変更は最小限
- コミット履歴がクリーン
- レビューが簡単
- ロールバック可能

## 💡 具体的な作業手順（推奨）

### 今すぐ実行すべきコマンド

```bash
# 1. レガシーブランチを保存
git branch legacy/direct-translation copilot/migrate-to-standard-translation
git push origin legacy/direct-translation

# 2. mainをチェックアウト
git fetch origin main
git checkout main

# 3. 新規ブランチ作成
git checkout -b po-migration

# 4. 移行ツールを追加（チェリーピック）
git checkout copilot/migrate-to-standard-translation -- \
  docs/Makefile \
  docs/requirements.txt \
  docs/scripts/migrate_translations_to_po.py \
  MIGRATION_TO_PO_GUIDE.md \
  MIGRATION_NEXT_STEPS.md \
  PO_TRANSLATION_WORKFLOW.md \
  QUICK_REFERENCE.md \
  WHY_PO_TRANSLATION.md \
  COMPARISON_OLD_VS_NEW.md \
  MIGRATION_SUMMARY.md \
  PR_SUMMARY_FOR_USER.md \
  TRANSLATION_MAPPING.md \
  MIGRATION_REPORT.md

# 5. コミット
git add .
git commit -m "Add .po migration infrastructure and documentation"

# 6. プッシュ
git push origin po-migration

# 7. .potと.po生成
cd docs
make gettext
make ja-update

# 8. 確認
ls -la locale/ja/LC_MESSAGES/

# 9. 最初の翻訳を追加（テスト）
vim locale/ja/LC_MESSAGES/index.po
# TRANSLATION_MAPPING.mdのindex.rstセクションを参照

# 10. ビルドしてテスト
make ja-build
python -m http.server 8000 --directory build/html/ja
```

## 🎯 最終的な状態

### mainブランチ
```
docs/source/
├── index.rst           # 英語
├── tutorial.rst        # 英語
└── ...                 # 全て英語

上流と同期可能 ✅
```

### po-migrationブランチ
```
docs/
├── source/             # 英語（mainと同じ）
│   ├── index.rst
│   └── ...
├── locale/ja/LC_MESSAGES/  # 日本語翻訳
│   ├── index.po
│   └── ...
└── Makefile            # 拡張版

完全な.poベースシステム ✅
```

### legacy/direct-translationブランチ
```
docs/source/
├── index.rst           # 日本語
├── tutorial.rst        # 日本語
└── ...                 # 日本語RST

参照用に保存 ✅
```

## ⚠️ 注意事項

1. **copilot/migrate-to-standard-translation ブランチの扱い**
   - 移行後は削除してOK
   - または `legacy/infrastructure-dev` として保存

2. **mainブランチは触らない**
   - mainは常に英語版
   - 上流と同期するため

3. **po-migrationブランチで作業**
   - すべての翻訳作業はこのブランチ
   - 完了後にmainにマージ

4. **段階的な翻訳移行**
   - 一度に全部やる必要なし
   - 優先度の高いページから

## 📈 期待される成果

### Before（現在のブランチで続行した場合）
- 161ファイルの変更
- 大量のコミット
- 複雑なgit history
- レビュー困難

### After（mainベース新規ブランチ）
- クリーンなgit history
- 段階的な移行
- レビューしやすい
- ロールバック可能

## ✅ 結論

**mainブランチベースの新規ブランチで完全移行することを強く推奨します。**

理由:
1. ✅ mainは既に英語版
2. ✅ 作業が最も単純
3. ✅ git historyがクリーン
4. ✅ レガシーは保存される
5. ✅ 上流との同期が容易

**次のアクション:**
1. 上記の「今すぐ実行すべきコマンド」を実行
2. TRANSLATION_MAPPING.mdを参照しながら翻訳を.poに移行
3. 段階的にコミット

---

## 📞 質問がある場合

このドキュメントに不明点があれば、GitHub Issueで質問してください。

**推奨アプローチで進めることで、最もスムーズに移行できます！** 🚀
