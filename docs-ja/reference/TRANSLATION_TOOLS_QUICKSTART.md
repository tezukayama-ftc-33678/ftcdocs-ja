# 翻訳ツール クイックスタートガイド

このガイドでは、翻訳作業支援ツールの基本的な使い方を5分で理解できます。

## 🚀 基本的な使い方

### 1. 翻訳進捗の確認

全ての翻訳状況を確認したい場合：

```bash
# リポジトリのルートディレクトリで実行
python docs/scripts/check_translation_progress.py

# 生成されたレポートを確認
cat TRANSLATION_PROGRESS.md
```

**出力例:**
```
============================================================
FTC Documentation Translation Progress Checker
============================================================

Scanning 255 RST files...

============================================================
Summary:
  Total files: 255
  Completed: 29 (11.4%)
  Partial: 54 (21.2%)
  Untranslated: 172 (67.5%)
============================================================

✓ Report saved to: TRANSLATION_PROGRESS.md
```

生成された `TRANSLATION_PROGRESS.md` には以下の情報が含まれます：
- 翻訳完了ファイルのリスト
- 部分的に翻訳されたファイルと問題箇所
- 未翻訳ファイルのリスト
- 統計情報と進捗バー

### 2. 特定ステータスのファイルを探す

#### 翻訳が必要なファイルを見つける

```bash
# 未翻訳ファイルの一覧を表示
python docs/scripts/find_files_by_status.py --status untranslated

# 未翻訳ファイルの数だけ表示
python docs/scripts/find_files_by_status.py --status untranslated --count
```

#### 修正が必要なファイルを見つける

```bash
# 部分的に翻訳されたファイルを問題数とともに表示
python docs/scripts/find_files_by_status.py --status partial --show-issues

# 特定ディレクトリ内の部分翻訳ファイルを表示
python docs/scripts/find_files_by_status.py --status partial --directory programming_resources
```

#### 完了したファイルを確認

```bash
# 翻訳完了ファイルの一覧を表示
python docs/scripts/find_files_by_status.py --status completed

# 翻訳完了ファイルの数を表示
python docs/scripts/find_files_by_status.py --status completed --count
```

## 📋 典型的なワークフロー

### 翻訳作業開始時

1. **現在の進捗を確認**
   ```bash
   python docs/scripts/check_translation_progress.py
   cat TRANSLATION_PROGRESS.md
   ```

2. **作業対象ファイルを選択**
   ```bash
   # 未翻訳ファイルから選ぶ
   python docs/scripts/find_files_by_status.py --status untranslated --directory programming_resources
   
   # または部分翻訳ファイルから修正が必要なものを選ぶ
   python docs/scripts/find_files_by_status.py --status partial --show-issues | head -10
   ```

3. **作業ブランチを作成**
   ```bash
   git checkout -b translate-imu-documentation
   ```

### 翻訳作業中

1. **ファイルを翻訳**
   - VSCode などのエディタでRSTファイルを開く
   - `TRANSLATION_GUIDE.md` に従って翻訳
   - `GLOSSARY.md` で用語統一を確認

2. **こまめにコミット**
   ```bash
   git add docs/source/programming_resources/imu/imu.rst
   git commit -m "Translate IMU documentation"
   ```

### 翻訳作業完了後

1. **進捗を再確認**
   ```bash
   python docs/scripts/check_translation_progress.py
   ```

2. **作業したファイルのステータス確認**
   - `TRANSLATION_PROGRESS.md` を開いて、完了ファイルに追加されているか確認
   - または特定ファイルの問題がなくなっているか確認

3. **プルリクエストを作成**
   ```bash
   git push origin translate-imu-documentation
   # GitHubでPRを作成
   ```

## 🔍 検出される問題の種類

翻訳チェッカーは以下のような問題を検出します：

### 1. 文末に英語が残っている
```
問題例：IMUは以下の機能を提供します: rotation measurement and heading control.
修正後：IMUは以下の機能を提供します：回転測定とヘディング制御。
```

### 2. 文中に英語が混在している
```
問題例：このセクションでは how to configure the IMU を説明します。
修正後：このセクションではIMUの設定方法を説明します。
```

### 3. 段落全体が未翻訳
```
問題例：
The Control Hub contains an internal IMU that can measure...
（段落全体が英語のまま）

修正後：
Control Hubには、測定可能な内部IMUが含まれています...
（完全に日本語化）
```

## ⚙️ 除外される項目

以下の項目は英語のままでも問題として検出されません：

- **コードブロック内の英語**
- **RSTディレクティブ** (`:doc:`, `:ref:` など)
- **URL**
- **技術用語** (`OpMode`, `Control Hub`, `IMU` など) - **GLOSSARY.mdから自動読み込み**

スクリプトは `GLOSSARY.md` を自動的に読み込み、「和訳しない用語」セクションに定義された技術用語を検出から除外します。これにより、翻訳ガイドラインに従った正しい翻訳が適切に認識されます。

## 💡 ヒント

### タスクを小分けにする
一度に大量のファイルを翻訳しようとせず、1〜3ファイルずつ翻訳してPRを作成するのがおすすめです。

### 進捗を可視化する
定期的に `check_translation_progress.py` を実行して、進捗バーが伸びていくのを確認するとモチベーションが上がります！

### チームで協力する
`find_files_by_status.py` で特定ディレクトリのファイルを分担して、効率的に作業を進めましょう。

## 📖 詳細情報

さらに詳しい情報は以下のドキュメントを参照してください：

- **[TRANSLATION_WORKFLOW_TOOLS.md](TRANSLATION_WORKFLOW_TOOLS.md)** - 詳細なツールガイド
- **[TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md)** - 翻訳ガイドライン
- **[TRANSLATION_ROADMAP.md](TRANSLATION_ROADMAP.md)** - 翻訳計画
- **[GLOSSARY.md](GLOSSARY.md)** - 用語統一リスト

## ❓ トラブルシューティング

### スクリプトが動かない
```bash
# Pythonのバージョンを確認（3.6以上が必要）
python --version

# リポジトリのルートディレクトリにいることを確認
pwd
# 出力: /path/to/ftcdocs-ja
```

### ファイルが誤検出される
技術用語として英語を残すべき箇所が問題として検出される場合があります。
これは意図的な場合は無視して構いません。`TRANSLATION_GUIDE.md` に従って判断してください。

---

**Happy Translating! 🎉**
