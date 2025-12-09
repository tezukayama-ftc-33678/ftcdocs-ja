Control Hub OSの更新
===========================

オペレーティングシステム（OS）は、タスクのスケジューリング、アプリケーションの実行、周辺機器の制御など、コンピューターの基本機能をサポートするソフトウェアです。**REV Control Hub** では、これを更新する必要がある場合があります。このOS更新は厳密には :doc:`ソフトウェア開発キット（SDK） </ftc_sdk/overview/index>` の一部ではありませんが、SDKが正しく動作するためには、Control HubでこれらのOS更新が必要です。

Control Hub OSを更新する方法は2つあります：

1. REV Hardware Client（RHC）
2. コンピューター上の管理ページ

Control Hub OSの更新に関する詳細情報は、
`REV Roboticsの優れたドキュメントサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system>`__ にあります。

.. dropdown:: 方法1 - REV Hardware Client（RHC） - Windowsコンピューターのみ

   1. REV Control Hubに12Vロボット電源を供給します。

   2. USB-Cデータケーブルを使用して、Control HubをREV Hardware Clientを実行しているコンピューターに直接接続します。

   3. Hubの大きなアイコン/矩形をクリックします。「Control Hub Operating
      System」の下に、現在のバージョンと最新バージョンの不一致がある場合は表示されます（下の黄色の楕円）。

      .. figure:: images/650-RHC-OS.png
         :alt: Control Hub OSの更新
         :width: 80%
         :align: center

         Control Hub OSの更新

   ドロップダウンメニューで最新バージョンを確認し、青色の「Update」矩形をクリックします（上の緑色の矢印）。
   :doc:`REV Hardware Clientの更新 </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
   で必要な更新ファイルが事前にダウンロードされているため、この更新の速度は向上しています。

   完了です！Control HubのOSが更新されました。

.. dropdown:: 方法2 - コンピューター上の管理ページ

   1. コンピューターをWi-Fi経由でControl Hubに接続します。Chromeブラウザで
      **FIRST Tech Challenge** インターフェースを開きます。

   2. Manageタブをクリックし、Update Control Hub Operating Systemまでスクロールします。

      .. figure:: images/700-manage-OS.png
         :alt: Control Hub OSの更新
         :width: 80%
         :align: center

         Control Hub OSの更新

   3. 必要に応じて、REV Roboticsの `Control
      Hub OS Webページ <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system#using-the-robot-controller-console>`__ から最新のOSファイルをダウンロードします。
      このファイルは解凍または「unzip」しないでください。

   4. 管理ページで「Select Update File…」をクリックし、OSファイルをダウンロードしたコンピューターのフォルダーに移動します。

   5. そのファイルを選択し、「Update & Reboot」をクリックします（上の緑色の矢印）。

   以上です！Control HubのOSが更新されました。
   
質問、コメント、修正は westsiderobotics@verizon.net まで

