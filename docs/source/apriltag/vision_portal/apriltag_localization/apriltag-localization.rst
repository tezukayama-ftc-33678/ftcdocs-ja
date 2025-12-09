AprilTag 位置推定
=====================

はじめに
------------

*FIRST Tech Challenge* (FTC)において、**位置推定**（localization）はセンサー入力を使用して、ロボットの現在位置を**ゲームフィールド上で**特定します。

2023年以降、FTC の **OpMode** は**カメラに対する相対的な** **AprilTag** の**姿勢**（位置と向き）を読み取ることができます。さらに **OpMode** は、メタデータとして保存されているその **AprilTag** の**グローバル**姿勢（FTCゲームフィールド上の位置）も読み取ることができます。

.. figure:: images/05-ITD-tags.png
   :align: center
   :width: 85%
   :alt: Field Locations of AprilTags in INTO THE DEEP

   INTO THE DEEPにおけるAprilTagsのフィールド配置

これは、カメラの**グローバル**姿勢、すなわちゲームフィールド上での位置と向きを計算できることを意味します。

さらに、カメラの姿勢がロボットの基準座標系で指定されている場合、**OpMode** は**ロボットのグローバル姿勢**（ゲームフィールド上）を決定できます。

.. figure:: images/06-Res-Q-field-axes.png   
   :align: center
   :width: 75%
   :alt: Field Coordinate System

   FTCフィールド座標系

この**位置推定**は、1つ以上の固定されたランドマーク（この場合は **AprilTag**）を検知することに基づいて、ロボットのグローバル位置と回転を決定する計算です。

この機能は、`Dryw Wade <https://github.com/sfe-SparkFro>`_ のおかげで、2024年にFTC SDKバージョン10.0でサンプル **OpMode** とともに提供されました。このチュートリアルでは、その **OpMode** の使用方法について説明します。

構成
-------------

*以下の場合はこのセクションをスキップしてください...*

* *アクティブなロボット構成にすでに「Webcam 1」が含まれている場合、または*
* *Android phoneの内蔵カメラを Robot Controller として使用している場合*

プログラミングを開始する前に、**REV Control Hub** ユーザーは **AprilTag** 位置推定に使用するUSBウェブカメラを含むロボット構成を作成する必要があります。

今のところ、デフォルトのウェブカメラ名「Webcam 1」を使用してください。別の名前を希望する場合は、ロボット構成内の正確なウェブカメラ名と一致するようにサンプル **OpMode** を編集してください。

その構成を**保存してアクティブ化**してください。ペアリングされた **Driver Station** 画面にその名前が表示されます。

サンプル OpMode を開く
----------------------

サンプル **OpMode** を開く方法については、以下の **Blocks** または Java セクションを選択してお読みください：

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      **Robot Controller** にWi-Fi経由で接続されたラップトップまたはデスクトップコンピューターで、Chromeブラウザを開きます。**REV Control Hub** のアドレス http://192.168.43.1:8080（Android RC phoneの場合は http://192.168.49.1:8080）にアクセスし、**Blocks** タブをクリックします。

      ``Create New OpMode`` をクリックし、「AprilTagLocalization_Darlene_v01」などの新しい名前を入力して、サンプル **OpMode** ``ConceptAprilTagLocalization`` を選択します。

      RC phoneの内蔵カメラを使用する場合は、**OpMode** の最初のブロック ``set USE_WEBCAM`` で ``true`` を ``false`` に変更してください。

      **OpMode** を保存したら、試してみましょう！

   .. tab-item:: Java
      :sync: java

      **OnBot Java** または **Android Studio** のいずれかを開きます。

      ``teamcode`` フォルダ内に、「AprilTagLocalization_Oscar_v01.java」などの名前で新しい **OpMode** を追加/作成し、サンプル **OpMode** ``ConceptAprilTagLocalization.java`` を選択します。

      RC phoneの内蔵カメラを使用する場合は、約71行目（\ ``USE_WEBCAM``\ ）で ``true`` を ``false`` に変更してください。

      「Build」をクリックしたら、試してみましょう！

サンプル OpMode を実行する
---------------------

**Driver Station** で、今保存またはビルドした **TeleOp** **OpMode** を選択します。

現在のFTCゲームの **AprilTag** にカメラを向けます。

.. figure:: images/07-full-tag-11.png
   :align: center
   :width: 85%
   :alt: Full AprilTag Image

   完全なAprilTag画像

実際の結果を得るには、1つ以上の正規の **AprilTag** が正しい位置に配置されたFTCゲームフィールドでテストを行う必要があります。

シミュレーション/カジュアルなテストの場合は、正しいサイズの紙の **AprilTag** を使用してください。または、**正しい物理サイズ**（この例では4 x 4インチ）に拡大した画像をコンピューター画面に表示することもできます：

.. figure:: images/08-tag-11.png
   :align: center
   :width: 85%
   :alt: Partial AprilTag Sheet

   部分的なAprilTagシート

**INITのみをタッチしてください。** テレメトリは表示されませんが、この時点でDSの **Camera Stream** プレビューにアクセスできます。プレビューについては次のセクションを参照してください。

プレビューを使用して **AprilTag** を狙った後、DSのStartボタンをタッチします。**OpMode** は**位置推定結果**を示すテレメトリを表示します：

.. figure:: images/10-DS-screen.png
   :align: center
   :width: 75%
   :alt: Driver Station Sample Output

   Driver Stationのサンプル出力

これらの詳細については後のセクションで説明します。この例では、カメラはINTO THE DEEPの **AprilTag** #11の真正面12インチの位置にあります。

**AprilTag** をカメラの視野内に完全に保ちながら、カメラをゆっくりと動かしてください。テレメトリはフィールド上のカメラの位置で更新されます。

機能しています！あなたの **OpMode** はカメラの**グローバル姿勢**を決定できます。後のセクションでは、ロボット上のカメラの配置に基づいて、グローバル**ロボット姿勢**を取得する方法について説明します。

*FTCプレビューの使用方法をすでに知っている場合は、次の2つのセクションをスキップしてください。*

DS プレビュー
----------

テレメトリデータを説明する前に、このページでは**プレビュー**を使用してカメラの **AprilTag** ビューを確認する2つのセクションを提供します。プレビューはロボットビジョンの作業に不可欠です。

**Driver Station** (DS)で、INITのままにしてください - Startボタンをタッチしないでください。

右上隅の3点メニューをタッチし、次に ``Camera Stream`` をタッチします。これによりカメラのビューが表示されます。画像をタップして更新します。

.. figure:: images/20-CameraStream.png
   :align: center
   :width: 85%
   :alt: DS Camera Stream

   DS Camera Streamの例

大きなプレビューを表示するには、右下隅の矢印をタッチします。

または、Camera Streamを再度選択して、前の画面とそのテレメトリに戻ります。

RC プレビュー
----------

**Robot Controller** (RC)デバイスも ``LiveView`` と呼ばれるプレビューを作成します。これはフルビデオで、RC phoneの画面に自動的に表示されます。

.. figure:: images/30-LiveView.png
   :align: center
   :width: 85%
   :alt: Control Hub Preview

   Control Hubプレビュー

上記のプレビューは **REV Control Hub** からのものです。

物理画面がないため、HDMIモニターを接続する**か**、オープンソースの `scrcpy <https://github.com/Genymobile/scrcpy>`_（「スクリーンコピー」と呼ばれる）を使用して、Wi-Fi経由で **Control Hub** に接続されているラップトップまたはコンピューターでプレビューを表示する必要があります。

基本的なテレメトリデータ
--------------------

DSテレメトリを詳しく見てみましょう：

.. figure:: images/40-telemetry.png
   :align: center
   :width: 85%
   :alt: DS Telemetry Example

   DSテレメトリの例

この例では、カメラはINTO THE DEEPの **AprilTag** #11の真正面12インチの位置にあります。

.. figure:: images/45-ITD-tag-numbers.png
   :align: center
   :width: 85%
   :alt: Tag Locations for INTO THE DEEP

   INTO THE DEEPの特定のタグ位置

**AprilTag** #11の中心は、フィールドの中心からX = -72インチの位置にあります。このテレメトリは、カメラのX位置を（約）-60インチ、つまりそのタグの12インチ前方として示しています。

**AprilTag** #11の中心は、フィールドの中心からY = 48インチの位置にあります。このテレメトリは、カメラのY位置を（約）48インチ、つまりそのタグと（水平方向に）直接整列していることを示しています。

**AprilTag** #11の中心は、Z = 5.9インチの位置（マット上）にあります。このテレメトリは、カメラのZ位置を（約）5.9インチ、つまりそのタグと（垂直方向に）直接整列していることを示しています。

カメラレンズは **AprilTag** に平行であるため、Pitch、Roll、Yawの値は直交（0度または90度の倍数）になるはずです。このテレメトリは、PRY値が（約）0度または90度であることで、平行な向きを確認しています。

基準座標系
----------------

上記の例では、yaw角度は（約）-90度として与えられています。しかし、カメラは負のX方向を向いているため、公式FTC
:ref:`フィールド座標系 <first field coordinate system>`
では-180度の方位またはyaw角度を持っています：

.. figure:: images/50-field-axes.png
   :align: center
   :width: 85%
   :alt: FTC Field Coordinate System

   FTCフィールド座標系

このサンプル **OpMode** は、:ref:`IMUまたはロボット軸 <imu axes def>`、オドメトリデバイスの軸、およびFTCフィールドシステム（上図参照）を含む他のFTCナビゲーションアプリケーションから期待されるものとは異なる可能性のある基準座標系（座標系）を使用します。これらの違いは、通常、軸方向の基本的で明白な変更、軸の入れ替え、直交角度（90度単位）をもたらします。

**AprilTag** 位置推定の特定のシナリオに対して、これらの違いを学び、**OpMode** に組み込んでください。特定のナビゲーション目標を達成するために、必要に応じて値を手動で調整してください。

オフセット、平滑化、その他の調整の有無にかかわらず、**AprilTag ナビゲーションの精度と信頼性を評価してください**。一部のFTCチームは、ナビゲーションに複数のデータソースを使用しています。広範なテストと改良を通じて**実証された**機能に基づいてロボット戦略を立ててください。

ロボット上のカメラ配置
-------------------------

サンプル **OpMode** は、ロボット上のカメラの位置と向きを指定するフィールドを提供します。返されるデータは、カメラの姿勢ではなく、グローバル**ロボット姿勢**を表します。

上記の基準座標系に関する注意事項に従いながら、**Blocks** およびJavaサンプル **OpMode** のコメント付き指示に従うように最善を尽くしてください：

..

   これらの値を設定するには、カメラとロボットの軸の定義が必要です：

   **カメラ軸：**

   * *原点位置：* レンズの中心
   * *軸の向き：* +x 右、+y 下、+z 前方（カメラの視点から）

   **ロボット軸：**（これは典型的ですが、好きなように定義できます）

   * *原点位置：* フィールド高さでのロボットの中心
   * *軸の向き：* +x 右、+y 前方、+z 上方

   **位置：**

   * すべての値がゼロ（変換なし）の場合、カメラがロボットの中心にあることを意味します。カメラが左に5インチ、前方に7インチ、地面から12インチ上に配置されているとすると、位置を(-5, 7, 12)に設定する必要があります。

   **向き：**

   * すべての値がゼロ（回転なし）の場合、カメラが真上を向いていることを意味します。
     straight up. In most cases, you'll need to set the pitch to -90 degrees
     (rotation about the x-axis), meaning the camera is horizontal. Use a yaw
     of 0 if the camera is pointing forwards, +90 degrees if it's pointing
     straight left, -90 degrees for straight right, etc. You can also set the
     roll to +/-90 degrees if it's vertical, or 180 degrees if it's
     upside-down.

To see the commands for setting **camera pose** (on the robot), select and read
the Blocks **or** Java section below:

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      .. figure:: images/60-camera-pose.png
         :align: center
         :width: 85%
         :alt: Camera Pose Blocks

      The third Block called ``.setCameraPose`` can be found in the toolbox
      under Vision/AprilTag/AprilTagProcessor.Builder.

   .. tab-item:: Java
      :sync: java

      These lines show that the camera placement on the robot becomes part of
      the AprilTag Processor, through the Java Builder pattern.

      .. code-block:: java

         import org.firstinspires.ftc.robotcore.external.navigation.Position;
         import org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles;
         .
         Position cameraPosition = new Position(DistanceUnit.INCH, 0, 0, 0, 0);
         YawPitchRollAngles cameraOrientation = new YawPitchRollAngles(AngleUnit.DEGREES, 0, -90, 0, 0);
         .
         AprilTagProcessor aprilTag = new AprilTagProcessor.Builder()
               .setCameraPose(cameraPosition, cameraOrientation)
               .build();

グローバル姿勢の読み取り
-------------------

**グローバルロボット姿勢**データを読み取るコマンドを確認するには、以下の **Blocks** または Java セクションを選択してお読みください：

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      これらの緑色のブロックは、後で使用するために位置変数に割り当てることができます。

      .. figure:: images/70-robot-position.png
         :align: center
         :width: 85%
         :alt: Robot Position Blocks

         ロボット位置ブロック

      これらの緑色のブロックは、後で使用するために向き変数に割り当てることができます。

      .. figure:: images/75-robot-orientation.png
         :align: center
         :width: 85%
         :alt: Robot Orientation Blocks

         ロボット向きブロック

   .. tab-item:: Java
      :sync: java

      これらの行は、後で使用するために位置と向きの値を変数に割り当てる方法を示しています。サンプル **OpMode** で使用されているように、これらは通常 ``for`` ループ内の「瞬時」値です。

      .. code-block:: java

         import org.firstinspires.ftc.vision.apriltag.AprilTagDetection;
         .
         AprilTagDetection detection;
         .
         double myX = detection.robotPose.getPosition().x;
         double myY = detection.robotPose.getPosition().y;
         double myZ = detection.robotPose.getPosition().z;
         .
         double myPitch = detection.robotPose.getOrientation().getPitch(AngleUnit.DEGREES);
         double myRoll = detection.robotPose.getOrientation().getRoll(AngleUnit.DEGREES);
         double myYaw = detection.robotPose.getOrientation().getYaw(AngleUnit.DEGREES);

まとめ
-------

2024年のFTCソフトウェアは、カメラとフィールド上の固定された **AprilTag** を使用した**ロボット位置推定**を可能にします。これは3つの要素を組み合わせることで実現されます：

* 基本的な **AprilTag** 姿勢データ
* タグに組み込まれたメタデータ
* ロボット上のカメラの姿勢

**AprilTag** 位置推定は、**IMU** やロボット軸、オドメトリデバイスの軸、FTCフィールドシステムなど、他のものとは異なる可能性のある基準座標系（座標系）を使用します。必要に応じて調整してください。

このナビゲーションツールを他の選択肢と比較評価し、実証された機能に基づいてロボット戦略を計画してください。

FTCロボットナビゲーションを開発して目標を達成できることをお祈りします！

