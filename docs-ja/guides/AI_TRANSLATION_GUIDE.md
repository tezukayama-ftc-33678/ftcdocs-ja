# AI翻訳総合ガイド

このドキュメントは、AI翻訳ツール（DeepL、ChatGPT、Claude等）を使用してFTC日本語ドキュメントを翻訳する際の**統合ガイド**です。

---

## 📋 目次

1. [翻訳の基本方針](#翻訳の基本方針)
2. [用語の取り扱い](#用語の取り扱い)
3. [RST構文ルール](#rst構文ルール)
4. [翻訳ワークフロー](#翻訳ワークフロー)
5. [エラー対策](#エラー対策)
6. [品質チェック](#品質チェック)
7. [リファレンス](#リファレンス)

---

## 翻訳の基本方針

### 文体と表記

**必須ルール:**
- **文体**: 「です・ます」調で統一
- **読点**: 「、」（全角）
- **句点**: 「。」（全角）
- **コロン**: 「：」（全角）
- **長音符号**: カタカナ語の長音（ー）は省略しない
  - ✅ 正: コンピューター、パラメーター、ユーザー
  - ❌ 誤: コンピュータ、パラメータ、ユーザ

### 翻訳してはいけないもの

1. **コードブロック内のコード**
   ```java
   // コメントのみ翻訳可能
   public class MyOpMode extends LinearOpMode {
   }
   ```

2. **RSTディレクティブ**
   ```rst
   .. note::  ← これは翻訳しない
   :doc:`リンクテキストのみ翻訳 </path/to/file>`
   :ref:`参照テキストのみ翻訳 <label>`
   ```

3. **URL とファイルパス**
   ```
   https://www.firstinspires.org/
   /docs/source/programming_resources/index.rst
   ```

4. **ファイル名と拡張子**
   ```
   config.xml
   MyOpMode.java
   README.md
   ```

---

## 用語の取り扱い

### 【重要】英語を残す用語は必ず太字（**用語**）で表記

技術用語、製品名、API名は**翻訳せず、英語のまま太字**で残してください。

**書式例:**
```markdown
**OpMode** を使用してロボットを制御します。
**Control Hub** に接続してください。
**AprilTag** による位置認識を実装します。
```

### 和訳しない用語リスト

#### API/クラス名
- **OpMode**, **LinearOpMode**, **Telemetry**, **HardwareMap**, **VisionPortal**

#### 制御モード
- **Autonomous**, **TeleOp**

#### ハードウェア製品名
- **Control Hub**, **Expansion Hub**, **Driver Hub**, **Driver Station**, **Robot Controller**, **IMU**, **HuskyLens**

#### アプリ/ソフトウェア名
- **Blocks**, **OnBot Java**, **Android Studio**, **Robot Controller App**, **Driver Station App**

#### ビジョン/画像処理
- **AprilTag**, **OpenCV**, **EasyOpenCV**, **VisionPortal**, **Camera Stream**, **Color Locator**

#### 組織名/プログラム名
- **FIRST**, **FIRST Tech Challenge (FTC)**, **Gracious Professionalism**

#### UI/機能名
- **Settings**, **Team Prop**, **Access Codes**, **Self Inspect**, **Inspection Reports**

**詳細は:** [GLOSSARY.md](../../GLOSSARY.md) を参照

### 和訳またはカタカナ表記する用語

#### プログラミング関連
- Debugging → デバッグ
- Feature → 機能
- Variable → 変数
- Parameter → パラメーター
- Configuration → 構成

#### FTC競技関連
- Team → チーム
- Coach → コーチ
- Competition → 競技
- Field → フィールド
- Robot → ロボット

---

## RST構文ルール

### 【最重要】インラインマークアップと日本語の間に必ずスペース

RSTパーサーの制限により、インラインマークアップ（太字、リテラル、ハイパーリンク、ディレクティブ）の直後に日本語が来る場合、**必ずスペース**を入れてください。

#### 必須パターン

```rst
✅ 正しい：
**OpMode** を使用します
``TeleOp`` モードで実行します
:doc:`入門 <intro>` を参照してください
`リンク <url>`__ の使用方法

❌ 間違い：
**OpMode**を使用します
``TeleOp``モードで実行します
:doc:`入門 <intro>`を参照してください
`リンク <url>`__の使用方法
```

**理由:** スペースがないとRSTパーサーがマークアップの終了を認識できず、ビルドエラーになります。

### タイトル下線の長さ

日本語文字は表示幅が2文字分です。タイトルの下線は以下のように計算してください：

```python
# 計算方法
タイトル = "プログラミング入門"
幅 = 日本語文字数 × 2 + ASCII文字数
必要な下線の長さ = 幅以上
```

```rst
✅ 正しい：
プログラミング入門
==================  # 18文字（余裕を持たせる）

❌ 間違い：
プログラミング入門
==============  # 14文字（短すぎる）
```

### ディレクティブの後に空行

```rst
✅ 正しい：
.. note::
   これは注意事項です。

次の段落が始まります。

❌ 間違い：
.. note::
   これは注意事項です。
次の段落が始まります。  # 空行なし
```

### リストの後も空行

```rst
✅ 正しい：
- 項目1
- 項目2
- 項目3

次の段落が始まります。

❌ 間違い：
- 項目1
- 項目2
- 項目3
次の段落が始まります。  # 空行なし
```

---

## 翻訳ワークフロー

### 推奨手順

```bash
# 1. 翻訳作業
# RSTファイルを編集

# 2. 自動修正を実行
python docs/scripts/fix_rst_inline_markup.py --dry-run  # 確認
python docs/scripts/fix_rst_inline_markup.py             # 実行

# 3. 構文検証
python docs/scripts/validate_rst_syntax.py

# 4. ビルドテスト
cd docs && make clean && make html

# 5. 警告確認
python docs/scripts/check_build_warnings.py --verbose

# 6. コミット
git add .
git commit -m "翻訳: [ファイル名] を追加"
```

### 翻訳時のチェックリスト

#### 用語の扱い
- [ ] API名やクラス名を**太字の英語**で残しているか
- [ ] 製品名を**太字の英語**で残しているか
- [ ] アプリ名を**太字の英語**で残しているか
- [ ] **FIRST** および **Gracious Professionalism** を**太字の英語**で残しているか

#### 文体と表記
- [ ] 文体が「です・ます」調で統一されているか
- [ ] カタカナ語の長音符号（ー）を省略していないか

#### RST構文
- [ ] インラインマークアップの後に日本語が続く場合、スペースを入れているか
- [ ] タイトルの下線が十分な長さか
- [ ] ディレクティブの後に空行があるか
- [ ] 箇条書きリストの後に空行があるか
- [ ] コードブロックが適切にインデントされているか

#### 翻訳対象外の確認
- [ ] コードブロック内のコードを翻訳していないか
- [ ] RSTディレクティブを翻訳していないか
- [ ] URL やファイルパスを翻訳していないか

---

## エラー対策

### よくあるエラーと解決方法

#### 1. インラインマークアップのスペース不足

**問題:**
```
WARNING: Inline interpreted text or phrase reference start-string without end-string.
```

**原因:** インラインマークアップの直後に日本語がある

**解決方法:**
```rst
# 修正前
``text``と入力します

# 修正後
``text`` と入力します
```

**自動修正:**
```bash
python docs/scripts/fix_rst_inline_markup.py
```

#### 2. タイトル下線の長さ不足

**問題:**
```
WARNING: Title underline too short.
```

**解決方法:**
```python
# Pythonで幅を計算
title = "プログラミング入門"
width = sum(2 if ord(c) > 127 else 1 for c in title)
print(f"必要な下線の長さ: {width}")  # 16
```

```rst
# 修正前
プログラミング入門
==============  # 14文字（不足）

# 修正後
プログラミング入門
==================  # 18文字（適切）
```

#### 3. ディレクティブ後の空行不足

**問題:**
```
WARNING: Explicit markup ends without a blank line; unexpected unindent.
```

**解決方法:**
```rst
# 修正前
.. note::
   内容
次の段落

# 修正後
.. note::
   内容

次の段落
```

#### 4. リスト後の空行不足

**問題:**
```
WARNING: Bullet list ends without a blank line; unexpected unindent.
```

**解決方法:**
```rst
# 修正前
- 項目1
- 項目2
次の段落

# 修正後
- 項目1
- 項目2

次の段落
```

### エラー優先度

#### 🔴 CRITICAL（必ず修正）
- インラインマークアップのスペース不足
- タイトル下線の長さ不足
- ディレクティブ後の空行不足
- 重複ラベル
- テーブル構造エラー

#### 🟡 IMPORTANT（修正推奨）
- 画像ファイルが見つからない
- リスト後の空行不足
- 引用ブロック後の空行不足

#### 🟢 LOW PRIORITY（オプション）
- 未定義ラベル（クロスリファレンスが機能しないが表示は問題なし）
- toctree未登録（ナビゲーションに表示されないが直接アクセス可能）
- Gridデザイン警告（表示は問題なし）

---

## 品質チェック

### 自動検証ツール

#### 1. RST構文検証
```bash
# すべてのRSTファイルを検証
python docs/scripts/validate_rst_syntax.py

# 特定ファイルのみ検証
python docs/scripts/validate_rst_syntax.py path/to/file.rst
```

**検出内容:**
- インラインマークアップのスペース不足
- タイトル下線の長さ不足
- ディレクティブ後の空行不足
- 重複ラベル

#### 2. インラインマークアップ自動修正
```bash
# ドライラン（変更なし確認）
python docs/scripts/fix_rst_inline_markup.py --dry-run --verbose

# 実際に修正
python docs/scripts/fix_rst_inline_markup.py
```

**修正内容:**
- `` `text`と`` → `` `text` と``
- `**text**と` → `**text** と`
- `` >`__の`` → `` >`__ の``

#### 3. ビルド警告解析
```bash
python docs/scripts/check_build_warnings.py --verbose
```

**出力:** 警告を優先度別に分類
- 🔴 CRITICAL: 必ず修正すべき問題
- 🟡 IMPORTANT: 修正を推奨する問題
- 🟢 LOW PRIORITY: オプションの問題

### 翻訳進捗チェック

```bash
python docs/scripts/check_translation_progress.py
```

**検出内容:**
- 文末に英語が残っている箇所
- 太字なしで3語以上の英単語が連続している箇所
- 完全に英語のままの段落

**重要:** 太字（`**用語**`）で英語の技術用語を囲むことで、これらが意図的に残された用語であることを明示し、誤検出を防ぎます。

---

## リファレンス

### 関連ドキュメント

#### 必読ドキュメント
- [GLOSSARY.md](../../GLOSSARY.md) - 用語集（和訳しない用語の完全リスト）
- [RST_TROUBLESHOOTING_GUIDE.md](../reference/RST_TROUBLESHOOTING_GUIDE.md) - エラー解決の詳細ガイド

#### 参考ドキュメント
- [TRANSLATION_ROADMAP.md](../reference/TRANSLATION_ROADMAP.md) - 翻訳ロードマップ
- [TRANSLATION_PROGRESS.md](../reference/TRANSLATION_PROGRESS.md) - 翻訳進捗状況

#### ツールドキュメント
- [TRANSLATION_TOOLS_QUICKSTART.md](../reference/TRANSLATION_TOOLS_QUICKSTART.md) - ツールクイックスタート
- [TRANSLATION_WORKFLOW_TOOLS.md](../reference/TRANSLATION_WORKFLOW_TOOLS.md) - ワークフローとツール詳細

### 検証スクリプト

すべてのスクリプトは `docs/scripts/` にあります：

- `validate_rst_syntax.py` - RST構文検証
- `fix_rst_inline_markup.py` - インラインマークアップ自動修正
- `check_build_warnings.py` - ビルド警告解析
- `check_translation_progress.py` - 翻訳進捗チェック

### 外部リンク

- [reStructuredText 公式ドキュメント](https://docutils.sourceforge.io/rst.html)
- [Sphinx ドキュメント](https://www.sphinx-doc.org/)
- [FIRST Tech Challenge 公式サイト](https://www.firstinspires.org/robotics/ftc)

---

## 翻訳例

### 良い例 ✓

**原文:**
```
Create a new OpMode using the Blocks programming environment. 
The OpMode will control the robot during the Autonomous period.
Connect your Control Hub to the Driver Station app.
```

**正しい翻訳:**
```
**Blocks** プログラミング環境を使用して新しい **OpMode** を作成します。
この **OpMode** は **Autonomous** 期間中にロボットを制御します。
**Control Hub** を **Driver Station** アプリに接続してください。
```

### 悪い例 ✗

**誤った翻訳1（太字なし）:**
```
Blocks プログラミング環境を使用して新しい OpMode を作成します。
```
→ **問題:** 技術用語が太字になっていないため、品質チェックで誤検出されます

**誤った翻訳2（用語を和訳）:**
```
**ブロックス** プログラミング環境を使用して新しい**操作モード**を作成します。
```
→ **問題:** 固有名詞を翻訳してしまっています

**誤った翻訳3（スペース不足）:**
```
**OpMode**を使用してロボットを制御します。
```
→ **問題:** インラインマークアップと日本語の間にスペースがありません

**誤った翻訳4（コードを翻訳）:**
```java
public class 私のオプモード extends リニアオプモード {
```
→ **問題:** コードを翻訳してはいけません

---

## トラブルシューティング FAQ

### Q1: ビルドは成功するが警告が多い場合

**A:** 警告の優先度を確認してください。`check_build_warnings.py` を使用して分類し、🔴高優先度のものから順に修正してください。

### Q2: 特定のファイルだけエラーが出る場合

**A:** そのファイルを単独で検証：
```bash
python docs/scripts/validate_rst_syntax.py docs/source/path/to/file.rst
```

### Q3: 自動修正ツールで直らないエラーがある場合

**A:** 以下の可能性があります：
- テーブル構造の問題 → 手動で修正
- ネストしたディレクティブ → 構造を見直す
- カスタムディレクティブ → ドキュメントを確認

### Q4: 日本語の表示幅計算が合わない場合

**A:** Python で確認：
```python
title = "あなたのタイトル"
width = sum(2 if ord(c) > 127 else 1 for c in title)
print(f"必要な下線の長さ: {width}")
```

---

## 更新履歴

- **2025-12-14**: 初版作成
  - 複数の翻訳ドキュメントを統合
  - RST構文ルールとエラー対策を追加
  - 検証ツールの使用方法を統合
  - ワークフローとチェックリストを整理

---

**このガイドを翻訳AIへのプロンプトと共に提示することで、一貫性のある高品質な翻訳を実現できます。**
