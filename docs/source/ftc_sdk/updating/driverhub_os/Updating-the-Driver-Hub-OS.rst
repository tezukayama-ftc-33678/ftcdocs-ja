Driver Hub OSの更新
==========================

オペレーティングシステム（OS）は、タスクのスケジューリング、アプリケーションの実行、周辺機器の制御など、コンピューターの基本機能をサポートするソフトウェアです。**REV Driver Hub** では、これを更新する必要がある場合があります。このOS更新は厳密には :doc:`ソフトウェア開発キット（SDK） </ftc_sdk/overview/index>` の一部ではありませんが、SDKが正しく動作するためには、Driver HubでこれらのOS更新が必要です。

Driver Hub OSを更新する方法は2つあります：

1. REV Hardware Client（RHC）
2. Driver Hub上のソフトウェアマネージャー

Driver Hub OSの更新に関する詳細情報は、
`REV Roboticsの優れたドキュメントサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-the-driver-hub>`__ にあります。

.. dropdown:: 方法1 - REV Hardware Client（RHC） - Windowsコンピューターのみ

   1. Driver Hubの電源を入れます。USB-Cデータケーブルを使用して、REV Hardware Clientを実行しているコンピューターに直接接続します。

   2. Driver Hubの大きなアイコン/矩形をクリックします。「Driver Hub
      Operating System」の下に、現在のバージョンと最新バージョンの不一致がある場合は表示されます（下の黄色の
      楕円）。

      .. figure:: images/600-RHC-DH-OS.png
         :alt: Driver Hub OSの更新
         :width: 80%
         :align: center

         Driver Hub OSの更新

      ドロップダウンメニューで最新バージョンを確認します（ある場合）。次に、該当する場合は「Update」と表示された青色の矩形をクリックします。
      :doc:`REV Hardware Clientの更新
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      で必要な更新ファイルが事前にダウンロードされているため、この更新の速度は向上しています。


   完了です！Driver HubのOSが更新されました。

.. dropdown:: 方法2 - ソフトウェアマネージャー

   REV Driver Hubには、ソフトウェアマネージャーと呼ばれる組み込みアプリがあり、
   Driver Hub OS（およびその他の関連ソフトウェア）を自動的に更新できます。
   インターネット接続のみが必要です。

   1. すべてのアプリを閉じ、Driver HubのWi-Fiメニューを開きます（設定内、またはホーム画面の上部から2回スワイプダウン）。
      Driver Hubを一時的にWi-Fi経由でインターネットに接続します。

   2. Driver Hubのホーム画面でソフトウェアマネージャーアプリを開きます（下の左側の画像）。

      .. figure:: images/910-DH-double.png
         :alt: ソフトウェアマネージャーの更新
         :width: 80%
         :align: center

         ソフトウェアマネージャーの更新

   3. ソフトウェアマネージャーは、必要な更新を自動的にチェックし、
      結果を表示します（上の右側の画像）。グレーのボタンをタッチして、必要に応じてDriver Hub Operating System（OS）を含む更新を実行します。

      .. note:: 
         REV RoboticsはDriver Hub用のダウンロード可能なOSイメージファイルを提供していますが、
         このチュートリアルで利用可能なツールは、OSを更新するためにこのファイルを提供することを受け付けていません。

   4. すべてが完了したら、インターネットアクセスに使用したWi-Fiネットワークを「削除」します。
      これで、Driver Hubは通常の競技での使用準備が整いました。

質問、コメント、修正は westsiderobotics@verizon.net まで

