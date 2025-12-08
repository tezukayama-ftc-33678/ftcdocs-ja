始め方
===============

構成の作成
~~~~~~~~~~~~~~~~~~~~~~~~

**Control Hub** または **Expansion Hub** に接続されているモーター、サーボ、センサーと通信する前に、まず **Robot Controller** に構成ファイルを作成する必要があります。これにより、**Robot Controller** は **Control Hub** または **Expansion Hub** の外部ポートで利用可能なハードウェアを認識できます。

Control Hub の準備
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Control Hub** を使用している場合、追加の接続は必要ありません。**Control Hub** の電源がオンになっており、**Driver Station** とペアリングされていることを確認するだけです。

Android スマートフォンを Expansion Hub に接続
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Android スマートフォンを **Robot Controller** として使用している場合、USB ケーブルと OTG（On-The-Go）アダプターを使用して、**Robot Controller** スマートフォンを **Expansion Hub** に物理的に接続する必要があります。また、**Driver Station** が現在 **Robot Controller** とペアリングされていることを確認する必要があります。

Android スマートフォンを Expansion Hub に接続する手順
-----------------------------------------------------------------

1. 電源スイッチをオンにして、**Expansion Hub** の電源を入れます。         

.. image:: images/ConfiguringHardwareStep1.jpg
   :align: center

|

2. USB ケーブルの Type B Mini 側（小さい方のコネクタ）を **Expansion Hub** の USB mini ポートに差し込みます。                                                 

.. image:: images/ConfiguringHardwareStep2.jpg
   :align: center

|

3. USB ケーブルの Type A 端を OTG アダプターに差し込みます。

.. image:: images/ConfiguringHardwareStep3.jpg
   :align: center

|

4. **Robot Controller** スマートフォンの電源がオンになっており、ロック解除されていることを確認します。USB Micro OTG アダプターを **Robot Controller** スマートフォンの OTG ポートに差し込みます。

.. image:: images/ConfiguringHardwareStep4.jpg
   :align: center

|

OTG アダプターがスマートフォンに差し込まれると、スマートフォンは **Expansion Hub** の存在を検出し、**Robot Controller** アプリを起動することに注意してください。

5. 初めて **Robot Controller** スマートフォンを **Expansion Hub** に接続すると、Android オペレーティングシステムが次のように求めるプロンプトを表示します。  
if it is OK to associate the newly detected USB device (which is the  
Expansion Hub) with the Robot Controller app.                     

.. image:: images/ConfiguringHardwareStep5.jpg
   :align: center

|

.. important:: 
   You might be prompted multiple times to associate the USB hardware with the
   Robot Controller.  Whenever you are prompted by your phone with this
   message, you should always select the "Use by default for this USB device"
   option and hit the "OK" button to associate the USB device with the Robot
   Controller app. If you fail to make this association, then the Robot
   Controller app might not reliably connect to this Expansion Hub the next
   time you turn your system on.


Creating a Configuration File Using the DRIVER STATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although the configuration file needs to reside on the Robot Controller,
for this tutorial we will use the DRIVER STATION app to create the
configuration file remotely. The DRIVER STATION can be used to create a
configuration file for a Control Hub or for an Android smartphone Robot
Controller.


Creating a Configuration File on the Robot Controller using the DRIVER STATION Instructions
-------------------------------------------------------------------------------------------

1. Touch the three vertical dots in the upper right hand corner of    
the Driver Station app. This will launch a pop-up menu.               

.. image:: images/ConfiguringHardwareNewStep1.jpg
   :align: center

|

2. Select **Configure Robot** from the pop up menu to display the     
**Configuration** screen.                                             

.. image:: images/ConfiguringHardwareNewStep2.jpg
   :align: center

|

3. If your Robot Controller does not have any existing configuration  
files, the screen will display a message indicating that you need to  
create a file before proceeding.                                      

.. image:: images/ConfiguringHardwareNewStep3.jpg
   :align: center

|

Hit the **New** button to create a new configuration file for your Robot Controller.

4. When the new configuration screen appears, the Robot Controller    
app will do a scan of the serial bus to see what devices are          
connected to the Robot Controller.                                    

.. image:: images/ConfiguringHardwareStep9.jpg
   :align: center

|

It will display the devices that it found in a list underneath the words "USB Devices in configuration." You should see an entry that says something like "Expansion Hub Portal 1" in the list.

Your Expansion Hub is listed as a Portal because it is directly connected to the Robot Controller phone through the USB cable or in the case of the Control Hub through the internal serial bus.

If you do not see your Expansion Hub Portal listed and you are using a smartphone as a Robot Controller, check the wired connections to make sure they are secure and then press the Scan button one or two times more to see if the smartphone detects the device on a re-scan of the USB bus.

5. Touch the Portal listing ("Expansion Hub Portal 1" in this         
example) to display what Expansion Hubs are connected through this    
Portal.                                                               

.. image:: images/ConfiguringHardwareStep10.jpg
   :align: center

|

Since we only have a single Expansion Hub connected, we should only see a single Expansion Hub configured ("Expansion Hub 2" in this example).

6. Touch the Expansion Hub listing ("Expansion Hub 2" in this         
example) to display the Input/Output ports for that device.           

.. image:: images/ConfiguringHardwareStep11.jpg
   :align: center

|

The screen should change and list all the motor, servo and sensor ports that are available on the selected Expansion Hub.
