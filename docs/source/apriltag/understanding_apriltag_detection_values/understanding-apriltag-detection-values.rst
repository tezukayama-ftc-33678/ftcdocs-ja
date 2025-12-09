AprilTag 検出値の理解
======================

*最終更新日: 2023年7月5日*

はじめに
--------

新しい SDK ビジョン処理システムによって AprilTag が検出されると、コアコードは、しばしば簡単には解釈できない生データのコレクションを返します。ただし、データはより使いやすくするために、馴染みのある参照フレームにさらに変換できます。

In the *FIRST* Tech Challenge SDK, the AprilTag API will present the Team
OpMode with a collection of translation and rotation values, called *ftcPose*,
that represent the Tag’s position in 3D space.

To understand how to interpret these values, it’s easier to consider a simpler
2D scenario where the vertical component is ignored. This is what is described
below.

以下の**図 1** は、考えられる 2D シナリオの 1 つを表しています。

.. figure:: images/figure1.jpg
   :width: 40%
   :alt: Figure 1
   :align: center

   図 1: AprilTag シナリオの上面図

This diagram looks down on the Camera and AprilTag from above. The camera’s
“forward” direction is identified by a dashed line drawn straight out from the
camera.

AprilTag 画像は図の左上に示されています。タグはカメラの前方 100 単位、左側 36.4 単位の位置にあります（前方視野に対して直角に測定）。

The AprilTag is also rotated 5 degrees counterclockwise from a normal “face on”
orientation.

考えられる検出シナリオの 1 つを明確に理解したので、SDK によって *ftcPose* として返されるさまざまな値の意味を見てみましょう。

**図 2** は、図 1 に示されているカメラ/ターゲットシナリオに関連する測定値を示しています。

.. figure:: images/figure2.jpg
   :width: 40%
   :alt: Figure 2
   :align: center

   図 2: シナリオに関連する測定値

Since this is a simple 2D diagram, the vertical “Z” (up) axis is being
ignored, so it is not shown here.

緑色の X 軸値は、タグへの横方向のオフセットを表します。この値は負（カメラ中心の左側）であることに注意してください。

赤色の Y 軸値は、タグへの前方距離を表します。

シアン色の Yaw 値は、Z 軸を中心としたタグの回転を表します。反時計回りの回転は正と見なされます。Yaw 値がゼロの場合、タグ画像がカメラの面と平行であることを意味することに注意してください。

.. note:: 
   豆知識: カメラが前方を向いている場合、X、Y、Z 軸はロボット座標系と一致しています。

X 軸と Y 軸の値から 3 つの追加パラメーターが導出されます。これらは、*Range*（ターゲットの中心までの直接距離）、*Bearing*（カメラがターゲットを直接指すために回転する必要がある度数）、および *Elevation*（カメラがタグの中心に向けて上に傾ける必要がある度数）です。ターゲット Bearing は同じ正の反時計回りの向きを持つことに注意してください。

実際のデータの調査
------------------

To illustrate this process, consider some real-world tags. The
data that follows is from a pair of tags printed on a card. The
left-most tags has an identical setup as described above. In Figure 3
the protractor origin is positioned directly in front of the camera, at
a distance of 25 inches. Both tags are to the left of the camera
centerline, and both are rotated +5 degrees. The left tag is 6.6” from
the centerline, and the right tag is 1.5” from the centerline. The
camera is located 6” inches above the center of the targets, looking out
horizontally (parallel to the ground).

.. figure:: images/apriltag_setup.jpg
   :width: 80%
   :alt: Tag Setup
   :align: center

   図 3: テスト用のサンプルタグセットアップ

The AprilTag video preview image from the Camera Stream preview is shown below.
The left tag has an ID of 0 and the right tag has an ID of 1. This video is
being captured by a Logitech C920 Pro HD webcam, running at 648x480 resolution.
In this mode the camera has Field-Of-View (FOV) of 60 degrees. The physical
tags are 3.4” square.

.. figure:: images/two_tags.jpg
   :width: 80%
   :alt: preview image
   :align: center

   図 4: 2 つの検出された AprilTag を示すカメラプレビュー

両方のタグが画像の左下隅にあることに注意してください。画像の中心は、カメラが向いている場所に対応しており、分度器の中心にあり、タグの上部の真上にあります。

Based on this setup, let’s review the data returned by the
“ConceptAprilTag.java” sample OpMode.

.. warning:: 
   このドキュメントの作成以降、ConceptAprilTag.java サンプルで使用されるタグが変更されました。したがって、この例を再現するには、Tag0 と Tag1 の代わりに適切なタグを使用する必要があります。

.. figure:: images/apriltag_telemetry.jpg
   :width: 50%
   :alt: telemetry
   :align: center

   図 5: AprilTag OpMode で表示される値

The values for the two AprilTags are listed as “ID0 Nemo”, and “ID1
Jonah”. These are the names assigned when adding the tags to the Tag
Library.

**OpMode** は、**図 2** に示されているパラメーターに対応する値を表示します。XYZ 行は、3 つの軸の移動値（X、Y、Z）をインチ単位で示します。PRY 行は、これらの軸を中心とした対応する回転（Pitch、Roll、Yaw）を度単位で示します。RBE 行は、ターゲットの Range（インチ単位）、Bearing、および Elevation（度単位）を示します。Elevation の角度は、カメラとタグの高さの違いから生じます。

*観察すべきいくつかの項目:*

-  Both Y values are about 25”, but the Y value for Tag 1 is slightly
   larger because it is behind the protractor base line.

-  The X values for Tag 0 and 1 correspond to the offset distances
   described earlier (-6.6” and -1.5”)

-  両方のタグは約 5 度の Yaw を示していますが、これは他の向き要因によって 1 ～ 2 度変化する可能性があります。

-  両方のターゲットへの Range はほぼ等しいですが、Tag 0 の Bearing は左側への変位により はるかに大きくなっています。

-  Both targets show the same negative Z value of -5.7, which is
   consistent with them being centered about 6” below the height of the
   camera.

-  Each tag also has an “Elevation” of about -12.6 degrees, which is a
   downward viewing angle to the center of each tag.

このデータの使用方法
--------------------

AprilTag 位置データを使用する方法はいくつかありますが、ここでは 2 つの基本的な方法を紹介します。

1. ターゲットに向けてポイントする（タンクドライブ）。

   AprilTag を使用して、射撃する必要があるターゲットの位置をマークしている場合、関心のある 2 つの主要なプロパティは、Tag Range と Tag Bearing です。Tag Bearing は、タグを直接指すために回転する必要がある度数を示し、Tag Range は、射撃する必要がある距離を示します。単純な差動（タンク）ドライブでも、これら 2 つのパラメーターを使用すると、ターゲットに向かって回転し、正しい範囲まで移動する（または範囲に基づいて射撃力を調整する）ことができます。

   A simple proportional controller could take the Tag Bearing, multiply
   it by a suitable gain and then use it in place of the turning
   joystick to turn the robot towards the target. Likewise, you could
   subtract the desired shooting range from the current Tag Range and
   use the result to control the robot’s forward speed.

   このアプローチは、ターゲットの正面に対して正方形に配置されることを保証するものではなく、単にそれに向かっていることを保証するだけであることに注意してください。正方形に配置するには、次のアプローチに示すように、Yaw 角度を考慮する必要があります。 

   詳細については、SDK サンプル: RobotAutoDriveToAprilTagTank.java を参照してください。

2. ターゲットに正面から接近する（オムニドライブ）。

   If an AprilTag is being used to mark the location of something that
   must be approached squarely from the front, then it’s important to
   consider the Tag Yaw value. This is a direct indication of how far
   off (in degrees) the camera is from the tag image’s centerline. This
   is related to, but not the same as the Tag Bearing. So, all three
   parameters (Range, Bearing & Yaw) must be used to approach the target
   and end up directly in front of it.

   ターゲットの真正面の一定距離に到達することは、ホロノミック（全方向）ドライブを備えたロボットで簡単に実行できます。これは、ストレイフィング（横移動）を直接横方向の動きに使用できるためです。3 つのアプローチを使用できます。1) ターゲット Bearing を使用して、ロボットをターゲットに向けて回転させることができます（上記のとおり）。2) ターゲット Yaw を使用して横方向にストレイフィングし、それによってターゲットの周りを回転して、その真正面に到達できます。3) ターゲット Range を使用して前方または後方に移動し、正しい待機距離を取得できます。

   3 つの軸の動きはそれぞれ、単純な比例制御ループで制御できます。ここでは、タグに向かって回転することに最高のゲイン（優先度）が与えられ、次に横方向へのストレイフィング、次にタグへの接近が続きます。

   詳細については、SDK サンプル: RobotAutoDriveToAprilTagOmni.java を参照してください。

