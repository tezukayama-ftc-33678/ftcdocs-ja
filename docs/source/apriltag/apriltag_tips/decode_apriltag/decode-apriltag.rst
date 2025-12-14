RTX提供のDECODEにおけるAprilTagの課題
=============================================

AprilTagとは？
--------------

`ミシガン大学 <https://april.eecs.umich.edu/software/apriltag>`_ で開発された **AprilTag** は、2Dバーコードや簡略化されたQRコードに似ています。数値の **ID コード** を含み、** 位置と向き** に使用できます。

RTX提供のDECODEシーズンの **FIRST** Tech Challenge では、**AprilTag** は3つの異なる方法で使用されます：

1. **OBELISK** 上では、**AprilTag** は各 **MATCH** でランダム化される3つの **MOTIF** の1つを識別するために使用されます。
2. **GOAL** 上では、**AprilTag** をターゲットに使用して、チームが **ARTIFACT** を正しい **GOAL** に正確に発射できます。
3. **GOAL** 上では、**AprilTag** はビジュアルオドメトリシステムとして使用でき、**AprilTag** が提供する情報を使用して **FIELD** 上の **ROBOT** の位置を計算します（ローカライゼーションと呼ばれるプロセス）。詳細については、:doc:`AprilTag ローカライゼーション <../../vision_portal/apriltag_localization/apriltag-localization>` ページを参照してください。

.. figure:: images/decode-apriltags.png
   :width: 50%
   :align: center
   :alt: DECODEフィールドとAprilTag位置を示す画像

   DECODEフィールド上のAprilTag IDと位置

困難な環境照明でのAprilTag
---------------------------

今シーズン、チームが直面する課題の1つは、カメラが **AprilTag** を正しく認識できるようにすることです。**AprilTag** は、**AprilTag** の白と黒の部分がコントラストの高い色であるという事実に依存しています - 環境の照明が十分なコントラストを許さない場合、**AprilTag** アルゴリズムは **AprilTag** を適切に検出できない可能性があります。幸いなことに、事実上すべてのウェブカメラで環境の問題を修正するのに役立つことができます。

優れた例の状況が倉庫で発生しました。**DECODE** フィールドが倉庫に設置され、``ConceptAprilTagEasy`` サンプルでデフォルト設定を使用していました。カメラストリームプレビューを表示すると、**OBELISK** 上の **AprilTag** は、晴れた日に **OBELISK** に直接当たる日光によって完全に白飛びし、**AprilTag** が見えませんでした。わずかに異なる角度の別のカメラが同じシーンの別の写真を撮りました。**AprilTag** は見えますが、**AprilTag** から反射する直接光が明らかに多すぎるため、認識できませんでした。このシナリオは、イベントが開催される可能性のある体育館に非常に似ており、晴れた日には光がカメラの **AprilTag** を表示する能力を妨げる可能性があります。何ができるでしょうか？

.. only:: html

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         画像 #1 - 例

         ^^^

         .. figure:: images/1-decode-washed-out-obelisk.*
            :align: center
            :width: 95%
            :alt: OBELISKのAprilTagが見えないDECODEフィールドの画像

         +++
         
         OBELISK上の白飛びしたAprilTag

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         画像 #2 - 別の視点

         ^^^

         .. figure:: images/2-decode-washed-out-obelisk.*
            :align: center
            :width: 85%
            :alt: 別の視点からのDECODEフィールドの画像

         +++

         OBELISKの別の視点

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         画像 #3 - 別の視点

         ^^^

         .. figure:: images/5-decode-warehouse-lighting.*
            :align: center
            :width: 85%
            :alt: 倉庫の窓から入ってくる光を示す画像

         +++

         倉庫に入る日光
         
.. only:: latex

   .. list-table:: 困難なシナリオの異なる視点
      :class: borderless

      * - .. image:: images/1-decode-washed-out-obelisk.*
        - .. image:: images/2-decode-washed-out-obelisk.*
        - .. image:: images/5-decode-warehouse-lighting.*

この環境照明に対抗する最良の方法は、**SDK** 内のウェブカメラ設定を使用して、ゲインと露出設定の両方を同時に調整することです。露出を最小化し（各画像フレームで光がセンサーに当たる時間を短縮）、ゲインを最大化する（センサーからの信号を増幅）ことで、結果の画像は通常の画像よりも暗くなりますが、**AprilTag** のような高コントラストの要素が強調され、認識できるようになります。これは ``ConceptAprilTagOptimizeExposure`` サンプルを使用して実験できます。

確かに、ウェブカメラの露出を最小化し、ゲインを最大化することで、ウェブカメラからの結果の画像を使用して、問題のある **AprilTag** を認識できました。さらに多くの例として、``RobotAutoDriveToAprilTag...`` サンプル **OpMode** もこの手法を使用して、カメラの露出とゲイン設定を調整し、ほとんどの条件下で **AprilTag** が読み取れるようにしています。

.. tip:: 
   大きな利点の1つは、この手法（露出を最小化しながらゲインを最大化）は、移動中の **AprilTag** を読み取る際のモーションブラーを減らすのにも非常に人気があることです - したがって、これには複数の利点があります！

露出とゲインが適切に設定された後の画像の例を次に示します。1つの画像は **AprilTag** 処理が有効になっており、**AprilTag** が適切に検出されていることを示しています。もう1つは処理が無効になっているため、ウェブカメラから返される生画像を見ることができます。

.. only:: html

   .. grid:: 1 2 2 2
      :gutter: 2

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         画像 #4 - 処理済み画像

         ^^^

         .. figure:: images/3-decode-recognized-obelisk.*
            :align: center
            :width: 95%
            :alt: OBELISKのAprilTagが処理されているDECODEフィールドの画像

         +++
         
         検出を示す処理済み画像

      .. grid-item-card::
         :class-header: sd-bg-dark font-weight-bold sd-text-white
         :class-body: sd-text-left body

         画像 #5 - 生の処理済み画像

         ^^^

         .. figure:: images/4-decode-recognized-obelisk-raw.*
            :align: center
            :width: 95%
            :alt: 生の処理済みDECODEフィールドの画像

         +++

         AprilTag処理なしの画像

.. only:: latex

   .. list-table:: 結果の画像
      :class: borderless

      * - .. image:: images/3-decode-recognized-obelisk.*
        - .. image:: images/4-decode-recognized-obelisk-raw.*

OBELISK上の複数のAprilTagの読み取り
------------------------------------

**OBELISK** は正三角柱（実際のオベリスクには4つの面があることは知っています）で、**FIELD** の **GOAL** 側に、**FIELD** 境界の外側に長方形の面の1つが中央に配置されています。**ROBOT** が **ALLIANCE** の **GOAL** に接触してフィールドに配置されると、**ROBOT** のカメラが複数の **AprilTag** を認識して処理する可能性が非常に高くなります。

.. warning:: 
   両方の **AprilTag** を読み取り、それら2つのタグを使用して実際にどの **AprilTag** が見えているかを判断（および検証）することは論理的に見えるかもしれません。ただし、**OBELISK** 上の **AprilTag** には定義された順序がないため、これは信頼できません。


.. figure:: images/6-decode-obelisk-tags.*
   :align: center
   :width: 75%
   :alt: 複数のAprilTagが見えるOBELISKを示す画像

   BLUE GOALからのOBELISK上のAprilTagの表示

**FIELD** に実際に表示されている **AprilTag** を判断する信頼できる方法は、**OBELISK** の正面の **AprilTag** のみが表示できる位置に **ROBOT** を移動することです。

今シーズンの幸運を祈ります！
