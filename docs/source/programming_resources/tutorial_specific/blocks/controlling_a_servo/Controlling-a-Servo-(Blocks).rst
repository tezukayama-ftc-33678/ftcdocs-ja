サーボの制御 :bdg-warning:`Blocks`
==================================

:doc:`Blocks を使った Op Mode の作成 <../creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks>` のセクションでは、**Blocks Programming Tool** を使用して 12V DC モーターを制御する **op mode** を作成する方法を学びました。このセクションでは、サーボモーターを制御する **op mode** を作成する方法を学びます。

サーボモーターとは？
~~~~~~~~~~~~~~~~~~~~

サーボモーターは、精密な動作のために設計された特殊なタイプのモーターです。典型的なサーボモーターには、限られた動作範囲があります。

下図には、「標準スケール」の 180 度サーボが示されています。このタイプのサーボは、ホビイストや *FIRST* Tech Challenge チームに人気があります。このサーボモーターは、そのシャフトを 180 度の範囲で回転させることができます。サーボコントローラーとして知られる電子モジュールを使用すると、サーボモーターを特定の位置に移動する **op mode** を作成できます。モーターがこの目標位置に到達すると、サーボのシャフトに外力が加えられても、その位置を保持します。

.. image:: images/hs485hbServo.jpg
   :align: center

|

サーボモーターは、精密な動きをしたい場合に便利です（例えば、センサーでエリアをスイープしてターゲットを探したり、リモコン飛行機の制御面を動かしたりする場合など）。

Op Mode を変更してサーボを制御する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**op mode** を変更して、サーボモーターを制御するために必要なロジックを追加しましょう。この例では、Logitech F310 ゲームパッドのボタンを使用してサーボモーターの位置を制御します。

典型的なサーボでは、サーボのターゲット位置を指定できます。サーボはモーターシャフトを回転させてターゲット位置に移動し、適度な力が加えられて位置を乱そうとしても、その位置を維持します。

**Blocks** の Program & Manage サーバーでは、サーボのターゲット位置を 0 から 1 の範囲で指定できます。ターゲット位置 0 は回転角度 0 度に対応し、ターゲット位置 1 は典型的なサーボモーターの回転角度 180 度に対応します。

.. image:: images/servo0to80.jpg
   :align: center

|

この例では、F310 コントローラーの右側にある色付きのボタンを使用してサーボの位置を制御します。最初に、**op mode** はサーボを中間位置（180 度範囲の 90 度）に移動します。黄色の「Y」ボタンを押すと、サーボは 0 度の位置に移動します。青色の「X」ボタンまたは赤色の「B」ボタンを押すと、サーボは 90 度の位置に移動します。緑色の「A」ボタンを押すと、サーボは 180 度の位置に移動します。

.. image:: images/LogitechF310.jpg
   :align: center

|


サーボモーターを制御するための Op Mode の変更手順
-------------------------------------------------

1. ラップトップが **Robot Controller** の Program & Manage Wi-Fi ネットワークにまだ接続されていることを確認します。

2. 「MyFIRSTOpMode」が編集用に開かれていることを確認します。開かれていない場合は、ラップトップのブラウザーウィンドウの左上隅にある *FIRST* ロゴをクリックします。これにより、メインの **Blocks Development Tool** プロジェクト画面に移動するはずです。

.. image:: images/ControlServoStep2ControlHub.jpg
   :align: center

|

   まだ開かれていない場合は、「MyFIRSTOpMode」プロジェクトをクリックして編集用に開きます。

3. 画面の左側で「Actuators」というカテゴリをクリックし、「Servos」というサブカテゴリを探します。

.. image:: images/ControlServoStep3ControlHub.jpg
   :align: center

|

4. 利用可能な Servo ブロックのリストから「set servoTest.Position to」ブロックを選択します。

.. image:: images/ControlServoStep4ControlHub.jpg
   :align: center

|

5. 「set servoTest.Position to」ブロックを「Put initialization blocks here.」と書かれたコメントブロックの真下の場所にドラッグします。ブロックがカチッと所定の位置に収まるはずです。

.. image:: images/ControlServoStep5ControlHub.jpg
   :align: center

|

6. Click on the number block "0" and change the block's value to      
"0.5".                                                                

.. image:: images/ControlServoStep6ControlHub.jpg
   :align: center

|

   When a user selects this op mode, the servo position will initially be set to the midway point (90-degree position).

7. Click on the "Logic" category of the programming blocks and select 
the "if do" block from the list of available blocks. Drag the block   
to the position immediately after the comment block that reads "Put   
loop blocks here."                                                    

.. image:: images/ControlServoStep7ControlHub.jpg
   :align: center

|

   The block should click into place.

8. Click on the "Gamepad" category of the programming blocks and      
select the "gamepad1.Y" block from the list of available blocks.      

.. image:: images/ControlServoStep8ControlHub.jpg
   :align: center

|

   Note that this block is towards the bottom of the list of blocks.  You might have to scroll down to the bottom of the list before you can select this block.

9. Drag the "gamepad1.Y" block to the right side of the "if do"       
block. The block should click into place.                             

.. image:: images/ControlServoStep9ControlHub.jpg
   :align: center

|

   The "if do" block will use the state of the gamepad1.Y value its test condition.  If the "Y" button is pressed, the statements within the "do" portion of the block will be executed.

10. On the left-hand side of the screen click on the category called  
"Actuators" and look for the subcategory called "Servos".             

.. image:: images/ControlServoStep10ControlHub.jpg
   :align: center

|

11. Select the "set servoTest.Position to" block from the list of     
available Servo blocks.                                               

.. image:: images/ControlServoStep11ControlHub.jpg
   :align: center

|

12. Drag the "set servoTest.Position to" block so that it snaps in    
place in the do portion of the "if do" block.                         

.. image:: images/ControlServoStep12ControlHub.jpg
   :align: center

|

   If the "Y" button is pressed on gamepad #1, the op mode will move the servo's position to the 0-degree position.

13. Click on the blue and white Settings icon for the "if do" block.  
This will display a pop-up menu that lets you modify the "if do"      
block.                                                                

.. image:: images/ControlServoStep13ControlHub.jpg
   :align: center

|

14. Drag an "else if" block from the left side of the pop-up menu and 
snap it into place under the "if" block.                              

.. image:: images/ControlServoStep14ControlHub.jpg
   :align: center

|

   Drag a second "else if" block from the left side and snap it into place on the right side under the first "else if" block.

15. Click on the Settings icon to hide the pop-up menu for the "if    
do" block. The "if do" block should now have two "else if" test       
conditions added.                                                     

.. image:: images/ControlServoStep15ControlHub.jpg
   :align: center

|

16. Click on the "Logic" category and select the logical "and" block. 

.. image:: images/ControlServoStep16ControlHub.jpg
   :align: center

|

17. Drag the "and" block so it clicks in place as the test condition  
for the first "else if" block.                                        

.. image:: images/ControlServoStep17ControlHub.jpg
   :align: center

|

18. Click on the word "and" and select "or" from the pop-up menu to   
change the block to a logical "or" block.                             

.. image:: images/ControlServoStep18ControlHub.jpg
   :align: center

|

19. Click on the "Gamepad" category and select the "gamepad1.X"       
block. Drag the block so that it clicks in place as the first test    
condition of the logical "or" block.                                  

.. image:: images/ControlServoStep19ControlHub.jpg
   :align: center

|

20. Click on the "Gamepad" category and select the "gamepad1.B"       
block. Drag the block so that it clicks in place as the second test   
condition of the logical "or" block.                                  

.. image:: images/ControlServoStep20ControlHub.jpg
   :align: center

|

21. Select a "set servoTest.Position to" block and place it into "do" 
clause of the first else-if block.                                    

.. image:: images/ControlServoStep21ControlHub.jpg
   :align: center

|

22. Highlight the number "0" and change it to "0.5". With this        
change, if the user presses the "X" button or "B" button on gamepad   
#1, the op mode will move the servo to the midway (90-degree)         
position.                                                             

.. image:: images/ControlServoStep22ControlHub.jpg
   :align: center

|

23. Use a "gamepad1.A" block as the test condition for the second     
"else if" block. Drag a "set servoTest.position to" block to the do   
clause of the second "else if" block and modify the numeric value so  
that the servo's position will be set to a value of 1.                

.. image:: images/ControlServoStep23ControlHub.jpg
   :align: center

|

   For this clause, if the "A" button is pressed on the #1 gamepad, the op mode will move the servo to the 180-degree position.

24. Insert a "call telemetry.addData" block (numeric) before the      
"call Telemetry.update" block. Rename the key field to "Servo         
Position" and insert a "servoTest.Position" block for the number      
field.                                                                

.. image:: images/ControlServoStep24ControlHub.jpg
   :align: center

|

   This set of blocks will send the current servo position value to the DRIVER STATION while the op mode is running.

25. Save your op mode and verify that it was saved successfully to    
the Robot Controller.                                                 

.. image:: images/ControlServoStep25ControlHub.jpg
   :align: center

|

26. Follow the procedure outlined in the section titled :doc:`Running Your 
OpMode <../running_op_modes/Running-Your-Op-Mode>` 
to run your updated op mode. Also, make sure that your gamepad is     
designated as User #1 before running your op mode.                    

.. image:: images/ControlServoStep26ControlHub.jpg
   :align: center

|

   You should now be able to control the servo position with the colored buttons.  The servo position should be displayed on the DRIVER STATION.


