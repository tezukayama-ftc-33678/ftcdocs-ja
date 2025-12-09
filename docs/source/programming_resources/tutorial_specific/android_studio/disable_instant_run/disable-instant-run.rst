Android Studio Instant Run の無効化 :bdg-warning:`Legacy` :bdg-success:`AS`
===========================================================================

.. attention::
   *Instant Run* は **Android Studio** バージョン 3.5 で削除され、**Android Studio** 3.5 以降のバージョンでは問題になりません。ただし、この記事は、以前のバージョンの **Android Studio** で *FIRST* Tech Challenge ソフトウェア開発キット（SDK）v7.1 以前を使用している人のために残されています。

はじめに
~~~~~~~~

**Android Studio** ユーザーの場合、**最も重要な手順の 1 つ**は、**Android Studio** の **Instant Run** を無効にすることです。**Instant Run** は、アプリにコード変更を適用する時間を短縮することで、開発プロセスを合理化するために設計された機能です。残念ながら、**Instant Run** は機能が制限されており、*FIRST* Tech Challenge **Android Studio** プロジェクトフォルダーで使用すると、**重大で**、**トラブルシューティングが困難な**問題を引き起こす可能性があります。

**Android Studio** を使用するチームは、**Instant Run** を無効にする**必要があります**。

Locating Instant Run Settings
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

Additional Information
~~~~~~~~~~~~~~~~~~~~~~

The Google Android Developer website has additional information about
Instant Run. It also has instructions on how to disable this feature:

https://developer.android.com/studio/run
