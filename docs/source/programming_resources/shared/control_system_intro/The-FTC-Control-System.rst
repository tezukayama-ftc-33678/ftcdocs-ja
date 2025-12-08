制御システム入門
===========================

*FIRST* Tech Challenge について
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*FIRST* Tech Challenge は、メンター指導による競技ロボットへの参加を通じて、若者が次世代のSTEMリーダーやイノベーターになるよう刺激することを目指しています。*FIRST* Tech Challenge に参加するチームは、さまざまなタスクを実行するロボットを構築する必要があります。タスクはシーズンごとに異なり、各シーズンの開始時に公開されるゲームルールに基づいています。ロボットが完了できるタスクが多いほど、チームはより多くのポイントを獲得できます。

.. image:: images/HoustonMatchPlay.jpg
   :align: center

.. rst-class:: center

(Photo courtesy of Dan Donovan, ©2017 Dan Donovan / www.dandonovan.com)

AUTO と TELEOP
~~~~~~~~~~~~~~~

*FIRST* Tech Challenge のマッチには、**AUTO** フェーズと **TELEOP** フェーズがあります。マッチの **AUTO** フェーズでは、ロボットは人間の入力や制御なしで動作します。**TELEOP** フェーズでは、ロボットは最大2人の人間ドライバーから入力を受け取ることができます。

ポイントツーポイント制御システム
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*FIRST* Tech Challenge では、Android デバイスを使用してロボットを制御します。競技中、各チームは2つの Android デバイスを使用します。

.. image:: images/PointToPointControl.jpg
   :align: center

|

1つの Android デバイスはロボットに搭載され、**Robot Controller** と呼ばれます。ほとんどの場合、**Robot Controller** は **REV Robotics Control Hub** に統合されています。**Robot Controller** はロボットの「頭脳」として機能します。ロボットのすべての思考を行い、ロボットに何をすべきかを指示します。**Robot Controller** アプリを実行する Android デバイスで構成されています。多くのチームは、モーター、サーボ、センサーをロボットに接続するための追加ポートとして、**REV Robotics Expansion Hub** も接続します。

2つ目の Android デバイスは、チームのドライバーと一緒に配置され、1つまたは2つのゲームパッドが接続されます。この2つ目のデバイスは **Driver Station** として知られています。**Driver Station** は、テレビを制御するために使用するリモコンのようなものです。**Driver Station** により、チームは（安全なワイヤレス接続を使用して）**Robot Controller** とリモート通信し、**Robot Controller** にコマンドを発行できます。**Driver Station** は、**Driver Station** アプリを実行する Android デバイスで構成されています。ほとんどのチームは **REV Robotics Driver Hub** を使用しますが、一部の Android スマートフォンもサポートされています。

REV Robotics Control Hub と Expansion Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**REV Robotics Control Hub** または **Expansion Hub** は、**Robot Controller** がロボットのモーター、サーボ、センサーと通信できるようにする電子入出力（「I/O」）モジュールです。**Robot Controller** は **Control Hub** に統合されており、シリアル接続を介して **Expansion Hub** と通信します。Android スマートフォンを **Robot Controller** として使用する場合は、USB ケーブルを使用してシリアル接続を確立します。

**Control Hub** と **Expansion Hub** は、12V バッテリーにも接続されており、**Control Hub**、**Expansion Hub**、モーター、サーボ、センサーに電力を供給します。Android スマートフォンを **Robot Controller** として使用する場合、スマートフォンには独自の独立したバッテリーがあります。

.. image:: images/REVControlHubLayout.png
   :align: center

|

Android スマートフォン
~~~~~~~~~~~~~~~~~~~

チームは、Android スマートフォンを **Driver Station**、**Robot Controller**、またはその両方として使用することを選択できます。**Driver Station** のスマートフォンには、**FTC Driver Station** アプリをインストールする必要があり、ゲームパッドを接続するには OTG アダプター USB ハブが必要です。

.. image:: images/ControlHubEquals.jpg
   :align: center

|

Android スマートフォンを **Robot Controller** として使用するチームは、モーター、サーボ、センサーを接続するために追加の **REV Robotics Expansion Hub** を必要とします。スマートフォンは、USB-A to USB-Mini ケーブルと OTG アダプターを介して **Expansion Hub** に接続されます。

.. image:: images/REVExpansionHubLayout.jpg
   :align: center

|

OpMode とは？
~~~~~~~~~~~~~~~~~

*FIRST* Tech Challenge のマッチでは、チームのロボットは得点を獲得するためにさまざまなタスクを実行する必要があります。たとえば、競技フィールド上の白い線をロボットに追従させ、マッチ中に自律的にゲーム要素（ボールなど）をゴールに得点させたいと考えるかもしれません。チームは、ロボットの動作を指定するために「**OpMode**」（「operational mode（動作モード）」の略）を作成します。

**OpMode** は、競技ロボットの動作をカスタマイズするために使用されるコンピュータプログラムです。**Robot Controller** は、選択された **OpMode** を実行して、マッチ中に特定のタスクを実行できます。

*FIRST* Tech Challenge に参加しているチームは、独自の **OpMode** を作成するために使用できるさまざまなプログラミングツールを持っています。チームは、**Blocks Programming Tool** と呼ばれるビジュアル（「ドラッグアンドドロップ」）プログラミングツールを使用して **OpMode** を作成できます。チームは、**OnBot Java Programming Tool** として知られるテキストベースの Java ツール、または Google の **Android Studio** 統合開発環境（「IDE」としても知られる）を使用して **OpMode** を作成することもできます。
