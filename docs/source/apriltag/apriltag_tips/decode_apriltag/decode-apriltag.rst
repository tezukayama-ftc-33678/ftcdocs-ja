RTX 提供の DECODE における AprilTag の課題
==============================================

AprilTag とは何ですか？
-----------------------

`ミシガン大学
<https://april.eecs.umich.edu/software/apriltag>`_ で開発された AprilTag は、2D バーコードや簡略化された QR コードに似ています。数値の **ID コード**を含み、**位置と向き**に使用できます。

RTX 提供の DECODE シーズン中の **FIRST** Tech Challenge では、AprilTag は 3 つの異なる方法で使用されます：

1. OBELISK では、AprilTag は各 MATCH でランダム化される 3 つの MOTIF のうちの 1 つを識別するために使用されます。
2. GOAL では、AprilTag を使用して、チームが ARTIFACT を正確に正しい GOAL に発射するためのターゲットにすることができます。
3. GOAL では、AprilTag をビジュアルオドメトリシステムとして使用でき、AprilTag が提供できる情報を使用して、FIELD 上の ROBOT の位置を計算します（ローカライゼーションと呼ばれるプロセスを通じて）。詳細については、:doc:`AprilTag Localization <../../vision_portal/apriltag_localization/apriltag-localization>` ページを参照してください。

.. figure:: images/decode-apriltags.png
   :width: 50%
   :align: center
   :alt: Image showing the DECODE field and AprilTag locations

   DECODE フィールド上の AprilTag ID と位置。

困難な環境照明での AprilTag
------------------------------

今シーズンにチームが直面する課題の 1 つは、カメラが AprilTag を正しく認識できるようにすることです。AprilTag は、AprilTag の白と黒の部分が対照的な色であるという事実に依存しています - 環境の照明が十分なコントラストを許可しない場合、AprilTag アルゴリズムは AprilTag を適切に検出できない可能性があります。幸いなことに、ほぼすべてのウェブカメラで環境の問題を修正するのに役立つことができます。

倉庫で優れた例の状況が発生しました。DECODE フィールドが倉庫に設置され、``ConceptAprilTagEasy`` サンプルでデフォルト設定を使用していました。カメラストリームプレビューを表示すると、晴れた日に太陽光が OBELISK に直接当たることで、OBELISK 上の AprilTag が完全に白飛びし、AprilTag が見えなくなりました。わずかに異なる角度にある別のカメラが同じシーンの別の写真を撮影し、AprilTag は見えますが、AprilTag から反射する直接光が明らかに多すぎて、認識できませんでした。このシナリオは、イベントが開催される可能性のある体育館と非常に似ており、晴れた日には光がカメラの AprilTag を表示する能力を妨げる可能性があります。何ができるでしょうか？

.. only:: html

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         Image #1 - Example

         ^^^

         .. figure:: images/1-decode-washed-out-obelisk.*
            :align: center
            :width: 95%
            :alt: Image of DECODE field with obelisk AprilTag unable to be seen

         +++
         
         Washed Out AprilTag on OBELISK

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         Image #2 - Alternate View

         ^^^

         .. figure:: images/2-decode-washed-out-obelisk.*
            :align: center
            :width: 85%
            :alt: Image of DECODE field from another perspective

         +++

         Alternate View of OBELISK

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         Image #3 - Alternate View

         ^^^

         .. figure:: images/5-decode-warehouse-lighting.*
            :align: center
            :width: 85%
            :alt: Image showing light coming in from windows of warehouse

         +++

         Sunlight Entering Warehouse
         
.. only:: latex

   .. list-table:: Different Views of Challenging Scenario
      :class: borderless

      * - .. image:: images/1-decode-washed-out-obelisk.*
        - .. image:: images/2-decode-washed-out-obelisk.*
        - .. image:: images/5-decode-warehouse-lighting.*

The best way to counter this environmental lighting is to use the webcam
settings within the SDK to adjust both the Gain and the Exposure settings at
the same time. By simultaneously minimizing the exposure (lessening the amount of
time light is allowed to strike the sensor each image frame) and maximizing
the gain (amplifying the signal from the sensor) the resulting image will be 
darker than a normal image but elements of high contrast will be accentuated, 
like AprilTags, allowing them to be recognized. This can be experimented with
using the ``ConceptAprilTagOptimizeExposure`` sample.

Sure enough, by minimizing the Exposure and maximizing the Gain of the webcam,
the resulting images from the webcam were able to be used to recognize the
problematic AprilTags. For more examples, the ``RobotAutoDriveToAprilTag...``
sample OpModes also use this technique for adjusting the exposure and gain 
settings of the camera to ensure the AprilTags are readable under most 
conditions. 

.. tip:: 
   One big advantage is that this technique (minimizing exposure while
   maximizing gain) is ALSO very popular in reducing motion blur for reading
   AprilTags while moving - so this has more than one benefit!

Here are examples of the images once the exposure and gain are set appropriately,
one image has the AprilTag processing enabled to show that the AprilTag is 
being detected properly, and the other has processing disabled so that we can 
see the raw image being returned by the webcam.

.. only:: html

   .. grid:: 1 2 2 2
      :gutter: 2

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         Image #4 - Processed Image

         ^^^

         .. figure:: images/3-decode-recognized-obelisk.*
            :align: center
            :width: 95%
            :alt: Image of DECODE field with obelisk AprilTag being processed

         +++
         
         Processed Image showing Detections

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         Image #5 - Raw Processed Image

         ^^^

         .. figure:: images/4-decode-recognized-obelisk-raw.*
            :align: center
            :width: 95%
            :alt: Image of raw processed DECODE field 

         +++

         Image without AprilTag processing

.. only:: latex

   .. list-table:: Resulting Images
      :class: borderless

      * - .. image:: images/3-decode-recognized-obelisk.*
        - .. image:: images/4-decode-recognized-obelisk-raw.*

Reading Multiple AprilTags on the OBELISK
-----------------------------------------

The OBELISK is an equilateral triangular prism (we know, real obelisks have 4
sides) which is positioned with 1 of the rectangular faces centered on the
GOAL-side of the FIELD, just outside of the FIELD perimeter. When ROBOTS are
set up on the field contacting their ALLIANCE'S GOAL, it is a very real
possibility that the ROBOT's camera will see and process multiple AprilTags.

.. warning:: 
   It might seem logical to read both AprilTags and use those two tags to
   determine (and verify) which AprilTag is actually being seen. However, there
   is no defined order for AprilTags on an OBELISK, so this is not reliable. 


.. figure:: images/6-decode-obelisk-tags.*
   :align: center
   :width: 75%
   :alt: Image showing OBELISK with more than one AprilTag visible

   View of AprilTags on OBELISK from BLUE GOAL

A reliable way to determine which AprilTag is truly showing on the FIELD
is to move the ROBOT into a position where the AprilTag on the front face of
the OBELISK is the only tag that can be viewed. 

Good Luck this season!
