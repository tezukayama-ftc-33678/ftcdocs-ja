**myBlock** の編集
==================

**myBlock** の Java コードを編集して再ビルドする場合、**Blocks** **OpMode** でその **myBlock** を** 置き換える** 必要がある場合があります。これは、**myBlock** の表示または外部機能（アノテーションフィールド、入力パラメーター、または返される出力）を変更するかどうかによって異なります。

Java の変更が外部機能に影響する場合、更新された **myBlock** は **Blocks** の Java Classes メニューからのみ使用できます。**OpMode に既に配置されている** そのような **myBlock** は古くなっており、**Blocks 警告** が生成される可能性があります。新しい **myBlock** に置き換えてください。場合によっては、トップレベルの **Blocks** リストから **OpMode** を再度開く必要があります。

.. image:: images/a0260-editing-error-Blocks.png

編集が **myBlock** の** 内部** 処理のみに影響する場合、「Build Everything」の後、Java Classes メニューからの新しい置き換えを必要とせずに自動的に更新される可能性があります。場合によっては、**Blocks** 画面で Save OpMode をクリックする必要さえない場合があります。**Driver Station** で INIT と Start を使用して **OpMode** を再実行するだけです。これにより、**myBlock** へのマイナーまたは内部の変更を非常に高速にテストできます。

いずれの場合も、**myBlock** 名に **myGreeting_v01** などの** バージョン** を追加することを検討してください。編集する前にコピーして貼り付けて、関連するすべての **myBlock** メソッドを** 同じ Java クラス** に保持します。**Blocks** では、一意に名前が付けられたすべてのバージョンが、その単一のクラス名の下の Java Classes メニューで使用できます。

クラス名は **MyBlocks、SampleMyBlocks、Team8604MyBlocks、DrivingMyBlocks** などのように** 短く汎用的** に保ちます。上記の簡単な例のように **myBlock** ごとに1つではなく、すべてまたは多くの関連する **myBlocks** が含まれます。

その単一のクラスでは、各 **myBlock** メソッドは独自のアノテーション ``@ExportToBlocks`` の後に表示される必要があります。そのクラスには、**myBlocks** ではない他のメソッドが含まれている場合があります。**myBlock** ではないメソッドの前にアノテーションを省略します。そのようなメソッドは、変数の初期化に使用されるか、1つ以上の **myBlocks** によって呼び出される（共有）サブメソッドである可能性があります。例は :ref:`こちら <programming_resources/shared/myblocks/method_example/method-example:example: non-myblock methods>` に示されています。

このチュートリアルでは、これまでに次の基本要件を説明しました：
- **org.firstinspires.ftc.teamcode** フォルダー/パッケージに作成/保存
- クラスは **BlocksOpModeCompanion** を** 拡張** する
- 各 **myBlock** メソッドにはアノテーション **@ExportToBlocks** が必要
- メソッドは **public** および **static** である必要があります（abstract であってはなりません）
- 外部編集後に **myBlocks** を置き換える

このチュートリアルの残りの部分では、**OnBot Java で再入力** して **Blocks でテスト** できる** 例** を示します。変更を加えて機能を追加してみてください！
