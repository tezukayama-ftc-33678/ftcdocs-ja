Op Mode の作成 :bdg-warning:`Blocks`
========================================


Op Mode とは？
~~~~~~~~~~~~~~

典型的な **FIRST** Tech Challenge のマッチでは、チームのロボットは得点を獲得するために
さまざまなタスクを実行する必要があります。例えば、チームは競技フロアの白線をロボットが
追従し、マッチ中に自律的にゲーム要素をゴールに入れることを望むかもしれません。チームは
ロボットの動作を指定するために **op modes**（「operational modes」の略）と呼ばれる
プログラムを作成します。これらの **op modes** は、**DRIVER STATION** で選択された後、
**Robot Controller** 上で実行されます。

**FIRST** Tech Challenge に参加するチームは、独自の **op modes** を作成するために
使用できるさまざまなプログラミングツールを利用できます。このセクションでは、
**Blocks Programming Tool** を使用してロボット用の **op mode** を作成する方法を説明します。

Blocks Programming Tool
~~~~~~~~~~~~~~~~~~~~~~~

**Blocks Programming Tool** は、**Robot Controller** によって提供されるユーザーフレンドリーな
プログラミングツールです。ユーザーはこのツールを使用してロボット用のカスタム **op modes** を
作成し、これらの **op modes** を **Robot Controller** に直接保存できます。ユーザーは
ジグソーパズル型のプログラミングブロックをデザイン「キャンバス」上にドラッグ＆ドロップし、
これらのブロックを配置して **op mode** のプログラムロジックを作成します。**Blocks Programming Tool** は
Google の Blockly ソフトウェアを利用しており、Google のサポートを受けて開発されました。

.. image:: images/BlocksPicture1New.jpg
   :align: center

|

このセクションの例では、Windows ラップトップコンピューターを使用して **Robot Controller** に
接続します。この Windows ラップトップコンピューターには、**Blocks Programming Tool** に
アクセスするために使用される JavaScript 対応のウェブブラウザがインストールされています。

.. image:: images/BlocksPicture2.jpg
   :align: center

|

**Robot Controller** として **Control Hub** を使用している場合でも、**op mode** を作成および
編集するプロセスは同じです。

.. image:: images/BlocksPicture2b.jpg
   :align: center

|

なお、Windows コンピューターの代わりに、Apple Mac ラップトップ、Apple iPad、Android タブレット、
または Chromebook などの代替デバイスを使用して **Blocks Programming Tool** にアクセスすることも
できます。ただし、このドキュメントに含まれる手順は、Windows ラップトップを使用していることを
前提としています。

また、このセクションでは、Android デバイスとロボットハードウェアのセットアップと構成が既に
完了していることを前提としています。また、ラップトップが **Robot Controller** の
Program & Manage ワイヤレスネットワークに正常に接続されていることも前提としています。

最初の Op Mode の作成
~~~~~~~~~~~~~~~~~~~~~~

ラップトップが **Robot Controller** の Program & Manage ワイヤレスネットワークに正常に
接続できた場合、最初の **op mode** を作成する準備が整いました。このセクションでは、
**Blocks Programming Tool** を使用して、最初の **op mode** のプログラムロジックを作成します。

なお、最初の **op mode** の作成には約 10 分かかります。

最初の Op Mode の作成手順
--------------------------

1. ラップトップでウェブブラウザを起動し（**FIRST** では Google Chrome の使用を推奨）、
**Robot Controller** の Program & Manage 画面に表示されているウェブアドレスを確認します。

.. important:: **Robot Controller** が Android スマートフォンの場合、Program & Manage サーバーにアクセスするアドレスは "192.168.49.1:8080" です。

.. image:: images/WritingFirstOpModeStep1a.jpg
   :align: center

|

.. important:: **Robot Controller** が **Control Hub** の場合、Program & Manage サーバーにアクセスするアドレスは "192.168.43.1:8080" です。IP アドレスの第3オクテットの違いに注意してください（**Control Hub** は "49" ではなく "43" です）。

.. image:: images/WritingFirstOpModeStep1aControlHub.jpg
   :align: center

|

   このウェブアドレスをブラウザのアドレスフィールドに入力し、RETURN キーを押して Program & Manage ウェブサーバーに移動します。

.. image:: images/WritingFirstOpModeStep1bControlHub.jpg
   :align: center

|

2. ウェブブラウザがプログラミングモードサーバーに接続されていることを確認します。
プログラミングモードサーバーに正常に接続されている場合、Robot Controller Console が
表示されます。

.. image:: images/WritingFirstOpModeStep2ControlHub.jpg
   :align: center

|

3. Console の上部にある **Blocks** リンクをクリックして、メインの Blocks Programming 
画面に移動します。

.. image:: images/WritingFirstOpModeStep3aControlHub.jpg
   :align: center

|

   メインの Blocks Programming 画面は、新しい **op modes** を作成する場所です。また、**Robot Controller** 上の既存の Blocks Op Modes のリストを表示する画面でもあります。最初の **op mode** を作成して保存するまで、このリストは空です。

.. image:: images/WritingFirstOpModeStep3bControlHub.jpg
   :align: center

|

4. ブラウザウィンドウの左上隅に表示されている "Create New Op Mode" ボタンをクリックします。

.. image:: images/WritingFirstOpModeStep4ControlHub.jpg
   :align: center

|

   プロンプトが表示されたら、**op mode** の名前を指定し、"OK" をクリックして続行します。

5. 新しい **op mode** が作成されたことを確認します。ウェブブラウザのメイン画面に、
新しく作成された **op mode** が編集用に開かれているはずです。

.. image:: images/WritingFirstOpModeStep5ControlHub.jpg
   :align: center

|

   ブラウザ画面の左側には、カテゴリ別に分類されたプログラミングブロックのリストが表示されています。カテゴリをクリックすると、ブラウザに関連する利用可能なプログラミングブロックのリストが表示されます。

   画面の右側は、プログラミングブロックを配置して **op mode** のロジックを作成する場所です。


Examining the Structure of Your Op Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you create a new op mode, there should already be a set of
programming blocks that are placed on the design canvas for your op
mode. These blocks are automatically included with each new op mode that
you create. They create the basic structure for your op mode.

.. image:: images/ExaminingStructurePic1ControlHub.jpg
   :align: center

|

上図では、**op mode** のメイン本体は、上部に "to runOpMode" という文字が付いた
外側の紫色のブラケットによって定義されています。ヘルプのヒントが示すように、
この関数は、この **op mode**（この例では "MyFIRSTOpMode"）が **DRIVER STATION** から
選択されたときに実行されます。

**op mode** を、**Robot Controller** が実行するタスクのリストと考えると役立ちます。
**Robot Controller** は、このタスクのリストを順次処理します。ユーザーは、制御ループ
（while ループなど）を使用して、**op mode** 内の特定のタスクを **Robot Controller** に
繰り返し（または反復）させることもできます。

.. image:: images/ExaminingStructurePic2.jpg
   :align: center

|

**op mode** をロボットへの命令リストと考えると、この命令セットは、チームメンバーが
この **Robot Controller** で利用可能な **op modes** のリストから "MyFIRSTOpMode" という
**op mode** を選択するたびに、ロボットによって実行されます。

疑問符（"?"）が付いた青いボタンをクリックすると、ヘルプテキストを非表示にできます。
この基本的な **op mode** のフローを見てみましょう。"Put initialization blocks here" という
文字が付いた青色のブロックはコメントです。コメントは、人間のユーザーのために **op mode** に
配置されます。ロボットは、**op mode** 内のコメントを無視します。

.. image:: images/ExaminingStructurePic3.jpg
   :align: center

|

"Put initialization blocks here" コメントの後（および "call MyFIRSTOpMode.waitForStart" 
ブロックの前）に配置されたプログラミングブロックは、ユーザーが **DRIVER STATION** で
**op mode** を最初に選択したときに実行されます。

**Robot Controller** が "call MyFIRSTOpMode.waitForStart" というラベルの付いたブロックに
到達すると、**DRIVER STATION** から Start コマンドを受信するまで停止して待機します。
Start コマンドは、ユーザーが **DRIVER STATION** の Start ボタンを押すまで送信されません。
"call MyFIRSTOpMode.waitForStart" ブロックの後のコードは、Start ボタンが押された後に
実行されます。

.. image:: images/ExaminingStructurePic4.jpg
   :align: center

|

"call MyFIRSTOpMode.waitForStart" の後には、条件付き "if" ブロック
（"if call MyFIRSTOpMode.isActive"）があり、**op mode** がまだアクティブな場合
（つまり、停止コマンドが受信されていない場合）にのみ実行されます。

.. image:: images/ExaminingStructurePic4bControlhub.jpg
   :align: center

|

"Put run blocks here" コメントの後、"repeat while call MyFirstOpMode.opModeIsActive" という
ラベルの付いた緑色のブロックの前に配置されたブロックは、Start ボタンが押された後、
**Robot Controller** によって順次実行されます。

"repeat while call MyFirstOpMode.opModeIsActive" というラベルの付いた緑色のブロックは、
反復またはループ制御構造です。

.. image:: images/ExaminingStructurePic5ControlHub.jpg
   :align: center

|

この緑色の制御ブロックは、"call MyFIRSTOpMode.opModeIsActive" の条件が true である限り、
ブロックの "do" 部分にリストされているステップを実行します。これは、**op mode** 
"MyFIRSTOpMode" が実行されている限り、ブロックの "do" 部分に含まれるステートメントが
繰り返し実行されることを意味します。ユーザーが Stop ボタンを押すと、
"call MyFIRSTOpMode.opModeIsActive" 句は true ではなくなり、"repeat while" ループは
繰り返しを停止します。

DC モーターの制御
~~~~~~~~~~~~~~~~~~

このセクションでは、ゲームパッドで DC モーターを制御できるようにするブロックを
**op mode** に追加します。

なお、このタスクを完了するには約 15 分かかります。

.. important:: ユーザーが構成したデバイス（モーター、サーボ、センサー）のプログラミングブロックは、構成されたデバイスが含まれたアクティブな構成ファイルがある場合にのみ、Blocks ツールに表示されます。デバイスのタイプがアクティブな構成ファイルに含まれていない場合、そのプログラミングブロックはブロックのパレットから欠落します。

まだ :doc:`構成ファイルを作成してアクティブ化していない </hardware_and_software_configuration/connecting_devices/index>` 場合は、
:doc:`このリンク </hardware_and_software_configuration/connecting_devices/index>` に従って実行してください。
構成ファイルを作成してアクティブ化した後、**op mode** を閉じて再度開くと、新しく構成された
デバイスのプログラミングブロックが表示されます。

DC モーターを制御するための Op Mode の変更手順
--------------------------------------------------

1. 画面の左側にある "Variables" というカテゴリをクリックして、**op mode** 内で
変数を作成および変更するために使用されるブロックコマンドのリストを表示します。

.. image:: images/AddingDCMotorStep1ControlHub.jpg
   :align: center

|

   "Create variable..." をクリックして、**op mode** のターゲットモーター出力を表す新しい変数を作成します。

2. プロンプトが表示されたら、新しい変数の名前（"tgtPower"）を入力します。

.. image:: images/AddingDCMotorStep2ControlHub.jpg
   :align: center

|

3. 新しい変数を作成すると、"Variables" ブロックカテゴリの下に追加の
プログラミングブロックが表示されます。

.. image:: images/AddingDCMotorStep3ControlHub.jpg
   :align: center

|

4. "set tgtPower to" プログラミングブロックをクリックし、マウスを使用して
"Put loop blocks here" コメントブロックの直後の位置にブロックをドラッグします。

.. image:: images/AddingDCMotorStep4ControlHub.jpg
   :align: center

|

   "set tgtPower to" ブロックは、正しい位置にスナップされます。

5. プログラミングブロックの "Gamepad" カテゴリをクリックし、利用可能な
ブロックのリストから "gamepad1.LeftStickY" ブロックを選択します。

.. image:: images/AddingDCMotorStep5ControlHub.jpg
   :align: center

|

   制御システムでは、最大 2 つのゲームパッドでロボットを制御できます。"gamepad1" を選択することで、ドライバー #1 として指定されたゲームパッドからの制御入力を使用するように **op mode** に指示しています。

6. "gamepad1.LeftStickY" ブロックをドラッグして、"set tgtPower to" ブロックの
右側にスナップするように配置します。このブロックセットは、継続的にループして
ゲームパッド #1 の左ジョイスティック（y 位置）の値を読み取り、変数 tgtPower を
左ジョイスティックの Y 値に設定します。

.. image:: images/AddingDCMotorStep6a.jpg
   :align: center

|

   F310 ゲームパッドの場合、ジョイスティックの Y 値は、ジョイスティックが最上位置にあるときは -1 から、最下位置にあるときは +1 までの範囲です。

.. image:: images/AddingDCMotorStep6bControlHub.jpg
   :align: center

|

   これは、例に示されているブロックの場合、左ジョイスティックを上に押すと、変数 tgtPower の値は -1 になることを意味します。

7. プログラミングブロックの "Math" カテゴリをクリックし、負の記号（"-"）を
選択します。

.. image:: images/AddingDCMotorStep7ControlHub.jpg
   :align: center

|

8. 負の記号（「否定演算子」とも呼ばれます）を "gamepad1.LeftStickY" ブロックの
左側にドラッグします。"set tgtPower to" ブロックの後、"gamepad1.LeftStickY" 
ブロックの前にクリックして配置されます。

.. image:: images/AddingDCMotorStep8ControlHub.jpg
   :align: center

|

この変更により、左ジョイスティックが最上位置にある場合、変数 tgtPower は +1 に設定され、ジョイスティックが最下位置にある場合は -1 に設定されます。

9. ブロックの "Actuators" カテゴリをクリックします。次に、"DcMotor" カテゴリの
ブロックをクリックします。

.. image:: images/AddingDCMotorStep9ControlHub.jpg
   :align: center

|

10. "set motorTest.Power to 1" プログラミングブロックを選択します。

.. image:: images/AddingDCMotorStep10ControlHub.jpg
   :align: center

|    

11. "set motorTest.Power to 1" ブロックをドラッグして、"set tgtPower to" ブロックの
すぐ下にスナップするように配置します。               

.. image:: images/AddingDCMotorStep11ControlHub.jpg
   :align: center

|

12. "Variables" ブロックカテゴリをクリックし、"tgtPower" ブロックを選択します。

.. image:: images/AddingDCMotorStep12ControlHub.jpg
   :align: center

|

13. "tgtPower" ブロックをドラッグして、"set motor1.Power to" ブロックの
すぐ右側にスナップするように配置します。

.. image:: images/AddingDCMotorStep13ControlHub.jpg
   :align: center

|

   "tgtPower" ブロックは、デフォルト値の "1" ブロックを自動的に置き換えます。

テレメトリステートメントの挿入
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**op mode** はほぼ実行準備が整いました。ただし、続行する前に、**Robot Controller** から
**DRIVER STATION** に情報を送信し、**DRIVER STATION** のユーザーインターフェースに
表示するテレメトリステートメントをいくつか追加します。このテレメトリメカニズムは、
ロボットからの状態情報を **DRIVER STATION** に表示するための便利な方法です。
このメカニズムを使用して、センサーデータ、モーターの状態、ゲームパッドの状態などを
**Robot Controller** から **DRIVER STATION** に表示できます。

なお、このタスクを完了するには約 15 分かかります。

テレメトリステートメントの挿入手順
------------------------------------

1. ブラウザウィンドウの左側にある "Utilities" カテゴリをクリックします。
"Telemetry" サブカテゴリを選択し、"call telemetry.addData(key, number)" ブロックを
選択します。

.. image:: images/TelemetryMotorStep1ControlHub.jpg
   :align: center

|

2. "call telemetry.addData(key, number)" ブロックをドラッグして、
"set motor1.Power to" ブロックの下に配置します。緑色のテキストブロック "key" を
クリックしてテキストをハイライトし、"Target Power" と読めるように変更します。

.. image:: images/TelemetryMotorStep2ControlHub.jpg
   :align: center

|

   "call telemetry.update" ブロックは重要なブロックです。テレメトリバッファに追加されたデータは、"telemetry.update" メソッドが呼び出されるまで **DRIVER STATION** に送信されません。

3. "Variables" ブロックカテゴリをクリックし、"tgtPower" ブロックを選択します。
ブロックをドラッグして、テレメトリプログラミングブロックの "number" パラメーターの
隣にクリックして配置します。

.. image:: images/TelemetryMotorStep3ControlHub.jpg
   :align: center

|

   **Robot Controller** は、変数 tgtPower の値を "Target Power" というキーまたはラベルとともに **DRIVER STATION** に送信します。キーは、**DRIVER STATION** の値の左側に表示されます。

4. このプロセスを繰り返し、新しいキーに "Motor Power" という名前を付けます。

.. image:: images/TelemetryMotorStep4ControlHub.jpg
   :align: center

|

5. "DcMotor" サブカテゴリを見つけてクリックします。"motorTest.Power" という
ラベルの付いた緑色のプログラミングブロックを探します。

.. image:: images/TelemetryMotorStep5ControlHub.jpg
   :align: center

|

6. "motorTest.Power" ブロックを 2 番目のテレメトリブロックの "number" パラメーターに
ドラッグします。

.. image:: images/TelemetryMotorStep6ControlHub.jpg
   :align: center

|

   これで、**op mode** はモーター出力情報も **Robot Controller** から送信して、**DRIVER STATION** に表示されるようになります。

Op Mode の保存
~~~~~~~~~~~~~~

**op mode** を変更した後、**op mode** を **Robot Controller** に保存することが非常に重要です。

なお、このタスクを完了するには約 1 分かかります。

Op Mode の保存手順
------------------

1. "Save Op Mode" ボタンをクリックして、**op mode** を **Robot Controller** に保存します。
保存が成功すると、ボタンの右側に "Save completed successfully" という文字が表示されます。

.. image:: images/SavingOpModeStep1ControlHub.jpg
   :align: center

|


Program & Manage 画面の終了
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**op mode** を変更して保存した後、**DRIVER STATION** がまだ Program & Manage 画面に
ある場合は、この画面を終了してメインの **DRIVER STATION** 画面に戻る必要があります。

なお、このタスクを完了するには約 1 分かかります。


プログラミングモードの終了手順
--------------------------------

1. Android の戻る矢印をクリックして、Program & Manage 画面を終了します。
**op mode** を実行する前に、Program & Manage 画面を終了する必要があります。

.. image:: images/SavingOpModeStep1ControlHub.jpg
   :align: center

|

おめでとうございます！**Blocks Programming Tool** を使用して最初の **op mode** を
作成しました！**op mode** の実行方法については、
:doc:`Running Your Op Mode <../running_op_modes/Running-Your-Op-Mode>` という
セクションで学習します。
