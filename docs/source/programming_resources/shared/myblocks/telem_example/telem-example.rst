例：**Telemetry** 設定の変更
==================================

**Telemetry**メッセージは、デフォルトでは**Robot Controller**から**Driver Station**に** 毎秒最大4回**送信されます。この最大更新レートは**Android Studio**または**OnBot Java**で変更できますが、通常の**Blocks**では変更** できません**。**myBlock** を使用すれば、この機能も提供できます！

この簡単な例では、**Blocks** ユーザーが標準の時間間隔を 250 ミリ秒から他の間隔に変更できます。

.. image:: images/a0600-Telemetry-interval.png

時間間隔を短くすると、センサーまたはエンコーダーデータの更新を高速化できます。間隔を長くすると、RC-DS 通信帯域幅の負荷を軽減できます。

メソッドのみの Java コードは次のとおりです：

.. image:: images/a0610-Telemetry-interval-Blocks.png

.. note:: このチュートリアルでは、上記の Java コードを**手動で入力** することを意図しています。この例の事前入力されたテキストが必要な場合は、以下をクリックしてください。リンクされたコピーには、通常のクラス宣言とパッケージ/インポート文が含まれています。

.. dropdown:: サンプルコード

   :download:`W_myBlocks.java <opmodes/W_myBlocks.java>`

   .. literalinclude:: opmodes/W_myBlocks.java
      :language: java


これが実際に機能することを確認したいですか？別の、やや高度な **myBlock**により、**Telemetry**更新間の時間を測定できます。以下に投稿されています。その**myBlock**は、以下に添付されているような**Blocks**プログラムで使用できます。生の**.blk ファイル**をダウンロードし、メインの**Blocks**メニューで**Upload Op Mode** ボタンをクリックしてください。すべてのコメントと指示をお読みください。

.. dropdown:: サンプルコード

   :download:`W_myBlocks_Telemetry_v02.java <opmodes/W_myBlocks_Telemetry_v02.java>`

   :download:`W_Telemetry_myBlocks_v02.blk <opmodes/W_Telemetry_myBlocks_v02.blk>`

   .. literalinclude:: opmodes/W_myBlocks_Telemetry_v02.java
      :language: java
