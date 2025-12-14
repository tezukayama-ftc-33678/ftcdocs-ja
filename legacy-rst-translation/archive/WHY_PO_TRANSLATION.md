# なぜ .po ベースの翻訳に移行するのか？

## 問題の背景

現在のftcdocs-jaプロジェクトは、RST ファイルを直接日本語に翻訳しています。

```
docs/source/index.rst
=====================
FIRST Tech Challenge へようこそ    ← 日本語に直接翻訳
このドキュメントは...                ← 
```

### 現在の方法の問題点

#### 1. 上流の変更への対応が困難

公式の英語リポジトリ（upstream）が更新されると：

```bash
# マージを試みると...
git merge upstream/main

# コンフリクトが大量発生！
CONFLICT (content): Merge conflict in docs/source/index.rst
CONFLICT (content): Merge conflict in docs/source/tutorial.rst
CONFLICT (content): Merge conflict in docs/source/hardware.rst
... (161 files)
```

**理由**: 英語版と日本語版で同じファイルを編集しているため

#### 2. どこが翻訳済みか不明確

```rst
# このファイルは完全に翻訳済み？一部だけ？
docs/source/tutorial.rst

*FIRST* Tech Challenge Tutorial    ← 英語？それとも固有名詞？
ここではロボットの制御方法を...      ← 日本語
Configure the Control Hub           ← 翻訳忘れ？
```

#### 3. 部分翻訳ができない

- 全ファイルを翻訳するまでビルドが中途半端
- 優先度の高いページから翻訳できない
- 段階的な公開が困難

#### 4. ツールが使えない

- Poedit、Weblate などの翻訳ツールが使えない
- 翻訳メモリ機能なし
- 進捗追跡が手動

## .po ベースの翻訳とは？

gettext という国際化（i18n）の標準的な仕組みです。

### ファイル構成

```
docs/
├── source/
│   └── index.rst              ← 英語のまま（変更不要）
│
└── locale/ja/LC_MESSAGES/
    └── index.po              ← 日本語翻訳だけ管理
```

### .po ファイルの例

```po
# docs/locale/ja/LC_MESSAGES/index.po

#: index.rst:10
msgid "Welcome to FIRST Tech Challenge"
msgstr "FIRST Tech Challenge へようこそ"

#: index.rst:15
msgid "This is the official documentation"
msgstr "これは公式ドキュメントです"
```

## 解決される問題

### ✅ 1. 上流の変更に簡単に対応

```bash
# 英語版を更新（コンフリクトなし！）
git merge upstream/main

# 翻訳を更新
make gettext && make ja-update

# 結果:
# - 新しいテキスト → msgstr が空（翻訳待ち）
# - 変更されたテキスト → "fuzzy" マーク（要確認）
# - 削除されたテキスト → コメントアウト
```

**Before**:
```
161 files changed
161 merge conflicts
手動で全て解決が必要
```

**After**:
```
0 merge conflicts
sphinx-intl が自動で差分を検出
翻訳が必要な箇所だけ作業
```

### ✅ 2. 翻訳状態が明確

```bash
# 翻訳進捗を確認
make ja-stats

# 出力例:
index.po: 45 translated, 5 fuzzy, 10 untranslated
tutorial.po: 120 translated, 0 fuzzy, 0 untranslated
hardware.po: 0 translated, 0 fuzzy, 80 untranslated
```

各ファイルの状態が一目瞭然！

### ✅ 3. 部分翻訳でもビルド可能

```po
# 翻訳されていない部分
msgid "This section is not translated yet"
msgstr ""   ← 空でもOK！自動的に英語で表示
```

**メリット**:
- 優先度の高いページから翻訳
- 段階的に公開できる
- 途中でもビルド可能

### ✅ 4. プロの翻訳ツールが使える

#### Poedit
```
無料のデスクトップアプリ
├── 翻訳メモリ機能
├── 用語集管理
├── 文法チェック
└── 自動翻訳提案
```

#### Weblate
```
オンライン翻訳プラットフォーム
├── チームで翻訳
├── Git と自動同期
├── レビュー機能
└── 翻訳メモリ共有
```

#### VS Code
```
エディタで直接翻訳
├── i18n Ally 拡張機能
├── インライン表示
└── Git と統合
```

## 具体的な改善例

### シナリオ 1: 上流がファイルを更新

**従来の方法**:
```bash
git merge upstream/main
# CONFLICT in 50 files

# 各ファイルを開いて:
<<<<<<< HEAD
**OpMode** を使用してロボットを制御します。
=======
Use OpMode to control your robot during autonomous.
>>>>>>> upstream/main

# これを50回繰り返す...
```

**.po ベースの方法**:
```bash
git merge upstream/main  # コンフリクトなし！
make gettext && make ja-update

# index.po を確認:
#, fuzzy  # ← 自動で「要確認」マーク
msgid "Use OpMode to control your robot during autonomous and tele-op"
msgstr "**OpMode** を使用してロボットを制御します。"
# → 新しい英語を確認して翻訳を更新するだけ
```

### シナリオ 2: 新しいページが追加

**従来の方法**:
```bash
# 新しい advanced_tutorial.rst が追加
git merge upstream/main

# 全て手動で翻訳
vim docs/source/advanced_tutorial.rst
# 1000行の英語を全て日本語に置き換え...
```

**.po ベースの方法**:
```bash
git merge upstream/main   # 英語版が追加される
make gettext && make ja-update

# 新しい advanced_tutorial.po が自動生成
# 空の状態でもビルド可能（英語で表示）

# 翻訳できるときに:
poedit locale/ja/LC_MESSAGES/advanced_tutorial.po
# 完成した分だけ保存 → 部分的に日本語化
```

### シナリオ 3: チームで翻訳

**従来の方法**:
```bash
# メンバーA が index.rst を翻訳中
# メンバーB が同じファイルの別の部分を翻訳
git merge   # コンフリクト！

# 誰がどこを翻訳したか不明
# 重複作業や翻訳漏れが発生
```

**.po ベースの方法**:
```bash
# Weblate を使用:
メンバーA: index.po の 1-50 行を翻訳
メンバーB: index.po の 51-100 行を翻訳

# 自動的にマージされ、進捗が可視化
# レビュー機能で品質保証
```

## 移行のコスト vs メリット

### 初期コスト（1回のみ）

| タスク | 時間 | 難易度 |
|--------|------|--------|
| sphinx-intl インストール | 5分 | ⭐ |
| .pot ファイル生成 | 10分 | ⭐ |
| .po ファイル作成 | 5分 | ⭐ |
| 既存翻訳の移行 | 数日-数週 | ⭐⭐⭐ |

**Total**: 段階的に行えば、1週間〜数週間

### 長期的なメリット

| メリット | 時間節約 | 頻度 |
|---------|---------|------|
| 上流の変更マージ | 数時間 → 数分 | 毎月 |
| 翻訳進捗の確認 | 手動確認 → 自動 | 毎日 |
| 部分翻訳・公開 | 不可能 → 可能 | 常時 |
| ツール活用 | なし → 多数 | 常時 |

**年間で数十〜数百時間の節約！**

## 実際の使用例

### Python ドキュメント
- 40+ 言語に翻訳
- .po ベースで管理
- 世界中のボランティアが貢献

### Sphinx ドキュメント
- 自身も .po ベースで多言語化
- 推奨方法として公式サポート

### Django ドキュメント
- 50+ 言語
- Transifex (Weblate類似) を使用
- 効率的なチーム翻訳

## 移行の決断

### やるべき理由

1. ✅ **上流との同期が必須**: FTC は毎年更新される
2. ✅ **長期的な維持**: 一度移行すれば、ずっと楽
3. ✅ **チーム協力**: 複数人で効率的に翻訳可能
4. ✅ **業界標準**: プロの翻訳者も使うツール
5. ✅ **将来の拡張**: 他の言語への展開も容易

### やらない理由

1. ❌ 初期の移行コスト
2. ❌ 新しいツールの学習
3. ❌ 既存ワークフローの変更

## 段階的な移行

すべてを一度に移行する必要はありません：

### フェーズ 1: テスト（1-2日）
```bash
# 1つのファイルで試す
git checkout upstream/main -- docs/source/index.rst
make gettext && make ja-update
# index.po を翻訳
make ja-build
# → 成功を確認
```

### フェーズ 2: 主要ページ（1週間）
```bash
# 重要な5-10ページを移行
# - index.rst
# - overview.rst
# - tutorial.rst
# など
```

### フェーズ 3: セクションごと（数週間）
```bash
# programming_resources/
# hardware_and_software_configuration/
# など、セクション単位で移行
```

### フェーズ 4: 完全移行
```bash
# すべてのページを .po ベースに
```

## 結論

**.po ベースの翻訳は:**

✅ 上流の変更に強い  
✅ 翻訳状態が明確  
✅ 段階的な翻訳が可能  
✅ プロのツールが使える  
✅ 業界標準の方法  
✅ 長期的に効率的  

**初期コストはかかりますが、長期的には必ず良い投資になります。**

特に、FTC のような**毎年更新されるドキュメント**では、上流との同期が最重要課題です。

---

## 次のステップ

1. **決定**: チームで移行を決定
2. **計画**: `MIGRATION_NEXT_STEPS.md` を読む
3. **実行**: 段階的に移行開始
4. **維持**: `PO_TRANSLATION_WORKFLOW.md` に従う

**質問・相談**: GitHub Issue または Discord で！
