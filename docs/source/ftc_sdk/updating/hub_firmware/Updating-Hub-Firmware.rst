Hubファームウェアの更新
=======================

ファームウェアは、デバイスの回路基板または電子 **ハードウェア** を制御する低レベルのソフトウェアです。:doc:`ソフトウェア開発キット（SDK） </ftc_sdk/overview/index>` が正しく動作するためには、REV Expansion HubおよびREV Control Hubでこれを更新する必要がある場合があります。

以下の5つの方法があります：

1. **REV Hardware Client** （RHC）
2. **Driver Station** アプリ
3. **Robot Controller (RC)** アプリ - RC スマートフォン上
4. コンピューター上の管理ページ
5. **Driver Station** デバイス（DS スマートフォンまたは **Driver Hub** ）上の管理ページ

.. dropdown:: 方法1 - **REV Hardware Client** （RHC） - Windows コンピューターのみ

   1. REV Control Hubの場合は、12Vロボット電源を供給します。REV Expansion Hubの場合は、
      12V電源はオプションです。

   2. REV HubをUSBデータケーブル（充電専用ではないもの）を使用して、REV Hardware Clientを実行しているコンピューターに直接接続します。Expansion Hubのポートは
      Mini USB（microではない）です。Control Hubの場合は、Mini USBポートではなく、USB-C
      ポートのみを使用してください。

   3. Hubの大きなアイコン/矩形をクリックします。「Expansion/Control Hub
      Firmware」の下に、現在のバージョンと最新バージョンの不一致がある場合は表示されます（下の黄色の楕円）。

      .. figure:: images/350-RHC-EH-firmware.png
         :alt: ファームウェアの更新
         :width: 80%
         :align: center

         ファームウェアの更新

      Control Hubの例は次のとおりです：

      .. figure:: images/400-RHC-EH-CH-firmware.png
         :alt: ファームウェアの更新
         :width: 80%
         :align: center

         ファームウェアの更新

      ドロップダウンメニューで最新バージョンを確認し、青色の「Re-install」矩形をクリックします（上の緑色の矢印）。これは迅速に実行されます。
      :doc:`REV Hardware Clientの更新 
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      で必要な更新ファイルが事前にダウンロードされているためです。

      完了です！Hubのファームウェアが更新されました。

   RHCを使用してHubファームウェアを更新する詳細については、`REV Roboticsの優れたドキュメントサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware>`__ を参照してください。

.. dropdown:: 方法2 - Driver Stationアプリ

   この方法は、DSスマートフォンまたはDriver Hubで実行されているすべてのDSアプリに適用されます。

   1. REV Control Hubの場合は、12Vロボット電源を供給します。REV Expansion Hubの場合は、
      Robot Controller（RC）スマートフォンに直接接続し、RCアプリを開き、 **さらに**
      12V電源を供給します。更新するExpansion Hubは、中間のControl Hubや
      他の（プライマリ）Expansion Hubを介さずに、RCスマートフォンに **直接接続** する必要があります。更新後、必要に応じてそのHubをセカンダリ位置に戻すことができます。

   2. DSスマートフォンまたはDriver HubからDSアプリをRCデバイスに接続/ペアリングします。DS Settings、Advanced（Robot Controller）Settings、REV
      Hub Firmware Updateを選択します。

      .. figure:: images/150-DS-firmware-double.png
         :alt: ファームウェアの更新
         :width: 80%
         :align: center

         ファームウェアの更新

      RCデバイスに保存されているHubファームウェアおよび/またはアプリに「バンドル」されているHubファームウェアの利用可能なリストを確認します。

   3. 最新版がリストに表示 **されない** 場合は、コンピューターからRobot Controllerにファームウェアファイルを転送できます。USBデータケーブル（充電専用ケーブルではない）を使用して、ファームウェアファイルをRCデバイスのFIRST/updates/Expansion Hub Firmwareというサブフォルダーに保存します。

      現在および古いファームウェアファイルは、
      `REV RoboticsのWebサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware/firmware-changelog>`__ にあります。

      次に、この利用可能なファームウェアのリストに戻ります。

   4. 最新のファームウェアバージョンを選択し、「Update Hub
      Firmware」をタッチします（上の緑色の矢印）。プロセスが完了するまで待ちます。Hubのプラグを抜いたり、ロボットを再起動したりしないでください。

   以上です！Hubのファームウェアが更新されました。

.. dropdown:: 方法3 - Robot Controller（RC）アプリ - RCスマートフォン上

   この方法は、上記の方法2と **全く同じ** です。
   DSアプリは単にRCアプリへのポータルまたはウィンドウを提供していたためです。

   ここに個別にリストされているのは、Control Hubには適用されず、**Expansion
   Hub** にのみ適用されるためです。Control HubはRCスマートフォンを使用しません。つまり、
   ユーザーは通常、Control Hub上のRCアプリと直接インターフェースすることはありません。

   繰り返しになりますが、Expansion Hubは、中間（プライマリ）Expansion Hubを介さずに、RCスマートフォンに **直接** 接続する必要があります。更新後、必要に応じてそのHubをセカンダリ位置に戻すことができます。

.. dropdown:: 方法4 - コンピューター上の管理ページ

   1. コンピューターをWi-Fi経由でControl HubまたはRCスマートフォンに接続します。Chromeブラウザで管理インターフェースを開きます。

   2. Manageタブをクリックし、Update REV Hub Firmwareまでスクロールします。

      .. figure:: images/250-manage-firmware.png
         :alt: ファームウェアの更新
         :width: 80%
         :align: center

         ファームウェアの更新

      グレーのボックス（上の緑色の矢印を参照）が、RCアプリに含まれている、またはバンドルされている最新のファームウェアバージョンを提供しているかどうかを確認します。

   3. そうでない場合は、「Select Firmware…」ボックスをクリックします。コンピューターに保存されている目的のファームウェアファイルに移動し、選択します。

      更新プロセスの一環として、選択したファームウェアファイルは、FIRST/updates/Expansion Hub Firmwareというサブフォルダーに、Control HubまたはRCスマートフォンに保存されます。

      現在および古いファームウェアファイルは、
      `REV RoboticsのWebサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware/firmware-changelog>`__ にあります。

   4. 「Update to…」または「Update using…」というボックスをクリックします（上の緑色の矢印を参照）。

      .. figure:: images/255-manage-firmware-confirm.png
         :alt: ファームウェアの管理
         :width: 80%
         :align: center

         ファームウェアの管理

   5. 確認プロンプトで、青色のボックス「Update Hub Firmware」をクリックします。
      プロセスが完了するまで待ちます。Hubのプラグを抜いたり、ロボットを再起動したりしないでください。

   以上です！Hubのファームウェアが更新されました。

.. dropdown:: 方法5 - Driver Stationデバイス上の管理ページ - DSスマートフォンまたはDriver Hub

   1. DSアプリのSettingsメニューから（Android デバイスのWi-Fi設定では決して使用しない）、DSアプリをControl HubまたはRCスマートフォンに接続します。

   2. DSアプリのメニューから、「Program and Manage」を選択します。次に、右上の3本のバーをタッチし、「Manage」を選択します。

      これは、ラップトップブラウザに表示されるのと同じ管理ページです。したがって、以下の手順は上記の方法4と類似しています。

   3. Update REV Hub Firmwareまでスクロールします。

      .. figure:: images/270-manage-firmware-DS-CH-landscape.png
         :alt: Hubファームウェアの更新
         :width: 80%
         :align: center

         Hubファームウェアの更新

      グレーのボックス「Update to…」が、DSアプリに含まれている、またはバンドルされている最新のファームウェアバージョンを提供しているかどうかを確認します。

   3. そうでない場合は、目的のファームウェアファイルを **Driver
      Stationデバイス** に転送できます。

      はい、それは正しいです：RCデバイスではなく、DSデバイスに転送します。
      この方法5では、DSデバイス上のローカルファイルを使用しますが、方法2および3
      （上記）では、RCデバイス上のローカルファイルを使用します。

      USBデータケーブル（充電専用ケーブルではない）を使用して、ファームウェアファイルをDSデバイスのDownloadsフォルダーに保存します。

      現在および古いファームウェアファイルは、REV Robotics
      のWebサイトの
      `こちら <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware/firmware-changelog>`__ にあります。

      次に、「Select Firmware…」ボックスをクリックします。DSデバイスの
      Downloadsフォルダーに移動し、目的のファームウェアファイルを選択します。

   4. 「Update to…」または「Update using…」というボックスをクリックします（上の2番目の緑色の矢印）。

      .. figure:: images/257-manage-firmware-confirm-DS.png
         :alt: Hubファームウェアの更新
         :width: 80%
         :align: center

         Hubファームウェアの更新

   5. 確認プロンプトで、下にスクロールして青色のボックス「Update Hub Firmware」をクリックします。プロセスが完了するまで待ちます。Hubのプラグを抜いたり、ロボットを再起動したりしないでください。

   以上です！Hubのファームウェアが更新されました。

質問、コメント、修正は westsiderobotics@verizon.net まで

