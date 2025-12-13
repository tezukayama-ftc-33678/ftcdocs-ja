Op Mode の実行（全言語共通）
-----------------------------------

**Op Mode** がゲームパッドからの入力を必要とする場合は、Logitech F310または他の承認されたゲームパッドを **DRIVER STATION** に接続する必要があります。**DRIVER STATION** には最大2つのゲームパッドを接続できます。スマートフォンを使用する場合は、USBハブが必要です。ただし、この例では、1つのゲームパッドのみを接続します。

このタスクの完了には約10分かかります。

Op Mode の実行手順
---------------------------------

1. ゲームパッドを **DRIVER STATION** に接続します。スマートフォンを使用する場合は、Micro USB OTGアダプターケーブルが必要です。

.. image:: images/GamepadDHConnection.jpg
   :align: center

|

.. image:: images/RunningOpModeStep2.jpg
   :align: center

|

2. このWikiの例では、**Op Mode** はユーザーまたはドライバー#1として指定されたゲームパッドからの入力を探します。Logitech F310コントローラーのStartボタンとAボタンを同時に押して、ゲームパッドをユーザー#1として指定します。PS4スタイルのゲームパッドを使用している場合は、OptionsボタンとCrossボタンを使用してゲームパッドをユーザー#1として指定します。

.. image:: images/RunningOpModeStep3.jpg
   :align: center

|

   注：StartボタンとBボタンを同時に押すと、ゲームパッドがユーザー#2として指定されます。

3. **DRIVER STATION** 画面で、三角形の「**TeleOp**」ドロップダウンリストボタンをタッチして、利用可能な **Op Mode** のリストを表示します。**Robot Controller** 上にある利用可能な **Op Mode** のリストの中に、最近保存した **Op Mode** が表示されるはずです。

.. image:: images/TeleopRunDH.png
   :align: center

|

.. image:: images/RunningOpModeStep4.jpg
   :align: center

|

   注：「**TeleOp**」は「Tele-Operated」の略で、ドライバーが制御する **Op Mode** （つまり、人間のドライバーから入力を受け取る **Op Mode** ）を意味します。

4. 「MyFIRSTOpMode」を選択して、**Robot Controller** に **Op Mode** をロードします。

.. image:: images/OpModeSelectionDH.png
   :align: center

|

.. image:: images/RunningOpModeStep5.jpg
   :align: center

|

   注：**DRIVER STATION** を使用して **Op Mode** を選択していますが、実際の **Op Mode** の命令は **Robot Controller** で実行されます。

5. INITボタンを押して、**Op Mode** を初期化します。

.. image:: images/InitDH.png
   :align: center

|

.. image:: images/RunningOpModeStep6.jpg
   :align: center

|

6. Startボタン（三角形の記号で示される）を押して、**Op Mode** の実行を開始します。

.. image:: images/RunDH.png
   :align: center

|

.. image:: images/RunningOpModeStep7.jpg
   :align: center

|

7. ゲームパッドの左ジョイスティックを使用して、DCモーターの動作を制御します。左ジョイスティックを上下に操作すると、ターゲットパワーとモーターパワーが画面の右上隅に表示されるはずです。

.. image:: images/TelemetryDH.png
   :align: center

|

.. image:: images/RunningOpModeStep8.jpg
   :align: center

|

   **Op Mode** を停止したい場合は、**DRIVER STATION** の四角形のStopボタンを押します。

