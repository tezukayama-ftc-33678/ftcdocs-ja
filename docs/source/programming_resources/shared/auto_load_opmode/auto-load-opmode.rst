ドライバー制御 **Op Mode** の自動ロード
==================================================

**FIRST** **Tech Challenge** の試合は、30秒の自律期間と、その後の2分間のドライバー制御（すなわち、テレオペレートまたは teleop）期間で構成されます。以前は、チームは自律部分の試合が終了した後、手動で teleop **op mode** を選択する必要がありました。

チームは現在、teleop **op mode** を事前選択でき、自律実行が完了するとすぐに **Driver Station** がこの **op mode** を自動的にロードするようにできます。この機能は、チームが試合中に間違った **op mode** を選択するのを避けるのに役立ちます。

この機能を使用するには、**SDK** ソフトウェア（**Robot Controller** と **Driver Station**）のバージョン 6.1 以降を使用していることを確認してください。

試合中に使用する自律プログラムを選択します。事前選択ボタンが画面の左下隅に表示されます。半透明で、隣接するテキストがなく、機能が非アクティブであることを示しています。


.. figure:: images/translucentPreselectLandscape.png   
   :align: center

   横向きモードで自律 **OpMode** が選択されると、事前選択ボタンが表示されます。

.. figure:: images/translucentPreselect.png   
   :align: center

   縦向きモードで自律 **OpMode** が選択されると、事前選択ボタンが表示されます。


事前選択ボタンを表示するには、選択された **op mode** が、Java を使用して記述されている場合は \_@Autonomous\_ アノテーションを使用するか、**Blocks** エディターで *Autonomous* オプションを選択することによって、自律 **op mode** として指定されている必要があることに注意してください。事前選択ボタンが表示されない場合は、現在選択されている **op mode** が自律として指定されていることを確認してください。

.. figure:: images/designateAsAutonomous.png   
   :align: center

   事前選択ボタンを表示するには、選択された **op mode** が Autonomous として指定されている必要があります。

アクティブ化するには、（半透明の）ボタンをタップして、**op mode** を選択するだけです。その後、ボタンは完全に不透明になり、事前選択された **op mode** の名前がボタンの隣に表示されます。これは、機能がアクティブであることを示しています。


.. figure:: images/opaquePreselectLandscape.png   
   :align: center

   横向きモードで、不透明なボタンと **op mode** 名は、機能がアクティブであることを示しています。

.. figure:: images/opaquePreselect.png   
   :align: center

   縦向きモードで、不透明なボタンと **op mode** 名は、機能がアクティブであることを示しています。


機能を無効にするには、事前選択ボタンをタップし、**None** を選択します。ボタンは半透明になり、隣接するテキストが削除されます。

自律 **OpMode** の実行が完了すると、事前選択された **OpMode** が **Driver Station** によって自動的にロードされます。
