# RST Troubleshooting Guide for FTC Japanese Documentation

このガイドは、FTC日本語ドキュメントのビルド時に発生する一般的なRST（reStructuredText）エラーと警告の解決方法をまとめたものです。

## 📋 目次

1. [よくあるエラーと解決方法](#よくあるエラーと解決方法)
2. [検証ツールの使用方法](#検証ツールの使用方法)
3. [翻訳時のベストプラクティス](#翻訳時のベストプラクティス)
4. [エラーメッセージリファレンス](#エラーメッセージリファレンス)

---

## よくあるエラーと解決方法

### 1. インラインマークアップのスペース不足

#### 問題
```
WARNING: Inline interpreted text or phrase reference start-string without end-string.
WARNING: Inline literal start-string without end-string.
```

#### 原因
インラインマークアップ（`` `` `、` **、`* *、ハイパーリンク）の直後に日本語文字がある場合、RSTパーサーがマークアップの終了を正しく認識できません。

#### 悪い例
```rst
``text``と入力します
**bold**を選択します
`link <url>`__の使用方法
:doc:`title <path>`**は重要です
```

#### 良い例
```rst
``text`` と入力します
**bold** を選択します
`link <url>`__ の使用方法
:doc:`title <path>` **は重要です
```

#### 自動修正方法
```bash
# ドライランで確認
python docs/scripts/fix_rst_inline_markup.py --dry-run

# 実際に修正
python docs/scripts/fix_rst_inline_markup.py
```

---

### 2. タイトル下線の長さ不足

#### 問題
```
WARNING: Title underline too short.
```

#### 原因
日本語文字は表示幅が2文字分ですが、下線（=、-、~、^など）の長さが不足しています。

#### 計算方法
```python
# タイトルの表示幅を計算
title = "プログラミング入門"
width = sum(2 if ord(c) > 127 else 1 for c in title)
# width = 16 (日本語8文字 × 2)
```

#### 悪い例
```rst
プログラミング入門
==============  # 14文字分（不足）
```

#### 良い例
```rst
プログラミング入門
================  # 16文字分（適切）

または

プログラミング入門
==================  # 18文字分（余裕を持たせる）
```

---

### 3. 明示的マークアップの後の空行不足

#### 問題
```
WARNING: Explicit markup ends without a blank line; unexpected unindent.
```

#### 原因
ディレクティブ（`.. note::`、`.. code::`など）のブロックの後に空行がありません。

#### 悪い例
```rst
.. note::
   これは注意事項です。
次の段落が始まります。
```

#### 良い例
```rst
.. note::
   これは注意事項です。

次の段落が始まります。
```

#### 特に注意が必要な場所
- `.. code::` ブロック
- `.. note::`、`.. warning::`、`.. tip::` などの警告ボックス
- `.. figure::`、`.. image::` 画像
- `.. only::` 条件付きブロック

---

### 4. 箇条書きリストの後の空行不足

#### 問題
```
WARNING: Bullet list ends without a blank line; unexpected unindent.
```

#### 原因
箇条書きリストの後に空行なしで通常の段落が続いています。

#### 悪い例
```rst
- 項目1
- 項目2
- 項目3
次の段落が始まります。
```

#### 良い例
```rst
- 項目1
- 項目2
- 項目3

次の段落が始まります。
```

---

### 5. 重複ラベル

#### 問題
```
WARNING: duplicate label xxx, other instance in ...
```

#### 原因
同じラベル名が複数回定義されています。

#### 悪い例
```rst
プログラミング入門
==================

プログラミング入門
~~~~~~~~~~~~~~~~~~
```

#### 良い例
```rst
プログラミング入門
==================

（サブセクションのタイトルは異なるものにする）
基本概念
~~~~~~~~
```

または、明示的にラベルを分ける：

```rst
.. _programming-intro-main:

プログラミング入門
==================

.. _programming-intro-basics:

基本概念
~~~~~~~~
```

---

### 6. コードブロックのインデント不足

#### 問題
```
WARNING: Literal block expected; none found.
```

#### 原因
`.. code::` ディレクティブの後のコード内容が正しくインデントされていません。

#### 悪い例
```rst
.. code:: java

public class MyClass {
}
```

#### 良い例
```rst
.. code:: java

   public class MyClass {
   }
```

**重要**: コード内容は3スペースまたは4スペースでインデントします。

---

## 検証ツールの使用方法

### 1. RST構文検証ツール

すべてのRSTファイルを検証：

```bash
python docs/scripts/validate_rst_syntax.py
```

特定のファイルのみ検証：

```bash
python docs/scripts/validate_rst_syntax.py docs/source/path/to/file.rst
```

### 2. インラインマークアップ自動修正

ドライラン（変更せず確認のみ）：

```bash
python docs/scripts/fix_rst_inline_markup.py --dry-run --verbose
```

実際に修正：

```bash
python docs/scripts/fix_rst_inline_markup.py
```

### 3. ビルド警告解析ツール

```bash
python docs/scripts/check_build_warnings.py --verbose
```

このツールは警告を優先度別に分類します：
- 🔴 **CRITICAL**: 必ず修正すべき問題
- 🟡 **IMPORTANT**: 修正を推奨する問題
- 🟢 **LOW PRIORITY**: オプションの問題

---

## 翻訳時のベストプラクティス

### 1. インラインマークアップの使用

```rst
✅ 良い例：
**OpMode** を使用してロボットを制御します。
``TeleOp`` **モードを選択します。
詳細は :doc:`入門ガイド <intro>` を参照してください。

❌ 悪い例：
**OpMode**を使用してロボットを制御します。
``TeleOp``**モードを選択します。
詳細は:doc:`入門ガイド <intro>`を参照してください。
```

### 2. タイトルとセクション

```rst
✅ 良い例：
プログラミング基礎
==================

基本概念
--------

変数の使用
~~~~~~~~~~

❌ 悪い例：
プログラミング基礎
==============  （短すぎる）

基本概念
------  （短すぎる）
```

### 3. リストの構造

```rst
✅ 良い例：
1. 最初のステップ
   
   詳細な説明をここに書きます。

2. 次のステップ

   別の説明。

次のセクションが始まります。

❌ 悪い例：
1. 最初のステップ
   詳細な説明をここに書きます。
2. 次のステップ
   別の説明。
次のセクションが始まります。（空行なし）
```

### 4. コードブロック

```rst
✅ 良い例：
以下のコードを参照してください：

.. code:: java

   public class Example {
       // コメントは翻訳可能
   }

次の段落が続きます。

❌ 悪い例：
以下のコードを参照してください：
.. code:: java
   public class Example {
   }
次の段落が続きます。（空行なし）
```

---

## エラーメッセージリファレンス

### 高優先度エラー

| エラーメッセージ | 重要度 | 解決方法 |
|----------------|--------|---------|
| `Inline interpreted text or phrase reference start-string without end-string` | 🔴 高 | インラインマークアップの後にスペースを追加 |
| `Title underline too short` | 🔴 高 | タイトル下線を長くする（日本語文字 × 2） |
| `Explicit markup ends without a blank line` | 🔴 高 | ディレクティブの後に空行を追加 |
| `duplicate label` | 🔴 高 | ラベル名を一意にする |
| `Malformed table` | 🔴 高 | テーブル構造を修正 |

### 中優先度警告

| 警告メッセージ | 重要度 | 解決方法 |
|--------------|--------|---------|
| `image file not readable` | 🟡 中 | 画像ファイルパスを確認・修正 |
| `Bullet list ends without a blank line` | 🟡 中 | リストの後に空行を追加 |
| `Block quote ends without a blank line` | 🟡 中 | 引用ブロックの後に空行を追加 |

### 低優先度警告

| 警告メッセージ | 重要度 | 影響 |
|--------------|--------|------|
| `undefined label` | 🟢 低 | クロスリファレンスが機能しない（表示は問題なし） |
| `document isn't included in any toctree` | 🟢 低 | ナビゲーションに表示されない（直接アクセスは可能） |
| `The parent of a 'grid-item' should be a 'grid-row'` | 🟢 低 | デザインシステムの警告（表示は問題なし） |

---

## ビルドと検証のワークフロー

### 推奨作業フロー

1. **翻訳作業**
   ```bash
   # RSTファイルを編集
   ```

2. **自動修正ツールを実行**
   ```bash
   python docs/scripts/fix_rst_inline_markup.py --dry-run
   # 問題なければ実行
   python docs/scripts/fix_rst_inline_markup.py
   ```

3. **構文検証**
   ```bash
   python docs/scripts/validate_rst_syntax.py
   ```

4. **ビルドテスト**
   ```bash
   cd docs
   make clean
   make html
   ```

5. **警告解析**
   ```bash
   python docs/scripts/check_build_warnings.py --verbose
   ```

6. **必要に応じて手動修正**

7. **再ビルド確認**

### Git Pre-commit フック（推奨）

`.git/hooks/pre-commit` ファイルを作成：

```bash
#!/bin/bash
# RST syntax validation pre-commit hook

echo "Running RST syntax validation..."
python docs/scripts/validate_rst_syntax.py $(git diff --cached --name-only --diff-filter=ACM | grep '\.rst$')

if [ $? -ne 0 ]; then
    echo "❌ RST validation failed. Please fix errors before committing."
    exit 1
fi

echo "✅ RST validation passed."
exit 0
```

実行権限を付与：

```bash
chmod +x .git/hooks/pre-commit
```

---

## トラブルシューティング FAQ

### Q1: ビルドは成功するが警告が多い場合

**A**: 警告の優先度を確認してください。`check_build_warnings.py` を使用して分類し、🔴高優先度のものから順に修正してください。

### Q2: 特定のファイルだけエラーが出る場合

**A**: そのファイルを単独で検証：
```bash
python docs/scripts/validate_rst_syntax.py docs/source/path/to/file.rst
```

### Q3: 自動修正ツールで直らないエラーがある場合

**A**: 以下の可能性があります：
- テーブル構造の問題 → 手動で修正
- ネストしたディレクティブ → 構造を見直す
- カスタムディレクティブ → ドキュメントを確認

### Q4: 日本語の表示幅計算が合わない場合

**A**: Python で確認：
```python
title = "あなたのタイトル"
width = sum(2 if ord(c) > 127 else 1 for c in title)
print(f"Required underline length: {width}")
```

---

## 参考リンク

- [reStructuredText 公式ドキュメント](https://docutils.sourceforge.io/rst.html)
- [Sphinx ドキュメント](https://www.sphinx-doc.org/)
- [TRANSLATION_INSTRUCTIONS_FOR_AI.md](./TRANSLATION_INSTRUCTIONS_FOR_AI.md) - 翻訳ガイドライン
- [RST_ERROR_FIX_SUMMARY.md](./RST_ERROR_FIX_SUMMARY.md) - 過去の修正履歴
- [RST_WARNING_FIX_SUMMARY.md](./RST_WARNING_FIX_SUMMARY.md) - 警告修正履歴

---

## 更新履歴

- 2025-12-14: 初版作成
  - 主要なRSTエラーと解決方法を文書化
  - 検証ツールの使用方法を追加
  - ベストプラクティスとワークフローを記載
