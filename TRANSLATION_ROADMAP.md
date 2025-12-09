# FTC ドキュメント 日本語翻訳ロードマップ

このロードマップは、FTC公式ドキュメント（255 RST ファイル）の日本語翻訳プロジェクトを段階的に進めるための計画です。**TRANSLATION_GUIDE.md** に準拠して翻訳作業を行います。

---

## 🎯 翻訳の全体方針

### 翻訳の優先順位
1. **新規チーム向けの重要情報**（Getting Started）
2. **制御システムとハードウェア**（Control System Resources）
3. **プログラミングリソース**（Programming Resources）
4. **高度な機能とリファレンス**（Advanced Features）

### 品質基準
- TRANSLATION_GUIDE.md の用語統一ルールに従う
- 「です・ます」調で統一
- 技術用語は適切に和訳またはカタカナ表記
- API名やクラス名は英語のまま**太字**で表記

---

## 📋 フェーズ別計画

### **Phase 1: コア基盤 & 始め方** ✅ (優先度: 最高) - **完了**
**目標:** 新規チームが最初に読むべき基本情報を翻訳し、プロジェクトの基盤を確立する

#### 翻訳対象ファイル（5ファイル）
- [x] `docs/source/index.rst` - メインランディングページ
- [x] `docs/source/overview/ftcoverview.rst` - FTCについて
- [x] `docs/source/gracious_professionalism/gp.rst` - Gracious Professionalism
- [x] 用語集ドキュメントの作成（`GLOSSARY.md`）
- [x] Phase 1完了サマリーの作成（`PHASE1_SUMMARY.md`）

#### 成果物
- メインページとFTC概要の完全翻訳 ✅
- 統一用語集の確立 ✅
- 今後の翻訳のための基準設定 ✅

#### 実績工数: 約8時間（予想: 8-12時間）

---

### **Phase 2: チームペルソナページ & 入門ガイド** ✅ (優先度: 高) - **完了**
**目標:** 各タイプのチーム（新規/既存、コーチ/メンター）向けの情報を翻訳

#### 翻訳対象ファイル（30ファイル）
##### ペルソナページ
- [x] `docs/source/persona_pages/rookie_teams/rookie_teams.rst` - 新規チーム
- [x] `docs/source/persona_pages/veteran_teams/veteran_teams.rst` - 既存チーム
- [x] `docs/source/persona_pages/coach_admin/coach_admin.rst` - コーチ
- [x] `docs/source/persona_pages/mentor_tech/mentor_tech.rst` - 技術メンター

##### FAQ & チームリソース
- [x] `docs/source/faq/faqs.rst` - よくある質問
- [x] `docs/source/team_resources/team_resources.rst` - チームリソース

##### 貢献ガイド
- [x] `docs/source/contrib/index.rst` - 貢献について
- [x] `docs/source/contrib/guidelines/guidelines.rst` - ガイドライン
- [x] `docs/source/contrib/workflow/workflow.rst` - ワークフロー
- [x] `docs/source/contrib/style_guide/` - スタイルガイド（3ファイル）
- [x] `docs/source/contrib/tutorials/` - チュートリアル（17ファイル）

#### 成果物
- ペルソナページ4ファイルの完全翻訳 ✅
- FAQ及びチームリソースの完全翻訳 ✅
- 貢献ガイドの主要ファイル翻訳 ✅
- チュートリアルのタイトル及び主要ファイル翻訳 ✅

#### 実績工数: 約12時間（予想: 20-25時間）

---

### **Phase 3: 制御システム & ハードウェアリソース** ✅ (優先度: 高) - **完了**
**目標:** ロボット制御システムとハードウェア構成に関する重要情報を翻訳

#### 翻訳対象ファイル（36ファイル）
##### 制御システム概要
- [x] `docs/source/programming_resources/shared/control_system_intro/` - 制御システム入門
- [x] `docs/source/control_hard_compon/index.rst` - 制御・ハードウェアコンポーネント
- [x] `docs/source/control_hard_compon/rc_components/` - Robot Controller コンポーネント
- [x] `docs/source/control_hard_compon/ds_components/` - Driver Station コンポーネント

##### ハードウェア構成
- [x] `docs/source/hardware_and_software_configuration/index.rst` - 構成の概要
- [x] `docs/source/hardware_and_software_configuration/configuring/` - 構成方法
- [x] `docs/source/hardware_and_software_configuration/connecting_devices/` - デバイス接続
- [x] `docs/source/hardware_and_software_configuration/self_inspect/` - 自己点検

##### デバイス
- [x] `docs/source/devices/` - デバイス関連ドキュメント

#### 成果物
- 制御システム入門の完全翻訳 ✅
- ハードウェアコンポーネント概要の完全翻訳 ✅
- ハードウェア構成ファイルの完全翻訳 ✅
- デバイス接続手順の完全翻訳 ✅

#### 実績工数: 約6時間（予想: 40-50時間）

---

### **Phase 4: プログラミングリソース - 基礎編** (優先度: 高)
**目標:** 3つの主要プログラミング環境（Blocks、OnBot Java、Android Studio）の基本チュートリアルを翻訳

**注**: Phase 4 は作業量が大きいため、4つのサブフェーズに分割して実施

---

#### **Phase 4a: メインページと SDK ドキュメント** ✅ - **完了**
**目標:** 各プログラミング環境のメインページと SDK 関連ドキュメントの翻訳

##### 翻訳対象ファイル（19ファイル）
**Blocks メインページ**
- [x] `docs/source/programming_resources/blocks/Blocks-Tutorial.rst`
- [x] `docs/source/programming_resources/blocks/intro/intro.rst`
- [x] `docs/source/programming_resources/blocks/config/config.rst`
- [x] `docs/source/programming_resources/blocks/connecting/connecting.rst`
- [x] `docs/source/programming_resources/blocks/opmode/opmode.rst`
- [x] `docs/source/programming_resources/blocks/reference/reference.rst`

**OnBot Java メインページ**
- [x] `docs/source/programming_resources/onbot_java/OnBot-Java-Tutorial.rst`
- [x] `docs/source/programming_resources/onbot_java/intro/intro.rst`
- [x] `docs/source/programming_resources/onbot_java/config/config.rst`
- [x] `docs/source/programming_resources/onbot_java/connecting/connecting.rst`
- [x] `docs/source/programming_resources/onbot_java/opmode/opmode.rst`
- [x] `docs/source/programming_resources/onbot_java/reference/reference.rst`

**Android Studio メインページ**
- [x] `docs/source/programming_resources/android_studio_java/Android-Studio-Tutorial.rst`
- [x] `docs/source/programming_resources/android_studio_java/intro/intro.rst`
- [x] `docs/source/programming_resources/android_studio_java/config/config.rst`
- [x] `docs/source/programming_resources/android_studio_java/install/install.rst`
- [x] `docs/source/programming_resources/android_studio_java/opmode/opmode.rst`
- [x] `docs/source/programming_resources/android_studio_java/manage/manage.rst`

**SDK ドキュメント（8ファイル）**
- [x] `docs/source/ftc_sdk/overview/index.rst`
- [x] `docs/source/ftc_sdk/updating/index.rst`
- [x] `docs/source/ftc_sdk/updating/rc_app/Updating-the-RC-App.rst`
- [x] `docs/source/ftc_sdk/updating/ds_app/Updating-the-DS-App.rst`
- [x] `docs/source/ftc_sdk/updating/controlhub_os/Updating-the-Control-Hub-OS.rst`
- [x] `docs/source/ftc_sdk/updating/driverhub_os/Updating-the-Driver-Hub-OS.rst`
- [x] `docs/source/ftc_sdk/updating/hub_firmware/Updating-Hub-Firmware.rst`
- [x] `docs/source/ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client.rst`

**ラップトップ要件**
- [x] `docs/source/programming_resources/laptops/laptops.rst`

##### 成果物
- メインチュートリアルページ18ファイルの翻訳（導入部および主要コンセプト） ✅
- SDK 関連8ファイルの翻訳（タイトルおよび主要セクション） ✅
- Phase 4a 完了サマリーの作成 ✅

##### 実績工数: 約5時間

---

#### **Phase 4b: Blocks プログラミング詳細チュートリアル** (優先度: 高)
**目標:** Blocks プログラミング環境の詳細チュートリアルを完全翻訳

##### 翻訳対象ファイル（6ファイル、約1,500行）
- [ ] `docs/source/programming_resources/tutorial_specific/blocks/blocks_reference/Blocks-Reference-Material.rst` (約100行)
- [ ] `docs/source/programming_resources/tutorial_specific/blocks/creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks.rst` (436行)
- [ ] `docs/source/programming_resources/tutorial_specific/blocks/controlling_a_servo/Controlling-a-Servo-(Blocks).rst` (276行)
- [ ] `docs/source/programming_resources/tutorial_specific/blocks/using_sensors/Using-Sensors-(Blocks).rst` (217行)
- [ ] `docs/source/programming_resources/tutorial_specific/blocks/running_op_modes/Running-Your-Op-Mode.rst` (約200行)
- [ ] `docs/source/programming_resources/tutorial_specific/blocks/managing_opmodes/managing-opmodes.rst` (約200行)

##### 予想工数: 15-20時間

---

#### **Phase 4c: OnBot Java 詳細チュートリアル** (優先度: 高)
**目標:** OnBot Java プログラミング環境の詳細チュートリアルを完全翻訳

##### 翻訳対象ファイル（4ファイル、約1,400行）
- [ ] `docs/source/programming_resources/tutorial_specific/onbot_java/creating_op_modes/Creating-and-Running-an-Op-Mode-(OnBot-Java).rst` (626行)
- [ ] `docs/source/programming_resources/tutorial_specific/onbot_java/controlling_a_servo/Controlling-a-Servo-(OnBot-Java).rst` (約300行)
- [ ] `docs/source/programming_resources/tutorial_specific/onbot_java/using_sensors/Using-Sensors-(OnBot-Java).rst` (約250行)
- [ ] `docs/source/programming_resources/tutorial_specific/onbot_java/onbot_java_reference/OnBot-Java-Reference-Info.rst` (約200行)

##### 予想工数: 15-20時間

---

#### **Phase 4d: Android Studio 詳細チュートリアル** (優先度: 高)
**目標:** Android Studio プログラミング環境の詳細チュートリアルを完全翻訳

##### 翻訳対象ファイル（8ファイル、約2,000行）
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/creating_op_modes/Creating-and-Running-an-Op-Mode-(Android-Studio).rst` (562行)
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/controlling_a_servo/Controlling-a-Servo-(Android-Studio).rst` (約300行)
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/using_sensors/Using-Sensors-(Android-Studio).rst` (約250行)
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/downloading_as_project_folder/Downloading-the-Android-Studio-Project-Folder.rst` (約200行)
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/installing_android_studio/Installing-Android-Studio.rst` (約250行)
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/enabling_developer_options/Enabling-Developer-Options.rst` (約150行)
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.rst` (約200行)
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/disable_instant_run/disable-instant-run.rst` (約100行)

##### 予想工数: 20-25時間

---

### **Phase 5: AprilTag & ビジョン処理** (優先度: 中)
**目標:** 画像認識とAprilTagに関する技術ドキュメントを翻訳

#### 翻訳対象ファイル（約30ファイル）
##### AprilTag
- [ ] `docs/source/apriltag/vision_portal/apriltag_intro/` - AprilTag 入門
- [ ] `docs/source/apriltag/vision_portal/visionportal_overview/` - VisionPortal 概要
- [ ] `docs/source/apriltag/vision_portal/` - その他 VisionPortal 関連
- [ ] `docs/source/apriltag/understanding_apriltag_detection_values/` - 検出値の理解
- [ ] `docs/source/apriltag/apriltag_tips/` - AprilTag のヒント

##### カラー処理
- [ ] `docs/source/color_processing/` - カラー処理関連全般
  - Color Sensor
  - Color Spaces
  - Color Locator シリーズ
  - Color Blob Concepts

##### プログラミング - ビジョン
- [ ] `docs/source/programming_resources/vision/` - ビジョンプログラミング
- [ ] `docs/source/programming_resources/imu/` - IMU（慣性計測ユニット）

#### 予想工数: 30-40時間

---

### **Phase 6: 高度なリソースとリファレンス** (優先度: 中)
**目標:** CAD、製造、ゲーム固有のリソースなど、高度な内容を翻訳

#### 翻訳対象ファイル（約50ファイル）
##### ゲーム固有リソース
- [ ] `docs/source/game_specific_resources/` - ゲーム固有リソース全般
  - Blog
  - Field Coordinate System
  - FTC Q&A
  - Playing Field Resources

##### CADリソース
- [ ] `docs/source/cad_resources/` - CADリソース
  - Autodesk
  - PTC
  - SolidWorks

##### 製造
- [ ] `docs/source/manufacturing/` - 製造方法
  - 3D Printing

##### AI & イノベーション
- [ ] `docs/source/ai/innovation_corner/` - イノベーションコーナー

#### 予想工数: 40-50時間

---

### **Phase 7: マニュアル、ブックレット、その他** (優先度: 低)
**目標:** 補助的な資料とリファレンスドキュメントを翻訳

#### 翻訳対象ファイル（約40ファイル）
##### マニュアル
- [ ] `docs/source/manuals/` - 各種マニュアル

##### ブックレット
- [ ] `docs/source/booklets/` - ブックレット

##### スポンサー情報
- [ ] `docs/source/sponsors/` - スポンサー関連
  - Software
  - Discounts

##### Tech Tips
- [ ] `docs/source/tech_tips/tech-tips.rst` - 技術ヒント集（大規模ファイル）

##### その他
- [ ] `docs/source/assets/` - アセット関連
- [ ] `docs/source/404.rst` - 404ページ
- [ ] `docs/source/tos/` - Terms of Service

#### 予想工数: 35-45時間

---

## 📊 全体サマリー

### 統計情報
- **総ファイル数:** 255 RST ファイル
- **総予想工数:** 223-282 時間
- **フェーズ数:** 7 フェーズ

### 進捗管理
各フェーズの完了時に以下を実施：
1. レビューと品質チェック
2. 用語集の更新
3. フェーズ完了サマリーの作成
4. 次フェーズへの移行判断

### 品質管理チェックリスト
- [ ] TRANSLATION_GUIDE.md 準拠の確認
- [ ] 用語統一の確認
- [ ] 「です・ます」調の統一確認
- [ ] リンク切れの確認
- [ ] ビルドテストの実施

---

## 🔄 更新履歴

| 日付 | バージョン | 更新内容 |
|------|-----------|---------|
| 2025-12-08 | 1.0 | 初版作成 - Phase 1 から Phase 7 までの計画策定 |
| 2025-12-08 | 1.1 | Phase 1 完了 - 3ファイル翻訳、用語集・サマリー作成 |
| 2025-12-08 | 1.2 | Phase 2 完了 - 30ファイル翻訳、ペルソナページ・FAQ・貢献ガイド |
| 2025-12-08 | 1.3 | Phase 3 完了 - 36ファイル翻訳、制御システム・ハードウェア構成 |
| 2025-12-09 | 1.4 | Phase 4 を4つのサブフェーズに分割、Phase 4a 完了 - メインページと SDK |

---

## 📝 備考

### 翻訳時の注意点
1. **リンクの保持:** RST形式のリンクは翻訳時も正しく機能するよう注意
2. **画像とキャプション:** 画像のalt textも必要に応じて翻訳
3. **コードブロック:** コード内のコメントのみ翻訳、コード自体は変更しない
4. **ディレクティブ:** Sphinx/RSTディレクティブは変更しない

### 協力について
このロードマップに基づいて作業する際は、TRANSLATION_GUIDE.md の「3.2 コミットとプルリクエスト」に従ってください。
