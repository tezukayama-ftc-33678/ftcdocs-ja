AprilTag ライブラリ
====================

**FIRST** Tech Challenge の試合では、あなたの **OpMode** には検出すべき既知の **AprilTag** のセットがあります。これらは、デフォルトで事前にロードされるか、カスタムタグありまたはなしで、あなたが指定します。

これらのタグは **AprilTag ライブラリ** を形成します。各ライブラリタグには、**Metadata** ページで説明されている 4 ～ 6 個のプロパティのセットがあります。

このページでは、AprilTag ライブラリを作成する多くの方法を示します。**Initialization** ページでは、これが **OpMode** で AprilTag を使用するための準備のオプションの **ステップ 1** であることを説明しました。

AprilTag ライブラリの使用をマスターするために、**これらの例を順番に試してください**。

簡単な方法
~~~~~~~~~~

Let’s start with… no Library! If your OpMode will use only the current 
season defaults, no Library action is needed.

単に次のように **AprilTagProcessor** を作成します：

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
         myAprilTagProcessor = AprilTagProcessor.easyCreateWithDefaults();

AprilTag Processor を作成するには、ライブラリの指定が必要です。この「簡単な方法」でも、裏側でデフォルトライブラリが指定されています。
this “Easy Way” does specify the default Library, behind the scenes.

デフォルトライブラリ
~~~~~~~~~~~~~~~~~~~~

SDK は、事前定義された AprilTag の 2 つのコアライブラリを使用します：

-  Sample OpMode でのみ使用されるタグ
-  Robot Game（競技）でのみ使用されるタグ

最初のライブラリは ``SampleTagLibrary`` と呼ばれ、SDK 8.2 で利用可能になりました。その基本的なメタデータ値は次のとおりです：

-  ``583, Nemo, 4, DistanceUnit.INCH``
-  ``584, Jonah, 4, DistanceUnit.INCH``
-  ``585, Cousteau, 6, DistanceUnit.INCH``
-  ``586, Ariel, 6, DistanceUnit.INCH``

The second Library, called ``CenterStageTagLibrary``, is planned for
future competition only. It’s available now in SDK 8.2, but currently
holding three “placeholder” tags:

-  ``0, MEOW, 0.166, DistanceUnit.METER``
-  ``1, WOOF, 0.166, DistanceUnit.METER``
-  ``2, OINK, 0.166, DistanceUnit.METER``

2023 年 9 月のキックオフ後、これらは CENTERSTAGE の**実際のタグ**に置き換えられます（SDK 9.0 で）。

便宜上、3 番目のライブラリにはこれら 2 つのコアライブラリの**両方**が含まれており、それ以外は何もありません。これは ``CurrentGameTagLibrary`` と呼ばれるデフォルトです。

AprilTag Processor
~~~~~~~~~~~~~~~~~~

Processor の**あらゆる側面**を指定するには、**Processor Builder** を使用します。これには少なくとも 2 つのコマンドが必要です：

-  Java キーワード ``new`` を使用して Builder を作成します

-  機能を指定/追加した後、``.build()`` メソッドの呼び出しで完了します

In between these actions, your OpMode will add one of the three
Libraries directly to the Processor Builder. It’s easiest to use the
default ``CurrentGameTagLibrary``, containing all of the predefined
tags.

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      まず、``AprilTagProcessor.Builder`` ツールボックス（またはパレット）から最初のコンポーネントを取得し、``AprilTagLibrary`` ツールボックスから 2 番目のコンポーネントを取得して、この式を作成します。

      .. figure:: images/020-Blocks-setTagLibrary-CurrentGame.png
         :width: 75%
         :align: center
         :alt: Set Current Game Tag Library

         Setting Current Game Tag Library

      **これの前後に**、Processor Builder を **create** するブロックを 1 つと、``.build()`` でプロセスを **finalize** するブロックをもう 1 つ配置します。

      .. figure:: images/030-Blocks-ATprocessor-CurrentGame.png
         :width: 75%
         :align: center
         :alt: Completing Builder

         Completing Builder 

      これらは ``AprilTagProcessor.Builder`` ツールボックスの最初と最後のブロックです。残りのブロックは、Processor のオプション機能を設定するために使用されます。ここではライブラリのみを設定しています。

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

別の方法として、最初にライブラリを独自の変数名に保存することもできます。次に、AprilTag Processor のその名前を指定します。ここでは ``myAprilTagLibrary`` を使用します（他の名前でも問題ありません）。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      まず、``AprilTagLibrary`` ツールボックスから最初のコンポーネントを取得し、``AprilTagProcessor.Builder`` ツールボックスから 2 番目のコンポーネントを取得して、この式を作成します。

      .. figure:: images/040-Blocks-ATProcessor-Variable.png
         :width: 75%
         :align: center
         :alt: Set Tag Library

         Set the Tag Library

      前と同様に、**これの前後に**、Processor Builder を **create** するブロックを 1 つと、``.build()`` でプロセスを **finalize** するブロックをもう 1 つ配置します。

      .. figure:: images/050-Blocks-ATprocessor-CurrentGame-Variable.png
         :width: 75%
         :align: center
         :alt: Build the AprilTag Processor

         Build the AprilTag Processor

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


ライブラリ Builder とデフォルト
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next we try the Builder pattern, to create a Library containing only
predefined AprilTags. It’s not needed (nothing new to Build!), but it’s
an easy introduction.

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      -  Create a Library Builder, not the same as a Processor Builder.
      -  Then use the ``addTags`` Block – note the plural “tags”, not
         “tag”.
      -  Finalize the process with the ``.build`` command.

      ビルドされたライブラリは、ここでは ``myAprilTagLibrary`` と呼ばれる変数に割り当てまたは保存されます。

      .. figure:: images/060-Blocks-LibraryBuilder-CurrentGame.png
         :width: 75%
         :align: center
         :alt: Build the Tag Library

         Build the Tag Library

      次に、おなじみの手順が続きます：

      -  Processor Builder を作成します。
      -  次に、前のシーケンスでビルドして保存したライブラリを設定または追加します。
      -  ``.build`` コマンドでプロセスを完了します。

      .. figure:: images/070-Blocks-Processor-Variable.png
         :width: 75%
         :align: center
         :alt: Build the Tag Processor

         Build the Tag Processor

      最終結果は前の例と同じですが、ここでは Library Builder の使用方法を確認できます。

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
~~~~~~~~~~~~~~~~~~~~~~~

最後に、ライブラリにカスタムタグを追加する準備ができました。

各タグにはメタデータが必要です。次のように、メタデータ値を新しいタグに直接入力できます。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      3 番目のブロックは、カスタムタグをライブラリに追加します。他のすべてのブロックは前の例と同じです。

      .. figure:: images/080-Blocks-addTag.png
         :width: 75%
         :align: center
         :alt: Custom Tag Library

         Add custom tags to Tag Library

   .. tab-item:: Java
      :sync: java

      カスタムタグは **1 行の新しい**コードで追加されます。それ以外は前の例と同じです。

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

         // ポーズ情報なしで、タグを AprilTagLibrary.Builder に追加します。
         myAprilTagLibraryBuilder.addTag(55, "Our Awesome Team Tag", 3.5, DistanceUnit.INCH);

         // AprilTag ライブラリをビルドし、変数に割り当てます。
         myAprilTagLibrary = myAprilTagLibraryBuilder.build();

         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // タグライブラリを設定します。
         myAprilTagProcessorBuilder.setTagLibrary(myAprilTagLibrary);

         // AprilTag プロセッサをビルドし、変数に割り当てます。
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();


カスタムタグ - 変数
~~~~~~~~~~~~~~~~~~~

別の方法として、メタデータを変数に割り当てて、その変数を使用して新しい AprilTag を作成できます。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      これら 2 つのブロックは、前の例の単一の新しいブロックを置き換えることができます。

      .. figure:: images/090-Blocks-add-Metadata.png
         :width: 75%
         :align: center
         :alt: Variable Metadata

         Setting Metadata with Variable

      These Blocks are separated, to illustrate that the Metadata Variable can
      be initialized/assigned anywhere before being added with the Library
      Builder. It doesn’t have to appear immediately before use.

   .. tab-item:: Java
      :sync: java

      カスタムタグは **2 行**のコードで追加され、前の例の **1 行の新しい行**を置き換えます。

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
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();

Blocks または Java の場合、``myTag1``、``myTag2`` などの複数の（短い！）変数名を使用して、複数のタグを追加できます。

上書き
~~~~~~

ライブラリに既に存在するタグと**同じ ID コード**を持つカスタム AprilTag を作成する場合があります。これは**上書き**であり、許可するかしないかを選択できます。

``setAllowOverwrite()`` が ``false``（デフォルト）に設定されていて、上書きが試みられた場合、**OpMode** は適切なエラーメッセージでクラッシュします。

``true`` に設定すると、カスタムタグが既存のタグを置き換えます。

なぜこれを行うのでしょうか？タグのサイズが正しくないとします。同じメタデータを持つ新しいタグを入力できますが、タグサイズを修正します。

または、独自のタグ名や距離単位を使用することを好む場合があります。

上級ユーザーは、**ゲームフィールド上**の事前定義されたタグの**位置**を指定したい場合があります。これは、オプションの Vector フィールドと Quaternion フィールドで実行できます。

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

