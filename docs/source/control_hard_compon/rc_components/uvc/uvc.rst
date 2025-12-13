UVC ウェブカメラ
================

ウェブカメラは、周囲の環境の視覚画像を提供するデバイスです。UVC（USB Video Class）は、ウェブカメラやデジタルカメラなどの USB デバイスが、特別なドライバーを必要とせずにビデオをコンピューターにストリーミングできるようにする標準です。*FIRST* Tech Challenge の一部として使用する場合、チームは市販の USB Video Class `(UVC) <https://www.usb.org/document-library/video-class-v15-document-set>`__ 互換カメラを使用する必要があります。このデバイスは、**REV Control Hub** に直接接続するか、USB ハブを介してロボット制御システムに接続できます。

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      Budget Webcam

      ^^^

      .. figure:: images/C270.jpg
         :align: center
         :width: 50 %
         :class: no-scaled-link
         :alt: Example budget UVC webcam
        
++++++++

      :ref:`logitech_c270_label`

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      Mid-range Webcam

      ^^^

      .. figure:: images/C920.jpg
         :align: center
         :width: 50 %
         :class: no-scaled-link
         :alt: Example mid-range UVC webcam
        
++++++++

      :ref:`logitech_c920_label`

ウェブカメラは、コンピュータービジョン関連のタスクで使用することを目的としています。
ウェブカメラの使用例には、以下が含まれます：

- **AprilTag** の :doc:`検出 <../../../apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values>`
- フィールド上でロボットが :doc:`どこにいるか <../../../apriltag/vision_portal/apriltag_localization/apriltag-localization>` の特定
- **OpenCV** を使用したゲーム要素の :doc:`色や形状の検出 <../../../color_processing/index>`

追加リソース
--------------------

- **VisionPortal** と互換性があることが知られている :doc:`ウェブカメラのリスト <../../../apriltag/vision_portal/visionportal_webcams/visionportal-webcams>`
- :ref:`Connecting UVC Camera via Powered USB Hub <hardware_and_software_configuration/configuring/configuring_uvc_camera/configuring-uvc-camera:configuring an external uvc camera and a powered usb hub>`
- :ref:`Connecting UVC Camera directly to REV Control Hub <hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam:configuring an external webcam with a control hub>`
- :ref:`USB Port Overview <control_hard_compon/rc_components/hub/ports/ch-ports:USB Ports>`
- :ref:`Vision in FIRST Tech Challenge <programming_resources/index:vision programming>`

