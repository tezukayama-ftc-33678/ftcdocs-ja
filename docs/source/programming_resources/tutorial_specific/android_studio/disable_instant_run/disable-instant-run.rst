**Android Studio** の Instant Run を無効にする :bdg-warning:`Legacy` :bdg-success:`AS`
======================================================================================

.. attention::
   *Instant Run* は **Android Studio** バージョン 3.5 で削除されました。
   **Android Studio** 3.5 以降のバージョンでは問題になりません。
   ただし、この記事は **FIRST** **Tech Challenge** ソフトウェア開発キット
   （**SDK** ）v7.1 以前のバージョンを古いバージョンの**Android Studio** で
   使用している方のために残されています。

はじめに
~~~~~~~~~~~~

**Android Studio** を使用する場合、** 最も重要なステップの1つ** は**Android Studio** の Instant Run を無効にすることです。Instant Run は、アプリへのコード変更を適用する時間を短縮することで開発プロセスを合理化するように設計された機能です。残念ながら、Instant Run は機能が制限されており、**FIRST** **Tech Challenge** の**Android Studio** プロジェクトフォルダーで使用すると、** 重大な** 問題や** トラブルシューティングが困難な** 問題を引き起こす可能性があります。

**Android Studio** を使用するチームは、Instant Run を** 必ず** 無効にしてください。

Instant Run 設定の場所
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Android Studio** を初めて起動すると、Welcome 画面が表示されます。この Welcome 画面から Instant Run**Settings** に移動するには、画面右下隅の「Configure」ドロップダウンリストから「Configure->Settings」項目を選択します。

.. image:: images/ConfigureSettings.jpg

**Settings** ウィンドウの左側に、「Build, Execution, Deployment」というカテゴリーがあります。このカテゴリー内で、「Instant Run」サブカテゴリーをクリックすると、**Android Studio** インストールの Instant Run 設定が表示されます。デフォルトでは、**Android Studio** を初めてインストールすると Instant Run が有効になっています。「Enable Instant Run to hot swap code/resource changes on deploy (default enabled)」オプションのチェックを外し、「OK」ボタンをクリックして Instant Run を無効にしてください。

.. image:: images/InstantRunConfiguration.jpg

追加情報
~~~~~~~~~~~~~~~~~~~~~~

Google **Android** Developer ウェブサイトには、Instant Run に関する追加情報があります。また、この機能を無効にする方法の説明もあります：

https://developer.android.com/studio/run
