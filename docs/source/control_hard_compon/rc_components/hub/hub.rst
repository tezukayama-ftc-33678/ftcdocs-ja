**REV Hub**
==========

**REV Hub** は、*FIRST* Tech Challenge ロボットのコア制御ユニットです。

**Control Hub**
------------

.. toctree::
    :maxdepth: 1

    ports/ch-ports

.. figure:: images/REV-31-1595.png
    :align: center
    :alt: REV-31-1595
    :width: 50%

    REV Control Hub (REV-31-1595)

**REV Control Hub** は、**REV Expansion Hub** に組み込まれた Android ドーターボードを組み合わせたものです。これは、ロボットのすべてのハードウェアコンポーネントを制御し、実際のロボットソフトウェアを実行できることを意味します。これは、ハードウェアデバイスのみを制御でき、SDK を解釈して実行することができなかった **REV Expansion Hub** とは対照的です。

**Expansion Hub**
--------------

.. toctree::
    :maxdepth: 1

    ports/exh-ports

.. figure:: images/REV-31-1153.png
    :align: center
    :alt: REV-31-1153
    :width: 50%

    REV Expansion Hub (REV-31-1153)

**REV Expansion Hub** は、ロボットのすべてのハードウェアコンポーネントを制御するために使用される Hub です。**Expansion Hub** は、モーターを動かす命令を受け取り、実際にモーターに正しい方法で電力を送ります。ただし、いつこれを行うかはわからないため、Android デバイスが必要になります。このデバイスは、USB 経由で接続された従来の Android スマートフォン、または **Control Hub** に組み込まれたデバイスのいずれかです。複数の Hub を使用する場合、これらの Hub は ``RS485`` または USB 経由で接続できます。詳細については、:ref:`こちら <hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>` を参照してください。
