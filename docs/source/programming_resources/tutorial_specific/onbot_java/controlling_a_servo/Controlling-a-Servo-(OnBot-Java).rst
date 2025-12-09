サーボの制御 :bdg-info:`OBJ`
===================================

このセクションでは、ゲームパッドのボタンでサーボモーターを制御するように **Op Mode** を変更します。

サーボモーターとは？
~~~~~~~~~~~~~~~~~~~~~~

サーボモーターは特殊なタイプのモーターです。サーボモーターは精密な動作を目的として設計されています。一般的なサーボモーターは可動範囲が制限されています。

下の図には、「標準スケール」の180度サーボが示されています。このタイプのサーボは、ホビイストや **FIRST Tech Challenge** チームに人気があります。このサーボモーターは、シャフトを180度の範囲で回転させることができます。サーボコントローラーと呼ばれる電子モジュールを使用して、サーボモーターを特定の位置に移動する **Op Mode** を作成できます。モーターが目標位置に達すると、サーボのシャフトに外力が加わっても、その位置を保持します。

.. image:: images/hs485hbServo.jpg
   :align: center

|

サーボモーターは、精密な動作を行いたい場合に便利です（例えば、ターゲットを探すためにセンサーで範囲をスキャンしたり、ラジコン飛行機の操縦翼面を動かしたりする場合など）。

サーボを制御するための Op Mode の変更
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

サーボモーターを制御するために必要なロジックを追加するために、**Op Mode** を変更しましょう。この例では、Logitech F310 ゲームパッドのボタンを使用して、サーボモーターの位置を制御します。

一般的なサーボでは、サーボの目標位置を指定できます。サーボはモーターシャフトを回転させて目標位置に移動し、その位置を乱そうとする適度な力が加えられても、その位置を維持します。

**FIRST Tech Challenge** 制御システムでは、サーボの目標位置を 0 から 1 の範囲で指定できます。目標位置 0 は回転角度 0 度に対応し、目標位置 1 は一般的なサーボモーターの回転角度 180 度に対応します。

.. image:: images/servo0to80.jpg
   :align: center

|

この例では、F310 コントローラーの右側にあるカラーボタンを使用して、サーボの位置を制御します。最初に、**Op Mode** はサーボを中間位置（180度範囲の90度）に移動します。黄色の「Y」ボタンを押すと、サーボは 0 度の位置に移動します。青色の「X」ボタンまたは赤色の「B」ボタンを押すと、サーボは 90 度の位置に移動します。緑色の「A」ボタンを押すと、サーボは 180 度の位置に移動します。

.. image:: images/LogitechF310.jpg
   :align: center

|

**Op Mode** を変更して、以下のコードを追加します：

.. code-block:: java

   // run until the end of the match (driver presses STOP)
   double tgtPower = 0;
   while (opModeIsActive()) {
       tgtPower = -this.gamepad1.left_stick_y;
       motorTest.setPower(tgtPower);
       // check to see if we need to move the servo.
       if(gamepad1.y) {
           // move to 0 degrees.
           servoTest.setPosition(0);
       } else if (gamepad1.x || gamepad1.b) {
           // move to 90 degrees.
           servoTest.setPosition(0.5);
       } else if (gamepad1.a) {
           // move to 180 degrees.
           servoTest.setPosition(1);
       }
       telemetry.addData("Servo Position", servoTest.getPosition());
       telemetry.addData("Target Power", tgtPower);
       telemetry.addData("Motor Power", motorTest.getPower());
       telemetry.addData("Status", "Running");
       telemetry.update();

   }

この追加されたコードは、F310 ゲームパッドのカラーボタンのいずれかが押されているかどうかをチェックします。Y ボタンが押されると、サーボは 0 度の位置に移動します。X ボタンまたは B ボタンのいずれかが押されると、サーボは 90 度の位置に移動します。A ボタンが押されると、サーボは 180 度の位置に移動します。**Op Mode** は、サーボの位置に関するテレメトリデータを **Driver Station** に送信します。

**Op Mode** を変更した後、ビルドして実行できます。ゲームパッド #1 がまだ構成されていることを確認してから、カラーボタンを使用してサーボの位置を移動させます。


