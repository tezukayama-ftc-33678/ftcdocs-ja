
Control Hubで外部Webカメラを設定する方法
==================================================


はじめに
--------

**競技マニュアル** では、コンピュータビジョン関連のタスクにUSB Video Class（UVC）対応カメラの使用が認められています。
**REV Robotics Control Hub** を使用する場合、内蔵カメラが搭載されていないため、外部Webカメラを利用する必要があります。
このドキュメントでは、Control Hubに外部Webカメラを接続・設定し、使用する方法について説明します。

本ドキュメント作成にご協力いただいたWestside Robotics（ロサンゼルス）のChris Johannesen氏に感謝します。


外部カメラの種類
-----------------

理論上、USB Video Class（UVC）対応カメラはどれでも動作しますが、**FIRST** ではLogitech製UVC Webカメラの使用を推奨しています。
以下のカメラはSDKソフトウェアで動作確認・キャリブレーション済みです：

- :ref:`logitech_c270_label`
- :ref:`logitech_c310_label`
- :ref:`logitech_c920_label`

UVCカメラのキャリブレーションは任意の高度な作業です。キャリブレーションファイルの作成方法は、
`teamwebcamcalibrations.xml <https://github.com/ftctechnh/ftc_app/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__
のコメント欄に記載されています（オンライン版は`こちら <https://github.com/ftctechnh/ftc_app/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__）。


カメラの接続方法
-----------------

UVCカメラは**REV Control Hub** のUSB 3.0ポートに直接接続できます。**REV Robotics Expansion Hub** とは異なり、外部電源付きUSBハブは不要です。

.. image:: images/USB-camera-Control-Hub.jpg
   :alt: Control HubにUVCカメラを接続した様子。

.. warning:: Control HubのUSB 2.0ポートで発生する静電気放電（ESD）により、Wi-Fiが切断される場合があります。

   **REV Control Hub** には、USB 2.0ポートに接続したデバイスによる
   `ESD問題 <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system#esd-mitigation-techniques>`_
   が報告されています。
   USB 2.0ポートを使用すると、ESDがWi-Fiチップに影響し、**Driver Hub** とのWi-Fi接続が切れることがあります。
   カメラなどのUSB機器は必ずUSB 3.0ポートに接続してください。

2台のWebカメラを接続したい場合は「`カメラとUSBハブ <#cameras-and-usb-hubs>`_」をご参照ください。


カメラの構成
------------

外部カメラを使用する前に、USB接続デバイスとしてアクティブな構成ファイルに追加する必要があります。

ペアリング済みの**DRIVER STATION** 端末で「Configure Robot」メニューを使用し、WebカメラをUSB接続デバイスとして既存または新規の構成ファイルに追加してください。
「Scan」操作でWebカメラが検出され、デフォルト名「Webcam 1」が割り当てられます。

.. image:: images/webcam-config-CH.jpg
   :alt: ScanボタンとWebcam 1が表示された画面。

このデフォルト名のままでも（サンプル**OpMode** はこの名前を参照します）、変更しても構いません。名前を変更した場合は、**OpMode** 内で新しい名前を参照するようにしてください。


サンプルOpMode
---------------

構成ファイルが保存・有効化されると、外部UVCカメラを使ったロボットビジョンのプログラムが可能になります。

SDKソフトウェアには、外部UVCカメラを**VisionPortal** で利用するための「webcam」版サンプル**Blocks** およびJava**OpMode** が用意されています。

.. image:: images/blockswebcam.png
   :alt: Webカメラ初期化のBlocksコード。

**OpMode** を編集する前に、カメラを含む構成が有効になっていること、**OpMode** で参照するカメラ名が構成ファイルの名前と一致していることを確認してください。


画像プレビュー
--------------

**FIRST Tech Challenge** アプリでは、**VisionPortal** を使った「ストリーム対応**OpMode**」でカメラプレビューが可能です。

ペアリング済みの**DRIVER STATION** 端末でカメラを接続・構成した状態で、ストリーム対応**OpMode** を選択します。INITボタンを押して、ストリーミングソフトウェアの初期化を待ちます（STARTボタンは押さないでください）。
画面右上のメニュー（三点アイコン）から「Camera Stream」を選択します。このオプションはこのタイミングのみ表示され、ゲームパッドやSTARTボタンは安全のため無効化されます。

.. image:: images/DS-webcam-preview-CH-1.jpg
   :alt: Camera Streamオプションが表示されたDriver Station画面。

カメラ画像が**DRIVER STATION** 画面に表示されます。画像を手動でタッチすると更新されます。帯域を節約するため、1フレームずつ送信されます。

.. image:: images/DS-webcam-preview-CH-2.jpg
   :alt: カメラ画像が表示されたDriver Station画面。

この機能を使ってカメラの調整が可能です。調整が終わったら、メニューから再度「Camera Stream」を選択してプレビューを終了します。プレビュー画像が閉じ、ゲームパッドが有効化され、STARTボタンを押して**OpMode** を実行できます。

.. image:: images/DS-webcam-preview-CH-3.jpg
   :alt: Camera Streamオプションが表示されたDriver Station画面。

.. note:: Camera Stream機能は**OpMode** のINITフェーズのみ利用可能です。必ず**waitForStart** コマンドの前に**VisionPortal** が有効化されていることを確認してください。

.. image:: images/activateBeforeWaitForStart.png
   :alt: waitForStart前にWebカメラのINITコードが呼ばれているBlocksコード。

メインメニューにCamera Streamオプションが表示されない場合は、**OpMode** 内で**VisionPortal** が**waitForStart** 前に有効化されているか、VisionPortalソフトウェアの初期化に十分な時間を確保しているか確認してください。


scrcpy
------

**OpMode** 実行中にパソコンでカメラ映像を確認したい場合は、
`scrcpy <https://github.com/Genymobile/scrcpy>`__を利用できます。
その際は、まず**Control Hub** とADB接続を確立する必要があります。
USB-A to USB-Cケーブルで**Control Hub** のUSB-Cポートに接続するか、Windowsの場合は**Control Hub** のWi-Fiネットワークに接続し、
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/gs/install>`__を開いてください。
接続後、`こちらの手順 <https://github.com/Genymobile/scrcpy?tab=readme-ov-file#get-the-app>`__でscrcpyをインストール・実行します。

.. image:: images/webcamWithScrcpy.jpg
   :alt: scrcpyでカメラ映像を表示した画面。

.. warning:: scrcpyはカメラ映像を確認するのに便利ですが、
   ** 競技マニュアル** では、競技中に**DRIVER STATION** 以外のデバイスを**Control Hub** に接続することは禁止されています。


外部HDMIモニター
-----------------

カメラ映像は、**REV Control Hub** のHDMIポートに接続したディスプレイモニター等でも表示できます。

.. image:: images/HDMIMonitor.jpg
   :alt: Control Hubに接続した外部HDMIモニターでカメラ映像を表示している様子。

.. warning:: ポータブルディスプレイモニターはカメラストリームの確認やトラブルシュートに利用できますが、
   競技中に**Control Hub** へ接続することは禁止されています。


上級者向け情報
---------------

独自ストリームを作成したい上級者の方は、**Android Studio** の
`APIドキュメント <https://javadoc.io/doc/org.firstinspires.ftc>`__を参照してください。
以下のクラスが参考になります：
- `CameraStreamClient <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/org/firstinspires/ftc/robotcore/external/stream/CameraStreamClient.html>`__
- `CameraStreamServer <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/org/firstinspires/ftc/robotcore/external/stream/CameraStreamServer.html>`__
- `CameraStreamSource <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/org/firstinspires/ftc/robotcore/external/stream/CameraStreamSource.html>`__


カメラとUSBハブ
----------------

UVC Webカメラは**Control Hub** のUSB 3.0ポートに直接接続できます。
では、2台のWebカメラを使いたい場合はどうすればよいでしょうか？
例えば、ロボットが前方・後方両方を同時に見られるようにしたい場合などです。
USB 3.0ポートにUSBハブを追加することで、2台のWebカメラを接続できます。
これにより、USB 2.0ポートのESD問題も回避できます。

.. note:: 標準的なUVC Webカメラ2台を使う場合、必ずしも電源付きUSBハブは必要ありません。

   ただし、Logitech C920のように消費電力が大きいWebカメラは、同時使用時にUSBポートから過剰な電力を消費する報告があります。
   C920を使う場合は電源付きUSBハブの利用を推奨します。

USBハブのもう一つの用途は、`Limelight 3A <https://limelightvision.io/products/limelight-3a>`_カメラの接続です。
このデバイスは独自のプロセッサを搭載しており、**OpMode** が動作していない時でも常に電力を消費します。
電源付きUSBハブを使うことで、Limelightによるロボットバッテリーの消耗を防げます。

おすすめの電源付きUSBハブは「Acer ODK350 5-IN-1 USB 3.0 Hub」です。
USB Cポートから全ての接続機器に電力供給が可能です。

.. note:: 本ドキュメント執筆時点では、Acer ODK350ハブはAcer公式サイトには掲載されていませんが、Amazonで購入可能です。
   
   すべてのUSBハブが電源付きとは限りません。
   一般的に、どのUSBポートにもモバイルバッテリーを接続できるわけではなく、電力供給専用ポートが必要です。
   電源付きUSBハブを探す際は、仕様欄に「*Note: This USB C port (with IN 5V printed) can not be used for data transfer and charge other devices. It can only supply power for the other 4 USB ports.*」のような記載があるか確認してください。

.. figure:: images/two-webcams.jpg
   :alt: 電源付きUSBハブと2台のWebカメラを接続したREV Control Hub。

   Acer ODK350 USBハブ

   USBハブは**Control Hub** のUSB 3.0ポートに接続します。
   USBハブのUSB Cポートにモバイルバッテリーを接続し、全ての機器に電力を供給します。
   2台のLogitech C920 WebカメラがUSBハブに接続されています。

2台のカメラを切り替えて**AprilTag** を検出するサンプルプログラムは、
`AprilTag Switchable Cameras <https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/ConceptAprilTagSwitchableCameras.java>`_をご参照ください。

もう一つの用途は、Limelightと電源付きUSBハブを使ってロボットバッテリー消耗を抑えることです。
以下の例ではLimelightとWebカメラの両方を接続しています。

.. figure:: images/webcam-and-limelight-3a.jpg
   :alt: USBハブにWebカメラとLimelight 3Aを接続したREV Control Hub。

   Acer ODK350 USBハブ

   USBハブは**Control Hub** のUSB 3.0ポートに接続します。
   USBハブのUSB Cポートにモバイルバッテリーを接続し、全ての機器に電力を供給します。
   Logitech C270 WebカメラとLimelight 3AがUSBハブに接続されています。

Limelight 3Aは**VisionPortal** 対応デバイスではないため、AprilTag切替サンプルコードは利用できません。
ただし、Limelightや**VisionPortal** Webカメラの結果を必要に応じて取得・活用することは可能です。


