エンコーダー（回転カウンター）
==============================

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      REV HD Hex Motor 

      ^^^

      .. figure:: images/REV-41-1291.png
         :align: center
         :width: 50%

      +++

      Built-in Encoder in the REV HD Hex Motor

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      REV Through Bore Encoder

      ^^^

      .. figure:: images/REV-11-1271.png
         :align: center
         :width: 50%

      +++

      REV Through Bore Encoder, in incremental mode.

エンコーダーは、軸の周りの回転変位を測定するデバイスです。ほとんどの合法的な **FIRST Tech Challenge** モーターには、
**REV Hub** と互換性のある直交エンコーダーが内蔵されています。また、上に示した **REV Through Bore Encoder** のような
スタンドアロンのインクリメンタルエンコーダーを使用することも可能です。インクリメンタルエンコーダーは、シャフトの部分的な回転ごとに
「ティック」を送出することで機能します。1 回転あたりに出力されるティック数の詳細については、製造元のウェブサイトで確認できます。
アブソリュートエンコーダーは、シャフトの開始位置からの変位と、「ゼロ」位置に対するシャフトの現在の正確な角度を示すことができます。


追加リソース
---------------------

 - :ref:`Encoder Port Overview <control_hard_compon/rc_components/hub/ports/exh-ports:encoder ports>`
