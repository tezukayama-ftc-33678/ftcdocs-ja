サーボの制御 :bdg-success:`AS`
=====================================

このセクションでは、ゲームパッドのボタンでサーボモーターを制御するように **Op Mode** を変更します。

サーボモーターとは何ですか？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

サーボモーターは特殊なタイプのモーターです。サーボモーターは精密な動作を実現するために設計されています。一般的なサーボモーターは、可動範囲が限られています。

以下の図には、「標準スケール」の180度サーボが示されています。このタイプのサーボは、ホビイストや **FIRST Tech Challenge** チームに人気があります。このサーボモーターは、シャフトを180度の範囲で回転させることができます。サーボコントローラーとして知られる電子モジュールを使用すると、サーボモーターを特定の位置に移動させる**Op Mode** を作成できます。モーターがこの目標位置に到達すると、サーボのシャフトに外力が加えられても、その位置を保持します。

.. image:: images/hs485hbServo.jpg
   :align: center

|

サーボモーターは、正確な動きを実現したい場合に便利です（たとえば、センサーでエリアをスキャンしてターゲットを探したり、リモートコントロール飛行機の操縦舵面を動かしたりする場合）。

サーボを制御するための **Op Mode** の変更
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

サーボモーターを制御するために必要なロジックを追加するように **Op Mode** を変更しましょう。この例では、Logitech F310ゲームパッドのボタンを使用して、サーボモーターの位置を制御します。

一般的なサーボでは、サーボの目標位置を指定できます。サーボはモーターシャフトを回転させて目標位置に移動し、その後、その位置を乱そうとする適度な力が加えられても、その位置を保持します。

**FIRST Tech Challenge** 制御システムでは、サーボの目標位置を0から1の範囲で指定できます。目標位置0は回転角度0度に対応し、目標位置1は一般的なサーボモーターの回転角度180度に対応します。

.. image:: images/servo0to80.jpg
   :align: center

|

この例では、F310コントローラーの右側にある色付きボタンを使用して、サーボの位置を制御します。最初に、**Op Mode** はサーボを中間位置（180度範囲の90度）に移動させます。黄色の「Y」ボタンを押すと、サーボは0度の位置に移動します。青色の「X」ボタンまたは赤色の「B」ボタンを押すと、サーボは90度の位置に移動します。緑色の「A」ボタンを押すと、サーボは180度の位置に移動します。

.. image:: images/LogitechF310.jpg
   :align: center

|

次のコードを追加するように **Op Mode** を変更します：

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

この追加されたコードは、F310ゲームパッドの色付きボタンのいずれかが押されているかどうかをチェックします。Yボタンが押されている場合、サーボは0度の位置に移動します。XボタンまたはBボタンのいずれかが押されている場合、サーボは90度の位置に移動します。Aボタンが押されている場合、サーボは180度の位置に移動します。また、**Op Mode** はサーボ位置に関するテレメトリーデータを**Driver Station** に送信します。

**Op Mode** を変更した後、ビルドして実行できます。ゲームパッド#1がまだ構成されていることを確認してから、色付きボタンを使用してサーボの位置を移動します。

