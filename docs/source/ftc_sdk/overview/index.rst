.. meta::
   :title: FIRST Tech Challengeソフトウェア開発キット
   :description: FTC SDKの簡単な紹介
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, RC, Robot Controller, DS, Driver Station

**FIRST Tech Challenge** ソフトウェア開発キット
===============================================

ソフトウェア開発キット（SDK）は、**FIRST Tech Challenge** ロボット用のソフトウェアを開発し、実行するためのツールのコレクションです。SDKソフトウェアには以下が含まれます：

-  **FIRST Tech Challenge Driver Station App**

   *  セルフインスペクト、 :doc:`ロボット構成 </hardware_and_software_configuration/configuring/index>` などを含む

-  **FIRST Tech Challenge Robot Controller App**

   *  :doc:`Blocksプログラミング環境 </programming_resources/blocks/Blocks-Tutorial>` を含む
   *  :doc:`OnBot Javaプログラミング環境 </programming_resources/onbot_java/OnBot-Java-Tutorial>` を含む

-  `Android Studioプロジェクト <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__
   :doc:`Android Studio </programming_resources/android_studio_java/Android-Studio-Tutorial>` でRobot Controller Appをビルドするため
-  `Javadocリファレンスドキュメント <https://javadoc.io/doc/org.firstinspires.ftc>`__
-  シーズン固有のアセット（TensorFlowモデル、Vuforiaデータベースなど）

すべてのリリース済みアプリ/ソースは、`SDK GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ にあります。

SDKリリース
------------

ソフトウェア開発キットは、**FIRST Tech Challenge** **Technology Team** として知られるコアグループによって、プライベートGitHubリポジトリ内で開発および保守されています。このリポジトリは、将来の**FIRST Tech Challenge** ゲームの秘密、開発中の機能、およびその他の開発の側面の詳細を漏らさないようにするため、プライベートに保たれています。開発とメンテナンスは年間を通じて継続的に行われています。

リリースコンテンツ
""""""""""""""""""

SDKがリリースする準備が整うと、プライベートSDKリポジトリがビルドされ、エクスポートされます。このビルドは以下で構成されます：

-  ビルドされたDriver Stationアプリ（``FtcDriverStation-release.apk`` ）
-  ビルドされたRobot Controllerアプリ（``FtcRobotController-release.apk`` ）
-  Android Studioプロジェクトのソースコード（``vX.X.zip``、``vX.X.tar.gz`` ）
-  `Javadocリファレンスドキュメント <https://javadoc.io/doc/org.firstinspires.ftc>`__
-  シーズン固有のアセット（TensorFlowモデル、Vuforiaデータベースなど、別途ホスト）

エクスポートは、`FtcRobotController GitHubリポジトリ
<https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に `ソフトウェアリリース
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ としてプッシュされます。

`FtcRobotController GitHubリポジトリ
<https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ は、エクスポートされたAndroid Studioプロジェクトのソースでも更新され、変更を追跡でき、GitHubリポジトリをチームが `フォーク
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks>`__
または `クローン
<https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`__
できます。ただし、この更新は一方向のプッシュであるため、FtcRobotControllerリポジトリへの公開貢献（`プルリクエスト
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>`__）は受け付けられません。ただし、コミュニティは自由に、**Technology Team** が検討して対処するための課題をリポジトリで作成することが奨励されています。

.. note:: 
   TensorFlowモデルやVuforiaデータベースなどの一部のシーズン固有のアセットは、FtcRobotController GitHubリポジトリに直接含まれていません。代わりに、Maven Centralでホストされている ``.AAR`` にパッケージ化されています。Robot Controller Appを使用する場合、これらのアセットはアプリに含まれています。Android Studioを使用する場合、これらのアセットはプロジェクトを最初にコンパイルするときにダウンロードされ、プロジェクトに含まれます（したがって、アクティブなインターネット接続が必要です）。

リリーススケジュール
""""""""""""""""""""

これらのリリースは、正確な日付が明確に定義されていない場合でも、定期的なスケジュールで行われます：

-  **キックオフSDKリリース** - 通常、**FIRST Tech Challenge** キックオフから1〜2週間以内にリリースされます。キックオフSDKは、通常、シーズン中の使用に必要な最小ソフトウェアバージョンです。
-  **更新/パッチリリース** - これらは通常、**FIRST Tech Challenge** シーズン中に、重大な問題または有用な機能がチームで利用可能になったときにリリースされます。更新/パッチリリースは、重大なパッチまたはバグ修正が発行されない限り、競技には通常必要ありません。
-  **オフシーズンリリース** - オフシーズンリリースは、破壊的変更に対してチームを準備するため、または次のシーズンの新機能のテクノロジープレビューを提供するために使用されます。

ソフトウェアSDKの更新は、`FIRST Tech Challengeブログ <https://community.firstinspires.org/topic/ftc>`__ および
`チームメールブラスト <https://www.firstinspires.org/resources/library/ftc/team-email-blast-archive>`__ を通じて発表されます。


SDKリリースノート
-----------------

SDKリリースの最も重要な要素の1つは、
`SDKリリースノート <https://github.com/FIRST-Tech-Challenge/FtcRobotController#release-information>`__ です。SDKリリースノートには、破壊的変更、機能強化、注目すべき重大なバグ修正など、各リリースの重要な側面が含まれています。

破壊的変更
""""""""""""""""

破壊的変更は、その名前が示すとおり、SDKのAPIまたは一般的なアーキテクチャ内で行われた変更であり、既存のコードまたは構成を破壊する可能性があります。SDKのすべてのユーザーが、特定のリリースに破壊的変更セクションが存在する場合は、リリースノートの破壊的変更セクションを読み、既存のコードへの影響を判断することが特に重要です。

機能強化
""""""""""""

機能強化は、SDKの新機能または既存機能の（非破壊的な）改善です。機能強化には、改善されたロギング、新しいユーザーインターフェース（UI）、より良いユーザーエクスペリエンス（UX）、新しいAPI、より良いパフォーマンス、または信頼性の向上などの項目が含まれる場合があります。SDKのすべての機能強化がリリースノートに記載されているわけではありませんが、ユーザーに直接影響を与えるものは記載されている必要があります。

バグ修正
"""""""""

SDKのほぼすべてのリリースにはバグ修正が含まれていますが、**Technology Team** が重要なバグ修正の可視性を高めたい場合、リリースノートのバグ修正セクションに含まれます。バグに回避策が必要だった場合、チームコードが影響を受ける可能性があり、リリースノートに記載されることは、**Technology Team** がチームに回避策が不要になったことを通知する方法です。

SDKソフトウェアの更新
---------------------

チームがSDKソフトウェアを更新することは重要です。シーズン中の更新は必須ではない場合があります。チームは、競技マニュアルでゲームに必要な最小ソフトウェアバージョンを確認できます。64ビットWindowsコンピューターが利用可能な場合は、REV Hardware Clientを使用してハードウェアを更新することをお勧めします。そうでない場合は、提供される代替方法を使用してソフトウェアを更新できます。

-  :doc:`REV Hardware Clientの更新 </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
-  :doc:`Driver Stationアプリの更新 </ftc_sdk/updating/ds_app/Updating-the-DS-App>`
-  :doc:`Robot Controllerアプリの更新 </ftc_sdk/updating/rc_app/Updating-the-RC-App>`
-  :doc:`Driver Hub OSの更新 </ftc_sdk/updating/driverhub_os/Updating-the-Driver-Hub-OS>`
-  :doc:`Control Hub OSの更新 </ftc_sdk/updating/controlhub_os/Updating-the-Control-Hub-OS>`
-  :doc:`Hubファームウェアの更新 </ftc_sdk/updating/hub_firmware/Updating-Hub-Firmware>`


