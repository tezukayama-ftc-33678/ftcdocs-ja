自動露出優先度
===============

**AE Priority** （自動露出優先度）は、特定の露出時間を選択する際にガイドとして使用できる設定です。

AE Priority を ``true`` に設定すると、カメラは手動で設定された露出時間をより重視し、同時にフレームレートをより柔軟に扱うことができます。これは、高速シャッタースピードが必要な場合（モーションブラーを削減するため）や、長い露出時間が必要な場合（暗い環境で）に役立ちます。

AE Priority を ``false`` に設定すると（デフォルト）、カメラはフレームレートをより重視し、露出時間を調整してフレームレートを維持します。

.. code:: java

   ExposureControl exposureControl;
   exposureControl = vuforia.getCamera().getControl(ExposureControl.class);
   exposureControl.setAePriority(true);  // または false

このメソッドは **SDK**7.0 で導入されました。これは**Vuforia** カメラでのみ機能します（**AprilTag** プロセッサーまたは TFOD プロセッサーと組み合わせて使用する場合）。

**VisionPortal** では、AE Priority は ``VisionPortal.Builder.setCameraMonitorViewId()`` を使用してカメラモニター（DS プレビュー）が有効になっている場合にのみ機能します。

実験によると、AE Priority が ``true`` に設定されている場合、より長い露出時間（約 40 ミリ秒まで）を設定できます。AE Priority が``false`` に設定されている場合（デフォルト）、露出時間は約 16 ミリ秒に制限されるようです。

注：露出時間の設定方法については、:doc:`露出制御 </programming_resources/vision/webcam_controls/exposure/control/control>` を参照してください。
