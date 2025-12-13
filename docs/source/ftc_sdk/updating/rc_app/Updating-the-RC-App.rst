**Robot Controller (RC)** アプリの更新
======================================

**Robot Controller**アプリは、**FIRST** **Tech Challenge**:doc:`ソフトウェア開発キット（SDK）</ftc_sdk/overview/index>` で提供されているアプリの1つです。**Robot Controller**アプリは、**Robot Controller** **Android**デバイス（**REV Control Hub**または承認された**Android**RC スマートフォン）で実行されるアプリケーションです。このアプリは**Driver Station** アプリと通信してロボットを制御します。

このページでは、以下のデバイスで **Robot Controller (RC)** アプリを更新する方法を説明します：

-  **REV Control Hub**
-  承認された **Android** RC スマートフォン

**Blocks**/**OnBot Java**対**Android Studio**
-------------------------------------------------

**Blocks**/**OnBot Java**
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Robot Controller (RC)**アプリには、**Blocks**と**OnBot Java** のプログラミング環境が含まれており、これらの環境を使用して開発されたユーザープログラム（チームコード）は、RC アプリとは独立して、RC アプリと並行して保存されます。これにより、チームコードに影響を与えることなく、RC アプリを独立して更新することが可能になります。RC アプリ自体をアップグレード/ダウングレードするために*コード*を変更する必要がないため、RC アプリソフトウェアの更新が非常に簡単になります。ただし、これは **Blocks**と**OnBot Java**のユーザーがアプリに同梱されている「デフォルト」の RC アプリ依存関係に制限されることを意味します。ただし、**Blocks**と**OnBot Java**プログラムは**Android Studio** でビルドされた RC アプリでも実行できるため、上級ユーザーにとってはこの点でまだある程度の柔軟性があります。

**Android Studio**
^^^^^^^^^^^^^^^^^^

**Android Studio**は、一般的に正反対の動作をします。**FtcRobotController**リポジトリ（**Android Studio**プロジェクト）には、完全な RC アプリをビルドするために必要な完全なソースコードが含まれています。**Android Studio**プロジェクトがコンパイルおよびデプロイされると、実際には完全な**Robot Controller**アプリをビルドして、RC**Android**デバイスにインストールしています。チームコード** と** **Robot Controller** コードは*一緒に*コンパイルされます。つまり、チームコードは RC アプリ内に埋め込まれており、RC アプリとは独立して更新/編集することはできません。**Android Studio**でデプロイされた RC アプリが**REV Hardware Client**または類似のプロセスを使用して置き換えられた場合、チームコードが埋め込まれた RC アプリは削除され、デフォルトの RC アプリに置き換えられます。したがって、**Android Studio**ユーザーは**Android Studio**以外を使用して RC アプリを更新しないでください！ただし、これによりソフトウェアのアップグレードとダウングレードが複雑になる可能性があります。**Android Studio**コードの RC アプリ部分をアップグレード/ダウングレードするには、チームの :doc:`Android Studio プロジェクト <../../../programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub>` を、使用したい**Robot Controller**アプリのバージョンに対応する `FtcRobotController リポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ コードのソフトウェアリリースと適切にマージする必要があります。**Android Studio** の使用を決定する際には、これを慎重に検討する必要があります。

**Android Studio** 向けの RC アプリの更新
-----------------------------------------

**Android Studio**ユーザーは、上記の理由により、このページの手順を使用して RC アプリを更新** しないでください**。**Android Studio**ユーザーは、**Android Studio** プロジェクトが `SDK GitHub リポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ の希望するバージョンで最新であることを確認する必要があります。

GitHub を使用して更新できる **Android Studio** プロジェクトを適切に作成および維持する方法については、:doc:`GitHub の Fork と Clone の使用 <../../../programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub>` を参照してください。

**Blocks**/**OnBot Java** 向けの RC アプリの更新
--------------------------------------------------

これらの手順は、独立した更新がサポートされている状況、つまり **Blocks**または**OnBot Java**開発で RC アプリを独立して更新するためのものです。お使いの**Robot Controller** ハードウェアに適用される以下の手順を展開してください：

.. dropdown:: **REV Control Hub**の**Robot Controller (RC)** アプリ

   **REV Control Hub** の RC アプリを更新する方法は3つあります：

   #. REV Hardware Client (RHC)
   #. コンピューター上の Manage ページ
   #. DS スマートフォンまたは Driver Hub 上の Manage ページ

   .. note:: 
      「サイドローディング」は可能ですが、**Control Hub** では追加の機器が必要な煩雑な手順が必要なため、ここでは説明しません。

   .. dropdown:: 方法1 - REV Hardware Client - Windows コンピューターのみ

      USB データケーブルを使用して、**REV Control Hub** の USB-C ポートを Windows コンピューターに接続します。RHC の「Hardware」タブが左上でアクティブになっていることを確認してください。

      :doc:`REV Hardware Client の更新 </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>` で、必要な DS 更新ファイルが以前にダウンロードされているため、ここではコンピューターをインターネットに接続する必要はありません。

      RHC アプリは、次に示すように **Control Hub** を認識します：

      .. figure:: images/070-RHC-recognize-CH.png
         :alt: Control Hub を認識
         :width: 80%
         :align: center

         **Control Hub** を認識

      認識されたら、**Control Hub** の大きなアイコン/長方形をクリックします。RHC アプリは、RC アプリの更新ステータス（ある場合）を表示します。

      .. figure:: images/082-RHC-update-RC-CH.png
         :alt: Control Hub を更新
         :width: 80%
         :align: center

         **Control Hub** を更新

      青い Update 長方形（緑色の矢印）をクリックするだけです – 完了！
      
   .. dropdown:: 方法2 - コンピューター上の Manage ページ

      1. ラップトップをインターネットに接続し、Web ブラウザーを開いて、`SDK GitHub リポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に移動します。

         .. figure:: images/050-FTC-repo.png
            :alt: SDK GitHub リポジトリ
            :width: 80%
            :align: center

            SDK GitHub リポジトリ

         右側の「Releases」の下にある「Latest」アイコン（上の黄色の楕円）をクリックします。

         次のページで、「Latest」セクションを少し下にスクロールして、「Assets」の短いリストを表示します。「FtcRobotController-release.apk」ファイルをクリックして、コンピューターにダウンロードします。

         .. figure:: images/090-github-assets-RC.png
            :alt: SDK GitHub リリース
            :width: 80%
            :align: center

            SDK GitHub リリース

         この時点で、現在のバージョン番号を反映するようにファイルの名前を変更できます。たとえば、``FtcRobotController-release-8.0.apk``または単に``RC-8.0-release.apk`` です。これにより、その RC スマートフォンに後で保存される可能性のある他のバージョンとファイルを区別できます。

      2. **Control Hub** の電源を入れ（ロボットの電源を投入）、緑色の LED が点灯するまで待ちます。

      3. 同じラップトップを Wi-Fi 経由で **Control Hub** に接続します。Chrome ブラウザーを開き、通常のアドレス ``http://192.168.43.1:8080`` を入力します。

         Manage タブをクリックし、「Update Robot Controller App」まで下にスクロールします。

         .. figure:: images/300-manage-RC-app.png
            :alt: RC アプリを更新
            :width: 80%
            :align: center

            RC アプリを更新

         「Select App…」をクリックします。RC APK ファイルが保存されているラップトップフォルダーに移動し、そのファイルを選択します。

         次に、「Update」ボタン（上の緑色の矢印）をクリックします。

         ソフトウェアは、既存の RC アプリを新しい更新された RC アプリに置き換えます。ラップトップと **Control Hub** 間の接続は一時的に失われ、その後自動的に復元されます。

      完了メッセージが表示されたら、更新された RC アプリが使用できる状態になります。

   .. dropdown:: 方法3 - Driver Hub または DS スマートフォン上の Manage ページ

      この方法は、コンピューターが利用できない場合、または Wi-Fi 経由で **Control Hub** に接続できない場合に使用できます。たとえば、デスクトップコンピューターには有線（Ethernet）ネットワークポートしかなく、Wi-Fi がない場合があります。

      ただし、この方法では、RC APK ファイルを **Driver Hub**または DS スマートフォンの Download（または Downloads）フォルダーに保存する必要があります。つまり、**Driver Station**デバイスに保存された**Robot Controller APK** です。

      まず、方法2の手順1に示すように、GitHub リポジトリからコンピューターに RC APK ファイルをダウンロードします。次に、USB データケーブルを使用して、その APK ファイルをコンピューターから DS デバイスの Download フォルダーに転送します。完了したら、DS デバイスをコンピューターから抜くことができます。

      DS アプリを **Control Hub**に接続します。DS アプリの Settings メニューから（**Android** デバイスの Wi-Fi 設定では決して接続しないでください）。

      DS アプリのメニューから「Program and Manage」を選択します。次に、右上の3本のバーをタッチし、「Manage」を選択します。

      これは、ラップトップブラウザーに表示されるのと同じ Manage ページです。したがって、以下の手順は、上記の方法2と同じです。

      「Update Robot Controller App」まで下にスクロールします。

      .. figure:: images/330-manage-RC-app-CH-DS.png
         :alt: RC アプリを更新
         :width: 80%
         :align: center

         RC アプリを更新

      「Select App…」をタッチします。DS デバイスの Download フォルダーに移動し、最新の RC APK ファイルを選択します。

      次に、「Update」ボタン（上の緑色の矢印）をタッチします。

      ソフトウェアは、既存の RC アプリを新しい更新された RC アプリに置き換えます。**Driver Station**と**Control Hub** 間の接続は一時的に失われ、その後自動的に復元されます。

      完了メッセージが表示されたら、更新された RC アプリが使用できる状態になります。

.. dropdown:: **Android**スマートフォンの**Robot Controller (RC)** アプリ

   **Robot Controller (RC)** スマートフォンの RC アプリを更新する方法は2つあります：

   1. REV Hardware Client (RHC)
   2. APK による「サイドローディング」

   .. note:: 
      コンピューターまたは **Driver Station**デバイス上の Program and Manage の下の Manage ページでは、接続された**Robot Controller**スマートフォンの RC アプリの更新は** 提供されません** 。

   .. dropdown:: 方法1 - REV Hardware Client - Windows コンピューターのみ

      RHC がインストールされて開いているコンピューターに、RC スマートフォンを直接接続します。USB データケーブルを使用してください（充電専用ケーブルではありません）。「Hardware」タブが左上でアクティブになっていることを確認してください。RC スマートフォンの RC アプリは開いている必要は**ありません** 。

      :doc:`REV Hardware Client の更新 </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>` で、必要な DS 更新ファイルが以前にダウンロードされているため、ここではコンピューターをインターネットに接続する必要はありません。

      RHC アプリは、次に示すようにスマートフォンを認識します：

      .. figure:: images/080-RHC-recognize-RC-phone.png
         :alt: スマートフォンを認識
         :width: 80%
         :align: center

         スマートフォンを認識

      スマートフォンが認識されない場合は、スマートフォンに :doc:`開発者オプション </programming_resources/tutorial_specific/android_studio/enabling_developer_options/Enabling-Developer-Options>` が有効になっていることを確認してください。必要に応じて、REV Hardware Client アプリの左下にある「Scan for Devices」ボタンをクリックして、RHC にデバイスの再スキャンを強制します。

      認識されたら、そのスマートフォンの大きなアイコン/長方形をクリックします。RHC アプリは、DS アプリの更新ステータス（ある場合）を表示します。

      .. figure:: images/082-RHC-update-RC-phone.png
         :alt: スマートフォンの更新ステータス
         :width: 80%
         :align: center

         スマートフォンの更新ステータス

      青い Update 長方形（緑色の矢印）をクリックするだけです – 完了！

      更新は高速でした。RC アプリが既に RHC にダウンロードされていたためです。これは、青い Update 長方形の左側に「(Already Downloaded)」と記載されていました。

      青い Update 長方形のすぐ上のドロップダウンリストで、RC アプリの**古い** バージョンを選択することもできます。

      インストール後、RC アプリアイコンをメニューからスマートフォンのホーム画面にドラッグします。

      RC スマートフォンをコンピューターから抜き、RHC アプリを閉じることができます。更新された RC アプリが使用できる状態になります。

   .. dropdown:: 方法2 - サイドロード

      ここでは、**Android Package**または**APK ファイル**を直接操作して、**Android** スマートフォンに RC アプリをインストールします。PC または Mac、古いまたは新しいコンピューターを使用できます。この方法は「サイドローディング」と呼ばれることがあります。

      1. コンピューターをインターネットに接続し、Web ブラウザーを開いて、`SDK GitHub リポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に移動します。

         .. figure:: images/050-FTC-repo.png
            :alt: SDK GitHub リポジトリ
            :width: 80%
            :align: center

            SDK GitHub リポジトリ

         右側の「Releases」の下にある「Latest」アイコン（上の黄色の楕円）をクリックします。

         次のページで、「Latest」セクションを少し下にスクロールして、「Assets」の短いリストを表示します。「FtcRobotController-release.apk」ファイルをクリックして、コンピューターにダウンロードします。

         .. figure:: images/090-github-assets-RC.png
            :alt: SDK GitHub リリース
            :width: 80%
            :align: center

            SDK GitHub リリース

         この時点で、現在のバージョン番号を反映するようにファイルの名前を変更できます。たとえば、``FtcRobotController-release-8.0.apk``または単に``RC-8.0-release.apk`` です。これにより、その RC スマートフォンに後で保存される可能性のある他のバージョンとファイルを区別できます。

      2. APK ファイルをコンピューターから RC スマートフォンの Downloads（または Download）フォルダーに転送します。USB データケーブルを使用してください（充電専用ケーブルではありません）。完了したら、RC スマートフォンをコンピューターから抜くことができます。

      3. 既存の（古い）RC アプリをアンインストールするには、そのアイコンをゴミ箱/アンインストールアイコンにドラッグします。または、RC アイコンをタッチして長押しして「App info」を表示し、Uninstall を選択します。

      4. RC スマートフォンで、Downloads フォルダーに移動します。これはいくつかの方法で実行できます：

         -  メインアプリメニュー（上にスワイプ）で、Files アイコンまたは Downloads アイコン（存在する場合）をタッチします
         -  Settings/Storage の基本ファイルマネージャーを使用します：Explore または Files をタッチします
         -  FX File Explorer などのサードパーティアプリを使用します（Google Play ストアから）

         転送した APK ファイル名をタッチします。プロンプトに応答して、更新された RC アプリをインストールします。

         インストール後、RC アプリアイコンをアプリメニューから RC スマートフォンのホーム画面にドラッグします。

      完了！更新された RC アプリが使用できる状態になります。

RC アプリの更新に関する他の説明は、`REV Robotics の優れたドキュメントサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-robot-controller-application>`__ にあります。

質問、コメント、修正は westsiderobotics@verizon.net までお願いします。
