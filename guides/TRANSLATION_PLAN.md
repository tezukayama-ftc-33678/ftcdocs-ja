# FTC ドキュメント翻訳計画 (TRANSLATION_PLAN)

このドキュメントは、`locales/ja/LC_MESSAGES` 以下の .po ファイルの翻訳計画を記載しています。  
**TRANSLATION_GUIDE.md** と **GLOSSARY.md** に準拠して翻訳を進めます。

---

## 📊 翻訳対象の概要

- **総ファイル数**: 255 ファイル
- **総エントリ数**: 4,176 エントリ
- **現在の翻訳率**: 0%
- **更新日**: 2025-12-16

---

## 🎯 翻訳戦略

### 基本方針

1. **段階的な翻訳**: 重要度と優先度の高いカテゴリから順次翻訳
2. **品質重視**: TRANSLATION_GUIDE.md と GLOSSARY.md に厳密に準拠
3. **一貫性の確保**: 用語統一リストを参照し、表記の統一を徹底
4. **検証体制**: 各フェーズ完了時に翻訳内容を検証

### 優先順位の基準

1. **ユーザー影響度**: 初心者・新規チームが最初に見るページ
2. **コンテンツ量**: エントリ数が多く、翻訳の効果が大きいカテゴリ
3. **技術的重要度**: プログラミングやハードウェア設定など、技術的に重要な内容
4. **アクセス頻度**: ドキュメント内でよく参照されるページ

---

## 📋 フェーズ別翻訳計画

### Phase 1: コアページ・導入コンテンツ（最優先）

**目標**: 新規ユーザーが最初に見るページと基本的な導入コンテンツを翻訳

**対象カテゴリ**:
- `root` (4 ファイル, 74 エントリ)
  - `index.po` - トップページ (56 エントリ) ★最重要
  - `404.po` (2 エントリ)
  - `sphinx.po` (15 エントリ)
  - `todo.po` (1 エントリ)
  
- `overview` (1 ファイル, 4 エントリ)
  - `overview/ftcoverview.po` (4 エントリ)

- `persona_pages` (4 ファイル, 71 エントリ)
  - `persona_pages/rookie_teams/rookie_teams.po` (31 エントリ) ★重要
  - `persona_pages/coach_admin/coach_admin.po` (16 エントリ)
  - `persona_pages/veteran_teams/veteran_teams.po` (13 エントリ)
  - `persona_pages/mentor_tech/mentor_tech.po` (11 エントリ)

- `gracious_professionalism` (1 ファイル, 8 エントリ)
  - `gracious_professionalism/gp.po` (8 エントリ)

**Phase 1 合計**: 10 ファイル, 157 エントリ

**推定作業時間**: 3-4 時間

---

### Phase 2: ハードウェア・ソフトウェア設定

**目標**: ロボットのセットアップに必要な基本的な設定情報を翻訳

**対象カテゴリ**:
- `hardware_and_software_configuration` (20 ファイル, 201 エントリ)
  - 優先順位の高いファイル:
    - `self_inspect/self-inspect.po` (41 エントリ)
    - `configuring/managing_esd/managing-esd.po` (27 エントリ)
    - `self_inspect/new-self-inspect.po` (25 エントリ)
  - その他の設定ファイル群

- `ftc_sdk` (8 ファイル, 150 エントリ)
  - `updating/rc_app/Updating-the-RC-App.po` (39 エントリ)
  - `updating/ds_app/Updating-the-DS-App.po` (31 エントリ)
  - `updating/hub_firmware/Updating-Hub-Firmware.po` (23 エントリ)
  - その他のアップデート関連ファイル

- `control_hard_compon` (14 ファイル, 291 エントリ)
  - `rc_components/sensors/sensors.po` (69 エントリ)
  - `rc_components/power_distr/power-distr.po` (60 エントリ)
  - その他のハードウェアコンポーネント

**Phase 2 合計**: 42 ファイル, 642 エントリ

**推定作業時間**: 10-12 時間

---

### Phase 3: プログラミング基礎

**目標**: プログラミング環境のセットアップと基本的なチュートリアルを翻訳

**対象カテゴリ**:
- `programming_resources` から優先度の高いファイルを選択
  - `laptops/laptops.po` (67 エントリ)
  - `shared/configuring_android/Configuring-Your-Android-Devices.po` (118 エントリ)
  - Blocks 関連の基礎ファイル
  - OnBot Java 関連の基礎ファイル
  - Android Studio 関連の基礎ファイル

**Phase 3 対象**: 約 20-25 ファイル, 約 400-500 エントリ

**推定作業時間**: 8-10 時間

---

### Phase 4: ビジョン処理（AprilTag・Color Processing）

**目標**: 画像認識と色処理に関する重要な技術ドキュメントを翻訳

**対象カテゴリ**:
- `apriltag` (20 ファイル, 605 エントリ)
  - `vision_portal/apriltag_intro/apriltag-intro.po` (63 エントリ)
  - `vision_portal/visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth.po` (66 エントリ)
  - その他の AprilTag 関連ファイル

- `color_processing` (8 ファイル, 336 エントリ)
  - `color-locator-round-blobs/color-locator-round-blobs.po` (70 エントリ)
  - `color-sensor/color-sensor.po` (64 エントリ)
  - `color-locator-challenge/color-locator-challenge.po` (56 エントリ)
  - その他の色処理関連ファイル

- `devices` (1 ファイル, 81 エントリ)
  - `huskylens/huskylens.po` (81 エントリ)

**Phase 4 合計**: 29 ファイル, 1,022 エントリ

**推定作業時間**: 15-18 時間

---

### Phase 5: プログラミング応用・IMU

**目標**: 高度なプログラミング技術と IMU センサーの活用方法を翻訳

**対象カテゴリ**:
- `programming_resources` の残り
  - `imu/imu.po` (160 エントリ) ★重要
  - その他の高度なプログラミングトピック

**Phase 5 対象**: 約 70 ファイル, 約 600-700 エントリ

**推定作業時間**: 12-15 時間

---

### Phase 6: ゲーム固有リソース・FAQ・その他

**目標**: ゲーム関連の情報、FAQ、技術 TIPS などを翻訳

**対象カテゴリ**:
- `game_specific_resources` (4 ファイル, 43 エントリ)
- `faq` (1 ファイル, 11 エントリ)
- `tech_tips` (3 ファイル, 156 エントリ)
- `team_resources` (1 ファイル, 10 エントリ)
- `tos` (1 ファイル, 32 エントリ)
- `sponsors` (2 ファイル, 43 エントリ)
- `booklets` (5 ファイル, 22 エントリ)
- `ai` (1 ファイル, 21 エントリ)
- `manuals` (1 ファイル, 1 エントリ)
- `cad_resources` (4 ファイル, 22 エントリ)

**Phase 6 合計**: 23 ファイル, 361 エントリ

**推定作業時間**: 6-8 時間

---

### Phase 7: Manufacturing・貢献者向けドキュメント

**目標**: 製造関連と貢献者向けのドキュメントを翻訳（優先度低）

**対象カテゴリ**:
- `manufacturing` (32 ファイル, 407 エントリ)
  - 3D プリンティング関連
  - プリンター選択ガイド
  
- `contrib` (24 ファイル, 543 エントリ)
  - 貢献者向けガイドライン
  - RST ドキュメント作成チュートリアル

**Phase 7 合計**: 56 ファイル, 950 エントリ

**推定作業時間**: 15-18 時間

---

## 📈 進捗管理

### 翻訳状況の確認方法

```bash
# 翻訳率の確認
msgfmt --statistics locales/ja/LC_MESSAGES/<path>/<file>.po

# すべての .po ファイルの統計を一括確認
find locales/ja/LC_MESSAGES -name "*.po" -exec msgfmt --statistics {} \;
```

### 翻訳完了の基準

1. すべての msgstr フィールドが適切に翻訳されている
2. TRANSLATION_GUIDE.md と GLOSSARY.md に準拠している
3. 技術用語の統一が守られている
4. RST マークアップが正しく保持されている
5. レビューを経て品質が確認されている

---

## 🔧 翻訳ツールと環境

### 推奨ツール

1. **Poedit** - .po ファイル専用エディタ
2. **VSCode** + gettext 拡張機能
3. **DeepL** - 機械翻訳の参考（そのまま使用は NG）

### 品質チェック

```bash
# .po ファイルの構文チェック
msgfmt -c -v -o /dev/null <file>.po

# 翻訳の一貫性チェック
msgcmp <file>.po <reference>.pot
```

---

## 📝 翻訳時の注意事項

### 必須ルール

1. **TRANSLATION_GUIDE.md を熟読**: 翻訳前に必ず確認
2. **GLOSSARY.md を参照**: 用語統一リストに従う
3. **太字の保持**: `**OpMode**` などの API 名は英語のまま太字で
4. **RST マークアップの保持**: `:doc:`、`.. code-block::` などを変更しない
5. **です・ます調**: 文体を統一
6. **リンク・URL の保持**: 外部リンクは変更しない

### 禁止事項

1. **機械翻訳の無批判な使用**: DeepL などの出力をそのまま貼り付けない
2. **用語の不統一**: 同じ概念に異なる訳語を使用しない
3. **RST マークアップの破壊**: ビルドエラーの原因となる
4. **コードの翻訳**: コード例やコメント内のコードを勝手に変更しない

---

## 🚀 Phase 1 実施内容（本タスク）

本タスクでは **Phase 1** を完了させます。

### Phase 1 対象ファイル

1. ✅ `index.po` (56 エントリ) - トップページ
2. ✅ `404.po` (2 エントリ) - 404 エラーページ
3. ✅ `sphinx.po` (15 エントリ) - Sphinx 関連
4. ✅ `todo.po` (1 エントリ) - TODO リスト
5. ✅ `overview/ftcoverview.po` (4 エントリ) - FTC 概要
6. ✅ `persona_pages/rookie_teams/rookie_teams.po` (31 エントリ) - 新規チーム向け
7. ✅ `persona_pages/coach_admin/coach_admin.po` (16 エントリ) - コーチ・管理者向け
8. ✅ `persona_pages/veteran_teams/veteran_teams.po` (13 エントリ) - 既存チーム向け
9. ✅ `persona_pages/mentor_tech/mentor_tech.po` (11 エントリ) - メンター向け
10. ✅ `gracious_professionalism/gp.po` (8 エントリ) - Gracious Professionalism

**合計**: 10 ファイル, 157 エントリ

---

## 📅 今後のスケジュール

- **Phase 1**: 2025-12-16 完了予定
- **Phase 2**: 2025-12-17 - 2025-12-18
- **Phase 3**: 2025-12-19 - 2025-12-20
- **Phase 4**: 2025-12-21 - 2025-12-23
- **Phase 5**: 2025-12-24 - 2025-12-26
- **Phase 6**: 2025-12-27 - 2025-12-28
- **Phase 7**: 2025-12-29 - 2026-01-02

---

## 参考資料

- [TRANSLATION_GUIDE.md](./TRANSLATION_GUIDE.md) - 翻訳ガイドライン
- [GLOSSARY.md](./GLOSSARY.md) - 用語統一リスト
- [README.md](./README.md) - プロジェクト概要

---

**更新履歴**

| 日付 | 内容 |
|------|------|
| 2025-12-16 | 初版作成 - 翻訳計画の策定 |
