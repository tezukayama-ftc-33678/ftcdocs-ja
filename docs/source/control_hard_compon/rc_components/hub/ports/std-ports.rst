バッテリーポート
--------------

.. danger:: 
   バッテリー充電器をバッテリーポートに直接接続**しないでください**。これにより、保証が無効になり、Hub が故障します。

黄色の `XT30 <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/xt-30-power-cable>`_ コネクタは、**REV Hub** とそれに接続されたすべてのデバイスに電力を供給するために使用されます。これらのポートの詳細については、`REV ドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#input-power-specifications>`_ を参照してください。これらのポートの1つは、アースストラップの接続にも使用できます。法的なアースストラップの詳細については、`競技マニュアル <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`_ の電源分配セクションを参照してください。

XT30 コネクタは脆弱性で知られているため、使用時には十分注意することを強くお勧めします。また、コネクタのピンを定期的に拡張することをお勧めします。REV には、XT30 コネクタのピンの拡張に関する `トラブルシューティング記事 <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting#xt30-pins-are-compressed>`_ があります。このプロセスの詳細については、この `YouTube ビデオ <https://www.youtube.com/watch?v=UYXTiSeVmB0>`_ をご覧ください。このビデオは XT30 の大型版である XT60 コネクタとドローンを取り上げていますが、アドバイスはほぼ同じです。

モーターポート
-------------

これらの `JST-VH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-vh-motor-power>`_ スタイルコネクタは、モーターに電力を供給するために使用されます。各 Hub にはこれらのポートが 4 つあり、0〜3 の番号が付けられています。ロボットごとに 8 つのモーターを使用できるため、これらの Hub が許可する以上のモーターを制御したい場合があります。その場合、:ref:`追加の Hub<hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>` を使用するか、`REV SPARKmini Motor Controller <https://www.revrobotics.com/rev-31-1230/>`_（REV-31-1230）を使用してより多くのモーターに電力を供給することができます。このポートの詳細については、`REV モーターポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#motor-port-specifications>`_ を参照してください。


エンコーダーポート
--------------

これらの 4 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ スタイルコネクタは、直交エンコーダーに使用されます。各 Hub にはこれらのポートが 4 つあり、隣接するモーターと組み合わせて使用できます。ただし、このポートを使用してスタンドアロンのインクリメンタルエンコーダーに接続することも可能です。4 つ以上のエンコーダーに接続するには、現在、追加の Hub を接続する必要があります。このポートの詳細については、`REV エンコーダーポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#encoder-port-specifications>`_ を参照してください。

サーボポート
------------

これらの 0.1 インチヘッダーピンは、サーボに電力を供給し、制御するために使用されます。各 Hub には 6 つのポートがあり、0〜5 の番号が付けられています。コネクタを反転することが可能であるため、このポートに接続するデバイスの極性を一致させるように注意してください。これらのサーボに供給される電力を増やすには、サーボパワーモジュールを使用することができます。承認されたサーボ電源デバイスについては、`競技マニュアル <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`_ のモーター＆アクチュエーターセクションを参照してください。このポートの詳細については、`REV サーボポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#servo-port-specifications>`_ を参照してください。

+5V 電源ポート
---------------

これらの 0.1 インチヘッダーピンは、さまざまな機器に電力を供給し、制御するために使用されます。各 Hub には 2 つのポートがあります。これらのコネクタは、電源付き USB ハブへの電力供給など、*FIRST* Tech Challenge の限られた範囲のアプリケーションに使用できます。このポートの詳細については、`REV +5V 電源ポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#id-5v-power-port-specifications>`_ および `競技マニュアル <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`_ の電力分配セクションを参照してください。

アナログポート
---------------

これらの 4 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ スタイルコネクタは、アナログ入力に使用されます。各 Hub にはこれらのポートが 4 つあり、0〜3 の番号が付けられています。アナログポートに接続されたデバイスは、2 つの状態のいずれかを交互に切り替えるデジタルではなく、値の範囲を提供します。このポートの詳細については、`REV アナログポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#analog-port-specifications>`_ を参照してください。

デジタルポート
---------------

これらの 4 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ スタイルコネクタは、デジタル入力に使用されます。各 Hub にはこれらのポートが 4 つあり、合計 8 つのチャンネルが `0-7` とラベル付けされています。デジタルポートに接続されたデバイスは、2 つの状態（例：オンとオフ）のいずれかを交互に切り替えます。そのようなデバイスの 1 つがボタンです。各ポートには 2 つのチャンネルがあり、`REV Touch Sensor <https://www.revrobotics.com/rev-31-1425/>`_ などのデバイスは 1 つのチャンネル（N+1）でのみ動作することに注意することが重要です。


I2C ポート
---------

.. todo::
   TODO [uvidyadharan]
   Add reference to I2C Driver creation tutorial once migrated

これらの 4 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ スタイルコネクタは、I2C センサーの接続に使用されます。各ポートは単一の I2C バスであり、複数のセンサーを接続できます。同じバス上で同一のアドレスを持つセンサーを使用すると、問題が発生する可能性があります。広範囲のセンサーを使用することは可能ですが、I2C センサーの大部分には SDK に組み込まれたドライバーがありません。コミュニティドライバーを使用するか、独自のドライバーを作成することができます。このポートの詳細については、`REV I2C ポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#i2c-port-specifications>`_ を参照してください。


RS485
-----

これらの 3 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ スタイルコネクタは、REV Hub 間のシリアル通信に使用されます。:ref:`このチュートリアル <hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>` で説明されているように、2 つ目の REV Hub を使用する場合にこのポートを使用します。両方の RS485 ポートを使用して、REV Hub 間の両方のポートを接続する 2 本のケーブルを使用することで、冗長性を追加できます。

UART
-----

このコネクタは**開発者**（エンドユーザー以外）のデバッグにのみ使用されます。その使用は *FIRST* によってサポートされていません。

