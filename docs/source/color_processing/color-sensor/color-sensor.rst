カラー処理 カラーセンサー
=============================

概要
--------

FTCの新しい**OpenCV**ビジョンツールを使用する簡単な方法は、「カラーセンサー」を操作することです。つまり、指定されたゾーンで**ロボットのカメラが見た色**を判定できます。

以下では、小さな中央の長方形が評価されている領域です：

.. figure:: images/10-sensor-intro.png
   :width: 75%
   :align: center
   :alt: INTO THE DEEPゲーム要素

   カラーセンサー検出ゾーン

主な利点は、例えば**REV Color Sensor**などと比較して、カメラがオブジェクトからはるかに遠くに離れていても機能することです。

それでも、カメラを正確に向け、検査する画像ゾーンを慎重に選択することが重要です。

上記の例の場合、**OpenCV**は次のような結果を提供できます：

.. figure:: images/20-telemetry-intro.png
   :width: 75%
   :align: center
   :alt: RED検出を示すDriver Stationアプリ

   カラーセンサーを使用したRED検出

以下のセクションでは、サンプル**OpMode**を使用してこれを行う方法について説明します。

構成
-------------

*次の場合、このセクションをスキップしてください...*


* *アクティブなロボット構成に既に「Webcam 1」が含まれている場合*、または
* *Androidスマートフォンの内蔵カメラをRobot Controllerとして使用している場合*

プログラミングを開始する前に、**REV Control Hub**ユーザーは、カラーセンサーとして使用するUSBウェブカメラを含むロボット構成を作成する必要があります。

今のところ、デフォルトのウェブカメラ名「Webcam 1」を使用してください。別の名前を希望する場合は、サンプル**OpMode**を編集して、ロボット構成の正確なウェブカメラ名と一致させてください。

その構成を保存してアクティブ化します。その名前は、ペアリングされた**Driver Station**画面に表示されるはずです。

サンプルOpMode
-------------

サンプルOpModeを開く
+++++++++++++++++++++++++

サンプル**OpMode**を開く方法については、**Blocks**または**Java**のタブをクリックしてください：

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      1. **Robot Controller**にWi-Fi経由で接続されたラップトップまたはデスクトップコンピューターで、Chromeブラウザを開きます。**REV Control Hub**のアドレス``http://192.168.43.1:8080``（またはAndroid RCスマートフォンの場合は``http://192.168.49.1:8080``）に移動し、*Blocks*タブをクリックします。

      2. ``Create New OpMode``をクリックし、「ColorSensor_Maria_v01」などの新しい名前を入力し、サンプル**OpMode** ``ConceptVisionColorSensor``を選択します。

      3. **Blocks**画面の上部で、このサンプル**OpMode**はゲームパッドを使用しないため、タイプを「TeleOp」から「Autonomous」に変更できます。

      4. RCスマートフォンの内蔵カメラを使用する場合は、左側の``VisionPortal.Builder``ツールボックスから関連するブロックをドラッグアウトします。

      5. **OpMode**を保存して、試してみましょう！


   .. tab-item:: Java
      :sync: java

      1. **OnBot Java**または**Android Studio**のいずれかを開きます。

      2. ``teamcode``フォルダーで、「ColorSensor_Bobby_v01.java」などの名前で新しい**OpMode**を追加/作成し、サンプル**OpMode** ``ConceptVisionColorSensor.java``を選択します。

      3. 約58行目で、このサンプル**OpMode**はゲームパッドを使用しないため、``@TeleOp``を``@Autonomous``に変更できます。

      4. RCスマートフォンの内蔵カメラを使用する場合は、**OpMode**のコメントに従ってそのカメラを指定します。

      5. 「Build」をクリックして、試してみましょう！

サンプルOpModeを実行する
+++++++++++++++++++++++++

**Driver Station**で：

1. 保存またはビルドしたばかりの**Autonomous** **OpMode**を選択します。
2. 自動30秒マッチタイマーをオフにします（緑のスライダー）。
3. INITのみにタッチします。

**OpMode**は**Telemetry**を提供し、関心領域内の主な「マッチした」色を示す必要があります。

.. figure:: images/30-DStelemetry.png
   :width: 75%
   :align: center
   :alt: Driver Station Telemetry

   Driver Station Telemetry

カメラを動かして、**Driver Station**画面の**Telemetry**エリアを見てください。青いオブジェクトを指しているときは「BLUE」と表示され、同様に他の一般的な色も識別するはずです。

**動作しています！** ロボットのカメラにカラーセンサーがあります。FTCロボットゲームでこれをどのように使用するか考えてみてください。

*FTCプレビューの使用方法をすでに知っている場合は、次の2つのセクションをスキップしてください。*

DSプレビュー
----------

**OpMode**を変更する方法を説明する前に、このページでは**プレビュー**で**OpenCV**の結果を表示する方法を示す2つのセクションを提供します。プレビューは、ビジョンコードの作業に不可欠です。

**DSプレビューを開く**

1. **Driver Station**（DS）で、INITのままにします - Startボタンにタッチしないでください。
2. 右上隅で、3点メニューをタッチしてから、``Camera Stream``をタッチします。これによりカメラのビューが表示されます。画像をタップして更新します。

.. figure:: images/34-CameraStream.png
   :width: 75%
   :align: center
   :alt: Camera Streamプレビュー

   Camera Streamプレビュー

画像上に描画されているのは、評価されている長方形で、**関心領域（Region of Interest、ROI）**と呼ばれます。ROIの境界線の色は、長方形の主な色で、DS **Telemetry**に報告されます。

その境界線が単色の背景に対して「消えて」しまった場合でも、細い白い十字線と4つの小さな白い点でROIを識別できます。

大きなプレビューを表示するには、右下隅の矢印をタッチします。

または、Camera Streamを再度選択して、前の画面とその**Telemetry**に戻ります。

RCプレビュー
----------

**Robot Controller**（RC）デバイスも、``LiveView``と呼ばれるプレビューを作成します。これはフルビデオで、RCスマートフォンの画面に自動的に表示されます。

.. figure:: images/38-LiveView.png
   :width: 75%
   :align: center
   :alt: Control Hub LiveView

   Control Hub LiveView

上記のプレビューは**REV Control Hub**からのものです。

物理的な画面がないため、HDMIモニターを接続する**か**、オープンソースの`scrcpy <https://github.com/Genymobile/scrcpy>`_（「スクリーンコピー」と呼ばれる）を使用して、Wi-Fi経由で**Control Hub**に接続されているラップトップまたはコンピューターでプレビューを表示する必要があります。

サンプルを変更する
-----------------

このサンプル**OpMode**は、ユーザーが**2つの入力**を選択/編集できるように設計されています：


* 関心領域（ROI）を定義する
* 見つかる可能性のある色をリストする

**最初の入力**では、ROIを定義する3つの方法があります：

* フレーム全体
* 標準の画像座標で定義されたサブ領域
* 正規化された+/- 1.0座標システムで定義されたサブ領域

**2番目の入力**では、「マッチ」として結果が選択される候補色をリストする必要があります。

単純に10個の「スウォッチ」から選択します：RED、ORANGE、YELLOW、GREEN、CYAN、BLUE、PURPLE、MAGENTA、BLACK、WHITE。効率を上げるために、マッチを合理的に期待できるスウォッチのみを追加してください。

**BlocksとJavaのOpModeには、これらの編集を案内する詳細なコメントが含まれています。** このチュートリアルでは繰り返しません。

VisionPortalをビルドする
-------------------------

サンプル**OpMode**は、まず**Builderパターン**を使用して「主要な色（Predominant Color）」**Processor**を作成します。これは、**AprilTag Processor**を作成するために使用されるのと同じBuilderパターンで、以前は**TensorFlow Processor**にも使用されていました。

次に、サンプル**OpMode**は、再びBuilderパターンを使用して**VisionPortal**を作成します。これには、「主要な色」Processorを**VisionPortal**に追加することが含まれます。

**OpenCV**はROIの「主要な色」をどのように決定するのでしょうか？`「k-means」 <https://en.wikipedia.org/wiki/K-means_clustering>`_と呼ばれるアルゴリズムが、類似した色のクラスターを決定します。最も多くのピクセルを持つクラスターの色が、ここでは「主要」と呼ばれます。*（これは最終試験には出ません。）*

Testing the Result
------------------

After trying and learning how the commands work, you can incorporate this Color
Sensor into your Autonomous and/or TeleOp OpModes.

As seen in the OpMode's Telemetry section, the result is called
``closestSwatch`` and appears as a word (RED, BLUE, etc.).  But this is not
plain text!

**Testing**, or comparing, for a particular color-match must be done as
follows.  Select and read the Blocks **or** Java section below:

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      At the left side, pull out the following multi-Block from ``Vision/PredominantColor/Processor``:

      .. figure:: images/50-closestSwatchCompare.png
         :align: center
         :width: 75%
         :alt: Closest Swatch Comparison
   
         Closest Swatch Comparison
         
      You must use this special Block to determine if the result is (for example) RED.

      Why?  The result, called ``closestSwatch`` is not **text** (yes it seems
      like text!).  It's a type called ``Swatch`` and can be compared only to
      another ``Swatch``.

   .. tab-item:: Java
      :sync: java

      In the sample OpMode, here's the Telemetry that gives the result:

      .. code-block:: java

         telemetry.addData("Best Match:", result.closestSwatch);

      This displays as text, but this is **not** Java type ``String``!

      Here's how to determine if the result is (for example) RED:

      .. code-block:: java

         if (result.closestSwatch == Swatch.RED)   {  }

      Why?  The result, called ``closestSwatch`` is of type ``Swatch`` and can
      be compared only to another ``Swatch``.


OpMode Programming
------------------

The Color Sensor part of your team's Autonomous OpMode might include these
goals:

#. Seek a color, using the code from this Sample OpMode
#. Take a robot action, based on finding that color

If so, select and read the Blocks **or** Java section below:

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      Beginners often try this first:

      .. figure:: images/55-IFclosestSwatchWrongWay.png
         :alt: Wrong way to act upon match result
         :width: 75%
         :align: center

         Wrong way to act upon match result

      The problem is, after the robot does the action for RED, the OpMode is
      still inside the vision loop.  Very messy and unpredictable.

      A better approach is to save the result (as text!), exit the loop, then
      retrieve the stored result to take the desired RED action.

      .. figure:: images/58-IFclosestSwatchRightWay.png
         :alt: Right way to act upon match result
         :width: 75%
         :align: center

         Right way to act upon match result

      How to exit the vision loop?  It could be based on `time
      <https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Timers-in-FTC-Blocks>`_
      , or finding a particular color, or finding a particular color 10 times
      in a row, or finding only a particular color for 1 full second, or any
      other desired criteria.

   .. tab-item:: Java
      :sync: java

      The color result is generated inside a vision loop.  Save the result (as
      text!), exit the loop, then retrieve the stored result to take the
      desired RED action.

      .. code-block:: java

         String savedColorMatch = "NULL";
         .
         .
         if (result.closestSwatch == Swatch.RED)     {
              savedColorMatch = "RED";
              // your code here: optional to exit the vision loop based on your criteria
              }
         .
         .
         // After exiting the vision loop...
         if (savedColorMatch == "RED")     {
              // your code here: robot actions if the ROI was RED
              }

      How to exit the vision loop?  It could be based on time, or finding a
      particular color, or finding a particular color 10 times in a row, or
      finding only a particular color for 1 full second, or any other desired
      criteria.

Advanced Use
------------

Some teams may prefer to read and evaluate the **actual RGB color values**,
rather than rely on a generic Swatch result.

RGB is a **Color Space** that uses three numerical components of Red, Green and
Blue.  Values range from 0 to 255.  For more info, see this tutorial's :doc:`Color
Spaces <../color-spaces/color-spaces>` page.

Extracting the RGB components can be seen in the Telemetry portion of the
Sample OpMode.  Click the Blocks or Java tab:

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      Here are the RGB components of the ROI's predominant color:

      .. figure:: images/70-Blocks-RGB.png
         :alt: Finding color by RGB
         :width: 75%
         :align: center

      Note: the ``Color`` Block has a drop-down list that includes Hue,
      Saturation and Value.  Those settings will **not work** here, to produce
      components in the HSV Color Space, because the source Block provides only
      RGB color (its method name is ``.rgb``\ ).

   .. tab-item:: Java
      :sync: java

      Here are the RGB components of the ROI's predominant color:

      * ``Color.red(result.rgb)``
      * ``Color.green(result.rgb)``
      * ``Color.blue(result.rgb)``    

For Blocks or Java, those component values can be assigned to numeric
variables, with names like ``ROIRedValue``, ``ROIGreenValue``, and
``ROIBlueValue``.

Now your code can process those RGB variables as desired.

Next Sections
-------------

Soon you can move ahead to try the **Color Locator** processor.

But first, learn a few basic concepts at this tutorial's :doc:`Color Blob Concepts
<../color-blob-concepts/color-blob-concepts>` page.

============

*Questions, comments and corrections to westsiderobotics@verizon.net*

