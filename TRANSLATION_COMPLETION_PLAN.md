# .po翻訳完成計画

## 📊 現在の状況（2025-12-14）

### 翻訳統計

- **翻訳済み**: 2,418エントリ (29.7%)
- **未翻訳**: 5,726エントリ (70.3%)
- **合計**: 8,144エントリ

### 完了済みファイル

✅ **index.po** - メインページ (67/67エントリ, 100%)

## 🎯 完成へのロードマップ

### フェーズ1: コアドキュメントの翻訳（推定: 1,500エントリ）

優先度の高いコアドキュメントから翻訳：

1. **index.po** (67エントリ) ✅ 完了
2. **overview/ftcoverview.po** (13エントリ) - FTC概要
3. **gracious_professionalism/gp.po** - Gracious Professionalism
4. **faq/faqs.po** - FAQ

**推定作業時間**: 3-5時間（AI翻訳使用）

### フェーズ2: プログラミング基礎（推定: 1,800エントリ）

初心者向けプログラミングチュートリアル：

1. **programming_resources/blocks/** - Blocks チュートリアル
   - Blocks-Tutorial.po
   - config/, intro/, opmode/ など
2. **programming_resources/onbot_java/** - OnBot Java チュートリアル
3. **programming_resources/android_studio_java/** - Android Studio チュートリアル

**推定作業時間**: 6-8時間（AI翻訳使用）

### フェーズ3: ハードウェアと設定（推定: 800エントリ）

ハードウェア接続と設定：

1. **hardware_and_software_configuration/** - ハードウェア設定
2. **control_hard_compon/** - 制御システムコンポーネント
3. **devices/** - デバイス（HuskyLensなど）

**推定作業時間**: 3-4時間（AI翻訳使用）

### フェーズ4: AprilTagとビジョン（推定: 1,200エントリ）

ビジョンとAprilTag関連：

1. **apriltag/vision_portal/** - VisionPortal関連
   - apriltag_intro.po
   - apriltag_localization.po
   - visionportal_webcams.po など
2. **programming_resources/vision/** - ビジョンプログラミング

**推定作業時間**: 4-6時間（AI翻訳使用）

### フェーズ5: 色処理（推定: 600エントリ）

Color Locatorと色センサー：

1. **color_processing/** - 色処理全般
   - color-sensor.po
   - color-locator-*.po シリーズ
   - color-spaces.po

**推定作業時間**: 2-3時間（AI翻訳使用）

### フェーズ6: 技術ドキュメント（推定: 600エントリ）

技術的な詳細ドキュメント：

1. **programming_resources/imu/imu.po** (276エントリ) - IMU詳細
2. **tech_tips/tech-tips.po** (321エントリ) - 技術Tips
3. **ftc_sdk/** - SDK関連

**推定作業時間**: 2-4時間（AI翻訳使用）

### フェーズ7: 貢献者向けドキュメント（推定: 400エントリ）

開発者・貢献者向け（優先度: 低）：

1. **contrib/** - コントリビューションガイド
   - style-guide.po
   - make_rst/ シリーズ
   - make_pr.po

**推定作業時間**: 2-3時間（AI翻訳使用）

### フェーズ8: その他リソース（推定: 800エントリ）

その他のリソース：

1. **manufacturing/** - 製造関連
2. **cad_resources/** - CADリソース
3. **game_specific_resources/** - ゲーム固有リソース
4. **sponsors/** - スポンサー情報

**推定作業時間**: 3-4時間（AI翻訳使用）

## ⏱️ 総推定作業時間

- **AI翻訳を使用した場合**: 25-35時間
- **手動翻訳の場合**: 150-200時間

## 🚀 効率的な翻訳手順

### 1日の翻訳セッション例（2-3時間）

```bash
# 1. バッチ抽出（5分）
python3 docs/scripts/batch_extract.py --top 5 --entries 30

# 2. AI翻訳（1.5-2時間）
# - translation_batches/の各ファイルをChatGPT/Claudeで翻訳
# - 30エントリ×5ファイル = 150エントリ/セッション

# 3. インポート（10分）
for file in translation_batches/*_translated.txt; do
    python3 docs/scripts/import_translations.py $file <対応する.po>
done

# 4. ビルドテスト（10分）
cd docs && make ja-build

# 結果: 1セッションで150エントリ完了
```

### 週次目標

- **週1セッション（2時間）**: 150エントリ
- **週2セッション（4時間）**: 300エントリ
- **週3セッション（6時間）**: 450エントリ

### 完成までのスケジュール

- **週3セッション**: 約13週間（3ヶ月）
- **週2セッション**: 約19週間（4.5ヶ月）
- **週1セッション**: 約38週間（9ヶ月）

## 📝 品質管理

### 各フェーズ後のチェックリスト

- [ ] すべてのmsgstrが埋まっている
- [ ] 技術用語が **太字** で英語のまま
- [ ] RSTマークアップが保持されている
- [ ] ビルドエラーがない
- [ ] 翻訳統計を更新

### 品質チェックコマンド

```bash
# 翻訳統計
cd docs && make ja-stats

# ビルドテスト
cd docs && make ja-build

# 特定ファイルの完成度チェック
python3 -c "
import polib
po = polib.pofile('docs/locale/ja/LC_MESSAGES/FILE.po')
trans = len([e for e in po if e.msgid and e.msgstr and not e.obsolete])
total = len([e for e in po if e.msgid and not e.obsolete])
print(f'Progress: {trans}/{total} ({trans/total*100:.1f}%)')
"
```

## 🤝 協力体制

### 複数人で翻訳する場合

1. **ファイル単位で分担**
   - 各人が特定のフェーズを担当
   - Gitブランチで作業を分離

2. **バッチ単位で分担**
   - batch_extract.pyで抽出
   - 各バッチファイルを個別に担当

3. **レビュー体制**
   - 翻訳後の相互レビュー
   - 用語の統一性チェック

## 📚 参考資料

### 必読ドキュメント

1. **TRANSLATION_WORKFLOW.md** - 翻訳ワークフロー
2. **po-translation/guides/AI_TRANSLATION_GUIDE.md** - AI翻訳ガイド
3. **po-translation/reference/GLOSSARY.md** - 用語集

### 翻訳支援ツール

1. **extract_for_translation.py** - エントリ抽出
2. **import_translations.py** - 翻訳インポート
3. **batch_extract.py** - バッチ抽出

## 🎯 マイルストーン

### 短期（1ヶ月）

- [ ] フェーズ1完了（コアドキュメント）
- [ ] フェーズ2開始（プログラミング基礎）
- [ ] 翻訳率40%達成

### 中期（3ヶ月）

- [ ] フェーズ1-5完了
- [ ] 翻訳率70%達成
- [ ] 主要機能のドキュメント完成

### 長期（6ヶ月）

- [ ] すべてのフェーズ完了
- [ ] 翻訳率100%達成
- [ ] 品質レビュー完了
- [ ] 公開準備完了

## 🏆 完成条件

### 必須条件

- [ ] すべての.poファイルが100%翻訳済み
- [ ] ビルドエラーなし
- [ ] 技術用語の統一性確認
- [ ] リンクとマークアップの正常動作確認

### 推奨条件

- [ ] ネイティブスピーカーによるレビュー
- [ ] 実際のユーザーによるテスト
- [ ] フィードバックの反映

## 📞 サポート

### 質問・問題が発生した場合

1. **TRANSLATION_WORKFLOW.md** を確認
2. **RST_TROUBLESHOOTING_GUIDE.md** を確認
3. GitHub Issuesで質問

### 進捗報告

- 週次で翻訳統計を更新
- フェーズ完了時に報告
- 問題点の早期共有

---

**このロードマップに従って、効率的に.po翻訳を完成させましょう！**

**最終更新**: 2025-12-14
