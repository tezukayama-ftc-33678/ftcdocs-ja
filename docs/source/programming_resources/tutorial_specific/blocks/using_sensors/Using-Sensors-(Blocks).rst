センサーの使用 :bdg-warning:`Blocks`
=============================================

カラー距離センサー
~~~~~~~~~~~~~~~~~~~~~

センサーは、**Robot Controller** が環境に関する情報を取得できるようにするデバイスです。この例では、**REV Robotics** のカラー距離センサーを使用して、範囲（物体からの距離）情報を**DRIVER STATION** に表示します。

カラー距離センサーは、反射光を使用してセンサーから対象物体までの距離を判断します。比較的正確に近距離（最大5インチ以上）を測定するために使用できます。このドキュメントが最近編集された時点では、**REV** のカラー距離センサーは約2インチ（5cm）で飽和します。これは、2インチ以下の距離の場合、センサーは約2インチに等しい測定距離を返すことを意味します。

このタスクの完了には約15分かかります。

距離を表示するための Op Mode の変更手順
------------------------------------------------------

1. ラップトップが **Robot Controller** のProgram & Manage Wi-Fiネットワークにまだ接続されていることを確認します。

2. 「MyFIRSTOpMode」が編集用に開かれていることを確認します。開かれていない場合は、ラップトップのブラウザウィンドウの左上隅にある **FIRST** ロゴをクリックします。これにより、メインの**Blocks** 開発ツールプロジェクト画面に移動します。

.. image:: images/DistanceSensorStep2ControlHub.jpg
   :align: center

|

   まだ開かれていない場合は、「MyFIRSTOpMode」プロジェクトをクリックして編集用に開きます。

3. ブラウザの左側にある「Utilities」カテゴリをクリックします。「**Telemetry**」サブカテゴリを見つけてクリックします。

.. image:: images/DistanceSensorStep3ControlHub.jpg
   :align: center

|

4. 「call **telemetry.addData**」ブロック（数値版）を選択し、「while」ループブロック内の「**telemetry.update**」ブロックの直前の位置にドラッグします。

.. image:: images/DistanceSensorStep4ControlHub.jpg
   :align: center

|

5. 「key」テキストをクリックしてハイライトし、テキストを「Distance (cm)」に変更します。

.. image:: images/DistanceSensorStep5ControlHub.jpg
   :align: center

|

6. 「Sensors」カテゴリをクリックして展開します。「**REV Color/Range Sensor**」サブカテゴリをクリックします。「call**sensorColorRange.getDistance**」プログラミングブロックをクリックして選択します。

.. image:: images/DistanceSensorStep6ControlHub.jpg
   :align: center

|

   注：**Blocks** プログラミングツールの以前のバージョンでは、**REV Robotics** カラー距離センサーを「LynxI2cColorRangeSensor」と呼んでいました。ソフトウェアの新しいバージョンでは、デバイスを「**REV Color/Range Sensor**」と呼びます。

7. 「call **sensorColorRange.getDistance**」プログラミングブロックを「call**telemetry.addData**」プログラミングブロックの「number」フィールドにドラッグします。

.. image:: images/DistanceSensorStep7ControlHub.jpg
   :align: center

|

   これにより、ターゲットまでの測定距離がセンチメートル単位で **DRIVER STATION** に送信されます。

8. **Op Mode** を保存し、**Robot Controller** に正常に保存されたことを確認します。

.. image:: images/DistanceSensorStep8ControlHub.jpg
   :align: center

|

9. :doc:`Op Mode の実行 <../running_op_modes/Running-Your-Op-Mode>` セクションで説明されている手順に従って、更新された **Op Mode** を実行します。

.. image:: images/DistanceSensorStep9ControlHub.jpg
   :align: center

|

   **Op Mode** を実行中、カラー光センサーの上に手をかざすと、測定距離が**DRIVER STATION** 画面で変化するはずです。**DRIVER STATION** に「NaN」（数値ではない）という表現が表示される場合、ターゲットは範囲外である可能性が高いです（センサーは反射光を検出しません）。

タッチセンサー
~~~~~~~~~~~~~~

この例では、**REV Robotics** のタッチセンサーが**Robot Controller** のアクティブな構成ファイルでデジタルタッチセンサーとして構成されていると仮定します。「**isPressed**」プログラミングブロックを使用して、センサー上のボタンが現在押されているかどうかを判断します。

.. image:: images/REVTouchSensor.jpg
   :align: center

|

**Control Hub** または**Expansion Hub** のデジタルポートには、ポートあたり2つのデジタルピンが含まれています。4線JSTケーブルを使用して**REV Robotics** のタッチセンサーを**Control Hub** または**Expansion Hub** のデジタルポートに接続すると、タッチセンサーはポート内の2つのデジタルピンのうち2番目に配線されます。4線ケーブルの最初のデジタルピンは接続されません。

たとえば、タッチセンサーを **Control Hub** または**Expansion Hub** の「0,1」デジタルポートに接続すると、タッチセンサーはポートの2番目のピン（「1」とラベル付け）に接続されます。最初のピン（「0」とラベル付け）は接続されません。

このタスクの完了には約15分かかります。

ボタン（タッチセンサー）状態を表示するための Op Mode の変更手順
-------------------------------------------------------------------------

1. ラップトップが **Robot Controller** のプログラミングモードWi-Fiネットワークにまだ接続されていることを確認します。

2. 「MyFIRSTOpMode」が編集用に開かれていることを確認します。開かれていない場合は、ラップトップのブラウザウィンドウの左上隅にある **FIRST** ロゴをクリックします。これにより、メインの**Blocks** 開発ツールプロジェクト画面に移動します。

.. image:: images/TouchSensorOpModeStep2ControlHub.jpg
   :align: center

|

   まだ開かれていない場合は、「MyFIRSTOpMode」プロジェクトをクリックして編集用に開きます。

3. 「Logic」カテゴリをクリックします。「if do else」ブロックを見つけてクリックします。

.. image:: images/TouchSensorOpModeStep3ControlHub.jpg
   :align: center

|

4. 「if do else」ブロックを「**telemetry.update**」ブロックの前の位置にドラッグします。

.. image:: images/TouchSensorOpModeStep4ControlHub.jpg
   :align: center

|

5. 「Sensors」カテゴリをクリックして展開します（まだ展開されていない場合）。「Touch Sensor」サブカテゴリをクリックし、「.**isPressed**」ブロックを見つけて選択します。

.. image:: images/TouchSensorOpModeStep5ControlHub.jpg
   :align: center

|

6. 「**isPressed**」ブロックを「if do else」プログラミングブロックのテスト条件にドラッグします。

.. image:: images/TouchSensorOpModeStep6ControlHub.jpg
   :align: center

|

7. ブラウザの左側にある「Utilities」カテゴリをクリックします。「**Telemetry**」サブカテゴリを見つけてクリックします。

.. image:: images/TouchSensorOpModeStep7ControlHub.jpg
   :align: center

|

   「call **telemetry.addData**」ブロック（テキスト版）を選択し、「if do else」ブロックの「do」句にドラッグします。

8. 「key」値を「testTouch」に、「text」値を「is pressed」に変更します。

.. image:: images/TouchSensorOpModeStep8ControlHub.jpg
   :align: center

|

9. 別の「**telemetry.addData**」ブロック（テキスト版）を「if do else」ブロックの「else」句に挿入します。「key」値を「testTouch」に、「text」値を「is NOT pressed」に変更します。

.. image:: images/TouchSensorOpModeStep9ControlHub.jpg
   :align: center

|

10. **Op Mode** を保存し、**Robot Controller** に正常に保存されたことを確認します。

.. image:: images/TouchSensorOpModeStep10ControlHub.jpg
   :align: center

|

11. :doc:`Op Mode の実行 <../running_op_modes/Running-Your-Op-Mode>` セクションで説明されている手順に従って、更新された **Op Mode** を実行します。

.. image:: images/TouchSensorOpModeStep11ControlHub.jpg
   :align: center

|

   **Op Mode** を実行してボタンを押したり離したりすると、**DRIVER STATION** のテレメトリメッセージがデジタルタッチセンサーの現在の状態を反映して更新されるはずです。

