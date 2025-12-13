Webcam の評価
----------------------

特定の Webcam のファームウェアは、ここで説明されている特定の機能をサポートする場合としない場合があります。**SDK** は、Webcam にクエリを実行したり、有効な応答が利用可能かどうかを示す値を返したりするいくつかのメソッドを提供します。

露出サポート
~~~~~~~~~~~~~~~~

露出および特定の露出モードをクエリする2つのメソッドを次に示します：

-  **isExposureSupported()**
-  **isModeSupported(ExposureControl.Mode._mode_)**

   -  *mode* には、テストしている特定のモード名を入力します

次のメソッドでは、露出が利用できない場合、long 型の ``unknownExposure`` というフィールドが返されます：

-  **getExposure(TimeUnit.MILLISECONDS)**
-  **getMinExposure(TimeUnit.MILLISECONDS)**
-  **getMaxExposure(TimeUnit.MILLISECONDS)**

露出とモードを設定するメソッドは、Boolean を返すこともできます。おそらく、操作が成功したかどうかを示しています。オプションの例として：

- ``wasExposureSet =  setExposure(25);`` 
- ``wasExposureModeSet = setMode(ExposureControl.Mode.Manual)``

同様に、AE Priority 機能も Boolean を返すことができます。例：

- ``wasAEPrioritySet =  setAePriority(true);``

ゲインサポート
~~~~~~~~~~~~

ゲインを設定するメソッドは、操作が成功したかどうかを示す Boolean を返すこともできます。オプションの例として：

- ``wasGainSet =  setGain(25);``

ホワイトバランスサポート
~~~~~~~~~~~~~~~~~~~~~

温度とモードを設定するメソッドは、操作が成功したかどうかを示す Boolean を返すこともできます。オプションの例として：

-  ``wasTemperatureSet = setWhiteBalanceTemperature(3000);``
-  ``wasWhiteBalanceModeSet = setMode(WhiteBalanceControl.Mode.MANUAL);``

フォーカスサポート
~~~~~~~~~~~~~

フォーカスおよび特定のフォーカスモードをクエリする2つのメソッドを次に示します：

- **isFocusLengthSupported()**
- **isModeSupported(FocusControl.Mode._mode_)**

次のメソッドは、要求されたフォーカス値が利用できない場合、**負の値**を返します。たとえば、Logitech C270 と Microsoft LifeCam VX-5000 は -1 を返します。Javadoc には、double 型の ``unknownFocusLength`` フィールドについても記載されています。

- getFocusLength() 
- getMinFocusLength() 
- getMaxFocusLength()

フォーカス長とモードを設定するメソッドは、おそらく操作が成功したかどうかを示す Boolean を返すこともできます。オプションの例として：

- ``wasFocusSet =  setFocusLength(25);`` 
- ``wasFocusModeSet = setMode(FocusControl.Mode.Fixed)``

PTZ サポート
~~~~~~~~~~~

パン/チルトペアとズーム値を設定するメソッドは、おそらく操作が成功したかどうかを示す Boolean を返すこともできます。オプションの例として：

- ``wasPanTiltSet =  setPanTilt(myHolder);``
- ``wasZoomSet = setZoom(3)``

PTZ の get() メソッドでは、一部の Webcam はサポートされていない値に対して単に**ゼロを返す**だけです。

いくつかの注意事項
------------

-  **SDK** は、`UVC 標準 <https://en.wikipedia.org/wiki/USB_video_device_class>`__ に準拠する Webcam をサポートしています

   -  多くの非 UVC Webcam は、UVC 認証がなくても、競技会でうまく機能します
   -  一部の非 UVC Webcam は Configure Robot にリストされますが、実行時に RC アプリをクラッシュさせます

-  Webcam は、プラグを抜いても、割り当てられた露出モードまたはフォーカスモードを保持する場合があります

   -  常に現在のモードを確認してください

-  特定の露出値の場合、あるモードのプレビューは、別のモードのプレビューとは大きく異なる場合があります
-  一部の Webcam は、**サポートされていないモード**を **accept** / ``set()`` し、**confirm** / ``get()`` します
-  Logitech C270 のプレビューは、露出 655 まで**明るく**なり、656 で**暗く**なります

   -  この Webcam の最小値は 0、最大値は 1000 です。

-  Logitech V-UAX16 のプレビューは、露出 = 0 で正常に見えますが、30-40 まで**暗く**なります
-  Logitech C920 の**ゲイン**値（0-255）は、プレビュー品質に大きく影響し、**露出**（0-204）に匹敵します
-  Webcam **OpMode** がクラッシュした後、RC アプリの再起動が必要になる場合があります
-  ファームウェアバージョンは、同じモデル番号の Webcam 間で異なる場合があります

最後に、ここでの一部の機能は、`OpenCV <https://opencv.org/>`__ や `EasyOpenCV <https://github.com/OpenFTC/EasyOpenCV>`__ などの外部ライブラリの助けを借りて実装または強化される可能性があります。その可能性は、この基本チュートリアルでは説明されていません。別のチュートリアルでは、**Blocks** と **OnBot Java** での `外部ライブラリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/External-Libraries-in-OnBot-Java-and-Blocks>`__ の一般的な使用について説明しています。
