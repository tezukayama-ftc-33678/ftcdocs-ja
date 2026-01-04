.. meta::
   :title: FIRST Tech Challenge ドキュメント（非公式日本語訳）
   :description: FIRST Tech Challenge 公式ドキュメントの非公式日本語訳
   :keywords: FTC Control System, Blocks, OnBot Java, Android Studio, OpenCV, EasyOpenCV, AprilTags, FTC SDK, Robot Controller App, Driver Station App, Control Hub, Driver Hub, IMU, Water Game, 日本語, Japanese

*FIRST* Tech Challenge ドキュメント（非公式日本語訳）
=======================================================

.. warning::
   **⚠️ 重要な注意事項**
   
   このドキュメントは **非公式の日本語翻訳** です。
   
   * 本翻訳は有志（Team 33678 Tezukayama-Rise）による非公式なものであり、FIRST® の公式ドキュメントではありません
   * AI翻訳（ローカルLLM）を使用しているため、不正確な翻訳や構造の崩れがある可能性があります
   * 現在、順次修正を進めています
   * **正確な情報については、必ず英語の公式ドキュメントをご確認ください**: https://ftc-docs.firstinspires.org
   
   翻訳の改善にご協力いただける方は、`GitHubリポジトリ <https://github.com/tezukayama-ftc-33678/ftcdocs-ja>`_ までお問い合わせください。

.. note::
   **📋 ライセンスと著作権について**
   
   * 原文: © 2022 FIRST Tech Challenge (BSD 3-Clause License)
   * 翻訳: Team 33678 Tezukayama (同ライセンス)
   * FIRST®、FIRST® Tech Challenge、およびロゴは FIRST® の登録商標です
   * 詳細は `LICENSE-JA.md <https://github.com/tezukayama-ftc-33678/ftcdocs-ja/blob/main/LICENSE-JA.md>`_ をご覧ください

*FIRST®* Tech Challenge ドキュメントへようこそ！このウェブサイトには、競技用ロボットを作成するために必要なすべての情報が含まれています。
*FIRST* Tech Challenge のソフトウェアとロボット制御システムの使用方法に関する情報とチュートリアルがあります。
また、コーチやメンター向けの情報もあります。

*FIRST* Tech Challenge は、中学生と高校生を対象としたロボティクスプログラムです。
ロボットを作るだけではなく、もっと多くのことがあります。詳しくは :doc:`FIRST Tech Challenge について <overview/ftcoverview>` と :doc:`gracious_professionalism/gp` をご覧ください。

.. toctree::
   :hidden:
   :maxdepth: 1

   /overview/ftcoverview
   gracious_professionalism/gp

.. toctree::
   :caption: はじめに
   :maxdepth: 1
   :hidden:

   persona_pages/rookie_teams/rookie_teams
   persona_pages/veteran_teams/veteran_teams
   persona_pages/coach_admin/coach_admin
   persona_pages/mentor_tech/mentor_tech
   
.. toctree::
   :caption: ゲームとシーズン固有のリソース
   :maxdepth: 1
   :hidden:

   game_specific_resources/blog/blog
   tech_tips/tech-tips
   ai/innovation_corner/innovation-corner
   Competition Manual <manuals/game_manuals/game_manuals>
   Game Q&A System <game_specific_resources/ftcqa/ftcqa>
   game_specific_resources/playing_field_resources/playing_field_resources
   Field Coordinate System <game_specific_resources/field_coordinate_system/field-coordinate-system>

.. toctree::
   :caption: ソフトウェア開発キット (SDK)
   :maxdepth: 1
   :hidden:

   Laptop Requirements <programming_resources/laptops/laptops>
   SDK Overview <ftc_sdk/overview/index>
   Updating Components <ftc_sdk/updating/index>

.. toctree::
   :caption: ロボット製作リソース
   :maxdepth: 1
   :hidden:


.. toctree::
   :caption: 制御システムリソース
   :maxdepth: 1
   :hidden:

   programming_resources/shared/control_system_intro/The-FTC-Control-System 
   control_hard_compon/index
   hardware_and_software_configuration/index
   hardware_and_software_configuration/self_inspect/new-self-inspect
   hardware_and_software_configuration/self_inspect/self-inspect
   programming_resources/index

.. toctree::
   :caption: AprilTag リソース
   :maxdepth: 1
   :hidden:

   AprilTag Introduction </apriltag/vision_portal/apriltag_intro/apriltag-intro>
   VisionPortal Overview </apriltag/vision_portal/visionportal_overview/visionportal-overview>
   Webcams for VisionPortal </apriltag/vision_portal/visionportal_webcams/visionportal-webcams>
   Understanding AprilTag Values </apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values>
   AprilTag Localization </apriltag/vision_portal/apriltag_localization/apriltag-localization>
   AprilTag Test Images </apriltag/opmode_test_images/opmode-test-images>

.. toctree::
   :caption: CAD リソース
   :maxdepth: 1
   :hidden:

   Computer Aided Design (CAD) <cad_resources/index>

.. toctree:: 
   :caption: 静電気放電
   :maxdepth: 1
   :hidden:

   Managing ESD Effects <hardware_and_software_configuration/configuring/managing_esd/managing-esd>

.. toctree::
   :caption: 製造
   :maxdepth: 1
   :hidden:

   Manufacturing Methods <manufacturing/index>
   
.. toctree::
   :caption: チームリソース
   :maxdepth: 1
   :hidden:    
   
   faq/faqs
   Team Complimentary Software<sponsors/software/software>
   Team Discounts<sponsors/discounts/discounts>
   team_resources/team_resources

.. toctree::
   :caption: FTC ドキュメント
   :maxdepth: 1
   :hidden:

   Booklets<booklets/index>
   Archive <https://ftc-docs.firstinspires.org/projects/ftcdocs-archive/en/latest/index.html>
   Site Feedback Form<ftc_docs/form/form>
   Contributing to FTC Docs<contrib/index>

.. Add Contrib Section here when added

**私は...**

- :doc:`新規チーム <persona_pages/rookie_teams/rookie_teams>` 新規チームは、どこから始めればよいかわからないかもしれません。ここから始めましょう！

- :doc:`既存チーム <persona_pages/veteran_teams/veteran_teams>` リソースを探している既存チームは、ここで見つけることができます。

- :doc:`コーチ <persona_pages/coach_admin/coach_admin>` ヘルプやチーム管理リソースを探しているコーチは、ここを見てください。

- :doc:`メンター <persona_pages/mentor_tech/mentor_tech>` 技術リソースを探している技術メンターは、まずここを見てください！

メインメニューには、トップレベルのコンテンツへのリンクがあります。以下は、トピック別に整理されたクイックリンクです。

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-black
      :class-body: sd-text-left 

      プログラミングリンク
   
      ^^^

      プログラミング言語リソースへのクイックリンク

      +++

      .. div:: container-fluid p-0

         .. div:: col-sm pl-1 pr-1

            .. button-ref:: programming_resources/blocks/Blocks-Tutorial
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Blocks
      
         .. div:: col-sm pl-1 pr-1

            .. button-ref:: programming_resources/onbot_java/OnBot-Java-Tutorial
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               OnBot Java
         
         .. div:: col-sm pl-1 pr-1
 
            .. button-ref:: programming_resources/android_studio_java/Android-Studio-Tutorial
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Android Studio

         .. div:: col-sm pl-1 pr-1

            .. button-ref:: ../../apriltag/vision_portal/apriltag_intro/apriltag-intro
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               AprilTags

         .. div:: col-sm pl-1 pr-1
 
            .. button-ref:: programming_resources/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               全てのリソース

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-black
      :class-body: sd-text-left 

      制御システムリンク
   
      ^^^

      *FIRST* Tech Challenge 制御システムを知りましょう！

      +++

      .. div:: container-fluid p-0

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: control_hard_compon/ds_components/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               ドライバーステーション

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: control_hard_compon/rc_components/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               ロボットコントローラー

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: hardware_and_software_configuration/connecting_devices/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               デバイス接続

         .. div:: col-sm pl-1 pr-1

            .. button-ref:: hardware_and_software_configuration/configuring/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               ハードウェア設定

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-black
      :class-body: sd-text-left 

      ソフトウェア開発キット (SDK)
   
      ^^^

      ソフトウェア開発キット (SDK) は、ソフトウェアを開発してロボットで実行するためのツールのコレクションです。

      +++
 
      .. div:: container-fluid p-0

         .. div:: col-sm pl-1 pr-1

            .. button-ref:: ftc_sdk/overview/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               SDK について

         .. div:: col-sm pl-1 pr-1
      
            .. button-link:: https://github.com/FIRST-Tech-Challenge/FtcRobotController/              
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               SDK GitHub リポジトリ

         .. div:: col-sm pl-1 pr-1
      
            .. button-link:: https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases               
               :color: black
               :outline:
               :expand:

               SDK リリース

         .. div:: col-sm pl-1 pr-1

            .. button-link:: https://javadoc.io/doc/org.firstinspires.ftc
               :color: black
               :outline:
               :expand:

               Javadoc ドキュメント

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-black
      :class-body: sd-text-left 

      ゲームリンク
   
      ^^^

      競技のルールに必ず従ってください！
      競技マニュアルは必須のドキュメントです。

      +++
 
      .. div:: container-fluid p-0

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: manuals/game_manuals/game_manuals
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               競技マニュアル

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: game_specific_resources/playing_field_resources/playing_field_resources
               :ref-type: doc
               :color: black
               :outline:
               :expand:

         .. div:: col-sm pl-1 pr-1

            .. button-link:: https://ftc-qa.firstinspires.org/
               :color: black
               :outline:
               :expand:

               ゲーム質問回答システム

.. note::

   このプロジェクトは積極的に開発中です。ここに含まれるものはすべて情報提供のみを目的としています。
   このドキュメントはチームをサポートし、ゲームルールに何らかの文脈を提供することを意図していますが、
   ゲームルールがここにあるすべてのドキュメントに優先します。このプロジェクトについてのフィードバックがある場合は、
   :doc:`フィードバックフォーム <ftc_docs/form/form>` をご利用ください。

