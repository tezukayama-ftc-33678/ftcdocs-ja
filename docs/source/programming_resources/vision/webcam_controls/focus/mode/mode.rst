フォーカス制御モード
------------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode`

Webcam は、さまざまなフォーカスモードのいずれかで動作する場合があります。フォーカス長を直接制御するには、Webcam を Fixed モードに設定します。

**SDK** は、**FocusControl.Mode** の次の値をサポートしています：

-  `Auto` 
-  `ContinuousAuto` 
-  `Fixed` 
-  `Infinity` 
-  `Macro` 
-  `Unknown`

モードは、これらの **FocusControl** メソッドで管理されます：

-  setMode(ExposureControl.Mode._mode_) 
-  getMode()

Logitech C920 Webcam は、**ContinuousAuto** と **Fixed** の2つのモードを提供し、**FocusControl** メソッドに応答します。Logitech C270（古いモデル）は **Fixed** モードのみを提供しますが、プログラムによる制御は許可されません。

詳細は、`FocusControl Javadoc <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/org/firstinspires/ftc/robotcore/external/hardware/camera/controls/FocusControl.html>`__ に記載されています。
