# AI翻訳ガイド (.po形式)

このガイドは、AI翻訳ツール（DeepL、ChatGPT、Claude等）を使用して **.poファイル** を翻訳するための完全なガイドです。

---

## 📋 目次

1. [AI翻訳の概要](#ai翻訳の概要)
2. [AI向け指示プロンプト](#ai向け指示プロンプト)
3. [翻訳ルール](#翻訳ルール)
4. [.poファイルの扱い方](#poファイルの扱い方)
5. [自動化スクリプト](#自動化スクリプト)
6. [品質チェック](#品質チェック)

---

## AI翻訳の概要

### なぜ.po形式はAI翻訳に最適か

1. **翻訳単位が明確** - 各 `msgid`/`msgstr` ペアが独立している
2. **構造が単純** - RSTの複雑な構文を気にする必要がない
3. **文脈が保持** - コメントにファイルと行番号が記載されている
4. **バッチ処理可能** - スクリプトで複数ファイルを処理できる

### 対応AI翻訳ツール

| ツール | API | 推奨度 | 備考 |
|-------|-----|--------|------|
| DeepL | ✅ | ⭐⭐⭐⭐⭐ | 最高品質の機械翻訳 |
| OpenAI (GPT-4) | ✅ | ⭐⭐⭐⭐⭐ | 文脈理解が優秀 |
| Claude | ✅ | ⭐⭐⭐⭐ | 長文処理に強い |
| Gemini | ✅ | ⭐⭐⭐ | 無料プランあり |
| Ollama | ローカル | ⭐⭐⭐ | プライバシー重視 |

---

## AI向け指示プロンプト

### 基本プロンプト（コピー&ペースト可）

AIツールに以下のプロンプトを与えてください：

```
あなたはFIRST Tech Challenge（FTC）ドキュメントの日本語翻訳者です。
以下の.poファイルのmsgstrフィールドを翻訳してください。

【翻訳ルール】
1. 文体: 「です・ます」調で統一
2. 句読点: 全角の「、」と「。」を使用
3. 長音: カタカナ語の長音（ー）は省略しない（例: コンピューター、パラメーター）
4. 技術用語: 以下の用語は**太字の英語**で残す
   - OpMode, LinearOpMode, TeleOp, Autonomous
   - Control Hub, Driver Station, Robot Controller
   - HuskyLens, AprilTag, VisionPortal
   - その他のAPI名、クラス名、製品名
5. コード: バッククォート内の``コード``は翻訳しない
6. RSTマークアップ: :doc:、:ref:などのディレクティブは保持
7. 固有名詞: FIRST、Gracious Professionalismは翻訳しない

【出力形式】
- msgidは変更しない
- msgstrのみを日本語で埋める
- .poファイルの構造を保持

【例】
入力:
msgid "Create a new OpMode"
msgstr ""

出力:
msgid "Create a new OpMode"
msgstr "新しい **OpMode** を作成します"
```

### 詳細プロンプト（高品質が必要な場合）

```
あなたはFIRST Tech Challenge（FTC）の公式ドキュメントを日本語に翻訳する専門家です。
技術的な正確性と読みやすさのバランスを重視してください。

【対象読者】
- 中高生のロボットチーム
- 初心者から中級者のプログラマー
- 教師やメンター

【翻訳の基本方針】
1. 文体
   - 「です・ます」調で統一
   - 親しみやすく、わかりやすい表現
   - 専門用語は適切に使用
   
2. 表記規則
   - 句読点: 「、」（読点）と「。」（句点）
   - カタカナ長音: 省略しない（コンピューター、ユーザー）
   - 英数字の前後: 必要に応じて半角スペースを入れる
   
3. 技術用語の扱い
   以下は**太字の英語**で残してください:
   
   【API/クラス名】
   - OpMode, LinearOpMode, Telemetry, HardwareMap
   - VisionPortal, AprilTagProcessor
   
   【制御モード】
   - Autonomous, TeleOp
   
   【ハードウェア】
   - Control Hub, Expansion Hub, Driver Station
   - Robot Controller, Driver Hub
   
   【ビジョン】
   - AprilTag, HuskyLens, OpenCV
   
   【プログラミング環境】
   - Blocks, OnBot Java, Android Studio
   
   【その他の固有名詞】
   - FIRST, Gracious Professionalism
   - Game Manual, SDK
   
4. 翻訳しないもの
   - コードブロック内のコード（コメントは翻訳可）
   - バッククォート内のコード: ``init()``
   - ファイルパスやURL
   - RSTディレクティブ: `.. note::`, `:doc:`, `:ref:`
   
5. RSTマークアップの保持
   - リンク: :doc:`テキストは翻訳 <path>`
   - 参照: :ref:`テキストは翻訳 <label>`
   - 強調: **太字**, *斜体*, ``コード``
   
【.poファイルの処理方法】
- msgid（英語）: そのまま保持
- msgstr: 日本語翻訳を記入
- コメント行（#で始まる）: そのまま保持
- 空のmsgstr（未翻訳）: 翻訳を追加
- fuzzyフラグ（#, fuzzy）: 確認後フラグを削除

【出力例】
入力:
#: ../../source/programming_resources/tutorial_specific/blocks/writing-an-op-mode/Writing-an-Op-Mode-with-FTC-Blocks.rst:10
msgid "This tutorial will guide you through creating your first OpMode using Blocks."
msgstr ""

出力:
#: ../../source/programming_resources/tutorial_specific/blocks/writing-an-op-mode/Writing-an-Op-Mode-with-FTC-Blocks.rst:10
msgid "This tutorial will guide you through creating your first OpMode using Blocks."
msgstr "このチュートリアルでは、**Blocks** を使用して最初の **OpMode** を作成する方法を説明します。"

【注意事項】
- 文脈に応じて自然な日本語に
- 直訳ではなく、読みやすさを優先
- 技術的な正確性は維持
```

---

## 翻訳ルール

### 1. 文体と表記

```po
# ✅ 正しい例
msgid "Initialize the robot hardware"
msgstr "ロボットのハードウェアを初期化します。"

# ❌ 間違った例（である調）
msgstr "ロボットのハードウェアを初期化する。"

# ❌ 間違った例（短音）
msgstr "ロボットのハードウエアを初期化します。"
```

### 2. 技術用語の処理

```po
# ✅ 太字で英語を残す
msgid "Create a new OpMode class"
msgstr "新しい **OpMode** クラスを作成します"

# ❌ 日本語に訳さない
msgstr "新しいオペレーションモードクラスを作成します"

# ❌ 太字を忘れない
msgstr "新しい OpMode クラスを作成します"
```

### 3. コードとリテラル

```po
# ✅ コードは翻訳しない
msgid "Call the ``init()`` method"
msgstr "``init()`` メソッドを呼び出します"

# ❌ コードを翻訳しない
msgstr "``初期化()`` メソッドを呼び出します"
```

### 4. RSTマークアップ

```po
# ✅ マークアップを保持
msgid "See :doc:`Introduction <intro>` for more information"
msgstr "詳細は :doc:`入門 <intro>` を参照してください"

# ✅ リンクテキストのみ翻訳
msgid "Visit the :ref:`configuration page <config>`"
msgstr ":ref:`設定ページ <config>` にアクセスしてください"
```

### 5. 複数行の翻訳

```po
# ✅ 複数行を適切に処理
msgid ""
"This is a long paragraph that explains "
"multiple concepts in detail."
msgstr ""
"これは複数の概念を詳しく説明する "
"長い段落です。"
```

---

## .poファイルの扱い方

### ファイル構造

```po
# ファイルヘッダー（変更不要）
msgid ""
msgstr ""
"Language: ja\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"

# 翻訳エントリ
#: ../../source/index.rst:5
msgid "Welcome"
msgstr "ようこそ"
```

### 翻訳の優先順位

1. **空のmsgstr** - 最優先で翻訳
   ```po
   msgid "New content"
   msgstr ""  ← これを翻訳
   ```

2. **Fuzzyフラグ** - 確認が必要
   ```po
   #, fuzzy  ← 変更を確認
   msgid "Updated text"
   msgstr "古い翻訳"
   ```

3. **既存の翻訳** - レビューのみ
   ```po
   msgid "Existing content"
   msgstr "既存の翻訳"  ← 必要に応じて改善
   ```

### バッチ処理のヒント

```bash
# 未翻訳エントリのみ抽出
grep -B2 'msgstr ""' locale/ja/LC_MESSAGES/index.po > untranslated.txt

# AIで翻訳

# 結果をマージ
```

---

## 自動化スクリプト

### AI翻訳支援スクリプト

プロジェクトには、AI翻訳を支援するスクリプトが含まれています：

```bash
# 未翻訳エントリを確認（ドライラン）
python po-translation/scripts/ai_translate_po.py \
  docs/locale/ja/LC_MESSAGES/index.po \
  --dry-run
```

**⚠️ 重要な注意事項:**

このスクリプトは **フレームワーク** です。実際のAPI呼び出しを実装する必要があります。

**現在の機能:**
- ✅ 未翻訳エントリの自動検出
- ✅ Fuzzyエントリの検出
- ✅ ドライランモード
- ⚠️ API呼び出しは **スタブ実装**（実装が必要）

**使用方法:**

1. **ドライランで未翻訳を確認:**
   ```bash
   python po-translation/scripts/ai_translate_po.py FILE.po --dry-run
   ```

2. **API実装後に使用:**
   ```bash
   # translate_with_api()関数を実装してから:
   python po-translation/scripts/ai_translate_po.py FILE.po \
     --api deepl --api-key YOUR_KEY
   ```

3. **または、手動/外部ツールで翻訳:**
   - ドライランで未翻訳エントリを確認
   - AIツール（ChatGPT等）に直接コピー&ペースト
   - 翻訳結果を.poファイルに貼り付け

**API実装が必要な理由:**

各APIは認証方法やエンドポイントが異なるため、ユーザーの環境に合わせた実装が必要です。
スクリプトは構造を提供し、実装箇所を明示しています。

詳細は `po-translation/scripts/ai_translate_po.py` のコメントを参照。

---

## 品質チェック

### 翻訳品質チェックスクリプト

```bash
# 全ファイルをチェック
python po-translation/scripts/check_po_quality.py \
  docs/locale/ja/LC_MESSAGES/

# レポート出力
python po-translation/scripts/check_po_quality.py \
  docs/locale/ja/LC_MESSAGES/ \
  --report quality_report.md
```

**チェック項目:**
- [ ] 空のmsgstrがないか
- [ ] Fuzzyフラグが残っていないか
- [ ] 技術用語が太字になっているか
- [ ] RSTマークアップが保持されているか
- [ ] 文体が統一されているか

### 手動チェック

```bash
# 1. .poファイルの構文チェック
msgfmt -c locale/ja/LC_MESSAGES/index.po

# 2. ビルドしてエラー確認
make ja-build

# 3. プレビューで見た目確認
python -m http.server 8000 --directory build/html/ja
```

### チェックリスト

翻訳後、以下を確認してください：

- [ ] すべてのmsgstrが埋まっている
- [ ] Fuzzyフラグを削除した
- [ ] 技術用語を **太字** で残した
- [ ] コードを翻訳していない
- [ ] RSTマークアップを保持した
- [ ] 文体が「です・ます」調
- [ ] ビルドエラーがない
- [ ] プレビューで表示を確認した

---

## 実践例

### Example 1: 簡単な文章

```po
#: tutorial.rst:10
msgid "This is a tutorial for beginners."
msgstr "これは初心者向けのチュートリアルです。"
```

### Example 2: 技術用語を含む

```po
#: opmode.rst:15
msgid "Create a new OpMode by extending LinearOpMode class."
msgstr "**LinearOpMode** クラスを継承して新しい **OpMode** を作成します。"
```

### Example 3: コードを含む

```po
#: coding.rst:20
msgid "Use the ``telemetry.addData()`` method to display data."
msgstr "``telemetry.addData()`` メソッドを使用してデータを表示します。"
```

### Example 4: リンクを含む

```po
#: intro.rst:25
msgid "For more information, see :doc:`Configuration Guide <config>`."
msgstr "詳細については、:doc:`設定ガイド <config>` を参照してください。"
```

### Example 5: 複数行

```po
#: overview.rst:30
msgid ""
"The Control Hub is a central component that manages "
"all hardware connections and provides processing power."
msgstr ""
"**Control Hub** は、すべてのハードウェア接続を管理し、"
"処理能力を提供する中心的なコンポーネントです。"
```

---

## トラブルシューティング

### Q: AIが技術用語を翻訳してしまう

**A:** プロンプトに用語リストを明示的に含めてください。また、翻訳後にスクリプトで自動修正も可能です。

### Q: RSTマークアップが壊れる

**A:** AIに「RSTマークアップをそのまま保持してください」と明示的に指示してください。

### Q: 複数行の処理がおかしい

**A:** .poファイルの構造を保持するよう指示し、msgid/msgstrのペアを明確に示してください。

### Q: 翻訳品質が低い

**A:** より詳細なプロンプトを使用し、対象読者や文脈を明確にしてください。GPT-4やClaudeなど、より高性能なモデルの使用も検討してください。

---

## 次のステップ

1. **[QUICK_START.md](QUICK_START.md)** - 基本的な.po翻訳ワークフロー
2. **[WORKFLOW.md](WORKFLOW.md)** - 日常的な翻訳作業
3. **[../reference/GLOSSARY.md](../reference/GLOSSARY.md)** - 完全な用語集

---

**AI翻訳は強力なツールですが、人間のレビューは不可欠です。必ず最終確認を行ってください。**
