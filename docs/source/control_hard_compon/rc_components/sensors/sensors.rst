センサー
=========

以下に、一般的なロボットセンサーの例をいくつか示します。*FIRST* Tech Challenge SDK は多くのセンサーをサポートしていますが、すべてがネイティブにサポートされているわけではありません。

例
----------

**Distance Sensor (Ultrasonic)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 1 2 2 2 
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      MaxBotix I2C Ultrasonic Sensor

      ^^^

      .. figure:: images/MB1242.jpg
         :align: center
         :alt: MB1242
         :width: 50%

      +++

      MB1242


超音波距離センサーは、物体とセンサー間の距離を測定できるデバイスです。
これは、音波を送出し、波が物体まで移動して戻ってくるまでの時間を測定することで行います。
これと音速を使用して、距離を計算できます。

**Distance Sensor (Optical)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 1 2 2 2 
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      REV 2m Distance Sensor

      ^^^

      .. figure:: images/REV-31-1505.png
         :align: center
         :alt: REV-31-1505
         :width: 50%

      +++

      REV-31-1505

光学式飛行時間（ToF）センサーは、物体とセンサー間の距離を測定できるデバイスです。
これは、光ビームを送出し、ビームが物体まで移動して戻ってくるまでの時間を測定することで行います。
この時間と既知の光速を使用して、距離を計算できます。
問題の物体が光とどのように相互作用するかによって、距離測定の精度が変わる可能性があることに注意してください。
フィールドパネルのような透明な物体は、しばしば不正確な測定を提供します。

**Color Sensor**
~~~~~~~~~~~~~~~~

.. grid:: 1 2 2 2 
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      REV Color Sensor 

      ^^^

      .. figure:: images/REV-31-1557.png
         :align: center
         :alt: REV-31-1557
         :width: 50%

      +++

      REV-31-1557

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      Modern Robotics Color Sensor

      ^^^

      .. figure:: images/45-2018.png
         :align: center
         :alt: MR 45-2018
         :width: 50%

      +++

      MR 45-2018

カラーセンサーは、通常、物体の色を測定できるデジタル出力デバイスです。
ほとんどのカラーセンサーは、問題の物体がセンサーに比較的近い位置にあることを必要とします。 

**Touch Sensor**
~~~~~~~~~~~~~~~~

.. grid:: 1 2 2 2 
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      REV Touch Sensor

      ^^^

      .. figure:: images/REV-31-1425.png
         :align: center
         :alt: REV-31-1425
         :width: 25%

      +++

      REV-31-1425

タッチセンサーは、ボタンのアクティベーションを検出するデジタル出力デバイスです。
これは、メカニズムの動作範囲を制限する方法であるリミットスイッチとして使用できます。
このようなデバイスは、通常、デジタルポートを使用します。


**Magnetic Limit Switch**
~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 1 2 2 2 
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      REV Magnetic Limit Switch

      ^^^

      .. figure:: images/REV-31-1462.png
         :align: center
         :alt: REV-31-1462
         :width: 25%

      +++

      REV-31-1462

磁気リミットスイッチは、近接した位置にある磁石の存在を検出するために使用されます。
これは、指定された制限を超えると損傷を引き起こすメカニズムの移動範囲を制限するために一般的に使用されます。
これは、リミットスイッチをアクティブにする磁石を該当するメカニズムに配置することで行われます。
デジタルデバイスとして、これはブール値の出力のみを送信し、範囲は送信しないことに注意することが重要です。
磁場の強度を測定するには、磁力計を参照してください。

IMU
~~~~~

.. grid:: 1 2 2 2 
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      Navigation Sensor

      ^^^

      .. figure:: images/navx2.png
         :align: center
         :alt: navX2-Micro
         :width: 50%

      +++

      navX2-Micro

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      BNO055

      ^^^

      .. figure:: images/BNO055.jpg
         :align: center
         :alt: BNO055
         :width: 50%

      +++

      BNO055


慣性測定ユニット（**IMU** ）は、ジャイロスコープ、加速度計、磁力計を組み合わせたセンサーです。
ジャイロスコープは、物体の 3 次元での `角度方向 <https://en.wikipedia.org/wiki/Orientation_(geometry)>`__ を報告するデバイスです。
加速度計は、物体の 3 次元での加速度を報告するデバイスです。加速度は、任意の瞬間における速度の変化率と考えることができます。
磁力計は、3 軸での磁場の強度を測定するデバイスです。これは、地球の極に対するロボットの方向を得るためのコンパスとして使用でき、
絶対的な測定値となります。

Potentiometer
~~~~~~~~~~~~~~~

.. grid:: 1 2 2 2 
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      REV Potentiometer

      ^^^

      .. figure:: images/REV-31-1155.png
         :align: center
         :alt: REV-31-1155
         :width: 50%

      +++

      REV-31-1155

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body
      
      50k Ohm Potentiometer

      ^^^

      .. figure:: images/BBG-770.jpg
         :align: center
         :width: 50%
         :alt: BBG-770

      +++

      50k Ohm Potentiometer

ポテンショメーターは、アジャスターが回転する程度に基づいて出力電圧を変更するデバイスです。
これは、車軸の絶対的な方向を測定する形式としてよく使用されます。出力電圧が変化する方法は、
使用されるポテンショメーターに基づいています。
このようなデバイスは、通常、**REV Hub** のアナログポートを介して接続されます。


センサー互換性チャート
---------------------------

センサー互換性に関するこの便利なチャートを提供してくれた **REV Robotics** の方々に感謝します。

.. list-table::
   :header-rows: 1
   :class: longtable

   * - **Sensor**
     - Type
     - Compatible
     - Adapters Needed

   * - Absolute Orientation IMU Fusion Breakout - BNO0552472Adafruit
     - I2C
     - Yes
     - | 3.3V Compatible
       | Custom Wiring Harness Needed

   * - RGB Color Sensor with IR filter and White LED - TCS347251334AdaFruit
     - I2C
     - Yes
     - | 3.3V Compatible
       | Custom Wiring Harness Needed

   * - ColorSensor45-2018Modern Robotics
     - I2C
     - Yes
     - .. figure:: images/image_3_3.png
          :align: center
   * - Compass45-2003Modern Robotics
     - I2C
     - Yes
     - .. figure:: images/image_4_3.png
          :align: center
   * - Integrating Gyro45-2005Modern Robotics
     - I2C
     - Yes
     - .. figure:: images/image_5_3.png
          :align: center
   * - IR Locator 36045-2009Modern Robotics
     - I2C
     - Yes
     - .. figure:: images/image_6_3.png
          :align: center
   * - IR Seeker V345-2017Modern Robotics
     - I2C
     - Yes
     - .. figure:: images/image_7_3.png
          :align: center
   * - Ranger Sensor45-2008Modern Robotics
     - I2C
     - Yes
     - .. figure:: images/image_8_3.png
          :align: center
   * - NeveRest MotorAM-3461, AM-3102, AM-2964a, AM-3103, AM-3104AndyMark
     - Quad Encoder
     - Yes
     - .. figure:: images/image_9_3.png
          :align: center
   * - HD Hex MotorREV-41-1301REV Robotics
     - Quad Encoder
     - Yes
     - | Directly Compatible 
       | No Custom Adapters Needed

   * - Core Hex MotorREV-41-1301REV Robotics
     - Quad Encoder
     - Yes
     - | Directly Compatible
       | No Custom Adapters Needed

   * - 12v 4mm Motor Kit50-0119MATRIX
     - Quad Encoder
     - Yes
     - .. figure:: images/image_12_3.png
          :align: center
   * - 12v 6mm Motor Kit50-0120MATRIX
     - Quad Encoder
     - Yes
     - .. figure:: images/image_13_3.png
          :align: center
   * - Standard Motor Kit50-0001MATRIX
     - Quad Encoder
     - Yes
     - .. figure:: images/image_14_3.png
          :align: center
   * - Max Motor Shaft Encoder KitW38000Tetrix
     - Quad Encoder
     - Yes
     - .. figure:: images/image_15_3.png
          :align: center
   * - Limit Switch45-2401Modern Robotics
     - Digital
     - Yes
     - | No Adapter Needed
       | Custom Wiring Harness Required.

   * - Rate Gyro45-2004Modern Robotics
     - Analog
     - No
     - Not Officially Supported

   * - Optical Distance Sensor45-2006Modern Robotics
     - Analog
     - No
     - Not Officially Supported

   * - Touch Sensor45-2007Modern Robotics
     - Analog
     - Yes
     - | No Adapter Needed
       | Custom Wiring Harness Required

   * - Light Sensor45-2015Modern Robotics
     - Analog
     - No
     - Not Officially Supported

   * - Magnetic Sensor45-2020Modern Robotics
     - Analog
     - No
     - Not Officially Supported

追加リソース
---------------------

 - :ref:`Analog Port Overview <control_hard_compon/rc_components/hub/ports/ch-ports:analog ports>`
 - :ref:`Digital Port Overview <control_hard_compon/rc_components/hub/ports/ch-ports:digital ports>`
 - :ref:`I2C Port Overview <control_hard_compon/rc_components/hub/ports/ch-ports:i2c ports>`
