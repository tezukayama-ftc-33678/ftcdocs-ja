露出時間の設定
==============

露出時間は、カメラのセンサーが光にさらされる時間の長さです。露出時間が長いほど、より多くの光がセンサーに到達し、画像が明るくなります。

手動で露出時間を設定するには、次の手順を実行します：

1. 露出モードを手動に設定
2. 希望する露出時間（ナノ秒単位）を設定

.. code:: java

   ExposureControl exposureControl;
   exposureControl = vuforia.getCamera().getControl(ExposureControl.class);
   
   // 手動モードに設定
   exposureControl.setMode(ExposureControl.Mode.Manual);
   
   // 露出時間を 10 ミリ秒（10,000,000 ナノ秒）に設定
   exposureControl.setExposure(10, TimeUnit.MILLISECONDS);

現在の露出時間を取得するには：

.. code:: java

   long currentExposure = exposureControl.getExposure(TimeUnit.MILLISECONDS);

**サポートされる露出範囲を確認する：**

.. code:: java

   long minExposure = exposureControl.getMinExposure(TimeUnit.MILLISECONDS);
   long maxExposure = exposureControl.getMaxExposure(TimeUnit.MILLISECONDS);

** 重要な注意事項：**

- 露出時間はナノ秒単位で指定されますが、``TimeUnit`` を使用してミリ秒、マイクロ秒などの他の単位を使用できます。
- サポートされる露出範囲はカメラによって異なります。
- AE Priority が ``true`` に設定されている場合、より長い露出時間を設定できます。詳細については、:doc:`自動露出優先度 </programming_resources/vision/webcam_controls/exposure/auto_exposure/auto-exposure>` を参照してください。
