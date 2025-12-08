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

ポート #0 ではなくポート #1 でタッチセンサーを構成していることに注意してください。これは、標準の 4 線 JST センサーケーブルを使用して **REV Robotics タッチセンサー**をデジタルポートに接続すると、2 番目のデジタルピンが接続されるためです。最初のピンは接続されたままです。

3. **Done** ボタンを押して前の画面に戻ります。        

.. image:: images/ConfiguringHardwareTouchNewStep3.jpg
   :align: center

|