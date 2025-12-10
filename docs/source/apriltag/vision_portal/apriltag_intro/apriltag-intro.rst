AprilTag 入門
=====================

はじめに
------------

カメラベースの技術として人気があるのが **AprilTag** です。これは QR コードに似たスキャン画像です。カスタム Signal Sleeves での効果的な動作と迅速なセットアップにより、POWERPLAY（2022-2023）シーズンでは、特に Java でプログラミングを行う *FIRST* Tech Challenge チームに **広く採用** されました。

.. figure:: images/005-AprilTag-Worlds.png
   :width: 75%
   :align: center
   :alt: Dual Detection

   Photo Credit: Mike Silversides

FTC Blocks を使用するチームを含む POWERPLAY のチームは、いくつかのリソースの使い方を学びました： 

-  AprilTag: フォーマットされた画像を評価するためのオープンソース技術 
-  EasyOpenCV: *FIRST* Tech Challenge に最適化された OpenCV（画像処理ライブラリ）とのインターフェース 
-  myBlocks: OnBot Java (OBJ) で作成されたカスタム Blocks

現在、これら3つの領域は *FIRST* **Tech Challenge Software Development Kit (SDK) のバージョン 8.2 以降** に提供、またはバンドルされています。

つまり、**AprilTag** と **EasyOpenCV** の主要な機能は、特別なダウンロードなしで Robot Controller (RC) と Driver Station (DS) アプリで利用できます。また、AprilTag の機能は、カスタム myBlocks を必要とせずに **FTC Blocks** に含まれています。

AprilTag の機能は、ウェブカメラと Android RC フォンカメラの両方で動作します。
単一の OpMode で AprilTag と Color Processing を使用できます。

*FIRST* Tech Challenge において、AprilTag はスポットライトを浴びる準備が整いました！

AprilTag とは？
-----------------

`ミシガン大学 <https://april.eecs.umich.edu/software/apriltag>`__ で開発された AprilTag は、2D バーコードまたは簡略化された QR コードのようなものです。数値の **ID コード** を含み、**位置と方向** の特定に使用できます。

.. figure:: images/010-apriltagrobots.png
   :width: 75%
   :align: center
   :alt: AprilTag Robots

   ロボット上の AprilTags。Photo Credit: University of Michigan

AprilTag は **視覚的フィデューシャル（visual fiducial）** またはフィデューシャルマーカーの一種で、情報を含み、簡単に認識できるように設計されています。

.. figure:: images/020-Sample-Tags.png
   :width: 75%
   :align: center
   :alt: Tag Families

   異なる AprilTag ファミリーのサンプル

上記のサンプルは、異なるフォーマット、つまり **ファミリー** を表しています。プロジェクトでは通常、単一の AprilTag ファミリーを使用します。

*FIRST* Tech Challenge では、**36h11** と呼ばれる一般的なファミリーを使用します。36h11 ファミリーの 0 から 20 までの番号を示す PDF は、ここからダウンロードできます：

- :download:`AprilTag PDF 0-20 <files/AprilTag_0-20_family36h11.pdf>`

各番号は、そのタグの ID コードです。

Here’s an AprilTag representing **ID code 2**. The SDK software
recognizes and overlays the ID code onto the image (small blue rectangle
**ID 02**).

.. figure:: images/080-CH-LiveView-ID-code.png
   :width: 75%
   :align: center
   :alt: Tag02 Preview

   検出されたタグ ID 02 を表示するストリーム出力 

上記の画像は、Robot Controller デバイス（Control Hub または RC フォン）からのカメラプレビュー画像（LiveView と呼ばれる）を示しています。

AprilTag ファミリー 36h11 には、587 個の ID コードの容量があります。すべてを見るには、次のリンクをたどってください：

- https://github.com/rgov/apriltag-pdfs/tree/main/tag36h11/us_letter/100mm

正方形の AprilTag パターンには、より小さな黒と白の正方形が含まれており、それぞれが **ピクセル** と呼ばれます。36h11 タグには、10 x 10 ピクセルが含まれており、**すべて白いピクセル** の外側の境界線と、**すべて黒いピクセル** の内側の境界線が含まれます。

**タグサイズ** は、36h11 の黒いピクセルで構成される **内側の境界線** の外側のエッジを横切って測定されます。

.. figure:: images/100-Tag-size-42.png
   :width: 75%
   :align: center
   :alt: Tag Size

   タグサイズの測定を示す図

上記の画像は、外側の白い境界線を持つ完全な AprilTag を示しています。36h11 ファミリーから、その ID コードは 42 です。

AprilTag ポーズ
-------------

Beyond ID code, the new SDK also provides **pose** data, namely position
and orientation (rotation) from the **camera’s point of view**.  This requires
a **flat AprilTag**, which was not possible with curved POWERPLAY Signal
Sleeves.

Let’s look again at the camera preview image, called LiveView, from a Robot
Controller device (Control Hub or RC phone).

.. figure:: images/200-CH-LiveView-offsets-crop.png
   :width: 75%
   :align: center
   :alt: LiveView Image

   説明のための追加マーキングを含む LiveView 画像

Imagine a laser beam pointing straight outward from the center of the camera
lens. Its 3-dimensional path appears (to the camera) as a single point,
indicated by the **green star**. You can see that the center of the AprilTag
(**yellow star**) is offset from that “laser beam”.

その **並進オフセット** は、互いに 90 度の角度にある軸に沿った 3 つの伝統的なコンポーネント（X、Y、Z 距離）に分解できます：

-  X 距離（水平のオレンジ色の線）は中心から右方向です
-  Y 距離（表示されていません）はレンズの中心から外側です
-  Z 距離（垂直のオレンジ色の線）は中心から上方向です

SDK は、これらの距離を画面上のピクセル数を報告するだけでなく、**実世界で** 提供します。非常に便利です！

You can also see that the AprilTag’s flat face is not parallel to the plane of
the camera. That **rotation offset** can break down into three angles about the
X, Y and Z axes. This is discussed further in the section below, called
**AprilTag Axes**.

In summary, the SDK evaluates the AprilTag image and performs **“pose
estimation”**, providing an estimated X, Y and Z **distance** between the tag
and the camera, along with an estimated **angle** of rotation around those
axes. A closer or larger AprilTag can yield a more accurate estimate of pose.

良好なポーズ推定を提供するために、各 RC フォンカメラまたはウェブカメラには、特定の解像度に対する **キャリブレーションデータ** が必要です。SDK には、限られた数のウェブカメラと解像度のためのそのようなデータが含まれています。チームは、提供された手順を使用して、**レンズ固有パラメーター** と呼ばれる独自のデータを生成できます。

ナビゲーション
----------

OpMode はナビゲーションを実現するために AprilTag ポーズを使用します：入力を評価し、目的地まで走行します。

OpMode はポーズデータを使用して、タグに向かって走行するか、タグに **対する** ターゲット位置と方向まで走行できます。（新しい SDK は Java **サンプル OpMode** ``RobotAutoDriveToAprilTagOmni.java`` と ``RobotAutoDriveToAprilTagTank.java`` を提供します。）もう1つのナビゲーションの可能性については、以下の **高度な使用法** で言及されています。

Navigation is best done with **continuous** pose estimates, if the AprilTag
remains within the camera’s field of view. Namely, an OpMode “**while() loop**”
should regularly read the updated pose data, to guide the robot’s driving
actions.

SDK は **複数のカメラ** をサポートしており、切り替え可能または同時使用が可能です。これは、ロボットが方向を変更する場合、または別の AprilTag（または Color Processing）を使用してナビゲートしたい場合に役立ちます。

ナビゲーションには、駆動モーターエンコーダー、REV Hub IMU、デッドホイールエンコーダー、カラー/距離センサー、超音波センサーなど、他のセンサーも使用できます。

It’s also possible to evaluate **non-AprilTag images** from the same camera
and/or a second camera. For example, the SDK can estimate the horizontal angle
(or Bearing) of an object detected with **Color Processing**, another vision
technology employed in *FIRST* Tech Challenge. Advanced teams might consider
active camera pointing control, to keep an AprilTag or other object in view.

アノテーション
-----------

プレビュー（RC フォン画面または DS Camera Stream）では、公式に認識された AprilTag は **色付きの境界線** とその数値 **ID コード** を表示します。これらの **アノテーション** により、認識を視覚的に簡単に確認できます：

.. figure:: images/280-DS-preview.png
   :width: 75%
   :align: center
   :alt: Simple Annotations

   異なるメタデータを持つ2つの AprilTags が検出され、アノテーションが表示されている

上記の :ref:`DS Camera Stream <hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam:image preview>` プレビューでは、左側の AprilTag はタグ **ライブラリ**（デフォルトまたはカスタマイズ）から認識されました。ライブラリタグには、タグサイズを含む事前にロードされた情報（**メタデータ** と呼ばれる）があり、**ポーズ推定** を可能にします。これらはデフォルトで **色付きの境界線** でアノテーションされます。

右側の AprilTag はタグライブラリにありませんでした。メタデータがないため、SDK は数値 **ID コード** のみを提供でき、ここでは **ID 03** として表示されています。このようなタグは、デフォルトでは色付きの境界線で **アノテーションされません**。

Note: **Camera Stream** displays a snapshot of the camera’s view, on the Driver
Station device. It’s available only during the INIT phase of an OpMode, and
also shows any AprilTag (or Color Processing) annotations. Instructions are posted here:

- :ref:`Camera Stream Image Preview Documentation <hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam:image preview>`

オプションのアノテーションには、タグ中心の **色付き軸** と、タグ画像から投影される **色付きボックス** が含まれます：

.. figure:: images/300-RC-preview.png
   :width: 75%
   :align: center
   :alt: Optional Annotations

   追加のアノテーションが有効になっている LiveView

上記の画像は、Android Robot Controller (RC) フォン上のプレビュー（LiveView と呼ばれる）を示しています。REV Control Hub は RC プレビューを生成しますが、HDMI 外部モニターまたは ``scrcpy`` で見ることができます。``scrcpy`` はここで見つけることができます：

- https://github.com/Genymobile/scrcpy

AprilTag 軸
-------------

SDK は、基礎となるポーズデータを次のように提供します： 

-  位置は、**カメラレンズから AprilTag** への X、Y、Z 距離に基づいています。 
-  方向は、右手の法則を使用して、これらの軸を中心とした回転に基づいています。

Note: the optional red-green-blue annotated axes represent the **tag’s
frame of reference**, unrelated to SDK pose data. That annotation
indicates only a successful AprilTag recognition.

新しい SDK での軸の指定は次のとおりです： 

- Y 軸はカメラレンズの中心から **まっすぐ外側** を指します 
- X 軸は Y 軸に垂直に **右方向** を指します 
- Z 軸は Y と X に垂直に **上方向** を指します

カメラがロボット上で直立して前方を向いている場合、これらの軸は次のために使用されるロボット座標系と一致しています 
:ref:`IMU navigation <programming_resources/imu/imu:axes definition>`.

注：これらの軸は、カメラの参照フレームからでも、公式 AprilTag
`definitions <https://github.com/AprilRobotics/apriltag/wiki/AprilTag-User-Guide#coordinate-system>`__,
even from the camera’s frame of reference.

SDK は AprilTag **回転** データを次のように提供します： 

- **ピッチ** は X 軸を中心とした回転の測定値です 
- **ロール** は Y 軸を中心とした回転の測定値です 
- ヘディング、または **ヨー** は、Z 軸を中心とした回転の測定値です

回転は、伝統的な右手の法則に従います：親指が正の軸に沿って指している状態で、指は正の回転の方向に巻き付きます。

さらなる議論はここで提供されています：

:ref:`Understanding AprilTag Detection Values <apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values:understanding apriltag detection values>`

注：この記事では、*FIRST* Tech Challenge 
:ref:`Field Coordinate System <game_specific_resources/field_coordinate_system/field-coordinate-system:scope>`.

OpMode は、ナビゲーションのためにロボットの方向を全体のフィールドまたは 
:download:`‘global coordinates’ <files/FTC-Global-Coordinates.png>`
for navigation, but that’s beyond this AprilTag introduction.

高度な使用法
------------

**オプション 1**

If a tag’s position and orientation **on the game field** are
specified in advance, the tag’s pose data could be used by an advanced
OpMode to calculate the robot’s position on the field. This conversion
math, an exercise for the reader, can allow a robot to use the tag’s
pose data in real-time to navigate to the desired location on the field.

**オプション 2**

ビジョン処理は、重要な **CPU リソース** と USB 通信 **帯域幅** を消費する可能性があります。*FIRST* Tech Challenge チームは、CPU および帯域幅リソースの過負荷のリスクに対して、より高い解像度と速度（フレーム/秒）の利点のバランスをとることができます。SDK 8.2 以降は、このバランスを管理するための多数のツールを提供します： 

- カメラの解像度を選択 
- RC プレビュー（LiveView と呼ばれる）を無効化および有効化 
- AprilTag（または Color Processing）プロセッサを無効化および有効化 
- カメラストリームを閉じる 
- 圧縮されたビデオストリーミング形式を選択 
- フレーム/秒を測定 
- デシメーション（ダウンサンプリング）を設定 
- ポーズソルバーアルゴリズムを選択

**オプション 3**

より鮮明なカメラ画像は、AprilTag（および Color Processing）ビジョン処理を改善できます。SDK は、FTC Blocks でも利用可能な強力な **ウェブカメラコントロール**（露出、ゲイン、フォーカスなど）を提供します！これらのコントロールは、さまざまな照明条件下で適用できます。

露出とゲインは一緒に調整されます。SDK は Java サンプル OpMode ``ConceptAprilTagOptimizeExposure.java`` を提供します。

**オプション 4**

上記の **AprilTag 軸** で説明した参照フレームは、8.2 SDK 以降でデフォルトで計算および提供されます。高度なチームは、AprilTag/EasyOpenCV パイプラインからの **生の値** に基づいて、独自のポーズ計算を実行することを好むかもしれません。

これらの生の値は、Java と Blocks プログラマーが利用できます。Java バージョンはここに示されています：

.. code:: java

   for (AprilTagDetection detection : aprilTag.getDetections())  {

        Orientation rot = Orientation.getOrientation(detection.rawPose.R, AxesReference.INTRINSIC, AxesOrder.XYZ, AngleUnit.DEGREES);

        // Original source data
        double poseX = detection.rawPose.x;
        double poseY = detection.rawPose.y;
        double poseZ = detection.rawPose.z;

        double poseAX = rot.firstAngle;
        double poseAY = rot.secondAngle;
        double poseAZ = rot.thirdAngle;
        }

これらの生の値は、SDK によって次のようにデフォルトのインターフェースに変換されます：

.. code:: java

   if (detection.rawPose != null)   {
        detection.ftcPose = new AprilTagPoseFtc();

        detection.ftcPose.x =  detection.rawPose.x;
        detection.ftcPose.y =  detection.rawPose.z;
        detection.ftcPose.z = -detection.rawPose.y;

        Orientation rot = Orientation.getOrientation(detection.rawPose.R, AxesReference.INTRINSIC, AxesOrder.YXZ, outputUnitsAngle);
        detection.ftcPose.yaw = -rot.firstAngle;
        detection.ftcPose.roll = rot.thirdAngle;
        detection.ftcPose.pitch = rot.secondAngle;

        detection.ftcPose.range = Math.hypot(detection.ftcPose.x, detection.ftcPose.y);
        detection.ftcPose.bearing = outputUnitsAngle.fromUnit(AngleUnit.RADIANS, Math.atan2(-detection.ftcPose.x, detection.ftcPose.y));
        detection.ftcPose.elevation = outputUnitsAngle.fromUnit(AngleUnit.RADIANS, Math.atan2(detection.ftcPose.z, detection.ftcPose.y));
        }

再度、さらなる議論はここで提供されています：

:ref:`Understanding AprilTag Detection Values <apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values:understanding apriltag detection values>`

まとめ
-------

AprilTag は、QR コードに似たスキャン画像を使用する、人気のあるカメラベースの技術です。

SDK バージョン 8.2 以降には、AprilTag と EasyOpenCV の主要な機能が含まれています。EasyOpenCV は、画像処理のための OpenCV との *FIRST* Tech Challenge に最適化されたインターフェースです。これらの方法は、**Java と Blocks プログラマー** が便利に使用できるようにパッケージ化されています。

デフォルトでは、SDK は 36h11 ファミリーの任意の AprilTag の ID コードを検出できます。

For AprilTags in a default or custom tag Library, the interface
provides calculated **pose** estimates (position and rotation) from the
**camera’s frame of reference**. The source data is also available for
advanced teams.

AprilTag 機能は、Android RC フォンカメラとウェブカメラで動作します。各カメラは、良好なポーズ推定を提供するために、特定の解像度の **キャリブレーションデータ** を必要とします。

複数のカメラがサポートされており、単一の OpMode で AprilTag と Color Processing を使用できます。AprilTag 検出は、FTC Blocks でも利用可能なウェブカメラカメラコントロールで改善されます。

***FIRST* Tech Challenge において、AprilTag は CENTERSTAGE を飾る準備ができています！**

====

Much credit to:

- EasyOpenCV developer `@Windwoes <https://github.com/Windwoes>`__ 
- FTC Blocks developer `@lizlooney <https://github.com/lizlooney>`__ 
- FTC navigation expert `@gearsincorg <https://github.com/gearsincorg>`__ 
- and the smart people at `UMich/AprilTag <https://april.eecs.umich.edu/software/apriltag>`__.

Questions, comments and corrections to westsiderobotics@verizon.net

