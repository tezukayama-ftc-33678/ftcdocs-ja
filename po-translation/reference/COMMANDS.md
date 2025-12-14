# .po 翻訳 コマンドリファレンス

このドキュメントは、.po翻訳で使用するすべてのコマンドの完全なリファレンスです。

---

## Make コマンド

### 基本コマンド

#### `make gettext`

英語RSTファイルから翻訳可能な文字列を抽出し、.potファイルを生成します。

```bash
cd docs
make gettext
```

**出力:** `docs/build/gettext/*.pot` ファイルが生成されます。

**使用タイミング:**
- 上流（英語版）の変更を取り込んだ後
- 新しいRSTファイルが追加されたとき
- 英語の文字列が変更されたとき

---

#### `make ja-update`

.potファイルから日本語.poファイルを生成/更新します。

```bash
cd docs
make ja-update
```

**出力:** `docs/locale/ja/LC_MESSAGES/*.po` ファイルが生成/更新されます。

**動作:**
- 新しい文字列 → 空の `msgstr ""` として追加
- 変更された文字列 → `#, fuzzy` フラグを付与
- 削除された文字列 → `#~` でコメントアウト

**使用タイミング:**
- `make gettext` の直後
- 翻訳を開始する前

---

#### `make ja-build`

日本語翻訳を適用してHTMLをビルドします。

```bash
cd docs
make ja-build
```

**出力:** `docs/build/html/ja/` に日本語HTMLが生成されます。

**使用タイミング:**
- 翻訳を追加/更新した後
- プレビューする前

---

#### `make ja-stats`

翻訳の進捗状況を表示します。

```bash
cd docs
make ja-stats
```

**出力例:**
```
locale/ja/LC_MESSAGES/index.po: 50 translated, 10 fuzzy, 5 untranslated messages.
locale/ja/LC_MESSAGES/tutorial.po: 100 translated messages.
...
```

**使用タイミング:**
- 翻訳進捗を確認したいとき
- どのファイルを優先すべきか判断するとき

---

### 組み合わせコマンド

```bash
# 完全なワークフロー
make gettext && make ja-update && make ja-build

# クリーンビルド
make clean && make gettext && make ja-update && make ja-build
```

---

## msgfmt コマンド

`.po`ファイルの検証と統計情報の取得に使用します。

### 統計情報の表示

```bash
# 特定ファイルの統計
msgfmt --statistics locale/ja/LC_MESSAGES/index.po

# 出力例:
# 50 translated messages, 10 fuzzy translations, 5 untranslated messages.
```

### 構文チェック

```bash
# .poファイルの構文をチェック
msgfmt -c locale/ja/LC_MESSAGES/index.po

# 詳細表示
msgfmt -c -v locale/ja/LC_MESSAGES/index.po
```

**エラーがある場合:**
```
index.po:123: 'msgstr' is not a valid C format string, unlike 'msgid'.
```

エラーメッセージに従って.poファイルを修正してください。

### すべての.poファイルをチェック

```bash
# すべての.poファイルの統計を表示
for po in locale/ja/LC_MESSAGES/*.po; do
    echo "=== $po ==="
    msgfmt --statistics "$po"
done
```

---

## grep コマンド

`.po`ファイル内の特定のパターンを検索します。

### 未翻訳エントリを探す

```bash
# 空のmsgstrを持つエントリ
grep -n 'msgstr ""' locale/ja/LC_MESSAGES/index.po

# 複数ファイルから検索
grep -r 'msgstr ""' locale/ja/LC_MESSAGES/
```

### Fuzzyエントリを探す

```bash
# fuzzyフラグが付いたエントリ
grep -n "fuzzy" locale/ja/LC_MESSAGES/index.po

# fuzzyとその次の2行を表示
grep -A 2 "fuzzy" locale/ja/LC_MESSAGES/index.po
```

### 特定の技術用語を検索

```bash
# OpModeを含むエントリ
grep -n "OpMode" locale/ja/LC_MESSAGES/index.po

# 大文字小文字を区別しない検索
grep -i "control hub" locale/ja/LC_MESSAGES/*.po
```

---

## Git コマンド

### 上流の変更を取り込む

```bash
# 上流のリポジトリを追加（初回のみ）
git remote add upstream https://github.com/FIRST-Tech-Challenge/ftcdocs.git

# 上流の変更を取得
git fetch upstream

# マージ
git merge upstream/main

# または、特定のブランチから
git merge upstream/v9.2
```

### 変更をコミット

```bash
# .poファイルをステージング
git add docs/locale/ja/

# コミット
git commit -m "翻訳: index, tutorial ページを更新"

# プッシュ
git push origin your-branch
```

### 差分を確認

```bash
# 変更されたファイルを確認
git status

# .poファイルの差分を表示
git diff docs/locale/ja/LC_MESSAGES/index.po

# 統計のみ表示
git diff --stat
```

---

## Python HTTPサーバー

ビルドしたHTMLをローカルでプレビューします。

```bash
# 日本語版をプレビュー
cd docs
python -m http.server 8000 --directory build/html/ja

# ブラウザで http://localhost:8000 を開く
```

**別のポートを使用:**
```bash
python -m http.server 8080 --directory build/html/ja
```

**終了:** Ctrl+C

---

## カスタムスクリプト

### AI翻訳支援

```bash
# 基本的な使い方
python po-translation/scripts/ai_translate_po.py \
  docs/locale/ja/LC_MESSAGES/index.po

# DeepL APIを使用
python po-translation/scripts/ai_translate_po.py \
  docs/locale/ja/LC_MESSAGES/index.po \
  --api deepl --api-key YOUR_API_KEY

# ドライラン（実行せずに確認）
python po-translation/scripts/ai_translate_po.py \
  docs/locale/ja/LC_MESSAGES/index.po \
  --dry-run
```

### 品質チェック

```bash
# 単一ファイルをチェック
python po-translation/scripts/check_po_quality.py \
  docs/locale/ja/LC_MESSAGES/index.po

# ディレクトリ全体をチェック
python po-translation/scripts/check_po_quality.py \
  docs/locale/ja/LC_MESSAGES/

# レポートを生成
python po-translation/scripts/check_po_quality.py \
  docs/locale/ja/LC_MESSAGES/ \
  --report quality_report.md
```

---

## 既存の翻訳支援スクリプト

プロジェクトには、従来のRST翻訳から引き継がれた便利なスクリプトもあります。

### RST構文チェック

```bash
python docs/scripts/validate_rst_syntax.py
```

### インラインマークアップ修正

```bash
# ドライラン
python docs/scripts/fix_rst_inline_markup.py --dry-run

# 実行
python docs/scripts/fix_rst_inline_markup.py
```

### ビルド警告チェック

```bash
python docs/scripts/check_build_warnings.py --verbose
```

---

## 便利なエイリアス

`.bashrc` や `.zshrc` に以下を追加すると便利です：

```bash
# .po翻訳ワークフロー
alias po-update='cd docs && make gettext && make ja-update && cd ..'
alias po-build='cd docs && make ja-build && cd ..'
alias po-stats='cd docs && make ja-stats && cd ..'
alias po-preview='cd docs && python -m http.server 8000 --directory build/html/ja'

# 完全なワークフロー
alias po-full='cd docs && make gettext && make ja-update && make ja-build && cd ..'
```

使用例:
```bash
po-update   # 翻訳ファイルを更新
# [.poファイルを編集]
po-build    # ビルド
po-preview  # プレビュー
```

---

## トラブルシューティングコマンド

### ビルドエラーの場合

```bash
# クリーンビルド
cd docs
make clean
make gettext
make ja-build

# エラーログを保存
make ja-build 2>&1 | tee build_error.log
```

### .poファイルの構文エラー

```bash
# すべての.poファイルを検証
for po in locale/ja/LC_MESSAGES/*.po; do
    echo "Checking $po"
    msgfmt -c "$po" || echo "ERROR in $po"
done
```

### 翻訳が反映されない

```bash
# 1. .poファイルのmsgstrが空でないか確認
grep -A 1 "msgid \"Your text\"" locale/ja/LC_MESSAGES/index.po

# 2. クリーンビルド
make clean && make ja-build

# 3. ブラウザのキャッシュをクリア
```

---

## よく使うコマンドの組み合わせ

### 日常的な翻訳作業

```bash
# 1. 上流の変更を取り込む
git fetch upstream
git merge upstream/main

# 2. 翻訳ファイルを更新
cd docs
make gettext && make ja-update

# 3. 変更を確認
make ja-stats

# 4. [.poファイルを編集]

# 5. ビルドとプレビュー
make ja-build
python -m http.server 8000 --directory build/html/ja

# 6. コミット
cd ..
git add docs/locale/ja/
git commit -m "翻訳: 更新"
git push
```

### 新しいページを翻訳

```bash
# 1. .pot/.poを生成
cd docs
make gettext && make ja-update

# 2. 新しい.poファイルを確認
git status

# 3. [新しい.poファイルを編集]

# 4. ビルドして確認
make ja-build
```

### 翻訳進捗の確認

```bash
# 全体の統計
cd docs
make ja-stats

# または、カスタムスクリプトで詳細チェック
cd ..
python po-translation/scripts/check_po_quality.py \
  docs/locale/ja/LC_MESSAGES/ \
  --report progress_report.md
```

---

## チートシート

### コピー&ペースト用コマンド

```bash
# 完全なワークフロー
git fetch upstream && \
git merge upstream/main && \
cd docs && \
make gettext && \
make ja-update && \
make ja-stats
# ↑ ここで .poファイルを編集 ↓
make ja-build && \
python -m http.server 8000 --directory build/html/ja
```

### 1行コマンド集

```bash
# すべての未翻訳エントリを数える
grep -r 'msgstr ""' docs/locale/ja/LC_MESSAGES/ | wc -l

# すべてのfuzzyエントリを数える
grep -r "fuzzy" docs/locale/ja/LC_MESSAGES/ | wc -l

# 翻訳完了率を計算（簡易版）
for po in docs/locale/ja/LC_MESSAGES/*.po; do msgfmt --statistics "$po" 2>&1; done

# 最近変更された.poファイルを表示
ls -lt docs/locale/ja/LC_MESSAGES/*.po | head -10
```

---

## 参考リンク

- [Sphinx i18n](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx-intl](https://sphinx-intl.readthedocs.io/)
- [GNU gettext](https://www.gnu.org/software/gettext/manual/)
- [PO file format](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)

---

**このリファレンスをブックマークして、翻訳作業中に参照してください！**
