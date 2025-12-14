VisionPortal 概要
=====================

**FIRST Tech Challenge** は**VisionPortal** を導入しました。これは、ビジョン処理のための包括的な新しいインターフェースです。

-  **FTC Blocks と Java** チームの場合、VisionPortal は**AprilTag** と**EasyOpenCV** の主要な機能に加えて、**TensorFlow Object Detection (TFOD)** を同時に提供します！

   .. figure:: images/020-dual-detection.png
      :width: 75%
      :align: center
      :alt: Dual Detection

      AprilTag と TensorFlow の両方を使用したデュアルプレビュー

   |

-  **AprilTag** 検出には、ID コードと** ポーズ**: カメラに対するタグの位置と方向が含まれます。

-  ウェブカメラの AprilTag と TFOD のパフォーマンスを向上させることができる **Camera Controls** が、**FTC Blocks** ユーザーに完全に利用可能になりました。

-  **複数のカメラ** を同時に操作できます – フォンカメラおよび/またはウェブカメラ。

   .. figure:: images/030-CH-preview-2-webcams.png
      :width: 75%
      :align: center
      :alt: Dual Camera

      複数カメラビュー

   |

-  **サンプル OpModes** と新しいツールが、**Builder パターン** を含むこれらの機能の操作とカスタマイズに利用できます。

-  重いビデオ処理の場合、**CPU リソース** と**USB 帯域幅** を管理するための多くのオプションが利用可能です。

-  DS と RC のプレビューは **大きく** できます！

   .. figure:: images/100-DH-DS-CS-BIG-TFOD.png
      :width: 75%
      :align: center
      :alt: Full Screen

      フルスクリーンプレビュー

VisionPortal 以降には、他にも多くの新機能と改善された機能が `あなたの発見を待っています
<https://github.com/FIRST-Tech-Challenge/FtcRobotController#release-information>`__。

----

2023-2024 CENTERSTAGE シーズンの準備として、新しい Software Development Kit (SDK) **VisionPortal** には**AprilTag 技術の組み込みサポート** が含まれています。以前は、チームは外部ライブラリをダウンロードして組み込む必要があり、プログラミング作業が複雑になっていました。

AprilTag は、**位置と方向** を推定するために使用される、シンプルな白黒タグを検出するための人気のあるビジョン技術です。2022-2023 POWERPLAY ゲームでは、多くのチームが Signal Sleeve 認識のための AprilTag の信頼性の高い Autonomous パフォーマンスを楽しみました。

   .. figure:: images/005-AprilTag-Worlds.png
      :width: 75%
      :align: center
      :alt: Dual Detection

      Photo Credit: Mike Silversides

**このガイドのすべてのセクションは、** :doc:`AprilTag 入門 <../apriltag_intro/apriltag-intro>` **を事前に読んでいることを前提としています。**
   
SDK はデフォルトで、**カメラに対する** AprilTag ポーズを記述します。この計算プロセスは**ポーズ推定** と呼ばれ、これは**カメラキャリブレーション** を含む多くの要因に基づく推定値のみであることを強調する用語です。目標を達成するために AprilTag の最適な使用法を決定する必要があります。

   :doc:`AprilTag 入門 <../apriltag_intro/apriltag-intro>`
   :doc:`ビジョンプロセッサの初期化 <../vision_processor_init/vision-processor-init>`
   **VisionPortal** の初期化 <../visionportal_init/visionportal-init>
   **VisionPortal** プレビュー <../visionportal_previews/visionportal-previews>
   **AprilTag ID** コード <../apriltag_id_code/apriltag-id-code>
   **AprilTag** メタデータ <../apriltag_metadata/apriltag-metadata>
   **AprilTag** 参照フレーム <../apriltag_reference_frame/apriltag-reference-frame>
   **AprilTag** カメラキャリブレーション <../apriltag_camera_calibration/apriltag-camera-calibration>
   **AprilTag** ポーズ <../apriltag_pose/apriltag-pose>
   **AprilTag** ライブラリ <../apriltag_library/apriltag-library>
   **VisionPortal** の CPU と帯域幅 <../visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth>
   **VisionPortal** カメラコントロール <../visionportal_camera_controls/visionportal-camera-controls>
   ビジョンマルチポータル <../vision_multiportal/vision-multiportal>
   **AprilTag** 高度な使用法 <../apriltag_advanced_use/apriltag-advanced-use>

====

謝辞 

- EasyOpenCV developer `@Windwoes <https://github.com/Windwoes>`__ 
- FTC Blocks developer `@lizlooney <https://github.com/lizlooney>`__ 
- *FIRST* Tech Challenge navigation expert `@gearsincorg <https://github.com/gearsincorg>`__ 
- and the smart people at `UMich/AprilTag <https://april.eecs.umich.edu/software/apriltag>`__.

質問、コメント、訂正は westsiderobotics@verizon.net までお寄せください。


