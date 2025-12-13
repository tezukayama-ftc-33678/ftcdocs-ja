
***FIRST* Tech Challenge Self Inspect**
=======================================

はじめに
------------

このページでは、**Driver Station** （DS）アプリと**Robot Controller** （RC）アプリにおける Self Inspect 画面について説明します。

Self Inspect 画面は、FTCの制御システムに関するルールに基づき、デバイスの状態をスナップショットとして表示します。
これらのルールは、競技マニュアル（Competition Manual）に記載されており、
`Current Game and Season Materials page <https://ftc-resources.firstinspires.org/files/ftc/game>`_（**FIRST** 公式サイト）で確認できます。

.. tip::
   `Inspection Checklist (PDF) <https://ftc-resources.firstinspires.org/ftc/event/inspection-check>`_ を使うことで、イベント前にロボットのセルフ検査が可能です。イベント前のセルフ検査を強く推奨します。
   
   また、`Inspection Quick Reference (PDF) <https://ftc-resources.firstinspires.org/ftc/event/inspection-reference>`_ には合法・非合法部品の例が掲載されています（ただし競技マニュアルの代用にはなりません）。

Self Inspect 画面は、制御システムの各要素が最新かつ正しく構成されているかをチームが確認するための、簡易的な参考情報として提供されています。

各検査画面は、ロボットの再起動有無にかかわらず自動で更新されるため、問題が解決されたかをすばやく確認できます。

限られた画面スペースで有用な情報を最大限に表示することが課題です。Self Inspect のレイアウトやグラフィックはFTCの要件に合わせて進化しており、本ページでは簡潔ながら意味のあるキャプションを解説します。


ロボット検査
----------------

Self Inspect レポートはFTC大会のロボット検査時に参照されることがありますが、FTCルールへの完全な準拠や公式基準を示すものでは** ありません** 。
ロボットと**Driver Station** が起動・接続された状態で、検査員は紙またはタブレットの**Inspection Checklist** フォームを使って確認します。
**Driver Station Inspection Report** と**Robot Controller Inspection Report** の両方をDSから表示できます。
多くのFTCイベントでは、RCインスペクトレポートに表示されるQRコードをスキャンします。


バージョン情報
-------------------

競技マニュアルには、デバイスのファームウェア、Android OS、FTCアプリの推奨最小バージョンが記載されています。
チームは、ロボット検査の合否に影響なく、古いバージョンを使用することも可能です。
これは、競技会場で急いでアップグレードし、失敗してロボットが動かなくなる事態を避けるためです。

.. note::
   本ページの画像はFTCアプリのバージョン10.3以降のものです。
   Driver HubとControl Hubのペアのみを例示しています。スマートフォンを**Driver Station** や**Robot Controller** として使う場合は若干異なる場合があります。
   バージョン10.2以前の画面は :doc:`old self-inspect<self-inspect>` を参照してください。

**FIRST** は、ファームウェア・Android OS・FTCアプリの最新版使用を推奨しますが、必須ではありません。
最新版にはバグ修正や機能強化が含まれています。例えば、**Control Hub Android OS** のバージョン1.1.6ではWi-Fi関連の修正が含まれています。

FTCの各シーズンでFTCアプリのメジャーバージョンがリリースされます。INTO THE DEEPのメジャーバージョンは10、DECODEは11です。
ゲームに**AprilTag** が含まれる場合、SDKには :doc:`localization<../../apriltag/vision_portal/apriltag_localization/apriltag-localization>` 情報が含まれ、ロボットのフィールド上の位置を特定できます。
シーズン中は、マイナーバージョン（例：11.1、11.2など）でバグ修正や機能追加が行われます。

どのバージョンを選択しても、インストールされている**Robot Controller** アプリと**Driver Station** アプリのメジャー・マイナーバージョンが一致していることを強く推奨します。すべてのバージョンが互換性を持つわけではありません。

チームは、ロボット検査の合否に影響なく、古いバージョンを使用することも可能です。

.. caution::
    一部のFTCアプリバージョンではロボット通信プロトコルが異なり、互いに接続できない場合があります。
   
    推奨バージョン未満のソフトウェアを使用しているチームに対して、フィールドスタッフは十分なサポートを提供できません。


Driver Station Self Inspect レポート
-------------------------------------

以下は、Driver Hubを縦向きにして、すべての項目がスクロールなしで1画面に表示される**Driver Station** Self Inspect レポートのスクリーンショットです。

.. figure:: images/newDS.png
   :align: center
   :width: 85%
   :alt: Driver station self inspection report

   すべての項目が正常

-  項目1：三点リーダーはメニューで、``Disconnect from Wi-Fi Direct`` と``Disable Bluetooth`` の2つの選択肢があります。
   Control HubとペアになっているDriver Hubでは通常不要ですが、スマートフォンを**Driver Station** や**Robot Controller** として使う場合に利用します。
   ``Disconnect from Wi-Fi Direct`` は動作しますが、アプリが自動で再ペアリングすることがあります。
   ``Disable Bluetooth`` は、DSでBluetoothが有効になっている場合以外は不要です。
-  項目2：``Manufacturer`` はREV Driver Hubの場合、**REV Robotics** である必要があります。
-  項目3：``Model`` は**Driver Hub** である必要があります。
-  項目4：``Driver Hub OS Version`` は通常1.2.0です。
-  項目5：``Android Version`` はDriver Hubの場合、通常10です。
-  項目6：``Battery Level`` はデバイスのバッテリー残量を表示します。豆知識：残量が減るとパーセンテージの緑色が** オレンジ** に近づきます。
-  項目7：``Bluetooth`` は**Disabled** （無効）である必要があります。
-  項目8：``Location services`` は**Enabled** （有効）である必要がありますが、**Android 8** 以上のデバイスのみ表示されます。これはSDK/Androidの技術要件であり、FTCルールではありません。
-  項目9：``Wi-Fi Enabled`` は**Yes** （はい）である必要があります。DSデバイスのWi-Fiが**ON** であることを示します。
-  項目10：``Standard Wi-Fi Connected`` は**Yes** （はい）である必要があります。Driver HubがControl Hubなどの標準Wi-Fiに接続されていることを示します。
-  項目11：``Driver Station Name`` はFTCの命名規則に合致している必要があります。チーム番号＋-DS（例：99999-DS）です。
   予備デバイスの場合は、<チーム番号>-<英字>-DS（例：12345-A-DS、12345-B-DS）となります。命名規則は競技マニュアルを参照してください。
-  項目12：``Robot Controller Name`` を表示します。未接続の場合は**None** となります。Robot ControllerとDriver Stationのチーム番号部分が一致しない場合はエラーが表示されます。
   RC名がFTC命名規則に合致しているかはチェックしません。詳細はRobot Controller Self Inspect レポートを参照してください。
-  項目13：Apps Installed ``Robot Controller`` は**Not installed** （未インストール）である必要があります。Driver StationデバイスにRobot Controllerアプリがインストールされていないことを確認します。
   各デバイスにはFTCアプリを1つだけインストールしてください。両方インストールすると正常に動作しない場合があります。
-  項目14：Apps Installed ``Driver Station`` はDriver Stationアプリのバージョン番号を表示します。**FIRST** は最新版の使用を推奨しますが、必須ではありません。
   デバイスの日付が不正または未来日付の場合、「The Driver Station app is obsolete」と表示され、検査項目が無効になることがあります。日付を修正すれば正常に戻ります。

==================================

以下は、Self Inspect で一部項目が** 不合格** となったDriver Stationのレポート例です。
問題は赤丸の感嘆符アイコン、またはオレンジ三角の感嘆符アイコンで示されます。

このDriver Hubはファームウェアリセットされ、DSバージョンが7に戻り、すべてのシステム・DSアプリ設定が初期化されました。
その後、`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client>`_でDSバージョン10.3にアップデートし、FTCRobotControllerアプリもAndroid StudioからDSデバイスにインストールしました。

.. figure:: images/newDSerrors.png   
   :align: center
   :width: 85%
   :alt: Driver station self inspection report

   Self Inspect に問題あり！

-  項目10：``Standard Wi-Fi Connected`` が**No** （いいえ）で不合格。
   DSがまだロボットに接続されていません。デバイス接続前にDriver Station Nameを修正してください。
-  項目11：``Driver Station Name`` がFTC命名規則に合致していないため不合格。**Android_a301** は新規DSの例です。
   DSアプリ設定でDriver Station Nameを競技マニュアルのルールに従い設定してください（例：99999-DS）。
-  項目12：``Robot Controller Name`` がDS名と一致しないため不合格。**None** はDSがRCに接続されていないことを示します。
   RC名の形式が有効かどうかはチェックせず、RC名とDS名のチーム番号部分が一致しているかのみ確認します。
-  項目13：DSデバイスにRCアプリがインストールされている場合は不合格。Driver StationデバイスからRCアプリをアンインストールしてください。

各問題を修正すると、検査レポートが自動で更新され、最新状態が表示されます。

.. tip::
   Self Inspect 画面の赤丸やオレンジ三角の感嘆符アイコンをタップすると、問題に関するメッセージが一時的に表示されます。

Robot Controller Self Inspect レポート
---------------------------------------

次は**Robot Controller** Self Inspect レポートです。
通常は**Driver Station** のInspection Reports画面から「Inspect Robot Controller」メニューを選択して表示します。
参考：Control HubのHDMIポートに外部モニター、USBポートにマウスを接続すれば、Control HubからRCインスペクトレポートを直接表示できます。

.. figure:: images/newRC.png   
   :align: center
   :width: 85%
   :alt: Robot controller self inspection report

   RC Password以外はすべて正常

-  項目1：三点リーダーはメニューで、``Disable Bluetooth`` のみ選択可能です。
   Control HubでBluetoothが有効になっている場合以外は不要です。
-  項目2：``Manufacturer`` はREV Control Hubの場合、**REV Robotics** である必要があります。
-  項目3：``Model`` は**Control Hub v1.0** である必要があります。
-  項目4：``Control Hub OS Version`` は最低でも1.1.6である必要があります。**FIRST** は最新版の使用を推奨しますが、必須ではありません。
-  項目5：``Android Version`` はControl Hubの場合、通常7.1.2です。
-  項目6：``Hub Firmware`` はハブのアドレスとファームウェアバージョンを表示します。
   この例ではControl Hubのみですが、Expansion Hubも表示可能です。
   チェックマークはRCアプリのバージョンに基づき、すべてのファームウェアが最新であることを示します。
   **FIRST** は最新版の使用を推奨しますが、必須ではありません。
-  項目7：``Battery Level`` はデバイスのバッテリー残量を表示します。
-  項目8：``Bluetooth`` は**Disabled** （無効）である必要があります。
-  項目9：``RC Password`` は RC Self Inspect のみに表示されます。この項目が不合格の場合、Control Hubの初期パスワード（"password"）から変更されていないことを示します。
   Program and ManageページでManageを選択し、RCパスワードを更新してください。
   DSとRCの再ペアリング後、新しいパスワードを入力して再接続する必要があります。
-  項目10：``Wi-Fi Enabled`` は**Yes** （はい）である必要があります。Control HubのWi-Fiが**ON** であることを示します。
-  項目11：``Standard Wi-Fi Connected`` は**Yes** （はい）である必要があります。
-  項目12：``Robot Controller Name`` はFTC命名規則に合致している必要があります。チーム番号＋-RC（例：99999-RC）です。
   予備デバイスの場合は、<チーム番号>-<英字>-RC（例：12345-A-RC、12345-B-RC）となります。命名規則は競技マニュアルを参照してください。
-  項目13：Apps Installed ``Robot Controller`` はRCアプリのバージョンを表示します。**FIRST** は最新版の使用を推奨しますが、必須ではありません。
-  項目14：``Matches DS Version`` は**Yes** （はい）である必要があります。**No** の場合はバージョンの小数点以下（例：10.0と10.1）が一致していないことが原因です。バージョン不一致は許容されますが、推奨されません。
-  項目15：Apps Installed ``Driver Station`` は**Not installed** （未インストール）である必要があります。Robot ControllerデバイスにDriver Stationアプリがインストールされていないことを確認します。
   各デバイスにはFTCアプリを1つだけインストールしてください。両方インストールすると正常に動作しない場合があります。
-  項目16：RCインスペクトレポートの最下部にはQRコードが表示され、検査員がタブレットを使って検査チェックリスト項目を自動入力できます。

.. figure:: images/newRcQrCode.png   
   :align: center
   :width: 85%
   :alt: Self Inspect QR code

   検査員は検査時にQRコードをスキャンする場合があります

まとめ
-------

Self Inspect 画面は、制御システムの各要素が最新かつ正しく構成されているかをチームが確認するための、簡易的な参考情報です。

Self Inspect はFTC大会のロボット検査時に参照されることがありますが、FTCルールへの完全な準拠や公式基準を示すものでは** ありません** 。

各検査画面は、ロボットの再起動有無にかかわらず自動で更新されるため、問題が解決されたかをすばやく確認できます。

