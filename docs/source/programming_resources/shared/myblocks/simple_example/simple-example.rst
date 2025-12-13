シンプルな例：**myGreeting** の作成
=========================================

「Hello World」（もちろん！）という挨拶を作成するシンプルな **myBlock** から始めます。

Wi-Fi 経由で **Control Hub** または RC スマートフォンに接続された Chrome ブラウザーを開きます。アドレス **http://192.168.43.1:8080**（CH）または **http://192.168.49.1:8080**（RC）にアクセスし、**OnBot Java** タブをクリックします。

.. note:: コンピューターは通常、一度に1つの Wi-Fi ネットワークにのみ接続できます。プログラミング中にこのチュートリアルに従うには、FTC Docs の PDF バージョンを使用してください。インターネットとプログラミングを同時に必要とする場合は、イーサネットケーブルをインターネットルーターに接続する**か**、USB Wi-Fi ドングルを追加してみてください。

大きな**プラス記号アイコン**をクリックして新しいファイルを開きます。**SampleMyBlocks.java** と呼びます。デフォルトの「teamcode」フォルダーの場所を使用します。Sample OpMode を選択せず、デフォルト設定の「Not an OpMode」を使用します。OK をクリックします。

.. image:: images/a0120-Hello-OBJ-circle.png

作業領域にシンプル/空の Java プログラムが表示されます。

.. image:: images/a0130-Hello-OBJ-empty.png

1行目はデフォルトのストレージフォルダー「teamcode」を示し、4行目は**クラス名**を示します（ファイル名と同じ）。これは ``public`` なので、他のクラスがアクセスできます。4行目の**左中括弧**と7行目の**右中括弧**に注意してください。すべてのコードをこれらの中括弧の間に配置します。

2つの順スラッシュマーク **//** は**コメント行**を示し、すべて Java ソフトウェアによって無視されます。優れたプログラマーは、チームメイトや**将来の自分**とコミュニケーションをとるために、多くのコメントを使用します！プログラムのすべての細部を覚えているわけではありません…大量にコメントを付けたことに後で感謝するでしょう！

   プログラミングに関する注意：**class** は、**objects**（クラスの例または**インスタンス**）で使用できる**メソッド**（アクション）と**フィールド**（プロパティ）を記述します。「dogs」というクラスには、メソッド「run」と「sleep」、およびフィールド「friendliness」と「appetite」が含まれる場合があります。ペットの Spot と Rover は、「dogs」クラスのオブジェクトまたはインスタンスです。

クラス名の後に、``extends BlocksOpModeCompanion`` と入力します。これは、新しいクラスを、より高い**スーパークラス**または**親**の**サブクラス**または**子**として宣言します。親クラス **BlocksOpModeCompanion** には、新しいサブクラスによって**継承**される便利なツールが含まれています。

.. image:: images/a0140-Hello-OBJ-extends-circle.png

その行を入力すると、OBJ ソフトウェアは**自動的**に ``import`` 文を作成し、親クラスを使用可能にします。便利です！

   プログラミングに関する注意：**BlocksOpModeCompanion** から継承されたクラスには、**OpMode**、**LinearOpMode**、**Telemetry**、**HardwareMap**、および **Gamepad** が含まれます。すべて非常に便利です！**myBlock** メソッドは、これらのクラスの**オブジェクト**または**インスタンス**を宣言せずに直接使用できます。以下に例を示します。

中括弧内に、次のように新しい行を入力します：

.. code:: java

   @ExportToBlocks (
          comment = "Here is a greeting for you.",
          tooltip = "Greet a person or group.",
          parameterLabels = {"Recipient"}
   )

これらは、新しい **myBlock** に表示されるオプションのラベルです。以下で説明します。これらの機能のいずれも使用したくない場合でも、 **アノテーション** 行 ``@ExportToBlocks`` は必要です。

そのアノテーションを入力すると、OBJ は自動的に ``import`` 文を追加しました。

これで、メソッド、つまり最初の **myBlock** を作成する準備が整いました。次の行を入力します：

.. code:: java

   public static String myGreeting (String greetingRecipient)  {
          return ("Hello " + greetingRecipient + "!");
   }

メソッドの名前は ``myGreeting`` です。これは ``public`` メソッドなので、他のクラスから使用または**呼び出す**ことができます。そして、これは ``static`` メソッドで、すべての **myBlock** メソッドに必要です。

このメソッドには、1つの入力または**パラメーター**があり、タイプは ``String``（テキスト）で、名前は ``greetingRecipient`` です。これは、挨拶の対象者または対象グループです。

メソッドには、1つの出力または**戻り値**もあります。タイプは ``String``（テキスト）です。出力値は、``return`` コマンドで記述されているように、文字「Hello」、続いてスペース、続いて入力されたパラメーター、続いて感嘆符です。

プログラムで、キーワード ``return`` が最初の文字位置にあることに注意してください。このサンプルではインデント（タブ）が使用されており、複数のレベルの中括弧がある場合にコードを読みやすくします。

また、プラス記号 ``+`` が3つのテキスト要素を結合または**連結**して、単一の ``String`` を形成していることにも注意してください。

**コードは完成しました！** 全体は次のようになります：

.. image:: images/a0150-Hello-OBJ-full-arrows.png

左上隅の Build Everything ボタンをクリックします。

.. image:: images/a0160-Hello-run-create-arrow.png

正常にビルドされるはずです。エラーがある場合は、上記のコードとまったく同じようにタイプミスがないか注意深く確認してください。大文字と小文字を区別し、引用符、セミコロン、中括弧を区別します。

正常にビルドされたら、**OnBot Java** から Chrome ブラウザーの **Blocks** タブに移動します。**Create New Op Mode** を選択するか、既存の OpMode を開いて編集します。

左側のメニューツールボックスで、**Java Classes** タブを選択します。

.. image:: images/a0170-Hello-run-menu-arrows.png

**SampleMyBlocks** サブメニューをクリックすると、新しい **myBlock** が表示されます！

.. image:: images/a0180-Hello-run-telemetry-circle.png

**myBlock** を作業領域にドラッグすると、入力ソケットにカーソルを合わせると、 **ツールチップ** 「Greet a person or group.」が表示されます。

.. image:: images/a0190-Hello-run-OpMode-circle.png

青い疑問符アイコンをクリックすると、 **コメント** 「Here is a greeting for you.」が表示されます。

.. image:: images/a0200-Hello-run-screenshot-circle.png

カスタムラベル「Recipient」が、灰色の入力ソケットの左側に表示されます。これらのオプション機能はすべて、Java コードのアノテーション ``@ExportToBlocks`` から取得されます。

ここで、このシンプルな **myBlock** の動作を確認するために、2つのコマンドで **Blocks** プログラムを作成できます：

.. image:: images/a0200-Hello-run-screenshot-circle.png

任意のテキストを入力できます。ボタン ``ABC`` をクリックして、それを入力します。この例では「World」を使用しています。

OpMode を保存して実行すると、**Driver Station** に挨拶が表示されます！

**おめでとうございます - 最初の myBlock が完成しました！**

.. note:: このチュートリアルでは、上記の Java コードを**手動で入力**することを意図しています。この例の事前入力されたテキストが必要な場合は、以下をクリックしてください。リンクされたコピーには、通常のクラス宣言とパッケージ/インポート文が含まれています。

.. dropdown:: サンプルコード

   :download:`SampleMyBlocks_v00.java <opmodes/SampleMyBlocks_v00.java>`

   .. literalinclude:: opmodes/SampleMyBlocks_v00.java
      :language: java

次の例では、上記の Java クラスにより多くの **myBlock** メソッドを追加します。それらは、ここで作成した SampleMyBlocks.java ファイルを編集して追加されます。
