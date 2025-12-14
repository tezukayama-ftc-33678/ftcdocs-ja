ドライバー制御 **Op Mode** の自動ロード
==================================================

**FIRST** **Tech Challenge** の試合は、30秒の自律期間と、その後の2分間のドライバー制御（すなわち、テレオペレートまたは teleop）期間で構成されます。以前は、チームは自律部分の試合が終了した後、手動で teleop**op mode** を選択する必要がありました。

チームは現在、teleop **op mode** を事前選択でき、自律実行が完了するとすぐに**Driver Station** がこの**op mode** を自動的にロードするようにできます。この機能は、チームが試合中に間違った**op mode** を選択するのを避けるのに役立ちます。

この機能を使用するには、**SDK** ソフトウェア（**Robot Controller** と**Driver Station** ）のバージョン 6.1 以降を使用していることを確認してください。

試合中に使用する自律プログラムを選択します。事前選択ボタンが画面の左下隅に表示されます。半透明で、隣接するテキストがなく、機能が非アクティブであることを示しています。


.. figure:: images/translucentPreselectLandscape.png   
   :align: center

   横向きモードで自律 **OpMode** が選択されると、事前選択ボタンが表示されます。

.. figure:: images/translucentPreselect.png   
   :align: center

   縦向きモードで自律 **OpMode** が選択されると、事前選択ボタンが表示されます。


事前選択ボタンを表示するには、選択された **op mode** が、Java を使用して記述されている場合は \_@Autonomous\_ アノテーションを使用するか、**Blocks** エディターで *Autonomous* オプションを選択することによって、自律 **op mode** として指定されている必要があることに注意してください。事前選択ボタンが表示されない場合は、現在選択されている**op mode** が自律として指定されていることを確認してください。

.. figure:: images/designateAsAutonomous.png   
   :align: center

   事前選択ボタンを表示するには、選択された **op mode** が Autonomous として指定されている必要があります。

アクティブ化するには、（半透明の）ボタンをタップして、**op mode** を選択するだけです。その後、ボタンは完全に不透明になり、事前選択された**op mode** の名前がボタンの隣に表示されます。これは、機能がアクティブであることを示しています。

.. figure:: images/selectTeleOpLandscape.png
   :align: center

   横向きモードで自動ロードされるドライバー制御 **OpMode** 。

.. figure:: images/selectTeleOp.png   
   :align: center

   縦向きモードで自動ロードされるドライバー制御 **OpMode** 。

その後、無効にしたい場合は、事前選択ボタンを長押しするだけです。ボタンは再び半透明になり、隣接するテキストが消えます。

自律プログラムが終了すると、**Driver Station** は、キューに入れられた**OpMode** を、自律開始前に事前選択された TeleOp プログラムに変更します。ユーザーが停止を押す（メイン停止または init 停止ボタンのいずれか）と、自動事前選択は中止されます。**OpMode** が自己終了するか、30秒タイマーによって終了された場合にのみ、遷移します。安全上の理由から、ドライブチームは依然として手動で Init を押して**op mode** を開始する必要があります。

自律プログラムを実行するたびに、手動で事前選択機能を有効にして構成する必要がない場合は、**OpMode** アノテーションを編集して ``preselectTeleOp="My TeleOp Name"`` を含めることができます。その後、**Driver Station** は自動的に事前選択機能をアクティブ化し、アノテーションで指定された**OpMode** を事前選択するように構成します。

.. code-block:: java
   :caption: preselectTeleOp パラメーターを使用して、事前選択された op mode を指定します。


   @Autonomous(name="Blue Alliance Auto", group="Pushbot", preselectTeleOp="BlueAllianceTeleOp")

**Blocks** ユーザーも、**Blocks** プログラムエディターの新しいドロップダウンを通じて、この機能を使用できます。

.. figure:: images/preselectBlocks.png   
   :align: center

   **Blocks** エディターを使用して、teleop**op mode** を事前選択できます。

**Driver Station** アプリの Settings メニューに「OpMode Auto Queue」というオプションがあることに注意してください。このオプションが有効になっている場合、**Driver Station** は、``preselectTeleOp`` パラメーターで指定されたとおり、自律**op mode** の事前選択された teleop**op mode** を自動的にロードします。このオプションが無効になっている場合、**Driver Station** は事前選択された teleop**op mode** を自動的にロードしません。「Op Mode Auto Queue」オプションが無効になっている場合でも、チームはメインの**Driver Station** アクティビティの事前選択ボタンを使用して、teleop**op mode** を選択できます。

.. figure:: images/AutoQueueEnabledLandscape.png   
   :align: center

   OpMode Auto Queue オプションが有効になっている場合、**Driver Station** は横向きモードで preselectTeleOp**op mode** を自動的にロードします。

.. figure:: images/AutoQueueEnabled.png   
   :align: center

   OpMode Auto Queue オプションが有効になっている場合、**Driver Station** は縦向きモードで preselectTeleOp**op mode** を自動的にロードします。
