スマートフォンRobot Controllerの管理
======================================

名前の変更
~~~~~~~~~~~~~~~~~

競技マニュアルに準拠するため、**Robot Controller** （**RC** ）スマートフォンの名前を変更する必要があります。

これは、以下に説明するように、**RC** アプリまたはペアリングされた **DS** アプリで行うことができます。（これらの手順は、ペアリングされた **DS** アプリから **Control Hub** の名前を変更する場合にも機能します。）

または、:ref:`デバイスの名前変更<programming_resources/shared/configuring_android/Configuring-Your-Android-Devices:renaming your smartphones>` では、スマートフォンのAndroid設定アクティビティを使用してスマートフォンの名前を変更する方法を示しています。

.. important:: **Robot Controller** の名前が変更されると、デバイス（**Driver Station** とプログラミング用ラップトップ）を新しく変更されたネットワークに再接続する必要がある場合があります。

Robot Controllerの名前を変更する手順
---------------------------------------

1. **Robot Controller** スマートフォンまたはペアリングされた **Driver Station** スマートフォンで、右上隅の3つのドットをタッチして、ポップアップメニューを表示します。

.. image:: images/touchThreeDots.jpg
   :align: center

|

2. ポップアップメニューから *Settings* メニュー項目を選択します。

.. image:: images/selectSettings.jpg
   :align: center

|

3. *ROBOT CONTROLLER SETTINGS* ページで、*Robot Controller Name* をクリックします。

.. image:: images/clickRobotControllerName.jpg
   :align: center

|

4. 新しい **Robot Controller** 名を指定し、*OK* を押して変更を受け入れます。

.. image:: images/specifyNewRobotControllerName.jpg
   :align: center

|

WiFiチャンネルの変更
~~~~~~~~~~~~~~~~~~~~~~~~~

デフォルトでは、スマートフォン **Robot Controller** は自動的に独自の動作WiFiチャンネルを選択します。ただし、デバイスの動作チャンネルを指定する必要がある場合があります。

たとえば、大規模な競技会では、会場に存在するワイヤレス干渉を避けるために、FTAが指定されたチャンネルに切り替えるように要求する場合があります。同様に、FTAが干渉やその他のワイヤレス障害のために指定されたチャンネルを監視しているため、特定のチャンネルに切り替えるように要求する場合があります。

**Robot Controller** または **Driver Station** の詳細設定メニューを使用して、動作チャンネルを変更できます。

.. warning:: すべてのAndroidスマートフォンがソフトウェアを通じてチャンネル変更をサポートしているわけではありません。ソフトウェアを通じてチャンネル変更をサポートする **FIRST** 承認のスマートフォンのリストについては、競技マニュアルを参照してください。

WiFiチャンネルを変更する手順
--------------------------------------

1. **Driver Station** が **Robot Controller** に接続されていることを確認します。

2. **Driver Station** のメイン画面の右上隅にある3つのドットをタップして、ポップアップメニューを表示し、メニューから *Settings* を選択します。

3. *Settings* 画面の *ROBOT CONTROLLER SETTINGS* セクションまで下にスクロールし、*Advanced Settings* という言葉をクリックして、*ADVANCED ROBOT CONTROLLER SETTINGS* アクティビティを表示します。

.. image:: images/clickAdvancedSettings.jpg
   :align: center

|

4. *Change Wifi Channel* リンクをクリックして、利用可能なチャンネルのリストを表示します。

.. image:: images/clickChangeWifiChannel.jpg
   :align: center

|

5. 希望する動作チャンネルを選択します。チャンネル変更が成功した場合、スマートフォンにトーストメッセージが表示されます。

.. image:: images/successChangeWifiChannel.jpg
   :align: center

|

6. Androidの戻る矢印を使用して、メインの **Driver Station** 画面に戻ります。新しい動作チャンネルが、**Robot Controller** の名前の下の Network: セクションに表示されます。

.. image:: images/operatingWifiChannel.jpg
   :align: center

|


ログファイルのダウンロード
~~~~~~~~~~~~~~~~~~~~~~~~~~

制御システムの問題をトラブルシューティングする際に、**Robot Controller** からログファイルをダウンロードすることが役立つことがよくあります。これは *Manage* ページから行うことができます。デフォルトでは、ログファイル名は *robotControllerLog.txt* です。

ログファイルをダウンロードする手順
-------------------------------------

1. ラップトップまたはChromebookがスマートフォン **Robot Controller** のProgram & Manageワイヤレスネットワークに接続されていることを確認します。ネットワークに接続されている場合、アドレス「192.168.49.1:8080」にアクセスすると、*Robot Controller Connection Info* ページが表示されるはずです：

.. image:: images/RCConnectionInfoPage.jpg
   :align: center

|

   ラップトップまたはChromebookが接続されておらず、*Robot Controller Connection Info* ページにアクセスできない場合は、以下のチュートリアルの手順を読んで、Program & Manageネットワークへの接続方法を学んでください。

   :doc:`Connecting a laptop to the Program & Manage Network <../program_and_manage_network/Connecting-a-Laptop-to-the-Program-&-Manage-Network>`

2. *Robot Controller Connection Info* ページの上部にある *Manage* リンクをクリックして、Manageページに移動します。

.. image:: images/manageLink.jpg
   :align: center

|

3. *Download Logs* ボタンをクリックして、**Robot Controller** ログファイルをダウンロードします。

.. image:: images/downloadLogs.jpg
   :align: center

|

4. **Robot Controller** ログファイルがコンピューターのDownloadsディレクトリにダウンロードされたことを確認します。


5. `Notepad++ <https://notepad-plus-plus.org/>`__ やMicrosoftのWordPadなどのテキストエディタを使用して、ログファイルの内容を開いて表示します。WindowsアプリのNotepadは、ログファイルの内容を正しく表示しないことに注意してください。

.. image:: images/notepadplusplus.jpg
   :align: center

|


Expansion Hubファームウェアの更新
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Robot Controller** スマートフォンは、USB接続を使用してスタンドアロンの **REV Robotics Expansion Hub** に接続します。**Expansion Hub** の目的は、**Robot Controller** とロボットのモーター、サーボ、センサー間の通信を容易にすることです。REV Roboticsは定期的に、**Expansion Hub** の修正と改善を含むファームウェアの新しいバージョンをリリースする場合があります。ファームウェアリリースはバイナリ（「.bin」）ファイルの形式です。

`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、USBケーブルでコンピューターに直接接続された **Expansion Hub** のファームウェアを更新できます。

または、**Expansion Hub** がUSB経由で接続された **Robot Controller** スマートフォンに接続されたラップトップまたは **Driver Station** （**DS** ）から *Manage* インターフェースを使用できます。Manageページでは、**Expansion Hub** のファームウェアをアップロードしたり、含まれているバージョンまたはアップロードされたバージョンを使用して更新したりできます。新しいファームウェアイメージは、`REV Roboticsウェブサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware#using-the-robot-controller-console>`__ から入手できます。

また、含まれているまたはアップロードされた **Expansion Hub** ファームウェアは、ペアリングされた **Driver Station** （**DS** ）アプリから **Robot Controller** の詳細設定で更新できます（以下に示します）。

これらの3つの更新方法は、RS485データワイヤを介して接続された **Expansion Hub** には適用されません。スタンドアロンの **Expansion Hub** は、直接USB接続で更新する必要があります。

Expansion Hubファームウェアを更新する手順
------------------------------------------------

1. **Robot Controller** ユーザーインターフェースの *Manage* ページで、*Select Firmware* ボタンを押して、アップロードするファームウェアファイルを選択します。

.. image:: images/selectFirmwareFile.jpg
   :align: center

|

   ファイルが正常に選択されると、*Upload* ボタンが表示されます。

2. *Upload* ボタンを押して、ファームウェアファイルをコンピューターから **Robot Controller** にアップロードします。

.. image:: images/uploadFirmwareFile.jpg
   :align: center

|

   ファイルが正常にアップロードされると、「Firmware upload complete」という言葉が表示されます。

3. **Expansion Hub** の電源がオンになっていて、新しく充電された12Vバッテリーで電源が供給されていること、および **Robot Controller** スマートフォンがUSB接続を介して **Expansion Hub** に接続されていることを確認します。更新が機能するために、**Robot Controller** はアクティブな構成ファイルに **Expansion Hub** を含める必要が** ない** ことに注意してください。

.. image:: images/ConfiguringHardwareStep4.jpg
   :align: center

|

4. **Driver Station** で、右上隅の3つのドットをタッチして、ポップアップメニューを表示します。

.. image:: images/touchThreeDots.jpg
   :align: center

|

5. ポップアップメニューから *Settings* を選択して、Settingsアクティビティを表示します。

.. image:: images/touchSettings.jpg
   :align: center

|

6. **Driver Station** で、下にスクロールして、*Advanced Settings* 項目（*ROBOT CONTROLLER SETTINGS* カテゴリの下）を選択します。

.. image:: images/selectAdvancedSettings.jpg
   :align: center

|

7. *ADVANCED ROBOT CONTROLLER SETTINGS* アクティビティで、*Expansion Hub Firmware Update* 項目を選択します。

.. image:: images/selectExpansionHubFirmwareUpdate.jpg
   :align: center

|

8. **Expansion Hub** に現在インストールされているバージョンとは異なるファームウェアファイルが正常にアップロードされた場合、**Driver Station** には現在のファームウェアバージョンと新しいファームウェアバージョンに関する情報が表示されます。*Update Expansion Hub Firmware* ボタンを押して、更新プロセスを開始します。

.. image:: images/pressUpdateExpansionHubFirmwareButton.jpg
   :align: center

|

9. ファームウェアが更新されている間、進行状況バーが表示されます。このプロセス中に **Robot Controller**/**Expansion Hub** の電源を切らないでください。更新プロセスが完了すると、**Driver Station** にメッセージが表示されます。

.. image:: images/dsUpdateComplete.jpg
   :align: center

|


Robot Controllerアプリの更新
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スマートフォンにインストールされている **Robot Controller** アプリを更新する方法を知っておくことは重要です。**FIRST** は、改善と修正、およびシーズン固有のデータと機能を含む、このアプリの新しいバージョンを定期的にリリースします。

**Robot Controller** または **Driver Station** ユーザーインターフェースを通じて、**Robot Controller** アプリのバージョン番号を確認できます。**Robot Controller** または **Driver Station** で *About* メニューオプションを選択し、*ABOUT ROBOT CONTROLLER* セクションの下のApp Version番号を確認してください。

.. image:: images/aboutRobotController.jpg
   :align: center

|

2021年現在、アプリ（v 6.1以降）はGoogle Playで入手できなくなりました。

`REV Hardware Clientソフトウェア <https://docs.revrobotics.com/rev-hardware-client/>`__ を使用すると、承認されたデバイス（**REV Control Hub** 、**REV Expansion Hub** 、**REV Driver Hub** 、および承認されたAndroidデバイス）にアプリをダウンロードできます。以下は、いくつかの利点です：

*  WiFi経由で **REV Control Hub** に接続します。
*  接続されたデバイス上のすべてのソフトウェアをワンクリックで更新します。
*  接続されたデバイスなしでソフトウェアアップデートを事前ダウンロードします。
*  **Control Hub** からユーザーデータをバックアップおよび復元します。
*  Androidデバイスに **DS** と **RC** アプリケーションをインストールして切り替えます。
*  **Control Hub** の **Robot Control** コンソールにアクセスします。

プログラミングに **Blocks** または **OnBot Java** を使用しているチームは、REV Hardware Clientを使用して **RC** スマートフォンの **Robot Controller** （**RC** ）アプリを更新できます。

このタスクを完了するには、デバイスごとに約7.5分かかることに注意してください。

または、アプリリリースは `FTCRobotController Github <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ で入手できます。**Robot Controller** APKファイルをコンピューターにダウンロードし、**RC** スマートフォンのDownloadsフォルダーに転送してから、そのファイルを開いて **RC** アプリをインストールします。このプロセスは「サイドローディング」と呼ばれます。

.. tip:: **Robot Controller** （**RC** ）アプリを更新する場合は、**Driver Station** （**DS** ）アプリも同じバージョン番号に更新する必要があります。

.. important:: **Android Studio** を使用しているチームは、REV Hardware Clientまたはサイドローディングで **RC** アプリを更新しないでください。代わりに、**Android Studio** プロジェクトフォルダーの最新バージョンに更新することで、プロジェクトをビルドして **RC** デバイスにインストールするときに **Robot Controller** アプリが更新されます。プロジェクトフォルダーの最新バージョンは `こちら <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ からダウンロードできます。

カスタムウェブカメラキャリブレーションファイルのアップロード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Robot Controller** アプリには、一般的に利用可能なさまざまなウェブカメラ用の組み込みキャリブレーション情報があります。ユーザーは独自のカスタムキャリブレーションファイルを作成し、これらのファイルを **Control Hub** にアップロードすることもできます。

キャリブレーションファイルの内容がどのようになるべきかについての注釈付きの例は、**Android Studio** プロジェクトフォルダーに含まれている *teamwebcamcalibrations.xml* というファイルにあります。
この例のキャリブレーションファイルは `こちら <https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__ にあります。

カスタムウェブカメラキャリブレーションファイルをアップロードする手順
--------------------------------------------------------------------

1. *Manage* ページで、*Select Webcam Calibration File* ボタンをクリックして、キャリブレーションファイルを選択します。

.. image:: images/selectWebcamCalibrationFile.jpg
   :align: center

|

   ファイルが正常に選択されると、*Upload* ボタンが表示されます。

2. *Upload* ボタンをクリックして、選択したファイルをアップロードします。アップロードが成功した場合、*Manage* ページにアップロードが完了したことを示すメッセージが表示されます。

.. image:: images/uploadWebcamCalibrationFileComplete.jpg
   :align: center

|
