デジタルタッチセンサーの構成
==================================

**REV Robotics タッチセンサー**はデジタルセンサーです。**OpMode** は、タッチセンサーにクエリを実行して、ボタンが押されているかどうかを確認できます。

デジタルタッチセンサーの構成手順
-----------------------------------------------

1. 画面の **Digital Devices** をタップして、デジタル I/O 構成画面を表示します。                                     

.. image:: images/ConfiguringHardwareTouchStep1.jpg
   :align: center

|

2. タッチスクリーンを使用して、ポート #1 に「REV Touch Sensor」を追加し、デバイスに「testTouch」という名前を付けます。                                          

.. image:: images/ConfiguringHardwareTouchNewStep2.jpg
   :align: center

|

Notice that we are configuring the Touch Sensor on port #1 instead of port #0.  This is because when the REV Robotics Touch Sensor is connected to a digital port using a standard 4-wire JST sensor cable, it is the second digital pin that is connected. The first pin remains disconnected.

3. Press the **Done** button to return to the previous screen.        

.. image:: images/ConfiguringHardwareTouchNewStep3.jpg
   :align: center

|