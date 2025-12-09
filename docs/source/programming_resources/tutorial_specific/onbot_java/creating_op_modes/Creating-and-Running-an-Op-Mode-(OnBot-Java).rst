Op Mode の作成と実行 :bdg-info:`OBJ`
===============================================

Java プログラミング言語
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このチュートリアルは、Javaプログラミング言語について十分な理解があることを前提としています。Javaを知らない場合は、ビジュアル開発ツールである **Blocks** プログラミングツールの使用を検討してください。**Blocks** プログラミングツールに関する情報は、以下のリンクで確認できます：

:doc:`Blocks チュートリアル <../../../blocks/Blocks-Tutorial>`

または、以下のアドレスで入手可能なOracle Javaチュートリアルを完了することで、Javaプログラミング言語を学ぶことができます：

https://docs.oracle.com/javase/tutorial/

Op Mode とは？
~~~~~~~~~~~~~~~~~~

典型的な **FIRST Tech Challenge** のマッチでは、チームのロボットはポイントを獲得するために様々なタスクを実行する必要があります。例えば、チームはロボットに競技フィールド上の白い線を追従させ、マッチ中に自律的にゲーム要素をゴールに入れることを望むかもしれません。チームは、ロボットの動作を指定するために *Op Mode*（「operational modes」の略）と呼ばれるプログラムを作成します。これらの **Op Mode** は、**DRIVER STATION** デバイスで選択された後、**Robot Controller** スマートフォン上で実行されます。

**FIRST Tech Challenge** に参加しているチームは、独自の **Op Mode** を作成するために使用できる様々なプログラミングツールを持っています。このドキュメントでは、**OnBot Java** プログラミングツールを使用してロボット用の **Op Mode** を作成する方法を説明します。

OnBot Java プログラミングツール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**OnBot Java** プログラミングツールは、**Robot Controller** スマートフォンによって提供されるユーザーフレンドリーなプログラミングツールです。ユーザーはこのツールを使用してロボット用のカスタム **Op Mode** を作成し、それらの **Op Mode** を **Robot Controller** に直接保存できます。ユーザーはJavaを使用して **Op Mode** を作成します。**Op Mode** は **Robot Controller** 上で非常に迅速にコンパイルされ、実行時に **Robot Controller** によって動的にロードされます。

.. image:: images/OnBotDoc001_MainScreen.jpg
   :align: center

|

このドキュメントの例では、Windowsのノートパソコンを使用して **Robot Controller** に接続します。このWindowsノートパソコンには、**OnBot Java** プログラミングツールにアクセスするために使用されるJavaScript対応のWebブラウザがインストールされています。

.. image:: images/BlocksPicture2b.jpg
   :align: center

|

なお、**Robot Controller** としてAndroidスマートフォンを使用している場合も、**Op Mode** の作成と編集に使用するプロセスは同じです。

.. image:: images/BlocksPicture2.jpg
   :align: center

|

なお、Windowsコンピューターの代わりに、Apple Macノートパソコン、Chromebook、またはiPadなどの代替デバイスを使用して **OnBot Java** プログラミングツールにアクセスすることもできます。ただし、このドキュメントに含まれる手順は、Windowsノートパソコンを使用していることを前提としています。

なお、このwikiのこのセクションは、Androidデバイスとロボットハードウェアをすでにセットアップおよび構成していることを前提としています。また、ノートパソコンを **Robot Controller** デバイスのProgam & Manageサーバーに正常に接続していることも前提としています。

最初の Op Mode の作成
~~~~~~~~~~~~~~~~~~~~~~~~~~~

ノートパソコンを **Robot Controller** のProgram & Manageワイヤレスネットワークに正常に接続できた場合、最初の **Op Mode** を作成する準備が整いました。このセクションでは、**OnBot Java** プログラミングツールを使用して、最初の **Op Mode** のプログラムロジックを作成します。


最初の Op Mode を作成する手順
----------------------------------------

1. ノートパソコン上でWebブラウザを起動し（**FIRST** はGoogle Chromeの使用を推奨しています）、**Robot Controller** のProgram & Manage画面に表示されているWebアドレスを見つけます。

.. image:: images/WritingFirstOpModeStep1aControlHub.jpg
   :align: center

|

.. important:: Note: If your Robot Controller is an Android smartphone, then the address to access the Program & Manage server is "192.168.49.1:8080". Notice the difference in the third octet of the IP addresses (the Control Hub has a "43" instead of a "49").

.. image:: images/WritingFirstOpModeStep1a.jpg
   :align: center

|

   Type this web address into the address field of your browser and press RETURN to navigate to the Program & Manage web server.

.. image:: images/WritingFirstOpModeStep1bControlHub.jpg
   :align: center

|


2. Webブラウザがプログラミングモードサーバーに接続されていることを確認します。プログラミングモードサーバーに正常に接続されている場合、**Robot Controller** コンソールが表示されます。

.. image:: images/WritingFirstOpModeStep2ControlHub.jpg
   :align: center

|

3. 画面上部にある *OnBotJava* という単語をクリックします。これにより、ブラウザが **OnBot Java** プログラミングモードに切り替わります。

.. image:: images/OnBotDoc_Step3_OnBotJavaButton.jpg
   :align: center

|

4. **OnBot Java** ユーザーインターフェースを確認します。左側にはプロジェクトブラウザペインがあります。右上隅にはソースコード編集ペインがあります。右下隅にはメッセージペインがあります。

.. image:: images/OnBotDoc_Step4_OnBotScreen.jpg
   :align: center

|

5. プロジェクトブラウザペインで「+」記号を押して、新しいファイルを作成します。このボタンを押すと、新規ファイルダイアログボックスが起動します。このダイアログボックスには、新しいファイルをカスタマイズするために構成できるいくつかのパラメーターがあります。

.. image:: images/OnBotDoc_Step5_NewFile.jpg
   :align: center

|

   この例では、新規ファイルダイアログボックスでファイル名として「MyFIRSTJavaOpMode」を指定します。

   サンプルドロップダウンリストコントロールを使用して、利用可能なサンプル **Op Mode** のリストから「BlankLinearOpMode」を選択します（上の画像を参照）。「BlankLinearOpMode」を選択すると、**OnBot Java** エディタが基本的な **LinearOpMode** フレームワークを自動的に生成します。

   「TeleOp」とラベル付けされたオプションをチェックして、この新しいファイルがテレオペレーション（つまり、ドライバー制御）**Op Mode** として構成されるようにします。
   
   また、「Setup Code for Configured Hardware」オプションもチェックしてください。このオプションを有効にすると、**OnBot Java** エディタは **Robot Controller** のハードウェア構成ファイルを確認し、**Op Mode** で構成されたデバイスにアクセスするために必要なコードを自動的に生成します。

   「OK」ボタンを押して、新しい **Op Mode** を作成します。

6. **OnBot Java** ユーザーインターフェースの編集ペインに、新しく作成された **Op Mode** が表示されるはずです。

.. image:: images/OnBotDoc_Step6_NewOpModeEditPane.jpg
   :align: center

|

おめでとうございます、最初の **Op Mode** を作成しました！この **Op Mode** は現在あまり機能しませんが、最終的にはより便利にするために修正します。

.. image:: images/OnBotDoc_Step6_ProjectBrowser.jpg
   :align: center

|

なお、**OnBot** **Op Mode** を作成すると、**Robot Controller** に保存される .java ファイルが作成されます。保存された **Op Mode** には、画面の左側にあるプロジェクトブラウザを使用してアクセスできます。また、プロジェクトブラウザを右クリックして、ファイルとフォルダーを作成、編集、または削除するオプションのリストを表示することで、保存された **Op Mode** を整理することもできます。

また、Program & Manageサーバーに接続されている限り、**OnBot Java** エディタは編集中に **Op Mode** を自動的に保存することにも注意してください。

Op Mode の構造を調べる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Op Mode** を、**Robot Controller** が実行するタスクのリストと考えると便利です。リニア **Op Mode** の場合、**Robot Controller** はこのタスクのリストを順次処理します。ユーザーは、制御ループ（whileループなど）を使用して、リニア **Op Mode** 内で特定のタスクを **Robot Controller** に繰り返し（または反復）実行させることもできます。

.. image:: images/ExaminingStructurePic2.jpg
   :align: center

|

**Op Mode** をロボットへの命令のリストと考えると、この作成した命令のセットは、チームメンバーがこの **Robot Controller** の利用可能な **Op Mode** のリストから「MyFIRSTJavaOpMode」という **Op Mode** を選択するたびに、ロボットによって実行されます。

新しく作成した **Op Mode** の構造を見てみましょう。以下は、**Op Mode** テキストのコピーです（いくつかのコメント、パッケージ定義、およびいくつかのインポートパッケージステートメントを除く）：

.. code-block:: java

   @TeleOp

   public class MyFIRSTJavaOpMode extends LinearOpMode {
       private Gyroscope imu;
       private DcMotor motorTest;
       private DigitalChannel digitalTouch;
       private DistanceSensor sensorColorRange;
       private Servo servoTest;


       @Override
       public void runOpMode() {
           imu = hardwareMap.get(Gyroscope.class, "imu");
           motorTest = hardwareMap.get(DcMotor.class, "motorTest");
           digitalTouch = hardwareMap.get(DigitalChannel.class, "digitalTouch");
           sensorColorRange = hardwareMap.get(DistanceSensor.class, "sensorColorRange");
           servoTest = hardwareMap.get(Servo.class, "servoTest");

           telemetry.addData("Status", "Initialized");
           telemetry.update();
           // Wait for the game to start (driver presses PLAY)
           waitForStart();

           // run until the end of the match (driver presses STOP)
           while (opModeIsActive()) {
               telemetry.addData("Status", "Running");
               telemetry.update();

           }
       }
   }

**Op Mode** の開始時に、クラス定義の前にアノテーションがあります。このアノテーションは、これがテレオペレーション（つまり、ドライバー制御）**Op Mode** であることを示しています：

.. code-block:: java

   @TeleOp

この **Op Mode** を自律 **Op Mode** に変更したい場合は、``@TeleOp`` を ``@Autonomous`` アノテーションに置き換えます。

サンプルコードから、**Op Mode** がJavaクラスとして定義されていることがわかります。この例では、**Op Mode** 名は「MyFIRSTJavaOpMode」と呼ばれ、**LinearOpMode** クラスから特性を継承しています。

.. code-block:: java

   public class MyFIRSTJavaOpMode extends LinearOpMode {

また、**OnBot Java** エディタがこの **Op Mode** 用に5つのプライベートメンバー変数を作成したこともわかります。これらの変数は、**OnBot Java** エディタが **Robot Controller** の構成ファイルで検出した5つの構成済みデバイスへの参照を保持します。

.. code-block:: java

       private Gyroscope imu;
       private DcMotor motorTest;
       private DigitalChannel digitalTouch;
       private DistanceSensor sensorColorRange;
       private Servo servoTest;

次に、runOpModeと呼ばれるオーバーライドされたメソッドがあります。**LinearOpMode** 型のすべての **Op Mode** は、このメソッドを実装する必要があります。このメソッドは、ユーザーが **Op Mode** を選択して実行したときに呼び出されます。

.. code-block:: java

       @Override
       public void runOpMode() {

runOpModeメソッドの開始時に、**Op Mode** はhardwareMapという名前のオブジェクトを使用して、**Robot Controller** の構成ファイルにリストされているハードウェアデバイスへの参照を取得します：

.. code-block:: java

           imu = hardwareMap.get(Gyroscope.class, "imu");
           motorTest = hardwareMap.get(DcMotor.class, "motorTest");
           digitalTouch = hardwareMap.get(DigitalChannel.class, "digitalTouch");
           sensorColorRange = hardwareMap.get(DistanceSensor.class, "sensorColorRange");
           servoTest = hardwareMap.get(Servo.class, "servoTest");

hardwareMapオブジェクトは、runOpModeメソッドで使用できます。これは **HardwareMap** クラス型のオブジェクトです。

なお、**Op Mode** で特定のデバイスへの参照を取得しようとする場合、**HardwareMap.get** メソッドの第2引数として指定する名前は、構成ファイルでデバイスを定義するために使用した名前と一致する必要があります。例えば、「motorTest」という名前のDCモーターを持つ構成ファイルを作成した場合、hardwareMapオブジェクトからこのモーターを取得するには、この同じ名前（大文字と小文字を区別）を使用する必要があります。名前が一致しない場合、**Op Mode** はデバイスを見つけることができないことを示す例外をスローします。

例の次のいくつかのステートメントでは、**Op Mode** はユーザーにスタートボタンを押して続行するように促します。runOpModeメソッドで使用できる別のオブジェクトを使用します。このオブジェクトは **telemetry** と呼ばれ、**Op Mode** は **addData** メソッドを使用して **DRIVER STATION** に送信するメッセージを追加します。次に、**Op Mode** は **update** メソッドを呼び出して、メッセージを **DRIVER STATION** に送信します。次に、**waitForStart** メソッドを呼び出して、ユーザーがDriver Stationのスタートボタンを押して **Op Mode** の実行を開始するまで待機します。

.. code-block:: java

           telemetry.addData("Status", "Initialized");
           telemetry.update();
           // Wait for the game to start (driver presses PLAY)
           waitForStart();

なお、すべてのリニア **Op Mode** には、ドライバーがスタートボタンを押すまでロボットが **Op Mode** の実行を開始しないようにするために、waitForStartステートメントが必要です。

スタートコマンドを受信した後、**Op Mode** はwhileループに入り、**Op Mode** がアクティブでなくなるまで（つまり、ユーザーが **DRIVER STATION** のストップボタンを押すまで）このループで反復を続けます：

.. code-block:: java

           // run until the end of the match (driver presses STOP)
           while (opModeIsActive()) {
               telemetry.addData("Status", "Running");
               telemetry.update();

           }

As the op mode iterates in the while loop, it will continue to send
telemetry messages with the index of "Status" and the message of
"Running" to be displayed on the DRIVER STATION.

Building Your Op Mode
~~~~~~~~~~~~~~~~~~~~~

When you create or edit an op mode the OnBot Java editor will auto-save
the .java file to the file system of the Robot Controller. However,
before you can execute your changes on the Robot Controller, you must
first build the op mode and convert it from a Java text file to a binary
that can be loaded dynamically into the Robot Controller app.

If you are satisfied with your op mode and are ready to build, press the
Build button (which is the button with the wrench symbol, see image
below) to start the build process. Note that the build process will
build **all of the .java files** on your Robot Controller.

.. image:: images/OnBotDoc_BuildButton.jpg
   :align: center

|

You should see messages appear in the message pane, which is located in
the lower right hand side of the window. If your build was successful,
you should see a "Build succeeded!" message in the message pane.

.. image:: images/OnBotDoc_BuildSucceeded.jpg
   :align: center

|

Once you have built the binary files with your updated op modes, they
are ready to run on the Robot Controller. Before we run our example op
mode, let's see what happens if a problem occurs during the build
process.

Troubleshooting Build Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the previous section, the build process went smoothly. Let's modify
your op mode slightly to cause an error in the build process.

In the editing pane of the OnBot Java window, look for the line that
reads ``private Servo servoTest;``. This should appear somewhere near the
beginning of your op mode class definition. Change the word "Servo" to
the word "Zervo":

.. code-block:: java

   private Zervo servoTest;

Also, let's modify the telemetry statement that informs the user that
the op mode has been initialized, and let's remove one of the two
arguments so that the statement looks like this:

.. code-block:: java

   telemetry.addData("Status",);

Note that when you eliminate the second argument, a little "x" should
appear next to the line with the modified addData statement. This "x"
indicates that there is a syntax error in the statement.

.. image:: images/OnBotDoc_SyntaxError.jpg
   :align: center

|

After you have modified your op mode, you can press the build button and
see what error messages appear.

.. image:: images/OnBotDoc_IllegalStart.jpg
   :align: center

|

When you first attempt to build the op mode, you should get an "illegal
start of expression error". This is because the addData method is
missing its second argument. The OnBot Java system also directs you to
the file that has the error, and the location within the file where the
error occurs.

In this example, the problem file is called
"org/firstinspires/ftc/teamcode/MyFIRSTJavaOpMode.java" and the error
occurs at line 62, column 37. It is important to note that the build
process builds all of the .java files on the Robot Controller. If there
is an error in a different file (one that you are not currently editing)
you will need to look at the file name to determine which file is
causing the problem.

Let's restore this statement back to its original, correct form:

.. code-block:: java

   telemetry.addData("Status", "Initialized");

After you have corrected the addData statement, push the build button
again to see what happens. The OnBot Java system should complain that it
cannot find the symbol "Zervo" in a source file called
"org/firstinspires/ftc/teamcode/MyFIRSTJavaOpMode.java" at line 51,
column 13.

.. image:: images/OnBotDoc_cannotFind.jpg
   :align: center

|

You should restore the statement back to its original form and then push
the build button and verify that the op mode gets built properly.

.. code-block:: java

   private Servo servoTest;

Running Your Op Mode
~~~~~~~~~~~~~~~~~~~~

*  If you successfully rebuilt your op mode, you are ready to run the op mode. Verify that the DRIVER STATION is still connected to the Robot Controller. Since you designated that your example op mode is a tele-operated op mode, it will be listed as a "TeleOp" op mode.
*  On the DRIVER STATION, use the "TeleOp" dropdown list control to display the list of available op modes. Select your op mode ("MyFIRSTJavaOpMode") from the list.

.. image:: images/OpModeSelectionDH.png
   :align: center

|

.. image:: images/OnBotDoc_SelectMyFIRSTOpMode.jpg
   :align: center

|

   Press the INIT button to initialize the op mode.

.. image:: images/InitDH.png
   :align: center

|

.. image:: images/OnBotDoc_MyFIRSTPushInit.jpg
   :align: center

|

The op mode will execute the statements in the runOpMode method up to
the waitForStart statement. It will then wait until you press the start
button (which is represented by the triangular shaped symbol) to
continue.

.. image:: images/RunDH.png
   :align: center

|

.. image:: images/OnBotDoc_PressStart.jpg
   :align: center

|

Once you press the start button, the op mode will continue to iterate
and send the "Status: Running" message to the DRIVER STATION. To stop
the op mode, press the square-shaped stop button.

.. image:: images/TelemetryDH.png
   :align: center

|

.. image:: images/OnBotDoc_PressStop.jpg
   :align: center

|

Congratulations! You ran your first java op mode!

Modifying Your Op Mode to Control a Motor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's modify your op mode to control the DC motor that you connected and
configured for your REV Expansion Hub. Modify the code for the program
loop so that it looks like the following:

.. code-block:: java

   // run until the end of the match (driver presses STOP)
   double tgtPower = 0;
   while (opModeIsActive()) {
       tgtPower = -this.gamepad1.left_stick_y;
       motorTest.setPower(tgtPower);
       telemetry.addData("Target Power", tgtPower);
       telemetry.addData("Motor Power", motorTest.getPower());
       telemetry.addData("Status", "Running");
       telemetry.update();

   }

If you look at the code that was added, you will see that we defined a
new variable called target power before we enter the while loop.

.. code-block:: java

   double tgtPower = 0;

At the start of the while loop we set the variable tgtPower equal to the
negative value of the gamepad1's left joystick:

.. code-block:: java

   tgtPower = -this.gamepad1.left_stick_y;

The object gamepad1 is available for you to access in the runOpMode
method. It represents the state of gamepad #1 in your OPERATOR CONSOLE.
Note that for the F310 gamepads that are used during the competition,
the Y value of a joystick ranges from -1, when a joystick is in its
topmost position, to +1, when a joystick is in its bottommost position.
In the example code above, you negate the left_stick_y value so that
pushing the left joystick forward will result in a positive power being
applied to the motor. Note that in this example, the notion of forwards
and backwards for the motor is arbitrary. However, the concept of
negating the joystick y value can be very useful in practice.

.. image:: images/OnBotDoc_left_stick_y.jpg
   :align: center

|

The next set of statements sets the power of motorTest to the value
represented by the variable tgtPower. The values for target power and
actual motor power are then added to the set of data that will be sent
via the telemetry mechanism to the DRIVER STATION.

.. code-block:: java

       tgtPower = -this.gamepad1.left_stick_y;
       motorTest.setPower(tgtPower);
       telemetry.addData("Target Power", tgtPower);
       telemetry.addData("Motor Power", motorTest.getPower());

After you have modified your op mode to include these new statements,
press the build button and verify that the op mode was built
successfully.

Running Your Op Mode with a Gamepad Connected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*  Your op mode takes input from a gamepad and uses this input to control
   a DC motor. To run your op mode, you will need to connect a Logitech
   F310 gamepad to the DRIVER STATION.

Connect the gamepad to the DRIVER STATION. If using a phone, you will
need a Micro USB OTG adapter cable.

.. image:: images/GamepadDHConnection.jpg
   :align: center

|

.. image:: images/RunningOpModeStep2.jpg
   :align: center

|

Your example op mode is looking for input from the gamepad designated as
the user or driver #1. Press the Start button and the A button
simultaneously on the Logictech F310 controller to designate your
gamepad as user #1. Note that pushing the Start button and the B button
simultaneously would designate the gamepad as user #2.

.. image:: images/RunningOpModeStep3.jpg
   :align: center

|

If you successfully designated the gamepad to be user #1, you should see
a little gamepad icon above the text "User 1" in the upper right hand
corner of the DRIVER STATION Screen. Whenever there is activity on
gamepad #1, the little icon should be highlighted in green. If the icon
is missing or if it does not highlight in green when you use your
gamepad, then there is a problem with the connection to the gamepad.

Select, initialize and run your "MyFIRSTJavaOpMode" op mode. It is
important to note that whenever you rebuild an op mode, you must stop
the current op mode run and then restart it before the changes that you
just built take effect.

If you configured your gamepad properly, then the left joystick should
control the motion of the motor. As you run your op mode, be careful and
make sure you do not get anything caught in the turning motor. Note that
the User #1 gamepad icon should highlight green each time you move the
joystick. Also note that the target power and actual motor power values
should be displayed in the telemetry area on the DRIVER STATION.

.. image:: images/TelemetryDH.png
   :align: center

|

.. image:: images/OnBotDoc_RunOpModeDCMotor.jpg
   :align: center

|

