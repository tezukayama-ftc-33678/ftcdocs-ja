ハードウェアの例：サーボの制御
=================================

ここでは、**myBlock** が**ロボットハードウェア**にアクセスする方法を示す非常に簡単な例を示します。ここで、**Blocks** ユーザーはサーボの名前を **myBlock** の**パラメーター**として入力します。

.. image:: images/a0300-wiggle-OBJ-short.png


.. dropdown:: サンプルコード

   :download:`SampleMyBlocks_v01.java <opmodes/SampleMyBlocks_v01.java>`

   .. literalinclude:: opmodes/SampleMyBlocks_v01.java
      :language: java

10-11行目には、 **「+」** 文字で結合されて **単一のテキスト文字列** を形成する2つのテキスト文字列（それぞれ引用符内）が含まれています。これは、コメントフィールドが「改行」なしで **単一行** のテキストである必要があるという要件を満たす別の方法です。短い文字列により、横にスクロールすることなく、すべてのテキストを画面上に表示できます。

15行目：このメソッドには3つの入力があり、出力はありません（キーワード **void**）。

17行目は、**BlocksOpModeCompanion** から提供される構成されたデバイスリストである **hardwareMap** にアクセスする方法を示しています。その単一の Java 行は次のことを行います：
- myServo という新しい変数を、型（クラス）Servo として宣言します
- hardwareMap から名前付きサーボのプロパティ（メソッドと変数）を**取得**します
- それらのプロパティを新しい変数 myServo に割り当てます

20行目は **for ループ**で、`こちら <https://www.w3schools.com/java/java_for_loop.asp>`__ または `こちら <https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html>`__ で学習できます。指定された期間とサイクル数を使用して、指定されたサーボを前後に動かします。この **for ループ**には、**OpMode** が停止されていないことを監視および検証するための追加条件 ``opModeIsActive()`` があります。

22行目と24行目：オブジェクト myServo は、Servo クラスのメソッド ``setPosition()`` を使用します。

23行目と25行目：オブジェクト linearOpMode は、**BlocksOpModeCompanion** から継承されたクラスのメソッド ``sleep()`` を使用します。

**Blocks** ユーザーは、**アクティブな構成**から正確なデバイス名を入力する必要があります。ハードウェアデバイス名（モーター、サーボ、センサー）は、RC アプリまたはペアリングされた DS アプリの Configure Robot メニューにあります。または、これらのデバイスタイプを含む任意の **Blocks** ドロップダウンリストから名前を再入力する方が簡単な場合があります。たとえば、緑色の Servo **Set** ブロックのドロップダウンリストです。

.. image:: images/a0320-wiggle-Blocks-use-only.png

このサンプル myBlock は、**Blocks** メニューの Java Classes をクリックし、次に SampleMyBlocks サブメニューをクリックして見つけることができます。

注：**OnBot Java** でのタイプミスやその他のエラーにより、Java Classes メニューに myBlock が表示されない場合があります。これは、**Blocks** の **Settings** メニューオプション Advanced > Developer Options を有効にすることで修正できます。次に、Browser Console から診断情報を読み取ります（以下のリンクを参照）。

詳細については、**Blocks** `Programming
Tutorial <https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Writing-an-Op-Mode-with-FTC-Blocks>`__ で、「ステップ12：Java クラスに属するブロック」を参照してください。

ここに Blocks OpMode 全体があります。**Blocks** エディターの Java Classes タブに myBlock を配置できます。

.. image:: images/a0310-wiggle-Blocks-v01.png

.. note:: このチュートリアルでは、上記の Java コードを**手動で入力**することを意図しています。この例の事前入力されたテキストが必要な場合は、上記の折りたたみ可能な**サンプルコード**セクションをクリックしてください。リンクされたコピーには、通常のクラス宣言とパッケージ/インポート文が含まれています。

**次の例に進む前に**、ここでコードを **OnBot Java** に入力し、**Blocks** でテストしてください。正常に動作するようになったら、**Blocks** の OpMode を保存し、上記のバージョンを簡単に復元できるように、わかりやすい名前を付けます。
