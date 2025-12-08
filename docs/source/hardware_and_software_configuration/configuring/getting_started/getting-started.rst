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
   USB ハードウェアを **Robot Controller** に関連付けるように複数回プロンプトが表示される場合があります。このメッセージが表示された場合は、常に「この USB デバイスをデフォルトで使用する」オプションを選択し、「OK」ボタンを押して USB デバイスを **Robot Controller** アプリに関連付けます。この関連付けを行わないと、次回システムをオンにしたときに **Robot Controller** アプリがこの **Expansion Hub** に確実に接続できない可能性があります。


DRIVER STATION を使用した構成ファイルの作成
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

構成ファイルは **Robot Controller** に存在する必要がありますが、このチュートリアルでは、**DRIVER STATION** アプリを使用してリモートで構成ファイルを作成します。**DRIVER STATION** は、**Control Hub** または Android スマートフォン **Robot Controller** の構成ファイルを作成するために使用できます。


DRIVER STATION の指示を使用した Robot Controller での構成ファイルの作成
-------------------------------------------------------------------------------------------

1. **Driver Station** アプリの右上隅にある 3 つの縦のドットをタッチします。これにより、ポップアップメニューが起動します。               

.. image:: images/ConfiguringHardwareNewStep1.jpg
   :align: center

|

2. ポップアップメニューから **Configure Robot** を選択して、**Configuration** 画面を表示します。                                             

.. image:: images/ConfiguringHardwareNewStep2.jpg
   :align: center

|

3. **Robot Controller** に既存の構成ファイルがない場合、画面には続行する前にファイルを作成する必要があることを示すメッセージが表示されます。                                      

.. image:: images/ConfiguringHardwareNewStep3.jpg
   :align: center

|

**New** ボタンをタッチして、**Robot Controller** の新しい構成ファイルを作成します。

4. 新しい構成画面が表示されると、**Robot Controller** アプリはシリアルバスのスキャンを実行して、**Robot Controller** に接続されているデバイスを確認します。                                    

.. image:: images/ConfiguringHardwareStep9.jpg
   :align: center

|

検出されたデバイスは、「USB Devices in configuration」という言葉の下のリストに表示されます。リストに「Expansion Hub Portal 1」のようなエントリが表示されるはずです。

**Expansion Hub** は、USB ケーブルを介して **Robot Controller** スマートフォンに直接接続されているか、**Control Hub** の場合は内部シリアルバスを介して接続されているため、Portal としてリストされます。

**Expansion Hub** Portal がリストされておらず、**Robot Controller** としてスマートフォンを使用している場合は、有線接続を確認して確実に接続されていることを確認し、Scan ボタンを 1〜2 回押して、USB バスの再スキャンでスマートフォンがデバイスを検出するかどうかを確認します。

5. Portal リスト（この例では「Expansion Hub Portal 1」）をタッチして、この Portal を介して接続されている **Expansion Hub** を表示します。                                                               

.. image:: images/ConfiguringHardwareStep10.jpg
   :align: center

|

単一の **Expansion Hub** のみが接続されているため、構成された単一の **Expansion Hub**（この例では「Expansion Hub 2」）のみが表示されるはずです。

6. **Expansion Hub** リスト（この例では「Expansion Hub 2」）をタッチして、そのデバイスの入出力ポートを表示します。           

.. image:: images/ConfiguringHardwareStep11.jpg
   :align: center

|

画面が変わり、選択した **Expansion Hub** で利用可能なすべてのモーター、サーボ、およびセンサーポートがリストされるはずです。
