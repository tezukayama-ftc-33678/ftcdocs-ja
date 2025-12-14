露出制御のサンプル
==================

以下は、露出制御を使用する方法の例です：

**例1：手動露出時間の設定**

.. code:: java

   ExposureControl exposureControl;
   exposureControl = vuforia.getCamera().getControl(ExposureControl.class);
   
   // 手動モードに設定
   exposureControl.setMode(ExposureControl.Mode.Manual);
   
   // 露出時間を 15 ミリ秒に設定
   exposureControl.setExposure(15, TimeUnit.MILLISECONDS);

**例2：サポートされる範囲の確認**

.. code:: java

   long minExp = exposureControl.getMinExposure(TimeUnit.MILLISECONDS);
   long maxExp = exposureControl.getMaxExposure(TimeUnit.MILLISECONDS);
   
   telemetry.addData("最小露出", "%d ms", minExp);
   telemetry.addData("最大露出", "%d ms", maxExp);

**例3：AE Priority を使用した長い露出時間**

.. code:: java

   // AE Priority を有効化
   exposureControl.setAePriority(true);
   
   // 手動モードに設定
   exposureControl.setMode(ExposureControl.Mode.Manual);
   
   // より長い露出時間（30 ミリ秒）を設定
   exposureControl.setExposure(30, TimeUnit.MILLISECONDS);

詳細については、:doc:`サンプル OpModes </programming_resources/vision/webcam_controls/samples/samples>` を参照してください。
