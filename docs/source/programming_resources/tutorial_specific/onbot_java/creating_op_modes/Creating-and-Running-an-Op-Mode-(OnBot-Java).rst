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

**FIRST Tech Challenge** に参加しているチームは、独自の**Op Mode** を作成するために使用できる様々なプログラミングツールを持っています。このドキュメントでは、**OnBot Java** プログラミングツールを使用してロボット用の**Op Mode** を作成する方法を説明します。

OnBot Java プログラミングツール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**OnBot Java** プログラミングツールは、**Robot Controller** スマートフォンによって提供されるユーザーフレンドリーなプログラミングツールです。ユーザーはこのツールを使用してロボット用のカスタム**Op Mode** を作成し、それらの**Op Mode** を**Robot Controller** に直接保存できます。ユーザーはJavaを使用して**Op Mode** を作成します。**Op Mode** は**Robot Controller** 上で非常に迅速にコンパイルされ、実行時に**Robot Controller** によって動的にロードされます。

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

ノートパソコンを **Robot Controller** のProgram & Manageワイヤレスネットワークに正常に接続できた場合、最初の**Op Mode** を作成する準備が整いました。このセクションでは、**OnBot Java** プログラミングツールを使用して、最初の**Op Mode** のプログラムロジックを作成します。


最初の Op Mode を作成する手順
----------------------------------------

1. ノートパソコン上でWebブラウザを起動し（**FIRST** はGoogle Chromeの使用を推奨しています）、**Robot Controller** のProgram & Manage画面に表示されているWebアドレスを見つけます。

.. image:: images/WritingFirstOpModeStep1aControlHub.jpg
   :align: center

|

.. important:: 注記: **Robot Controller** がAndroidスマートフォンの場合、Program & Manageサーバーにアクセスするためのアドレスは「192.168.49.1:8080」です。IPアドレスの第3オクテットの違いに注意してください（**Control Hub** は「49」ではなく「43」です）。

.. image:: images/WritingFirstOpModeStep1a.jpg
   :align: center

|

   このWebアドレスをブラウザのアドレスフィールドに入力し、RETURNキーを押してProgram & Manage Webサーバーに移動します。

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

   サンプルドロップダウンリストコントロールを使用して、利用可能なサンプル **Op Mode** のリストから「BlankLinearOpMode」を選択します（上の画像を参照）。「BlankLinearOpMode」を選択すると、**OnBot Java** エディタが基本的な**LinearOpMode** フレームワークを自動的に生成します。

   「TeleOp」とラベル付けされたオプションをチェックして、この新しいファイルがテレオペレーション（つまり、ドライバー制御）**Op Mode** として構成されるようにします。
   
   また、「Setup Code for Configured Hardware」オプションもチェックしてください。このオプションを有効にすると、**OnBot Java** エディタは**Robot Controller** のハードウェア構成ファイルを確認し、**Op Mode** で構成されたデバイスにアクセスするために必要なコードを自動的に生成します。

   「OK」ボタンを押して、新しい **Op Mode** を作成します。

6. **OnBot Java** ユーザーインターフェースの編集ペインに、新しく作成された**Op Mode** が表示されるはずです。

.. image:: images/OnBotDoc_Step6_NewOpModeEditPane.jpg
   :align: center

|

おめでとうございます、最初の **Op Mode** を作成しました！この**Op Mode** は現在あまり機能しませんが、最終的にはより便利にするために修正します。

.. image:: images/OnBotDoc_Step6_ProjectBrowser.jpg
   :align: center

|

なお、**OnBot** **Op Mode** を作成すると、**Robot Controller** に保存される .java ファイルが作成されます。保存された**Op Mode** には、画面の左側にあるプロジェクトブラウザを使用してアクセスできます。また、プロジェクトブラウザを右クリックして、ファイルとフォルダーを作成、編集、または削除するオプションのリストを表示することで、保存された**Op Mode** を整理することもできます。

また、Program & Manageサーバーに接続されている限り、**OnBot Java** エディタは編集中に**Op Mode** を自動的に保存することにも注意してください。

Op Mode の構造を調べる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Op Mode** を、**Robot Controller** が実行するタスクのリストと考えると便利です。リニア**Op Mode** の場合、**Robot Controller** はこのタスクのリストを順次処理します。ユーザーは、制御ループ（whileループなど）を使用して、リニア**Op Mode** 内で特定のタスクを**Robot Controller** に繰り返し（または反復）実行させることもできます。

.. image:: images/ExaminingStructurePic2.jpg
   :align: center

|

**Op Mode** をロボットへの命令のリストと考えると、この作成した命令のセットは、チームメンバーがこの**Robot Controller** の利用可能な**Op Mode** のリストから「MyFIRSTJavaOpMode」という**Op Mode** を選択するたびに、ロボットによって実行されます。

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

この **Op Mode** を自律**Op Mode** に変更したい場合は、``@TeleOp`` を``@Autonomous`` アノテーションに置き換えます。

サンプルコードから、**Op Mode** がJavaクラスとして定義されていることがわかります。この例では、**Op Mode** 名は「MyFIRSTJavaOpMode」と呼ばれ、**LinearOpMode** クラスから特性を継承しています。

.. code-block:: java

   public class MyFIRSTJavaOpMode extends LinearOpMode {

また、**OnBot Java** エディタがこの**Op Mode** 用に5つのプライベートメンバー変数を作成したこともわかります。これらの変数は、**OnBot Java** エディタが**Robot Controller** の構成ファイルで検出した5つの構成済みデバイスへの参照を保持します。

.. code-block:: java

       private Gyroscope imu;
       private DcMotor motorTest;
       private DigitalChannel digitalTouch;
       private DistanceSensor sensorColorRange;
       private Servo servoTest;

次に、runOpModeと呼ばれるオーバーライドされたメソッドがあります。**LinearOpMode** 型のすべての**Op Mode** は、このメソッドを実装する必要があります。このメソッドは、ユーザーが**Op Mode** を選択して実行したときに呼び出されます。

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

例の次のいくつかのステートメントでは、**Op Mode** はユーザーにスタートボタンを押して続行するように促します。runOpModeメソッドで使用できる別のオブジェクトを使用します。このオブジェクトは**telemetry** と呼ばれ、**Op Mode** は**addData** メソッドを使用して**DRIVER STATION** に送信するメッセージを追加します。次に、**Op Mode** は**update** メソッドを呼び出して、メッセージを**DRIVER STATION** に送信します。次に、**waitForStart** メソッドを呼び出して、ユーザーがDriver Stationのスタートボタンを押して**Op Mode** の実行を開始するまで待機します。

.. code-block:: java

           telemetry.addData("Status", "Initialized");
           telemetry.update();
           // Wait for the game to start (driver presses PLAY)
           waitForStart();

なお、すべてのリニア **Op Mode** には、ドライバーがスタートボタンを押すまでロボットが**Op Mode** の実行を開始しないようにするために、waitForStartステートメントが必要です。

スタートコマンドを受信した後、**Op Mode** はwhileループに入り、**Op Mode** がアクティブでなくなるまで（つまり、ユーザーが**DRIVER STATION** のストップボタンを押すまで）このループで反復を続けます：

.. code-block:: java

           // run until the end of the match (driver presses STOP)
           while (opModeIsActive()) {
               telemetry.addData("Status", "Running");
               telemetry.update();

           }

**Op Mode** がwhileループで反復すると、「Status」というインデックスと「Running」というメッセージを含むテレメトリメッセージを**DRIVER STATION** に表示するために送信し続けます。

Op Mode のビルド
~~~~~~~~~~~~~~~~~~~~~

**Op Mode** を作成または編集すると、**OnBot Java** エディタは .java ファイルを**Robot Controller** のファイルシステムに自動保存します。ただし、**Robot Controller** で変更を実行する前に、まず**Op Mode** をビルドして、Javaテキストファイルから**Robot Controller** アプリに動的にロードできるバイナリに変換する必要があります。

**Op Mode** に満足してビルドする準備ができている場合は、ビルドボタン（レンチ記号のあるボタン、下の画像を参照）を押してビルドプロセスを開始します。なお、ビルドプロセスは**Robot Controller** 上の** すべての .java ファイル** をビルドします。

.. image:: images/OnBotDoc_BuildButton.jpg
   :align: center

|

ウィンドウの右下にあるメッセージペインにメッセージが表示されるはずです。ビルドが成功した場合、メッセージペインに「Build succeeded!」というメッセージが表示されるはずです。

.. image:: images/OnBotDoc_BuildSucceeded.jpg
   :align: center

|

更新された **Op Mode** でバイナリファイルをビルドしたら、**Robot Controller** で実行する準備が整いました。例の**Op Mode** を実行する前に、ビルドプロセス中に問題が発生した場合に何が起こるかを見てみましょう。

ビルドメッセージのトラブルシューティング
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

前のセクションでは、ビルドプロセスが順調に進みました。**Op Mode** を少し修正して、ビルドプロセスでエラーを発生させてみましょう。

**OnBot Java** ウィンドウの編集ペインで、``private Servo servoTest;`` と記述されている行を探します。これは、**Op Mode** クラス定義の先頭近くに表示されるはずです。「Servo」という単語を「Zervo」という単語に変更します：

.. code-block:: java

   private Zervo servoTest;

また、**Op Mode** が初期化されたことをユーザーに通知するテレメトリステートメントを変更し、2つの引数のうちの1つを削除して、ステートメントが次のようになるようにしましょう：

.. code-block:: java

   telemetry.addData("Status",);

なお、2番目の引数を削除すると、変更された addData ステートメントの行の横に小さな「x」が表示されるはずです。この「x」は、ステートメントに構文エラーがあることを示しています。

.. image:: images/OnBotDoc_SyntaxError.jpg
   :align: center

|

**Op Mode** を変更したら、ビルドボタンを押して、どのようなエラーメッセージが表示されるかを確認できます。

.. image:: images/OnBotDoc_IllegalStart.jpg
   :align: center

|

**Op Mode** を最初にビルドしようとすると、「illegal start of expression error」が表示されるはずです。これは、addData メソッドに2番目の引数がないためです。**OnBot Java** システムは、エラーがあるファイルと、ファイル内でエラーが発生した場所も示します。

この例では、問題のファイルは「``org/firstinspires/ftc/teamcode/MyFIRSTJavaOpMode.java`` 」と呼ばれ、エラーは62行37列で発生します。ビルドプロセスは **Robot Controller** 上のすべての .java ファイルをビルドすることに注意することが重要です。別のファイル（現在編集していないファイル）にエラーがある場合は、ファイル名を確認して、どのファイルが問題を引き起こしているかを判断する必要があります。

このステートメントを元の正しい形式に戻しましょう：

.. code-block:: java

   telemetry.addData("Status", "Initialized");

addData ステートメントを修正した後、ビルドボタンをもう一度押して、何が起こるかを確認します。**OnBot Java** システムは、「``org/firstinspires/ftc/teamcode/MyFIRSTJavaOpMode.java``」というソースファイルの51行13列で、シンボル「``Zervo`` 」を見つけることができないと文句を言うはずです。

.. image:: images/OnBotDoc_cannotFind.jpg
   :align: center

|

ステートメントを元の形式に戻してから、ビルドボタンを押して、**Op Mode** が適切にビルドされることを確認する必要があります。

.. code-block:: java

   private Servo servoTest;

Op Mode の実行
~~~~~~~~~~~~~~~~~~~~

*  **Op Mode** のリビルドに成功した場合、**Op Mode** を実行する準備が整いました。**DRIVER STATION** がまだ**Robot Controller** に接続されていることを確認します。例の**Op Mode** をテレオペレーション**Op Mode** として指定したため、「TeleOp」**Op Mode** としてリストされます。

*  **DRIVER STATION** で、「TeleOp」ドロップダウンリストコントロールを使用して、利用可能な**Op Mode** のリストを表示します。リストから**Op Mode** （「MyFIRSTJavaOpMode」）を選択します。

.. image:: images/OpModeSelectionDH.png
   :align: center

|

.. image:: images/OnBotDoc_SelectMyFIRSTOpMode.jpg
   :align: center

|

   INITボタンを押して、**Op Mode** を初期化します。

.. image:: images/InitDH.png
   :align: center

|

.. image:: images/OnBotDoc_MyFIRSTPushInit.jpg
   :align: center

|

**Op Mode** は、waitForStart ステートメントまで runOpMode メソッド内のステートメントを実行します。その後、スタートボタン（三角形の記号で表される）を押して続行するまで待機します。

.. image:: images/RunDH.png
   :align: center

|

.. image:: images/OnBotDoc_PressStart.jpg
   :align: center

|

スタートボタンを押すと、**Op Mode** は反復を続け、「Status: Running」メッセージを**DRIVER STATION** に送信します。**Op Mode** を停止するには、四角形のストップボタンを押します。

.. image:: images/TelemetryDH.png
   :align: center

|

.. image:: images/OnBotDoc_PressStop.jpg
   :align: center

|

おめでとうございます！最初のJava **Op Mode** を実行しました！

Op Mode を変更してモーターを制御する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**REV Expansion Hub** に接続して構成したDCモーターを制御するように**Op Mode** を変更しましょう。プログラムループのコードを次のように変更します：

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

追加されたコードを見ると、whileループに入る前に、target powerという新しい変数を定義していることがわかります。

.. code-block:: java

   double tgtPower = 0;

whileループの開始時に、変数 tgtPower を gamepad1 の左ジョイスティックの負の値と等しく設定します：

.. code-block:: java

   tgtPower = -this.gamepad1.left_stick_y;

オブジェクト gamepad1 は、runOpMode メソッドでアクセスできます。これは、**OPERATOR CONSOLE** のゲームパッド #1 の状態を表します。なお、競技中に使用されるF310ゲームパッドの場合、ジョイスティックのY値は、ジョイスティックが最上位置にあるときは -1 から、最下位置にあるときは +1 までの範囲です。上記の例のコードでは、left_stick_y 値を否定して、左ジョイスティックを前方に押すとモーターに正のパワーが適用されるようにしています。なお、この例では、モーターの前方と後方の概念は任意です。ただし、ジョイスティックのy値を否定する概念は、実際には非常に便利です。

.. image:: images/OnBotDoc_left_stick_y.jpg
   :align: center

|

次のステートメントのセットは、motorTest のパワーを変数 tgtPower で表される値に設定します。次に、目標パワーと実際のモーターパワーの値が、**telemetry** メカニズムを介して**DRIVER STATION** に送信されるデータのセットに追加されます。

.. code-block:: java

       tgtPower = -this.gamepad1.left_stick_y;
       motorTest.setPower(tgtPower);
       telemetry.addData("Target Power", tgtPower);
       telemetry.addData("Motor Power", motorTest.getPower());

**Op Mode** を変更してこれらの新しいステートメントを含めた後、ビルドボタンを押して、**Op Mode** が正常にビルドされたことを確認します。

ゲームパッドを接続して Op Mode を実行する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*  **Op Mode** はゲームパッドから入力を受け取り、この入力を使用してDCモーターを制御します。**Op Mode** を実行するには、Logitech F310 ゲームパッドを**DRIVER STATION** に接続する必要があります。

ゲームパッドを **DRIVER STATION** に接続します。スマートフォンを使用している場合は、Micro USB OTG アダプターケーブルが必要です。

.. image:: images/GamepadDHConnection.jpg
   :align: center

|

.. image:: images/RunningOpModeStep2.jpg
   :align: center

|

例の **Op Mode** は、ユーザーまたはドライバー #1 として指定されたゲームパッドからの入力を探しています。Logictech F310 コントローラーのスタートボタンとAボタンを同時に押して、ゲームパッドをユーザー #1 として指定します。なお、スタートボタンとBボタンを同時に押すと、ゲームパッドがユーザー #2 として指定されます。

.. image:: images/RunningOpModeStep3.jpg
   :align: center

|

ゲームパッドをユーザー #1 として正常に指定した場合、**DRIVER STATION** 画面の右上隅にある「User 1」というテキストの上に小さなゲームパッドアイコンが表示されるはずです。ゲームパッド #1 でアクティビティがあるたびに、小さなアイコンが緑色で強調表示されるはずです。アイコンが表示されない場合、またはゲームパッドを使用しても緑色で強調表示されない場合は、ゲームパッドへの接続に問題があります。

「MyFIRSTJavaOpMode」**Op Mode** を選択、初期化、実行します。なお、**Op Mode** をリビルドするたびに、現在の**Op Mode** 実行を停止してから再起動する必要があります。これにより、作成した変更が有効になります。

ゲームパッドを正しく構成した場合、左ジョイスティックでモーターの動きを制御できるはずです。**Op Mode** を実行するときは、注意して、回転するモーターに何も巻き込まれないようにしてください。なお、ジョイスティックを動かすたびに、ユーザー #1 ゲームパッドアイコンが緑色で強調表示されるはずです。また、目標パワーと実際のモーターパワーの値が**DRIVER STATION** のテレメトリエリアに表示されるはずです。

.. image:: images/TelemetryDH.png
   :align: center

|

.. image:: images/OnBotDoc_RunOpModeDCMotor.jpg
   :align: center

|

