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

REV Robotics Control Hub と Expansion Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**REV Robotics Control Hub** または **Expansion Hub** は、**Robot Controller** がロボットのモーター、サーボ、センサーと通信できるようにする電子入出力（「I/O」）モジュールです。**Robot Controller** は **Control Hub** に統合されており、シリアル接続を介して **Expansion Hub** と通信します。Android スマートフォンを **Robot Controller** として使用する場合は、USB ケーブルを使用してシリアル接続を確立します。

**Control Hub** と **Expansion Hub** は、12V バッテリーにも接続されており、**Control Hub**、**Expansion Hub**、モーター、サーボ、センサーに電力を供給します。Android スマートフォンを **Robot Controller** として使用する場合、スマートフォンには独自の独立したバッテリーがあります。


















REV Robotics Control Hub and Expansion Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The REV Robotics Control Hub or Expansion Hub is the electronic input/output (or “I/O”)
module that lets the Robot Controller talk to the robot’s motors,
servos, and sensors. The Robot Controller is integrated into the Control Hub, and communicates with the
Expansion Hub through a serial connection. For the situation where an
Android smartphone is used as the Robot Controller, a USB cable is used
to establish the serial connection.

The Control Hub and Expansion Hub are also connected to a 12V battery which is used to
OpMode とは？
~~~~~~~~~~~~~~~~~

典型的な *FIRST* Tech Challenge のマッチでは、チームのロボットは得点を獲得するためにさまざまなタスクを実行する必要があります。たとえば、チームは、競技フィールド上の白い線をロボットに追従させ、マッチ中に自律的にゲーム要素（ボールなど）をゴールに得点させたいと考えるかもしれません。チームは、ロボットの動作を指定するために「**OpMode**」（「operational mode（動作モード）」の略）を作成します。

**OpMode** は、競技ロボットの動作をカスタマイズするために使用されるコンピュータプログラムです。**Robot Controller** は、選択された **OpMode** を実行して、マッチ中に特定のタスクを実行できます。

*FIRST* Tech Challenge に参加しているチームは、独自の **OpMode** を作成するために使用できるさまざまなプログラミングツールを持っています。チームは、**Blocks Programming Tool** と呼ばれるビジュアル（「ドラッグアンドドロップ」）プログラミングツールを使用して **OpMode** を作成できます。チームは、**OnBot Java Programming Tool** として知られるテキストベースの Java ツール、または Google の **Android Studio** 統合開発環境（「IDE」としても知られる）を使用して **OpMode** を作成することもできます。






















   :align: center

|

What’s an OpMode?
~~~~~~~~~~~~~~~~~

During a typical *FIRST* Tech Challenge match, a team’s robot has to
perform a variety of tasks in an effort to score points. For example, a
team might want their robot to follow a white line on the competition
floor and then score a game element (such as a ball) into a goal
autonomously during a match. Teams write “OpModes” (which stand for
“operational modes”) to specify the behavior for their robot.

An *OpMode* is a computer program that is used to customize the behavior
of a competition robot. The Robot Controller can *execute* a selected OpMode
to perform certain tasks during a match.

Teams who are participating in *FIRST* Tech Challenge have a variety
of programming tools that they can use to create their own OpMode.
Teams can use a visual (“drag and drop”) programming tool called the
*Blocks Programming Tool* to create their op modes. Teams can also
use a text-based Java tool known as the *OnBot Java Programming
Tool* or Google’s *Android Studio* integrated development environment
(also known as an “IDE”) to create their OpModes.
