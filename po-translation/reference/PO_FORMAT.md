# .po ファイル形式リファレンス

このドキュメントは、.poファイルの構造と仕様を詳しく説明します。

---

## 📚 .poファイルとは

**.po (Portable Object)** ファイルは、GNU gettextで使用される国際化（i18n）の標準フォーマットです。

### 特徴

- **プレーンテキスト** - 任意のエディタで編集可能
- **バージョン管理に適している** - Gitで差分管理が容易
- **標準フォーマット** - 多くのツールでサポート
- **メタデータを含む** - ファイル情報、翻訳者情報等

---

## 基本構造

### 最小限の.poファイル

```po
# Translation file header
msgid ""
msgstr ""
"Language: ja\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: source/index.rst:5
msgid "Welcome"
msgstr "ようこそ"
```

---

## ヘッダー

### ファイルヘッダー

すべての.poファイルは、メタデータを含むヘッダーから始まります。

```po
# FIRST Tech Challenge Documentation
# Copyright (C) 2024
# This file is distributed under the same license as the ftcdocs package.
msgid ""
msgstr ""
"Project-Id-Version: ftcdocs\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2024-12-14 10:00+0000\n"
"PO-Revision-Date: 2024-12-14 15:00+0900\n"
"Last-Translator: Your Name <your.email@example.com>\n"
"Language-Team: Japanese\n"
"Language: ja\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
```

### 主要なヘッダーフィールド

| フィールド | 説明 | 例 |
|-----------|------|-----|
| `Project-Id-Version` | プロジェクト名とバージョン | `ftcdocs` |
| `POT-Creation-Date` | .potファイルの生成日時 | `2024-12-14 10:00+0000` |
| `PO-Revision-Date` | .poファイルの最終更新日時 | `2024-12-14 15:00+0900` |
| `Last-Translator` | 最終翻訳者 | `Your Name <email>` |
| `Language` | 言語コード | `ja` |
| `Content-Type` | 文字エンコーディング | `text/plain; charset=UTF-8` |

---

## エントリ（翻訳単位）

### 基本的なエントリ

```po
#: source/index.rst:10
msgid "Documentation"
msgstr "ドキュメント"
```

**構成要素:**
- `#:` - コメント（元のファイルと行番号）
- `msgid` - 翻訳元のテキスト（英語）
- `msgstr` - 翻訳後のテキスト（日本語）

---

## コメント

### コメントの種類

```po
# Translator comment（翻訳者のコメント）
#. Extracted comment（抽出されたコメント、ソースコードから）
#: source/file.rst:10（参照、ファイル名と行番号）
#, fuzzy（フラグ、確認が必要）
#| msgid "Old text"（以前のmsgid、変更履歴）
#~ msgid "Removed"（削除されたエントリ）
```

### 例

```po
# この文は初心者向けなので、わかりやすく訳す
#. This is an important note for beginners
#: source/tutorial.rst:15
msgid "This is your first program"
msgstr "これがあなたの最初のプログラムです"
```

---

## msgid と msgstr

### 単一行

```po
msgid "Short text"
msgstr "短いテキスト"
```

### 複数行

長いテキストは複数行に分割できます。

```po
msgid ""
"This is a very long text that spans "
"multiple lines in the documentation."
msgstr ""
"これはドキュメント内で複数行にわたる "
"非常に長いテキストです。"
```

**ルール:**
- 最初の行は空の文字列 `""`
- 各行は `"` で囲む
- 行末の改行は明示的に `\n` で指定（通常は不要）

---

## 特殊文字

### エスケープシーケンス

| シーケンス | 意味 |
|-----------|------|
| `\n` | 改行 |
| `\t` | タブ |
| `\"` | ダブルクォート |
| `\\` | バックスラッシュ |

### 例

```po
msgid "Line 1\nLine 2"
msgstr "1行目\n2行目"

msgid "He said \"Hello\""
msgstr "彼は「こんにちは」と言いました"
```

---

## フラグ

### Fuzzy（あいまい）

翻訳が古い可能性がある、または確認が必要なエントリ。

```po
#, fuzzy
msgid "This text has been updated"
msgstr "このテキストは更新されました"
```

**処理:**
1. 翻訳を確認
2. 必要に応じて更新
3. `#, fuzzy` 行を削除

### その他のフラグ

```po
#, c-format
msgid "You have %d items"
msgstr "アイテムが %d 個あります"

#, no-c-format
msgid "100% complete"
msgstr "100% 完了"
```

---

## 削除されたエントリ

英語版で削除された文字列は、`#~` でコメントアウトされます。

```po
#~ msgid "This feature was removed"
#~ msgstr "この機能は削除されました"
```

**処理:**
- 通常は無視してOK
- ファイルサイズが気になる場合は削除可能
- 次回の `make ja-update` で完全に削除される

---

## 複数形（Plural Forms）

英語には単数形と複数形があります。

```po
msgid "You have %d robot"
msgid_plural "You have %d robots"
msgstr[0] "ロボットが %d 台あります"
```

**日本語の場合:**
- 日本語には複数形の概念がないため、`msgstr[0]` のみを使用
- 同じ翻訳を複数のフォームに適用する場合もある

---

## RSTマークアップ

.poファイル内では、RSTマークアップがそのまま保持されます。

### インラインマークアップ

```po
msgid "This is **bold** text"
msgstr "これは **太字** のテキストです"

msgid "Use the ``code`` function"
msgstr "``code`` 関数を使用します"
```

### ディレクティブ

```po
msgid "See :doc:`Introduction <intro>` for details"
msgstr "詳細は :doc:`入門 <intro>` を参照してください"

msgid "Refer to :ref:`configuration <config>`"
msgstr ":ref:`設定 <config>` を参照してください"
```

**重要:** RSTマークアップは変更せずに保持してください。

---

## 変数とプレースホルダー

### Python形式

```po
msgid "Welcome, %(name)s!"
msgstr "ようこそ、%(name)s さん！"
```

### C形式

```po
msgid "Version %s"
msgstr "バージョン %s"
```

**ルール:** プレースホルダーは翻訳せず、そのまま保持してください。

---

## ファイルエンコーディング

### UTF-8（推奨）

```po
"Content-Type: text/plain; charset=UTF-8\n"
```

すべての.poファイルはUTF-8エンコーディングを使用すべきです。

### BOMなし

- UTF-8 BOMは使用しない
- プレーンなUTF-8を使用

---

## 翻訳の状態

### 完全な翻訳

```po
msgid "Documentation"
msgstr "ドキュメント"
```

### 未翻訳

```po
msgid "New feature"
msgstr ""
```

### Fuzzy（要確認）

```po
#, fuzzy
msgid "Updated text"
msgstr "古い翻訳"
```

### 削除済み

```po
#~ msgid "Removed"
#~ msgstr "削除済み"
```

---

## ツールとの互換性

### msgfmt（検証）

```bash
# 構文チェック
msgfmt -c file.po

# 統計表示
msgfmt --statistics file.po
```

### msgmerge（更新）

```bash
# .potから.poを更新
msgmerge -U ja.po messages.pot
```

### msgunfmt（逆変換）

```bash
# .moから.poを生成
msgunfmt file.mo -o file.po
```

---

## ベストプラクティス

### 1. ヘッダーを更新する

翻訳を更新したら、`PO-Revision-Date` と `Last-Translator` を更新してください。

```po
"PO-Revision-Date: 2024-12-14 15:00+0900\n"
"Last-Translator: Your Name <your.email@example.com>\n"
```

### 2. Fuzzyを残さない

Fuzzyフラグがある場合は、必ず確認して削除してください。

### 3. コメントを活用

難しい翻訳には、コメントを残しておくと便利です。

```po
# "OpMode"は技術用語なので英語のまま残す
msgid "Create a new OpMode"
msgstr "新しい **OpMode** を作成します"
```

### 4. 一貫性を保つ

同じ用語は常に同じ翻訳を使用してください。

```bash
# 過去の翻訳を検索
grep -r "OpMode" locale/ja/LC_MESSAGES/*.po | grep msgstr
```

---

## トラブルシューティング

### 構文エラー

```bash
# エラー: unterminated string
msgid "Text without closing quote
msgstr "閉じられていない文字列"
```

**修正:**
```po
msgid "Text with closing quote"
msgstr "正しく閉じられた文字列"
```

### エンコーディングエラー

```bash
# エラー: invalid multibyte sequence
```

**修正:** ファイルをUTF-8で保存し直してください。

### フォーマット文字列のミスマッチ

```bash
# エラー: format specifications mismatch
msgid "You have %d items"
msgstr "アイテムがあります"  # %d がない
```

**修正:**
```po
msgid "You have %d items"
msgstr "アイテムが %d 個あります"
```

---

## 参考リンク

- [GNU gettext manual](https://www.gnu.org/software/gettext/manual/)
- [PO file format](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)
- [Plurals in gettext](https://www.gnu.org/software/gettext/manual/html_node/Plural-forms.html)

---

**このリファレンスを活用して、高品質な.po翻訳を作成しましょう！**
