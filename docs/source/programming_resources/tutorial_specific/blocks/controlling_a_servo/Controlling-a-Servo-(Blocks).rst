サーボの制御 :bdg-warning:`Blocks`
=========================================

:doc:`Blocks で Op Mode を作成する <../creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks>` セクションでは、**Blocks**プログラミングツールを使用して12V DCモーターを制御する**Op Mode**を作成する方法を学びました。このセクションでは、サーボモーターを制御する**Op Mode** を作成する方法を学びます。

サーボモーターとは？
~~~~~~~~~~~~~~~~~~~~~~

サーボモーターは、精密な動きのために設計された特殊なタイプのモーターです。典型的なサーボモーターは、動作範囲が制限されています。

以下の図では、「標準スケール」の180度サーボが示されています。このタイプのサーボは、ホビイストや **FIRST Tech Challenge**チームに人気があります。このサーボモーターは、シャフトを180度の範囲で回転させることができます。サーボコントローラーとして知られる電子モジュールを使用すると、サーボモーターを特定の位置に移動させる**Op Mode** を作成できます。モーターがこのターゲット位置に到達すると、サーボのシャフトに外力が加えられても、その位置を保持します。

.. image:: images/hs485hbServo.jpg
   :align: center

|

サーボモーターは、精密な動きをしたい場合に便利です（たとえば、ターゲットを探すためにセンサーでエリアをスイープしたり、遠隔操作の飛行機の制御面を動かしたりする場合など）。

サーボを制御するための Op Mode の変更
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

サーボモーターを制御するために必要なロジックを追加するために、**Op Mode** を変更しましょう。この例では、Logitech F310ゲームパッドのボタンを使用してサーボモーターの位置を制御します。

典型的なサーボでは、サーボのターゲット位置を指定できます。サーボはモーターシャフトを回転させてターゲット位置に移動し、その位置を乱そうとする中程度の力が加えられても、その位置を維持します。

**Blocks** のProgram & Manageサーバーでは、サーボのターゲット位置を0から1の範囲で指定できます。ターゲット位置0は0度の回転に対応し、ターゲット位置1は典型的なサーボモーターの180度の回転に対応します。

.. image:: images/servo0to80.jpg
   :align: center

|

この例では、F310コントローラーの右側にあるカラーボタンを使用してサーボの位置を制御します。最初に、**Op Mode** はサーボを中間位置（180度範囲の90度）に移動します。黄色の「Y」ボタンを押すと、サーボが0度の位置に移動します。青色の「X」ボタンまたは赤色の「B」ボタンを押すと、サーボが90度の位置に移動します。緑色の「A」ボタンを押すと、サーボが180度の位置に移動します。

.. image:: images/LogitechF310.jpg
   :align: center

|


サーボモーターを制御するための Op Mode の変更手順
-----------------------------------------------------------

1. ラップトップが **Robot Controller** のProgram & Manage Wi-Fiネットワークにまだ接続されていることを確認します。

2. 「MyFIRSTOpMode」が編集用に開かれていることを確認します。開かれていない場合は、ラップトップのブラウザウィンドウの左上隅にある **FIRST**ロゴをクリックします。これにより、メインの**Blocks** 開発ツールプロジェクト画面に移動します。

.. image:: images/ControlServoStep2ControlHub.jpg
   :align: center

|

   まだ開かれていない場合は、「MyFIRSTOpMode」プロジェクトをクリックして編集用に開きます。

3. 画面の左側にある「Actuators」カテゴリをクリックし、「Servos」サブカテゴリを探します。

.. image:: images/ControlServoStep3ControlHub.jpg
   :align: center

|

4. 利用可能なServoブロックのリストから「set **servoTest.Position** to」ブロックを選択します。

.. image:: images/ControlServoStep4ControlHub.jpg
   :align: center

|

5. 「set **servoTest.Position** to」ブロックを「Put initialization blocks here.」と書かれたコメントブロックのすぐ下にドラッグします。ブロックは所定の位置にクリックして収まるはずです。

.. image:: images/ControlServoStep5ControlHub.jpg
   :align: center

|

6. 数値ブロック「0」をクリックし、ブロックの値を「0.5」に変更します。

.. image:: images/ControlServoStep6ControlHub.jpg
   :align: center

|

   ユーザーがこの **Op Mode** を選択すると、サーボ位置は最初に中間点（90度の位置）に設定されます。

7. プログラミングブロックの「Logic」カテゴリをクリックし、利用可能なブロックのリストから「if do」ブロックを選択します。ブロックを「Put loop blocks here.」と書かれたコメントブロックの直後の位置にドラッグします。

.. image:: images/ControlServoStep7ControlHub.jpg
   :align: center

|

   ブロックは所定の位置にクリックして収まるはずです。

8. プログラミングブロックの「Gamepad」カテゴリをクリックし、利用可能なブロックのリストから「**gamepad1.Y**」ブロックを選択します。

.. image:: images/ControlServoStep8ControlHub.jpg
   :align: center

|

   注：このブロックはブロックのリストの下部にあります。このブロックを選択する前に、リストの最後までスクロールダウンする必要がある場合があります。

9. 「**gamepad1.Y**」ブロックを「if do」ブロックの右側にドラッグします。ブロックは所定の位置にクリックして収まるはずです。

.. image:: images/ControlServoStep9ControlHub.jpg
   :align: center

|

   「if do」ブロックは、**gamepad1.Y** 値の状態をテスト条件として使用します。「Y」ボタンが押されると、ブロックの「do」部分内のステートメントが実行されます。

10. 画面の左側にある「Actuators」カテゴリをクリックし、「Servos」サブカテゴリを探します。

.. image:: images/ControlServoStep10ControlHub.jpg
   :align: center

|

11. 利用可能なServoブロックのリストから「set **servoTest.Position** to」ブロックを選択します。

.. image:: images/ControlServoStep11ControlHub.jpg
   :align: center

|

12. 「set **servoTest.Position** to」ブロックを「if do」ブロックの「do」部分にスナップするようにドラッグします。

.. image:: images/ControlServoStep12ControlHub.jpg
   :align: center

|

   ゲームパッド#1で「Y」ボタンが押されると、**Op Mode** はサーボの位置を0度の位置に移動します。

13. 「if do」ブロックの青と白のSettingsアイコンをクリックします。これにより、「if do」ブロックを変更できるポップアップメニューが表示されます。

.. image:: images/ControlServoStep13ControlHub.jpg
   :align: center

|

14. ポップアップメニューの左側から「else if」ブロックをドラッグし、「if」ブロックの下に所定の位置にスナップします。

.. image:: images/ControlServoStep14ControlHub.jpg
   :align: center

|

   2番目の「else if」ブロックを左側からドラッグし、最初の「else if」ブロックの下の右側に所定の位置にスナップします。

15. Settingsアイコンをクリックして、「if do」ブロックのポップアップメニューを非表示にします。「if do」ブロックに2つの「else if」テスト条件が追加されているはずです。

.. image:: images/ControlServoStep15ControlHub.jpg
   :align: center

|

16. 「Logic」カテゴリをクリックし、論理「and」ブロックを選択します。

.. image:: images/ControlServoStep16ControlHub.jpg
   :align: center

|

17. 「and」ブロックを最初の「else if」ブロックのテスト条件として所定の位置にクリックするようにドラッグします。

.. image:: images/ControlServoStep17ControlHub.jpg
   :align: center

|

18. 「and」という単語をクリックし、ポップアップメニューから「or」を選択して、ブロックを論理「or」ブロックに変更します。

.. image:: images/ControlServoStep18ControlHub.jpg
   :align: center

|

19. 「Gamepad」カテゴリをクリックし、「**gamepad1.X**」ブロックを選択します。ブロックを論理「or」ブロックの最初のテスト条件として所定の位置にクリックするようにドラッグします。

.. image:: images/ControlServoStep19ControlHub.jpg
   :align: center

|

20. 「Gamepad」カテゴリをクリックし、「**gamepad1.B**」ブロックを選択します。ブロックを論理「or」ブロックの2番目のテスト条件として所定の位置にクリックするようにドラッグします。

.. image:: images/ControlServoStep20ControlHub.jpg
   :align: center

|

21. 「set **servoTest.Position** to」ブロックを選択し、最初の「else-if」ブロックの「do」句に配置します。

.. image:: images/ControlServoStep21ControlHub.jpg
   :align: center

|

22. 数値「0」をハイライトし、「0.5」に変更します。この変更により、ユーザーがゲームパッド#1で「X」ボタンまたは「B」ボタンを押すと、**Op Mode** はサーボを中間（90度）の位置に移動します。

.. image:: images/ControlServoStep22ControlHub.jpg
   :align: center

|

23. 2番目の「else if」ブロックのテスト条件として「**gamepad1.A**」ブロックを使用します。「set**servoTest.position** to」ブロックを2番目の「else if」ブロックの「do」句にドラッグし、サーボの位置が値1に設定されるように数値を変更します。

.. image:: images/ControlServoStep23ControlHub.jpg
   :align: center

|

   この句では、#1ゲームパッドで「A」ボタンが押されると、**Op Mode** はサーボを180度の位置に移動します。

24. 「call **Telemetry.update**」ブロックの前に「call**telemetry.addData**」ブロック（数値版）を挿入します。キーフィールドを「Servo Position」に変更し、数値フィールドに「**servoTest.Position**」ブロックを挿入します。

.. image:: images/ControlServoStep24ControlHub.jpg
   :align: center

|

   このブロックのセットは、**Op Mode**の実行中に現在のサーボ位置の値を**DRIVER STATION** に送信します。

25. **Op Mode**を保存し、**Robot Controller** に正常に保存されたことを確認します。

.. image:: images/ControlServoStep25ControlHub.jpg
   :align: center

|

26. :doc:`Op Mode の実行 <../running_op_modes/Running-Your-Op-Mode>` セクションで説明されている手順に従って、更新された **Op Mode**を実行します。また、**Op Mode** を実行する前に、ゲームパッドがユーザー#1として指定されていることを確認してください。

.. image:: images/ControlServoStep26ControlHub.jpg
   :align: center

|

   これで、カラーボタンでサーボの位置を制御できるようになります。サーボの位置は **DRIVER STATION** に表示されるはずです。


