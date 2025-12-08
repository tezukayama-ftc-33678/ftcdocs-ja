Control Hub ポート
=================

.. figure:: images/CH-HUB.png
    :align: center
    :alt: REV Control Hub

    Part number REV-31-1595

.. include:: std-ports.rst


.. figure:: images/CH-HUB-FRONT.png
    :align: center
    :alt: The ports from left to right are: USB 2.0, USB 3.0, USB C, USB Mini (below the USB C port),  HDMI, and Micro SD.

    Control Hub フロントポート

USB ポート
---------

Universal Serial Bus（USB）は、多くの種類の電子機器間でデータ交換と電力供給を可能にする業界標準です。**Control Hub** には、以下に説明する4つの USB ポートがあります。

USB 2.0 と USB 3.0 は、データ交換速度と電力供給に関連する USB 仕様を指します。

USB Type-A、USB-C、USB Mini-B は、コネクタのタイプを指します。

- USB Type-A は、より大きな長方形のコネクタです。
- USB-C は、より小さな楕円形のコネクタです。
- USB Mini-B は、面取りされた端を持つより小さな長方形のコネクタです。

USB 2.0
^^^^^^^

これは、USB 2.0 を実装する メス USB Type-A ポートであり、競技マニュアルで許可されている USB デバイスの接続に使用できます。

.. warning:: Control Hub の USB 2.0 ポートでの静電気放電（ESD）イベントは、Wi-Fi 切断を引き起こす可能性があります。

   REV Control Hub には、USB 2.0 ポートに接続されたデバイスに関する `既知の ESD 問題 <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system#esd-mitigation-techniques>`_ があります。USB 2.0 ポートを使用すると、ESD が Control Hub の Wi-Fi チップに影響を与える可能性があります（Driver Hub との Wi-Fi 切断を引き起こします）。カメラなどの USB デバイスは、Control Hub の USB 3.0 ポートに接続してください。

USB 3.0
^^^^^^^

これは、USB 3.0 を実装する メス USB Type-A ポートであり、主に USB ビデオデバイスクラス（UVC）カメラ（ウェブカメラ）の接続に使用されます。

USB C
^^^^^

A Control Hub has a female USB-C port that implements USB 2.0. This is primarily used for connecting to a
laptop for loading the SDK but can also be used with a UVC Camera.

MINI USB
^^^^^^^^

This is a female USB Mini-B port that implements USB 2.0. It is used only to communicate directly to
the I/O system. In this case, it is only for the purpose of uploading firmware
to the device.

HDMI
-----

The Control Hub lacks a display of its own even though it is a fully-fledged
Android device. The Control Hub has an HDMI port that provides video output for
the device; this HDMI port can be used to connect to an external display.

MICRO SD
--------

This is a port for a Micro SD memory card. It is not normally used.
