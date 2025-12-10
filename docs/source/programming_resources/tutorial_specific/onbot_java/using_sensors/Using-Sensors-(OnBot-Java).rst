センサーの使用 :bdg-info:`OBJ`
=============================

Color-Distance センサー
~~~~~~~~~~~~~~~~~~~~~

センサーは、**Robot Controller** が環境に関する情報を取得できるようにするデバイスです。この例では、**REV Robotics** Color-Distance センサーを使用して、範囲（オブジェクトからの距離）情報を **Driver Station** に表示します。

Color-Range センサーは反射光を使用して、センサーからターゲットオブジェクトまでの距離を測定します。合理的な精度で近距離（5インチ以上）を測定するために使用できます。このドキュメントが最後に編集された時点で、REV Color-Range センサーは約2インチ（5cm）で飽和することに注意してください。これは、2インチ以下の距離では、センサーが約2インチに等しい測定距離を返すことを意味します。

**Op Mode** を変更して、距離情報（センチメートル単位）を **Driver Station** に送信するテレメトリステートメントを追加します。

.. code-block:: java

   telemetry.addData("Servo Position", servoTest.getPosition());
   telemetry.addData("Target Power", tgtPower);
   telemetry.addData("Motor Power", motorTest.getPower());
   telemetry.addData("Distance (cm)", sensorColorRange.getDistance(DistanceUnit.CM));
   telemetry.addData("Status", "Running");
   telemetry.update();

**Op Mode** を変更した後、ビルドボタンを押してから **Op Mode** を実行し、**Driver Station** に距離が表示されることを確認します。距離が「NaN」（「Not a Number」の略）と表示される場合は、センサーがターゲットから遠すぎる（反射がゼロ）ことを意味している可能性があります。また、センサーは約5cmで飽和することにも注意してください。

タッチセンサー
~~~~~~~~~~~~

**REV Robotics** タッチセンサーは、**Control Hub** または **Expansion Hub** のデジタルポートに接続できます。タッチセンサーは、押されていない場合は HIGH（TRUE を返す）です。押されると LOW（FALSE を返す）に引き下げられます。

.. image:: images/REVTouchSensor.jpg
   :align: center

|

**Control Hub** または **Expansion Hub** のデジタルポートには、ポートごとに2つのデジタルピンが含まれています。4線式 JST ケーブルを使用して **REV Robotics** タッチセンサーを **Control Hub** または **Expansion Hub** のデジタルポートに接続すると、タッチセンサーはポート内の2つのデジタルピンのうち2番目のピンに配線されます。4線式ケーブルの最初のデジタルピンは未接続のままです。

例えば、タッチセンサーを **Control Hub** または **Expansion Hub** の「0,1」デジタルポートに接続すると、タッチセンサーはポートの2番目のピン（「1」とラベル付けされている）に接続されます。最初のピン（「0」とラベル付けされている）は未接続のままです。

**Op Mode** 内の waitForStart コマンドの前に発生するコードを変更して、デジタルチャネルを入力モードに設定します。

.. code-block:: java

   // set digital channel to input mode.
   digitalTouch.setMode(DigitalChannel.Mode.INPUT);

   telemetry.addData("Status", "Initialized");
   telemetry.update();
   // Wait for the game to start (driver presses PLAY)
   waitForStart();

また、while ループ内のコードを変更して、デジタル入力チャネルの状態をチェックする if-else ステートメントを追加します。チャネルが LOW（false）の場合、タッチセンサーボタンが押されており、グラウンドに LOW に引き下げられています。それ以外の場合、タッチセンサーボタンは押されていません。

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

**Op Mode** を再ビルドしてから、**Op Mode** を再初期化して再起動します。**Op Mode** は、ボタンの状態（「PRESSED」または「NOT PRESSED」）を表示するようになります。

