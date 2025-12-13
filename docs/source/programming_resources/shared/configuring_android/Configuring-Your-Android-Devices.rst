Androidデバイスの構成
================================

制御システムに必要な構成は何ですか？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Driver Hubの構成
^^^^^^^^^^^^^^^^^^^^^^^^

**REV Robotics Driver Hub** を **DRIVER STATION** として使用しているチームは、**REV Robotics Driver Hub** のセットアップと使用方法については、`REV Roboticsの公式ドキュメント <https://docs.revrobotics.com/duo-control/driver-hub-gs>`_ を参照してください。

Control Hubの構成
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   **DRIVER STATION** スマートフォンへの参照は、**Driver Station** （**DS** ）アプリがプリインストールされている `REV Robotics Driver Hub <https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications>`__ にも適用される場合があります。

**Control Hub** （統合されたAndroidデバイスを備えている）を使用しているチームは、**DRIVER STATION** として使用する単一のスマートフォンを構成するだけで済みます。プロセスは次のとおりです：

*  スマートフォンの名前を「<TEAM NUMBER>-DS」に変更します（<TEAM NUMBER>はチーム番号に置き換えます）。
*  **Driver Station** （**DS** ）アプリを **DRIVER STATION** デバイスにインストールします。（**DS** アプリは **REV Robotics Driver Hub** にプリインストールされています。）
*  スマートフォンを機内モードにします（WiFi無線はオンのまま）。
*  **DRIVER STATION** を **Control Hub** にペアリングします（つまり、ワイヤレスで接続します）。

.. image:: images/ControlHubAndPhone.jpg
   :align: center

|

.. important:: 最終的には、競技マニュアルに準拠するように **Control Hub** の名前を変更する必要がありますが、今のところはデフォルトの名前で **Control Hub** を使用します。**Control Hub** の管理方法（名前、パスワードなどの変更）については、:doc:`このチュートリアル <../managing_control_hub/Managing-a-Control-Hub>` で学ぶことができます。

2台のAndroidスマートフォンの構成
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2台のスマートフォンを持っており、**Control Hub** を使用していないチームは、1台のスマートフォンを **Robot Controller** として、もう1台のスマートフォンを **DRIVER STATION** として構成する必要があります。プロセスは次のとおりです：

*  1台のスマートフォンの名前を「<TEAM NUMBER>-RC」に変更します（<TEAM NUMBER>はチーム番号に置き換えます）。
*  **Robot Controller** アプリを **Robot Controller** スマートフォンにインストールします。
*  2台目のスマートフォンの名前を「<TEAM NUMBER>-DS」に変更します（<TEAM NUMBER>はチーム番号に置き換えます）。
*  **Driver Station** アプリを **DRIVER STATION** デバイスにインストールします。（**DS** アプリは **REV Robotics Driver Hub** にプリインストールされています。）
*  スマートフォンを機内モードにします（WiFi無線はオンのまま）。
*  **DRIVER STATION** を **Robot Controller** にペアリングします（つまり、ワイヤレスで接続します）。

.. image:: images/twoAndroidPhones.jpg
   :align: center

|

.. Do not change the name of the following Header title, as it's linked from elsewhere. Currently it is called "Renaming Your Smartphones".

スマートフォンの名前変更
~~~~~~~~~~~~~~~~~~~~~~~~~

**FIRST** Tech Challengeの公式ルール（R707を参照）では、スマートフォンのWi-Fi名を、チーム番号と、スマートフォンが **Robot Controller** の場合は「-RC」、**DRIVER STATION** の場合は「-DS」を含むように変更する必要があります。チームが複数のAndroidスマートフォンのセットを持っている場合は、追加のダッシュと文字（「A」、「B」、「C」など）を挿入できます。

たとえば、チームのチーム番号が9999で、チームが複数のスマートフォンのセットを持っている場合、チームは1台のスマートフォンを **Robot Controller** 用に「9999-C-RC」、もう1台のスマートフォンを **DRIVER STATION** 用に「9999-C-DS」と名付けることを決定する場合があります。「-C」は、これらのデバイスがこのチームの3番目のスマートフォンセットに属していることを示します。

**Robot Controller** スマートフォンの名前は、:ref:`ここにある <programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller:changing the name>` 手順を使用して、**RC** アプリで変更できます。また、**RC** アプリ、ペアリングされた **DS** アプリ、または接続されたラップトップから *Manage* ページで変更することもできます。完了したら ``Apply Wi-Fi Settings`` をクリックしてください。

**DRIVER STATION** デバイスの名前は、:ref:`ここにある <programming_resources/shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station:changing the name>` 手順を使用して、**DS** アプリで変更できます。

または、以下に説明するように、Androidシステムレベルでデバイス名を変更することもできます。

.. note:: このタスクを完了するには、スマートフォンごとに約5分かかります。

.. |rename1| image:: images/RenameStep1.jpg
.. |rename2| image:: images/RenameStep2.jpg
.. |rename3| image:: images/RenameStep3.jpg
.. |rename4| image:: images/RenameStep4.jpg
.. |rename5| image:: images/RenameStep5.jpg
.. |rename6| image:: images/RenameStep6.jpg
.. |rename7| image:: images/RenameStep7.jpg
.. |rename8| image:: images/RenameStep8.jpg

.. list-table::
   :widths: 50 50
   :header-rows: 0
   :class: longtable


   * - 手順
     - 画像

   * - 1. スマートフォンで利用可能なアプリのリストを参照し、**Settings** アイコンを見つけます。**Settings** アイコンをクリックして、Settings画面を表示します。
     - |rename1|

   * - 2. **Wi-Fi** をクリックして、Wi-Fi画面を起動します。
     - |rename2|

   * - 3. 縦に並んだ3つのドットをタッチして、ポップアップメニューを表示します。
     - |rename3|

   * - 4. ポップアップメニューから **Advanced** を選択します。
     - |rename4|

   * - 5. **Advanced Wi-Fi** 画面から **Wi-Fi Direct** を選択します。
     - |rename5|

   * - 6. 縦に並んだ3つのドットをタッチして、ポップアップメニューを表示します。
     - |rename6|

   * - 7. ポップアップメニューから **Configure Device** を選択します。
     - |rename7|

   * - 8. タッチパッドを使用して、デバイスの新しい名前を入力します。デバイスが **Robot Controller** になる場合は、チーム番号と「-RC」を指定します。デバイスが **DRIVER STATION** になる場合は、チーム番号と「-DS」を指定します。また、Wi-Fi Directの非アクティブタイムアウトを *Never disconnect* に設定してから、**SAVE** ボタンを押して変更を保存することもできます。右に示すスクリーンショットでは、チーム番号は9999です。「-C」は、これがこのチームの3番目のスマートフォンペアからのものであることを示します。「-RC」は、このスマートフォンが **Robot Controller** になることを示します。
     - |rename8|

   * - 9. スマートフォンの名前を変更した後、デバイスの電源を入れ直します。
--------------------------------------------------------------------------


FIRST Tech Challengeアプリのインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

アプリのインストールと更新に関する詳細な手順については、以下の他のページを参照してください：

:ref:`ROBOT CONTROLLERアプリ <ftc_sdk/updating/rc_app/updating-the-rc-app:updating the robot controller (rc) app>`

:ref:`DRIVER STATIONアプリ <ftc_sdk/updating/ds_app/updating-the-ds-app:updating the driver station app>`


**2021年現在、SDKアプリ（v 6.1以降）はGoogle Playで入手できなくなりました。**

`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアを使用すると、デバイス（**REV Robotics Control Hub** 、**REV Robotics Expansion Hub** 、**REV Robotics Driver Hub** 、およびその他の承認されたAndroidデバイス）にアプリをダウンロードできます（*以下の「Androidスマートフォンでのアプリの更新」というセクションを参照*）。以下は、いくつかの利点です：

*  WiFi経由で **REV Robotics Control Hub** に接続します。
*  接続されたデバイス上のすべてのソフトウェアをワンクリックで更新します。
*  接続されたデバイスなしでソフトウェアアップデートを事前ダウンロードします。
*  **Control Hub** からユーザーデータをバックアップおよび復元します。
*  Androidデバイスに **DS** と **RC** アプリケーションをインストールして切り替えます。
*  **Control Hub** の **Robot Control** コンソールにアクセスします。

アプリリリースは、`FtcRobotController GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ でも入手できます。**Robot Controller** （**RC** ）および **Driver Station** （**DS** ）スマートフォンにアプリを「サイドロード」することは可能です。ただし、このドキュメントのこのセクションには、そのような手順は含まれて** いません** 。他のドキュメントページでは、:ref:`RCアプリ <programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller:Updating the Robot Controller App>` と :ref:`DSアプリ <programming_resources/shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station:Updating the Driver Station App>` のサイドローディングについて説明しています。

REV Roboticsデバイス（REV Robotics Expansion Hub、REV Robotics Control Hub、REV Robotics Driver Hub）でのアプリとファームウェアの更新
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、REV Roboticsのデバイスにアプリ、ファームウェア、および/またはオペレーティングシステムをインストールおよび更新するために使用されます。REV Hardware Clientをインストールして実行しているPCにUSB経由でデバイスを接続するだけで、ソフトウェアが接続されたハードウェアを検出します。検出後、REV Hardware Clientは、`REV Robotics Control HubでRobot Controller（RC）アプリを更新 <https://docs.revrobotics.com/rev-hardware-client/control-hub/updating-control-hub>`__ したり、`REV Robotics Driver HubでDriver Station（DS）アプリを更新 <https://docs.revrobotics.com/rev-hardware-client/driver-hub/updating-a-driver-hub>`__ したり、`ファームウェアを更新 <https://docs.revrobotics.com/rev-hardware-client/expansion-hub/updating-expansion-hub>`__ したりできます。

Androidスマートフォンでのアプリの更新
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、`Androidスマートフォンでのアプリのインストール、アンインストール、更新 <https://docs.revrobotics.com/rev-hardware-client/android-device/installing-rc-ds-applications>`__ に使用されます。ただし、REV Hardware Clientソフトウェアによってスマートフォンが適切に認識および更新されるためには、スマートフォンで **Developer Options** （開発者オプション）を有効にする必要があります。Developer Optionsを有効にするプロセスは次のとおりです：

.. |devop1| image:: images/1-developer-options.jpg
.. |devop2a| image:: images/2a-developer-options.jpg
.. |devop2b| image:: images/2b-developer-options.jpg
.. |devop4| image:: images/4-developer-options.jpg
.. |devop5| image:: images/5-developer-options.*

.. list-table::
   :widths: 50 50
   :header-rows: 1
   :class: longtable

   * - 手順
     - 画像

   * - 1. 「Settings」に移動し、「About device」または「About phone」をタップします。
     - |devop1|

   * - 2. 下にスクロールして、「Build number」を7回タップします。デバイスとオペレーティングシステムによっては、「Software information」をタップしてから、「Build number」を7回タップする必要がある場合があります。
     - |devop2a|       |devop2b|

   * - 3. パターン、PIN、またはパスワードを入力して、Developer optionsメニューを有効にします。
----------------------------------------------------------------------------------------------

   * - 4. 「Developer options」メニューがSettingsメニューに表示されるようになります。デバイスによっては、Settings > General > Developer optionsの下に表示される場合があります。
     - |devop4|

   * - 5. Developer optionsをいつでも無効にするには、スイッチをタップします。
     - |devop5|


スマートフォンをWi-Fiオンの機内モードにする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**FIRST** Tech Challenge競技会では、**Robot Controller** と **DRIVER STATION** デバイスを機内モードにする一方で、Wi-Fi無線はオンのままにしておくことが重要です。これは、マッチ中に携帯電話機能を有効にしたくないためです。携帯電話機能は、マッチ中のロボットの機能を妨げる可能性があります。

.. note:: このタスクを完了するには、スマートフォンごとに約2.5分かかります。また、Androidデバイスに表示される画面は、このドキュメントに含まれる画像と若干異なる場合があることに注意してください。

.. |airplane1| image:: images/AirplaneStep1.jpg
.. |airplane2| image:: images/AirplaneStep2.jpg

.. list-table::
   :widths: 50 50
   :header-rows: 1


   * - 手順
     - 画像

   * - 1. 各スマートフォンのメインAndroid画面で、指を使って画面の上部から下部に向かってスライドして、クイック構成画面を表示します。一部のスマートフォンでは、特に画面の上部にメッセージや通知が表示されている場合、クイック構成画面を表示するために複数回下にスワイプする必要がある場合があることに注意してください。機内モードアイコン（飛行機の形をしています）を探し、アイコンがアクティブになっていない場合は、アイコンをタッチしてスマートフォンを機内モードにします。
     - |airplane1|

   * - 2. スマートフォンを機内モードにすると、Wi-Fi無線がオフになります。Wi-Fiアイコンに斜線が入っている場合（上記の手順1を参照）、Wi-Fi無線は無効になっています。クイック構成画面の **Wi-Fi** アイコンをタッチして、Wi-Fi無線を再びオンにする必要があります。
     - |airplane2|


DRIVER STATIONをRobot Controllerにペアリングする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _control-hub-users-1:

Control Hubのペアリング
^^^^^^^^^^^^^^^^^^^^^^^

**REV Robotics Control Hub** には、**Robot Controller** アプリがプリインストールされています。Androidスマートフォンに **Driver Station** を正常にインストールしたら、**Control Hub** と **DRIVER STATION** の間にセキュアなワイヤレス接続を確立します。この接続により、**DRIVER STATION** デバイスは **Robot Controller** で **Op Mode** を選択し、これらのプログラムにゲームパッド入力を送信できます。同様に、**Robot Controller** で実行されている **Op Mode** は、**DRIVER STATION** スマートフォンにテレメトリデータを送信でき、そこでドライバー用に表示できます。2つのデバイスを接続するプロセスは「ペアリング」として知られています。

.. note:: **Control Hub** には独自の内部バッテリーがありません。**Driver Station** を **Control Hub** に接続する前に、**Control Hub** を12Vバッテリーに接続する必要があります。

また、このタスクを完了するには約10分かかることに注意してください。

.. |pairing1| image:: images/PairingControlHubStep1.jpg
.. |pairing2| image:: images/PairingControlHubStep2.jpg
.. |pairing3| image:: images/PairingControlHubStep3.jpg
.. |pairing4| image:: images/PairingControlHubStep4.jpg
.. |pairing5| image:: images/PairingControlHubStep5.jpg
.. |pairing6| image:: images/PairingControlHubStep6.jpg
.. |pairing7| image:: images/PairingControlHubStep7.jpg
.. |pairing8| image:: images/PairingControlHubStep8.jpg
.. |pairing9| image:: images/PairingControlHubStep9.jpg
.. |pairing10| image:: images/PairingControlHubStep10.jpg
.. |pairing11| image:: images/PairingControlHubStep11.jpg
.. |pairing12| image:: images/PairingControlHubStep12.jpg
.. |pairing13| image:: images/PairingControlHubStep13.jpg

.. list-table::
   :widths: 50 50
   :header-rows: 1
   :class: longtable



   * - 手順
     - 画像

   * - 1. 承認された12Vバッテリーを電源スイッチ（REV-31-1387）に接続し、スイッチがオフ位置にあることを確認します。スイッチを **Control Hub** のXT30ポートに接続し、スイッチをオンにします。**Control Hub** のLEDは最初は青色になります。
     - |pairing1|

   * - 2. **Control Hub** の電源が入るまでに約18秒かかります。LEDが緑色に変わると、**Control Hub** は **Driver Station** とのペアリングの準備ができています。注：ライトは約5秒ごとに青色で点滅して、**Control Hub** が正常であることを示します。
     - |pairing2|

   * - 3. **Driver Station** デバイスで、利用可能なアプリを参照し、**FTC Driver Station** アイコンを見つけます。アイコンをタップして、**Driver Station** アプリを起動します。初めてアプリを起動するときは、アプリが正しく実行するために必要な権限をAndroidデバイスが要求する場合があることに注意してください。プロンプトが表示されたら、**Allow** を押して要求された権限を付与します。
     - |pairing3|

   * - 4. **Driver Station** アプリのメイン画面の右上隅にある縦に並んだ3つのドットをタッチします。これにより、ポップアップメニューが起動します。
     - |pairing4|

   * - 5. ポップアップメニューから **Settings** を選択します。
     - |pairing5|

   * - 6. **Settings** 画面から、**Pairing Method** を探して選択し、**Pairing Method** 画面を起動します。
     - |pairing6|

   * - 7. **Control Hub** という言葉をタッチして、この **DRIVER STATION** が **Control Hub** とペアリングすることを示します。
     - |pairing7|

   * - 8. **Settings** 画面から、**Pair with Robot Controller** を探して選択し、**Pair with Robot Controller** 画面を起動します。
     - |pairing8|

   * - 9. **Pair with Robot Controller** 画面から、**Wifi Settings** ボタンを探して押し、デバイスのAndroid WifiSettings画面を起動します。
     - |pairing9|

   * - 10. 利用可能なWiFiネットワークのリストから、**Control Hub** のワイヤレスネットワークの名前を見つけます。ネットワーク名をクリックして、ネットワークを選択します。**Control Hub** に初めて接続する場合、デフォルトのネットワーク名はプレフィックスFTC-で始まるはずです（この例ではFTC-1Ybr）。デフォルトのネットワーク名は、**Control Hub** の底面に貼られたステッカーに記載されています。
     - |pairing10|

   * - 11. プロンプトが表示されたら、**Control Hub** のWiFiネットワークのパスワードを指定し、**Connect** を押してHubに接続します。**Control Hub** ネットワークのデフォルトパスワードは ``password`` であることに注意してください。また、**Control Hub** のWiFiネットワークに正常に接続すると、**DRIVER STATION** はインターネットにアクセスできなくなることに注意してください。
     - |pairing11|

   * - 12. Hubに正常に接続したら、戻る矢印を使用して前の画面に戻ります。「Current Robot Controller:」の下にWiFiネットワークの名前が表示されるはずです。戻る矢印キーを使用してSettings画面に戻ります。次に、戻る矢印キーをもう一度押して、メインの **DRIVER STATION** 画面に戻ります。
     - |pairing12|

   * - 13. **DRIVER STATION** 画面が変更され、**Control Hub** に接続されていることが示されていることを確認します。**Control Hub** のWiFiネットワークの名前（この例ではFTC-1Ybr）が、**Driver Station** のNetworkフィールドに表示されます。
     - |pairing13|


.. _users-with-two-android-smartphones-1:

2台のAndroidスマートフォンのペアリング
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important:: **DRIVER STATION** が以前に **Control Hub** とペアリングされていて、現在Androidスマートフォン **Robot Controller** に接続したい場合は、**Robot Controller** とのペアリングを試みる前に、以前の **Control Hub** のWi-Fiネットワークを忘れ（**DRIVER STATION** のAndroid Wifi Settings画面を使用）、**DRIVER STATION** スマートフォンの電源を入れ直す必要があります。以前の **Control Hub** の電源がオンになっていて、このネットワークを忘れていない場合、**DRIVER STATION** は **Control Hub** に接続しようとし、**Robot Controller** スマートフォンに接続できない可能性があります。

Androidスマートフォンにアプリを正常にインストールしたら、2つのデバイス間にセキュアなワイヤレス接続を確立します。この接続により、**DRIVER STATION** デバイスは **Robot Controller** スマートフォンで **Op Mode** を選択し、これらのプログラムにゲームパッド入力を送信できます。同様に、**Robot Controller** スマートフォンで実行されている **Op Mode** は、**DRIVER STATION** デバイスにテレメトリデータを送信でき、そこでドライバー用に表示できます。2台のスマートフォンを接続するプロセスはペアリングとして知られています。

このタスクを完了するには約10分かかることに注意してください。

.. |pairingns1| image:: images/PairingNewStep1.jpg
.. |pairingns1b| image:: images/PairingNewStep1b.jpg
.. |pairingns2| image:: images/PairingNewStep1.jpg
.. |pairingns3| image:: images/PairingNewStep3.jpg
.. |pairingns3b| image:: images/PairingNewStep3b.jpg
.. |pairingns4| image:: images/PairingNewStep4.jpg
.. |pairingns5| image:: images/PairingNewStep5.jpg
.. |pairingns6| image:: images/PairingNewStep6.jpg
.. |pairingns7| image:: images/PairingNewStep7.jpg
.. |pairingns8| image:: images/PairingNewStep8.jpg
.. |pairingns9| image:: images/PairingNewStep9.jpg
.. |pairingns10| image:: images/PairingNewStep10.jpg
.. |pairingns11| image:: images/PairingNewStep11.jpg
.. |pairingns12| image:: images/PairingNewStep12.jpg

.. list-table::
   :widths: 50 50
   :class: longtable
   :header-rows: 1


   * - 手順
     - 画像

   * - 1. **Robot Controller** デバイスで、利用可能なアプリを参照し、**FTC Robot Controller** アイコンを見つけます。アイコンをタップして、**Robot Controller** アプリを起動します。初めてアプリを起動するときは、アプリが正しく実行するために必要な権限をAndroidデバイスが要求する場合があることに注意してください。プロンプトが表示されたら、**Allow** を押して要求された権限を付与します。
     - |pairingns1| |pairingns1b|

   * - 2. **Robot Controller** アプリが実行されていることを確認します。正しく動作している場合、**Robot Status** フィールドにはrunningと表示されるはずです。
     - |pairingns2|

   * - 3. **DRIVER STATION** デバイスで、利用可能なアプリを参照し、**FTC Driver Station** アイコンを見つけます。アイコンをタップして、**Driver Station** アプリを起動します。初めてアプリを起動するときは、アプリが正しく実行するために必要な権限をAndroidデバイスが要求する場合があることに注意してください。プロンプトが表示されたら、**Allow** を押して要求された権限を付与します。
     - |pairingns3| |pairingns3b|

   * - 4. **Driver Station** アプリのメイン画面の右上隅にある縦に並んだ3つのドットをタッチします。これにより、ポップアップメニューが起動します。
     - |pairingns4|

   * - 5. ポップアップメニューから **Settings** を選択します。
     - |pairingns5|

   * - 6. **Settings** 画面から、**Pairing Method** を探して選択し、**Pairing Method** 画面を起動します。
     - |pairingns6|

   * - 7. **Wifi Direct** モードが選択されていることを確認します。これは、この **DRIVER STATION** が別のAndroidデバイスとペアリングすることを意味します。
     - |pairingns7|

   * - 8. **Settings** 画面から、**Pair with Robot Controller** を探して選択し、**Pair with Robot Controller** 画面を起動します。
     - |pairingns8|

   * - 9. リストから **Robot Controller** の名前を見つけて選択します。選択したら、戻る矢印キーを使用してSettings画面に戻ります。次に、戻る矢印キーをもう一度押して、メインの **DRIVER STATION** 画面に戻ります。
     - |pairingns9|

   * - 10. **DRIVER STATION** がメイン画面に戻ると、**Robot Controller** への接続を初めて試みるときに、**Robot Controller** 画面にプロンプトが表示されます。**ACCEPT** ボタンをクリックして、**DRIVER STATION** からの接続リクエストを受け入れます。
     - |pairingns10|

   * - 11. **DRIVER STATION** 画面が変更され、**Robot Controller** に接続されていることが示されていることを確認します。**Robot Controller** のリモートネットワークの名前（この例では9999-C-RC）が、**DRIVER STATION** のNetworkフィールドに表示されます。
     - |pairingns11|

   * - 12. **Robot Controller** 画面が変更され、**DRIVER STATION** に接続されていることが示されていることを確認します。**Robot Controller** のメイン画面で、Network statusにはactive、connectedと表示されるはずです。
     - |pairingns12|
