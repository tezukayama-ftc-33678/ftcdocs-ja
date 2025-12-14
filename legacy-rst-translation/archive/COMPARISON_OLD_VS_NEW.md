# 翻訳方法の比較: 従来 vs .po ベース

## 📊 ビジュアル比較

### ファイル構成

#### 従来の方法
```
docs/source/
├── index.rst          ← 直接日本語に翻訳
├── tutorial.rst       ← 直接日本語に翻訳  
└── hardware.rst       ← 直接日本語に翻訳

問題:
❌ 英語版と同じファイルを編集
❌ 上流とマージできない
❌ 翻訳状態が不明
```

#### .po ベースの方法
```
docs/
├── source/
│   ├── index.rst           ← 英語のまま
│   ├── tutorial.rst        ← 英語のまま
│   └── hardware.rst        ← 英語のまま
│
└── locale/ja/LC_MESSAGES/
    ├── index.po            ← 日本語翻訳
    ├── tutorial.po         ← 日本語翻訳
    └── hardware.po         ← 日本語翻訳

メリット:
✅ 英語版と分離
✅ 上流と簡単にマージ
✅ 翻訳状態を追跡
```

## 🔄 ワークフロー比較

### シナリオ1: 上流の変更をマージ

#### 従来の方法
```bash
1. git merge upstream/main
   
   結果: 161個のコンフリクト！
   
   index.rst:
   <<<<<<< HEAD (日本語版)
   FIRST Tech Challenge へようこそ
   =======
   Welcome to FIRST Tech Challenge
   Additional new content added...
   >>>>>>> upstream/main (英語版)

2. 各ファイルを手動で解決
   - どこが変更されたか分からない
   - 新しいコンテンツを翻訳
   - 既存の翻訳を保持
   - 161回繰り返す...

3. 時間: 数時間〜数日
```

#### .po ベースの方法
```bash
1. git merge upstream/main
   
   結果: コンフリクトなし！
   （英語ファイルだけが更新される）

2. make gettext && make ja-update
   
   結果:
   index.po に自動マーク:
   
   #, fuzzy  ← 「要確認」マーク
   msgid "Welcome to FIRST Tech Challenge. Additional new content added..."
   msgstr "FIRST Tech Challenge へようこそ"
   
   tutorial.po:
   msgid "New section added"  ← 新規追加
   msgstr ""  ← 空（翻訳待ち）

3. 変更箇所だけ翻訳
   - 自動的に検出される
   - 効率的に作業

4. 時間: 数分〜数時間
```

### シナリオ2: 新しいページを追加

#### 従来の方法
```bash
1. 上流に新しい advanced.rst が追加

2. git merge upstream/main
   
3. advanced.rst を全て日本語に翻訳
   - 1000行の英語を手動で翻訳
   - 全て完了するまでビルド不可
   
4. 時間: 数日
```

#### .po ベースの方法
```bash
1. 上流に新しい advanced.rst が追加

2. git merge upstream/main
   （英語版が追加される）

3. make gettext && make ja-update
   （advanced.po が自動生成）

4. 今すぐビルド可能！
   - 翻訳前: 英語で表示
   - 部分翻訳: 一部日本語、一部英語
   - 完全翻訳: 全て日本語

5. 優先度に応じて段階的に翻訳
   
6. 時間: 柔軟に対応可能
```

### シナリオ3: 翻訳進捗の確認

#### 従来の方法
```bash
# 翻訳済みかどうか確認
grep -r "です\|ます" docs/source/

結果:
- 英語と日本語が混在
- どこまで完了か不明
- 手動で確認が必要

時間: 手動確認（数十分）
```

#### .po ベースの方法
```bash
# 翻訳統計を表示
make ja-stats

結果:
index.po: 100 translated, 0 fuzzy, 0 untranslated [100%]
tutorial.po: 80 translated, 5 fuzzy, 15 untranslated [80%]
hardware.po: 0 translated, 0 fuzzy, 120 untranslated [0%]

Total: 180 translated, 5 fuzzy, 135 untranslated [56%]

時間: 数秒
```

## 📝 ファイル内容の比較

### RST ファイル (従来の方法)

```rst
FIRST Tech Challenge へようこそ
=====================================

これは **FIRST** Tech Challenge の公式ドキュメントです。

**OpMode** を使用してロボットを制御します。

.. code-block:: java

   public class MyOpMode extends LinearOpMode {
       // コードは英語のまま
   }
```

**問題**:
- 日本語と英語が混在
- 上流の変更で全てコンフリクト
- コードコメントも翻訳？技術用語は？判断が難しい

### PO ファイル (.po ベースの方法)

**index.rst** (英語のまま):
```rst
Welcome to FIRST Tech Challenge
=====================================

This is the official documentation for *FIRST* Tech Challenge.

Use OpMode to control your robot.

.. code-block:: java

   public class MyOpMode extends LinearOpMode {
       // Code stays in English
   }
```

**index.po** (翻訳だけ):
```po
#: index.rst:1
msgid "Welcome to FIRST Tech Challenge"
msgstr "FIRST Tech Challenge へようこそ"

#: index.rst:4
msgid "This is the official documentation for *FIRST* Tech Challenge."
msgstr "これは **FIRST** Tech Challenge の公式ドキュメントです。"

#: index.rst:6
msgid "Use OpMode to control your robot."
msgstr "**OpMode** を使用してロボットを制御します。"

# コードブロックは自動的にスキップ（翻訳不要）
```

**利点**:
- 英語と日本語が完全に分離
- コードは自動的にスキップ
- 翻訳すべき文字列が明確

## 🛠️ ツールの比較

### 従来の方法

| タスク | ツール | 効率 |
|--------|--------|------|
| 翻訳 | テキストエディタ | ⭐⭐ |
| 進捗確認 | 手動grep | ⭐ |
| マージ | 手動解決 | ⭐ |
| 翻訳メモリ | なし | - |
| チーム協力 | Git | ⭐⭐ |

### .po ベースの方法

| タスク | ツール | 効率 |
|--------|--------|------|
| 翻訳 | Poedit, Weblate, VS Code | ⭐⭐⭐⭐⭐ |
| 進捗確認 | `make ja-stats` | ⭐⭐⭐⭐⭐ |
| マージ | 自動 | ⭐⭐⭐⭐⭐ |
| 翻訳メモリ | ビルトイン | ⭐⭐⭐⭐⭐ |
| チーム協力 | Git + Weblate | ⭐⭐⭐⭐⭐ |

## 📈 長期的なメリット

### 1年間のメンテナンス作業

#### 従来の方法
```
上流の更新: 月1回 × 12ヶ月
├── コンフリクト解決: 5時間/回
├── 翻訳漏れチェック: 2時間/回
└── 合計: 84時間/年

新機能の翻訳: 年4回
├── 全文翻訳: 8時間/回
└── 合計: 32時間/年

総計: 約116時間/年
```

#### .po ベースの方法
```
上流の更新: 月1回 × 12ヶ月
├── 自動マージ: 5分/回
├── 変更箇所の翻訳: 1時間/回
└── 合計: 13時間/年

新機能の翻訳: 年4回
├── 段階的翻訳: 2時間/回
└── 合計: 8時間/年

総計: 約21時間/年

削減: 約95時間/年 (82%削減！)
```

## 🎯 具体例: tech-tips.rst の更新

### 従来の方法

```bash
# 上流で tech-tips.rst が100行追加、50行変更

git merge upstream/main

# コンフリクト:
<<<<<<< HEAD
ロボットのトラブルシューティング
=================================

バッテリーの確認：
1. 充電レベルを確認
2. 接続を確認

モーターの問題：
=======
Robot Troubleshooting
=====================

Check Battery:
1. Verify charge level
2. Check connections
3. Test voltage

Motor Issues:
4. Check wiring
5. Verify configuration

New Section: Advanced Diagnostics
==================================
[100 lines of new English content]
>>>>>>> upstream/main

手動作業:
1. 新旧のコンテンツを比較
2. 新しい100行を翻訳
3. 変更された50行を更新
4. 元の翻訳を保持
5. テストとレビュー

時間: 4-6時間
```

### .po ベースの方法

```bash
# 上流で tech-tips.rst が100行追加、50行変更

git merge upstream/main   # コンフリクトなし！
make gettext && make ja-update

# tech-tips.po の変更:
# 1. 新しい100行 → msgstr ""（空）
msgid "New Section: Advanced Diagnostics"
msgstr ""  # ← 翻訳待ち

# 2. 変更された50行 → fuzzy マーク
#, fuzzy
msgid "Motor Issues: Check wiring, verify configuration"
msgstr "モーターの問題：配線を確認"  # ← 要更新

# 3. 変更なし → そのまま
msgid "Check Battery: Verify charge level"
msgstr "バッテリーの確認：充電レベルを確認"  # ← OK

自動作業:
- 新規・変更・不変を自動識別
- 翻訳が必要な箇所だけマーク

手動作業:
1. fuzzy 箇所を確認・更新
2. 新規箇所を翻訳（優先度に応じて）

時間: 1-2時間
```

## 💰 コスト比較

### 初期コスト

| 従来の方法 | .po ベースの方法 |
|-----------|-----------------|
| 学習時間: 数時間 | 学習時間: 1-2日 |
| セットアップ: なし | セットアップ: 1日 |
| 移行作業: なし | 移行作業: 1-4週間 |
| **合計: 数時間** | **合計: 2-5週間** |

### 運用コスト（年間）

| 従来の方法 | .po ベースの方法 |
|-----------|-----------------|
| マージ作業: 60時間 | マージ作業: 1時間 |
| 翻訳作業: 40時間 | 翻訳作業: 15時間 |
| 進捗管理: 10時間 | 進捗管理: 1時間 |
| トラブル対応: 6時間 | トラブル対応: 4時間 |
| **合計: 116時間/年** | **合計: 21時間/年** |

### ROI (投資対効果)

```
初期投資: 2-5週間
年間削減: 95時間

回収期間: 約2-3ヶ月
2年目以降: 毎年95時間の削減！
```

## 🎓 学習曲線

### 従来の方法
```
難易度: ⭐⭐⭐
- RST構文
- Git コンフリクト解決
- 手動での翻訳管理
- 進捗追跡の方法

習得時間: 数時間
マスター時間: 数週間
```

### .po ベースの方法
```
難易度: ⭐⭐
- .po ファイルの基本（msgid/msgstr）
- Make コマンド（3つだけ）
- sphinx-intl の使い方

習得時間: 1-2日
マスター時間: 1週間
```

**実際には .po の方が簡単！**

## 結論

| 観点 | 従来の方法 | .po ベース | 勝者 |
|------|-----------|-----------|-----|
| 初期コスト | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 従来 |
| 運用コスト | ⭐ | ⭐⭐⭐⭐⭐ | .po |
| 上流との同期 | ⭐ | ⭐⭐⭐⭐⭐ | .po |
| ツール対応 | ⭐ | ⭐⭐⭐⭐⭐ | .po |
| チーム協力 | ⭐⭐ | ⭐⭐⭐⭐⭐ | .po |
| 進捗追跡 | ⭐ | ⭐⭐⭐⭐⭐ | .po |
| 学習曲線 | ⭐⭐⭐ | ⭐⭐⭐⭐ | .po |
| 長期的効率 | ⭐ | ⭐⭐⭐⭐⭐ | .po |

**総合評価**: .po ベースの圧勝（初期コスト以外）

---

## 次のアクション

1. **理解**: この比較を読む ✓
2. **学習**: WHY_PO_TRANSLATION.md で詳細を確認
3. **決定**: チームで移行を検討
4. **実行**: MIGRATION_NEXT_STEPS.md に従う
5. **運用**: PO_TRANSLATION_WORKFLOW.md を使用

**質問がありますか？** GitHub Issue で気軽に聞いてください！
