カラー距離センサーの構成
=====================================

**REV Robotics カラー距離センサー**は I2C センサーです。実際には、2 つのセンサー機能を 1 つのデバイスに組み合わせています。これは、物体の色を判定できるカラーセンサーです。また、短距離を測定するために使用できる距離またはレンジセンサーでもあります。このチュートリアルでは、「distance（距離）」という言葉が「range（範囲）」という言葉と同じ意味で使用されていることに注意してください。

Configuring a Color Distance Sensor Instructions
------------------------------------------------

1. 画面の **I2C Bus 0** という言葉をタッチして、この I2C バスの I2C 構成画面を起動します。

.. image:: images/ConfiguringHardwareColorDistanceStep1.jpg
   :align: center

|

**Control Hub** または **Expansion Hub** には、「0」から「3」とラベル付けされた 4 つの独立した I2C バスがあります。この例では、カラーセンサーを「0」とラベル付けされたポートに接続したため、I2C バス 0 に配置されます。

2. **I2C Bus 0** 画面を見てください。このバス用に既に構成されているセンサーがあるはずです。**Control Hub** または **Expansion Hub** には、独自の内蔵慣性測定ユニット（IMU）センサーがあります。このセンサーは、ロボットの方向を決定したり、ロボットの加速度を測定したりするために使用できます。

.. image:: images/ConfiguringHardwareColorDistanceStep2.jpg
   :align: center

|

内蔵 IMU は、各 **Control Hub** または **Expansion Hub** の I2C バス 0 に内部的に接続されています。**Robot Controller** を使用して **Control Hub** または **Expansion Hub** を構成するたびに、アプリは I2C バス 0 の IMU を自動的に構成します。カラーセンサーを構成できるようにするには、このバス用に別の I2C デバイスを追加する必要があります。

3. Press the **Add** button to add another I2C device to this bus.    

.. image:: images/ConfiguringHardwareColorDistanceStep3.jpg
   :align: center

|

4. Select "REV Color/Range Sensor" from the dropdown selector for     
this new device. Use the touchscreen keyboard to name this device     
"sensorColorRange".                                                   

.. image:: images/ConfiguringHardwareColorDistanceStep4.jpg
   :align: center

|

5. Press the **Done** button to complete the I2C sensor               
configuration. The app should return to the previous screen.          

.. image:: images/ConfiguringHardwareColorDistanceStep5.jpg
   :align: center

|