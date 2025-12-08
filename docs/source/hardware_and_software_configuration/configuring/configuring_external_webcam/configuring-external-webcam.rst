Control Hub での外部ウェブカメラの構成
==================================================

はじめに
------------

競技マニュアルでは、コンピュータービジョン関連のタスクに USB Video Class（UVC）互換カメラの使用を許可しています。**REV Robotics Control Hub** を使用している場合、**Control Hub** には内蔵カメラが含まれていないため、外部ウェブカメラを使用する必要があります。このドキュメントでは、外部ウェブカメラを **Control Hub** に接続、構成、使用する方法について説明します。

このドキュメントをまとめてくれた Westside Robotics (Los Angeles) の Chris Johannesen に特別な感謝を捧げます。

外部カメラのタイプ
-----------------------

理論的には、任意の USB Video Class（UVC）カメラがシステムで動作するはずです。ただし、*FIRST* は Logitech の UVC ウェブカメラの使用を推奨しています。次のカメラはテストされており、SDK ソフトウェアで正確に動作するようにキャリブレーションされています。

- :ref:`logitech_c270_label`
- :ref:`logitech_c310_label`
- :ref:`logitech_c920_label`

UVC カメラのキャリブレーションは、オプションの高度なタスクです。キャリブレーションファイルの作成手順は、ftc_app プロジェクトフォルダーの `teamwebcamcalibrations.xml <https://github.com/ftctechnh/ftc_app/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__ ファイルのコメントにあります（ファイルのオンラインコピーについては、この `リンク <https://github.com/ftctechnh/ftc_app/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__ にアクセスしてください）。

カメラの接続
---------------------

UVC カメラは、**REV Control Hub** の USB 3.0 ポートに直接接続できます。**REV Expansion Hub** とは異なり、外部電源付き USB ハブは必要ありません。

.. image:: images/USB-camera-Control-Hub.jpg
   :alt: Control Hub with UVC camera connected.
   
.. warning:: **Control Hub** の USB 2.0 ポートでの静電気放電（ESD）イベントは、Wi-Fi の切断を引き起こす可能性があります。

   REV **Control Hub** には、USB 2.0 ポートに接続されたデバイスに関する
   `既知の ESD 問題 <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system#esd-mitigation-techniques>`_
   があります。
   USB 2.0 ポートを使用すると、ESD が **Control Hub** の Wi-Fi チップに影響を与える可能性があります（ドライバーハブとの Wi-Fi 切断を引き起こす）。
   カメラなどの USB デバイスは、**Control Hub** の USB 3.0 ポートに接続してください。 
   
2 つのウェブカメラを接続する場合は、`カメラと USB ハブ`_ を参照してください。

カメラの構成
--------------------

外部カメラを使用する前に、USB 接続デバイスとしてアクティブな構成ファイルに追加する必要があります。

Use the Configure Robot menu item on the paired DRIVER STATION device to
add the webcam as a USB-connected device to an existing or newly created
configuration file. Note that the Scan operation for the Configure Robot
activity should detect the webcam and give it a default name of “Webcam
1”.

.. image:: images/webcam-config-CH.jpg
   :alt: Screen shot showing the Scan button circled in yellow and the resulting USB device listed as Webcam 1.

このデフォルト名を保持する（サンプル **OpMode** はこの名前を参照します）か、変更できます。ウェブカメラ名を変更する場合は、**OpMode** がこの新しい名前を参照していることを確認してください。

サンプル OpMode
---------------

構成が保存されてアクティブ化されると、外部 UVC カメラをロボットビジョンタスク用にプログラムできます。

The SDK software offers “webcam” versions of its sample Blocks and Java
Op Modes, showing how to use the external UVC camera for VisionPortal operations.

.. image:: images/blockswebcam.png
   :alt: Blocks code for initializing a webcam.

**OpMode** を開いて編集する前に、意図した構成（カメラ付き）がアクティブであることを確認します。また、**OpMode** で参照されている名前が構成ファイルで指定された名前と一致していることを確認します。

Image Preview
-------------

The *FIRST* Tech Challenge apps provide camera preview for ‘stream-enabled’ Op
Modes using VisionPortal.

ペアリングされた **DRIVER STATION** デバイスで、カメラを接続して構成し、ストリーム対応 **OpMode** を選択します。INIT ボタンを押し、ストリーミングソフトウェアが初期化されるまで少し待ちます。START ボタンを押さないでください。代わりに、メインメニュー（画面右上の 3 つのドット）を開き、Camera Stream を選択します。このオプションは、ゲームパッドと START ボタンが安全のために無効になっているこの時点でのみ表示されます。

.. image:: images/DS-webcam-preview-CH-1.jpg
   :alt: Driver Station screen shot showing the menu with the Camera Stream option circled in yellow.

カメラ画像が **DRIVER STATION** 画面に表示されます。画像を手動でタッチして更新します。帯域幅を節約するために、一度に 1 つのフレームのみが送信されます。

.. image:: images/DS-webcam-preview-CH-2.jpg
   :alt: Driver Station screen shot showing the camera image. 

このオプションを使用して、必要に応じて頻繁に手動で画像を更新しながら、カメラを調整できます。完了したら、メインメニューを開き、Camera Stream を再度選択してプレビューをオフにします。プレビュー画像が閉じ、ゲームパッドが有効になり、START ボタンを押して **OpMode** の実行を続行できます。

.. image:: images/DS-webcam-preview-CH-3.jpg
   :alt: Driver Station screen shot showing the menu with the Camera Stream option circled in yellow.

.. note:: Camera Stream 機能は **OpMode** の INIT フェーズ中にのみ使用できるため、waitForStart コマンドの**前**に **OpMode** で **VisionPortal** がアクティブ化されていることを確認する必要があります。

.. image:: images/activateBeforeWaitForStart.png
   :alt: Blocks code showing the INIT code for the webcam is called before wait for start.

If you do not see the Camera Stream option in your main menu on your
DRIVER STATION, then verify that the VisionPortal is activated
before the waitForStart command in your Op Mode. Also make sure you’ve
given the system enough time to initialize the VisionPortal software before
you check to see if Camera Stream is available.

Scrcpy
------

**OpMode** の実行中にコンピューターからカメラ出力を表示するには、`scrcpy <https://github.com/Genymobile/scrcpy>`__ を使用できます。これを行うには、まず **Control Hub** との ADB 接続を取得する必要があります。これは、**Control Hub** の USB-C ポートに USB-A から USB-C ケーブルを接続することで実行できます。Windows の場合、**Control Hub** WiFi ネットワークに接続し、`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/gs/install>`__ を開くこともできます。接続したら、`これらの指示 <https://github.com/Genymobile/scrcpy?tab=readme-ov-file#get-the-app>`__ を使用して、コンピューターに scrcpy をインストールして実行します。

.. image:: images/webcamWithScrcpy.jpg
   :alt: Screen shot showing the camera output viewed with scrcpy.

.. warning:: scrcpy はカメラ出力を表示する優れた方法ですが、競技マニュアルでは、マッチ中に **DRIVER STATION** 以外のデバイスを **Control Hub** に接続することを許可していません。

外部 HDMI モニター
---------------------

また、カメラ出力は、REV **Control Hub** の HDMI ポートに接続されたディスプレイモニターまたは他のデバイスで表示できます。

.. image:: images/HDMIMonitor.jpg
   :alt: Photo showing an external HDMI monitor displaying the camera output from a connected control hub.

.. warning:: ポータブルディスプレイモニターを使用して **Control Hub** のカメラストリームを表示またはトラブルシューティングできますが、マッチ中にポータブルディスプレイモニターを **Control Hub** に接続することは許可されていません。

上級ユーザー
--------------

カスタムストリームの場合、**Android Studio** の上級ユーザーは、`CameraStreamClient <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/org/firstinspires/ftc/robotcore/external/stream/CameraStreamClient.html>`__、`CameraStreamServer <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/org/firstinspires/ftc/robotcore/external/stream/CameraStreamServer.html>`__、および `CameraStreamSource <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/org/firstinspires/ftc/robotcore/external/stream/CameraStreamSource.html>`__ クラスの `API ドキュメント <https://javadoc.io/doc/org.firstinspires.ftc>`__ を参照できます。

カメラと USB ハブ
^^^^^^^^^^^^^^^^^^^^

**Control Hub** の USB 3.0 ポートに UVC ウェブカメラをすでに接続できます。しかし、2 つのウェブカメラを使用したい場合はどうでしょうか？おそらく、ロボットを回転させることなく、ロボットが前方や後方を見ることができるようにしたいでしょう。**Control Hub** の USB 3.0 ポートで 2 つのウェブカメラを使用するには、USB ハブを追加できます。これにより、USB 2.0 ポートのデバイスでの ESD 問題が回避されます。

.. note:: 2 つの標準 UVC ウェブカメラを使用している場合、電源付き USB ハブを使用する必要はありません。

   ただし、Logitech C920 のような一部のウェブカメラは他のものよりも多くの電力を消費し、同時に使用すると USB ポートから過剰な電力を消費するという報告があります。したがって、C920 には電源付き USB ハブを使用する必要があります。

USB ハブのもう 1 つの使用例は、`Limelight 3A <https://limelightvision.io/products/limelight-3a>`_ カメラを使用している場合です。このデバイスにはボード上に独自のプロセッサがあり、これの欠点の 1 つは、**opMode** が実行されていない場合でも、カメラが常に電力を消費することです。電源付き USB ハブを追加することで、Limelight はロボットのバッテリーを消耗しません。

適切な電源付き USB ハブの 1 つは、Acer ODK350 5-IN-1 USB 3.0 Hub です。 
It has a USB C port that can supply power to all connected devices.

.. note:: At the time this was written, the Acer ODK350 hub was not listed on Acer's website, but was available on Amazon's website.
   
   Not all USB hubs are powered hubs.
   Typically, you can't just plug a power bank into any of the USB hub's ports. It must be a port that is designed to supply power.
   So if you looking for a powered USB hub there should be a note in the specifications something like the following:
   *Note: This USB C port (with IN 5V printed) can not be used for data transfer and charge other devices. It can only supply power for the other 4 USB ports.*

.. figure:: images/two-webcams.jpg
   :alt: A REV Control Hub with a powered USB hub and two webcams.
   
   Acer ODK350 USB hub
   
   The USB Hub is connected to the USB 3.0 port of the Control Hub.
   A powerbank is connected to the USB C port on the USB hub to supply power to the connected devices.
   Two Logitech C920 webcams are connected to the USB hub.

2 つのカメラを切り替えて **AprilTag** を検出する方法を示す `AprilTag Switchable Cameras <https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/ConceptAprilTagSwitchableCameras.java>`_ サンプルプログラムを参照してください。

もう 1 つの使用例は、Limelight を電源付き USB ハブと一緒に使用して、ロボットのバッテリーの消耗を減らすことです。この例では、Limelight とウェブカメラの両方を示しています。

.. figure:: images/webcam-and-limelight-3a.jpg
   :alt: A USB hub with a webcam and a Limelight 3A connected to a REV Control Hub.

   Acer ODK350 USB hub
     
   The USB Hub is connected to the USB 3.0 port of the Control Hub.
   A powerbank is connected to the USB C port on the USB hub to supply power to the connected devices.
   A Logitech C270 webcam and a Limelight 3A are connected to the USB hub.

Limelight 3A は互換性のある **VisionPortal** デバイスではありません。したがって、**AprilTag** 切り替え可能カメラのサンプルコードを使用できません。ただし、Limelight や **VisionPortal** ウェブカメラのいずれかから結果を取得し、必要に応じて使用できます。


