ホワイトバランス制御モード
--------------------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode`

このインターフェイスは、**WhiteBalanceControl.Mode** の3つの値をサポートしています：

-  AUTO
-  MANUAL
-  UNKNOWN

カラーバランス温度を直接制御するには、Webcam を Manual モードに設定します。モードは、これらの **WhiteBalanceControl** メソッドで管理されます：

-  **setMode(WhiteBalanceControl.Mode.MODE)**
-  **getMode()**

Logitech C920 は、ホワイトバランス制御のデフォルトとして Auto モードになっており、前のセッションで Manual に設定された後でも、新しいセッションでは Auto に戻ります。他の **CameraControl** 設定では、一部の Webcam はデフォルト値に戻り、一部は最後にコマンドされた値を保持します。
