AprilTag ライブラリ
===================

**FIRST** Tech Challenge の競技では、**OpMode** は検出すべき既知の**AprilTag** セットを持っています。これらはデフォルトでプリロードされているか、カスタムタグの有無に関わらず、皆さんが指定することができます。

これらのタグは**AprilTag Library** を形成します。各ライブラリタグには4から6のプロパティがあり、**Metadata** ページで説明されています。

このページでは、**AprilTag** ライブラリを作成する多くの方法を示します。**Initialization** ページでは、これが**OpMode** で**AprilTag** を使用するための準備の** ステップ1** （オプション）であることを説明しました。**AprilTag** ライブラリの使用をマスターするために、** これらの例を順番に試してください** 。

簡単な方法
~~~~~~~~~~

まず、ライブラリなしから始めましょう！**OpMode** が現在のシーズンのデフォルトのみを使用する場合、ライブラリの操作は不要です。

次のように**AprilTagProcessor** を作成するだけです：

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      .. figure:: images/010-Blocks-ATprocessor-Easy.png
         :width: 75%
         :align: center
         :alt: シンプルな AprilTag Processor

         シンプルな AprilTag Processor

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         AprilTagProcessor myAprilTagProcessor;

         // AprilTag プロセッサを作成し、変数に割り当てます。
         myAprilTagProcessor = AprilTagProcessor.easyCreateWithDefaults();**AprilTag Processor** を作成するには、ライブラリの指定が必要です。この「簡単な方法」でも、背後でデフォルトのライブラリを指定しています。

デフォルトライブラリ
~~~~~~~~~~~~~~~~~~~~**SDK** は、事前定義された**AprilTag** の2つのコアライブラリを使用します：

-  サンプル**OpMode** でのみ使用されるタグ
-  ロボットゲーム（競技）でのみ使用されるタグ

最初のライブラリは ``SampleTagLibrary`` と呼ばれ、SDK 8.2で利用可能です。基本的な**Metadata** 値は次のとおりです：

-  ``583, Nemo, 4, DistanceUnit.INCH``
-  ``584, Jonah, 4, DistanceUnit.INCH``
-  ``585, Cousteau, 6, DistanceUnit.INCH``
-  ``586, Ariel, 6, DistanceUnit.INCH``

2番目のライブラリは ``CenterStageTagLibrary`` と呼ばれ、将来の競技のみを対象としています。SDK 8.2で現在利用可能ですが、現在は3つの「プレースホルダー」タグを保持しています：

-  ``0, MEOW, 0.166, DistanceUnit.METER``
-  ``1, WOOF, 0.166, DistanceUnit.METER``
-  ``2, OINK, 0.166, DistanceUnit.METER``

2023年9月のキックオフ後、これらは**CENTERSTAGE** の** 実際のタグ** に置き換えられます（SDK 9.0で）。

便宜上、3番目のライブラリには、これら2つのコアライブラリの** 両方** が含まれており、それ以外は何も含まれていません。これがデフォルトで、``CurrentGameTagLibrary`` と呼ばれます。

AprilTag Processor
~~~~~~~~~~~~~~~~~~**Processor** の** 任意の側面** を指定するには、**Processor Builder** を使用します。少なくとも2つのコマンドが必要です：

-  Java キーワード ``new`` を使用して**Builder** を作成

-  機能を指定/追加した後、``.build()`` メソッドの呼び出しで完了

これらのアクション間で、**OpMode** は3つのライブラリのいずれかを**Processor Builder** に直接追加します。すべての事前定義タグを含むデフォルトの ``CurrentGameTagLibrary`` を使用するのが最も簡単です。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      まず、この式を作成します。最初のコンポーネントを ``AprilTagProcessor.Builder`` ツールボックス（またはパレット）から描画し、2番目のコンポーネントを ``AprilTagLibrary`` ツールボックスから描画します。

      .. figure:: images/020-Blocks-setTagLibrary-CurrentGame.png
         :width: 75%
         :align: center
         :alt: 現在のゲームのタグライブラリを設定

         現在のゲームのタグライブラリを設定** これを囲むように** （前後に）、**Processor Builder** を** 作成** する1つのブロックと、``.build()`` でプロセスを** 完了** する別のブロックを配置します。

      .. figure:: images/030-Blocks-ATprocessor-CurrentGame.png
         :width: 75%
         :align: center
         :alt: Builder の完成

         Builder の完成

      これらは ``AprilTagProcessor.Builder`` ツールボックスの最初と最後のブロックです。残りのブロックは、**Processor** のオプション機能を設定するために使用されます。ここでは、ライブラリのみを設定しています。

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagProcessor myAprilTagProcessor;

         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // タグライブラリを設定します。
         // 現在のシーズンの AprilTagLibrary を取得します。
         myAprilTagProcessorBuilder.setTagLibrary(AprilTagGameDatabase.getCurrentGameTagLibrary());

         // AprilTag プロセッサをビルドし、変数に割り当てます。
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();


ライブラリ変数
~~~~~~~~~~~~~~

別の方法として、まずライブラリを独自の変数名に格納することもできます。次に、**AprilTag Processor** にその名前を指定します。ここでは ``myAprilTagLibrary`` を使用します（他の名前でも問題ありません）。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      まず、この式を作成します。最初のコンポーネントを ``AprilTagLibrary`` ツールボックスから描画し、2番目のコンポーネントを ``AprilTagProcessor.Builder`` ツールボックスから描画します。

      .. figure:: images/040-Blocks-ATProcessor-Variable.png
         :width: 75%
         :align: center
         :alt: タグライブラリを設定

         タグライブラリを設定

      前と同様に、** これを囲むように** （前後に）、**Processor Builder** を** 作成** する1つのブロックと、``.build()`` でプロセスを** 完了** する別のブロックを配置します。

      .. figure:: images/050-Blocks-ATprocessor-CurrentGame-Variable.png
         :width: 75%
         :align: center
         :alt: AprilTag Processor をビルド

         AprilTag Processor をビルド

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagProcessor myAprilTagProcessor;
         AprilTagLibrary myAprilTagLibrary;

         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // 現在のシーズンの AprilTagLibrary を取得します。
         myAprilTagLibrary = AprilTagGameDatabase.getCurrentGameTagLibrary();

         // タグライブラリを設定します。
         myAprilTagProcessorBuilder.setTagLibrary(myAprilTagLibrary);

         // AprilTag プロセッサをビルドし、変数に割り当てます。
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();


ライブラリ Builder、デフォルトを使用
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

次に、**Builder** パターンを試して、事前定義された**AprilTag** のみを含むライブラリを作成します。これは必要ではありませんが（ビルドする新しいものはありません！）、簡単な導入です。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      -**Library Builder** を作成します。**Processor Builder** とは異なります。
      -  次に ``addTags`` ブロックを使用します - 複数形の "tags" であり、"tag" ではないことに注意してください。
      -  ``.build`` コマンドでプロセスを完了します。

      ビルドされたライブラリは、ここでは ``myAprilTagLibrary`` と呼ばれる変数に割り当てられるか保存されます。

      .. figure:: images/060-Blocks-LibraryBuilder-CurrentGame.png
         :width: 75%
         :align: center
         :alt: タグライブラリをビルド

         タグライブラリをビルド

      次に、おなじみの手順が続きます：

      -**Processor Builder** を作成します。
      -  次に、前のシーケンスでビルドおよび保存されたライブラリを設定または追加します。
      -  ``.build`` コマンドでプロセスを完了します。

      .. figure:: images/070-Blocks-Processor-Variable.png
         :width: 75%
         :align: center
         :alt: タグプロセッサをビルド

         タグプロセッサをビルド

      最終結果は前の例と同じですが、今度は**Library Builder** の使用方法がわかります。

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         AprilTagLibrary.Builder myAprilTagLibraryBuilder;
         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagLibrary myAprilTagLibrary;
         AprilTagProcessor myAprilTagProcessor;

         // 新しい AprilTagLibrary.Builder オブジェクトを作成し、変数に割り当てます。
         myAprilTagLibraryBuilder = new AprilTagLibrary.Builder();

         // 指定された AprilTagLibrary からすべてのタグを AprilTagLibrary.Builder に追加します。
         // 現在のシーズンの AprilTagLibrary を取得します。
         myAprilTagLibraryBuilder.addTags(AprilTagGameDatabase.getCurrentGameTagLibrary());

         // AprilTag ライブラリをビルドし、変数に割り当てます。
         myAprilTagLibrary = myAprilTagLibraryBuilder.build();

         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // タグライブラリを設定します。
         myAprilTagProcessorBuilder.setTagLibrary(myAprilTagLibrary);

         // AprilTag プロセッサをビルドし、変数に割り当てます。
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();


カスタムタグ - 直接指定
~~~~~~~~~~~~~~~~~~~~~~~~

最後に、ライブラリにカスタムタグを追加する準備が整いました。

各タグには**Metadata** が必要です。次のように、新しいタグに**Metadata** 値を直接入力できます。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      3番目のブロックは、カスタムタグをライブラリに追加します。他のすべてのブロックは前の例と同じです。

      .. figure:: images/080-Blocks-addTag.png
         :width: 75%
         :align: center
         :alt: カスタムタグライブラリ

         タグライブラリにカスタムタグを追加

   .. tab-item:: Java
      :sync: java

      カスタムタグは**1行の新しいコード** で追加され、それ以外は前の例と同じです。

      .. code-block:: java

         AprilTagLibrary.Builder myAprilTagLibraryBuilder;
         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagLibrary myAprilTagLibrary;
         AprilTagProcessor myAprilTagProcessor;

         // 新しい AprilTagLibrary.Builder オブジェクトを作成し、変数に割り当てます。
         myAprilTagLibraryBuilder = new AprilTagLibrary.Builder();

         // 指定された AprilTagLibrary からすべてのタグを AprilTagLibrary.Builder に追加します。
         // 現在のシーズンの AprilTagLibrary を取得します。
         myAprilTagLibraryBuilder.addTags(AprilTagGameDatabase.getCurrentGameTagLibrary());

         // ポーズ情報なしでタグを AprilTagLibrary.Builder に追加します。
         myAprilTagLibraryBuilder.addTag(55, "Our Awesome Team Tag", 3.5, DistanceUnit.INCH);

         // AprilTag ライブラリをビルドし、変数に割り当てます。
         myAprilTagLibrary = myAprilTagLibraryBuilder.build();

         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // タグライブラリを設定します。
         myAprilTagProcessorBuilder.setTagLibrary(myAprilTagLibrary);

         // AprilTag プロセッサをビルドし、変数に割り当てます。
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();


カスタムタグ - 変数を使用
~~~~~~~~~~~~~~~~~~~~~~~~~~

別の方法として、**Metadata** を変数に割り当て、その変数を使用して新しい**AprilTag** を作成できます。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      これら2つのブロックは、前の例の1つの新しいブロックを置き換えることができます。

      .. figure:: images/090-Blocks-add-Metadata.png
         :width: 75%
         :align: center
         :alt: 変数 Metadata

         変数を使用した Metadata の設定

      これらのブロックは分離されており、**Metadata** 変数は**Library Builder** で追加される前のどこででも初期化/割り当てできることを示しています。使用の直前に表示する必要はありません。

   .. tab-item:: Java
      :sync: java

      カスタムタグは**2行のコード** で追加され、前の例の**1行の新しいコード** を置き換えます。

      .. code-block:: java

         AprilTagMetadata myAprilTagMetadata;
         AprilTagLibrary.Builder myAprilTagLibraryBuilder;
         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagLibrary myAprilTagLibrary;
         AprilTagProcessor myAprilTagProcessor;

         // 新しい AprilTagLibrary.Builder オブジェクトを作成し、変数に割り当てます。
         myAprilTagLibraryBuilder = new AprilTagLibrary.Builder();

         // 指定された AprilTagLibrary からすべてのタグを AprilTagLibrary.Builder に追加します。
         // 現在のシーズンの AprilTagLibrary を取得します。
         myAprilTagLibraryBuilder.addTags(AprilTagGameDatabase.getCurrentGameTagLibrary());

         // 新しい AprilTagMetdata オブジェクトを作成し、変数に割り当てます。
         myAprilTagMetadata = new AprilTagMetdata(55, "Our Awesome Team Tag", 3.5, DistanceUnit.INCH);

         // タグを AprilTagLibrary.Builder に追加します。
         myAprilTagLibraryBuilder.addTag(myAprilTagMetadata);

         // AprilTag ライブラリをビルドし、変数に割り当てます。
         myAprilTagLibrary = myAprilTagLibraryBuilder.build();

         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // タグライブラリを設定します。
         myAprilTagProcessorBuilder.setTagLibrary(myAprilTagLibrary);

         // AprilTag プロセッサをビルドし、変数に割り当てます。
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();**Blocks** または**Java** の場合、複数のタグを複数の（より短い！）変数名（``myTag1`` 、``myTag2`` など）で追加できます。

上書き
~~~~~~

ライブラリに既に存在するタグと** 同じ ID コード** を持つカスタム**AprilTag** を作成する場合があります。これは** 上書き** であり、許可するかどうかを選択できます。

``setAllowOverwrite()`` が ``false`` （デフォルト）に設定されており、上書きが試みられると、**OpMode** は適切なエラーメッセージとともにクラッシュします。

``true`` に設定すると、カスタムタグが既存のタグを置き換えます。

なぜこれを行うのでしょうか？タグサイズが正確ではないとします。同じ**Metadata** で新しいタグを入力できますが、タグサイズを修正します。

または、独自のタグ名または距離単位を使用することを好む場合があります。

上級ユーザーは、** ゲームフィールド** 上の事前定義タグの** 位置** を指定したい場合があります。これは、オプションの**Vector** および**Quaternion** フィールドで行うことができます。

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

