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

   .. list-table:: 困難なシナリオの異なる視点
      :class: borderless

      * - .. image:: images/1-decode-washed-out-obelisk.*
        - .. image:: images/2-decode-washed-out-obelisk.*
        - .. image:: images/5-decode-warehouse-lighting.*

この環境照明に対抗する最良の方法は、SDK 内のウェブカメラ設定を使用して、Gain と Exposure の設定を同時に調整することです。露出を最小化（各画像フレームで光がセンサーに当たることを許可する時間を短縮）し、ゲインを最大化（センサーからの信号を増幅）することにより、結果の画像は通常の画像よりも暗くなりますが、AprilTag のような高コントラストの要素が強調され、認識できるようになります。これは ``ConceptAprilTagOptimizeExposure`` サンプルで実験できます。

案の定、ウェブカメラの Exposure を最小化し、Gain を最大化することで、ウェブカメラからの結果の画像を使用して、問題のある AprilTag を認識できました。その他の例については、``RobotAutoDriveToAprilTag...`` サンプル **OpMode** も、ほとんどの条件下で AprilTag が読み取り可能であることを確認するために、カメラの露出とゲイン設定を調整するこの技術を使用します。 

.. tip:: 
   大きな利点の 1 つは、この技術（露出を最小化してゲインを最大化する）が、移動中に AprilTag を読み取るためのモーションブラーを減らすためにも非常に人気があることです - これには複数の利点があります！

露出とゲインが適切に設定された後の画像の例を以下に示します。1 つの画像は AprilTag 処理が有効になっており、AprilTag が適切に検出されていることを示し、もう 1 つは処理が無効になっているため、ウェブカメラから返される生の画像を確認できます。

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

   .. list-table:: 結果の画像
      :class: borderless

      * - .. image:: images/3-decode-recognized-obelisk.*
        - .. image:: images/4-decode-recognized-obelisk-raw.*

OBELISK 上の複数の AprilTag の読み取り
-----------------------------------------

OBELISK は正三角柱です（実際のオベリスクには 4 つの面があることはわかっています）。これは、長方形の面の 1 つが FIELD の GOAL 側の中央に配置され、FIELD の境界のすぐ外側にあります。ROBOT が自分の ALLIANCE の GOAL に接触するようにフィールドに設置されている場合、ROBOT のカメラが複数の AprilTag を認識して処理する可能性が非常に高くなります。

.. warning:: 
   両方の AprilTag を読み取り、それらの 2 つのタグを使用して、実際に認識されている AprilTag を判断（および検証）することは論理的に思えるかもしれません。ただし、OBELISK 上の AprilTag には定義された順序がないため、これは信頼できません。 


.. figure:: images/6-decode-obelisk-tags.*
   :align: center
   :width: 75%
   :alt: Image showing OBELISK with more than one AprilTag visible

   BLUE GOAL から見た OBELISK 上の AprilTag

FIELD に実際に表示されている AprilTag を判断する信頼できる方法は、ROBOT を OBELISK の前面の AprilTag が表示できる唯一のタグである位置に移動することです。 

今シーズン、幸運を祈ります！
