フォーカス制御
--------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl`

「フォーカス長」と呼ばれる距離で、被写体の画像（光線）がレンズから収束して、Webcam センサー上に鮮明な画像を形成します。

Webcam でサポートされている場合、フォーカスは次の **FocusControl** メソッドで管理できます：

-  **setFocusLength(double focusLength)**
-  **getFocusLength()**

距離単位はここでは指定されていません。許可された範囲内の無次元値である場合があります。たとえば、Logitech C920 は 0 から 250 までの値を許可し、**より高い** 値は**より近い** オブジェクトにフォーカスします。

Webcam は、フォーカス長の最小値と最大値をサポートする場合があります。これらは次の方法で取得できます：

-  getMinFocusLength() 
-  getMaxFocusLength()

最小フォーカス長と最大フォーカス長の ``set()`` メソッドはありません。これらは Webcam のファームウェアにハードコードされています。ファームウェア設定は、同じ Webcam モデルの異なるバージョン間で異なる場合があることに注意してください。

これらおよび他のフォーカスメソッドは、露出について上記で説明したように、**FocusControl** オブジェクトで呼び出されます。
