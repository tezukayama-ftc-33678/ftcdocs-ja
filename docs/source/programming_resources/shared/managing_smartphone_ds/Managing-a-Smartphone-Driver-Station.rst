**Driver Hub** の管理
=====================

**REV Driver Hub**
~~~~~~~~~~~~~~~~~~

`REV Driver Hub <https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications>`__ には、**Driver Station (DS)** アプリがプリロードされています。以下の **REV Driver Hub** について説明する手順は、**Android** スマートフォンを DS として使用する場合にも適用されます。

名前の変更
~~~~~~~~~~~~~~~~~

**Competition Manual** に準拠するために、**Driver Station (DS)** の名前を変更する必要があります。チーム番号に合わせてデバイスを構成します。使用する **ROBOT CONTROLLER**、**DRIVER STATION**、および予備は、次のように正しいチーム番号に対応するように構成/名前を付ける必要があります：

A.     **ROBOT CONTROLLER** は <チーム番号>-RC（例：12345-RC）という名前にする必要があります。

B.     **DRIVER STATION** は <チーム番号>-DS（例：12345-DS）という名前にする必要があります。

C.     予備の **ROBOT CONTROLLER** または **DRIVER STATION** が構成されている場合、文字指定子を追加できます <チーム番号>-<文字>-RC/DS（例：12345-A-DS、12345-B-DS）

*Control, Command & Signals System* に関連する規則については、現在の **Competition Manual** を確認してください。

**Driver Hub** の名前は、以下に説明するように DS アプリで変更できます。

.. note:: 以下の手順は、ドライバーステーションに **Android** スマートフォンを使用する場合でも、ほとんど同じです。

   制御システムにスマートフォンを使用している場合、:ref:`このリンク <programming_resources/shared/configuring_android/Configuring-Your-Android-Devices:Renaming Your Smartphones>` は、スマートフォンの Android Settings アクティビティを使用してスマートフォンの名前を変更する方法を示しています。

.. tip:: トラブルシューティング

   DS 画面に黄色の丸い感嘆符アイコンが表示され、それをタッチすると、「*DS* does not match *DS*, see the FTC Competition Manual」というメッセージが一時的にポップアップ表示されます。
   注：*DS* は **Driver Station** の現在の名前で、*RC* は現在の **Robot Controller** の名前です。
   
   これは、DS と RC の名前が一致しないためです。**Competition Manual** で要求されているように、上記のように両方の名前をチーム番号を含むように変更する必要があります。
   
   .. image:: images/ds-mismatch-screen.png
      :align: center
      :alt: 黄色のアイコンの不一致と名前の不一致ポップアップメッセージを示す Driver Station 画面。

**Driver Station** の名前を変更する手順
--------------------------------------------------

1. **Driver Station** アプリで、右上隅の3つのドットをタッチして、ポップアップメニューを表示します。

.. image:: images/touchThreeDots1.png
   :align: center
   :alt: 3つのドットがオレンジ色の円で強調表示された Driver Station メイン画面。

|

2. ポップアップメニューから *Settings* メニュー項目を選択します。

.. image:: images/selectSettings.png
   :align: center
   :alt: Settings オプションが強調表示されたポップアップメニュー。

|

3. *Driver Station Name* をタッチします。

.. image:: images/clickDriverStationName.png
   :align: center
   :alt: Driver Station Name が強調表示された Settings 画面。

|

4. 新しい **Driver Station** 名を入力し、OK をタッチして変更を保存します。

.. image:: images/specifyNewDriverStationName.png
   :align: center
   :alt: 新しい名前を入力するためのダイアログボックス。

|

5. 変更を確認します。

.. image:: images/aboutDriverStation.png
   :align: center
   :alt: 新しい名前を表示する Settings 画面。


プログラムと管理ページへのアクセス
---------------------------------------

**Driver Hub** には、**Program & Manage** Web サーバーへのアクセスを提供する専用ボタンはありません。ただし、**Driver Station** アプリを使用して、**Robot Controller** の **Program & Manage** ページにアクセスできます。

1. **Driver Station** アプリで、右上隅の3つのドットをタッチします。

2. *Program & Manage* を選択します。

3. Web ブラウザーが開き、**Robot Controller** の **Program & Manage** ページが表示されます（**Robot Controller** がペアリングされ、アクティブである場合）。

.. note:: この機能を使用するには、**Driver Station** が **Robot Controller** に接続されている必要があります。


バッテリーレベルの確認
------------------------

**Driver Hub** のバッテリーレベルは、デバイスの上部に表示されます。バッテリーアイコンは、現在の充電レベルを示します。

.. note:: **Driver Hub** は、標準の USB-C 充電器を使用して充電できます。試合中は、**Driver Hub** を電源に接続したままにすることをお勧めします。


まとめ
-------

**Driver Hub** は、**Driver Station** アプリを実行するための専用デバイスです。使いやすく、スマートフォンを **Driver Station** として使用するよりも堅牢です。名前の変更、**Program & Manage** ページへのアクセス、バッテリーレベルの確認は、すべて **Driver Station** アプリから直接実行できます。
