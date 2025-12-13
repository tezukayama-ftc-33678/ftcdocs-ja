
*FIRST* Tech Challenge向け **HuskyLens** 入門
==============================================

はじめに
-------------

このチュートリアルは、*FIRST* Tech Challenge で
`HuskyLens <https://www.dfrobot.com/product-1922.html>`__ を活用する方法を、すでにその可能性を探求することを決めたチームの皆さん向けにご紹介します。

.. figure:: images/020-HuskyLens-dual.png
   :align: center
   :width: 85%
   :alt: HuskyLens

   DFRobot HuskyLens

この**ビジョンセンサー** の基本的なサポートは、2023年9月の CENTERSTAGE ロボットゲーム開始時に **FTC SDK** バージョン9.0 で追加されました。

**HuskyLens** は、** オンボードプログラミング** によって AI 支援の学習、画像処理、認識を行います。**REV Control Hub** または **REV Expansion Hub** の **I2C センサーポート** に接続します。

**HuskyLens** は **USB ウェブカメラ** ではなく、FTC の
:ref:`VisionPortal <apriltag/vision_portal/visionportal_overview/visionportal-overview:VisionPortal Overview>`
ソフトウェアも使用しません。


電気的な接続
---------------------

**HuskyLens** を **REV Control Hub** または **Expansion Hub** の I2C ポートに接続するには、** カスタムアダプターケーブル** が必要です。**HuskyLens** コネクタの4本のワイヤ／ピンは、REV Hub の4ピンと順番や位置が異なります。

3本のワイヤは、REV センサーケーブルのワイヤと** 同じ色** です。カスタムケーブルでは、** 赤は赤** 、** 黒は黒** 、** 青は青** で接続してください。残る **HuskyLens** の** 緑色のワイヤ** は、REV の** 白色のワイヤ** に接続します。とてもシンプルです！

このチュートリアルでは、

- 既存ケーブルのピン順変更、または
- 新規ケーブルの製作方法（はんだ付け、圧着コネクタ、レバーナットなど）
については扱いません。


**FTC 競技マニュアル** ではこの作業が認められていますが、チームは競技シーズンを通じて高品質なケーブルを確保してください。

.. figure:: images/060-adapter.png
   :align: center
   :width: 85%
   :alt: Wiring an Adapter

   image credit: @texasdiaz


配線方法が正しいか確認したい場合は、
`HuskyLens 公式ドキュメント <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336#target_3>`__
や `REV Hub 公式ドキュメント <https://docs.revrobotics.com/duo-control/sensors/i2c#wiring>`__
を参照してください。以下の「ピン配置」情報が得られます：

- HuskyLens ** 緑** ワイヤ 1（「T」）SDA（データ） == REV Hub ** 白** ワイヤ 3「SDA」（データ）
- HuskyLens ** 青** ワイヤ 2（「R」）SCL（クロック） == REV Hub ** 青** ワイヤ 4「SCL」（クロック）
- HuskyLens ** 黒** ワイヤ 3（「-」）GND（グラウンド） == REV Hub ** 黒** ワイヤ 1「GND」（グラウンド）
- HuskyLens ** 赤** ワイヤ 4（「+」）VCC（+3.3-5VDC） == REV Hub ** 赤** ワイヤ 2「3.3V」（Vcc）

.. figure:: images/070-ports.png
   :align: center
   :width: 85%
   :alt: Ports

   image credit: @texasdiaz


構成方法
--------------

新しいアダプターケーブルを使い、**HuskyLens** を **REV Hub** の I2C ポートに接続します。I2C 接続は **Bus 1, 2, 3** のいずれかを推奨します（データトラフィックの過負荷を避けるため）。

ラベル「0」は I2C Bus 0 で、通常は Port 0 に** 内蔵 IMU** が接続されています。I2C Bus には複数の I2C ポートがあり、トラフィックを共有します。

**Driver Station** で、三点メニューから ``Configure Robot`` を選択します。

既存の（正しい）構成を編集するか、``New`` をタップします。``Scan`` をタップし、Portal レベルを経由して **HuskyLens** が接続された ``Expansion Hub`` または ``Control Hub`` を選択します。

**HuskyLens** が接続されている Bus 番号（例：``I2C Bus 3`` ）を選択します。

.. figure:: images/120-DS-config.png
   :align: center
   :width: 85%
   :alt: DS Config

   Driver Station Config


``Add`` をタップし、Port 0（または最初の空きポート）のドロップダウンリストから「HuskyLens」を選択します。デバイス名は「huskylens」と入力してください（サンプル **OpMode** で期待される名前です）。

``Done`` を数回タップし、``Save`` で構成を保存・名前変更します。DS の「Back」矢印でホーム画面に戻ります。

新しい構成が画面上でアクティブ構成として表示されていることを確認してください。


サンプル **OpMode**
~~~~~~~~~~~~~~~~~~~

プログラミング用コンピューターを **Robot Controller** に接続し、プログラミングソフトウェアを開きます。このチュートリアルでは **FTC Blocks** を使用します。

.. note::
   **OnBot Java** や **Android Studio** ユーザーも同じロジックで簡単に追従できます（Java サンプル **OpMode** はコメントも充実しています）。

**FTC Blocks** で、「SensorHuskyLens」というサンプルを使って新しい **OpMode** を作成します。

.. figure:: images/140-Sample-Blocks.png
   :align: center
   :width: 85%
   :alt: Blocks Sample

   HuskyLens Blocks Sample

このサンプルでは、**OpMode** のタイプを ``TeleOp`` から ``Autonomous`` に変更してください（ゲームパッドは使用しません）。


.. figure:: images/160-Algorithm-Blocks.png
   :align: center
   :width: 85%
   :alt: Algorithm

   HuskyLens Blocks Algorithm


デフォルトのアルゴリズムは ``TAG_RECOGNITION`` で、センサーの視野内にある（一般的な）**AprilTag** を検出します。この認識は FTC ゲーム CENTERSTAGE の10個の **AprilTag** （メタデータ付き）とは関係ありません。ここでは、**HuskyLens** の動作確認のためのシンプルな内蔵機能です。

**AprilTag** の認識やナビゲーションには、UVC ウェブカメラと FTC の
:ref:`VisionPortal <apriltag/vision_portal/visionportal_overview/visionportal-overview:VisionPortal Overview>`
ソフトウェアの方が有用な場合があります。FTC ロボットは **HuskyLens** と USB ウェブカメラの両方を使うことができます。

``Save OpMode`` をクリックし、Driver Station からこの **OpMode** を選択して実行します。Start 矢印をタップしたら、**HuskyLens** を一般的な 36h11 ファミリーの **AprilTag** に向けてください。


.. figure:: images/210-AprilTag-double.png
   :align: center
   :width: 85%
   :alt: Uncategorized Apriltag

   Uncategorized AprilTag Detected


**HuskyLens** の小さな画面には、認識した **AprilTag** が細い白いバウンディングボックスで囲まれて表示されます。

対応する DS テレメトリーは以下の通りです：


.. figure:: images/220-DS-1-big-AprilTag.png
   :align: center
   :width: 85%
   :alt: DS AprilTag

   AprilTag Telemetry


データには以下が含まれます：

- 検出されたオブジェクト（「ブロック」と呼ばれる）の数
- オブジェクトの ID コード（正確でない場合や意味がない場合もあります）
- バウンディングボックスのサイズ（ピクセル単位）
- バウンディングボックスの中心位置（ピクセル単位、原点は左上）

**HuskyLens** の画面サイズは 320 x 240 ピクセル、中心は (160, 120) です。

** おめでとうございます！** これで **HuskyLens** デバイス、REV Hub への接続、サンプル **OpMode** の動作確認ができました。


**AprilTag** 検出
------------------

次に、**HuskyLens** が CENTERSTAGE の Spike Mark 上の **AprilTag** の位置を検出できるかテストします。これは実際のゲームシナリオではありません（**Team Prop**＝チームゲームエレメントは **AprilTag** を使えません）。ここでは、ロボットが **HuskyLens** で2～3個の Spike Mark を一度に「見る」ことができるかを検証します。


.. figure:: images/230-3-tags-double.png
   :align: center
   :width: 85%
   :alt: 3 Tags

   HuskyLens Viewing 3 Uncategorized Tags


この例では、**HuskyLens** をマットから約10インチ離れた、Spike Mark タイル手前のフォームタイル中央付近に配置しました。視野には3つの Spike Mark の中央がすべて含まれています。

3つの **AprilTag** がすべて認識されました：


.. figure:: images/235-DS-3-AprilTag.png
   :align: center
   :width: 85%
   :alt: 3 Blocks

   Telemetry Showing 3 Blocks


これは、**HuskyLens** が訓練済みオブジェクトを既知の複数位置のいずれかで認識できる可能性を示しています。CENTERSTAGE ゲームの **Autonomous** フェーズで有用です。


単色の学習
---------------------

次は ``COLOR_RECOGNITION`` という別のアルゴリズムを試しますが、その前に **HuskyLens** の内蔵 AI 機能で「単色」を学習させます。


3～4インチ程度の、完全に一色の物体を用意してください（色は何でも構いません）。ここでは、均一な** 赤色** の平らな四角いコースター（LEGO!）を使います。


検出に使う予定の位置や照明環境でこの物体を配置します。CENTERSTAGE の Spike Mark 上でも構いません。


.. figure:: images/240-red-color-ID.png
   :align: center
   :width: 85%
   :alt: Red Color ID

   Red Color ID


上記画像では、学習した色が **``Color:ID1``** として長方形のバウンディングボックスで表示されています。以下の手順で色の学習を行います。


**HuskyLens** の色学習手順は `公式オンライン <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336#target_19>`__ に掲載されています。そちらを参照するか、同等の説明を本チュートリアルでご確認ください。少し練習が必要かもしれません。


**HuskyLens** 上部の左側のダイヤルは「**Function ボタン**」（ダイヤル兼ボタン）、右側の小さいボタンは「**Learning ボタン**」です。


Function ボタンを左右に回し、画面下部に「Color Recognition」が表示されるまで操作します。


これは公式手順の ``Operation and Setting`` のステップ1です。今はステップ2～4で複数色を学習しようとしないでください。


**HuskyLens** 画面中央の「+」アイコンを物体の主な色領域に合わせます。白い枠が表示され、主色をターゲットします。枠内にターゲット色だけが入るように狙いましょう。


これは ``Learning and Detection`` のステップ1です。次はステップ2、色の学習です。


主色が枠内に入ったら、右側の小さい **Learning ボタン** を** 長押し** します。画面に黄色い枠が表示され、**HuskyLens** が色を学習中であることを示します。長押し中は、色領域を指しながら **HuskyLens** を動かし、様々な距離や角度から色を学習させます。終わったら Learning ボタンを離して学習を完了します。ボタンを再度押さず（プロンプトは無視）、5秒のタイムアウトを待ちます。


長押し学習は数秒で完了します。Learning ボタンを離した後、タイムアウトで学習終了となります。これで色の学習は完了です！


上記のように、学習した色は画面上で **``Color:ID1``** として長方形のバウンディングボックスで表示されます。この「ブロック」（色領域）は次のサンプル **OpMode** で報告されます。


再度学習したい場合は、Learning ボタンを短押し→もう一度短押しで学習済み色を** 忘却** します。再び「+」アイコンが表示されるので、中心に合わせて長押しで学習を繰り返し、タイムアウトまで待ちます。


このセクションでは単色の学習方法を説明しました。チュートリアル完了後、**2色** （例：赤系と青系）を学習する方法も後半で解説します。


**HuskyLens** 公式ドキュメントでは色領域を「ブロック」と呼びますが、物理的なブロックやキューブとは異なります。認識領域も「ブロック」と呼ばれます。


公式の注意事項：

.. warning:: 
   「色認識は周囲の照明に大きく影響されます。**HuskyLens** は似た色を誤認識する場合があります。できるだけ照明環境を一定に保ってください。」


単色の検出
----------------------

**HuskyLens** を色学習済みの物体に向けます。


.. figure:: images/250-two-red.png
   :align: center
   :width: 85%
   :alt: Two Red Objects

   HuskyLens Detecting Two Red Objects


上記のように、**HuskyLens** は色付き物体を **``Color:ID1``** として認識・ラベル付けします（ここでは赤色の物体2つが黄色矢印で示されています）。


プログラミングソフトウェア（同じ **OpMode** ）で、アルゴリズムを ``COLOR_RECOGNITION`` に変更します：


.. figure:: images/245-Color-Algorithm-Blocks.png
   :align: center
   :width: 85%
   :alt: COLOR_RECOGNITION algorithm

   Selecting COLOR_RECOGNITION algorithm


Java サンプル **OpMode** では、アルゴリズム選択を以下のように変更します：

.. code:: java

   huskyLens.selectAlgorithm(HuskyLens.Algorithm.COLOR_RECOGNITION);


この **OpMode** を保存し、Driver Station で選択・実行します。アクティブ構成に **HuskyLens** が含まれていることを確認してください。


.. figure:: images/260-DS-two-red.png
   :align: center
   :width: 85%
   :alt: DS Telemetry Two Objects

   DS Telemetry Two Objects


上記のように、**OpMode** では白いバウンディングボックス（「ブロック」）のサイズと位置が表示されます。これは **FOR ループ** で処理され、複数認識が1つずつ処理されます。


Java サンプル **OpMode** の **FOR ループ内** では、現在認識されたバウンディングボックスの詳細情報（``blocks[i].width`` 、``blocks[i].height`` 、``blocks[i].left`` 、``blocks[i].top`` 、中心座標の ``blocks[i].x`` 、``blocks[i].y`` ）を保存・評価できます。色 ID（``blocks[i].id`` ）は単色検出の場合常に1です。これらは Java の ``int`` 型です。


**Team Prop** の色が Spike Mark の赤や青と近い場合でも、空の Spike Mark のバウンディングボックスの形状（アスペクト比）を判定して除外する **OpMode** コードを書くことができます。


以下は学習済み** 青色物体** の例です：


.. figure:: images/270-two-blue-double.png
   :align: center
   :width: 85%
   :alt: Two Blue Objects

   HuskyLens Two Blue Objects


両方の青色物体が **OpMode** で認識されました：

.. figure:: images/280-DS-2-blue.png
   :align: center
   :width: 85%
   :alt: DS Two Blue Objects

   Telemetry for Two Blue Objects


同様に、コードでバウンディングボックスのサイズや位置を評価し、物体の「本物の」認識かどうかを判定できます。


競技に関する注意事項
--------------------

1. **Team Prop**
~~~~~~~~~~~~~~~~

実際の **Team Prop** （チームゲームエレメント）の色認識実験が可能です。**Competition Manual** や `FTC Q&A <https://ftc-qa.firstinspires.org/>`__ で **Team Prop** の要件を確認し、「赤」「青」の色合いを選び、上記と同じ手順で学習・認識を行ってください。


2. 色
~~~~~~~~

上記の学習済み** 青色物体** は Spike Mark の青とは異なる色合いです。この違いにより、物体色の明確かつ正確な認識の可能性が高まります。

このゲームでは、**Competition Manual** で **Team Prop** の色が Spike Mark の公式テープ色と異なる赤・青でも認められています。


3. 照明
~~~~~~~~~~~

**HuskyLens** 公式ドキュメント（上記参照）では、周囲の照明が学習済み色の認識に影響する旨の注意があります。

そのため、競技用の学習は、**Team Prop** を Spike Mark 上に置き、**HuskyLens** を試合開始予定位置（ロボット上）に設置して行うのが理想です。

また、学習時の照明環境は試合本番に近いものにしてください。大会や試合準備の一環として最終色学習を行うのも良いでしょう。慣れれば数秒で完了します。


4. プログラミング
~~~~~~~~~~~~~~~~~

このサンプル **OpMode** では、メインループは DS の Stop ボタンを押すまで終了しません。競技用には、少なくとも以下2点で** コードを修正** してください：

- 重要な認識があった場合、FOR ループ内でアクションを起こすか重要情報を保存する
- 独自の基準でメインループを終了し、**OpMode** を継続する

例として、重要な認識があれば Boolean 変数 ``isPropDetected`` を ``true`` に設定するなどが考えられます。

また、どの Spike Mark（赤・青テープ）に **Team Prop** があるかを判定・保存することもできます。

メインループは、**HuskyLens** が3つの Spike Mark をすべて見終えた時や、コードが高信頼度の結果を出した時に終了しても良いでしょう。複数 Spike Mark が視野に入る場合は、** バウンディングボックス** のサイズや位置が有用です。認識にかける時間や、認識できなかった場合の対応も検討してください。

いずれの場合も、**OpMode** はメインループを抜けて、保存した情報を使って処理を続行します。


複数色の学習
--------------------

上記のチュートリアルで単色の学習が完了したら、**2色** （例：赤系と青系）を学習することもできます。

これにより、FTC トーナメント中に複数回色学習を行う必要がなくなります。単色の場合は、Red Alliance の試合前に赤を、Blue Alliance の試合前に青を学習します。

複数色の場合、Red Alliance の **Autonomous OpMode** では **``Color:ID1``** を、Blue Alliance の **Autonomous OpMode** では **``Color:ID2``** を探すことができます。

複数色学習の **HuskyLens** 公式手順は `オンライン <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336#target_19>`__ に掲載されています。そちらを参照するか、本チュートリアルの説明を参考にしてください。こちらも少し練習が必要です。

再確認：**HuskyLens** 上部の左側のダイヤルは「**Function ボタン**」（ダイヤル兼ボタン）、右側の小さいボタンは「**Learning ボタン**」です。

** ステップ1.** Function ボタンを左右に回し、画面下部に「Color Recognition」が表示されるまで操作します。

**Function ボタンを長押し** して Color Recognition を選択します。

** ステップ2.** 次のメニューで「Learn Multiple」を選択します。必要に応じて Function ボタンを回し、「Learn Multiple」をハイライトします。

**Function ボタンを短押し** して「Learn Multiple」を選択します。

「Learn Multiple」の ON/OFF スライダーが表示されます。必要に応じて Function ボタンを回し、青い四角をスライダーの** 右側** に移動します（黄色矢印参照）：

.. figure:: images/340-Husky-LearnMultiple.png
   :align: center
   :width: 85%
   :alt: Learn Multiple

   HuskyLens - Learn Multiple

**Function ボタンを短押し** して「Learn Multiple」を **ON** にします。

** ステップ3.** Function ボタンを左に回し、「Save & Return」を短押しで選択します。

画面の「Do you want to save the parameters?」や「Do you save data?」のプロンプトで、Function ボタンを短押しして「Yes」を選択します。これで「Learn Multiple」モードが保存され、設定メニューを終了します。

これで学習準備完了です！

** ステップ4.** 先ほどと同様に、**HuskyLens** 画面中央の「+」アイコンを物体の主な色領域に合わせます。** 白い枠** が表示され、主色をターゲットします。枠内にターゲット色だけが入るように狙いましょう。

主色が枠内に入ったら、右側の小さい **Learning ボタン** を** 長押し** します。** 黄色い枠** が表示され、**HuskyLens** が色を学習中であることを示します。

長押し中は、色領域を指しながら **HuskyLens** を動かし、様々な距離や角度から色を学習させます。終わったら Learning ボタンを離して学習を完了します。

長押し学習は数秒で完了します。Learning ボタンを離した後、**``Color:ID1``** が学習され、ラベルが画面に表示されます。簡単です！

.. figure:: images/240-red-color-ID.png
   :align: center
   :width: 85%
   :alt: RED Color 1 Trained

   HuskyLens - RED (Color 1) Trained

** ステップ5.** 画面の指示に従い、Learning ボタンをもう一度短押しします（5秒タイムアウト前）。これで次の色の学習準備ができます。

** ステップ6.** レンズを2色目に向け、前述のステップ4を繰り返します。Learning ボタンを長押し、狙い・動かし、離して学習を完了します。


これで **``Color:ID2``** も学習され、ラベルが画面に表示されます。

** ステップ7.** 画面の指示に従い、もう一方のボタン（Function ボタン）を短押しするか、5秒のタイムアウトを待ちます。どちらでも複数色学習が完了します。お疲れさまでした！

.. figure:: images/360-two-colors.png
   :align: center
   :width: 85%
   :alt: Two Colors Trained

   HuskyLens - Two Colors Trained (ID1 and ID2)

すべてをやり直したい場合は、Learning ボタンを短押し→画面の指示に従いもう一度短押しで、学習済み色をすべて** 忘却** します。

再び「+」アイコンが表示されるので、ステップ4から繰り返して色を再学習できます。


複数色の検出
---------------------

例えば **``Color:ID2``** を **OpMode** コードで読み取るには、アルゴリズムを ``COLOR_RECOGNITION`` に設定し、``HuskyLens.Block.id`` フィールドが「2」になります。これは上記サンプル **OpMode** のテレメトリー部分で確認できます。

.. figure:: images/400-Blocks-Color-ID.png
   :align: center
   :width: 85%
   :alt: Color Detection Blocks

   Adding Telemetry for Colors

上記サンプル **OpMode** （単色用、コード変更なし）での DS テレメトリー例：

.. figure:: images/420-2-color-telemetry.png
   :align: center
   :width: 85%
   :alt: 2 Color Telemetry

   Example Telemetry showing Both Colors

IDコード1と2の2色が学習・認識されています（黄色矢印参照）。

これら2行のテレメトリーは、同じ FOR ループの異なるサイクルで生成されます。``Telemetry.update`` ブロックが FOR ループ終了後に実行されるため、両方が同時に表示されます。FOR ループは HuskyLens の「color block」リストをすべて処理します。

Java サンプル **OpMode** では、FOR ループ内に以下の行を追加します：

.. code:: java

   int thisColorID = blocks[i].id;                      // 現在認識した色IDを保存
   telemetry.addData("This Color ID", thisColorID);     // 色IDを表示

``.id`` 以外にも、現在認識したバウンディングボックスの ``.width`` 、``.height`` 、``.left`` 、``.top`` 、``.x`` 、``.y``（中心座標）などのフィールドが利用できます。

色ID番号は** 学習順** で割り当てられます。後から番号変更はできないので、学習順と **OpMode** コードの対応を計画してください。

.. tip::
   ** 応用ヒント：** 色認識が照明環境に大きく左右される場合、異なる照明条件ごとに別の HuskyLens 色として学習する方法もあります。例えば、赤系 Team Prop を明るい環境で **``Color:ID1``** 、暗い環境や影で **``Color:ID2``** として学習し、**OpMode** でどちらのIDも「赤」として扱うことができます。青系も同様にID3・ID4など複数登録可能です。


オブジェクト学習
~~~~~~~~~~~~~~~~

このチュートリアルは **HuskyLens** の「色学習」で終了です。これで **HuskyLens** の基本操作・学習・FTC プログラミング手順を習得できました。

今後は、**HuskyLens** で「実際の物体」を認識する学習にも挑戦してみてください。20種類のプリセットモデル（「Object Recognition」）や、独自に学習したモデル・画像（「Object Classification」）も利用できます。いずれも色学習と同様の手順で、`HuskyLens 公式ドキュメント <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336>`__ を参考にしてください。

**HuskyLens** の「物体認識」は、AI・機械学習の教育的な体験や、色認識よりも高い信頼性を得られる場合があります。

皆さんの FTC シーズンの成功を祈っています！

============

ご質問・ご意見・修正依頼は westsiderobotics@verizon.net までお寄せください。
