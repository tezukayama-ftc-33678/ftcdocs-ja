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
- 技術用語は適切に和訳またはカタカナ表記(GLOSSARY.mdも参照)
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
**目標:** 3つの主要プログラミング環境（Blocks、OnBot Java、Android Studio）の基本チュートリアル、共通リソース、SDK、ビジョン処理、IMUなど、プログラミングに関連する全てのリソースを翻訳

> **⚠️ 翻訳時の注意:**
> - 一部のファイルは500行以上の大規模ファイルです（例: Creating-and-Running-an-Op-Mode 系のファイル）
> - IMUファイルは1194行の超大規模ファイルです
> - 生成AIは大規模ファイルの翻訳中に、途中で翻訳が完了したと誤認する可能性があります
> - ファイルの最後まで翻訳されているか必ず確認してください
> - 翻訳が途中で終わっている場合は、残りの部分を続けて翻訳してください

#### Sub-Phase 4.1: Blocks プログラミング - チュートリアル基礎 ✅ **完了**
##### チュートリアルメインファイル（2ファイル、517行）
- [x] `docs/source/programming_resources/blocks/Blocks-Tutorial.rst` - **37行** Blocks チュートリアル
- [x] `docs/source/programming_resources/tutorial_specific/blocks/creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks.rst` - **480行** Op Mode作成

##### 実績工数: 約2時間

#### Sub-Phase 4.2: Blocks プログラミング - センサーと機能 ✅ **完了**
##### チュートリアル応用ファイル（5ファイル、655行）
- [x] `docs/source/programming_resources/tutorial_specific/blocks/using_sensors/Using-Sensors-(Blocks).rst` - **178行** センサー利用
- [x] `docs/source/programming_resources/tutorial_specific/blocks/controlling_a_servo/Controlling-a-Servo-(Blocks).rst` - **242行** サーボ制御
- [x] `docs/source/programming_resources/tutorial_specific/blocks/managing_opmodes/managing-opmodes.rst` - **91行** Op Mode管理
- [x] `docs/source/programming_resources/tutorial_specific/blocks/running_op_modes/Running-Your-Op-Mode.rst` - **97行** Op Mode実行
- [x] `docs/source/programming_resources/tutorial_specific/blocks/blocks_reference/Blocks-Reference-Material.rst` - **47行** リファレンス資料

##### 実績工数: 約2時間

#### Sub-Phase 4.2b: Blocks プログラミング - 構成とリファレンス
##### Blocksメインディレクトリファイル（5ファイル、41行）
- [ ] `docs/source/programming_resources/blocks/config/config.rst` - **8行** 構成
- [ ] `docs/source/programming_resources/blocks/connecting/connecting.rst` - **8行** 接続
- [ ] `docs/source/programming_resources/blocks/intro/intro.rst` - **9行** イントロ
- [ ] `docs/source/programming_resources/blocks/opmode/opmode.rst` - **10行** Op Mode
- [ ] `docs/source/programming_resources/blocks/reference/reference.rst` - **6行** リファレンス

##### 予想工数: 0.5-1時間

#### Sub-Phase 4.3: OnBot Java - チュートリアル基礎 ✅ **完了**
##### チュートリアルメインファイル（2ファイル、499行）
- [x] `docs/source/programming_resources/onbot_java/OnBot-Java-Tutorial.rst` - **28行** OnBot Java チュートリアル
- [x] `docs/source/programming_resources/tutorial_specific/onbot_java/creating_op_modes/Creating-and-Running-an-Op-Mode-(OnBot-Java).rst` - **471行** Op Mode作成

##### 実績工数: 約2時間

#### Sub-Phase 4.4: OnBot Java - センサーと機能 ✅ **完了**
##### チュートリアル応用ファイル（3ファイル、185行）
- [x] `docs/source/programming_resources/tutorial_specific/onbot_java/using_sensors/Using-Sensors-(OnBot-Java).rst` - **67行** センサー利用
- [x] `docs/source/programming_resources/tutorial_specific/onbot_java/controlling_a_servo/Controlling-a-Servo-(OnBot-Java).rst` - **73行** サーボ制御
- [x] `docs/source/programming_resources/tutorial_specific/onbot_java/onbot_java_reference/OnBot-Java-Reference-Info.rst` - **45行** リファレンス情報

##### 実績工数: 約1時間

#### Sub-Phase 4.4b: OnBot Java - 構成とリファレンス
##### OnBot Javaメインディレクトリファイル（5ファイル、38行）
- [ ] `docs/source/programming_resources/onbot_java/config/config.rst` - **8行** 構成
- [ ] `docs/source/programming_resources/onbot_java/connecting/connecting.rst` - **8行** 接続
- [ ] `docs/source/programming_resources/onbot_java/intro/intro.rst` - **8行** イントロ
- [ ] `docs/source/programming_resources/onbot_java/opmode/opmode.rst` - **8行** Op Mode
- [ ] `docs/source/programming_resources/onbot_java/reference/reference.rst` - **6行** リファレンス

##### 予想工数: 0.5-1時間

#### Sub-Phase 4.5: Android Studio - セットアップと基礎 ✅ **完了**
##### チュートリアルメインファイル（3ファイル、853行）
- [x] `docs/source/programming_resources/android_studio_java/Android-Studio-Tutorial.rst` - **29行** Android Studio チュートリアル
- [x] `docs/source/programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.rst` - **401行** GitHub Fork & Clone
- [x] `docs/source/programming_resources/tutorial_specific/android_studio/creating_op_modes/Creating-and-Running-an-Op-Mode-(Android-Studio).rst` - **423行** Op Mode作成

##### 実績工数: 約2時間

#### Sub-Phase 4.6: Android Studio - センサーと機能 ✅ **完了**
##### チュートリアル応用ファイル（2ファイル、139行）
- [x] `docs/source/programming_resources/tutorial_specific/android_studio/using_sensors/Using-Sensors-(Android-Studio).rst` - **67行** センサー利用
- [x] `docs/source/programming_resources/tutorial_specific/android_studio/controlling_a_servo/Controlling-a-Servo-(Android-Studio).rst` - **72行** サーボ制御

##### 実績工数: 約1時間

#### Sub-Phase 4.6b: Android Studio - 追加チュートリアルとセットアップ
##### 追加のAndroid Studioチュートリアルファイル（4ファイル、307行）
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/disable_instant_run/disable-instant-run.rst` - **50行** Instant Run無効化
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/downloading_as_project_folder/Downloading-the-Android-Studio-Project-Folder.rst` - **144行** プロジェクトフォルダダウンロード
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/enabling_developer_options/Enabling-Developer-Options.rst` - **41行** 開発者オプション有効化
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/installing_android_studio/Installing-Android-Studio.rst` - **72行** Android Studioインストール

##### 予想工数: 3-4時間

#### Sub-Phase 4.6c: Android Studio - 構成とリファレンス
##### Android Studioメインディレクトリファイル（5ファイル、38行）
- [ ] `docs/source/programming_resources/android_studio_java/config/config.rst` - **9行** 構成
- [ ] `docs/source/programming_resources/android_studio_java/install/install.rst` - **7行** インストール
- [ ] `docs/source/programming_resources/android_studio_java/intro/intro.rst` - **9行** イントロ
- [ ] `docs/source/programming_resources/android_studio_java/manage/manage.rst` - **5行** 管理
- [ ] `docs/source/programming_resources/android_studio_java/opmode/opmode.rst` - **8行** Op Mode

##### 予想工数: 0.5-1時間

#### Sub-Phase 4.7: 共通リソース - デバイス管理 ✅ **完了**
##### デバイス管理ファイル（3ファイル、1046行）
- [x] `docs/source/programming_resources/shared/managing_control_hub/Managing-a-Control-Hub.rst` - **420行** Control Hub管理
- [x] `docs/source/programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller.rst` - **279行** スマートフォンRC管理
- [x] `docs/source/programming_resources/shared/configuring_android/Configuring-Your-Android-Devices.rst` - **347行** Android設定

##### 実績工数: 約2時間

#### Sub-Phase 4.7b: 共通リソース - 追加デバイス管理
##### 追加のデバイス管理ファイル（4ファイル、445行）
- [ ] `docs/source/programming_resources/shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station.rst` - **134行** スマートフォンDS管理
- [ ] `docs/source/programming_resources/shared/phone_pairing/phone-pairing.rst` - **102行** 電話ペアリング
- [ ] `docs/source/programming_resources/shared/required_materials/Required-Materials.rst` - **106行** 必要な材料
- [ ] `docs/source/programming_resources/shared/using_android_device/Using-Your-Android-Device.rst` - **103行** Androidデバイス使用

##### 予想工数: 4-5時間

#### Sub-Phase 4.8: SDK・ライブラリ・ラップトップ要件 **進行中**
##### SDK概要（1ファイル、104行）
- [x] `docs/source/ftc_sdk/overview/index.rst` - **104行** SDK概要

##### SDK更新（7ファイル、961行）
- [x] `docs/source/ftc_sdk/updating/index.rst` - **20行** 更新概要
- [x] `docs/source/ftc_sdk/updating/controlhub_os/Updating-the-Control-Hub-OS.rst` - **61行** Control Hub OS更新
- [x] `docs/source/ftc_sdk/updating/driverhub_os/Updating-the-Driver-Hub-OS.rst` - **66行** Driver Hub OS更新
- [x] `docs/source/ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client.rst` - **78行** REV Hardware Client更新
- [x] `docs/source/ftc_sdk/updating/hub_firmware/Updating-Hub-Firmware.rst` - **180行** Hubファームウェア更新
- [x] `docs/source/ftc_sdk/updating/ds_app/Updating-the-DS-App.rst` - **204行** Driver Stationアプリ更新
- [ ] `docs/source/ftc_sdk/updating/rc_app/Updating-the-RC-App.rst` - **352行** Robot Controllerアプリ更新

##### プログラミングリソース（2ファイル、850行）
- [ ] `docs/source/programming_resources/laptops/laptops.rst` - **377行** ラップトップ要件
- [ ] `docs/source/programming_resources/shared/external_libraries_blocks/external-libraries-blocks.rst` - **473行** 外部ライブラリ（Blocks）

##### 実績工数: 約4時間（予想: 8-10時間）
##### 進捗: 7ファイル完了（613行、35%）、残り3ファイル（1202行、65%）

#### Sub-Phase 4.9: 共通リソース - PID制御とその他
##### PID/PIDF制御（2ファイル、301行）
- [ ] `docs/source/programming_resources/shared/pid_coefficients/pid-coefficients.rst` - **146行** PID係数
- [ ] `docs/source/programming_resources/shared/pidf_coefficients/pidf-coefficients.rst` - **155行** PIDF係数

##### その他の共通リソース（6ファイル、553行）
- [ ] `docs/source/programming_resources/shared/auto_load_opmode/auto-load-opmode.rst` - **117行** Op Mode自動ロード
- [ ] `docs/source/programming_resources/shared/choosing_program_lang/choosing-program-lang.rst` - **75行** プログラミング言語選択
- [x] `docs/source/programming_resources/shared/control_system_intro/The-FTC-Control-System.rst` - **71行** FTC制御システム（Phase 3で完了）
- [ ] `docs/source/programming_resources/shared/installing_javascript_browser/Installing-a-Javascript-Enabled-Browser.rst` - **41行** JavaScriptブラウザインストール
- [ ] `docs/source/programming_resources/shared/installing_kotlin/Installing-Kotlin.rst` - **111行** Kotlinインストール
- [ ] `docs/source/programming_resources/shared/program_and_manage_network/Connecting-a-Laptop-to-the-Program-&-Manage-Network.rst` - **138行** ラップトップ接続

##### 予想工数: 7-9時間

#### Sub-Phase 4.10: MyBlocks（カスタムブロック）
##### MyBlocksチュートリアルとリファレンス（13ファイル、890行）
- [ ] `docs/source/programming_resources/shared/myblocks/annotation/annotation.rst` - **72行** アノテーション
- [ ] `docs/source/programming_resources/shared/myblocks/driving_example/driving-example.rst` - **36行** ドライブ例
- [ ] `docs/source/programming_resources/shared/myblocks/editing/editing.rst` - **51行** 編集
- [ ] `docs/source/programming_resources/shared/myblocks/hardware_example/hardware-example.rst` - **89行** ハードウェア例
- [ ] `docs/source/programming_resources/shared/myblocks/ideas/ideas.rst` - **52行** アイデア
- [ ] `docs/source/programming_resources/shared/myblocks/intro/intro.rst` - **50行** イントロ
- [ ] `docs/source/programming_resources/shared/myblocks/method_example/method-example.rst` - **59行** メソッド例
- [ ] `docs/source/programming_resources/shared/myblocks/parameter/parameter.rst` - **59行** パラメータ
- [ ] `docs/source/programming_resources/shared/myblocks/rw_example/rw-example.rst` - **74行** 読み書き例
- [ ] `docs/source/programming_resources/shared/myblocks/simple_example/simple-example.rst` - **175行** シンプル例
- [ ] `docs/source/programming_resources/shared/myblocks/summary/summary.rst` - **28行** サマリー
- [ ] `docs/source/programming_resources/shared/myblocks/telem_example/telem-example.rst` - **48行** テレメトリ例
- [ ] `docs/source/programming_resources/shared/myblocks/timer_example/timer-example.rst` - **97行** タイマー例

##### MyBlocksインデックス（1ファイル、26行）
- [ ] `docs/source/programming_resources/shared/myblocks/index.rst` - **26行** MyBlocksインデックス

##### 予想工数: 8-10時間

#### Sub-Phase 4.11: ビジョン処理 - カメラ制御
##### ビジョン概要とカメラ較正（2ファイル、181行）
- [ ] `docs/source/programming_resources/vision/camera_calibration/camera-calibration.rst` - **62行** カメラ較正
- [ ] `docs/source/programming_resources/vision/vision_overview/vision-overview.rst` - **119行** ビジョン概要

##### Webcam制御 - 概要とサンプル（4ファイル、263行）
- [ ] `docs/source/programming_resources/vision/webcam_controls/eval/eval.rst` - **131行** 評価
- [ ] `docs/source/programming_resources/vision/webcam_controls/index.rst` - **39行** インデックス
- [ ] `docs/source/programming_resources/vision/webcam_controls/overview/overview.rst` - **44行** 概要
- [ ] `docs/source/programming_resources/vision/webcam_controls/samples/samples.rst` - **49行** サンプル

##### Webcam制御 - 露出（5ファイル、137行）
- [ ] `docs/source/programming_resources/vision/webcam_controls/exposure/auto_exposure/auto-exposure.rst` - **41行** 自動露出
- [ ] `docs/source/programming_resources/vision/webcam_controls/exposure/control/control.rst` - **32行** 露出制御
- [ ] `docs/source/programming_resources/vision/webcam_controls/exposure/index.rst` - **10行** インデックス
- [ ] `docs/source/programming_resources/vision/webcam_controls/exposure/mode/mode.rst` - **27行** モード
- [ ] `docs/source/programming_resources/vision/webcam_controls/exposure/samples/samples.rst` - **27行** サンプル

##### Webcam制御 - フォーカス（3ファイル、66行）
- [ ] `docs/source/programming_resources/vision/webcam_controls/focus/control/control.rst` - **30行** フォーカス制御
- [ ] `docs/source/programming_resources/vision/webcam_controls/focus/index.rst` - **8行** インデックス
- [ ] `docs/source/programming_resources/vision/webcam_controls/focus/mode/mode.rst` - **28行** モード

##### Webcam制御 - ゲイン（5ファイル、163行）
- [ ] `docs/source/programming_resources/vision/webcam_controls/gain/control/control.rst` - **34行** ゲイン制御
- [ ] `docs/source/programming_resources/vision/webcam_controls/gain/ex1/ex1.rst` - **65行** 例1
- [ ] `docs/source/programming_resources/vision/webcam_controls/gain/ex2/ex2.rst` - **38行** 例2
- [ ] `docs/source/programming_resources/vision/webcam_controls/gain/ex3/ex3.rst` - **16行** 例3
- [ ] `docs/source/programming_resources/vision/webcam_controls/gain/index.rst` - **10行** インデックス

##### Webcam制御 - PTZ（パン・チルト・ズーム）（3ファイル、86行）
- [ ] `docs/source/programming_resources/vision/webcam_controls/ptz/index.rst` - **18行** インデックス
- [ ] `docs/source/programming_resources/vision/webcam_controls/ptz/pan_tilt/pan-tilt.rst` - **50行** パン・チルト
- [ ] `docs/source/programming_resources/vision/webcam_controls/ptz/zoom/zoom.rst` - **18行** ズーム

##### Webcam制御 - ホワイトバランス（3ファイル、69行）
- [ ] `docs/source/programming_resources/vision/webcam_controls/white_balance/control/control.rst` - **40行** ホワイトバランス制御
- [ ] `docs/source/programming_resources/vision/webcam_controls/white_balance/index.rst` - **8行** インデックス
- [ ] `docs/source/programming_resources/vision/webcam_controls/white_balance/mode/mode.rst` - **21行** モード

##### 予想工数: 8-10時間

#### Sub-Phase 4.12: IMU（慣性計測ユニット）
##### IMU詳細ドキュメント（1ファイル、1194行）
- [ ] `docs/source/programming_resources/imu/imu.rst` - **超大規模ファイル（1194行）**
  - **注意:** このファイルは1000行以上あるため、複数のセッションに分けて翻訳することを推奨

##### 予想工数: 10-15時間

#### Sub-Phase 4.13: プログラミングリソース - インデックス
##### メインインデックスファイル（1ファイル、139行）
- [ ] `docs/source/programming_resources/index.rst` - **139行** プログラミングリソースのメインインデックス

##### 予想工数: 1-2時間

#### Phase 4 合計
- **総ファイル数:** 102ファイル
- **完了:** 31ファイル（30.4%）
- **残り:** 71ファイル（69.6%）
- **実績工数:** 約16時間
- **残り予想工数:** 50-67時間
- **Phase 4 合計予想工数:** 66-83時間

---

### **Phase 5: AprilTag & カラー処理** (優先度: 中)
**目標:** AprilTagとカラー処理に関する技術ドキュメントを翻訳

> **⚠️ 翻訳時の注意:**
> - 一部のファイルは400行以上の大規模ファイルです（AprilTagライブラリ、カラーセンサー等）
> - 生成AIは大規模ファイルの翻訳中に、途中で翻訳が完了したと誤認する可能性があります
> - ファイルの最後まで翻訳されているか必ず確認してください
> 
> **📝 注記:** ビジョン処理（Webcam制御）とIMUは Phase 4.11 および 4.12 に移動しました

#### Sub-Phase 5.1: AprilTag 入門と概要（約3ファイル）✅ **完了**
- [x] `docs/source/apriltag/vision_portal/apriltag_intro/apriltag-intro.rst` - **大規模ファイル（417→341行）** AprilTag 入門
- [x] `docs/source/apriltag/vision_portal/visionportal_overview/visionportal-overview.rst` - **114→101行** VisionPortal 概要
- [x] `docs/source/apriltag/opmode_test_images/opmode-test-images.rst` - **129→99行** テスト画像
  - 注：ロードマップ記載の `apriltag-test-images.rst` は存在せず、実際には `opmode-test-images.rst` が該当

##### 実績工数: 約3時間（予想: 6-8時間）
##### 注記: Python スクリプトを使用した段階的翻訳により効率的に完了。全3ファイル（合計654→541行）を翻訳。

#### Sub-Phase 5.2: AprilTag ライブラリと検出（約5ファイル）
- [ ] `docs/source/apriltag/vision_portal/apriltag_library/apriltag-library.rst` - **大規模ファイル（約424行）** AprilTag ライブラリ
- [ ] `docs/source/apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values.rst` - 検出値の理解
- [ ] `docs/source/apriltag/apriltag_tips/apriltag-tips.rst` - AprilTag のヒント

##### 予想工数: 6-8時間

#### Sub-Phase 5.3: AprilTag 位置推定と最適化（約5ファイル）
- [ ] `docs/source/apriltag/vision_portal/apriltag_localization/apriltag-localization.rst` - **大規模ファイル（約410行）** AprilTag位置推定
- [ ] `docs/source/apriltag/vision_portal/visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth.rst` - **大規模ファイル（約461行）** CPU・帯域幅最適化
- [ ] `docs/source/apriltag/vision_portal/visionportal_multiportal/visionportal-multiportal.rst` - マルチポータル

##### 予想工数: 7-9時間

#### Sub-Phase 5.4: カラーセンサーと色空間（約4ファイル）
- [ ] `docs/source/color_processing/color-sensor/color-sensor.rst` - **大規模ファイル（約403行）** カラーセンサー
- [ ] `docs/source/color_processing/color-spaces/color-spaces.rst` - 色空間
- [ ] `docs/source/color_processing/color-blob-concepts/color-blob-concepts.rst` - Color Blob概念

##### 予想工数: 6-8時間

#### Sub-Phase 5.5: Color Locator シリーズ（約5ファイル）
- [ ] `docs/source/color_processing/color-locator-discover/color-locator-discover.rst` - **大規模ファイル（約341行）** Color Locator発見
- [ ] `docs/source/color_processing/color-locator-explore/color-locator-explore.rst` - **大規模ファイル（約505行）** Color Locator探索
- [ ] `docs/source/color_processing/color-locator-challenge/color-locator-challenge.rst` - **大規模ファイル（約565行）** Color Locatorチャレンジ

##### 予想工数: 8-10時間

#### Phase 5 合計予想工数: 27-35時間
#### Phase 5 注記
- ビジョンプログラミング（Webcam制御）は Phase 4.11 に移動
- IMU（慣性計測ユニット）は Phase 4.12 に移動
- これらはプログラミングリソースとしてPhase 4に含めることで、Phase 4の完全性を確保

---

### **Phase 6: 高度なリソースとリファレンス** (優先度: 中)
**目標:** CAD、製造、ゲーム固有のリソースなど、高度な内容を翻訳

> **⚠️ 翻訳時の注意:**
> - このフェーズには多様なトピックが含まれます
> - 生成AIは複数の小規模ファイルを連続で翻訳する際、途中で完了したと誤認する可能性があります
> - 各ディレクトリ内のファイルが全て翻訳されているか確認してください

#### Sub-Phase 6.1: ゲーム固有リソース - ブログと座標系（約8ファイル）
- [ ] `docs/source/game_specific_resources/blog/` - ブログ記事
- [ ] `docs/source/game_specific_resources/field_coordinate_system/` - フィールド座標系
  - コンセプト
  - 実装例
  - ドキュメント

##### 予想工数: 6-8時間

#### Sub-Phase 6.2: ゲーム固有リソース - Q&Aとフィールド（約8ファイル）
- [ ] `docs/source/game_specific_resources/ftc_qa/` - FTC Q&A
- [ ] `docs/source/game_specific_resources/playing_field_resources/` - フィールドリソース
  - フィールド設計
  - フィールドパーツ

##### 予想工数: 6-8時間

#### Sub-Phase 6.3: CADリソース - Autodesk（約6ファイル）
- [ ] `docs/source/cad_resources/autodesk/` - Autodesk関連
  - Fusion 360
  - Inventor
  - チュートリアル

##### 予想工数: 5-7時間

#### Sub-Phase 6.4: CADリソース - PTC と SolidWorks（約8ファイル）
- [ ] `docs/source/cad_resources/ptc/` - PTC関連
  - Creo
  - Onshape
- [ ] `docs/source/cad_resources/solidworks/` - SolidWorks関連
  - チュートリアル
  - ライブラリ

##### 予想工数: 6-8時間

#### Sub-Phase 6.5: 製造とファブリケーション（約6ファイル）
- [ ] `docs/source/manufacturing/3d_printing/` - 3D プリンティング
  - 基礎
  - 設計ガイドライン
  - トラブルシューティング

##### 予想工数: 5-7時間

#### Sub-Phase 6.6: AIとイノベーション（約10ファイル）
- [ ] `docs/source/ai/innovation_corner/` - イノベーションコーナー
  - AI概要
  - 機械学習
  - プロジェクト例
  - チュートリアル

##### 予想工数: 8-10時間

#### Phase 6 合計予想工数: 36-48時間

---

### **Phase 7: マニュアル、ブックレット、その他** (優先度: 低)
**目標:** 補助的な資料とリファレンスドキュメントを翻訳

> **⚠️ 翻訳時の注意:**
> - **tech-tips.rstは2053行の超大規模ファイルです**
> - 生成AIは必ず途中で翻訳が完了したと誤認します
> - 複数回に分けて翻訳を進め、毎回ファイルの最後まで到達しているか確認してください
> - セクション単位で翻訳を進めることを強く推奨します

#### Sub-Phase 7.1: Tech Tips - パート1（約500行）
- [ ] `docs/source/tech_tips/tech-tips.rst` - **超大規模ファイル（パート1/4: 行1～500目安）**
  - ファイルの冒頭から約500行まで翻訳
  - セクション区切りで分割を調整可（自然な区切りを優先）

##### 予想工数: 8-10時間

#### Sub-Phase 7.2: Tech Tips - パート2（約500行）
- [ ] `docs/source/tech_tips/tech-tips.rst` - **超大規模ファイル（パート2/4: 行501～1000目安）**
  - 約501行目から約1000行目まで翻訳
  - 前回の翻訳終了位置を正確に把握（セクション区切りで調整可）

##### 予想工数: 8-10時間

#### Sub-Phase 7.3: Tech Tips - パート3（約500行）
- [ ] `docs/source/tech_tips/tech-tips.rst` - **超大規模ファイル（パート3/4: 行1001～1500目安）**
  - 約1001行目から約1500行目まで翻訳（セクション区切りで調整可）
  - 翻訳の一貫性を保つため用語集を参照

##### 予想工数: 8-10時間

#### Sub-Phase 7.4: Tech Tips - パート4（残り約553行）
- [ ] `docs/source/tech_tips/tech-tips.rst` - **超大規模ファイル（パート4/4: 行1501～末尾）**
  - 約1501行目からファイル末尾（2053行）まで翻訳
  - 全体の翻訳が完了したか最終確認（必ず末尾まで到達すること）

##### 予想工数: 8-10時間

#### Sub-Phase 7.5: マニュアル（約10ファイル）
- [ ] `docs/source/manuals/` - 各種マニュアル
  - Robot Controller マニュアル
  - Driver Station マニュアル
  - システムマニュアル
  - トラブルシューティング

##### 予想工数: 8-10時間

#### Sub-Phase 7.6: ブックレットとスポンサー（約10ファイル）
- [ ] `docs/source/booklets/` - ブックレット
  - 各種ガイドブック
  - クイックスタート
- [ ] `docs/source/sponsors/` - スポンサー関連
  - Software
  - Discounts

##### 予想工数: 6-8時間

#### Sub-Phase 7.7: その他のページ（約5ファイル）
- [ ] `docs/source/assets/` - アセット関連
- [ ] `docs/source/404.rst` - 404ページ
- [ ] `docs/source/tos/` - Terms of Service
- [ ] その他の小規模ファイル

##### 予想工数: 3-5時間

#### Phase 7 合計予想工数: 49-63時間

---

## 📊 全体サマリー

### 統計情報
- **総ファイル数:** 255 RST ファイル
- **総予想工数:** 約204-255時間（全フェーズ合計）
  - 完了済み（Phase 1-3）: 約26時間
  - Phase 4: 66-83時間（31ファイル完了、71ファイル残り）
  - 残り（Phase 5-7）: 112-146時間
- **フェーズ数:** 7 メインフェーズ + 31 サブフェーズ（Phase 4を13サブフェーズに拡張、Phase 5を5サブフェーズに縮小）
- **完了フェーズ:** Phase 1-3（3フェーズ）+ Phase 4の8サブフェーズ部分完了 + Phase 5.1完了
- **残りフェーズ:** Phase 4の5サブフェーズ + Phase 5の4サブフェーズ + Phase 6-7（2フェーズ、13サブフェーズ）

### フェーズ別工数内訳
- **Phase 4:** 66-83時間（13サブフェーズ、102ファイル）
  - 完了: 31ファイル（30.4%）、実績16時間
  - 残り: 71ファイル（69.6%）、予想50-67時間
- **Phase 5:** 27-35時間（5サブフェーズ、ビジョン・IMUをPhase 4に移動）
- **Phase 6:** 36-48時間（6サブフェーズ）
- **Phase 7:** 49-63時間（7サブフェーズ）

### 進捗管理
各サブフェーズの完了時に以下を実施：
1. レビューと品質チェック
2. 用語集の更新
3. サブフェーズ完了の記録
4. 次サブフェーズへの移行判断

各メインフェーズの完了時に以下を追加実施：
1. フェーズ完了サマリーの作成
2. 全体的な品質チェック
3. 次フェーズへの移行判断

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
| 2025-12-09 | 2.0 | Phase 4-7を27サブフェーズに細分化、大規模ファイル対応の注意事項追加 |
| 2025-12-09 | 2.1 | Sub-Phase 4.1 完了 - Blocks チュートリアル基礎（2ファイル翻訳、1ファイル不存在を確認） |
| 2025-12-09 | 2.2 | Sub-Phase 4.2 完了 - Blocks センサーと機能（5ファイル翻訳、計857行） |
| 2025-12-09 | 2.3 | Sub-Phase 4.3 完了 - OnBot Java チュートリアル基礎（2ファイル翻訳、計680行） |
| 2025-12-10 | 2.4 | Sub-Phase 5.1 完了 - AprilTag 入門と概要（3ファイル翻訳、計541行） |
| 2025-12-09 | 2.4 | Sub-Phase 4.7 完了 - 共通リソース デバイス管理（3ファイル翻訳、計1342行） |
| 2025-12-09 | 2.4 | Sub-Phase 4.5 完了 - Android Studio セットアップと基礎（3ファイル翻訳、計1204行） |
| 2025-12-09 | 2.4 | Sub-Phase 4.6 完了 - Android Studio センサーと機能（2ファイル翻訳、計200行） |
| 2025-12-09 | 2.4 | Sub-Phase 4.4 完了 - OnBot Java センサーと機能（3ファイル翻訳、計259行） |
| 2025-12-10 | 3.0 | **Phase 4大幅拡張** - Phase 4を8サブフェーズから13サブフェーズに拡張。102ファイル全てをロードマップに追加（MyBlocks、ビジョン処理、IMU、追加構成ファイル等、72の未記載ファイルを追加）。Phase 4の第一目標完遂に向けて完全な網羅性を確保。 |

---

## 📝 備考

### 翻訳時の注意点
1. **リンクの保持:** RST形式のリンクは翻訳時も正しく機能するよう注意
2. **画像とキャプション:** 画像のalt textも必要に応じて翻訳
3. **コードブロック:** コード内のコメントのみ翻訳、コード自体は変更しない
4. **ディレクティブ:** Sphinx/RSTディレクティブは変更しない

### 🚨 生成AIによる翻訳時の重要な注意事項
大規模ファイルの翻訳時、生成AIは以下の問題が発生する可能性があります：

#### 問題点
- **途中完了の誤認:** ファイルの途中で翻訳が完了したと誤認することがあります
- **400行以上のファイル:** 特に400行を超えるファイルで発生しやすい
- **1000行以上のファイル:** ほぼ確実に複数回に分けた翻訳が必要です

#### 対策
1. **翻訳前の確認:**
   - ファイルの総行数を確認する（`wc -l <ファイル名>`）
   - 大規模ファイルは複数セッションに分けることを計画する

2. **翻訳中の確認:**
   - 定期的にファイル末尾まで到達しているか確認する
   - セクション見出しを目印に進捗を把握する

3. **翻訳後の確認:**
   - 元ファイルの最終行と翻訳後ファイルの最終行を比較する
   - 翻訳が途中で終わっている場合、残りの部分を続けて翻訳する
   - diff ツールで翻訳前後の構造が一致しているか確認する

4. **特に注意が必要なファイル:**
   - `tech-tips.rst`: 2053行（Phase 7で4分割推奨）
   - `imu.rst`: 1194行（Phase 5で複数セッション推奨）
   - 各種チュートリアルファイル: 400-646行

### 協力について
このロードマップに基づいて作業する際は、TRANSLATION_GUIDE.md の「3.2 コミットとプルリクエスト」に従ってください。
