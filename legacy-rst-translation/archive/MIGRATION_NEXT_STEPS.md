# 次のステップ: .po-based Translation への移行

## 現在の状況

✅ 完了したこと:
- sphinx-intl のインストールと設定
- 移行ガイドの作成 (MIGRATION_TO_PO_GUIDE.md)
- 既存の日本語翻訳のスキャン (161ファイル、3258ブロック)
- 翻訳マッピングの抽出 (TRANSLATION_MAPPING.md)
- 移行スクリプトの作成

⚠️ 現在の問題:
- docs/source/ に既に日本語が含まれているため、.potファイルが生成できない
- .pot ファイルは英語版RST から生成する必要がある

## 🎯 次に必要なステップ

### オプション1: 完全な移行 (推奨)

この方法では、上流の英語版リポジトリと同期しながら.po翻訳システムへ移行します。

#### 1. 上流リポジトリを追加

```bash
# 公式の英語版リポジトリをリモートに追加
cd /home/runner/work/ftcdocs-ja/ftcdocs-ja
git remote add upstream https://github.com/FIRST-Tech-Challenge/ftcdocs.git
git fetch upstream
```

#### 2. 英語版RST を一時的に復元

```bash
# 現在の日本語版をバックアップブランチに保存
git checkout -b japanese-rst-backup

# メインブランチに戻る
git checkout copilot/migrate-to-standard-translation

# 英語版のRSTファイルをマージ（docsディレクトリのみ）
git checkout upstream/main -- docs/source

# コミット
git add docs/source
git commit -m "Restore English RST files from upstream for .pot generation"
```

#### 3. .pot ファイルを生成

```bash
cd docs
make gettext
```

これで `docs/build/gettext/` に .pot ファイルが生成されます。

#### 4. 日本語 .po ファイルを作成

```bash
sphinx-intl update -p build/gettext -l ja
```

これで `docs/locale/ja/LC_MESSAGES/` に .po ファイルが生成されます。

#### 5. 翻訳を .po ファイルに移行

`TRANSLATION_MAPPING.md` を参照しながら、翻訳を .po ファイルに手動でコピーします：

```po
# docs/locale/ja/LC_MESSAGES/index.po の例

# 英語
msgid "Welcome to FIRST Tech Challenge"
# 日本語翻訳を追加
msgstr "FIRST Tech Challenge へようこそ"

msgid "This is the official documentation"
msgstr "これは公式ドキュメントです"
```

**推奨ツール:**
- [Poedit](https://poedit.net/) - GUI .po エディタ
- VS Code の i18n Ally 拡張機能
- [Weblate](https://weblate.org/) - オンライン翻訳プラットフォーム

#### 6. 日本語版をビルド

```bash
cd docs
make -e SPHINXOPTS="-D language='ja'" html
```

または:

```bash
sphinx-build -D language=ja source build/html/ja
```

#### 7. ビルドを確認

```bash
# 生成されたHTMLを確認
firefox build/html/ja/index.html
# または
python -m http.server 8000 --directory build/html/ja
```

### オプション2: 段階的な移行

すべてを一度に移行するのではなく、少しずつ移行することもできます。

#### 手順:

1. **サンプルファイルで試す**
   ```bash
   # 1つのファイルだけ英語に戻す
   git checkout upstream/main -- docs/source/index.rst
   
   # .pot を生成してテスト
   sphinx-build -b gettext docs/source docs/build/gettext
   sphinx-intl update -p docs/build/gettext -l ja
   
   # index.po を翻訳
   vim docs/locale/ja/LC_MESSAGES/index.po
   
   # ビルドしてテスト
   make -e SPHINXOPTS="-D language='ja'" html
   ```

2. **徐々に拡張**
   - 少数のファイルで成功したら、セクションごとに移行
   - 各セクション: persona_pages、programming_resources など

3. **並行運用**
   - `.po` ベースの翻訳と直接RST翻訳を一時的に並行運用
   - 徐々に .po に移行

### オプション3: 自動化スクリプトを使用 (開発中)

将来的には、以下のような自動化が可能です：

```bash
# 英語版を取得し、既存の翻訳を自動的に .po にマップ
python scripts/auto_migrate_to_po.py \
  --upstream https://github.com/FIRST-Tech-Challenge/ftcdocs.git \
  --mapping TRANSLATION_MAPPING.md \
  --output docs/locale/ja
```

## 📊 移行の利点

### Before (現在の方法)
```
docs/source/index.rst    ← 日本語翻訳を直接編集
├── 上流の変更に対応困難
├── マージコンフリクトが頻発
└── どこが翻訳済みか不明
```

### After (.po ベース)
```
docs/source/index.rst           ← 英語のまま（上流と同期可能）
docs/locale/ja/LC_MESSAGES/
└── index.po                    ← 日本語翻訳を管理
    ├── 翻訳状態を追跡可能
    ├── 部分翻訳でもビルド可能
    └── 翻訳ツールを利用可能
```

## ⚙️ 今後のワークフロー

### 上流の変更を取り込む

```bash
# 1. 上流から変更を取得
git fetch upstream
git merge upstream/main

# 2. 新しい/変更された文字列を抽出
cd docs
make gettext

# 3. .po ファイルを更新
sphinx-intl update -p build/gettext -l ja

# 4. 変更された文字列を翻訳
# sphinx-intl が自動的に:
# - 新しい文字列: msgstr が空
# - 変更された文字列: "fuzzy" マーク
# - 削除された文字列: コメントアウト

# 5. 翻訳して確認
make -e SPHINXOPTS="-D language='ja'" html

# 6. コミット
git add locale/
git commit -m "翻訳: 上流の変更を反映"
```

### 新しいページを翻訳する

```bash
# 1. 上流に新しいページが追加されたら
git fetch upstream
git merge upstream/main

# 2. .pot を更新
cd docs
make gettext

# 3. .po を更新
sphinx-intl update -p build/gettext -l ja

# 4. 新しい .po ファイルを編集
vim locale/ja/LC_MESSAGES/new_page.po

# 5. ビルド
make -e SPHINXOPTS="-D language='ja'" html
```

## 🔍 よくある質問

### Q: 既存の翻訳はどうなりますか？

A: `TRANSLATION_MAPPING.md` に抽出されています。これを参照しながら .po ファイルに手動でコピーします。

### Q: 一度にすべてを移行する必要がありますか？

A: いいえ、段階的に移行できます。翻訳されていない部分は自動的に英語で表示されます。

### Q: 上流の変更はどのように追跡できますか？

A: `sphinx-intl update` を実行すると:
- 新しい msgid が追加される
- 変更された msgid は "fuzzy" マークされる
- 削除された msgid はコメントアウトされる

### Q: 複数人で翻訳する場合は？

A: .po ファイルを Git で管理するか、Weblate などのプラットフォームを使用します。

### Q: mainブランチはどうすればいいですか？

A: mainブランチは英語のまま（上流と同期）にし、日本語翻訳は locale/ja/ で管理します。これにより上流の変更を容易に取り込めます。

## 📝 推奨される次のアクション

1. **テスト移行** (1-2時間)
   - 小さなファイル（index.rst）で試す
   - ワークフローを理解する

2. **本格移行の決定** (議論)
   - チームで移行方針を決定
   - 完全移行 vs 段階的移行

3. **移行実行** (数日-数週間)
   - 選択した方法で実行
   - TRANSLATION_MAPPING.md を参照

4. **ドキュメント更新**
   - AI_TRANSLATION_GUIDE.md を .po ベースに更新
   - 新しいワークフローを文書化

## 🆘 サポート

問題が発生した場合:
1. MIGRATION_TO_PO_GUIDE.md を参照
2. GitHub Issue を作成
3. [Sphinx i18n ドキュメント](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)を参照

---

**重要**: この移行は一度の作業で、その後のメンテナンスが大幅に改善されます。段階的に進めることで、リスクを最小限に抑えられます。
