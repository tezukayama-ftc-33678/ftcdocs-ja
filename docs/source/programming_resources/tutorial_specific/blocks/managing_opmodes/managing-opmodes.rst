Blocks での OpMode 管理 :bdg-warning:`Blocks`
=============================================

**Blocks** は、グラフィカルなプログラミング要素を使用してプログラムを作成するプログラミング言語です。そのため、そのファイル形式は、例えば JAVA や他のテキストベースのプログラミング言語ファイルとは異なります。Blocks プログラムは **.blk** 拡張子で保存されますが、その内容は実際には XML（Extensible Markup Language）としてフォーマットされています。Blocks プログラムの実際の XML 形式はこのドキュメントの範囲外ですが、Blocks 以外のプログラムで読み取り/表示/解釈されることを意図していないということだけ言っておきます。MAC や PC には Blocks プログラムを表示または編集できる一般的なプログラムはなく、常に **Robot Controller** アプリ（**REV Control Hub** または認可された Android スマートフォン上で実行）内の Blocks インターフェースを通じて行う必要があります。つまり、ファイルをダブルクリックしてコンピューター上のエディタープログラムで開くことはできません。

OpMode の作成
-------------

**OpMode** を作成するための :doc:`優れたチュートリアル <../creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks>` があり、Blocks インターフェースについて多くのことを説明し、Blocks プログラムが何をするのかを理解するのに役立ちます。Blocks **OpMode** の操作方法を学ぶには、このドキュメントをチェックすることをお勧めします。

OpMode の保存
-------------

**OpMode** を**「保存」**するということの意味を理解することが重要です。**OpMode** をプログラミング/編集する際、Web ブラウザー（Chrome など）を使用しているか、Web ブラウザーとして*動作する*プログラム（**REV Hardware Client** など）を使用しています。作成/編集しているプログラムは、Web ブラウザー内に*一時的に*のみ存在します。プログラムが最終的にデバイス（**REV Control Hub** または認可されたスマートフォン）に保存され、ロボットで使用できるようにするための自動保存機能はありません。*SAVE* 操作のみが、実際に **OpMode** を **.blk** ファイルとしてデバイスに保存します。したがって、Blocks プログラマーは頻繁に、特に作業を完了したら、作業を*保存*することが不可欠です。**OpMode** を*保存*するメカニズムは、ソフトウェアの編集ウィンドウ内の「**Save Op Mode**」ボタンを使用します。

.. figure:: images/blocks_save.jpg
   :align: center
   :width: 80%
   :alt: Saving Opmode

   Saving the OpMode within the Blocks Editor

Once a program is saved, a message will appear on the right-hand side of the 
same row to indicate that the program has been saved.

.. figure:: images/blocks_saved.jpg
   :align: center
   :width: 80%
   :alt: Opmode Saved

   Message indicating OpMode has been Saved

Downloading an OpMode
---------------------

Once an OpMode has been saved to a device, the OpMode can be selected via the
DRIVER STATION or edited again via the programming interfaces. However, that
Blocks program only exists as a Blocks File (**.blk**) on the device. Often it
is desirable to save a copy of the program on your laptop (or on another
device, or in some other safe location) or provide the program for use by
others (teammates, another robot, other teams, provide online, etc.). 

In order to get a copy of the Blocks program from the device, you need to 
*download* the program from the device. You can do this in one of two ways, either 
through the editing interface or the main Blocks management interface.

Downloading an OpMode through the Editing Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While editing an OpMode, an OpMode can be *saved* and it can also be *downloaded*
(there are other options, but we're just going to focus on these two for the time
being). When an OpMode is saved, the program is saved **onto the device** into a
Blocks file (**.blk**). In order to save a copy of the program to your local computer
(for safe storage or for sharing) you need to *download* the program. Downloading the
program *does* issue a Save action on the current program, but this should not be
relied upon - programmers should always save their program before downloading.
Downloading an OpMode is performed via the "**Download Op Mode**" button within the Editing
Interface.

.. figure:: images/blocks_download.jpg
   :align: center
   :width: 80%
   :alt: Opmode Download

   Downloading a Blocks program

Pressing the "Download Op Mode" button makes the file available to the web
browser, so the web browser will manage the file in its usual way (e.g. with
Chrome the file is saved into the computer's "Downloads" folder).

Downloading an OpMode through the Management Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By clicking on the "Blocks" menu item, you will be taken to the Blocks
management interface. This interface shows you all of the Blocks OpModes
currently on the device and provides you with options for managing those
OpModes.

.. figure:: images/blocks_manage.png
   :align: center
   :width: 80%
   :alt: Blocks Management

   Blocks Management Interface

OpModes can be downloaded through this interface. Initially, the "**Download
Selected Op Modes**" button on this interface is grayed out. One or more Op Modes
can be selected in this interface, and then they can all be downloaded at once.
In the example below, the "Mecanum Drive" opmode is selected and then downloaded
via the "**Download Selected Op Modes**" button.

.. figure:: images/blocks_manage_download.png
   :align: center
   :width: 80%
   :alt: Blocks Management Download

   Downloading Blocks via the Management Interface

Uploading Blocks
----------------

If you have a previously downloaded Blocks file, or you receive a Blocks file
from another source (like sample Blocks from REV, for example) you will want 
to *upload* the Blocks file (**.blk**) to the device (REV Control Hub or 
Android Smartphone). Within the Blocks Management interface, there is a button
on the top menu marked, "**Upload Op Mode**". 

Once you press "**Upload Op Mode**" a pop-up window will appear to allow you to 
choose the file you want to upload. Click the "**Choose File**" button to open a file
browser for your local computer to select the **.blk** Blocks file to upload.
Once uploaded, the Blocks program will open within the Blocks interface.

.. figure:: images/blocks_manage_upload.png
   :align: center
   :width: 80%
   :alt: Blocks Management File Upload

   Uploading Blocks Files via the Management Interface

Once a block is uploaded, it can be edited and modified like any other OpMode!


