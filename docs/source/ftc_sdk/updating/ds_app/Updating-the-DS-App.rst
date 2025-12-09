Driver Stationアプリの更新
===============================

**Driver Station App** は、**FIRST Tech
Challenge** :doc:`ソフトウェア開発キット（SDK） </ftc_sdk/overview/index>` で提供されるアプリの1つです。Driver
Stationアプリは、ロボット構成、ゲームパッドのサポート、 
セルフインスペクト、チームコードの選択と実行などの主要なインターフェースです。このアプリは
REV Driver Hubまたは承認されたAndroidスマートフォンで実行されます。

このページでは、以下のデバイスで**Driver Station**（**DS**）アプリを更新する方法を示します：


-  REV Driver Hub
-  承認されたAndroid DSスマートフォン

Driver Stationアプリを更新するこれらの方法は、
ロボットチームコードのプログラミングに使用されるプログラミング言語/環境に関係なく同じです。

.. dropdown:: REV Driver Hub上のDriver Station（DS）アプリの更新

   REV Driver Hub上のDSアプリを更新する3つの方法があります： 

   #. REV Hardware Client（RHC） 
   #. "Side loading” with APK 
   #. REV Driver Hub上のソフトウェアマネージャー

   .. dropdown:: 方法1 - REV Hardware Client（RHC） - Windowsコンピューターのみ

      REV Driver HubをRHCがインストールされて開いているWindowsコンピューターにUSB-Cデータケーブルを使用して直接接続します。
      installed and open. Use a USB-C data cable. Make sure the “Hardware” tab
      Driver Hub上のDSアプリを開く必要は **ありません**。
      

      ここでは、コンピューターをインターネットに接続する必要はありません。
      :doc:`REV Hardware Clientの更新 
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      で必要なDS更新ファイルが事前にダウンロードされているためです。

      RHCアプリは、ここに示すようにDriver Hubを認識します：

      .. figure:: images/070-RHC-recognize-DH.png
         :alt: Driver Hubの認識
         :width: 80%
         :align: center

         Driver Hubの認識

      Once recognized, click on the Driver Hub’s large icon/rectangle. The RHC app now displays
      

      .. figure:: images/075-RHC-update-DH.png
         :alt: Updating the Driver Hub
         :width: 80%
         :align: center

         Updating the Driver Hub

      Simply click the blue Update rectangle (green arrow) – done!

      The update was fast, because you had already downloaded the DS app to
      the RHC. That was noted with ’(Already Downloaded)“, to the left of the
      blue Update rectangle.

      You could have selected an **older** version of the DS app, in the
      drop-down list just above the blue Update rectangle.

      After install, drag the DS app icon from the app menu to the Driver
      Hub’s home screen, if needed.

      You may now unplug the Driver Hub from the computer, and close the RHC
      app. The updated DS app is ready to use.

   .. dropdown:: Method 2 - Side-load APK

      Here you will work directly with the Android Package or **APK file** to
      install the DS app on the Driver Hub. Any computer can be used, PC or
      Mac, old or new. This method is sometimes called “side-loading”.

      1. Connect your computer to the internet, open a web browser, and
         navigate to the `SDK github
         repository <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__.

         .. figure:: images/050-FTC-repo.png
            :alt: SDK GitHub Repo
            :width: 80%
            :align: center

            SDK GitHub Repo

         At the right side under “Releases”, click the “Latest” icon (yellow
         oval, above).

         In the next page, scroll down slightly in the “Latest” section, to the
         short list of “Assets”. Click on the file
         “FtcDriverStation-release.apk”, to download it to your computer.

         .. figure:: images/060-github-assets-DS.png
            :alt: SDK GitHub Releases
            :width: 80%
            :align: center

            SDK GitHub Releases

         At this time, you could rename the file to reflect its current version
         number. For example, ``FtcDriverStation-release-8.0.apk`` or simply
         ``DS-8.0-release.apk``. This distinguishes the file from other versions
         that might be stored later on that Driver Hub.

      2. Transfer the APK file from the computer to the Driver Hub’s Downloads
         folder. Use a USB-C data cable. When complete, you may unplug the
         Driver Hub from the computer.

      3. Uninstall the existing (obsolete) DS app, by dragging its icon to the
         Trash/Uninstall icon. Or, touch and hold the DS icon for “App info”,
         then choose Uninstall.

      4. On the Driver Hub, navigate to the Downloads folder. This can be done
         in several ways:

         -  at the main app menu (swipe up), touch the Files icon, then three
            bars at top left

         -  use the basic file manager in Settings/Storage, then touch Files

         -  use a third-party app such as FX File Explorer (from the Google Play
            Store)

         Touch the APK filename that you transferred. Respond to the prompts, to
         install the updated DS app.

         After install, drag the DS app icon from the menu to the Driver Hub’s
         home screen, if needed.

      Done! The updated DS app is now ready to use.

   .. dropdown:: Method 3 - Software Manager

      The REV Driver Hub has a built-in app called the Software Manager, which
      can automatically update the DS app (and other related software). It
      requires only an internet connection.

      5. Close all apps, and open the Driver Hub’s Wi-Fi menu (in Settings, or
         swipe down twice from top of home screen). Temporarily connect the
         Driver Hub to the internet via Wi-Fi.

      6. Open the Software Manager app at the Driver Hub home screen (left
         image, below).

         .. figure:: images/910-DH-double.png
            :alt: REV Software Manager
            :width: 80%
            :align: center

            REV Software Manager

      7. The Software Manager will automatically check for any updates needed,
         and display the results (right image, above). Click the grey box to
         update the Driver Station (DS) app, if needed.

      8. When all is complete, “Forget” the Wi-Fi network used for internet
         access. 

      Done! Now the Driver Hub is updated and ready for use. 

.. dropdown:: Updating Driver Station (DS) app on Android smartphone

   There are 2 methods to update the DS app on a DS phone:

   1. REV Hardware Client (RHC)
   2. “Side loading” with APK

   .. dropdown:: 方法1 - REV Hardware Client（RHC） - Windowsコンピューターのみ

      Plug the DS phone directly into the computer with RHC installed and
      open. Use a USB data cable, not a charge-only cable. Make sure the
      “Hardware” tab is active, at top left. The DS app on the phone does
      **not** need 

      ここでは、コンピューターをインターネットに接続する必要はありません。
      :doc:`REV Hardware Clientの更新 
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      で必要なDS更新ファイルが事前にダウンロードされているためです。

      The RHC app will recognize the phone, as shown here:

      .. figure:: images/030-RHC-recognize-phone.png
         :alt: Recognizing the Phone
         :width: 80%
         :align: center

         Recognizing the Phone

      If the phone is not recognized, ensure that the phone has :doc:`developer
      options
      </programming_resources/tutorial_specific/android_studio/enabling_developer_options/Enabling-Developer-Options>`
      enabled. If necessary, click the "Scan for Devices" button in the
      lower-left of the REV Hardware Client app to force the RHC to rescan
      devices.

      Once recognized, click on that phone’s large icon/rectangle. The RHC app
      now displays 

      .. figure:: images/040-RHC-update-DS-phone.png
         :alt: Update Status of Phone
         :width: 80%
         :align: center

         Update Status of Smartphone

      Simply click the blue Update rectangle (green arrow) – done!

      The update was fast, because you had already downloaded the DS app to
      the RHC. That was noted with ’(Already Downloaded)“, to the left of the
      blue Update rectangle.

      You could have selected an **older** version of the DS app, in the
      drop-down list just above the blue Update rectangle.

      After install, drag the DS app icon from the app menu to the phone’s
      home screen.

      You may now unplug the DS phone from the computer, and close the RHC
      app. The updated DS app is ready to use.

   .. dropdown:: Method 2 - Side-load APK

      Here you will work directly with the Android Package or **APK file** to
      install the DS app on the Android phone. Any computer can be used, PC or
      Mac, old or new. This method is sometimes called “side-loading”.

      1. Connect your computer to the internet, open a web browser, and
         navigate to the `SDK github
         repository <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__.

         .. figure:: images/050-FTC-repo.png
            :alt: SDK GitHub Repo
            :width: 80%
            :align: center

            SDK GitHub Repo

         At the right side under “Releases”, click the “Latest” icon (yellow
         oval, above).

         In the next page, scroll down slightly in the “Latest” section, to the
         short list of “Assets”. Click on the file
         “FtcDriverStation-release.apk”, to download it to your computer.

         .. figure:: images/060-github-assets-DS.png
            :alt: SDK GitHub Releases
            :width: 80%
            :align: center

            SDK GitHub Releases

         At this time, you could rename the file to reflect its current version
         number. For example, ``FtcDriverStation-release-8.0.apk`` or simply
         ``DS-8.0-release.apk``. This distinguishes the file from other versions
         that might be stored later on that DS phone.

      2. Transfer the APK file from the computer to the DS phone’s Downloads
         (or Download) folder. Use a USB data cable (not a charge-only cable).
         When complete, you may unplug the DS phone from the computer.

      3. Uninstall the existing (obsolete) DS app, by dragging its icon to a
         Trash/Uninstall icon. Or, touch and hold the DS icon for “App info”,
         then choose Uninstall.

      4. On the DS phone, navigate to the Downloads folder. This can be done
         in several ways:

         -  at the main app menu (swipe up), touch the Files icon or the
            Downloads icon (if present)

         -  use the basic file manager in Settings/Storage, then Explore or Files

         -  use a third-party app such as FX File Explorer (from the Google Play
            Store)

         Touch the APK filename that you transferred. Respond to the prompts, to
         install the updated DS app.

         After install, drag the DS app icon from the menu to the phone’s home
         screen.

      Done! The updated DS app is now ready to use.

Questions, comments and corrections to westsiderobotics@verizon.net

