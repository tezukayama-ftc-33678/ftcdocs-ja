ソフトウェアの概要
------------------

**SDK** には、**CameraControl** と呼ばれるスーパーインターフェイスが含まれており、5つのインターフェイスが含まれています：

- :doc:`ExposureControl </programming_resources/vision/webcam_controls/exposure/index>`
- :doc:`GainControl </programming_resources/vision/webcam_controls/gain/index>` 
- :doc:`WhiteBalanceControl </programming_resources/vision/webcam_controls/white_balance/index>` （**SDK** 7.1 の新機能）
- :doc:`FocusControl </programming_resources/vision/webcam_controls/focus/index>`
- :doc:`PtzControl </programming_resources/vision/webcam_controls/ptz/index>`

Java クラスと同様に、Java インターフェイスはメソッドを提供します。Webcam は、これら5つのインターフェイスのメソッドを使用して制御できます。

**PtzControl** では、仮想パン、チルト、ズームの3つの関連機能を制御できます。**ExposureControl** には、自動露出優先度、または AE Priority と呼ばれる機能も含まれています。このチュートリアルでは、合わせて **8つの Webcam 制御** について説明します。

公式ドキュメントは `Javadocs <https://javadoc.io/doc/org.firstinspires.ftc>`__ にあります。**RobotCore** のリンクをクリックし、左側の列の **CameraControl** リンクをクリックします。

.. figure:: images/020-RobotCore.png
   :align: center

   **RobotCore** Javadoc API

そのページには、上記の5つのインターフェイスへのリンクがあります。

ここで説明するメソッドは、**Android Studio** または **OnBot Java** で使用できます。また、別の :ref:`Blocks プログラミングチュートリアル <programming_resources/blocks/blocks-tutorial:blocks programming tutorial>` で説明されている **myBlocks** を作成することで、**Blocks** プログラマーに提供することもできます。

ここと、以下の `サンプル OpModes <#sample-opmodes>`__ で **Vuforia** について言及されています。** なぜ Vuforia なのか？** **FIRST** **Tech Challenge** の Google の **TensorFlow Lite** の実装は、**Vuforia** ビデオストリームからカメラ画像を受信します。**SDK** にはすでに **Vuforia** がナビゲーション用に含まれており、使用されているため、カメラストリームを **TFOD** に渡すための便利なツールです。

これらの **CameraControl** インターフェイスにより、独自のパフォーマンスのための **Vuforia** の要件または設定内で、Webcam をある程度制御できます。このような設定には、ここでは説明しない解像度とフレームレートが含まれます。
