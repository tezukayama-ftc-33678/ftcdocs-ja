ホワイトバランス制御
---------------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl`

他のインターフェイスに続いて、**SDK** （バージョン 7.1 の新機能）は、ホワイトバランス制御のメソッドを提供します。

ホワイトバランスは、画像内の** 色温度** のバランスをとるデジタルカメラ設定です。色温度はケルビン度（K）の単位で測定され、光の物理的特性です。

たとえば、正午の日光は 5200-6000 K の間で測定されます。白熱電球（暖かい/オレンジ）の色温度は約 3000 K ですが、日陰（涼しい/青）は約 8000 K で測定されます。

自動で実行されると、ホワイトバランスは色温度を中立に戻すために、画像に反対の色を追加します。このインターフェイス **WhiteBalanceControl** により、色温度をユーザーが直接プログラムできます。

ここでは、ホワイトバランス温度を制御するために、Java タイプの整数で、ケルビン度の単位で単一の値が使用されます。メソッドは次のとおりです：

-  **setWhiteBalanceTemperature(int temperature)**
-  **getWhiteBalanceTemperature()**

露出やゲインと同様に、Webcam はホワイトバランス温度の最小値と最大値をサポートする場合があります。これらは次の方法で取得できます：

-  getMinWhiteBalanceTemperature()
-  getMaxWhiteBalanceTemperature()

最小温度値と最大温度値の ``set()`` メソッドはありません。これらは Webcam のファームウェアにハードコードされています。ファームウェア設定は、同じ Webcam モデルの異なるバージョン間で異なる場合があることに注意してください。

Logitech C920 Webcam の最小値は 2000、最大値は 6500 です。
