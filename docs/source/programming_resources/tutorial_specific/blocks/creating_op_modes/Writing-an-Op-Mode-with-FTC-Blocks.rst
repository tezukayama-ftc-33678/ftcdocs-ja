Op Mode の作成 :bdg-warning:`Blocks`
====================================


Op Mode とは？
~~~~~~~~~~~~~~

典型的な *FIRST* Tech Challenge のマッチでは、チームのロボットは得点を獲得するためにさまざまなタスクを実行する必要があります。例えば、チームは競技フィールドの白い線に沿ってロボットを動かし、マッチ中に自律的にゲーム要素をゴールに得点させたいと考えるかもしれません。チームは、ロボットの動作を指定するために **op mode**（「operational modes」の略）と呼ばれるプログラムを作成します。これらの **op mode** は、**DRIVER STATION** で選択された後、**Robot Controller** 上で実行されます。

*FIRST* Tech Challenge に参加しているチームは、独自の **op mode** を作成するために使用できるさまざまなプログラミングツールを利用できます。このセクションでは、**Blocks Programming Tool** を使用してロボット用の **op mode** を作成する方法について説明します。

Blocks Programming Tool
~~~~~~~~~~~~~~~~~~~~~~~

**Blocks Programming Tool** は、**Robot Controller** によって提供されるユーザーフレンドリーなプログラミングツールです。ユーザーはこのツールを使用して、ロボット用のカスタム **op mode** を作成し、これらの **op mode** を **Robot Controller** に直接保存できます。ユーザーはジグソーパズルの形をしたプログラミングブロックをデザイン「キャンバス」にドラッグアンドドロップし、これらのブロックを配置して **op mode** のプログラムロジックを作成します。**Blocks Programming Tool** は Google の Blockly ソフトウェアを搭載しており、Google のサポートを受けて開発されました。

.. image:: images/BlocksPicture1New.jpg
   :align: center

|

The examples in this section use a Windows laptop computer to connect to
the Robot Controller. This Windows laptop computer has a
Javascript-enabled web browser installed that is used to access the 
Blocks Programming Tool.

.. image:: images/BlocksPicture2.jpg
   :align: center

|

**Control Hub** を **Robot Controller** として使用している場合でも、**op mode** の作成と編集に使用するプロセスは同じです。

.. image:: images/BlocksPicture2b.jpg
   :align: center

|

必要に応じて、Windows コンピューターの代わりに、Apple Mac ラップトップ、Apple iPad、Android タブレット、または Chromebook などの代替デバイスを使用して **Blocks Programming Tool** にアクセスできます。ただし、このドキュメントに含まれる手順は、Windows ラップトップを使用していることを前提としています。

また、このセクションでは、Android デバイスとロボットハードウェアの設定と構成が既に完了していることを前提としています。また、ラップトップが **Robot Controller** の Program & Manage ワイヤレスネットワークに正常に接続されていることも前提としています。

最初の Op Mode の作成
~~~~~~~~~~~~~~~~~~~~~

ラップトップを **Robot Controller** の Program & Manage ワイヤレスネットワークに正常に接続できた場合、最初の **op mode** を作成する準備が整いました。このセクションでは、**Blocks Programming Tool** を使用して、最初の **op mode** のプログラムロジックを作成します。

最初の **op mode** の作成には約 10 分かかる見込みです。

最初の Op Mode の作成手順
-------------------------

1. ラップトップで Web ブラウザーを起動し（*FIRST* は Google Chrome の使用を推奨）、**Robot Controller** の Program & Manage 画面に表示されている Web アドレスを見つけます。

.. important:: **Robot Controller** が Android スマートフォンの場合、Program & Manage サーバーにアクセスするアドレスは「192.168.49.1:8080」です。

.. image:: images/WritingFirstOpModeStep1a.jpg
   :align: center

|

.. important:: **Robot Controller** が **Control Hub** の場合、Program & Manage サーバーにアクセスするアドレスは「192.168.43.1:8080」です。IP アドレスの第3オクテットの違いに注意してください（**Control Hub** は「49」ではなく「43」です）。

.. image:: images/WritingFirstOpModeStep1aControlHub.jpg
   :align: center

|

   この Web アドレスをブラウザーのアドレスフィールドに入力し、RETURN キーを押して Program & Manage Web サーバーに移動します。

.. image:: images/WritingFirstOpModeStep1bControlHub.jpg
   :align: center

|

2. Web ブラウザーがプログラミングモードサーバーに接続されていることを確認します。プログラミングモードサーバーに正常に接続されている場合、**Robot Controller Console** が表示されます。

.. image:: images/WritingFirstOpModeStep2ControlHub.jpg
   :align: center

|

3. コンソールの上部にある **Blocks** リンクを押して、メインの **Blocks Programming** 画面に移動します。

.. image:: images/WritingFirstOpModeStep3aControlHub.jpg
   :align: center

|

   メインの **Blocks Programming** 画面は、新しい **op mode** を作成する場所です。また、**Robot Controller** 上の既存の **Blocks Op Mode** のリストを表示する画面でもあります。最初の **op mode** を作成して保存するまで、このリストは空です。

.. image:: images/WritingFirstOpModeStep3bControlHub.jpg
   :align: center

|

4. ブラウザーウィンドウの左上隅に表示されている「Create New Op Mode」ボタンを押します。

.. image:: images/WritingFirstOpModeStep4ControlHub.jpg
   :align: center

|

   プロンプトが表示されたら、**op mode** の名前を指定し、「OK」を押して続行します。

5. 新しい **op mode** が作成されたことを確認します。Web ブラウザーのメイン画面に、新しく作成された **op mode** が編集用に開かれているのが表示されるはずです。

.. image:: images/WritingFirstOpModeStep5ControlHub.jpg
   :align: center

|

   ブラウザー画面の左側には、カテゴリ別に分類されたプログラミングブロックのリストが表示されています。カテゴリをクリックすると、ブラウザーに関連する利用可能なプログラミングブロックのリストが表示されます。

   画面の右側は、プログラミングブロックを配置して **op mode** のロジックを作成する場所です。


Op Mode の構造を調べる
~~~~~~~~~~~~~~~~~~~~~~~

新しい **op mode** を作成すると、**op mode** のデザインキャンバスに配置されたプログラミングブロックのセットがすでに存在しているはずです。これらのブロックは、作成する各新しい **op mode** に自動的に含まれます。これらは、**op mode** の基本構造を作成します。

.. image:: images/ExaminingStructurePic1ControlHub.jpg
   :align: center

|

上図に示されているように、**op mode** の本体は、上部に「to runOpMode」という言葉がある外側の紫色の括弧によって定義されています。ヘルプのヒントが示すように、この関数は、この **op mode**（この例では「MyFIRSTOpMode」）が **DRIVER STATION** から選択されたときに実行されます。

**op mode** を **Robot Controller** が実行するタスクのリストと考えると役立ちます。**Robot Controller** はこのタスクのリストを順番に処理します。ユーザーは、制御ループ（while ループなど）を使用して、**Robot Controller** に **op mode** 内の特定のタスクを繰り返し（または反復）させることもできます。

.. image:: images/ExaminingStructurePic2.jpg
   :align: center

|

If you think about an op mode as a list of instructions for the robot,
this set of instructions will be executed by the robot whenever a team
member selects the op mode called "MyFIRSTOpMode" from the list of
available op modes for this Robot Controller.

You can hide the help text by clicking on the blue button with the
question mark ("?") on it. Let's look at the flow of this basic op mode.
The blue colored block with the words "Put initialization blocks here"
is a comment. Comments are placed in an op mode for the benefit of the
human user. The robot will ignore any comments in an op mode.

.. image:: images/ExaminingStructurePic3.jpg
   :align: center

|

「Put initialization blocks here」コメントの後（および「call MyFIRSTOpMode.waitForStart」ブロックの前）に配置されたプログラミングブロックは、**DRIVER STATION** でユーザーが **op mode** を最初に選択したときに実行されます。

**Robot Controller** が「call MyFIRSTOpMode.waitForStart」というラベルの付いたブロックに到達すると、停止して **DRIVER STATION** から Start コマンドを受信するまで待機します。Start コマンドは、ユーザーが **DRIVER STATION** の Start ボタンを押すまで送信されません。「call MyFIRSTOpMode.waitForStart」ブロックの後のコードは、Start ボタンが押された後に実行されます。

.. image:: images/ExaminingStructurePic4.jpg
   :align: center

|

「call MyFIRSTOpMode.waitForStart」の後には、**op mode** がまだアクティブである場合（つまり、停止コマンドが受信されていない場合）にのみ実行される条件付き「if」ブロック（「if call MyFIRSTOpMode.isActive」）があります。

.. image:: images/ExaminingStructurePic4bControlhub.jpg
   :align: center

|

「Put run blocks here」コメントの後で、「repeat while call MyFirstOpMode.opModeIsActive」というラベルの緑色のブロックの前に配置されたブロックは、Start ボタンが押された後に **Robot Controller** によって順次実行されます。

「repeat while call MyFirstOpMode.opModeIsActive」というラベルの緑色のブロックは、反復またはループ制御構造です。

.. image:: images/ExaminingStructurePic5ControlHub.jpg
   :align: center

|

この緑色の制御ブロックは、条件「call MyFIRSTOpMode.opModeIsActive」が真である限り、ブロックの「do」部分の下にリストされているステップを実行します。つまり、**op mode**「MyFIRSTOpMode」が実行されている限り、ブロックの「do」部分に含まれるステートメントが繰り返し実行されるということです。ユーザーが Stop ボタンを押すと、「call MyFIRSTOpMode.opModeIsActive」句はもはや真ではなくなり、「repeat while」ループは繰り返しを停止します。

DC モーターの制御
~~~~~~~~~~~~~~~~~

このセクションでは、**op mode** にいくつかのブロックを追加して、ゲームパッドで DC モーターを制御できるようにします。

このタスクを完了するには約 15 分かかる見込みです。

.. important:: ユーザーが構成したデバイス（モーター、サーボ、センサー）のプログラミングブロックは、構成されたデバイスを含むアクティブな構成ファイルがある場合にのみ、Blocks ツールで表示されます。デバイスのタイプがアクティブな構成ファイルに含まれていない場合、そのプログラミングブロックはブロックのパレットから欠落します。

まだ :doc:`構成ファイルを作成してアクティブ化 </hardware_and_software_configuration/connecting_devices/index>` していない場合は、:doc:`このリンク </hardware_and_software_configuration/connecting_devices/index>` に従ってください。
構成ファイルを作成してアクティブ化した後、**op mode** を閉じてから再度開くと、新しく構成されたデバイスのプログラミングブロックが表示されます。

DC モーターを制御するための Op Mode の変更手順
----------------------------------------------

1. 画面の左側にある「Variables」というカテゴリをクリックして、**op mode** 内で変数を作成および変更するために使用されるブロックコマンドのリストを表示します。

.. image:: images/AddingDCMotorStep1ControlHub.jpg
   :align: center

|

   「Create variable...」をクリックして、**op mode** の目標モーターパワーを表す新しい変数を作成します。

2. プロンプトが表示されたら、新しい変数の名前（「tgtPower」）を入力します。

.. image:: images/AddingDCMotorStep2ControlHub.jpg
   :align: center

|

3. 新しい変数を作成すると、「Variables」ブロックカテゴリの下にいくつかの追加のプログラミングブロックが表示されます。

.. image:: images/AddingDCMotorStep3ControlHub.jpg
   :align: center

|

4. 「set tgtPower to」プログラミングブロックをクリックし、マウスを使用してブロックを「Put loop blocks here」コメントブロックの直後の場所にドラッグします。                                                  

.. image:: images/AddingDCMotorStep4ControlHub.jpg
   :align: center

|

   The "set tgtPower to" block should snap right into position.

5. Click on the "Gamepad" category of the programming blocks and      
select the "gamepad1.LeftStickY" block from the list of available     
blocks.  

.. image:: images/AddingDCMotorStep5ControlHub.jpg
   :align: center

|

   Note that the control system lets you have up to two gamepads controlling a robot.  By selecting "gamepad1" you are telling the op mode to use the control input from the gamepad that is designated as driver #1.

6. Drag the "gamepad1.LeftStickY" block so it snaps in place onto the 
right side of the "set tgtPower to" block. This set of blocks will    
continually loop and read the value of gamepad #1's left joystick     
(the y position) and set the variable tgtPower to the Y value of the  
left joystick.  

.. image:: images/AddingDCMotorStep6a.jpg
   :align: center

|

   Note that for the F310 gamepads, the Y value of a joystick ranges from -1, when a joystick is in its topmost position, to +1, when a joystick is in its bottommost position.

.. image:: images/AddingDCMotorStep6bControlHub.jpg
   :align: center

|

   This means that for the blocks shown in our example, if the left joystick is pushed to the top, the variable tgtPower will have a value of -1.

7. Click on the "Math" category for the programming blocks and select 
the negative symbol ("-").   

.. image:: images/AddingDCMotorStep7ControlHub.jpg
   :align: center

|

8. Drag the negative symbol (also known as a "negation operator") to  
the left of the "gamepad1.LeftStickY" block. It should click in place 
after the "set tgtPower to" block and before the                      
"gamepad1.LeftStickY" block.    

.. image:: images/AddingDCMotorStep8ControlHub.jpg
   :align: center

|

With this change, the variable tgtPower will be set to +1 if the left joystick is in its topmost position and will be set to -1 if the joystick is in its bottommost position.

9. Click on the "Actuators" category of blocks. Then click on the     
"DcMotor" category of blocks.   

.. image:: images/AddingDCMotorStep9ControlHub.jpg
   :align: center

|

10. Select the "set motorTest.Power to 1" programming block.   

.. image:: images/AddingDCMotorStep10ControlHub.jpg
   :align: center

|    

11. Drag and place the "set motorTest.Power to 1" block so that it    
snaps in place right below the "set tgtPower to" block.               

.. image:: images/AddingDCMotorStep11ControlHub.jpg
   :align: center

|

12. Click on the "Variables" block category and select the "tgtPower" 
block.                                                                

.. image:: images/AddingDCMotorStep12ControlHub.jpg
   :align: center

|

13. Drag the "tgtPower" block so it snaps in place just to the right  
of the "set motor1.Power to" block.                                   

.. image:: images/AddingDCMotorStep13ControlHub.jpg
   :align: center

|

   The "tgtPower" block should automatically replace the default value of "1" block.

Inserting Telemetry Statements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your op mode is just about ready to run. However, before continuing, you
will add a couple of telemetry statements that will send information
from the Robot Controller to the DRIVER STATION for display on the
DRIVER STATION user interface. This telemetry mechanism is a useful way
to display status information from the robot on the DRIVER STATION. You
can use this mechanism to display sensor data, motor status, gamepad
state, etc. from the Robot Controller to the DRIVER STATION.

Note that you will need an estimated 15 minutes to complete this task.

Inserting Telemetry Statements Instructions
-------------------------------------------

1. Click on the "Utilities" category on the left-hand side of the     
browser window. Select the "Telemetry" subcategory and select the     
"call telemetry.addData(key, number)" block.                          

.. image:: images/TelemetryMotorStep1ControlHub.jpg
   :align: center

|

2. Drag the "call telemetry.addData(key, number)" block and place it  
below the "set motor1.Power to" block. Click on the green text block  
"key" and highlight the text and change it to read "Target Power".    

.. image:: images/TelemetryMotorStep2ControlHub.jpg
   :align: center

|

   Note that the "call telemetry.update" block is an important block.  Data that is added to the telemetry buffer will not be sent to the DRIVER STATION until the "telemetry.update" method is called.

3. Click on the "Variables" block category and select the "tgtPower"  
block. Drag the block so it clicks into place next to the "number"    
parameter on the telemetry programming block.                         

.. image:: images/TelemetryMotorStep3ControlHub.jpg
   :align: center

|

   The Robot Controller will send the value of the variable tgtPower to the DRIVER STATION with a key or label of "Target Power".  The key will be displayed to the left of the value on the DRIVER STATION.

4. Repeat this process and name the new key "Motor Power".            

.. image:: images/TelemetryMotorStep4ControlHub.jpg
   :align: center

|

5. Find and click on the "DcMotor" subcategory. Look for the green    
programming block labeled "motorTest.Power".                          

.. image:: images/TelemetryMotorStep5ControlHub.jpg
   :align: center

|

6. Drag the "motorTest.Power" block to the "number" parameter of the  
second telemetry block.                                               

.. image:: images/TelemetryMotorStep6ControlHub.jpg
   :align: center

|

   Your op mode will now also send the motor power information from the Robot Controller to be displayed on the DRIVER STATION.

Saving Your Op Mode
~~~~~~~~~~~~~~~~~~~

After you have modified your op mode, it is very important to save the
op mode to the Robot Controller.

Note it will take an estimated 1 minute to complete this task.

Saving Your Op Mode Instructions
--------------------------------

1. Press the "Save Op Mode" button to save the op mode to the Robot   
Controller. If your save was successful, you should see the words     
"Save completed successfully" to the right of the buttons.            

.. image:: images/SavingOpModeStep1ControlHub.jpg
   :align: center

|


Exiting Program & Manage Screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you have modified and saved your op mode, if your DRIVER STATION
is still in the Program & Manage screen, then you should exit this
screen and return to the Main DRIVER STATION screen.

Note it will take an estimated 1 minute to complete this task.


Exiting Programming Mode Instructions
-------------------------------------

1. Press the Android back arrow to exit the Program & Manage screen.  
You need to exit the Program & Manage screen before you can run your  
op mode.                                                              

.. image:: images/SavingOpModeStep1ControlHub.jpg
   :align: center

|

Congratulations! You wrote your first op mode using the Blocks
Programming Tool! You will learn how to run your op mode in the the
section entitled :doc:`Running Your Op Mode <../running_op_modes/Running-Your-Op-Mode>`.
