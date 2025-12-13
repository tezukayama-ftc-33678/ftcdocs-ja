
はじめに
========

構成ファイルの作成
------------------

**Control Hub** や **Expansion Hub** に接続されたモーター、サーボ、センサーと通信するためには、まず **Robot Controller** 上で構成ファイルを作成する必要があります。これにより、**Robot Controller** は **Control Hub** や **Expansion Hub** の外部ポートにどのハードウェアが接続されているかを認識できるようになります。

Control Hub の準備
------------------

**Control Hub** を使用する場合、追加の接続は不要です。**Control Hub** の電源が入っていて、**DRIVER STATION** とペアリングされていることを確認してください。

Android スマートフォンを Expansion Hub に接続する
-------------------------------------------------

Android スマートフォンを **Robot Controller** として使用する場合は、USB ケーブルと OTG（On-The-Go）アダプターを使って、スマートフォンを **Expansion Hub** に物理的に接続する必要があります。また、**DRIVER STATION** が現在 **Robot Controller** とペアリングされていることも確認してください。

Android スマートフォンを Expansion Hub に接続する手順
-----------------------------------------------------

1. **Expansion Hub** の電源スイッチを入れて、電源をオンにします。

.. image:: images/ConfiguringHardwareStep1.jpg
   :align: center

|

2. USB ケーブルの Type B Mini 端子を **Expansion Hub** の USB mini ポートに接続します。

.. image:: images/ConfiguringHardwareStep2.jpg
   :align: center

|

3. USB ケーブルの Type A 端子を OTG アダプターに接続します。

.. image:: images/ConfiguringHardwareStep3.jpg
   :align: center

|

4. **Robot Controller** スマートフォンの電源が入っていて、ロック解除されていることを確認します。USB Micro OTG アダプターをスマートフォンの OTG ポートに接続します。

.. image:: images/ConfiguringHardwareStep4.jpg
   :align: center

|

OTG アダプターをスマートフォンに接続すると、スマートフォンが **Expansion Hub** を検出し、**Robot Controller** アプリが起動します。

5. 初めて **Robot Controller** スマートフォンを **Expansion Hub** に接続した際、Android の OS から新しく検出された USB デバイス（**Expansion Hub** ）を **Robot Controller** アプリに関連付けてもよいか確認するメッセージが表示されます。

.. image:: images/ConfiguringHardwareStep5.jpg
   :align: center

|

.. important::
   USB ハードウェアの関連付けを求めるメッセージが複数回表示される場合があります。表示された際は、必ず「この USB デバイスにデフォルトで使用する」オプションを選択し、「OK」ボタンを押して **Robot Controller** アプリに関連付けてください。関連付けを行わないと、次回システム起動時に **Robot Controller** アプリがこの **Expansion Hub** に正常に接続できない場合があります。


DRIVER STATION を使った構成ファイルの作成
------------------------------------------

構成ファイルは **Robot Controller** に保存する必要がありますが、このチュートリアルでは **DRIVER STATION** アプリを使ってリモートで構成ファイルを作成します。**DRIVER STATION** は **Control Hub** や Android スマートフォン **Robot Controller** 用の構成ファイルを作成できます。


DRIVER STATION を使って Robot Controller に構成ファイルを作成する手順
---------------------------------------------------------------------

1. **Driver Station** アプリ右上の縦三点（︙）をタッチします。ポップアップメニューが表示されます。

.. image:: images/ConfiguringHardwareNewStep1.jpg
   :align: center

|

2. ポップアップメニューから「**Configure Robot**」を選択し、「**Configuration**」画面を表示します。

.. image:: images/ConfiguringHardwareNewStep2.jpg
   :align: center

|

3. **Robot Controller** に既存の構成ファイルがない場合、ファイル作成が必要である旨のメッセージが表示されます。

.. image:: images/ConfiguringHardwareNewStep3.jpg
   :align: center

|

「**New**」ボタンを押して、新しい構成ファイルを作成します。

4. 新しい構成画面が表示されると、**Robot Controller** アプリがシリアルバスをスキャンし、接続されているデバイスを検出します。

.. image:: images/ConfiguringHardwareStep9.jpg
   :align: center

|

検出されたデバイスは「USB Devices in configuration.」の下にリスト表示されます。「Expansion Hub Portal 1」などのエントリが表示されるはずです。

**Expansion Hub** は、USB ケーブル（スマートフォンの場合）や内部シリアルバス（**Control Hub** の場合）を通じて **Robot Controller** に直接接続されているため「Portal」として表示されます。

スマートフォンを **Robot Controller** として使用していて「Expansion Hub Portal」が表示されない場合は、配線が確実に接続されているか確認し、「Scan」ボタンを1～2回押して再スキャンしてください。

5. 「Expansion Hub Portal 1」などの Portal リストをタッチすると、その Portal に接続されている **Expansion Hub** が表示されます。

.. image:: images/ConfiguringHardwareStep10.jpg
   :align: center

|

**Expansion Hub** が1台だけ接続されている場合は、1つだけ「Expansion Hub 2」などのエントリが表示されます。

6. 「Expansion Hub 2」などの Expansion Hub リストをタッチすると、そのデバイスの入出力ポート一覧が表示されます。

.. image:: images/ConfiguringHardwareStep11.jpg
   :align: center

|

選択した **Expansion Hub** に利用可能なモーター、サーボ、センサーのポートがすべて表示されます。
