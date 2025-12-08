*FIRST* Tech Challenge 自己点検
===================================

はじめに
------------

このページでは、**FTC Driver Station（DS）**アプリと **FTC Robot Controller（RC）**アプリの自己点検画面について説明します。

自己点検画面は、制御システムの FTC ルールに関連するデバイスステータスのスナップショットを提供します。これらのルールは、*FIRST* ウェブサイトの `Current Game and Season Materials ページ <https://ftc-resources.firstinspires.org/files/ftc/game>`_ にある競技マニュアルで説明されています。

.. tip:: イベント前にチームがロボットを自己点検するのに役立つ `Inspection Checklist (PDF) <https://ftc-resources.firstinspires.org/ftc/event/inspection-check>`_ が利用可能です。チームはイベント前に自己点検を行うことを強く推奨されています。
   
   また、合法および違法な部品の例を示した `Inspection Quick Reference (PDF) <https://ftc-resources.firstinspires.org/ftc/event/inspection-reference>`_ もあります（ただし、競技マニュアルの代替ではありません）。

自己点検画面は、チームが特定の制御システム要素が最新であり、適切に構成されていることを確認するのに役立つ、迅速で便利なリファレンスとしてのみ提供されています。

各点検画面は、ロボットの再起動の有無にかかわらず、自動的に更新されます。これにより、問題が解決されたことを迅速に確認できます。

課題は、小さな画面で有用な情報を最大化することです。自己点検のレイアウトとグラフィックスは FTC の要件に応じて進化します。このページでは、簡潔で意味のあるキャプションのいくつかを明確にします。

ロボット検査
----------------

自己点検レポートは FTC トーナメントのロボット検査でレビューされる場合がありますが、FTC ルールへの準拠の包括的または公式の基準では**ありません**。ロボットとドライバーステーションがオンになって接続されている状態で、検査官は **Inspection Checklist** フォーム（紙またはタブレット上）を確認できます。**Driver Station Inspection Report** と **Robot Controller Inspection Report** の両方を確認します。これらはどちらも DS から表示できます。多くの FTC イベントでは、RC Inspection Report に表示される QR コードをスキャンします。

バージョン情報
-------------------

競技マニュアルには、デバイスファームウェア、Android オペレーティングシステム、FTC アプリの最小推奨バージョンがリストされています。チームは、ロボット検査ステータスに影響を与えることなく、古いバージョンを実行することを選択できます。これにより、競技会の直前にデバイスをアップグレードしようとして、ミスがロボットを動作不能にする状況を回避できます。

.. note::
  このページの画像は、FTC アプリのバージョン 10.3 以降を示しています。このページは、**Control Hub** とペアリングされた **Driver Hub** のみを示しており、ドライバーステーションまたはロボットコントローラーとしてスマートフォンを使用する場合、わずかな違いがある可能性があります。アプリバージョン 10.2 以前の画面画像については、:doc:`旧自己点検 <self-inspect>` ページを参照してください。

*FIRST* は、チームがファームウェア、Android オペレーティングシステム、FTC アプリの最新バージョンを使用することを推奨していますが、必須ではありません。現在のバージョンには、最新のバグ修正と機能強化があります。たとえば、**Control Hub Android OS** のバージョン 1.1.6 には、Wi-Fi に関連する修正があります。

各 FTC シーズンでは、FTC アプリの新しいメジャーバージョンがリリースされます。INTO THE DEEP のメジャーバージョンは 10 で、DECODE のメジャーバージョンは 11 です。ゲームに AprilTag がある場合、SDK にはそれらのタグの :doc:`ローカリゼーション <../../apriltag/vision_portal/apriltag_localization/apriltag-localization>` 情報が含まれており、フィールド上のロボットの位置を判断できます。シーズンが進むにつれて、マイナーリリースにはバグ修正といくつかの機能強化が含まれます（例：11.1、11.2 など）。

選択したバージョンに関係なく、インストールされている **ROBOT CONTROLLER** アプリと **DRIVER STATION** アプリのバージョンがメジャーおよびマイナー値で一致することを強く推奨します。すべてのソフトウェアバージョンが互いに互換性があるわけではないためです。

チームは、ロボット検査ステータスに影響を与えることなく、古いバージョンを実行することを選択できます。

.. caution::
   一部の FTC アプリバージョンには異なるロボット通信プロトコルがあり、互いに接続できません。
   
   フィールドスタッフは、推奨バージョンより古いソフトウェアを使用しているチームに包括的なサポートを提供できません。

Driver Station 自己点検レポート
-------------------------------------

次は、**Driver Hub** を回転させて画面をポートレートモードにし、レポートのすべてのアイテムがスクロールせずに1つの画面に表示されるようにした DS 自己点検レポートのスクリーンショットです。

.. figure:: images/newDS.png
   :align: center
   :width: 85%
   :alt: Driver station self inspection report

   All items are good

-  項目 1 3 つのドットは、``Disconnect from Wi-Fi Direct`` と ``Disable Bluetooth`` の 2 つの選択肢があるメニューです。どちらも **Control Hub** とペアリングされた **Driver Hub** には必要ありませんが、ドライバーステーションまたはロボットコントローラーとして使用できるスマートフォンには主に必要です。``Disconnect from Wi-Fi Direct`` は機能しますが、アプリが自動的に再ペアリングされることがあります。``Disable Bluetooth`` は、DS で Bluetooth が何らかの形で有効になっている場合を除いて、必要ありません。
-  項目 2 ``Manufacturer`` は REV **Driver Hub** の場合 **REV Robotics** である必要があります。
-  項目 3 ``Model`` は **Driver Hub** である必要があります。
-  項目 4 ``Driver Hub OS Version`` はおそらく 1.2.0 です。
-  項目 5 ``Android Version`` は **Driver Hub** の場合おそらく 10 です。 
-  Item 6 shows the ``Battery Level`` of the device being reported. Fun
   fact: the green color of the percentage value changes towards
   **orange** as the charge level goes down.
-  Item 7 ``Bluetooth`` should be **Disabled**.
-  Item 8 ``Location services`` should be **Enabled**, but appears only on devices running
   **Android 8** or higher. This is an SDK/Android technology requirement, not an FTC rule.
-  Item 9 ``Wi-Fi Enabled`` must be **Yes** as it means the DS device’s Wi-Fi radio is **ON**.
-  Item 10 ``Standard Wi-Fi Connected`` must be **Yes** to indicate the Driver Hub is connected to a standard Wi-Fi source, such as a Control Hub.
-  項目 11 は、``Driver Station Name`` が FTC フォーマット要件を満たしていることを示します。チーム番号に -DS を加えたものである必要があります。例：99999-DS。予備デバイスが構成されている場合、文字指定子を追加できます <チーム番号>-<文字>-DS（例：12345-A-DS、12345-B-DS）。デバイスの命名規則については、競技マニュアルを参照してください。
-  項目 12 は ``Robot Controller Name`` を示します。接続されていない場合は **None** が表示されます。**Robot Controller** と **Driver Station** の名前のチーム番号部分が一致しない場合は、エラーが表示されます。RC 名が FTC フォーマット要件と一致しているかどうかはチェックしません。**Robot Controller** 自己点検レポートを参照してください。
-  項目 13 Apps Installed ``Robot Controller`` は **Not installed** である必要があります。これは、**Driver Station** デバイスに **Robot Controller** アプリもインストールされて**いない**ことを確認します。各デバイスには 1 つの FTC アプリのみをインストールする必要があります。両方のアプリを誤ってインストールすることは可能ですが、これは通常、アプリが正しく動作しない原因となります。
-  項目 14 Apps Installed ``Driver Station`` は、**Driver Station** アプリのバージョン番号を示す必要があります。*FIRST* は、チームが現在利用可能なバージョンを使用することを推奨していますが、必須ではありません。無効または将来のデバイスシステムの日付は、ここで「Driver Station app is obsolete」というメッセージで無効な検査項目を引き起こす可能性があります。デバイスの日付を修正すると、無効な検査項目が修正されるはずです。

==================================

Here’s a report from a Driver Station with some items **rejected** by Self Inspect.
Problems are indicated by a red circle exclamation mark icon, or an orange triangle exclamation mark icon.

This was a driver hub that was firmware reset. This reset the DS version to 7 and restored all system and DS app settings to defaults.
Then the `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client>`_ was used to update the DS version 10.3. 
Then the FTCRobotController app was also deployed to the DS device from Android Studio.
   
.. figure:: images/newDSerrors.png   
   :align: center
   :width: 85%
   :alt: Driver station self inspection report

   Self Inspect with issues!

-  項目 10 は ``Standard Wi-Fi Connected`` が **No** であることを拒否します。DS はまだロボットに接続されていません。デバイスを接続する前に **Driver Station** 名を修正する必要があります。
-  項目 11 は、FTC フォーマット要件を満たしていないため ``Driver Station Name`` を拒否します。**Android_a301** は、新品の DS の DS 名の例です。DS アプリの設定に移動し、競技マニュアルのルールに従って **Driver Station** 名を設定します。例：チーム番号に -DS を加えたもの：**99999-DS**。
-  項目 12 は、DS 名と一致しないため ``Robot Controller Name`` を拒否します。**None** の値は、DS が RC に接続されていないためです。この項目は、RC 名のフォーマットが有効かどうかをチェックせず、RC 名のチーム番号部分が DS 名のチーム番号部分と一致することのみをチェックします。
-  項目 13 は、この DS デバイスにインストールされた RC アプリの存在を拒否します。ドライバーステーションデバイスから RC アプリをアンインストールします。

各問題を修正すると、検査レポートが更新され、現在の状態が表示されるはずです。

.. tip::
   自己点検画面で赤い円の感嘆符アイコンまたはオレンジ色の三角形の感嘆符アイコンをタッチすると、問題に関連するメッセージが一時的に表示されるはずです。
   
Robot Controller 自己点検レポート
---------------------------------------

ここで、**Robot Controller** 自己点検レポートに変更します。これは通常、Inspection Reports DS 画面の **Inspect Robot Controller** メニューオプションを選択することで **Driver Station** から表示されます。参考までに - **Control Hub** の HDMI ポートに外部モニターを接続し、USB ポートにマウスを接続すると、**Control Hub** から直接 RC 検査レポートを表示できます。

.. figure:: images/newRC.png   
   :align: center
   :width: 85%
   :alt: Robot controller self inspection report

   All items are good, except RC Password

-  項目 1 3 つのドットは、``Disable Bluetooth`` という 1 つの選択肢があるメニューです。**Control Hub** で Bluetooth が何らかの形で有効になっている場合を除いて、必要ありません。
-  項目 2 ``Manufacturer`` は REV **Control Hub** の場合 **REV Robotics** である必要があります。
-  項目 3 ``Model`` は **Control Hub v1.0** である必要があります。
-  項目 4 ``Control Hub OS Version`` は少なくとも 1.1.6 である必要があります。*FIRST* は、チームが現在利用可能なバージョンを使用することを推奨していますが、必須ではありません。
-  項目 5 ``Android Version`` は **Control Hub** の場合おそらく 7.1.2 です。
-  項目 6 ``Hub Firmware`` は、ハブアドレスとファームウェアレベルをリストします。この例では 1 つの **Control Hub** が表示されていますが、**Expansion Hub** もここにリストできます。チェックマークは、RC アプリの現在のバージョンに基づいてすべてのファームウェアが最新であることを示します。*FIRST* は、チームが現在利用可能なバージョンを使用することを推奨していますが、必須ではありません。
-  項目 7 は、報告されているデバイスの ``Battery Level`` を示します。
-  項目 8 ``Bluetooth`` は **Disabled** である必要があります。
-  Item 9 ``RC Password`` appears only in RC Self Inspect. This inspection item has failed the FTC requirement for a Control Hub
   password different than the factory default (“password”). Go to the Program and Manage page, select Manage and then update the RC password.
   You will have to re-pair the DS to the RC and enter the new password to reconnect.
-  Item 10 ``Wi-Fi Enabled`` must be **Yes** as it means the control hub’s Wi-Fi radio is **ON**.
-  Item 11 ``Standard Wi-Fi Connected`` must be **Yes**.
-  項目 12 は、``Robot Controller Name`` が FTC フォーマット要件を満たしていることを示します。チーム番号に -RC を加えたものである必要があります。例：99999-RC。予備デバイスが構成されている場合、文字指定子を追加できます <チーム番号>-<文字>-RC（例：12345-A-RC、12345-B-RC）。デバイスの命名規則については、競技マニュアルを参照してください。
-  項目 13 Apps Installed ``Robot Controller`` は、RC アプリのバージョンを表示する必要があります。*FIRST* は、チームが現在利用可能なバージョンを使用することを推奨していますが、必須ではありません。
-  項目 14 ``Matches DS Version`` は **Yes** である必要があります。**No** がここに表示される可能性があり、おそらくポイントの不一致（例：10.0 と 10.1）が原因です。不一致は現在許可されていますが、推奨されません。
-  項目 15 Apps Installed ``Driver Station`` は **Not installed** である必要があります。これは、**Robot Controller** デバイスに **Driver Station** アプリもインストールされて**いない**ことを確認します。各デバイスには 1 つの FTC アプリのみをインストールする必要があります。両方のアプリを誤ってインストールすることは可能ですが、これは通常、アプリが正しく動作しない原因となります。
-  項目 16 RC 検査レポートの下部には、検査官がタブレットを使用している場合に、検査チェックリスト項目の多くを入力するために検査中にスキャンできる QR コードがあります。

.. figure:: images/newRcQrCode.png   
   :align: center
   :width: 85%
   :alt: Self Inspect QR code

   ロボット検査官は検査中に QR コードをスキャンできます

まとめ
-------

自己点検画面は、チームが特定の制御システム要素が最新であり、適切に構成されていることを確認するのに役立つ、迅速で便利なリファレンスです。

自己点検は FTC トーナメントのロボット検査でレビューされる場合がありますが、FTC ルールへの準拠の包括的または公式の基準では**ありません**。

各検査画面は、ロボットの再起動の有無にかかわらず、自動的に更新されます。これにより、問題が解決されたことを迅速に確認できます。

