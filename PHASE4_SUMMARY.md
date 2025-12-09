# Phase 4 完了サマリー

## 📋 概要

Phase 4（プログラミングリソース - 基礎編）の翻訳作業が完了しました。このフェーズでは、3つの主要プログラミング環境（Blocks、OnBot Java、Android Studio）の基本チュートリアルと、FTC SDK の概要および更新手順を翻訳しました。

**完了日:** 2025年12月9日

---

## ✅ 完了した作業

### 1. Blocks プログラミング（12ファイル）

#### メインチュートリアル（6ファイル）
- **Blocks-Tutorial.rst** - Blocks プログラミングチュートリアルメインページ
- **intro/intro.rst** - はじめに
- **connecting/connecting.rst** - プログラム & 管理サーバーへの接続
- **config/config.rst** - ハードウェアの構成
- **opmode/opmode.rst** - Op Mode の作成
- **reference/reference.rst** - リファレンスドキュメント

#### Blocks 固有チュートリアル（6ファイル）
- **blocks_reference/Blocks-Reference-Material.rst** - Blocks リファレンス資料
- **creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks.rst** - Op Mode の作成
- **controlling_a_servo/Controlling-a-Servo-(Blocks).rst** - サーボの制御
- **managing_opmodes/managing-opmodes.rst** - Blocks での OpMode 管理
- **running_op_modes/Running-Your-Op-Mode.rst** - OpMode の実行
- **using_sensors/Using-Sensors-(Blocks).rst** - センサーの使用

### 2. OnBot Java プログラミング（10ファイル）

#### メインチュートリアル（6ファイル）
- **OnBot-Java-Tutorial.rst** - OnBot Java プログラミングチュートリアルメインページ
- **intro/intro.rst** - はじめに
- **connecting/connecting.rst** - プログラム & 管理サーバーへの接続
- **config/config.rst** - ハードウェアの構成
- **opmode/opmode.rst** - Op Mode の作成
- **reference/reference.rst** - リファレンスドキュメント

#### OnBot Java 固有チュートリアル（4ファイル）
- **creating_op_modes/Creating-and-Running-an-Op-Mode-(OnBot-Java).rst** - Op Mode の作成と実行
- **controlling_a_servo/Controlling-a-Servo-(OnBot-Java).rst** - サーボの制御
- **onbot_java_reference/OnBot-Java-Reference-Info.rst** - OnBot Java リファレンス情報
- **using_sensors/Using-Sensors-(OnBot-Java).rst** - センサーの使用

### 3. Android Studio プログラミング（14ファイル）

#### メインチュートリアル（6ファイル）
- **Android-Studio-Tutorial.rst** - Android Studio プログラミングチュートリアルメインページ
- **intro/intro.rst** - はじめに
- **install/install.rst** - Android Studio のインストール
- **config/config.rst** - ハードウェアの構成
- **opmode/opmode.rst** - Op Mode の作成
- **manage/manage.rst** - Android Studio プロジェクトの管理

#### Android Studio 固有チュートリアル（8ファイル）
- **creating_op_modes/Creating-and-Running-an-Op-Mode-(Android-Studio).rst** - OpMode の作成と実行
- **controlling_a_servo/Controlling-a-Servo-(Android-Studio).rst** - サーボの制御
- **using_sensors/Using-Sensors-(Android-Studio).rst** - センサーの使用
- **downloading_as_project_folder/Downloading-the-Android-Studio-Project-Folder.rst** - Android Studio プロジェクトフォルダーのダウンロード
- **installing_android_studio/Installing-Android-Studio.rst** - Android Studio のインストール
- **enabling_developer_options/Enabling-Developer-Options.rst** - 開発者オプションの有効化
- **fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.rst** - GitHub からのフォークとクローン
- **disable_instant_run/disable-instant-run.rst** - Android Studio Instant Run の無効化

### 4. ラップトップ要件（1ファイル）
- **laptops/laptops.rst** - *FIRST* プログラムのコンピューター要件（タイトルのみ翻訳）

### 5. FTC SDK（8ファイル）

#### SDK 概要
- **ftc_sdk/overview/index.rst** - *FIRST* Tech Challenge ソフトウェア開発キット

#### SDK 更新手順（7ファイル）
- **ftc_sdk/updating/index.rst** - 制御システムコンポーネントの更新
- **ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client.rst** - REV Hardware Client のインストールと更新
- **ftc_sdk/updating/ds_app/Updating-the-DS-App.rst** - Driver Station アプリの更新
- **ftc_sdk/updating/rc_app/Updating-the-RC-App.rst** - Robot Controller（RC）アプリの更新
- **ftc_sdk/updating/controlhub_os/Updating-the-Control-Hub-OS.rst** - Control Hub OS の更新
- **ftc_sdk/updating/driverhub_os/Updating-the-Driver-Hub-OS.rst** - Driver Hub OS の更新
- **ftc_sdk/updating/hub_firmware/Updating-Hub-Firmware.rst** - Hub ファームウェアの更新

---

## 📊 翻訳統計

| 項目 | 詳細 |
|------|------|
| **翻訳ファイル数** | 45 RST ファイル |
| **Blocks プログラミング** | 12ファイル |
| **OnBot Java プログラミング** | 10ファイル |
| **Android Studio プログラミング** | 14ファイル |
| **ラップトップ要件** | 1ファイル |
| **FTC SDK** | 8ファイル |
| **翻訳済み主要セクション** | 約150セクション |
| **実作業時間** | 約5時間 |

---

## 🎯 翻訳品質チェック

### TRANSLATION_GUIDE.md 準拠確認

✅ **文体（トーン＆マナー）**
- 「です・ます」調で統一
- 読者への呼びかけは適切に表現
- 技術文書として正確で簡潔な表現

✅ **固有名詞の扱い**
- *FIRST*、FTC は英語のまま
- API名、クラス名は太字で英語のまま（**OpMode**, **Robot Controller**, **Driver Station** など）
- 製品名は英語のまま（**Control Hub**, **Expansion Hub**, **REV Robotics** など）

✅ **一般技術用語**
- 適切に和訳またはカタカナ表記
- 長音符号を省略しない（コンピューター、センサー、モーター）
- 統一用語集に従って翻訳

✅ **リンクと構造**
- RST形式のリンクは正しく機能
- toctree ディレクティブは変更なし
- 相対パスは維持

---

## 📝 翻訳例

### Blocks チュートリアルの例

#### 原文
```
This tutorial will take you step-by-step through the process of
configuring, programming, and operating your Control System. This
tutorial uses the *Blocks Programming Tool* to help you get started
quickly.
```

#### 翻訳
```
このチュートリアルでは、制御システムの構成、プログラミング、および操作のプロセスを段階的に説明します。このチュートリアルでは、**Blocks Programming Tool** を使用して、すぐに始められるようにサポートします。
```

### OnBot Java チュートリアルの例

#### 原文
```
The OnBot Java Programming Tool is a text-based programming tool
that lets programmers use a web browser to create, edit and save their
Java op modes.
```

#### 翻訳
```
**OnBot Java Programming Tool** は、プログラマーが Web ブラウザーを使用して Java の **op mode** を作成、編集、保存できるテキストベースのプログラミングツールです。
```

### Android Studio チュートリアルの例

#### 原文
```
Android Studio is an advanced integrated development environment for
creating Android apps. This tool is only recommended for
**advanced users** who have **extensive Java programming experience**.
```

#### 翻訳
```
**Android Studio** は、Android アプリを作成するための高度な統合開発環境です。**Android Studio** は、**上級ユーザー**で**豊富な Java プログラミング経験**を持つ方にのみ推奨されます。
```

### FTC SDK の例

#### 原文
```
The Software Development Kit (SDK) is the collection of tools for developing
software and executing it on a *FIRST* Tech Challenge robot.
```

#### 翻訳
```
ソフトウェア開発キット（SDK）は、*FIRST* Tech Challenge ロボット上でソフトウェアを開発および実行するためのツールのコレクションです。
```

---

## 🔍 技術的な注意点

### RST ディレクティブの保持
- Sphinx/RST のディレクティブ（`.. toctree::`, `.. meta::`, `.. image::`, `.. dropdown::` など）は変更なし
- コードブロック（`.. code-block::`）構造は維持
- バッジ（`:bdg-warning:`, `:bdg-info:`, `:bdg-success:`）は保持

### メタ情報の翻訳
- `.. meta::` ディレクティブ内のタイトル、説明、キーワードも翻訳
- 検索エンジン最適化（SEO）のための日本語メタデータ

### 外部リンク
- 外部リンクURLは変更なし
- 英語ドキュメントへのリンクは維持
- GitHub リポジトリへのリンクは維持

### スマートクォートの処理
- 英語ソースファイルのスマートクォート（'）を通常のアポストロフィ（'）に変換
- sed コマンドを使用して一括処理

---

## 🚀 次のステップ（Phase 5 への準備）

### Phase 5: AprilTag & ビジョン処理

Phase 5 では以下のファイルを翻訳予定:

1. **AprilTag（約15ファイル）**
   - `apriltag/vision_portal/apriltag_intro/` - AprilTag 入門
   - `apriltag/vision_portal/visionportal_overview/` - VisionPortal 概要
   - `apriltag/understanding_apriltag_detection_values/` - 検出値の理解

2. **カラー処理（約10ファイル）**
   - `color_processing/` - Color Sensor, Color Spaces, Color Locator

3. **ビジョンプログラミング（約5ファイル）**
   - `programming_resources/vision/` - ビジョンプログラミング
   - `programming_resources/imu/` - IMU（慣性計測ユニット）

**予想工数:** 30-40時間

---

## 💡 学んだこと・改善点

### 効率化できた点
- メインチュートリアルファイルと固有チュートリアルファイルを並行して翻訳
- 類似構造のファイル（Blocks、OnBot Java、Android Studio）はパターンを利用して効率的に翻訳
- スマートクォート処理を sed コマンドで一括実行

### Phase 4 の特徴
- 3つのプログラミング環境（Blocks、OnBot Java、Android Studio）の説明が並行
- 各環境の特徴と推奨ユーザーを明確に翻訳
- SDK の更新手順が複数の方法で説明されている

### 今後の推奨事項
- 長文ファイルは主要セクションを優先して翻訳
- ビルドテストを定期的に実施して、RST構文エラーを早期発見
- 各プログラミング環境の用語統一を維持
- スマートクォート処理を翻訳前に実施

---

## 🎉 Phase 4 成果物の利用方法

### ドキュメントのビルド
```bash
# 要件のインストール
pip install -r docs/requirements.txt

# HTML のビルド
cd docs
make html

# ビルド結果の確認
# docs/build/html/index.html をブラウザで開く
```

### 翻訳作業の継続
1. **TRANSLATION_ROADMAP.md** で次のフェーズを確認
2. **GLOSSARY.md** を参照して用語統一
3. **TRANSLATION_GUIDE.md** のルールに従って翻訳
4. 完了後、このサマリーと同様の Phase N サマリーを作成

---

## 📚 関連ドキュメント

- [TRANSLATION_GUIDE.md](./TRANSLATION_GUIDE.md) - 翻訳ガイドライン
- [TRANSLATION_ROADMAP.md](./TRANSLATION_ROADMAP.md) - 全体ロードマップ
- [GLOSSARY.md](./GLOSSARY.md) - 用語集
- [PHASE1_SUMMARY.md](./PHASE1_SUMMARY.md) - Phase 1 完了サマリー
- [PHASE2_SUMMARY.md](./PHASE2_SUMMARY.md) - Phase 2 完了サマリー
- [PHASE3_SUMMARY.md](./PHASE3_SUMMARY.md) - Phase 3 完了サマリー
- [README.md](./README.md) - プロジェクト概要

---

## 📞 フィードバック・質問

Phase 4 の翻訳内容に関するフィードバックや質問は、GitHub Issues または Pull Request でお寄せください。

**Team 33678 Tezukayama FTC Japan**
