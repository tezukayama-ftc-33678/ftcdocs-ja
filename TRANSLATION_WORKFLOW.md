# .po翻訳完成ワークフロー

このドキュメントは、残りの未翻訳エントリ（約5,786エントリ）を効率的に翻訳するためのワークフローを説明します。

## 📊 現状

- **翻訳済み**: 2,368エントリ (29.0%)
- **未翻訳**: 5,786エントリ (71.0%)
- **合計**: 8,144エントリ

## 🛠️ 翻訳ツール

### 新規追加されたスクリプト

プロジェクトに以下の3つのスクリプトが追加されました：

1. **`extract_for_translation.py`** - 未翻訳エントリを抽出
2. **`import_translations.py`** - 翻訳済みエントリを取り込み
3. **`batch_extract.py`** - 複数ファイルから一括抽出

## 🚀 翻訳ワークフロー

### オプション1: 単一ファイルを翻訳

#### ステップ1: 未翻訳エントリを抽出

```bash
cd /home/runner/work/ftcdocs-ja/ftcdocs-ja

# 例: index.poから30エントリを抽出
python3 docs/scripts/extract_for_translation.py \
  docs/locale/ja/LC_MESSAGES/index.po \
  index_to_translate.txt \
  30
```

#### ステップ2: AI翻訳ツールで翻訳

生成された `index_to_translate.txt` の内容を以下のいずれかのツールにコピー＆ペーストして翻訳：

- **ChatGPT** (GPT-4推奨)
- **Claude** (Anthropic)
- **DeepL**
- **Google Gemini**

#### ステップ3: 翻訳結果を保存

AI翻訳の結果を `index_translated.txt` として保存

#### ステップ4: .poファイルに反映

```bash
python3 docs/scripts/import_translations.py \
  index_translated.txt \
  docs/locale/ja/LC_MESSAGES/index.po
```

#### ステップ5: 確認とビルド

```bash
# 構文チェック
msgfmt -c docs/locale/ja/LC_MESSAGES/index.po

# ビルドしてテスト
cd docs && make ja-build
```

### オプション2: バッチで複数ファイルを翻訳

#### ステップ1: 一括抽出

```bash
cd /home/runner/work/ftcdocs-ja/ftcdocs-ja

# 未翻訳エントリが多い上位10ファイルから各30エントリを抽出
python3 docs/scripts/batch_extract.py --top 10 --entries 30
```

これにより `translation_batches/` ディレクトリに複数の抽出ファイルが作成されます：

```
translation_batches/
├── 001_tech-tips_to_translate.txt (30エントリ)
├── 002_imu_to_translate.txt (30エントリ)
├── 003_basic_rst_content_to_translate.txt (30エントリ)
└── ...
```

#### ステップ2: 各ファイルをAI翻訳

各 `.txt` ファイルをAIツールで翻訳し、`_translated.txt` として保存

#### ステップ3: 一括インポート（将来実装予定）

現在は各ファイルを個別にインポート：

```bash
python3 docs/scripts/import_translations.py \
  translation_batches/001_tech-tips_translated.txt \
  docs/locale/ja/LC_MESSAGES/tech_tips/tech-tips.po
```

## 📝 翻訳ルール（AI_TRANSLATION_GUIDE.mdより）

翻訳時は以下のルールを厳守してください：

### 1. 文体と表記

- **文体**: 「です・ます」調で統一
- **句読点**: 全角の「、」と「。」を使用
- **長音**: カタカナ語の長音（ー）は省略しない
  - ✅ コンピューター、パラメーター
  - ❌ コンピュータ、パラメータ

### 2. 技術用語

以下の用語は **太字の英語** で残してください：

#### API/クラス名
- `**OpMode**`, `**LinearOpMode**`, `**Telemetry**`, `**HardwareMap**`
- `**VisionPortal**`, `**AprilTagProcessor**`

#### 制御モード
- `**Autonomous**`, `**TeleOp**`

#### ハードウェア
- `**Control Hub**`, `**Expansion Hub**`, `**Driver Station**`
- `**Robot Controller**`, `**Driver Hub**`

#### ビジョン
- `**AprilTag**`, `**HuskyLens**`, `**OpenCV**`

#### プログラミング環境
- `**Blocks**`, `**OnBot Java**`, `**Android Studio**`

#### その他
- `**FIRST**`, `**Gracious Professionalism**`
- `**SDK**`, `**Game Manual**`

### 3. 翻訳しないもの

- コードブロック内のコード（コメントは翻訳可）
- バッククォート内のコード: `` `init()` ``
- ファイルパスやURL
- RSTディレクティブ: `:doc:`, `:ref:`, `.. note::`

### 4. RSTマークアップの保持

```
# ✅ 正しい例
msgid "See :doc:`Configuration Guide <config>`"
msgstr ":doc:`設定ガイド <config>` を参照してください"

# ❌ 間違った例（マークアップを削除してはいけない）
msgstr "設定ガイドを参照してください"
```

## 🎯 優先順位

以下の順序で翻訳することを推奨します：

### 優先度: 高

1. **index.po** (60未翻訳) - メインページ
2. **tech_tips/tech-tips.po** (321未翻訳) - 技術Tips
3. **programming_resources/imu/imu.po** (276未翻訳) - IMU関連

### 優先度: 中

4. **AprilTag関連ファイル**
   - apriltag_localization (106未翻訳)
   - visionportal_webcams (98未翻訳)
   - visionportal_camera_controls (89未翻訳)

5. **Color Processing関連**
   - color-sensor (115未翻訳)
   - color-locator-* シリーズ

### 優先度: 低

6. **Contribution ガイド**（開発者向け）
7. **製造関連**（3Dプリンティングなど）

## 📈 進捗管理

### 翻訳状況の確認

```bash
cd /home/runner/work/ftcdocs-ja/ftcdocs-ja/docs
make ja-stats
```

### 特定ファイルの翻訳率を確認

```bash
python3 -c "
import polib
po = polib.pofile('docs/locale/ja/LC_MESSAGES/index.po')
trans = len([e for e in po if e.msgid and e.msgstr and not e.obsolete])
total = len([e for e in po if e.msgid and not e.obsolete])
print(f'Translated: {trans}/{total} ({trans/total*100:.1f}%)')
"
```

## 💡 Tips

### 1. AIツールの効果的な使用

- **ChatGPT**: プロンプトと一緒に抽出ファイルを貼り付け
- **Claude**: 長文に強いため、多めのエントリを一度に処理可能
- **DeepL**: 専門用語の翻訳品質が高い

### 2. 翻訳の品質チェック

```bash
# ビルドしてエラーを確認
cd docs && make ja-build

# 警告を確認
cd docs && make ja-build 2>&1 | grep -i warning
```

### 3. バッチ処理

一度に30-50エントリずつ翻訳することで、AIツールの精度とスピードのバランスを取ります。

## ⚠️ 注意事項

### よくある間違い

1. **技術用語を翻訳してしまう**
   - ❌ "OpMode" → "オペレーションモード"
   - ✅ "**OpMode**"

2. **太字マークアップを忘れる**
   - ❌ "OpMode"
   - ✅ "**OpMode**"

3. **RSTマークアップを削除してしまう**
   - ❌ `:doc:` を削除
   - ✅ `:doc:` を保持

### ビルドエラーが出た場合

```bash
# エラーログを確認
cat docs/build/ja.log

# トラブルシューティングガイドを参照
cat docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md
```

## 📚 参考資料

- **AI翻訳ガイド**: `po-translation/guides/AI_TRANSLATION_GUIDE.md`
- **用語集**: `po-translation/reference/GLOSSARY.md`
- **コマンドリファレンス**: `po-translation/reference/COMMANDS.md`
- **RSTトラブルシューティング**: `docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md`

## 🎉 完成後

すべての翻訳が完了したら：

1. **最終ビルドテスト**
   ```bash
   cd docs && make clean && make ja-build
   ```

2. **翻訳統計の更新**
   ```bash
   python3 docs/scripts/check_translation_progress.py
   ```

3. **プルリクエストの作成**

---

**このワークフローを使用して、効率的に残りの5,786エントリを翻訳しましょう！**
