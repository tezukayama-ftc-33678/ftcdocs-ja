VisionPortal 概要
=====================

**FIRST Tech Challenge** は **VisionPortal** を導入しました。これは、ビジョン処理のための包括的な新しいインターフェースです。

-  **FTC Blocks と Java** チームの場合、VisionPortal は **AprilTag** と **EasyOpenCV** の主要な機能に加えて、**TensorFlow Object Detection (TFOD)** を同時に提供します！

   .. figure:: images/020-dual-detection.png
      :width: 75%
      :align: center
      :alt: Dual Detection

      AprilTag と TensorFlow の両方を使用したデュアルプレビュー

   |

-  **AprilTag** 検出には、ID コードと **ポーズ**: カメラに対するタグの位置と方向が含まれます。

-  ウェブカメラの AprilTag と TFOD のパフォーマンスを向上させることができる **Camera Controls** が、**FTC Blocks** ユーザーに完全に利用可能になりました。

-  **複数のカメラ** を同時に操作できます – フォンカメラおよび/またはウェブカメラ。

   .. figure:: images/030-CH-preview-2-webcams.png
      :width: 75%
      :align: center
      :alt: Dual Camera

      複数カメラビュー

   |

-  **サンプル OpModes** と新しいツールが、**Builder パターン** を含むこれらの機能の操作とカスタマイズに利用できます。

-  重いビデオ処理の場合、**CPU リソース** と **USB 帯域幅** を管理するための多くのオプションが利用可能です。

-  DS と RC のプレビューは **大きく** できます！

   .. figure:: images/100-DH-DS-CS-BIG-TFOD.png
      :width: 75%
      :align: center
      :alt: Full Screen

      フルスクリーンプレビュー

VisionPortal 以降には、他にも多くの新機能と改善された機能が `あなたの発見を待っています
<https://github.com/FIRST-Tech-Challenge/FtcRobotController#release-information>`__。

----

2023-2024 CENTERSTAGE シーズンの準備として、新しい Software Development Kit (SDK) **VisionPortal** には **AprilTag 技術の組み込みサポート** が含まれています。以前は、チームは外部ライブラリをダウンロードして組み込む必要があり、プログラミング作業が複雑になっていました。

AprilTag is a popular vision technology for detecting a simple black-and-white
tag, used to estimate **position and orientation**. In the 2022-2023 POWERPLAY
game, many Teams enjoyed AprilTag’s reliable Autonomous performance for
Signal Sleeve recognition.

   .. figure:: images/005-AprilTag-Worlds.png
      :width: 75%
      :align: center
      :alt: Dual Detection

      Photo Credit: Mike Silversides

**このガイドのすべてのセクションは、** :doc:`AprilTag 入門 <../apriltag_intro/apriltag-intro>` **を事前に読んでいることを前提としています。**
   
The SDK describes AprilTag pose **relative to the camera**, by default.
This computing process is called **pose estimation**, a term that emphasizes
this is an estimate only, based on many factors including **camera
calibration**. You must determine AprilTag’s best use for reaching your 
goals.

.. toctree::
   :maxdepth: 1

   AprilTag Introduction <../apriltag_intro/apriltag-intro>
   Vision Processor Initialization <../vision_processor_init/vision-processor-init>
   VisionPortal Initialization <../visionportal_init/visionportal-init>
   VisionPortal Previews <../visionportal_previews/visionportal-previews>
   AprilTag ID Codes <../apriltag_id_code/apriltag-id-code>
   AprilTag Metadata <../apriltag_metadata/apriltag-metadata>
   AprilTag Reference Frame <../apriltag_reference_frame/apriltag-reference-frame>
   AprilTag Camera Calibration <../apriltag_camera_calibration/apriltag-camera-calibration>
   AprilTag Pose <../apriltag_pose/apriltag-pose>
   AprilTag Library <../apriltag_library/apriltag-library>
   VisionPortal CPU and Bandwidth <../visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth>
   VisionPortal Camera Controls <../visionportal_camera_controls/visionportal-camera-controls>
   Vision Multiportal <../vision_multiportal/vision-multiportal>
   AprilTag Advanced Use <../apriltag_advanced_use/apriltag-advanced-use>

====

Much credit to 

- EasyOpenCV developer `@Windwoes <https://github.com/Windwoes>`__ 
- FTC Blocks developer `@lizlooney <https://github.com/lizlooney>`__ 
- *FIRST* Tech Challenge navigation expert `@gearsincorg <https://github.com/gearsincorg>`__ 
- and the smart people at `UMich/AprilTag <https://april.eecs.umich.edu/software/apriltag>`__.

Questions, comments and corrections to westsiderobotics@verizon.net


