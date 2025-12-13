露出モード
==========

露出モードは、カメラが画像の明るさをどのように調整するかを決定します。

**自動露出** モードでは、カメラがシーンに基づいて露出時間を自動的に調整します。このモードは、照明条件が変化する場合や、カメラが異なる場所を見ている場合に便利です。

**手動露出** モードでは、特定の露出時間を設定できます。このモードは、一貫した画像品質が必要な場合や、カメラが静的なシーンを見ている場合に役立ちます。

露出モードを設定するには、次のコードを使用します：

.. code:: java

   ExposureControl exposureControl;
   exposureControl = vuforia.getCamera().getControl(ExposureControl.class);
   
   // 手動モードに設定
   exposureControl.setMode(ExposureControl.Mode.Manual);
   
   // または自動モードに設定
   exposureControl.setMode(ExposureControl.Mode.Auto);

露出モードを取得するには：

.. code:: java

   ExposureControl.Mode currentMode = exposureControl.getMode();

**注意** ：手動露出時間を設定する前に、まず手動モードに切り替える必要があります。詳細については、:doc:`露出制御 </programming_resources/vision/webcam_controls/exposure/control/control>` を参照してください。
