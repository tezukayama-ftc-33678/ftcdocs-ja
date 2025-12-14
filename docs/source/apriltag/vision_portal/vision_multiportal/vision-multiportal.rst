Vision MultiPortal
==================

**SDK** は2つのポータルを収容でき、それぞれに **AprilTag** および **TFOD** プロセッサを含む完全な機能があり、切り替え可能なカメラさえあります。USB帯域幅を考慮する必要があります。特に外部USBハブを共有するウェブカメラの場合です。

Viewport ID
~~~~~~~~~~~

各ポータルには、Android オペレーティングシステムによって ``Viewport ID`` が割り当てられます。初期化時に、**OpMode** はこれらのID番号を ** キャプチャ** し、ポータルの操作に使用する必要があります。

Android は通常、**OpMode** の各実行ごとに異なる **Viewport ID** 番号を割り当てます。必要に応じて、**Telemetry** を **Driver Station** に送信することでこれを観察できます。

``makeMultiPortalView()`` ブロックまたはメソッドは、**Viewport ID** のリストを返します。各IDをリストから抽出し、``setCameraMonitorViewId()`` ブロックまたはメソッドを使用して各 **VisionPortal Builder** に提供する必要があります。

「デュアルカメラ」は以前（そして今でも）**EasyOpenCV** で利用可能でした。今では **SDK** 内でこれが可能です。

テスト OpMode
~~~~~~~~~~~~~

サンプルFTC **Blocks OpMode** は `こちら <https://gist.github.com/WestsideRobotics/587b5c74375429ac4a929f690ae40940>`__ に投稿されており、**2つのカメラから同時に** **AprilTag** 検出を実証しています。Java版については、**Blocks** 編集ウィンドウで ``Export to Java`` をクリックしてください。

以下は、そのテスト **OpMode** の画像です。注意深く研究すると、複数のカメラストリームを同時に作成および操作するための **Blocks** および **Java** メソッドをよりよく理解できます。

右クリックして新しいブラウザタブで画像を開き、大きなPCスクリーンで拡大表示してください。

.. figure:: images/500-W_MultiPortal_v01.png
   :width: 75%
   :align: center
   :alt: Multiportal Blocks OpMode

   Blocks Multiportal OpMode の例

Moto e4 **RC** スマートフォンでは、**OpMode** は内蔵スマートフォンカメラとウェブカメラを一緒に実行できます。

**Control Hub** では、2つのウェブカメラを実行できます：

- 両方を **Hub** に直接接続、または
- 両方を非電源式USBハブに接続（より制限されたUSB帯域幅で）

デュアルプレビュー
~~~~~~~~~~~~~~~~~~

デュアル **RC** プレビューは ``VERTICAL`` として表示するか、列挙型 ``HORIZONTAL`` で並べて表示できます：

.. figure:: images/200-RC-horizontal.png
   :width: 75%
   :align: center
   :alt: デュアル RC プレビュー

   デュアル RC プレビュー

**DS Camera Stream** プレビューは、1つのカメラのビューのみを表示できます（`既知の特性 <https://github.com/FIRST-Tech-Challenge/FtcRobotController/issues/585>`__ ）。

USB 帯域幅
~~~~~~~~~~

**USB帯域幅** はデュアル ** ウェブカメラ** の懸念事項です。内部スマートフォンカメラには独立した高速相互接続（USBではない）があり、追加されたUSBウェブカメラの影響を受けません。

USB帯域幅の分析については、**Managing CPU and Bandwidth** ページを参照してください。

2つのウェブカメラは同じフォーマットまたは解像度を使用する *必要はありません* 。上記のテストでは、Logitech C920とLogitech C270に同じフォーマットと解像度が適用されました。

Control Hub
~~~~~~~~~~~

**Control Hub に直接接続された** デュアルウェブカメラの場合、USB 2.0およびUSB 3.0ポートは異なるバス上にあります。

これにより、USB帯域幅容量に関する懸念が軽減されますが、解像度が高いと自動最適化されたフレームレートが低下します（以下のテストデータを参照）。

ここでは、ストリームフォーマットの選択にはほとんど影響がありません。しかし、USB 2.0バスは **Control Hub** の **WiFiラジオ** も運ぶため、ウェブカメラを追加するとその信頼性に影響を与える可能性があります。

外部 USB Hub
~~~~~~~~~~~~

一方、** 外部USBハブ**（CH 3.0ポートに接続）上の両方のウェブカメラは、**USB帯域幅制限** を超える可能性があります（ここでは定量化されていません）。

レガシー **YUY2フォーマット** では、1つのウェブカメラまたはもう1つのウェブカメラが、おおよそ640x360解像度を超えるとストリーミングを停止する場合があります。これは、検出がなく、``scrcpy`` 経由の **RC** プレビューで青い画面で示されます。

**MJPEGフォーマット** では、おおよそ432x240未満の解像度では、画像が劣化して少なくとも1つのウェブカメラで **AprilTag** 検出を防ぐ可能性があり、より高い解像度では **RC** アプリを停止するか、**Control Hub** をクラッシュさせる場合があります。

両方のフォーマットで、解像度が高いとフレームレートが低下します。**Managing CPU and Bandwidth** ページでは、テスト、トレードオフ、最適化について説明しています。

チームは、フレーム/秒（FPS）を提供する新しいレポート機能 ``getFps()`` の支援を受けて、これらのトレードオフを評価できます。これは **Blocks** および **Java** で利用できます。

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

