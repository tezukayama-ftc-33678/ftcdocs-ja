パンとチルト
=============

Webcam は通常、パンとチルトの値を*ピクセル*（Webcam センサーによる画像キャプチャの最小単位）で表現しません。たとえば、Logitech C920 と Microsoft LifeCam VX-5000 の範囲は +/-36,000 ユニットで、各軸のピクセル数よりもはるかに大きくなっています。

Webcam は、パンとチルトを (x, y) 値のペアとして受け入れます。したがって、**SDK** のパンおよびチルトメソッドは、これらの値を **PanTiltHolder** という名前の特別なクラスで** ペアとしてのみ** 処理します。このクラスには、整数型の pan と tilt という2つのフィールドがあります。

基本メソッドの使用を説明する例を次に示します：

.. code:: java

   myHolder.pan = 5;                  // pan フィールドを割り当てる
   myHolder.tilt = 10;                // tilt フィールドを割り当てる
   myPtzControl.setPanTilt(myHolder);         // (x, y) ペアで Webcam にコマンドを送る

Webcam から値を取得するには：

.. code:: java

   newHolder = myPtzControl.getPanTilt();      // Webcam から (x, y) ペアを取得
   int currentPanValue = newHolder.pan;        // pan 値にアクセス
   int currentTiltValue = newHolder.tilt;      // tilt 値にアクセス

上記の例では、これらのオブジェクトが既に存在することを前提としています：

.. code:: java

   PtzControl myPtzControl = vuforia.getCamera().getControl(PtzControl.class); // PTZ Webcam 制御オブジェクトを作成
   PtzControl.PanTiltHolder myHolder = new PtzControl.PanTiltHolder();         // 入力ホルダーオブジェクトをインスタンス化
   PtzControl.PanTiltHolder newHolder;                                 // 出力ホルダーオブジェクトを宣言

Webcam は、許可された最小および最大のパン/チルトペア値をサポートする場合があります。上記の制御オブジェクトのガイドラインに従って、これらは次のように取得できます：

-  ``minPanTiltHolder = getMinPanTilt();`` 
-  ``maxPanTiltHolder = getMaxPanTilt();``

最小および最大のパン/チルト値の ``set()`` メソッドはありません。これらは Webcam のファームウェアにハードコードされています。ファームウェア設定は、同じ Webcam モデルの異なるバージョン間で異なる場合があることに注意してください。

これらのパンおよびチルトメソッドは、露出について上記で説明したように、**PtzControl** オブジェクトで呼び出されます。
