センサーの使用 :bdg-warning:`Blocks`
====================================

カラー距離センサー
~~~~~~~~~~~~~~~~~~

センサーは、**Robot Controller** が環境に関する情報を取得できるようにするデバイスです。この例では、**REV Robotics** のカラー距離センサーを使用して、範囲（オブジェクトからの距離）情報を **DRIVER STATION** に表示します。

カラー距離センサーは、反射光を使用して、センサーからターゲットオブジェクトまでの距離を判定します。これは、妥当な精度で近距離（5 インチ以上）を測定するために使用できます。このドキュメントが最近編集された時点では、**REV** カラー距離センサーは約 2 インチ（5cm）で飽和することに注意してください。これは、2 インチ以下の距離では、センサーが約 2 インチに等しい測定距離を返すことを意味します。

このタスクを完了するには約 15 分かかる見込みです。

距離を表示するための Op Mode の変更手順
---------------------------------------

1. ラップトップが **Robot Controller** の Program & Manage Wi-Fi ネットワークにまだ接続されていることを確認します。                          

2. Verify that "MyFIRSTOpMode" is opened for editing. If it is not,   
you can click on the FIRST logo in the upper left hand corner of the  
browser window on the laptop. This should take you to the main 
Blocks Development Tool project screen.                               

.. image:: images/DistanceSensorStep2ControlHub.jpg
   :align: center

|

   Click on the "MyFIRSTOpMode" project to open it for editing if it is not already opened.

3. Click on the "Utilities" category on the left-hand side of your    
browser. Find and click on the "Telemetry" subcategory.               

.. image:: images/DistanceSensorStep3ControlHub.jpg
   :align: center

|

4. Select the "call telemetry.addData" block (the numeric version)    
and drag it to the spot in your "while" loop block immediately before 
the "telemetry.update" block.                                         

.. image:: images/DistanceSensorStep4ControlHub.jpg
   :align: center

|

5. Click and highlight the "key" text and change the text so it reads 
"Distance (cm)".                                                      

.. image:: images/DistanceSensorStep5ControlHub.jpg
   :align: center

|

6. Click and expand the "Sensors" category. Click on the "REV         
Color/Range Sensor" subcategory. Click on and select the "call        
sensorColorRange.getDistance" programming block.                      

.. image:: images/DistanceSensorStep6ControlHub.jpg
   :align: center

|

   Note that earlier versions of the Blocks Programming tool refer to the REV Robotics Color-Distance Sensor as the "LynxI2cColorRangeSensor".  Newer versions of the software refer to the device as the "REV Color/Range Sensor".

7. Drag the "call sensorColorRange.getDistance" programming block to  
the "number" field of the "call telemetry.addData" programming block. 

.. image:: images/DistanceSensorStep7ControlHub.jpg
   :align: center

|

   This will send the measured distance to the target in centimeters back to the DRIVER STATION.

8. Save your op mode and verify that it was saved successfully to the 
Robot Controller.                                                     

.. image:: images/DistanceSensorStep8ControlHub.jpg
   :align: center

|

9. Follow the procedure outlined in the section titled :doc:`Running Your  
OpMode <../running_op_modes/Running-Your-Op-Mode>` 
to run your updated op mode.                                          

.. image:: images/DistanceSensorStep9ControlHub.jpg
   :align: center

|

   As you run the op mode, if you move your hand above the color light sensor, you should see the measured distance change on the DRIVER STATION screen.  If the expression "NaN" (not a number) is displayed on the DRIVER STATION, the target is most likely out of range (and the sensor does not detect any reflected light).

Touch Sensor
~~~~~~~~~~~~

For this example, we assume that the REV Robotics Touch Sensor has been
configured as a digital touch sensor in the Robot Controller's active
configuration file. We will use the "isPressed" programming block to
determine if the button on the sensor is currently pressed or not.

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

Note that it will take an estimated 15 minutes to complete this task.

Modifying the Op Mode to Display Button (Touch Sensor) State Instructions
-------------------------------------------------------------------------

1. Verify that your laptop is still connected to the Robot            
Controller's Programming Mode Wi-Fi network.                          

2. Verify that "MyFIRSTOpMode" is opened for editing. If it is not,   
you can click on the FIRST logo in the upper left hand corner of the  
browser window on the laptop. This should take you to the main 
Blocks Development Tool project screen.                               

.. image:: images/TouchSensorOpModeStep2ControlHub.jpg
   :align: center

|

   Click on the "MyFIRSTOpMode" project to open it for editing if it is not already opened.

3. Click on the "Logic" category. Find and click on the "if do else"  
block.                                                                

.. image:: images/TouchSensorOpModeStep3ControlHub.jpg
   :align: center

|

4. Drag the "if do else" block to the position before the             
"telemetry.update" block.                                             

.. image:: images/TouchSensorOpModeStep4ControlHub.jpg
   :align: center

|

5. Click on the "Sensors" category to expand it (if it isn't already  
expanded). Click on the "Touch Sensor" subcategory, then find and     
select the ".isPressed" block.                                        

.. image:: images/TouchSensorOpModeStep5ControlHub.jpg
   :align: center

|

6. Drag the "isPressed" block to the test condition of the "if do     
else" programming block.                                              

.. image:: images/TouchSensorOpModeStep6ControlHub.jpg
   :align: center

|

7. Click on the "Utilities" category on the left-hand side of your    
browser. Find and click on the "Telemetry" subcategory.               

.. image:: images/TouchSensorOpModeStep7ControlHub.jpg
   :align: center

|

   Select the "call telemetry.addData" block (the text version) and drag it to the "do" clause of the "if do else" block.

8. Change the "key" value to "testTouch" and the "text" value to "is  
pressed".                                                             

.. image:: images/TouchSensorOpModeStep8ControlHub.jpg
   :align: center

|

9. Insert another "telemetry.addData" block (the text version) to the 
"else" clause of the "if do else" block. Change the "key" value to    
"testTouch" and the "text" value to "is NOT pressed".                 

.. image:: images/TouchSensorOpModeStep9ControlHub.jpg
   :align: center

|

10. Save your op mode and verify that it was saved successfully to    
the Robot Controller.                                                 

.. image:: images/TouchSensorOpModeStep10ControlHub.jpg
   :align: center

|

11. Follow the procedure outlined in the section titled :doc:`Running Your 
OpMode <../running_op_modes/Running-Your-Op-Mode>`
to run your updated op mode.                                          

.. image:: images/TouchSensorOpModeStep11ControlHub.jpg
   :align: center

|

   As you run the op mode and push or release the button, the telemetry message on the DRIVER STATION should update to reflect the current state of the digital Touch Sensor.

