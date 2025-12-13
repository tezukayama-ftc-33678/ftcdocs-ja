Control Hubの管理
======================

名前の変更
~~~~~~~~~~~~~~~~~

デフォルトでは、**Control Hub** は「FTC-」で始まり、工場で割り当てられた4文字で終わる名前を持っています。競技マニュアルに準拠するため、名前を変更する必要があります。

**Control Hub**（または**Robot Controller**スマートフォン）の名前は、ペアリングされた**DS** アプリから変更できます。詳細は :ref:`名前の変更<programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller:changing the name>` を参照してください。

または、接続された **Driver Station** またはラップトップから *Manage* ページで **Control Hub** の名前を変更することもできます。以下に説明します。変更後は ``Apply Wi-Fi Settings`` をクリックしてください。

.. important:: **Control Hub**の名前を変更すると、Hubのワイヤレスネットワークの名前も変更されます。名前が変更されると、デバイス（**Driver Station** とプログラミング用ラップトップ）を新しいネットワークに接続し直す必要があります。

Control Hubの名前を変更する手順
----------------------------------

1. ラップトップまたはChromebookが **Control Hub** のProgram & Manageワイヤレスネットワークに接続されていることを確認します。ネットワークに接続されている場合、アドレス「192.168.43.1:8080」にアクセスすると、*Robot Controller Connection Info* ページが表示されるはずです：

.. image:: images/RCConnectionInfoPage.jpg
   :align: center

|

   ラップトップまたはChromebookが接続されておらず、*Robot Controller Connection Info* ページにアクセスできない場合は、以下のチュートリアルの手順を読んで、Program & Manageネットワークへの接続方法を学んでください。

   :doc:`Connecting a laptop to the Program & Manage Network <../program_and_manage_network/Connecting-a-Laptop-to-the-Program-&-Manage-Network>`

2. *Robot Controller Connection Info* ページの上部にある *Manage* リンクをクリックして、Manageページに移動します。

.. image:: images/manageLink.jpg
   :align: center

|

3. *Robot Controller Name* フィールドで名前を変更し、*Change Name* ボタンをクリックして **Control Hub** の名前を変更します。            

.. image:: images/manageLink.jpg
   :align: center

|

4. *Change Name* ボタンを押すと、ダイアログボックスが表示され、名前が変更されたこと、および新しいワイヤレスネットワークに接続して現在のページを更新する必要があることが示されます。

.. image:: images/changeNameWarning.jpg
   :align: center

|

パスワードの変更
~~~~~~~~~~~~~~~~~~~~~

デフォルトでは、**Control Hub**のパスワードは工場出荷時に「password」に設定されています。**Control Hub** の使用を開始する前に、パスワードをデフォルト値から変更することをお勧めします。

**Control Hub**のProgram & ManagementページにHubに接続されたラップトップまたはChromebookを使用して、**Control Hub** のパスワードを変更できます。

.. warning:: 新しいパスワードを忘れないように、記憶するか、安全な場所に保管してください。**Control Hub**を管理および操作するには、このパスワードが必要です。また、パスワードが変更されると、デバイス（**Driver Station** とプログラミング用ラップトップ/Chromebook）を新しいパスワードを使用してネットワークに再接続する必要があることに注意してください。

Control Hubのパスワードを変更する手順
--------------------------------------

1. **Control Hub** ユーザーインターフェースの *Manage* ページで、ページの *Access Point Password* セクションに新しいパスワードを指定し、この新しいパスワードを確認します。*Change Password* ボタンを押してパスワードを変更します。

.. image:: images/changePassword.jpg
   :align: center

|

2. *Change Password* ボタンを押すと、ダイアログボックスが表示され、パスワードが変更されたこと、および新しいパスワードを使用してワイヤレスネットワークに再接続する必要があることが示されます。

.. image:: images/changePasswordWarning.jpg
   :align: center

|

Control Hubのリセット
~~~~~~~~~~~~~~~~~~~~~~~

**Control Hub** のネットワーク名またはパスワードを忘れた場合、Hubの名前とパスワードを工場出荷時のデフォルト値にリセットできます。

.. important:: **Control Hub**をリセットすると、デフォルトのネットワーク名とパスワードが復元されます。ただし、既存の構成ファイルと**Op Mode**はリセットの影響を受けません。これには、**Blocks**、**OnBot Java**、および**Android Studio**ツールを使用して作成された**Op Mode** が含まれます。

リセット手順
-----------------------

1. **Control Hub** の電源を5秒間オフにします。
2. **Control Hub** のボタンを押し続けます（下の画像を参照）。

.. image:: images/controlHubButton.jpg
   :align: center

|

3. ボタンを押し続けながら、**Control Hub**の電源を入れます。**Control Hub** が再起動している間、LEDを監視します。最終的に、LEDは青色の点灯から、複数色の点滅パターンに切り替わります。

   リセットが開始されると、LEDは紫、黄、青、赤の順に点滅します。このパターンは5回連続して高速に発生します。
   
   複数色の点滅パターンが完了したら、ボタンを離すことができます。**Control Hub** のネットワーク名とパスワードが工場出荷時の値に復元されます。再起動とリセットのプロセスは、完了するまでに約30秒かかることに注意してください。

WiFiチャンネルの変更
~~~~~~~~~~~~~~~~~~~~~~~~~

**Control Hub**は、**Driver Station**とプログラミング用ラップトップまたはChromebook用のワイヤレスアクセスポイントとして機能します。デフォルトでは、**Control Hub** は動作するWiFiチャンネルを自動的に選択します。ただし、Hubの動作チャンネルを指定する必要がある場合があります。

たとえば、大規模な競技会では、会場に存在するワイヤレス干渉を避けるために、FTAが指定されたチャンネルに切り替えるように要求する場合があります。同様に、FTAが干渉やその他のワイヤレス障害のために指定されたチャンネルを監視しているため、特定のチャンネルに切り替えるように要求する場合があります。

*Manage* ページから **Control Hub** の動作チャンネルを選択できます。

WiFiチャンネルを変更する手順
--------------------------------------

1. **Control Hub** ユーザーインターフェースの *Manage* ページで、ドロップダウンセレクターを使用して、希望する動作チャンネルを選択します。**Control Hub** は2.4 GHzと5 GHzの両方のバンドをサポートしていることに注意してください。

.. image:: images/selectChannel.jpg
   :align: center

|

2. *Change Channel* ボタンを押して、新しいチャンネルに変更します。チャンネル変更が発生すると、**Driver Station**が**Control Hub**から一時的に切断される場合があることに注意してください。ただし、最終的には**Control Hub** のワイヤレスネットワークに再接続されます。

3. **Driver Station**で、**Control Hub**が希望するWiFiチャンネルで動作していることを確認します。動作チャンネルは、メインの**Driver Station** 画面の *Network* セクションのネットワーク名の下に表示されます。

.. image:: images/dsOperatingChannel.jpg
   :align: center

|

ログファイルのダウンロード
~~~~~~~~~~~~~~~~~~~~~~~~~~

制御システムの問題をトラブルシューティングする際に、**Control Hub** からログファイルをダウンロードすることが役立つことがよくあります。これは *Manage* ページから行うことができます。デフォルトでは、ログファイル名は *robotControllerLog.txt* です。

ログファイルをダウンロードする手順
-------------------------------------

1. **Control Hub** ユーザーインターフェースの *Manage* ページで、*Download Logs* ボタンを押して、**Robot Controller** ログファイルをダウンロードします。

.. image:: images/downloadLogs.jpg
   :align: center

|

2. **Robot Controller** ログファイルがコンピューターのDownloadsディレクトリにダウンロードされたことを確認します。

3. `Notepad++ <https://notepad-plus-plus.org/>`__ やMicrosoftのWordPadなどのテキストエディタを使用して、ログファイルの内容を開いて表示します。WindowsアプリのNotepadは、ログファイルの内容を正しく表示しないことに注意してください。

.. image:: images/notepadplusplus.jpg
   :align: center

|

Expansion Hubファームウェアの更新
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control Hub**には、独自の組み込み**REV Robotics Expansion Hub**があります。**Expansion Hub**ボードの目的は、**Control Hub**のAndroidコントローラーとロボットのモーター、サーボ、センサー間の通信を容易にすることです。REV Roboticsは定期的に、**Expansion Hub** の修正と改善を含むファームウェアの新しいバージョンをリリースします。ファームウェアリリースはバイナリ（.bin）ファイルの形式です。

`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、**Control Hub**の組み込み**Expansion Hub** のファームウェアを更新できます。

または、接続されたラップトップまたは **Driver Station**（**DS** ）アプリから *Manage* インターフェースを使用して、**Control Hub** のファームウェアをアップロードしたり、含まれているバージョンまたはアップロードされたバージョンを使用して更新したりできます。新しいファームウェアイメージは、`REV Robotics ウェブサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware#using-the-robot-controller-console>`__ から入手できます。

また、含まれているまたはアップロードされた **Control Hub**ファームウェアは、ペアリングされた**Driver Station**（**DS**）アプリから**Robot Controller** の詳細設定で更新できます（以下に示します）。

これらの3つの方法は、RS485データワイヤを介して **Control Hub**に接続された**Expansion Hub**のファームウェアを更新する場合には適用されません。スタンドアロンの**Expansion Hub**は、REV Hardware Clientを実行しているラップトップまたは**Robot Controller** スマートフォンに直接USB接続して更新する必要があります。

Expansion Hubファームウェアのアップロードと更新
-------------------------------------------------

1. **Control Hub** ユーザーインターフェースの *Manage* ページで、*Select Firmware* ボタンを押して、アップロードするファームウェアファイルを選択します。

.. image:: images/notepadplusplus.jpg
   :align: center

|

   ファイルが正常に選択されると、*Upload* ボタンが表示されます。

2. *Upload* ボタンを押して、ファームウェアファイルをコンピューターから **Control Hub** にアップロードします。

.. image:: images/uploadFirmwareFile.jpg
   :align: center

|

   ファイルが正常にアップロードされると、「Firmware upload complete」という言葉が表示されます。

3. **Driver Station** で、右上隅の3つのドットをタッチして、ポップアップメニューを表示します。

.. image:: images/touchThreeDots.jpg
   :align: center

|

4. ポップアップメニューから *Settings* を選択して、Settings アクティビティを表示します。

.. image:: images/touchSettings.jpg
   :align: center

|

5. **Driver Station** で、下にスクロールして、*Advanced Settings* 項目（*ROBOT CONTROLLER SETTINGS* カテゴリの下）を選択します。

.. image:: images/selectAdvancedSettings.jpg
   :align: center

|

6. *ADVANCED ROBOT CONTROLLER SETTINGS* アクティビティで、*Expansion Hub Firmware Update* 項目を選択します。

.. image:: images/selectExpansionHubFirmwareUpdate.jpg
   :align: center

|

7. **Expansion Hub**に現在インストールされているバージョンとは異なるファームウェアファイルが正常にアップロードされた場合、**Driver Station** には現在のファームウェアバージョンと新しいファームウェアバージョンに関する情報が表示されます。*Update Expansion Hub Firmware* ボタンを押して、更新プロセスを開始します。

.. image:: images/pressUpdateExpansionHubFirmwareButton.jpg
   :align: center

|

8. ファームウェアが更新されている間、進行状況バーが表示されます。このプロセス中に **Control Hub**/**Expansion Hub**の電源を切らないでください。更新プロセスが完了すると、**Driver Station** にメッセージが表示されます。

.. image:: images/dsUpdateComplete.jpg
   :align: center

|

Robot Controllerアプリの更新
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Control Hub**にインストールされている**Robot Controller**アプリを更新する方法を知っておくことは重要です。**FIRST** は、改善と修正、およびシーズン固有のデータと機能を含む、このアプリの新しいバージョンを定期的にリリースします。

**Driver Station**ユーザーインターフェースを通じて、**Robot Controller**アプリのバージョン番号を確認できます。**Driver Station** で *About* メニューオプションを選択し、*ABOUT ROBOT CONTROLLER* セクションの下のApp Version番号を確認してください。

.. image:: images/aboutRobotController.jpg
   :align: center

|

`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、**Control Hub**の**Robot Controller**（**RC** ）アプリを更新できます。

または、**Control Hub**ユーザーは、**FIRST Tech Challenge**`Githubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ から**RC** アプリをダウンロードし、*Manage* ページを使用して更新を完了できます。

**Android Studio**ユーザーの場合は、**Android Studio**プロジェクトフォルダーの最新バージョンに更新することで、プロジェクトをビルドして**Control Hub**にインストールするときに**Robot Controller** アプリが更新されます。

.. tip:: **Robot Controller**を更新する場合は、**Driver Station** ソフトウェアも同じバージョン番号に更新する必要があります。

Robot Controllerアプリを更新する手順
----------------------------------------------

1. `GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ にアクセスします。

2. *FtcRobotController-release.apk* ファイルを見つけます。

.. image:: images/apkFolderOnRepo.jpg
   :align: center

|

3. ファイル名（または *Download* ボタン）をクリックして、**Robot Controller** アプリをAPKファイルとしてコンピューターにダウンロードします。

.. image:: images/downloadRobotControllerAPK.jpg
   :align: center

|

4. *Manage* ページで、*Select App* ボタンをクリックして、**Control Hub**にアップロードする**Robot Controller** アプリを選択します。

.. image:: images/downloadRobotControllerAPK.jpg
   :align: center

|
  
   APKファイルが正常に選択されると、*Update* ボタンが表示されます。

5. *Update* ボタンをクリックして、更新プロセスを開始します。

.. image:: images/uploadRobotControllerPleaseWait.jpg
   :align: center

|

6. 更新プロセス中に、**Control Hub** がインストールされるAPKのデジタル署名が既にインストールされているAPKのデジタル署名と異なることを検出した場合、Hubは現在のアプリをアンインストールして新しいアプリに置き換えてもよいかを尋ねるプロンプトを表示する場合があります。
   
   このデジタル署名の違いは、たとえば、以前のバージョンのアプリが **Android Studio** を使用してビルドおよびインストールされたが、新しいアプリがGitHubリポジトリからダウンロードされた場合に発生する可能性があります。
   
   *OK* を押して、古いアプリをアンインストールし、更新プロセスを続行します。

.. image:: images/uploadRobotControllerWarning.jpg
   :align: center

|

7. 更新プロセスで以前のバージョンの **Robot Controller**アプリをアンインストールする必要があった場合、**Control Hub**のネットワーク名とパスワードは工場出荷時の値にリセットされます。この場合、工場出荷時のデフォルト値を使用して、コンピューターを**Control Hub** に再接続する必要があります。

.. image:: images/uploadRobotControllerUninstalling.jpg
   :align: center

|

8. 更新プロセスが完了し、コンピューターが **Control Hub** のネットワークに正常に再接続されると、*Manage* ウェブページに *installed successfully* メッセージが表示されます。

.. image:: images/uploadRobotControllerInstalledSuccessfully.jpg
   :align: center

|

カスタムウェブカメラキャリブレーションファイルのアップロード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Robot Controller**アプリには、一般的に利用可能なさまざまなウェブカメラ用の組み込みキャリブレーション情報があります。ユーザーは独自のカスタムキャリブレーションファイルを作成し、これらのファイルを**Control Hub** にアップロードすることもできます。

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

Control Hub OSの更新
~~~~~~~~~~~~~~~~~~~~~~~~~~~

REV Roboticsは、**Control Hub** オペレーティングシステム（OS）の新しいバージョンを定期的にリリースします。これらの新しいバージョンには、修正、改善、および新機能が組み込まれています。

**Driver Station**ユーザーインターフェースを通じて、**Control Hub**OSのバージョン番号を確認できます。**Driver Station** で *About* メニューオプションを選択し、*ABOUT ROBOT CONTROLLER* セクションの下のOperating System Version番号を確認してください。

.. image:: images/aboutRobotControllerOSVersion.jpg
   :align: center

|

`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、**Control Hub** オペレーティングシステムを更新できます。

または、**Control Hub**ユーザーは、REV Roboticsウェブサイトから新しい**Control Hub** OSファイルをダウンロードし、*Manage* ページを使用してOSの更新を完了できます。

Control Hub OSを更新する手順
----------------------------------------

1. `REV Roboticsウェブサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system>`__ から新しい **Control Hub** OS更新ファイルをダウンロードします。

2. *Manage* ページで、*Select Update File* ボタンをクリックして、アップロードするOS更新ファイルを選択します。

.. image:: images/selectOSUpdateFile.jpg
   :align: center

|

   更新ファイルが正常に選択されると、*Update & Reboot* ボタンが表示されます。

3. *Update & Reboot* ボタンをクリックして、更新プロセスを開始します。
OSファイルが **Control Hub**にアップロードされるまでお待ちください。ファイルが比較的大きいため、アップロードが完了するまでに数分かかる場合があることに注意してください。プロセスが進行中の間は、**Control Hub** の電源を切らないでください。

.. image:: images/osUpdatePleaseWait.jpg
   :align: center

|

4. アップロードが成功した場合、*Manage* ページにデバイスが再起動中で、更新がインストールされていることを示すメッセージが表示されます。

.. image:: images/osUpdateVerificationSucceeded.jpg
   :align: center

|

5. OS更新が完了すると、**Control Hub**LEDは青色から通常の点滅パターン（緑色、次にHubのシリアルアドレス番号を示すために1回青色で点滅し、そのパターンが繰り返されます）に戻ります。コンピューターを**Control Hub** ネットワークに再接続し、更新が成功したことを確認します。

.. image:: images/osUpdateSuccess.jpg
   :align: center

|

   **Control Hub**OSの更新されたバージョン番号を確認するには、（**Driver Station** アプリを通じて）Aboutページでも確認できます。

.. image:: images/aboutRobotControllerNewOSVersion.jpg
   :align: center

|

ワイヤレスADBを使用してControl Hubに接続する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Android Studio**を使用して**Robot Controller**アプリを**Control Hub**にビルドしてインストールする上級ユーザーは、Android Debug Bridge（**adb**）ユーティリティに精通している必要があります。**adb**は、Android開発プラットフォームツールに含まれています。**Control Hub** などのAndroidデバイスと通信するために使用できます。

従来、プログラマーは、**adb**を使用してAndroidデバイスと通信するために、有線USB接続を使用します。**adb** は、ワイヤレス接続を介してコマンドを送受信するモードもサポートしています。

**Control Hub**は、ポート5555で**adb** ワイヤレス接続リクエストを自動的にサポートするように構成されています。

ワイヤレスADBを使用してControl Hubに接続する手順
-------------------------------------------------------------

1. ラップトップが **Control Hub** のProgram & Manageワイヤレスネットワークに接続されていることを確認します。ネットワークに接続されている場合、アドレス「192.168.43.1:8080」にアクセスすると、*Robot Controller Connection Info* ページが表示されるはずです：

.. image:: images/aboutRobotControllerNewOSVersion.jpg
   :align: center

|

   ラップトップが接続されておらず、*Robot Controller Connection Info* ページにアクセスできない場合は、以下のチュートリアル（Connecting-a-Laptop-to-the-Program-&-Manage-Network）の手順を読んで、Program & Manageネットワークへの接続方法を学んでください。

   :doc:`Connecting a laptop to the Program & Manage Network <../program_and_manage_network/Connecting-a-Laptop-to-the-Program-&-Manage-Network>`

2. Windowsコンピューターのパス環境変数に、adb.exe実行可能ファイルへのパスが含まれていることを確認します。`Android Developerウェブサイト <https://developer.android.com/tools/adb>`__ には、Android SDKインストールのどこでadb.exeファイルを見つけることができるかが記載されています。`HelpDeskGeek.com <https://helpdeskgeek.com/add-windows-path-environment-variable/>`__ からの `この投稿 <https://helpdeskgeek.com/add-windows-path-environment-variable/>`__ は、Windowsのパス環境変数にディレクトリを追加する方法を示しています。

3. Windowsコマンドプロンプトを開き、「adb.exe connect 192.168.43.1:5555」と入力します。これにより、**adb**サーバーがワイヤレス接続を介して**Control Hub** に接続されます。

