外部 UVC カメラと電源付き USB ハブの構成
==========================================================

はじめに
------------

競技マニュアルでは、コンピュータービジョン関連のタスクに USB Video Class（UVC）互換カメラの使用を許可しています。Android スマートフォンを **Robot Controller** として使用しているチームは、コンピュータービジョンタスクに内蔵カメラの代わりに外部接続カメラを使用するオプションがあります。

The advantage of using an external camera is that the camera can be
mounted in a location that is convenient for vision-related tasks while
Android **Robot Controller** は、**Robot Controller** 関連のタスクに便利な場所に取り付けることができます。

外部カメラを使用する欠点は、USB 接続カメラによって追加の複雑さが導入されることです。外部カメラは、ロボットにコストと重量を追加し、正しく動作するために正しく配線する必要があります。

どのタイプの外部カメラを使用できますか？
-----------------------------------------

システムは UVC カメラをサポートしています。理論的には、カメラが UVC 準拠であれば、システムで動作するはずです。ただし、*FIRST* Tech Challenge ソフトウェアでテストされ、このソフトウェアで正確に動作するようにキャリブレーションされた推奨ウェブカメラがいくつかあります。

-  Logitech HD Webcam C310
-  Logitech HD Pro Webcam C920

チームが使用できる :doc:`その他の UVC ウェブカメラ <../../../apriltag/vision_portal/visionportal_webcams/visionportal-webcams>` に関する注記があります。

UVC カメラのキャリブレーションは高度なタスクであることに注意してください。キャリブレーションファイルの作成方法の詳細は、ftc_app プロジェクトフォルダーの一部として利用可能な *teamwebcamcalibrations.xml* ファイルのコメントにあります（ファイルのオンラインコピーについては、この `リンク <https://github.com/ftctechnh/ftc_app/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__ にアクセスしてください）。

REV Expansion Hub and Phone
---------------------------

For teams using an Android phone and an Expansion Hub you are required to add a USB Hub to use a webcam.

.. image:: images/uvcdiagram.png
   :alt: A REV expansion hub connected to an Android phone and a webcam via a USB Hub.

USB Hub
^^^^^^^

Teams who would like to use an external camera will need a USB hub to
connect their Android Robot Controller to the external camera and the
REV Robotics Expansion Hub. To work properly, the USB hub should meet
the following requirements:

1. Compatible with USB 2.0. Note: a USB 3.0 hub will still work, just not at the faster speed.
2. Supports a data transfer rate of 480Mbps.

Note that the Modern Robotics Core Power Distribution Module cannot be
used for this task since its data transfer speed is not fast enough to
work with the USB-connected webcam.

Also note that the Competition Manual permits the use of a powered USB
hub to make this connection. If a
team uses a powered USB hub, the power to operate the USB hub can only
come from either of the following sources:

1. An externally connected commercially available off-the-shelf (COTS) USB Battery Pack in compliance with the
   Competition Manual. 
2. The 5V DC Aux power port of a REV Robotics Expansion Hub (note that
   this requires advanced skills to implement).

*FIRST* has tested a few USB 2.0 powered hubs and recommends one from
Anker. At the time this document was written, this hub was available
from `Anker.com <https://www.anker.com/products/a7516>`__.

.. image:: images/ankerhub.jpg
   :alt: Hub with charger and cable.

The Anker 4-port powered hub is convenient because it has a Micro USB
port that is used to connect the hub to a 5V power source (highlighted
with orange circle in figure below).

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
   
   The USB hub is drawing power from a power bank.

The USB hub is connected via it's Type A connector and cable to an OTG cable which connects to the phone.
The power bank is connected to the USB type B Micro port on the USB hub.
The webcam is connected to one of the USB type A ports on the USB hub.
A USB Type A to USB Mini B cable connects the USB hub to the REV Expansion Hub.

A USB hub can also draw power from the 5V auxiliary ports on the REV
Robotics Expansion Hub. This configuration requires that the user have a
special cable that on one end can be plugged into the 5V Auxiliary port
and on the other end can be plugged into the power port of the USB hub.

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

Sample Op Modes
^^^^^^^^^^^^^^^

There are sample Blocks and Java Op Modes that demonstrate how to use
the external UVC web camera for VisionPortal operations. Before
a team can use the external UVC camera, a configuration file must be
configured with the external camera defined as one of the USB-connected
devices.

Once a valid configuration file has been defined and activated, the
programmer can use the external UVC camera, instead of the internal
Android cameras, for vision-related tasks.

.. image:: images/blockswebcam.png
   :alt: Sample Blocks code

