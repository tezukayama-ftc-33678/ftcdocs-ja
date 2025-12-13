OpMode の作成と実行 :bdg-success:`AS`
======================================

TeamCode モジュール
~~~~~~~~~~~~~~~~~~~

Android Studio プロジェクトフォルダーを正常にインポートした場合、プロジェクトブラウザーに ``TeamCode`` という名前の Android モジュールが表示されます。Android Studio プロジェクトフォルダーは、競技用ロボットを制御するために作成するカスタム **OpMode**を含む**Robot Controller** アプリのバージョンをビルドするために使用されます。

.. image:: images/teamcodeFolder.jpg
   :align: center

|

クラスと **OpMode** を作成する際は、TeamCode モジュールに存在する ``org.firstinspires.ftc.teamcode`` パッケージ内に作成します。このパッケージは、Android Studio プロジェクトフォルダー内であなたが使用するために予約されています。

Javadoc リファレンス情報
~~~~~~~~~~~~~~~~~~~~~~~~

SDK の Javadoc リファレンスドキュメントはオンラインで利用できます。
SDK ドキュメントを表示するには、次の URL にアクセスしてください。

*  https://javadoc.io/doc/org.firstinspires.ftc

自動インポートの有効化
~~~~~~~~~~~~~~~~~~~~~~

**Android Studio**の自動インポート機能は、**OpMode** を記述する際の時間を節約するのに役立つ便利な機能です。この機能を有効にする場合は、Android Studio 設定画面から Editor->General->Auto Import 項目を選択します。これにより、エディターの自動インポート設定が表示されます。

「Add unambiguous imports on the fly」をチェックすると、**Android Studio**が**OpMode** で使用したいクラスに必要なインポート文を自動的に追加します。

.. image:: images/AutoImport.jpg
   :align: center

|

サンプル OpMode
~~~~~~~~~~~~~~~

ロボットのプログラミング方法を学ぶ優れた方法は、Android Studio プロジェクトフォルダーに含まれているサンプル **OpMode** を調べることです。これらのファイルは、FtcRobotController モジュールの ``org.firstinspires.ftc.robotcontroller.external.samples`` パッケージにあります。

.. image:: images/externalSamples.jpg
   :align: center

|

サンプル **OpMode** を使用したい場合は、``org.firstinspires.ftc.robotcontroller.external.samples``パッケージからコピーして、``org.firstinspires.ftc.teamcode`` パッケージに移動します。

新しくコピーした **OpMode** で、次のアノテーションを探します。

``@Disabled``

この行をコメントアウトして **OpMode**を有効にし、**Robot Controller** で実行できるようにします。

``//@Disabled``

最初の OpMode の作成
~~~~~~~~~~~~~~~~~~~~

``org.firstinspires.ftc.teamcode``パッケージを右クリックし、ポップアップメニューから New->Java Class を選択します。Create New Class ダイアログボックスが表示されます。新しいクラスの名前を``MyFIRSTJavaOpMode`` と指定します。

.. image:: images/CreateLinearOpMode.jpg
   :align: center

|

OK ボタンを押して新しいクラスを作成します。新しいクラスのソースコードが Android Studio ユーザーインターフェースの編集ペインに表示されます。

.. image:: images/NewOpMode.jpg
   :align: center

|

**OpMode** のメイン部分を次のコードのように変更します（次のソースコードでは、パッケージ定義といくつかのインポート文が省略されていることに注意してください）。

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

このソースコードを、最初の **OpMode** のフレームワークとして使用します。
**Android Studio** は、編集中にソースコードを自動的に保存することに注意してください。

おめでとうございます！**OpMode** を作成しました。まだあまり機能はありませんが、より便利にするために変更を加えていきます。

OpMode の構造を理解する
~~~~~~~~~~~~~~~~~~~~~~~

**OpMode**を、**Robot Controller**が実行するタスクのリストと考えると役立ちます。線形**OpMode**の場合、**Robot Controller**はこのタスクのリストを順次処理します。ユーザーは、制御ループ（while ループなど）を使用して、**Robot Controller**に線形**OpMode** 内の特定のタスクを繰り返し（または反復）させることもできます。

.. image:: images/ExaminingStructurePic2.jpg
   :align: center

|

**OpMode**をロボットへの命令のリストと考えると、作成したこの一連の命令は、チームメンバーがこの**Robot Controller**で利用可能な**OpMode**のリストから ``MyFIRSTJavaOpMode`` という**OpMode** を選択すると、ロボットによって実行されます。

新しく作成した **OpMode**の構造を見てみましょう。以下は**OpMode** テキストのコピーです（一部のコメント、パッケージ定義、およびいくつかのインポートパッケージステートメントは省略されています）。

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

**OpMode**の開始時には、クラス定義の前にアノテーションがあります。このアノテーションは、これが遠隔操作（つまり、ドライバーが制御する）**OpMode** であることを示しています。

``@TeleOp``

この **OpMode**を自律**OpMode** に変更したい場合は、``@TeleOp``を``@Autonomous`` アノテーションに置き換えます。

サンプルコードから、**OpMode**が Java クラスとして定義されていることがわかります。この例では、**OpMode**名は ``MyFIRSTJavaOpMode`` と呼ばれ、**LinearOpMode** クラスから特性を継承しています。

.. code-block:: java

   public class MyFIRSTJavaOpMode extends LinearOpMode {

また、OnBot Java エディターがこの **OpMode**用に5つのプライベートメンバー変数を作成したことがわかります。これらの変数は、OnBot Java エディターが**Robot Controller** の構成ファイルで検出した5つの構成済みデバイスへの参照を保持します。

.. code-block:: java

       private Gyroscope imu;
       private DcMotor motorTest;
       private DigitalChannel digitalTouch;
       private DistanceSensor sensorColorRange;
       private Servo servoTest;

次に、``runOpMode``と呼ばれるオーバーライドされたメソッドがあります。``LinearOpMode`` 型のすべての **OpMode**は、このメソッドを実装する必要があります。このメソッドは、ユーザーが**OpMode** を選択して実行したときに呼び出されます。

.. code-block:: java

       @Override
       public void runOpMode() {

``runOpMode``メソッドの開始時に、**OpMode**は``hardwareMap`` という名前のオブジェクトを使用して、**Robot Controller** の構成ファイルにリストされているハードウェアデバイスへの参照を取得します。

.. code-block:: java

           imu = hardwareMap.get(Gyroscope.class, "imu");
           motorTest = hardwareMap.get(DcMotor.class, "motorTest");
           digitalTouch = hardwareMap.get(DigitalChannel.class, "digitalTouch");
           sensorColorRange = hardwareMap.get(DistanceSensor.class, "sensorColorRange");
           servoTest = hardwareMap.get(Servo.class, "servoTest");

``hardwareMap``オブジェクトは、``runOpMode`` メソッド内で使用できます。これは **HardwareMap** クラスのタイプのオブジェクトです。

**OpMode**で特定のデバイスへの参照を取得しようとする場合、``HardwareMap.get``メソッドの2番目の引数として指定する名前は、構成ファイルでデバイスを定義するために使用された名前と一致する必要があることに注意してください。例えば、``motorTest``という名前の DC モーターを持つ構成ファイルを作成した場合、``hardwareMap`` オブジェクトからこのモーターを取得するには、同じ名前（大文字と小文字が区別されます）を使用する必要があります。名前が一致しない場合、**OpMode** はデバイスが見つからないことを示す例外をスローします。

例の次のいくつかのステートメントで、**OpMode**はユーザーに続行するためのスタートボタンを押すように促します。``runOpMode``メソッドで使用できる別のオブジェクトを使用します。このオブジェクトは telemetry と呼ばれ、**OpMode**は``addData``メソッドを使用して**Driver Station**に送信するメッセージを追加します。次に、**OpMode**は update メソッドを呼び出してメッセージを**Driver Station**に送信します。その後、``waitForStart`` メソッドを呼び出して、ユーザーがドライバーステーションのスタートボタンを押して**OpMode** の実行を開始するまで待機します。

.. code-block:: java

           telemetry.addData("Status", "Initialized");
           telemetry.update();
           // Wait for the game to start (driver presses PLAY)
           waitForStart();

すべての線形 **OpMode**には、ドライバーがスタートボタンを押すまでロボットが**OpMode** の実行を開始しないようにするために、``waitForStart`` ステートメントが必要であることに注意してください。

スタートコマンドを受信した後、**OpMode**は while ループに入り、**OpMode**がアクティブでなくなるまで（つまり、ユーザーが**Driver Station** の停止ボタンを押すまで）このループで反復を続けます。

.. code-block:: java

           // run until the end of the match (driver presses STOP)
           while (opModeIsActive()) {
               telemetry.addData("Status", "Running");
               telemetry.update();

           }

**OpMode**が while ループで反復する際、インデックスが「Status」でメッセージが「Running」のテレメトリメッセージを**Driver Station** に表示し続けます。

OpMode のビルドとインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Robot Controller** スマートフォンがラップトップに接続されており、ラップトップがスマートフォンに対する USB デバッグ権限を持っていることを確認します。

.. image:: images/phoneUSBConnected.jpg
   :align: center

|

または、**Control Hub**を使用している場合は、**Control Hub**が新しく充電された 12V バッテリーで駆動されており、USB Type C ポートを介してラップトップに接続されていることを確認します。**Control Hub** には USB デバッグ権限が自動的に有効になっている必要があることに注意してください。

.. image:: images/controlHubUSBConnected.jpg
   :align: center

|

**Control Hub**を使用する場合は、**Control Hub** を開発用ラップトップに接続する際に、Type C ポート（USB Mini ポートではなく）を使用するようにしてください。

.. image:: images/typeC.jpg
   :align: center

|

Android Studio ユーザーインターフェースの上部を見て、``TeamCode`` という単語の横にある小さな緑色の再生または実行ボタン（緑色の円形の矢印で表されます）を見つけます。正しいデバイスが選択されていることを確認してから、この緑色のボタンを押して **Robot Controller**アプリをビルドし、**Control Hub** （または RC スマートフォン）にインストールします。

.. image:: images/RunTeamCode.jpg
   :align: center

|

以前に Google Play ストアから **Robot Controller**アプリのコピーをインストールしていた場合、新しくビルドされたアプリのインストールは最初の試行時に失敗します。これは、**Android Studio**が、今ビルドしたアプリが Google Play からインストールされた公式バージョンの**Robot Controller** アプリとは異なるデジタル署名を持っていることを検出するためです。

.. image:: images/ApplicationInstallFailed.jpg
   :align: center

|

これが発生した場合、**Android Studio**は、デバイスから以前の（公式）バージョンのアプリをアンインストールし、更新されたバージョンのアプリに置き換えても良いかどうかを尋ねます。``OK`` を選択して以前のバージョンをアンインストールし、新しく作成した**Robot Controller** アプリに置き換えます（上の画像を参照）。

.. image:: images/RCLaunched.jpg
   :align: center

|

インストールが成功すると、**Robot Controller**アプリがターゲット Android デバイスで起動されるはずです。**Robot Controller**として Android スマートフォンを使用している場合は、スマートフォンにメインの**Robot Controller** アプリ画面が表示されます。

**Control Hub**には組み込みの画面がありませんが、**Control Hub**ユーザーの場合、**Driver Station**を確認することで、アプリが**Control Hub**に正しくインストールされたことを確認できます。**Driver Station**が**Control Hub** に正常に接続されていることを示している場合（更新の発生中に一時的に切断された後）、アプリは正常に更新されました。

OpMode の実行
~~~~~~~~~~~~~

新しい **OpMode**を含む更新された Android アプリを正常にビルドおよびインストールした場合、**OpMode**を実行する準備が整いました。**Driver Station**がまだ**Robot Controller**に接続されていることを確認します。サンプルの**OpMode**を遠隔操作**OpMode**として指定したため、``TeleOp``**OpMode** としてリストされます。

**Driver Station**で、``TeleOp`` ドロップダウンリストコントロールを使用して、使用可能な**OpMode**のリストを表示します。リストから**OpMode** （「MyFIRSTJavaOpMode」）を選択します。

.. image:: images/OpModeSelectionDH.png
   :align: center

|

.. image:: images/OnBotDoc_SelectMyFIRSTOpMode.jpg
   :align: center

|

「INIT」ボタンを押して **OpMode** を初期化します。

.. image:: images/InitDH.png
   :align: center

|

.. image:: images/OnBotDoc_MyFIRSTPushInit.jpg
   :align: center

|

**OpMode** は、runOpMode メソッド内のステートメントを waitForStart ステートメントまで実行します。その後、続行するためにスタートボタン（三角形の記号で表されます）を押すまで待機します。

.. image:: images/RunDH.png
   :align: center

|

.. image:: images/OnBotDoc_PressStart.jpg
   :align: center

|

スタートボタンを押すと、**OpMode**は反復を続け、「Status: Running」メッセージを**Driver Station**に送信します。**OpMode** を停止するには、四角形の停止ボタンを押します。

.. image:: images/TelemetryDH.png
   :align: center

|

.. image:: images/OnBotDoc_PressStop.jpg
   :align: center

|

おめでとうございます！最初の Java **OpMode** を実行しました！

モーターを制御するための OpMode の変更
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**REV Robotics Control Hub**または**REV Robotics Expansion Hub**用に接続および構成した DC モーターを制御するために、**OpMode** を変更しましょう。プログラムループのコードを次のように変更します。

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

追加されたコードを見ると、while ループに入る前に、target power という新しい変数を定義したことがわかります。

.. code-block:: java

   double tgtPower = 0;

while ループの開始時に、変数 tgtPower を gamepad1 の左ジョイスティックの負の値に設定します。

.. code-block:: java

   tgtPower = -this.gamepad1.left_stick_y;

``gamepad1``オブジェクトは、``runOpMode`` メソッド内でアクセスできます。これは、**Driver Station** 上のゲームパッド #1 の状態を表します。
競技中に使用される F310 ゲームパッドでは、ジョイスティックの Y 値は、ジョイスティックが最上部の位置にあるときは -1 から、最下部の位置にあるときは +1 までの範囲であることに注意してください。
上のサンプルコードでは、``left_stick_y`` 値を否定して、左ジョイスティックを前方に押すとモーターに正の電力が適用されるようにします。この例では、モーターの前進と後退の概念は任意であることに注意してください。ただし、ジョイスティックの y 値を否定する概念は、実際には非常に有用です。

.. image:: images/OnBotDoc_left_stick_y.jpg
   :align: center

|

次の一連のステートメントは、motorTest の電力を変数 tgtPower で表される値に設定します。次に、目標電力と実際のモーター電力の値が、テレメトリメカニズムを介して **Driver Station** に送信されるデータのセットに追加されます。

.. code-block:: java

       tgtPower = -this.gamepad1.left_stick_y;
       motorTest.setPower(tgtPower);
       telemetry.addData("Target Power", tgtPower);
       telemetry.addData("Motor Power", motorTest.getPower());

これらの新しいステートメントを含めるように **OpMode**を変更したら、ビルドボタンを押して**OpMode** が正常にビルドされたことを確認します。

ゲームパッドを接続して OpMode を実行する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**OpMode**は、ゲームパッドから入力を受け取り、この入力を使用して DC モーターを制御します。**OpMode**を実行するには、Logitech F310 または他の承認されたゲームパッドを**Driver Station** に接続する必要があります。

ゲームパッドを **Driver Station**に接続します。**REV Robotics Driver Hub**を使用している場合、ゲームパッドを USB-A ポートの1つに直接接続できます。**DRIVER STATION** スマートフォンの場合、Micro USB OTG アダプターケーブルが必要です。

.. image:: images/GamepadDHConnection.jpg
   :align: center

|

.. image:: images/RunningOpModeStep2.jpg
   :align: center

|

サンプル **OpMode** は、ユーザーまたはドライバー #1 として指定されたゲームパッドからの入力を探しています。Logitech F310 コントローラーの Start ボタンと A ボタンを同時に押して、ゲームパッドをユーザー #1 として指定します。Start ボタンと B ボタンを同時に押すと、ゲームパッドがユーザー #2 として指定されることに注意してください。PS4 スタイルのゲームパッドでは、ユーザー #1 の場合は Options ボタンと Cross を、ユーザー #2 の場合は Options と Circle を使用します。

.. image:: images/RunningOpModeStep3.jpg
   :align: center

|

ゲームパッドをユーザー #1 として正常に指定した場合、**Driver Station** 画面の右上隅にある「User 1」というテキストの上に小さなゲームパッドアイコンが表示されます。ゲームパッド #1 でアクティビティがあるたびに、小さなアイコンが緑色で強調表示されます。アイコンが表示されない場合、またはゲームパッドを使用したときに緑色で強調表示されない場合は、ゲームパッドへの接続に問題があります。

``MyFIRSTJavaOpMode`` **OpMode** を選択、初期化、実行します。

ゲームパッドを正しく構成した場合、左ジョイスティックでモーターの動きを制御できるはずです。**OpMode**を実行する際は、回転するモーターに何もが巻き込まれないように注意してください。ジョイスティックを動かすたびに、ユーザー #1 ゲームパッドアイコンが緑色で強調表示されることに注意してください。また、目標電力と実際のモーター電力の値が**Driver Station** のテレメトリエリアに表示されることにも注意してください。

.. image:: images/TelemetryDH.png
   :align: center

|

.. image:: images/OnBotDoc_RunOpModeDCMotor.jpg
   :align: center

|

