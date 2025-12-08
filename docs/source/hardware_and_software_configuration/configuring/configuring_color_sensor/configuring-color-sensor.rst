カラー距離センサーの構成
=====================================

**REV Robotics カラー距離センサー**は I2C センサーです。実際には、2 つのセンサー機能を 1 つのデバイスに組み合わせています。これは、物体の色を判定できるカラーセンサーです。また、短距離を測定するために使用できる距離またはレンジセンサーでもあります。このチュートリアルでは、「distance（距離）」という言葉が「range（範囲）」という言葉と同じ意味で使用されていることに注意してください。

Configuring a Color Distance Sensor Instructions
------------------------------------------------

1. Touch the words **I2C Bus 0** on the screen to launch the I2C      
configuration screen for this I2C bus.                                

.. image:: images/ConfiguringHardwareColorDistanceStep1.jpg
   :align: center

|

The Control Hub or Expansion Hub has four independent I2C buses, labeled "0" through "3".  In this example, since you connected the Color Sensor to the port labeled "0", it resides on I2C Bus 0.

2. Look at the **I2C Bus 0** screen. There should already be a sensor 
configured for this bus. The Control Hub or Expansion Hub has its own built-in       
inertial measurement unit (IMU) sensor. This sensor can be used to    
determine the orientation of a robot, as well as measure the          
accelerations on a robot.                                             

.. image:: images/ConfiguringHardwareColorDistanceStep2.jpg
   :align: center

|

The built-in IMU is internally connected to I2C Bus 0 on each Control Hub or Expansion Hub.  Whenever you configure a Control Hub or Expansion Hub using the Robot Controller, the app automatically configures the IMU for I2C Bus 0. You will need to add another I2C device for this bus to be able to configure the color sensor.

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