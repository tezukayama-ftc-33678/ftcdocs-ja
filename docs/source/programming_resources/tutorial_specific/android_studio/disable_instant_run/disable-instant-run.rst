**Android Studio** の Instant Run を無効にする :bdg-warning:`Legacy` :bdg-success:`AS`
============================================================================

.. attention::
   *Instant Run* は **Android Studio** バージョン 3.5 で削除されました。
   **Android Studio** 3.5 以降のバージョンでは問題になりません。
   ただし、この記事は **FIRST** **Tech Challenge** ソフトウェア開発キット
   （**SDK**）v7.1 以前のバージョンを古いバージョンの **Android Studio** で
   使用している方のために残されています。

はじめに
~~~~~~~~~~~~

**Android Studio** を使用する場合、**最も重要なステップの1つ**は **Android Studio** の Instant Run を無効にすることです。Instant Run は、アプリへのコード変更を適用する時間を短縮することで開発プロセスを合理化するように設計された機能です。残念ながら、Instant Run は機能が制限されており、**FIRST** **Tech Challenge** の **Android Studio** プロジェクトフォルダーで使用すると、**重大な**問題や**トラブルシューティングが困難な**問題を引き起こす可能性があります。

**Android Studio** を使用するチームは、Instant Run を**必ず**無効にしてください。

Instant Run 設定の場所
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you first launch Android Studio a Welcome screen should appear. You
can navigate to the Instant Run Settings from this Welcome screen by
selecting the “Configure->Settings” item from the “Configure” dropdown
list in the lower right hand corner of the screen.

.. image:: images/ConfigureSettings.jpg

On the left hand side of the Settings window, there should be a category
called “Build, Execution, Deployment”. Within this category, click on
the “Instant Run” subcategory to display the Instant Run settings for
your Android Studio installation. By default, Instant Run is enabled
when you first install Android Studio. Uncheck the “Enable Instant Run
to hot swap code/resource changes on deploy (default enabled)” option
and then click on the “OK” button to disable Instant Run.

.. image:: images/InstantRunConfiguration.jpg

追加情報
~~~~~~~~~~~~~~~~~~~~~~

Google **Android** Developer ウェブサイトには、Instant Run に関する追加情報があります。また、この機能を無効にする方法の説明もあります：

https://developer.android.com/studio/run
