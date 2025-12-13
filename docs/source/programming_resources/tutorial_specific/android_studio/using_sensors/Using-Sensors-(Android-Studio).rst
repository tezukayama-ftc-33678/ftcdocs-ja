センサーの使用 :bdg-success:`AS`
================================

カラー距離センサー
~~~~~~~~~~~~~~~~~~~~~

センサーは、**Robot Controller** がその環境に関する情報を取得できるようにするデバイスです。この例では、**REV Robotics** のカラー距離センサーを使用して、範囲（物体からの距離）情報を **Driver Station** に表示します。

カラー距離センサーは、反射光を使用してセンサーからターゲット物体までの距離を測定します。このセンサーは、近距離（最大5インチ程度）を適切な精度で測定できます。このドキュメントが最後に編集された時点では、**REV** カラー距離センサーは約2インチ（5cm）で飽和することに注意してください。これは、2インチ以下の距離では、センサーが約2インチに等しい測定距離を返すことを意味します。

距離情報（センチメートル単位）を **Driver Station** に送信するテレメトリーステートメントを追加するように、**Op Mode** を変更します。

.. code-block:: java

   telemetry.addData("Servo Position", servoTest.getPosition());
   telemetry.addData("Target Power", tgtPower);
   telemetry.addData("Motor Power", motorTest.getPower());
   telemetry.addData("Distance (cm)", sensorColorRange.getDistance(DistanceUnit.CM));
   telemetry.addData("Status", "Running");
   telemetry.update();

**Op Mode** を変更した後、更新された **Robot Controller** アプリをビルドしてインストールし、**Op Mode** を実行して、**Driver Station** に距離が表示されることを確認します。距離が「NaN」（「Not a Number」の略）と表示される場合は、おそらくセンサーがターゲットから遠すぎる（反射がゼロ）ことを意味します。また、センサーは約5cmで飽和することに注意してください。

タッチセンサー
~~~~~~~~~~~~~~

**REV Robotics** のタッチセンサーは、**Control Hub** または **Expansion Hub** のデジタルポートに接続できます。タッチセンサーは、押されていない場合はHIGH（TRUEを返す）です。押されると、LOW（FALSEを返す）になります。

.. image:: images/REVTouchSensor.jpg
   :align: center

|

**Control Hub** または **Expansion Hub** のデジタルポートには、1つのポートあたり2つのデジタルピンが含まれています。4線式JSTケーブルを使用して **REV Robotics** のタッチセンサーを **Control Hub** または **Expansion Hub** のデジタルポートに接続すると、タッチセンサーはポート内の2つのデジタルピンの2番目に配線されます。4線式ケーブルの最初のデジタルピンは接続されないままになります。

たとえば、タッチセンサーを **Control Hub** または **Expansion Hub** の「0,1」デジタルポートに接続する場合、タッチセンサーはポートの2番目のピン（「1」とラベル付けされている）に接続されます。最初のピン（「0」とラベル付けされている）は接続されないままになります。

デジタルチャンネルを入力モードに設定するために、**waitForStart** コマンドの前に発生する **Op Mode** のコードを変更します。

.. code-block:: java

   // set digital channel to input mode.
   digitalTouch.setMode(DigitalChannel.Mode.INPUT);

   telemetry.addData("Status", "Initialized");
   telemetry.update();
   // Wait for the game to start (driver presses PLAY)
   waitForStart();

また、whileループ内のコードを変更して、デジタル入力チャンネルの状態をチェックするif-else文を追加します。チャンネルがLOW（false）の場合、タッチセンサーボタンが押されており、グラウンドにLOWで引かれています。それ以外の場合は、タッチセンサーボタンは押されていません。

.. code-block:: java

   // is button pressed?
   if (digitalTouch.getState() == false) {
       // button is pressed.
       telemetry.addData("Button", "PRESSED");
   } else {
       // button is not pressed.
       telemetry.addData("Button", "NOT PRESSED");
   }

   telemetry.addData("Status", "Running");
   telemetry.update();

更新された **Robot Controller** アプリをビルドしてインストールし、**Op Mode** を再初期化して再起動します。**Op Mode** は、ボタンの状態（「PRESSED」または「NOT PRESSED」）を表示するようになります。

