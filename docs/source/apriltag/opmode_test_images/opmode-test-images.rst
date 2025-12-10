*FIRST* Tech Challenge AprilTag テストサンプル
===============================================

はじめに
------------

2023-2024 シーズンでは、`FIRST Tech Challenge が AprilTags を導入しました
<https://ftc-docs.firstinspires.org/en/latest/apriltag/vision_portal/apriltag_intro/apriltag-intro.html>`__。これはシーズン固有の競技に使用されます。AprilTags は、ミシガン大学の April Robotics Laboratory によって開発され、QR コードと同様の概念に基づいて構築された視覚的フィデューシャルタギングシステムで、拡張現実、ロボティクス、カメラキャリブレーションを含む幅広いタスクに有用です。適切にキャリブレーションされたカメラとタグライブラリを使用して、AprilTags を検出し、カメラに対するタグの範囲と方向情報（**ポーズ** データとも呼ばれる）などの情報を提供できます。*FIRST* Tech Challenge Software Development Kit (SDK) は、チームがこのリソースを利用できるように AprilTag 検出 API を追加するために更新されました。

このドキュメントには、SDK 内の *FIRST* Tech Challenge AprilTag サンプルで使用することを目的とした AprilTags の例が含まれています。2023-2024 シーズンで使用されるすべての AprilTags は、36h11 タグファミリーから来ています。これは、事前に決定されたタグのセットです。主要なタグ領域は、黒と白の *ピクセル* の 8x8 正方形マトリックスで構成されています。タグのサイズは、タグの全体の黒い正方形部分の物理的寸法に基づいて測定されます – 4 インチの AprilTag には、各辺が 4 インチを測定する黒い正方形部分があります。AprilTag のサイズを測定する際には使用されませんが、各タグには、主要なタグ領域を囲む 1 *ピクセル* 厚の白い境界線も必要です（合計タグサイズは 10x10 *ピクセル* になります）。追加された白い境界線により、たとえば、4 インチの AprilTag には各辺 5 インチのフットプリントが必要です。

.. figure:: images/apriltag_sizing.png
   :width: 75%
   :align: center
   :alt: AprilTag Sizing

   Example sizing for 4-inch AprilTag

*FIRST* Tech Challenge の AprilTag API は複数のタグサイズを処理できます；各個別のタグは独立してサイズを設定できますが、個別のタグに複数のサイズを設定することはできません。各タグに対して計算される一部のポーズ情報（カメラからタグまでの距離データなど）には、使用されるタグの正確なサイズを知る必要があります。SDK 内のサンプルプログラムで使用されるデフォルトのタグサイズは次のとおりです：

+-----------------------------------+-----------------------------------+
| **タグの説明**                     | **タグのサイズ（インチ）          |
|                                   | （ミリメートル）**                |
+===================================+===================================+
| Tag ID: 583 (AKA “Nemo”)          | 4 in (101.6 mm)                   |
+-----------------------------------+-----------------------------------+
| Tag ID: 584 (AKA “Jonah”)         | 4 in (101.6 mm)                   |
+-----------------------------------+-----------------------------------+
| Tag ID: 585 (AKA “Cousteau”)      | 6 in (152.4 mm)                   |
+-----------------------------------+-----------------------------------+
| Tag ID: 586 (AKA “Ariel”)         | 6 in (152.4 mm)                   |
+-----------------------------------+-----------------------------------+

When printing out the :download:`PDF version of this document
<files/FTCAprilTagSDK82SamplesExtended.pdf>`, or portions thereof, please set
the Page Size settings to “Actual Size” to ensure that the tags are printed
properly. Every printer is slightly different, so it’s also a good idea to
measure the width and height of the black-square portion of the main tag area
to verify that the page printed properly.

.. figure:: images/printing.png
   :width: 75%
   :align: center
   :alt: Printing Document 

   Example printing settings for printing PDF at Actual Size

AprilTag 検出値に関するより詳細な情報と、それらが何を意味するかをよりよく理解するには、次のウェブサイトにアクセスしてください：

:ref:`AprilTag 検出値の理解 <apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values:understanding apriltag detection values>`
- :download:`公式 PDF をダウンロードして印刷 <files/FTCAprilTagSDK82SamplesExtended.pdf>`


AprilTags
---------

認識のためにこれらのタグにカメラを向けることができます - ftc-docs は画像の引き伸ばしを許可しているため、表示領域の幅が画像の幅よりも小さい場合、画像が明確かつ正確に表現されない可能性があります。
:download:`公式 PDF をダウンロードして印刷する <files/FTCAprilTagSDK82SamplesExtended.pdf>` ことをお勧めします。

.. figure:: images/tag583_nemo.png
   :height: 4 in
   :width: 4 in
   :align: center
   :alt: Tag583_nemo

   タグ 583、「Nemo」

|

.. figure:: images/tag584_jonah.png
   :height: 4 in
   :width: 4 in
   :align: center
   :alt: Tag584_jonah

   タグ 584、「Jonah」

|

.. figure:: images/tag585_cousteau.png
   :height: 6 in
   :width: 6 in
   :align: center
   :alt: Tag585_cousteau

   タグ 585、「Cousteau」

|

.. figure:: images/tag586_ariel.png
   :height: 6 in
   :width: 6 in
   :align: center
   :alt: Tag586_ariel

   タグ 586、「Ariel」

|

