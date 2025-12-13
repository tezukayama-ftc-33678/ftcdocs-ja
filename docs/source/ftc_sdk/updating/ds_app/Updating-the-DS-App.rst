Driver Stationアプリの更新
===============================

**Driver Station App**は、**FIRST Tech Challenge**:doc:`ソフトウェア開発キット（SDK） </ftc_sdk/overview/index>` で提供されるアプリの1つです。**Driver Station**アプリは、ロボット構成、ゲームパッドのサポート、セルフインスペクト、チームコードの選択と実行などの主要なインターフェースです。このアプリは**REV Driver Hub** または承認されたAndroidスマートフォンで実行されます。

このページでは、以下のデバイスで**Driver Station**（**DS** ）アプリを更新する方法を示します：

-  **REV Driver Hub**
-  承認されたAndroid DSスマートフォン

**Driver Station** アプリを更新するこれらの方法は、ロボットチームコードのプログラミングに使用されるプログラミング言語/環境に関係なく同じです。

.. dropdown:: REV Driver Hub上のDriver Station（DS）アプリの更新

   **REV Driver Hub** 上のDSアプリを更新する3つの方法があります：

   #. REV Hardware Client（RHC）
   #. APKを使用した「サイドローディング」
   #. REV Driver Hub上のソフトウェアマネージャー

   .. dropdown:: 方法1 - REV Hardware Client（RHC） - Windowsコンピューターのみ

      **REV Driver Hub**をRHCがインストールされて開いているWindowsコンピューターにUSB-Cデータケーブルを使用して直接接続します。左上の「Hardware」タブがアクティブであることを確認してください。**Driver Hub**上のDSアプリを開く必要は** ありません** 。

      ここでは、コンピューターをインターネットに接続する必要はありません。
      :doc:`REV Hardware Clientの更新 
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      で必要なDS更新ファイルが事前にダウンロードされているためです。

      RHCアプリは、ここに示すように**Driver Hub** を認識します：

      .. figure:: images/070-RHC-recognize-DH.png
         :alt: Driver Hubの認識
         :width: 80%
         :align: center

         Driver Hubの認識

      認識されたら、**Driver Hub** の大きなアイコン/矩形をクリックします。RHCアプリは、DSアプリの更新ステータスを表示します（ある場合）。

      .. figure:: images/075-RHC-update-DH.png
         :alt: Driver Hubの更新
         :width: 80%
         :align: center

         Driver Hubの更新

      青色のUpdate矩形（緑色の矢印）をクリックするだけです – 完了です！

      RHCにDSアプリを既にダウンロードしていたため、更新は高速でした。これは、青色のUpdate矩形の左側に「(Already Downloaded)」と表示されていました。

      青色のUpdate矩形のすぐ上のドロップダウンリストで、DSアプリの **古い** バージョンを選択することもできました。

      インストール後、必要に応じて、アプリメニューからDSアプリアイコンを**Driver Hub** のホーム画面にドラッグします。

      これで、**Driver Hub** をコンピューターから取り外し、RHCアプリを閉じることができます。更新されたDSアプリは使用準備が整いました。

   .. dropdown:: 方法2 - サイドロードAPK

      ここでは、Android Package または **APKファイル**を直接操作して、**Driver Hub** にDSアプリをインストールします。PCまたはMac、新旧を問わず、どのコンピューターでも使用できます。この方法は「サイドローディング」と呼ばれることがあります。

      1. コンピューターをインターネットに接続し、Webブラウザーを開いて、`SDK GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に移動します。

         .. figure:: images/050-FTC-repo.png
            :alt: SDK GitHubリポジトリ
            :width: 80%
            :align: center

            SDK GitHubリポジトリ

         右側の「Releases」の下にある「Latest」アイコン（上の黄色の楕円）をクリックします。

         次のページで、「Latest」セクションで少し下にスクロールして、「Assets」の短いリストを表示します。ファイル「FtcDriverStation-release.apk」をクリックして、コンピューターにダウンロードします。

         .. figure:: images/060-github-assets-DS.png
            :alt: SDK GitHubリリース
            :width: 80%
            :align: center

            SDK GitHubリリース

      2. **Driver Hub** をUSB-Cデータケーブルでコンピューターに接続します。

      3. ブラウザーのファイル転送ウィンドウを使用するか、コンピューターのファイルマネージャーを使用して、ダウンロードしたAPKファイルを**Driver Hub**の**Downloads** フォルダーに転送します。

      4. **Driver Hub**で、ファイルマネージャーアプリを開き、**Downloads** フォルダーに移動します。

      5. APKファイルをタッチしてインストールプロセスを開始します。プロンプトに従ってインストールを完了します。

         .. note::
            初めてサイドローディングする場合、不明なソースからのアプリのインストールを許可する必要がある場合があります。

      6. インストール後、アプリメニューからDSアプリアイコンを**Driver Hub** のホーム画面にドラッグします。

      完了です！更新されたDSアプリは使用準備が整いました。

   .. dropdown:: 方法3 - ソフトウェアマネージャー

      **REV Driver Hub** には、ソフトウェアマネージャーと呼ばれる組み込みアプリがあり、DSアプリ（およびその他の関連ソフトウェア）を自動的に更新できます。インターネット接続のみが必要です。

      1. すべてのアプリを閉じ、**Driver Hub**のWi-Fiメニューを開きます（設定内、またはホーム画面の上部から2回スワイプダウン）。**Driver Hub** を一時的にWi-Fi経由でインターネットに接続します。

      2. **Driver Hub** のホーム画面でソフトウェアマネージャーアプリを開きます（下の左側の画像）。

         .. figure:: images/910-DH-double.png
            :alt: ソフトウェアマネージャーの更新
            :width: 80%
            :align: center

            ソフトウェアマネージャーの更新

      3. ソフトウェアマネージャーは、必要な更新を自動的にチェックし、結果を表示します（上の右側の画像）。グレーのボタンをタッチして、必要に応じてDSアプリを含む更新を実行します。

      4. すべてが完了したら、インターネットアクセスに使用したWi-Fiネットワークを「削除」します。これで、**Driver Hub** は通常の競技での使用準備が整いました。

.. dropdown:: Androidスマートフォン上のDriver Station（DS）アプリの更新

   AndroidスマートフォンでDSアプリを更新する2つの方法があります：

   1. REV Hardware Client（RHC）
   2. APKを使用した「サイドローディング」

   .. dropdown:: 方法1 - REV Hardware Client（RHC） - Windowsコンピューターのみ

      DSスマートフォンをRHCがインストールされて開いているコンピューターにUSBデータケーブルを使用して直接接続します。充電専用ケーブルではなく、USBデータケーブルを使用してください。左上の「Hardware」タブがアクティブであることを確認してください。スマートフォン上のDSアプリを開く必要は **ありません** 。

      ここでは、コンピューターをインターネットに接続する必要はありません。
      :doc:`REV Hardware Clientの更新 
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      で必要なDS更新ファイルが事前にダウンロードされているためです。

      RHCアプリは、ここに示すようにスマートフォンを認識します：

      .. figure:: images/030-RHC-recognize-phone.png
         :alt: スマートフォンの認識
         :width: 80%
         :align: center

         スマートフォンの認識

      スマートフォンが認識されない場合は、スマートフォンで :doc:`開発者オプション
      </programming_resources/tutorial_specific/android_studio/enabling_developer_options/Enabling-Developer-Options>`
      が有効になっていることを確認してください。必要に応じて、REV Hardware Clientアプリの左下にある「Scan for Devices」ボタンをクリックして、RHCにデバイスを再スキャンさせます。

      認識されたら、そのスマートフォンの大きなアイコン/矩形をクリックします。RHCアプリは更新ステータスを表示します。

      .. figure:: images/040-RHC-update-DS-phone.png
         :alt: スマートフォンの更新ステータス
         :width: 80%
         :align: center

         スマートフォンの更新ステータス

      青色のUpdate矩形（緑色の矢印）をクリックするだけです – 完了です！

      RHCにDSアプリを既にダウンロードしていたため、更新は高速でした。これは、青色のUpdate矩形の左側に「(Already Downloaded)」と表示されていました。

      青色のUpdate矩形のすぐ上のドロップダウンリストで、DSアプリの **古い** バージョンを選択することもできました。

      インストール後、アプリメニューからDSアプリアイコンをスマートフォンのホーム画面にドラッグします。

      これで、スマートフォンをコンピューターから取り外し、RHCアプリを閉じることができます。更新されたDSアプリは使用準備が整いました。

   .. dropdown:: 方法2 - サイドロードAPK

      ここでは、Android Package または **APKファイル** を直接操作して、スマートフォンにDSアプリをインストールします。PCまたはMac、新旧を問わず、どのコンピューターでも使用できます。この方法は「サイドローディング」と呼ばれることがあります。

      1. コンピューターをインターネットに接続し、Webブラウザーを開いて、`SDK GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に移動します。

         .. figure:: images/050-FTC-repo.png
            :alt: SDK GitHubリポジトリ
            :width: 80%
            :align: center

            SDK GitHubリポジトリ

         右側の「Releases」の下にある「Latest」アイコン（上の黄色の楕円）をクリックします。

         次のページで、「Latest」セクションで少し下にスクロールして、「Assets」の短いリストを表示します。ファイル「FtcDriverStation-release.apk」をクリックして、コンピューターにダウンロードします。

         .. figure:: images/060-github-assets-DS.png
            :alt: SDK GitHubリリース
            :width: 80%
            :align: center

            SDK GitHubリリース

      2. スマートフォンをUSBデータケーブルでコンピューターに接続します。充電専用ケーブルではなく、データケーブルを使用してください。

      3. ブラウザーのファイル転送ウィンドウを使用するか、コンピューターのファイルマネージャーを使用して、ダウンロードしたAPKファイルをスマートフォンの **Downloads** フォルダーに転送します。

      4. スマートフォンで、ファイルマネージャーアプリを開き、**Downloads** フォルダーに移動します。

      5. APKファイルをタッチしてインストールプロセスを開始します。プロンプトに従ってインストールを完了します。

         .. note::
            初めてサイドローディングする場合、不明なソースからのアプリのインストールを許可する必要がある場合があります。

      6. インストール後、アプリメニューからDSアプリアイコンをスマートフォンのホーム画面にドラッグします。

      完了です！更新されたDSアプリは使用準備が整いました。

質問、コメント、修正は westsiderobotics@verizon.net まで

