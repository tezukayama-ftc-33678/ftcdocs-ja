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
**目標:** 3つの主要プログラミング環境（Blocks、OnBot Java、Android Studio）の基本チュートリアルを翻訳

> **⚠️ 翻訳時の注意:**
> - 一部のファイルは500行以上の大規模ファイルです（例: Creating-and-Running-an-Op-Mode 系のファイル）
> - 生成AIは大規模ファイルの翻訳中に、途中で翻訳が完了したと誤認する可能性があります
> - ファイルの最後まで翻訳されているか必ず確認してください
> - 翻訳が途中で終わっている場合は、残りの部分を続けて翻訳してください

#### Sub-Phase 4.1: Blocks プログラミング - チュートリアル基礎（約8ファイル）✅ **完了**
- [x] `docs/source/programming_resources/blocks/Blocks-Tutorial.rst` - Blocks チュートリアル
- [x] `docs/source/programming_resources/tutorial_specific/blocks/creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks.rst` - **大規模ファイル（約511行）** Op Mode作成
- [ ] ⚠️ `docs/source/programming_resources/tutorial_specific/blocks/writing_an_op_mode_controller/writing_an_op_mode_controller.rst` - **ファイルが存在しません**（リポジトリに該当ファイルなし）

##### 実績工数: 約2時間（予想: 8-10時間）
##### 注記: 3番目のファイルはリポジトリに存在しませんでした。該当する類似ファイルとして `controlling_a_servo` や `using_sensors` が存在しますが、これらは Phase 4.2 に含まれる可能性があります。

#### Sub-Phase 4.2: Blocks プログラミング - センサーと機能（約5ファイル）✅ **完了**
- [x] `docs/source/programming_resources/tutorial_specific/blocks/using_sensors/Using-Sensors-(Blocks).rst` - **226行** センサー利用
- [x] `docs/source/programming_resources/tutorial_specific/blocks/controlling_a_servo/Controlling-a-Servo-(Blocks).rst` - **311行** サーボ制御
- [x] `docs/source/programming_resources/tutorial_specific/blocks/managing_opmodes/managing-opmodes.rst` - **147行** Op Mode管理
- [x] `docs/source/programming_resources/tutorial_specific/blocks/running_op_modes/Running-Your-Op-Mode.rst` - **115行** Op Mode実行
- [x] `docs/source/programming_resources/tutorial_specific/blocks/blocks_reference/Blocks-Reference-Material.rst` - **58行** リファレンス資料
- [ ] ⚠️ `docs/source/programming_resources/tutorial_specific/blocks/telemetry/telemetry.rst` - **ファイルが存在しません**（リポジトリに該当ファイルなし）
- [ ] ⚠️ `docs/source/programming_resources/tutorial_specific/blocks/applying_pid_control/applying_pid_control.rst` - **ファイルが存在しません**（リポジトリに該当ファイルなし）

##### 実績工数: 約2時間（予想: 5-7時間）
##### 注記: ロードマップに記載されていたtelemetry.rstとapplying_pid_control.rstは存在しませんでした。代わりに、Blocksチュートリアルの実際のファイル5つを翻訳しました。

#### Sub-Phase 4.3: OnBot Java - チュートリアル基礎（約8ファイル）✅ **完了**
- [x] `docs/source/programming_resources/onbot_java/OnBot-Java-Tutorial.rst` - **34行** OnBot Java チュートリアル
- [x] `docs/source/programming_resources/tutorial_specific/onbot_java/creating_op_modes/Creating-and-Running-an-Op-Mode-(OnBot-Java).rst` - **大規模ファイル（646行）** Op Mode作成
- [ ] ⚠️ `docs/source/programming_resources/tutorial_specific/onbot_java/writing_an_op_mode_controller/writing_an_op_mode_controller.rst` - **ファイルが存在しません**（リポジトリに該当ファイルなし）

##### 実績工数: 約2時間（予想: 10-12時間）
##### 注記: 3番目のファイルはリポジトリに存在しませんでした。Phase 4.1 および 4.2 と同様のパターンです。

#### Sub-Phase 4.4: OnBot Java - センサーと機能（約5ファイル）✅ **完了**
- [x] `docs/source/programming_resources/tutorial_specific/onbot_java/using_sensors/Using-Sensors-(OnBot-Java).rst` - **95行** センサー利用
- [x] `docs/source/programming_resources/tutorial_specific/onbot_java/controlling_a_servo/Controlling-a-Servo-(OnBot-Java).rst` - **105行** サーボ制御
- [x] `docs/source/programming_resources/tutorial_specific/onbot_java/onbot_java_reference/OnBot-Java-Reference-Info.rst` - **59行** リファレンス情報
- [ ] ⚠️ `docs/source/programming_resources/tutorial_specific/onbot_java/telemetry/telemetry.rst` - **ファイルが存在しません**（リポジトリに該当ファイルなし）
- [ ] ⚠️ `docs/source/programming_resources/tutorial_specific/onbot_java/applying_pid_control/applying_pid_control.rst` - **ファイルが存在しません**（リポジトリに該当ファイルなし）

##### 実績工数: 約1時間（予想: 5-7時間）
##### 注記: ロードマップに記載されていたtelemetry.rstとapplying_pid_control.rstは存在しませんでした。Phase 4.2（Blocks）と同様のパターンです。代わりに、OnBot Javaチュートリアルの実際のファイル3つを翻訳しました。

#### Sub-Phase 4.5: Android Studio - セットアップと基礎（約8ファイル）
- [ ] `docs/source/programming_resources/android_studio_java/Android-Studio-Tutorial.rst` - Android Studio チュートリアル
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.rst` - **大規模ファイル（約603行）** GitHub Fork & Clone
- [ ] `docs/source/programming_resources/tutorial_specific/android_studio/creating_op_modes/Creating-and-Running-an-Op-Mode-(Android-Studio).rst` - **大規模ファイル（約566行）** Op Mode作成

##### 予想工数: 10-12時間

#### Sub-Phase 4.6: Android Studio - センサーと機能（約5ファイル）✅ **完了**
- [x] `docs/source/programming_resources/tutorial_specific/android_studio/using_sensors/Using-Sensors-(Android-Studio).rst` - **96行** センサー利用
- [x] `docs/source/programming_resources/tutorial_specific/android_studio/controlling_a_servo/Controlling-a-Servo-(Android-Studio).rst` - **104行** サーボ制御
- [ ] ⚠️ `docs/source/programming_resources/tutorial_specific/android_studio/telemetry/telemetry.rst` - **ファイルが存在しません**（リポジトリに該当ファイルなし）
- [ ] ⚠️ `docs/source/programming_resources/tutorial_specific/android_studio/applying_pid_control/applying_pid_control.rst` - **ファイルが存在しません**（リポジトリに該当ファイルなし）

##### 実績工数: 約1時間（予想: 5-7時間）
##### 注記: ロードマップに記載されていたtelemetry.rstとapplying_pid_control.rstは存在しませんでした（Phase 4.2および4.4と同様のパターン）。代わりに、Android Studioチュートリアルの実際のファイル2つを翻訳しました。

#### Sub-Phase 4.7: 共通リソース - デバイス管理（約8ファイル）
- [ ] `docs/source/programming_resources/shared/managing_control_hub/Managing-a-Control-Hub.rst` - **大規模ファイル（約525行）** Control Hub管理
- [ ] `docs/source/programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller.rst` - **大規模ファイル（約384行）** スマートフォンRC管理
- [ ] `docs/source/programming_resources/shared/configuring_android/Configuring-Your-Android-Devices.rst` - **大規模ファイル（約433行）** Android設定

##### 予想工数: 8-10時間

#### Sub-Phase 4.8: SDK・ライブラリ・ラップトップ要件（約8ファイル）
- [ ] `docs/source/programming_resources/laptops/laptops.rst` - **大規模ファイル（約377行）** ラップトップ要件
- [ ] `docs/source/programming_resources/shared/external_libraries_blocks/external-libraries-blocks.rst` - **大規模ファイル（約473行）** 外部ライブラリ
- [ ] `docs/source/ftc_sdk/overview/` - SDK 概要
- [ ] `docs/source/ftc_sdk/updating/` - SDK 更新

##### 予想工数: 8-10時間

#### Phase 4 合計予想工数: 59-75時間

---

### **Phase 5: AprilTag & ビジョン処理** (優先度: 中)
**目標:** 画像認識とAprilTagに関する技術ドキュメントを翻訳

> **⚠️ 翻訳時の注意:**
> - 一部のファイルは400行以上の大規模ファイルです（AprilTagライブラリ、カラーセンサー等）
> - 特にIMUファイルは1194行と非常に大規模です
> - 生成AIは大規模ファイルの翻訳中に、途中で翻訳が完了したと誤認する可能性があります
> - ファイルの最後まで翻訳されているか必ず確認してください

#### Sub-Phase 5.1: AprilTag 入門と概要（約5ファイル）
- [ ] `docs/source/apriltag/vision_portal/apriltag_intro/apriltag-intro.rst` - **大規模ファイル（約417行）** AprilTag 入門
- [ ] `docs/source/apriltag/vision_portal/visionportal_overview/visionportal-overview.rst` - VisionPortal 概要
- [ ] `docs/source/apriltag/vision_portal/apriltag_intro/apriltag-test-images.rst` - テスト画像

##### 予想工数: 6-8時間

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

#### Sub-Phase 5.6: ビジョンプログラミングとIMU（約6ファイル）
- [ ] `docs/source/programming_resources/vision/` - ビジョンプログラミング
- [ ] `docs/source/programming_resources/imu/imu.rst` - **超大規模ファイル（約1194行）** IMU（慣性計測ユニット）
  - **注意:** このファイルは1000行以上あるため、複数のセッションに分けて翻訳することを推奨

##### 予想工数: 10-15時間

#### Phase 5 合計予想工数: 43-58時間

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
- **総予想工数:** 約213-270時間（全フェーズ合計）
  - 完了済み（Phase 1-3）: 約26時間
  - 残り（Phase 4-7）: 187-244時間
- **フェーズ数:** 7 メインフェーズ + 27 サブフェーズ
- **完了フェーズ:** Phase 1-3（3フェーズ）
- **残りフェーズ:** Phase 4-7（4フェーズ、27サブフェーズ）

### フェーズ別工数内訳（残り）
- **Phase 4:** 59-75時間（8サブフェーズ）
- **Phase 5:** 43-58時間（6サブフェーズ）
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
| 2025-12-09 | 2.4 | Sub-Phase 4.6 完了 - Android Studio センサーと機能（2ファイル翻訳、計200行） |
| 2025-12-09 | 2.4 | Sub-Phase 4.4 完了 - OnBot Java センサーと機能（3ファイル翻訳、計259行） |

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
