*FIRST* Tech Challenge 用 HuskyLens 入門
==========================================

はじめに
------------

これは、**すでに決定した**チームのために、*FIRST* Tech Challenge で `HuskyLens <https://www.dfrobot.com/product-1922.html>`__ の使用を紹介するシンプルなチュートリアルです。その潜在能力を探索することを決定したチーム向けです。

.. figure:: images/020-HuskyLens-dual.png
   :align: center
   :width: 85%
   :alt: HuskyLens

   DFRobot HuskyLens

この**ビジョンセンサー**の基本サポートは、2023年9月の CENTERSTAGE ロボットゲームキックオフで FTC SDK バージョン 9.0 に追加されました。

HuskyLens は**オンボードプログラミング**を使用して、AI 支援学習、ビジョン処理、認識を実行します。**REV Control Hub** または **REV Expansion Hub** の **I2C センサーポート**に接続します。

HuskyLens は **USB ウェブカメラではなく**、FTC :ref:`VisionPortal <apriltag/vision_portal/visionportal_overview/visionportal-overview:VisionPortal Overview>` ソフトウェアを**使用しません**。

電気接続
---------------------

HuskyLens を **REV Control Hub** または **Expansion Hub** の I2C ポートに接続するには、**カスタムアダプターケーブル**が必要です。HuskyLens コネクタの 4 本のワイヤー/ピンは、REV Hub の 4 本のピンと同じ順序/位置ではありません。

3 本のワイヤーは、REV センサーケーブルのワイヤーと**同じ色**です。カスタムケーブルは、**赤を赤**に、**黒を黒**に、**青を青**に接続する必要があります。これにより、HuskyLens の**緑のワイヤー**のみが残ります。これを REV の**白いワイヤー**に接続します。簡単です！

このチュートリアルでは、次の（多くの）方法については説明して**いません**。

-  既存のケーブルを変更する（1 つのコネクタのピン順序を変更する）、**または**
-  カスタムケーブルを製作する：

   -  はんだ付け
   -  圧着コネクタ
   -  レバーナット（以下の例）

FTC 競技マニュアルではこの作業を許可していますが、チームはシーズンを通じてロボット競技のために高品質を確保する必要があります。

.. figure:: images/060-adapter.png
   :align: center
   :width: 85%
   :alt: Wiring an Adapter

   image credit: @texasdiaz

これらの配線手順が正しいことを確認するには、`HuskyLens のドキュメント <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336#target_3>`__ と `REV Hub のドキュメント <https://docs.revrobotics.com/duo-control/sensors/i2c#wiring>`__ を参照してください。次の「ピンアウト」情報が表示されます。

- HuskyLens **緑**ワイヤー 1（「T」）SDA またはデータ == REV Hub **白**ワイヤー 3「SDA」またはデータ
- HuskyLens **青**ワイヤー 2（「R」）SCL またはクロック == REV Hub **青**ワイヤー 4「SCL」またはクロック
- HuskyLens **黒**ワイヤー 3（「-」）GND またはグラウンド == REV Hub **黒**ワイヤー 1「GND」またはグラウンド
- HuskyLens **赤**ワイヤー 4（「+」）VCC または +3.3-5VDC == REV Hub **赤**ワイヤー 2「3.3V」または Vcc
.. figure:: images/070-ports.png
   :align: center
   :width: 85%
   :alt: Ports

   image credit: @texasdiaz

構成
-------------

新しいアダプターケーブルを使用して、HuskyLens を REV Hub の I2C ポートに接続します。**Bus 1、2、または 3** とラベル付けされた I2C 接続を使用すると、データトラフィックの過負荷（可能性は低い）を回避できます。

ラベル 0（ゼロ）は I2C Bus 0 であり、おそらく Port 0 に**内蔵 IMU** があります。I2C Bus には、トラフィックを共有する複数の I2C ポートを含めることができます。

**Driver Station** で、3 つのドットメニューをタッチし、``Configure Robot`` を選択します。

既存の（正しい）構成を編集するか、``New`` をタッチします。``Scan`` をタッチし、（Portal レベルを通じて）HuskyLens が接続されている特定の ``Expansion Hub`` または ``Control Hub`` に移動します。

HuskyLens が接続されている Bus 番号の ``I2C Bus 3`` またはその他の Bus を選択します。

.. figure:: images/120-DS-config.png
   :align: center
   :width: 85%
   :alt: DS Config

   Driver Station Config

Touch ``Add``, and select device “HuskyLens” from the drop-down list for
Port 0 (or first available port). Type the device name “huskylens”, as
expected by the Sample OpMode.

Touch ``Done`` several times, then ``Save``, to save and name/rename
this updated robot configuration. Touch the DS “Back” arrow, returning
to the DS app’s home screen.

新しい構成がアクティブな構成として画面に表示されていることを確認します。

サンプル OpMode
-------------

プログラミングコンピューターを **Robot Controller** に接続し、プログラミングソフトウェアを開きます。このチュートリアルでは、**FTC Blocks** を使用します。

.. note::
   **OnBot Java** and **Android Studio** users can easily follow along, since
   the Java Sample OpMode uses the same programming logic and is well
   commented.

In FTC Blocks, create a new OpMode using the sample called
“SensorHuskyLens”:

.. figure:: images/140-Sample-Blocks.png
   :align: center
   :width: 85%
   :alt: Blocks Sample

   HuskyLens Blocks サンプル

このサンプルはゲームパッドを使用しないため、**OpMode** タイプを ``TeleOp`` から ``Autonomous`` に変更します。

.. figure:: images/160-Algorithm-Blocks.png
   :align: center
   :width: 85%
   :alt: Algorithm

   HuskyLens Blocks Algorithm

Notice the default algorithm here is ``TAG_RECOGNITION``, which simply
detects any (common) AprilTags in the sensor’s field of view. This
recognition is unrelated to the FTC game CENTERSTAGE and its 10
AprilTags with metadata. Instead, this is a simple built-in, generic
function of HuskyLens, used here only to validate the sensor’s
operation.

**AprilTag** の認識とナビゲーションには、FTC チームは UVC ウェブカメラと FTC
:ref:`VisionPortal <apriltag/vision_portal/visionportal_overview/visionportal-overview:VisionPortal Overview>`
ソフトウェアからはるかに多くの価値を見出すかもしれません。FTC ロボットは、HuskyLens **と** USB ウェブカメラの両方を使用できます。

``Save OpMode`` をクリックし、**Driver Station** からこの **OpMode** を選択して実行します。開始矢印をタッチした後、HuskyLens を一般的な 36h11 ファミリーの任意の **AprilTag** に向けます。

.. figure:: images/210-AprilTag-double.png
   :align: center
   :width: 85%
   :alt: Uncategorized Apriltag

   未分類の AprilTag が検出されました

HuskyLens の小さな画面には、認識された **AprilTag** が薄い白いバウンディングボックスで囲まれて表示されます。

Here’s the corresponding DS Telemetry:
対応する DS **Telemetry** は次のとおりです。
.. figure:: images/220-DS-1-big-AprilTag.png
   :align: center
   :width: 85%
   :alt: DS AprilTag

   AprilTag Telemetry

データには以下が含まれます。 
データには以下が含まれます。

- 検出されたオブジェクト（「ブロック」と呼ばれる）の数
- オブジェクトの ID コード（正しくないか意味がない可能性があります）
- バウンディングボックスのサイズ（ピクセル単位）
- バウンディングボックスの中心位置（ピクセル単位）、(X, Y) の原点は左上
HuskyLens デバイスの画面は 320 x 240 ピクセルで、中心位置は
HuskyLens デバイスの画面は 320 x 240 ピクセルで、中心位置は (160, 120) です。
**Congratulations!** At this point, you have validated the HuskyLens
device, its connection to the REV Hub, and the Sample OpMode program.
**おめでとうございます！** この時点で、HuskyLens デバイス、REV Hub への接続、およびサンプル **OpMode** プログラムを検証しました。
------------------

Now you can test whether the HuskyLens can detect the AprilTag’s
position on the CENTERSTAGE Spike Marks. This is not a real game
scenario, since a Team Prop (Team Game Element) cannot use an AprilTag.
これで、HuskyLens が CENTERSTAGE Spike Marks 上の **AprilTag** の位置を検出できるかどうかをテストできます。チームプロップ（チームゲーム要素）は **AprilTag** を使用できないため、これは実際のゲームシナリオではありません。これは、ロボットが HuskyLens を向けて、単一のビューで 2 つまたは 3 つの Spike Marks を「見る」ことができるかどうかを確認するだけです。
   :width: 85%
   :alt: 3 Tags

   HuskyLens Viewing 3 Uncategorized Tags

ここでは、HuskyLens はマットから約 10 インチ
from the mat, near the middle of the foam tile before the Spike-Mark
tile. The view **does include** the middle of all three Spike Marks.

3 つすべての **AprilTag** が認識されました。

.. figure:: images/235-DS-3-AprilTag.png
   :align: center
   :width: 85%
   :alt: 3 Blocks

   Telemetry Showing 3 Blocks

これは、HuskyLens がトレーニングされた
object in one of various known positions – useful for the Autonomous
phase of the CENTERSTAGE game.

Single Color Training
---------------------

Soon you will try a different algorithm called ``COLOR_RECOGNITION``.
But first you need the HuskyLens to “learn” a single color, using its
built-in AI feature.

Choose any object, about 3 to 4 inches in size, that’s completely one
color – any color. Here we use a flat square beverage coaster (LEGO!),
with a uniform **red color**.

検出に使用する予定の位置と照明にこのオブジェクトを配置
for detection. This could be on a CENTERSTAGE Spike Mark, if available.

.. figure:: images/240-red-color-ID.png
   :align: center
   :width: 85%
   :alt: Red Color ID

   Red Color ID

In the above image, the trained color is shown as **``Color:ID1``** with
a rectangular Bounding Box. The following steps describe how to do this
training.

The **HuskyLens instructions** for learning a color are `posted
online <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336#target_19>`__.
You could try to follow those, or use the equivalent description here.
Some practice may be required!

On the top of the HuskyLens, the wheel at the left side is called the
**Function button** (actually a dial and button). At the right side is
the small **Learning button**.

Dial the Function button to the right or left until **“Color
Recognition”** is displayed at the bottom of the screen.

This is Step 1 only, under ``Operation and Setting`` of the HuskyLens
instructions. For now, do not try to “learn” more than one color with
Steps 2-4.

Point the plus-sign “+” icon in the center of the HuskyLens screen at
your object’s main color area. A white frame appears on the screen,
targeting the main color. Aim the HuskyLens so the white frame includes
only the target color.

This is Step 1 of ``Learning and Detection``. Next comes Step 2, Color
Learning.

With the main color framed, **long press** (press and hold) the small
**Learning button** (right side). A yellow frame is displayed on the
screen, indicating that HuskyLens is learning the color. During this
long press, move the HuskyLens while pointing at the color area, to let
HuskyLens learn the color from various distances and angles. Then,
release the Learning button to complete learning that color. Do not
press the button again (ignore the prompt); allow the 5-second time-out
to finish.

長押し学習期間は数秒間続くことができます。Learning ボタンを離した後、トレーニングをタイムアウトさせました。学習する色はもうありません。トレーニングが完了しました！

As shown above, the trained color will be shown on-screen as
**``Color:ID1``** with a rectangular Bounding Box. This “block” (of
color) will be reported in the Sample OpMode (next step).

If you want to do this over again, short-press the Learning button, then
short-press again to **Forget** the learned color(s). This will make the
plus-sign “+” icon appear again. Aim the plus-sign at the center of the
color area, and repeat the learning (long-press the Learning button).
Release and let the time-out finish.

This section showed how to train a single color. After completing this
tutorial, you may wish to train **two colors** (e.g. a Red shade and a
Blue shade). This is described near the end of this tutorial.

HuskyLens documentation refers to the color zone as a “block” of color.
This is not the same as a physical block or cube. HuskyLens uses the
same word “block” for recognitions.

公式警告に注意してください。

.. warning:: 
   “Color recognition is greatly affected by ambient light. Sometimes
   HuskyLens may misidentify similar colors. Please try to keep the
   ambient light unchanged.”

単一色の検出
----------------------

HuskyLens を色をトレーニングしたオブジェクトの 1 つ以上に向けます。

.. figure:: images/250-two-red.png
   :align: center
   :width: 85%
   :alt: Two Red Objects

   HuskyLens が 2 つの赤いオブジェクトを検出

上に示すように、HuskyLens は色付きオブジェクトを **``Color:ID1``** で認識してラベル付けする必要があります。ここでは、両方の赤いオブジェクトが識別されています（黄色の矢印）。

プログラミングソフトウェア（同じ **OpMode**）で、``COLOR_RECOGNITION`` という別のアルゴリズムを選択します。

.. figure:: images/245-Color-Algorithm-Blocks.png
   :align: center
   :width: 85%
   :alt: COLOR_RECOGNITION algorithm

   COLOR_RECOGNITION アルゴリズムの選択

Java サンプル **OpMode** で、アルゴリズムの選択を次のように変更します。

.. code:: java

   huskyLens.selectAlgorithm(HuskyLens.Algorithm.COLOR_RECOGNITION);

この **OpMode** を保存してから、**Driver Station** で選択して実行します。アクティブな構成に HuskyLens が含まれていることを確認してください。

.. figure:: images/260-DS-two-red.png
   :align: center
   :width: 85%
   :alt: DS Telemetry Two Objects

   DS Telemetry Two Objects

As shown above, the OpMode provides the size and location of the white
Bounding Boxes (called “blocks”). This is done in a **FOR loop**;
multiple recognitions are processed one at at time.

In the Java sample OpMode, **inside the FOR loop**, you could save or
evaluate **specific** info for the currently recognized Bounding Box:
``blocks[i].width``, ``blocks[i].height``, ``blocks[i].left``,
``blocks[i].top``, and (for the Box’s center) ``blocks[i].x`` and
``blocks[i].y``. The Color ID ``blocks[i].id`` is always 1 here, for
single-color detection. These values have Java type ``int``.

Even if your Team Prop’s color closely matches the color of the red or
blue Spike Mark, you could write OpMode code to reject the narrow shape
(aspect ratio) of an empty Spike Mark’s Bounding Box.

Here’s an example with a trained **blue object**:

.. figure:: images/270-two-blue-double.png
   :align: center
   :width: 85%
   :alt: Two Blue Objects

   HuskyLens 2 つの青いオブジェクト

両方の青いオブジェクトが **OpMode** によって認識されました。

.. figure:: images/280-DS-2-blue.png
   :align: center
   :width: 85%
   :alt: DS Two Blue Objects

   Telemetry for Two Blue Objects

Again, your code can evaluate the size and location of any provided
Bounding Box, to verify a “real” recognition of your object.

Competition Notes
-----------------

1. Team Prop
~~~~~~~~~~~~

Now you are ready to experiment with color recognition of an actual Team
Prop, also called a Team Game Element. Study the Competition Manual
and the `FTC Q&A <https://ftc-qa.firstinspires.org/>`__ for the Team
Prop requirements. Choose your shades of “red” and “blue” (see note
below), and follow the same steps as above.

2. 色
~~~~~~~~

上でトレーニングした**青いオブジェクト**は、青い Spike Mark と同じ青の色合いではありません。この違いにより、オブジェクトの色を明確かつ正確に認識する可能性が高まります。

このゲームでは、競技マニュアルは、Spike Marks の公式テープの色と比較して、チームプロップが異なる赤または青の色合いであることを特に許可していました。

3. 照明
~~~~~~~~~~~

HuskyLens のドキュメントは、周囲の照明がトレーニングされた色の認識に影響を与える可能性があるという警告を提供しています（上記を参照）。

For this reason, competition training should ideally be done with the
Team Prop (Team Game Element) on the Spike Mark, and the HuskyLens in
its planned match start position, “on-robot”.

また、トレーニングされた周囲の照明は、予想されるマッチ条件に類似している必要があります。これは、トーナメントまたはマッチのセットアップの一部として最終的な色トレーニングを実行することを示唆している可能性があります。練習すれば、数秒で完了できます。

4. プログラミング
~~~~~~~~~~~~~~

このサンプル **OpMode** では、メインループは DS 停止ボタンをタッチした場合にのみ終了します。競技では、チームは少なくとも 2 つの方法でこの**コードを変更**する必要があります。

-  重要な認識の場合、FOR ループ内でアクションを実行するか、重要な情報を保存します

-  基準に基づいてメインループを終了し、**OpMode** を続行します

例として、重要な認識が発生した場合、ブール変数 ``isPropDetected`` を ``true`` に設定することができます。

また、どのランダム化された Spike Mark（赤または青のテープストライプ）がチームプロップを保持しているかを評価して保存することもできます。

Regarding the main loop, it could end after the HuskyLens views all
three Spike Marks, or after your code provides a high-confidence result.
If the HuskyLens’ view includes more than one Spike Mark position,
perhaps the **Bounding Box** size(s) and location(s) could be useful.
Teams should consider how long to seek an acceptable recognition, and
what to do otherwise.

いずれの場合も、**OpMode** はメインループを終了し、保存された情報を使用して実行を続行する必要があります。 

Multi-Color Training
--------------------

After completing the above tutorial with a single trained color, you may
wish to train **two colors** (e.g. a Red shade and a Blue shade).

これにより、FTC トーナメント中に複数の色トレーニングセッションを行う必要がなくなります。単一色の場合、レッドアライアンスとして FTC マッチをプレイする前に赤色をトレーニングし、ブルーアライアンスとしてプレイする前に青色をトレーニングします。

マルチカラーでは、たとえば、レッドアライアンスの **Autonomous** **OpMode** は **``Color:ID1``** として赤を探し、ブルーアライアンスの **Autonomous** **OpMode** は **``Color:ID2``** として青を探すことができます。

複数の色を学習するための **HuskyLens の指示書**は`オンラインで公開されています <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336#target_19>`__。それらに従うか、ここで同等の説明を使用できます。繰り返しますが、練習が必要な場合があります！

注意：HuskyLens の上部にある左側のホイールは **Function ボタン**（実際にはダイヤルとボタン）と呼ばれます。右側には小さな **Learning ボタン**があります。

**Step 1.** Dial the Function button to the right or left until **“Color
Recognition”** is displayed at the bottom of the screen.

**Long press** (press and hold) the Function button to select Color
Recognition.

**Step 2.** This brings up the next menu, containing the choice “Learn
Multiple”. If needed, dial the Function button to highlight “Learn
Multiple”.

**Short press** (press and release) the Function button to select Learn
Multiple.

This brings up the OFF-ON slider bar for “Learn Multiple”. If needed,
dial the Function Button to move the blue square to the **right side**
of the blue slider bar. See yellow arrow:

.. figure:: images/340-Husky-LearnMultiple.png
   :align: center
   :width: 85%
   :alt: Learn Multiple

   HuskyLens - Learn Multiple

**Short press** the Function button to set “Learn Multiple” to **ON**.

**Step 3.** Dial the Function button to the left, and **short press** to
select “Save & Return”.

At the screen prompt “Do you want to save the parameters?” or “Do you
save data?”, **short press** the Function button to select “Yes”. This
saves the mode (again) as “Learn Multiple” and exits the settings menu.

Now ready for learning!

**Step 4.** As before, point the plus-sign “+” icon in the center of the
HuskyLens screen at your object’s main color area. A **white frame**
appears on the screen, targeting the main color. Aim the HuskyLens so
the white frame includes only the target color.

メイン色がフレームに収められた状態で、小さな **Learning ボタン**（右側）を**長押し**（押し続ける）します。画面に**黄色のフレーム**が表示され、HuskyLens が色を学習していることを示します。

この長押し中に、色領域を指しながら HuskyLens を動かして、HuskyLens にさまざまな距離と角度から色を学習させます。次に、Learning ボタンを離して、その色の学習を完了します。

長押し学習期間は数秒間続くことができます。Learning ボタンを離すと、**``Color:ID1``** がトレーニングされ、そのラベルが画面に表示されます。簡単です！

.. figure:: images/240-red-color-ID.png
   :align: center
   :width: 85%
   :alt: RED Color 1 Trained

   HuskyLens - RED（Color 1）トレーニング済み

**ステップ 5.** 画面に表示されたら、**短押し**Learning ボタンをもう一度押します（5 秒のタイムアウト前）。これにより、次の色を学習する準備が整います。

**ステップ 6.** レンズを 2 番目の色に向け、前のステップ 4 を繰り返します。つまり、Learning ボタンを**長押し**し、狙いを定めて移動し、**離して**その色の学習を完了します。

これで **``Color:ID2``** がトレーニングされ、そのラベルが画面に表示されます。

**Step 7.** As prompted, **short press** the “other” button, the
Function button. Or, allow the 5-second time-out to complete. In either
case, this completes the multi-color training. All done!

.. figure:: images/360-two-colors.png
   :align: center
   :width: 85%
   :alt: Two Colors Trained

   HuskyLens - 2 つの色がトレーニング済み（ID1 と ID2）

これをすべて**やり直したい**場合は、Learning ボタンを短押しし、次に（プロンプトが表示されたら）もう一度短押しして、**学習したすべての色を``忘れます``**。

This makes the plus-sign “+” icon appear again. Repeat the above, from
Step 4, to train colors again.

マルチカラー検出
---------------------

たとえば、**OpMode** コードが **``Color:ID2``** を読み取るには、アルゴリズムを ``COLOR_RECOGNITION`` に設定する必要があり、フィールド ``HuskyLens.Block.id`` は **値 2** になります。これは、上で使用したサンプル **OpMode** の **Telemetry** 部分で確認できます。

.. figure:: images/400-Blocks-Color-ID.png
   :align: center
   :width: 85%
   :alt: Color Detection Blocks

   Adding Telemetry for Colors

Here’s the DS Telemetry from the Sample OpMode used above for single
color, **with no coding changes**:

.. figure:: images/420-2-color-telemetry.png
   :align: center
   :width: 85%
   :alt: 2 Color Telemetry

   両方の色を示す Telemetry の例

これで、ID コード 1 と 2 を持つ、トレーニングおよび認識された 2 つの色があります。上の黄色の矢印を参照してください。

These two lines of Telemetry are generated in different cycles of the
same FOR Loop. They display together, since the ``Telemetry.update``
Block appears **after** the FOR Loop has completed all of its cycles.
Namely, the FOR Loop has processed each HuskyLens “color block” in the
``List`` of HuskyLens “blocks”.

Java サンプル **OpMode** で、**FOR ループ内**にこれらの行を追加します。

.. code:: java

   int thisColorID = blocks[i].id;                      // save the current recognition's Color ID
   telemetry.addData("This Color ID", thisColorID);     // display that Color ID

``.id`` に加えて、現在認識されているバウンディングボックスには、他の Java フィールドが使用できます：``.width``、``.height``、``.left``、``.top``、および ``.x`` と ``.y``（中心位置）。

色 ID 番号は**トレーニングの順序で**割り当てられます。後でこれらの番号を変更することはできないため、トレーニングと **OpMode** コーディングが互いに一致するように計画してください。

.. tip::
   **Advanced tip:** If your color recognition is heavily affected by ambient
   lighting, you could try training your object in various lighting conditions
   **as different HuskyLens colors**. Namely, the Red-shade Team Prop could be
   trained as **``Color:ID1``** in bright light, and trained as
   **``Color:ID2``** in dim light or shadow. Your OpMode could accept
   **either** Color ID (1 or 2) as “Red”. Likewise, Blue shades could have
   Color IDs 3 and 4.

オブジェクトトレーニング
---------------

このチュートリアルは、HuskyLens の**色トレーニング**で終了します。これで、HuskyLens の操作、トレーニング、および FTC プログラミングの基本的な手順に精通しました。

You are encouraged to proceed with training the HuskyLens to recognize
an **actual object**. This could be one of its 20 pre-trained models
(“Object Recognition”) or a **custom model or image** that you train
(“Object Classification”). In each case, follow a process similar to
color training, using the `HuskyLens
documentation <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336>`__.

HuskyLens の**オブジェクト認識**は、色認識よりも信頼性の高い結果とともに、AI と機械学習のプロセスに対するより多くの（教育的な）露出を提供することがわかるかもしれません。

今シーズンの幸運を祈ります！

============

質問、コメント、訂正は westsiderobotics@verizon.net まで
