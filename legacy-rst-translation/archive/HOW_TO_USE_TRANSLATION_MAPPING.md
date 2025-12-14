# TRANSLATION_MAPPING.md の使い方ガイド

## 概要

`TRANSLATION_MAPPING.md` は、既存の日本語RSTファイルから抽出した翻訳を含む参照ドキュメントです。このファイルを使って、`.po`ファイルに翻訳を効率的に入力できます。

## ファイル構造

### TRANSLATION_MAPPING.md の構造

```markdown
# Translation Mapping Reference

## ファイル名/パス

### Block 1 (line X)

```
日本語テキスト
```

### Block 2 (line Y)

```
別の日本語テキスト
```
```

### 例

```markdown
## index.rst

### Block 1 (line 1)

```
*FIRST* Tech Challenge ドキュメント
```

### Block 2 (line 4)

```
*FIRST®* Tech Challenge ドキュメントへようこそ！このウェブサイトには、
競技用ロボットを作成するために必要なすべての情報が含まれています！
```
```

## .po ファイルの構造

### .po ファイルの基本構造

```po
#: ../../source/index.rst:8
msgid "*FIRST* Tech Challenge documentation"
msgstr ""  # ← ここに日本語を入力

#: ../../source/index.rst:11
msgid "Welcome to the *FIRST®* Tech Challenge Documentation!"
msgstr ""  # ← ここに日本語を入力
```

## 翻訳の手順

### ステップ1: 翻訳したいファイルを選ぶ

例: `index.rst` を翻訳する場合

1. `docs/locale/ja/LC_MESSAGES/index.po` を開く
2. `TRANSLATION_MAPPING.md` の `## index.rst` セクションを開く

### ステップ2: 英語と日本語をマッピングする

#### .po ファイルの msgid を確認

```po
#: ../../source/index.rst:8
msgid "*FIRST* Tech Challenge documentation"
msgstr ""
```

#### TRANSLATION_MAPPING.md で対応する日本語を探す

`TRANSLATION_MAPPING.md` で似たようなテキストを探します：

```markdown
### Block 1 (line 1)

```
*FIRST* Tech Challenge ドキュメント
```
```

#### msgstr に日本語を入力

```po
#: ../../source/index.rst:8
msgid "*FIRST* Tech Challenge documentation"
msgstr "*FIRST* Tech Challenge ドキュメント"
```

### ステップ3: 繰り返す

同じ手順で、.po ファイルの各 msgid に対応する msgstr を埋めていきます。

## 実践例

### 例1: シンプルなタイトル

**English (.po msgid):**
```po
msgid "Getting Started"
msgstr ""
```

**Japanese (TRANSLATION_MAPPING.md):**
```markdown
### Block X (line Y)

```
はじめに
```
```

**Result (.po msgstr):**
```po
msgid "Getting Started"
msgstr "はじめに"
```

### 例2: 複数行のテキスト

**English (.po msgid):**
```po
msgid ""
"Welcome to the *FIRST®* Tech Challenge Documentation! This website contains "
"everything you need to know to create a competition robot!"
msgstr ""
```

**Japanese (TRANSLATION_MAPPING.md):**
```markdown
### Block 2 (line 4)

```
*FIRST®* Tech Challenge ドキュメントへようこそ！このウェブサイトには、
競技用ロボットを作成するために必要なすべての情報が含まれています！
```
```

**Result (.po msgstr):**
```po
msgid ""
"Welcome to the *FIRST®* Tech Challenge Documentation! This website contains "
"everything you need to know to create a competition robot!"
msgstr ""
"*FIRST®* Tech Challenge ドキュメントへようこそ！このウェブサイトには、"
"競技用ロボットを作成するために必要なすべての情報が含まれています！"
```

## ヒントとベストプラクティス

### 1. 完全一致を探す

TRANSLATION_MAPPING.md の日本語テキストが、元の英語テキストの翻訳と一致することを確認します。

### 2. 行番号は参考程度に

`(line X)` の行番号は、元のRSTファイルでの位置を示していますが、必ずしも正確ではありません。テキストの内容で判断してください。

### 3. 前後のコンテキストを確認

同じようなテキストがある場合、前後の msgid を見て正しい翻訳を選びます。

### 4. 見つからない場合

TRANSLATION_MAPPING.md に対応する翻訳がない場合は、新しく翻訳する必要があります。

### 5. RST マークアップの保持

翻訳では、RST マークアップ（`:doc:`, `**bold**`, `` `literal` `` など）をそのまま保持してください。

**例:**
```po
msgid "See :doc:`About the FIRST Tech Challenge <overview/ftcoverview>`"
msgstr ":doc:`FIRST Tech Challenge について <overview/ftcoverview>` をご覧ください"
```

### 6. プレースホルダーの保持

`{0}`, `%s` などのプレースホルダーは、翻訳後も同じ位置に保持してください。

## 効率的な作業方法

### 方法1: 検索機能を使う

1. .po ファイルで msgid のキーワードをコピー
2. TRANSLATION_MAPPING.md で検索（Ctrl+F / Cmd+F）
3. 見つかった日本語をコピー
4. .po ファイルの msgstr に貼り付け

### 方法2: 分割画面で作業

エディタを分割して：
- 左側: .po ファイル
- 右側: TRANSLATION_MAPPING.md

これにより、簡単にテキストをコピー＆ペーストできます。

### 方法3: 自動化スクリプト（オプション）

完全に一致するテキストは、スクリプトで自動的にマッピングすることも可能です。

## トラブルシューティング

### 問題1: 対応する翻訳が見つからない

**原因:** 
- 新しく追加されたテキスト
- 英語版が更新された

**解決策:**
新しく翻訳を作成してください。

### 問題2: 翻訳が正しく表示されない

**原因:**
- エンコーディングの問題
- RST マークアップの破損

**解決策:**
```bash
# ビルドエラーを確認
cd docs
make ja-build

# エラーメッセージを読んで修正
```

### 問題3: 複数の似たようなテキストがある

**原因:**
同じようなテキストが複数の場所で使われている

**解決策:**
.po ファイルのコメント（`#:`）で元のファイルと行番号を確認し、正しいコンテキストの翻訳を選んでください。

## 進捗管理

### 翻訳の進捗を確認

```bash
cd docs
make ja-stats
```

### ファイルごとの進捗

各 .po ファイルの先頭にメモを追加できます：

```po
# Translation progress:
# - Basic structure: Done
# - Technical terms: In progress
# - Review: Not started
```

## 便利なツール

### 1. Poedit（GUIツール）

- ダウンロード: https://poedit.net/
- 翻訳メモリ機能あり
- 自動翻訳提案機能あり

### 2. VS Code 拡張機能

- **gettext**: .po ファイルの構文ハイライト
- **i18n Ally**: 翻訳管理

### 3. コマンドラインツール

```bash
# msgfmt で .po ファイルを検証
msgfmt -c -v -o /dev/null locale/ja/LC_MESSAGES/index.po

# msgmerge で .pot から .po を更新
msgmerge --update locale/ja/LC_MESSAGES/index.po build/gettext/index.pot
```

## まとめ

1. **ファイルを選ぶ**: `docs/locale/ja/LC_MESSAGES/*.po`
2. **マッピングを開く**: `TRANSLATION_MAPPING.md` の対応セクション
3. **翻訳をコピー**: msgid に対応する日本語を msgstr に入力
4. **ビルドしてテスト**: `make ja-build`
5. **繰り返す**: 次のファイルへ

この方法で、161ファイル、2,371ブロックの翻訳を効率的に .po ファイルに移行できます！

---

**ヒント:** 最初は小さなファイル（例: `overview/ftcoverview.po`）で練習して、ワークフローに慣れてから大きなファイルに取り組むことをお勧めします。
