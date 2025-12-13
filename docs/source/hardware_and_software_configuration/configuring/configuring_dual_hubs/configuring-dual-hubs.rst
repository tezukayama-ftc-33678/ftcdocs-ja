Expansion Hub の追加
=======================

はじめに
~~~~~~~~~~~~

単一の **REV Robotics Control Hub**または**Expansion Hub**には、限られた数の入出力（I/O）ポートしかありません。場合によっては、利用可能なポート数よりも多くのデバイスを使用したい場合があります。このような場合、最初の Hub に**Expansion Hub** を接続して、I/O ポートを追加する必要があるかもしれません。

このドキュメントでは、FIRST Tech Challenge で使用する追加の **Expansion Hub** を接続および構成する方法について説明します。FIRST Tech Challenge
競技マニュアルは、単一のロボット上の **Control Hub**または**Expansion Hub** の最大数を 2 つに制限しています。

必要な機器
~~~~~~~~~~~~~~~~

このドキュメントの手順に従うには、次のアイテムが必要です。

.. list-table::
   :header-rows: 1
   :widths: 50 50
   :class: longtable

   * - 必要なアイテム
     - 画像

   * - **REV Robotics Driver Hub** （REV-31-1596）
     - .. figure:: images/driverHub.jpg

   * - **REV Robotics** スイッチ、ケーブル、ブラケット（REV-31-1387）
     - .. figure:: images/REVSwitch.jpg

   * - **REV Robotics** Tamiya to XT30 アダプターケーブル（REV-31-1382）
     - .. figure:: images/TamiyaAdapter.jpg

   * - **FIRST** 承認 12V バッテリー（Tetrix W39057 など）。
       **FIRST** 承認 12V バッテリーのリストについては、現在の競技マニュアルを参照してください。
     - .. figure:: images/Battery.jpg

   * - **REV Robotics Control Hub** （REV-31-1595）
     - .. figure:: images/controlHub.jpg

   * - **REV Robotics Expansion Hub** （REV-31-1153）
     - .. figure:: images/ExpansionHub.jpg

   * - **REV Robotics** （または同等品）3 ピン JST PH ケーブル（REV-35-1414、3 本パックを表示していますが 1 本のみ必要）
     - .. figure:: images/3PinJSTPH.jpg

   * - **REV Robotics** XT30 延長ケーブル（REV-31-1394）
     - .. figure:: images/xt30Extension.jpg

**Expansion Hub** の接続
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 最初のステップは、3 ピン JST PH ケーブルと XT30 ケーブルを使用して、
2 つの Hub をデイジーチェーン接続することです。これを行う前に、
どちらの Hub も電源が入っていないことを確認してください。

XT30 延長ケーブルを使用して、**Control Hub** の XT30 電源ポートを
もう一方の **Expansion Hub** の XT30 電源ポートに接続します。

.. note:: 画像はこちらに挿入予定

2. **Control Hub**と**Expansion Hub** は、デバイス間の通信に RS-485 シリアルバス標準を使用します。
3 ピン JST PH ケーブルを使用して、**Control Hub** の「RS485」とラベル付けされたポートの 1 つを、
**Expansion Hub** の「RS485」とラベル付けされたポートの 1 つに接続できます。

.. note:: 画像はこちらに挿入予定

**Expansion Hub**または**Control Hub** でどの「RS485」ポートを選択するかは重要ではありません。
どちらのポートでも機能するはずです。


.. figure:: images/RS485Port.jpg
   :align: center

3. 2 つのデバイスをデイジーチェーン接続したら（12V 電源と RS-485 信号）、
バッテリーと電源スイッチを接続し、デバイスの電源を入れることができます。

.. note:: 画像はこちらに挿入予定

両方のデバイスの構成
~~~~~~~~~~~~~~~~~~~~~~~~

**Expansion Hub**と**Control Hub** をデイジーチェーン接続できた場合、
両方のデバイスを含む新しい構成ファイルを作成できるはずです。

**注：** **Control Hub** のみを含む構成が既にある場合は、構成を編集して
「Scan」ボタンを押すことで **Expansion Hub** を追加できます。

**Driver Hub**を**Control Hub**の WiFi ネットワークに接続し、**Driver Station** アプリから
Configure Robot オプションを選択します。**New** ボタンを押して、新しい構成ファイルを作成します。
最初にハードウェアをスキャンすると、**Robot Controller**は組み込みの**Control Hub** を検出するはずです。
**Robot Controller**は、このデバイスに自動的に**Control Hub** 「Portal」とラベル付けします。
**Robot Controller** は、このポータルを介して個々の Hub と通信します。


<INSERT IMAGE>

構成画面の Portal アイテムをクリックすると、**Control Hub**と**Expansion Hub** の
両方がリストされているはずです。

<INSERT IMAGE>

この構成ファイルを保存して、**Driver Station** のメイン画面に戻ることができます。
ロボットが再起動された後、両方の Hub の LED が緑色に点灯するはずです。
**Expansion Hub** では、LED が約 5 秒ごとに青色に点滅するはずです。

おめでとうございます。**Control**と**Expansion Hub** の組み合わせを使用する準備が整いました！
これらの Hub を個々の Hub と同じように構成および操作できます。

Using Two Expansion Hubs
~~~~~~~~~~~~~~~~~~~~~~~~

**Control Hub**にアクセスできないチームは、ロボットで 2 つの**Expansion Hub** を使用できます。

Additional Equipment Needed
---------------------------

ロボットで **Control Hub** を使用していないチームには、いくつかの追加機器が必要です。

.. list-table::
   :header-rows: 1
   :widths: 50 50
   :class: longtable

   * - 必要なアイテム
     - 画像

   * - **FIRST**承認の Android スマートフォンで、**FTC Robot Controller**
       アプリがインストールされているもの。**FIRST** 承認の Android スマートフォンのリストについては、
       現在の競技マニュアルを参照してください。
     - .. figure:: images/oneAndroidPhone.jpg

   * - USB Type A オス - Type mini-B オスケーブル
     -  .. figure:: images/USBTypeACable.jpg

   * - Micro USB OTG アダプター
     - .. figure:: images/OTGAdapter.jpg
  
   * - 追加の **REV Robotics Expansion Hub** （REV-31-1153）
     - .. figure:: images/ExpansionHub.jpg

Changing the Address of an Expansion Hub
----------------------------------------

You can use the Advanced Settings menu of the Robot Controller App
to change the address of any connected Expansion Hubs.

**重要な注意：** 両方の**Expansion Hub** が同じアドレスを持っている場合、
または箱から取り出したばかりの場合（デフォルトでは、アドレスは 2 に設定されています）、
それらを接続する _前に_ 一方のアドレスを変更する必要があります。
このガイドでは、2 番目の **Expansion Hub** を接続する前に、
最初の **Expansion Hub** のアドレスを設定することを前提としています。

最初の **Expansion Hub**を 12V バッテリーと**Robot Controller** に接続した状態で、
**Robot Controller**アプリから**Settings**メニューを起動します（**DRIVER STATION** が
**Robot Controller**とペアリングされている場合は、**Driver Station** アプリからこれを行うこともできます）。

1. **Advanced Settings** アイテムを選択して、Advanced Settings メニューを表示します。

.. figure:: images/AdvancedSettings.jpg
   :align: center

2. 次に、**Expansion Hub Address Change** アイテムを選択して、
**Expansion Hub** アドレス画面を表示します。

.. figure:: images/ExpansionHubAddressChange.jpg
   :align: center

3. **Expansion Hub** の USB シリアル番号と現在割り当てられているアドレスが表示されるはずです。

**重要な注意：** 物理的に接続され、電源が入っている**Expansion Hub** が表示されない場合、
アドレスの競合がある可能性があります。これが発生した場合は、
アドレスを変更したい Hub 以外のすべての **Expansion Hub** を切断してください。

.. figure:: images/DefaultAddress.*
   :align: center

4. 右側のドロップダウンリストコントロールを使用して、**Expansion Hub** の
アドレスを変更します。現在接続されている他の **Expansion Hub** と競合するアドレスは
使用できません。

.. figure:: images/NewAddress.*
   :align: center

Push the “Done” button to change the address. You should see a message
indicating that the Expansion Hub’s address has been changed.

.. figure:: images/AddressChangeComplete.jpg
   :align: center

Connecting the Two Expansion Hubs
---------------------------------

5. Hub の 1 つのアドレスを変更した後、3 ピン JST PH ケーブルと XT30 ケーブルを使用して、
2 つの Hub をデイジーチェーン接続できます。これを行う前に、
最初の **Expansion Hub** から 12V バッテリーと電源スイッチを切断してください。

XT30 延長ケーブルを使用して、一方の **Expansion Hub** の XT30 電源ポートを
もう一方の Hub の XT30 電源ポートに接続します。

.. figure:: images/XT30ExtensionConnected.jpg
   :align: center

6. The Expansion Hubs use the RS-485 serial bus standard to communicate
between devices. You can use the 3-pin JST PH cable to connect one of
the ports labeled “RS485” on one Expansion Hub to one of the ports
labeled “RS485” on the other Expansion Hub.

.. figure:: images/RS485Connected.jpg
   :align: center

Note that it is not important which “RS485” port that you select on an
Expansion Hub. Either port should work.

.. figure:: images/RS485Port.jpg
   :align: center

7. Once you have the two devices daisy chained together (12V power and
RS-485 signal) you can reconnect the battery and power switch, and then
**Robot Controller** を接続し、デバイスの電源を入れます。

.. figure:: images/DualConnected.jpg
   :align: center

Configuring Your Expansion Hubs
-------------------------------

2 つの **Expansion Hub** をデイジーチェーン接続できた場合、
両方のデバイスを含む新しい構成ファイルを作成できるはずです。

**注：** USB 接続された**Expansion Hub** のみを含む構成が既にある場合は、
構成を編集して「Scan」ボタンを押すことで、2 番目の **Expansion Hub** を追加できます。

Connect the Robot Controller and select the Configure Robot option from
the Settings menu. Press the New button to create a new configuration
file. When you first scan for hardware, your Robot Controller should
detect the Expansion Hub that is immediately connected to the Robot
Controller via the OTG adapter and USB cable. The Robot Controller will
automatically label this device as an Expansion Hub “Portal”. The Robot
Controller will communicate through this portal to the individual Expansion
Hubs.

.. figure:: images/ExpansionHubPortal.jpg
   :align: center

構成画面の Portal アイテムをクリックすると、2 つの **Expansion Hub** がリストされているはずです。
それぞれのデフォルトのデバイス名の一部として、それぞれのアドレスが表示されます。

.. figure:: images/TwoHubsConfigured.jpg
   :align: center

You can save this configuration file and return to the main screen of
the Robot Controller. After the robot has been restarted, each Hub’s LED
should be blinking in the manner that indicates its individual address.

おめでとうございます。デュアル **Expansion Hub** を使用する準備が整いました！
これらの Hub を個々の Hub と同じように構成および操作できます。
