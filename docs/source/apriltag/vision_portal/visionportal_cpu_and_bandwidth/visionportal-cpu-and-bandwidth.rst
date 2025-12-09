VisionPortal の CPU と帯域幅
==============================

はじめに
------------

ビジョン処理は、重要な **CPU リソース** とUSB通信 **帯域幅** を消費する可能性があります。このような制限に達すると、プレビューに影響を与え、**OpMode** または **Robot Controller** が遅くなったり、フリーズしたり、クラッシュしたりする可能性があります。

チームは、より高い解像度と速度（フレーム毎秒）の利点と、CPUおよび帯域幅リソースの過負荷リスクとのバランスを取ることができます。

8.2 SDKは、このバランスを管理するための多数のツールを提供します：

- RCプレビュー（**LiveView** と呼ばれる）を無効化および有効化 - 「レベル1」
- **AprilTag**（またはTFOD）プロセッサを無効化および有効化 - 「レベル2」
- カメラストリームを停止および再開 - 「レベル3」
- **VisionPortal** を閉じる - 「レベル4」
- フレーム毎秒（FPS）を監視
- 圧縮ビデオストリーミング形式を選択
- カメラの解像度を選択
- デシメーション（ダウンサンプリング）を設定
- 姿勢ソルバーアルゴリズムを選択
- **AprilTag Processor** からすべてまたは新しい検出のみを取得
- TFOD Processorからすべてまたは新しい認識のみを取得

最初の4つのアクションは、利点と応答について非公式に評価されています：

- **LiveView** 「レベル1」：使用されるリソースの削減効果は一部、停止後の再開が非常に高速
- **プロセッサ** 「レベル2」：使用されるリソースの削減効果がより大きい、停止後の再開が高速
- **カメラストリーム** 「レベル3」：使用されるリソースの削減効果が高い、停止後の再開が比較的遅い
- **VisionPortal** 「レベル4」：使用されるリソースの削減効果が最大、停止後は再開しない

カメラステータス
-------------

ビジョン処理リソースを管理するツールについて説明する前に、利用可能な**カメラ状態**を再確認する必要があります。これは、最適化の取り組みを監視、評価、トラブルシューティングするのに役立つ可能性があります。

**Camera Controls** ページから繰り返しますが、これらのカメラ状態が現在利用可能です：

- OPENING_CAMERA_DEVICE - ビジョン処理は行われていません。
- CAMERA_DEVICE_READY - カメラが開いています。EOCV（フレームの取得と色変換の実行）からのバックグラウンド処理を含め、処理は行われていません。``resumeStreaming()`` を呼び出す準備ができています。
- STARTING_STREAM - 処理は行われていません。
- STREAMING - フレームが処理（**AprilTag** および/またはTFOD認識）およびプレビュー（**LiveView** RCプレビューおよびDS Camera Stream）に利用可能です。
- STOPPING_STREAM - 処理が行われている場合と行われていない場合があります。このステータスの後に ``CAMERA_DEVICE_READY`` が続きます。
- CLOSING_CAMERA_DEVICE - 処理は行われていません。
- CAMERA_DEVICE_CLOSED - 何も実行されておらず、USB通信は閉じています。閉じた後は、この **OpMode** 中にカメラを再度開かないでください。
- ERROR

これらの **enum** は、カメラを開く（新規ビルド）、ストリーミングを開始または再開する、ストリーミングを停止する、**VisionPortal** を閉じる、という順序でリストされています。

上記のすべては、**AprilTag** および/またはTFODプロセッサのステータスとは完全に別です。これらはいつでも有効または無効にできますが、カメラ画像を実際に処理するには当然 ``STREAMING`` ステータスが必要です。

プレビューについて
--------------

**Previews** ページで述べたように、**LiveView** は **Robot Controller** プレビューのみを指します。これは **Driver Station** (DS) **Camera Stream** とは完全に別物で、**LiveView** が停止されていても（手動または自動で）通常通り動作します。

DS Camera Streamは独自のフレーム収集プロセスを使用しますが、これは当然カメラ/パイプラインのステータスが ``STREAMING`` である必要があります。

DS Camera Streamを表示する手順は、
:ref:`ftc-docs <hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam:image preview>`
に示されています。

DS Camera Streamは、新しいMultiPortal機能の下でも、1台のカメラの画像のみを表示できます。チームは、マッチのセットアップに必要な場合、一方のカメラの画像または他方のカメラの画像を表示するための専用 **OpMode** を作成できます。

補足：SDK 8.2では、「LiveView」がRCプレビューの新しい統一名称になりました。古い名前の2つのインスタンスが残っています：

- ``myVisionPortalBuilder.enableCameraMonitoring(true);``（以下で説明）
- 停止時にプレビューステータスウィンドウに ``VIEWPORT`` が表示される

LiveView の一時停止 - 直接
-----------------------

CPUリソースを節約する1つの方法（「レベル1」）は、**OpMode** の実行中に **LiveView** を**直接一時停止**することです。CPUは **AprilTag** および/またはTFOD認識のためにカメラ画像の処理を続けますが、実際にはRCプレビュー画像（ビデオ）を生成しません。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      これらは ``Vision`` カテゴリの下にある ``VisionPortal`` ツールボックスまたはパレットにあります。

      .. figure:: images/050-Blocks-LiveView-toggle.png
         :width: 75%
         :align: center
         :alt: Toggle LiveView

         LiveView切り替えの例

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         // ライブビュー（RCプレビュー）を一時的に停止します。
         myVisionPortal.stopLiveView();

         // ライブビュー（RCプレビュー）を再度開始します。
         myVisionPortal.resumeLiveView();  

これらの「stop」と「resume」アクションは迅速に行われるため、**OpMode** はここでカメラステータスの **enum** を処理する必要は**ありません**。

上記のコマンドは **LiveView** のみを切り替えます。DS Camera Streamプレビュー（タッチして更新）は引き続き利用可能です。

LiveView の一時停止 - 間接
-------------------------

SDKは、**Blocks** とJavaで利用可能な **LiveView** の**間接的な**制御も提供します：

.. code-block:: java

   builder.setAutoStopLiveView(true)

この設定により、両方のプロセッサ（**AprilTag** とTFOD）が無効化されている場合、**LiveView** が**自動的に**停止します。Builderパターンの一部であるため、この機能は **OpMode** 中に直接 ``true`` と ``false`` を切り替えることはできません。

この設定は、**両方の**プロセッサが無効化されたときにトリガーされます。デフォルトで ``false`` に設定されている場合、モニターは注釈なしでカメラのビューを表示し続けます。``true`` に設定されている場合、モニターは自動一時停止され、プロセッサが有効になっていない場合は単色のオレンジ色の画面が表示されます。したがって、このAutoPause機能を使用してプレビューを効果的にオン/オフ**できます**。

1つまたは両方のプロセッサが再有効化されると、**LiveView** が再開されます。この設定は **LiveView** のみに影響します。**Driver Station** Camera Streamプレビューは引き続き利用可能です。

LiveView を無効化
----------------

SDKには、**Blocks** とJavaで利用可能な、**LiveView** を**一般的に**許可（または禁止）する別のBuilder設定も含まれています：

.. code-block:: java

   builder.enableLiveView(true);

サンプル **OpMode** は、デフォルトでこのBuilderフィールドを ``true`` に設定します。

**OpMode** が **LiveView** プレビューをまったく必要としない場合、これを ``false`` に設定できます。Builderパターンの一部であるため、この機能は **OpMode** 中に直接 ``true`` と ``false`` を切り替えることはできません。

プロセッサの切り替え
-----------------

CPUリソースを節約するもう1つの方法（「レベル2」）は、**OpMode** の実行中に **AprilTag またはTFOD Processor を無効化**することです。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      これらは ``Vision`` カテゴリの下にある ``VisionPortal`` ツールボックスまたはパレットにあります。

      .. figure:: images/060-Blocks-Processor-toggle.png
         :width: 75%
         :align: center
         :alt: Toggle Processor

         プロセッサ切り替えの例

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         // AprilTagプロセッサを有効または無効にします。
         myVisionPortal.setProcessorEnabled(myAprilTagProcessor, true);

         // TensorFlow Object Detectionプロセッサを有効または無効にします。
         myVisionPortal.setProcessorEnabled(myTfodProcessor, true);

Disabling a Processor does not close LiveView, with its own controls described
above.  Any annotations will stop appearing in the preview.

Disabling and re-enabling processors is very fast, and saves CPU resources.
But EOCV frame pulling and color conversion continue running in the background.

カメラストリームの切り替え
--------------------

CPUリソースを節約するより積極的な方法（「レベル3」）は、**OpMode** の実行中に**カメラストリームを停止**することです。これは当然、レベル1と2も達成します：**LiveView** を停止し、**AprilTag** およびTFOD Processorの動作を防ぎます。DS Camera Streamは新しいスナップショットを提供しません。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      これらは ``Vision`` カテゴリの下にある ``VisionPortal`` ツールボックスまたはパレットにあります。

      .. figure:: images/080-Blocks-Streaming-toggle.png
         :width: 75%
         :align: center
         :alt: Toggle Camera Stream

         カメラストリーム切り替えの例

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         // ストリーミングセッションを一時的に停止します。これによりCPU
         // リソースを節約でき、必要に応じて迅速に再開できます。
         myVisionPortal.stopStreaming();

         // 以前に停止した場合、ストリーミングセッションを再開します。
         myVisionPortal.resumeStreaming();

ストリームの停止（および後での再開）は若干リスクがあり、約1秒かかる可能性があり、すべてのバックグラウンド処理を停止します。これは、``SwitchableCameras`` と呼ばれるサンプル **OpMode** でカメラを切り替えるときに発生することです。1つのストリームが停止し、もう1つのストリームが開始します。

VisionPortal を閉じる
------------------

``close()`` でポータルを閉じると、すべてのバックグラウンド処理が永続的に停止し（「レベル4」）、カメラとのUSB通信が閉じられます。

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      これらは ``Vision`` カテゴリの下にある ``VisionPortal`` ツールボックスまたはパレットにあります。

      .. figure:: images/100-Blocks-close-VisionPortal.png
         :width: 75%
         :align: center
         :alt: Close VisionPortal

         VisionPortalを閉じる例

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         // 不要になった場合、いつでもVisionPortalを閉じてコンピューティングリソースを
         // 節約します。
         myVisionPortal.close();

``close()`` プロセスは、すべてのカメラ処理の「破棄」です。同じ **OpMode** 内で別の **VisionPortal** をビルドしてカメラを「再オープン」することは推奨されません。これはリスクがあり、数秒かかる可能性があります。

したがって、SDKは対応する ``reopen()`` または ``resume()`` メソッドを提供していません。

``close()`` プロセスは、任意の **OpMode** の最後に自動的に行われます。

``close()`` を呼び出す前に ``stopStreaming()`` を呼び出すことは（明確にするために）許可されていますが、必須ではありません。``close()`` は該当する場合、内部的に ``stopStreaming()`` を呼び出すためです。

高速切り替え
--------------

**OpMode**（または手動テスト）は、上記で説明した「オン」と「オフ」のアクションを高速で積み重ねることを避けるか、処理する必要があります。

ステータスが ``STOPPING_STREAM`` の間に ``resumeStreaming()`` を呼び出すことは合法です。ただし、停止操作が完了するまでプログラムは**ブロック**されます。

**ブロッキング**とは、最新の関数がすぐに戻らないことを意味します。したがって、コードは ``sleep()`` コマンドを実行しているかのように、一時的にそこで「スタック」します。

ステータスが ``STARTING_STREAM`` の間に ``stopStreaming()`` を呼び出す場合も同様です。これは許可されていますが、コードは待機する必要があるかもしれません。

ブロッキングを避けるには、前の操作が完了していることを確認するために、関連する**ステータス enum** をチェックするのが最善です。これは、線形 **OpMode** で空の ``while()`` ループを使用して行うことができます。

CPU管理の選択肢
----------------------

これまでのところ、上記で説明したビジョンプロセス制御のみを使用して、CPUパフォーマンスを評価するための**10の可能な構成**があります：

- **VisionPortal** が閉じている
- **VisionPortal** が開いている、ストリーミングオフ

次に、ストリーミングオン、プレビューオフで4つ：

- **AprilTag** プロセッサのみが有効
- TFODプロセッサのみが有効
- 両方が有効
- 両方が無効

次に、ストリーミングオン、プレビューオンで4つ：

- **AprilTag** プロセッサのみが有効
- TFODプロセッサのみが有効
- 両方が有効
- 両方が無効

これにより、チームにはCPUパフォーマンスとUSB帯域幅を評価および管理する十分な機会が与えられます。他にも多くのツールが残っています：

- フレーム毎秒（FPS）を監視
- 圧縮ビデオストリーミング形式を選択
- カメラの解像度を選択
- デシメーション（ダウンサンプリング）を設定
- 姿勢ソルバーアルゴリズムを選択
- **AprilTag Processor** からすべてまたは新しい検出のみを取得
- TFOD Processorからすべてまたは新しい認識のみを取得

フレームレート
----------

**VisionPortal** は最大フレームレート、つまり1秒あたりの処理フレーム数（FPS）を**自動的に最適化**します。この最適化が **CPUリソース** に基づいていると仮定すると、**フレームレート**への影響を測定することで、CPUリソースのステータス/消費量/容量を間接的に反映できる可能性があります。

フレームレートは、**LiveView** ステータスウィンドウで視覚的に報告されます。また、**Blocks** とJavaで **OpMode** が追跡、記録、評価するためにも利用可能です：

.. code-block:: java

   float myFPS = myVisionPortal.getFps();

チームはFPSデータを収集して、たとえば（a）解像度と（b）実行中のプロセッサがCPUパフォーマンスに与える一般的な影響を示すことができます。結果は、ウェブカメラ、コードベース（その他の処理）、ビジョンターゲット（数、タイプ、距離）など、多くのチーム固有の要因に依存します。

このような研究の詳細については、この `Dataloggingチュートリアル
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Datalogging>`__ をご覧ください。

デュアルウェブカメラ
------------

ストリーミング形式について説明する前に、**USB帯域幅**が**デュアルウェブカメラ**にとって懸念事項になる可能性があることに言及する必要があります。

.. note::
   内部phone camerasは独立した高速相互接続（USBではない）を持っており、追加されたUSBウェブカメラの影響を受けません。

2つのウェブカメラは、同じ形式または解像度を使用する必要は*ありません*。

**Control Hub に直接接続された**デュアルウェブカメラの場合、USB 2.0およびUSB 3.0ポートは異なるバス上にあります。これにより、帯域幅容量に関する懸念は軽減されますが、より高い解像度により自動最適化されたフレームレートが低下する可能性があります。

**Control Hub** の2つのUSBポートを使用する場合、ストリーム形式の選択はほとんど影響しません。ただし、USB 2.0バスは **Control Hub** の **WiFiラジオ**も伝送します。ウェブカメラを追加すると、その信頼性に影響を与える可能性があります。

一方、**外部USBハブ**（CH 3.0ポートに接続）上の両方のウェブカメラは**帯域幅制限**に達する可能性があり、プレビューの失敗や **OpMode** のクラッシュを引き起こします。これは、すでに説明した要因と、**ストリーミング形式**の選択によって管理できます。

ストリーミング形式
-----------------

レガシーの **YUY2形式**では、（共有ハブ上の）一方または他方のウェブカメラが、約640x360解像度を超えるとストリーミングを停止する可能性があります。これは640x480の**デフォルト解像度を下回っています**。

帯域幅の問題は、**検出なし**と **LiveView** の青い画面によって示されることがよくあります。デフォルトの解像度を使用しているチームは、デュアルウェブカメラが**機能しない**と（誤って）素早く結論付ける可能性があります。

SDKは現在、圧縮された **MJPEG形式**を提供しています。これにより、USB帯域幅の問題を大幅に軽減できますが、認識の速度と品質についても評価する必要があります。

MJPEG形式では、約432x240未満の解像度では、少なくとも1つのウェブカメラで **AprilTag** 検出を防ぐために画像が劣化する可能性があります。一方、より高い解像度では、時々RCアプリが停止したり、**Control Hub** がクラッシュしたりする可能性があります。

両方の形式で、より高い解像度はフレームレートを低下させる可能性があります。

これらの要因は、**VisionPortal** パフォーマンスを最適化するための実験とDataloggingの多くの機会を提供します。

カメラ解像度
-----------------

一部のチームは、ウェブカメラを購入し、**AprilTag** とTFODの使用のために解像度を指定する際に、「より高い解像度がより良い」と信じています。

ここの前のセクションで示されているように、複数の目標と課題を満たす「適切な解像度」を検討する方がより有用です：

- 迅速で信頼性の高い **AprilTag** 検出
- オブジェクト追跡を含む、迅速で信頼性の高いTFOD認識
- 正確な **AprilTag** 姿勢推定
- 運転中のスムーズで正確なナビゲーション（高FPS）
- CPU過負荷を回避
- USB帯域幅制限を回避
- キャリブレーション値が存在する解像度（またはアスペクト比）
- 照明条件と適用されるCamera Controlsに対応

最終的に、ニーズを満たす**最低解像度**を好むかもしれません。

カメラがサポートする解像度を見つけるのは簡単です。**誤った（偽の）解像度**で任意の **VisionPortal** **OpMode** を実行してみてください。エラーメッセージがサポートされている解像度を教えてくれます。将来の参照のためにこれらを書き留めてください。

その他のツール
-----------

このトピックは、CPU使用量を管理するための高度なツールについて説明する **AprilTag Advanced Use** ページで続きます。**Blocks** とJavaでテスト **OpMode** が含まれています。

今のところ、興味のあるユーザーが調査および研究するために、以下が残されています：

- デシメーション（ダウンサンプリング）を設定
- 姿勢ソルバーアルゴリズムを選択
- **AprilTag Processor** からすべてまたは新しい検出のみを取得
- TFOD Processorからすべてまたは新しい認識のみを取得

上記のすべての機能は、Visionカテゴリの下にある **FTC Blocks** ツールボックスまたはパレットで簡単に見つけることができます。

**Java** ユーザーは、SDK
`Javadocs <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/overview-summary.html>`__
サイトで **VisionPortal** インターフェースを確認する必要があります。簡単なナビゲーションのために **FRAMES** をクリックしてください。

====

*質問、コメント、修正は westsiderobotics@verizon.net まで*

