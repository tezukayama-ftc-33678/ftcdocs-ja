バッテリーポート
--------------

.. danger:: 
   バッテリー充電器をバッテリーポートに直接接続**しないでください**。これにより、保証が無効になり、Hub が故障します。

黄色の `XT30 <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/xt-30-power-cable>`_ コネクタは、**REV Hub** とそれに接続されたすべてのデバイスに電力を供給するために使用されます。これらのポートの詳細については、`REV ドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#input-power-specifications>`_ を参照してください。これらのポートの1つは、アースストラップの接続にも使用できます。法的なアースストラップの詳細については、`競技マニュアル <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`_ の電源分配セクションを参照してください。

XT30 コネクタは脆弱性で知られているため、使用時には十分注意することを強くお勧めします。また、コネクタのピンを定期的に拡張することをお勧めします。REV には、XT30 コネクタのピンの拡張に関する `トラブルシューティング記事 <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting#xt30-pins-are-compressed>`_ があります。このプロセスの詳細については、この `YouTube ビデオ <https://www.youtube.com/watch?v=UYXTiSeVmB0>`_ をご覧ください。このビデオは XT30 の大型版である XT60 コネクタとドローンを取り上げていますが、アドバイスはほぼ同じです。

モーターポート
-------------

These `JST-VH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-vh-motor-power>`_ 
style connectors are used to power your motors. There are 4 of these ports 
per hub and they are numbered from 0-3. As you are able to use 8 motors per robot you may 
want to control more than these hubs allow. In that case it is possible for you to use 
an :ref:`additional hub<hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>` 
or to use a `REV SPARKmini Motor Controller <https://www.revrobotics.com/rev-31-1230/>`_ 
(REV-31-1230) to power more motors. For more information on this port please see 
`REV Motor Port Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#motor-port-specifications>`_.


エンコーダーポート
--------------

これらの 4 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ スタイルコネクタは、直交エンコーダーに使用されます。各 Hub にはこれらのポートが 4 つあり、隣接するモーターと組み合わせて使用できます。ただし、このポートを使用してスタンドアロンのインクリメンタルエンコーダーに接続することも可能です。4 つ以上のエンコーダーに接続するには、現在、追加の Hub を接続する必要があります。このポートの詳細については、`REV エンコーダーポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#encoder-port-specifications>`_ を参照してください。

Servo Ports
------------

These 0.1” Header pins are used to power and control your servos. There are 6 ports on each hub and they are numbered from 0-5. 
Be mindful of matching the polarity of the device attached to this port as it is possible to flip the connector. 
For increasing the power supplied to these servos it is possible to use a Servo Power Module. 
See the Motors & Actuators section of the `Competition Manual <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`_ for approved servo power devices.
サーボポート
------------

これらの 0.1 インチヘッダーピンは、サーボに電力を供給し、制御するために使用されます。各 Hub には 6 つのポートがあり、0〜5 の番号が付けられています。コネクタを反転することが可能であるため、このポートに接続するデバイスの極性を一致させるように注意してください。これらのサーボに供給される電力を増やすには、サーボパワーモジュールを使用することができます。承認されたサーボ電源デバイスについては、`競技マニュアル <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`_ のモーター＆アクチュエーターセクションを参照してください。このポートの詳細については、`REV サーボポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#servo-port-specifications>`_ を参照してください。

+5V 電源ポート
---------------

これらの 0.1 インチヘッダーピンは、さまざまな機器に電力を供給し、制御するために使用されます。各 Hub には 2 つのポートがあります。これらのコネクタは、電源付き USB ハブへの電力供給など、*FIRST* Tech Challenge の限られた範囲のアプリケーションに使用できます。このポートの詳細については、`REV +5V 電源ポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#id-5v-power-port-specifications>`_ および `競技マニュアル <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`_ の電力分配セクションを参照してください。
of values rather than digital which alternates between one of two states. For more information on this port please see 
`REV Analog Port Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#analog-port-specifications>`_.

Digital Ports
---------------

These 4-pin `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ 
style connectors are used for your digital inputs. There are 4 of these ports on each hub with a total of 8 channels labeled from `0-7`. 
A device attached to a digital port alternates between one of two states (e.g., on and off). One such device would be a button. It is important
to note that each port has two channels and devices such as the `REV Touch Sensor <https://www.revrobotics.com/rev-31-1425/>`_ will only operate on one channel (N+1).


I2C Ports
---------

.. todo::
   TODO [uvidyadharan]
   Add reference to I2C Driver creation tutorial once migrated

These 4-pin `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ 
style connectors are used for connecting I2C sensors. Each port is a single I2C bus where multiple sensors can be 
attached. Using sensors with identical addresses on the same bus can cause problems. 
While it is possible to use a large range of 
sensors, the vast majority of I2C sensors do not have drivers built into the SDK. It is possible to use community drivers 
or create your own. For more information on this port please see 
`REV I2C Port Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#i2c-port-specifications>`_.


RS485
-----

These 3-pin `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ 
style connectors are used for serial communication between REV Hubs. You would use this port if you wished to use a second REV Hub 
as described :ref:`in this tutorial <hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>`. 
Both RS485 ports can be used to add redundancy by using two cables connecting both ports between the REV Hubs.

UART
-----

This connector is used only for **Developer** (non end user) debugging. Its use is not supported 
by *FIRST*.

