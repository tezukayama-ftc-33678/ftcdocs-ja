外部 UVC カメラと電源付き USB ハブの構成
==========================================================

はじめに
------------

競技マニュアルでは、コンピュータービジョン関連のタスクに USB Video Class（UVC）互換カメラの使用を許可しています。Android スマートフォンを **Robot Controller** として使用しているチームは、コンピュータービジョンタスクに内蔵カメラの代わりに外部接続カメラを使用するオプションがあります。

外部カメラを使用する利点は、ビジョン関連のタスクに便利な場所にカメラを取り付けることができ、同時に Android **Robot Controller** を制御タスクに便利な別の場所に取り付けることができることです。

外部カメラを使用する欠点は、USB 接続カメラによって追加の複雑さが導入されることです。外部カメラは、ロボットにコストと重量を追加し、正しく動作するために正しく配線する必要があります。

どのタイプの外部カメラを使用できますか？
-----------------------------------------

システムは UVC カメラをサポートしています。理論的には、カメラが UVC 準拠であれば、システムで動作するはずです。ただし、*FIRST* Tech Challenge ソフトウェアでテストされ、このソフトウェアで正確に動作するようにキャリブレーションされた推奨ウェブカメラがいくつかあります。

-  Logitech HD Webcam C310
-  Logitech HD Pro Webcam C920

チームが使用できる :doc:`その他の UVC ウェブカメラ <../../../apriltag/vision_portal/visionportal_webcams/visionportal-webcams>` に関する注記があります。

UVC カメラのキャリブレーションは高度なタスクであることに注意してください。キャリブレーションファイルの作成方法の詳細は、ftc_app プロジェクトフォルダーの一部として利用可能な *teamwebcamcalibrations.xml* ファイルのコメントにあります（ファイルのオンラインコピーについては、この `リンク <https://github.com/ftctechnh/ftc_app/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__ にアクセスしてください）。

REV Expansion Hub とスマートフォン
---------------------------

Android スマートフォンと **Expansion Hub** を使用しているチームは、ウェブカメラを使用するために USB ハブを追加する必要があります。

.. image:: images/uvcdiagram.png
   :alt: A REV expansion hub connected to an Android phone and a webcam via a USB Hub.

USB ハブ
^^^^^^^

外部カメラを使用したいチームは、Android **Robot Controller** を外部カメラと REV Robotics **Expansion Hub** に接続するために USB ハブが必要です。正しく動作するには、USB ハブは次の要件を満たす必要があります。

1. USB 2.0 と互換性があります。注：USB 3.0 ハブも機能しますが、高速では動作しません。
2. 480Mbps のデータ転送速度をサポートします。

Modern Robotics Core Power Distribution Module は、データ転送速度が USB 接続ウェブカメラで動作するのに十分な速度ではないため、このタスクには使用できないことに注意してください。

また、競技マニュアルは、この接続を行うために電源付き USB ハブの使用を許可していることに注意してください。チームが電源付き USB ハブを使用する場合、USB ハブを操作する電力は、次のいずれかのソースからのみ供給できます。

1. 競技マニュアルに準拠した外部接続の市販の（COTS）USB バッテリーパック。
2. REV Robotics **Expansion Hub** の 5V DC Aux 電源ポート（これを実装するには高度なスキルが必要であることに注意してください）。

*FIRST* はいくつかの USB 2.0 電源付きハブをテストし、Anker のものを推奨しています。このドキュメントが書かれた時点で、このハブは `Anker.com <https://www.anker.com/products/a7516>`__ から入手できました。

.. image:: images/ankerhub.jpg
   :alt: Hub with charger and cable.

Anker 4 ポート電源付きハブは、ハブを 5V 電源に接続するために使用される Micro USB ポートがあるため便利です（下図のオレンジ色の円で強調表示）。

.. image:: images/ankerpowerport.jpg
   :alt: USB Hub with Micro USB port.

This port allows a user to plug a standard USB type B Micro Cable into
the hub, and then connect the other end of the cable (which has a USB
Type A connector) into the output port of an external 5V USB battery
pack. In the image below, the Anker 4 port hub is powered by a
“limefuel” external 5V battery pack using a standard Type A to Type B
USB Micro cable. Note the battery is highlighted by the yellow outline
in the figure below.

.. figure:: images/limefuel.png
   :alt: A complete setup for using a phone and webcam.
   
   USB ハブはパワーバンクから電力を供給されています。

USB ハブは、そのタイプ A コネクタとケーブルを介して、スマートフォンに接続する OTG ケーブルに接続されています。パワーバンクは USB ハブの USB タイプ B Micro ポートに接続されています。ウェブカメラは USB ハブの USB タイプ A ポートの 1 つに接続されています。USB タイプ A から USB Mini B へのケーブルが USB ハブを REV **Expansion Hub** に接続します。

USB ハブは、REV Robotics **Expansion Hub** の 5V 補助ポートから電力を引き出すこともできます。この構成では、ユーザーが特別なケーブルを持っている必要があり、一端は 5V 補助ポートに接続でき、もう一端は USB ハブの電源ポートに接続できます。

.. figure:: images/5vauxcable.png
   :alt: :alt: A complete setup for using a phone and webcam.
   
   The USB hub is connected to the 5V Auxiliary port.

Note that teams can create this special cable using one end of a servo
extension cable (to plug into the 5V aux port) and one end of a Micro
USB cable (to plug into the Anker hub’s power port). **Creating this
cable is an advanced task and should only be attempted by teams who have
guidance from an adult mentor who has expertise in electronics and
wiring! It is extremely important that the polarity is correct for this
special cable. If the polarity is reversed it could damage your
electronic equipment.**

サンプル OpMode
^^^^^^^^^^^^^^^

外部 UVC ウェブカメラを **VisionPortal** 操作に使用する方法を示すサンプル **Blocks** および Java **OpMode** があります。チームが外部 UVC カメラを使用する前に、外部カメラを USB 接続デバイスの 1 つとして定義した構成ファイルを構成する必要があります。

有効な構成ファイルが定義されてアクティブ化されると、プログラマーは、内部 Android カメラの代わりに外部 UVC カメラをビジョン関連のタスクに使用できます。

.. image:: images/blockswebcam.png
   :alt: Sample Blocks code

