センサーの使用 :bdg-info:`OBJ`
==============================

カラー距離センサー
~~~~~~~~~~~~~~~~~~

センサーは、**Robot Controller** が環境に関する情報を取得できるようにするデバイスです。この例では、**REV Robotics** のカラー距離センサーを使用して、範囲（オブジェクトからの距離）情報を Driver Station に表示します。

カラー距離センサーは、反射光を使用して、センサーからターゲットオブジェクトまでの距離を判定します。これは、妥当な精度で近距離（5 インチ以上）を測定するために使用できます。このドキュメントが最近編集された時点では、**REV** カラー距離センサーは約 2 インチ（5cm）で飽和することに注意してください。これは、2 インチ以下の距離では、センサーが約 2 インチに等しい測定距離を返すことを意味します。

距離情報（センチメートル単位）を **Driver Station** に送信するテレメトリーステートメントを追加するように、**op mode** を変更します。

.. code-block:: java

   telemetry.addData("Servo Position", servoTest.getPosition());
   telemetry.addData("Target Power", tgtPower);
   telemetry.addData("Motor Power", motorTest.getPower());
   telemetry.addData("Distance (cm)", sensorColorRange.getDistance(DistanceUnit.CM));
   telemetry.addData("Status", "Running");
   telemetry.update();

After you have modified your op mode, push the build button, then run
the op mode to verify that it now displays distance on your Driver
Station. Note that if the distance reads "NaN" (short for "Not a
Number") it probably means that your sensor is too far from the target
(zero reflection). Also note that the sensor saturates at around 5 cm.

Touch Sensor
~~~~~~~~~~~~

The REV Robotics Touch Sensor can be connected to a digital port on the
Control Hub or Expansion Hub. The Touch Sensor is HIGH (returns TRUE) when it is not
pressed. It is pulled LOW (returns FALSE) when it is pressed.

.. image:: images/REVTouchSensor.jpg
   :align: center

|

The Control Hub or Expansion Hub digital ports contain two digital pins per port. When
you use a 4-wire JST cable to connect a REV Robotics Touch sensor to a Control Hub or
Expansion Hub digital port, the Touch Sensor is wired to the second of
the two digital pins within the port. The first digital pin of the
4-wire cable remains disconnected.

For example, if you connect a Touch Sensor to the "0,1" digital port of
the Control Hub or Expansion Hub, the Touch Sensor will be connected to the second pin
(labeled "1") of the port. The first pin (labeled "0") will stay
disconnected.

Modify the code in your op mode that occurs before the waitForStart
command to set the digital channel for input mode.

.. code-block:: java

   // set digital channel to input mode.
   digitalTouch.setMode(DigitalChannel.Mode.INPUT);

   telemetry.addData("Status", "Initialized");
   telemetry.update();
   // Wait for the game to start (driver presses PLAY)
   waitForStart();

Also, modify the code in your while loop to add an if-else statement
that checks the state of the digital input channel. If the channel is
LOW (false), the touch sensor button is pressed and being pulled LOW to
ground. Otherwise, the touch sensor button is not pressed.

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

Rebuild your op mode, then reinitialize and restart your op mode. The op
mode should now display the state of the button ("PRESSED" or "NOT
PRESSED").

