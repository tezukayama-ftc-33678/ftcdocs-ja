**FIRST** プログラムのコンピューター要件
==========================================

**FIRST**\ :sup:`®` LEGO\ :sup:`®` League、**FIRST**\ :sup:`®` Tech Challenge、**FIRST**\ :sup:`®` Robotics Competition などの **FIRST**\ :sup:`®` プログラムは、参加するチームと同じくらいユニークです。このユニークさは、プログラムに技術を提供するさまざまなベンダー、各プログラムの独自の目標を管理するために必要なハードウェアとソフトウェア、そしてチームが参加し優れた成果を上げるために役立つツールと技術の絶えず進化する状況に一部起因しています。プログラム間の共通点の1つは、チームがソフトウェア開発、設計、およびコラボレーションのためのコンピュータープラットフォームを必要とすることです。このドキュメントは、そのコンピューターシステムのハードウェアとオペレーティングシステムの要件に関する推奨事項として機能します。

コンピューターの最小要件に影響を与える可能性のある多くの要因のうち、これらが最も大きく影響します：

-  プログラム内でコンピューターが実行する可能性のある役割固有のタスク

-  コンピューターで使用される可能性のあるコンピューター支援設計（CAD）ソフトウェアのタイプ

-  ソフトウェア開発とハードウェア更新の要件

-  ベンダー固有のアプリケーション要件と制限

プログラム固有の要件
-----------------------------

各プログラムには独自の要件セットがありますが、それらの各要件は最小限のコンピューター構成で満たすことができます。このセクションでは、各プログラムの役割の最小要件を特定しようとしています。各要件を満たす具体的な推奨ハードウェアは、「推奨ハードウェアセット」セクションに記載されています。

**FIRST**\ :sup:`®` LEGO\ :sup:`®` League の推奨コンピューターハードウェア
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**FIRST** LEGO League には、プログラム可能なプラットフォームを使用する2つのディビジョンがあります：`LEGO\ ® Education SPIKE\ ™ Prime <https://education.lego.com/en-us/product-resources/spike-prime/downloads/system-requirements/>`__ プラットフォームを使用する **FIRST** LEGO League Challenge と、`LEGO\ ® Education SPIKE\ ™ Essential <https://education.lego.com/en-us/products/lego-education-spike-essential-set/45345/>`__ プラットフォームを使用する **FIRST** LEGO League Explore です。両方のプラットフォームは、ほぼ同じコンピューター要件を持っており、違いは以下に記載されています。これらのプラットフォームは、ほとんどのコンピューター構成でサポートされているため、最もアクセスしやすいものの1つです。

*ソフトウェア開発に推奨：*

-  `Windows Standard Laptop`_

サポート対象：

-  `MacOS Standard Laptop`_

-  `Chrome OS Standard Laptop`_

-  `iOS Standard Tablet`_

   -  LEGO\ :sup:`®` Education SPIKE™ Essential hub は iPad では更新できません

-  `Android Standard Tablet`_

   -  LEGO\ :sup:`®` Education SPIKE™ Essential はサポートされていません

また、Google Play ストア（Chromebook Android アプリ用）へのアクセス、アプリ内コンテンツのダウンロード、教師サポート資料へのアクセス、ライブ気象データなどの特定の機能を使用するために、アクティブなインターネット接続を持つことも推奨されます。

**FIRST**\ :sup:`®` Tech Challenge の推奨コンピューターハードウェア
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**FIRST** Tech Challenge で使用される主要なハードウェアプラットフォームは、`REV Control Hub <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics>`__ と `REV Driver Hub <https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications>`__ です。これらのプラットフォームには独自のオペレーティングシステムとアプリケーション要件がありますが、ほとんどのハードウェアプラットフォームで基本的な機能のほとんどを実行できます（ただし、より多くの手動手順が必要です）。**FIRST** Tech Challenge のチームは、ソフトウェア開発と CAD という2つの基本的な目的でコンピューターを使用しており、この2つの使用法におけるチームの好みが必要なハードウェアを形成します。

*ソフトウェア開発と CAD に推奨：*

-  `Windows Performance Laptop`_



*ソフトウェア開発のみに推奨：*

-  `Windows Standard Laptop`_

   -  クラウド CAD ソリューションのみ推奨

      -  OnShape、SolidWorks 3D Experience など


サポート対象：

-  `MacOS Standard Laptop`_

   -  `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ はサポートされていません

      -  ブラウザベースのインターフェースを使用して手動で更新する必要があります

-  `Chrome OS Standard Laptop`_

   -  `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ はサポートされていません

      -  ブラウザベースのインターフェースを使用して手動で更新する必要があります

   -  `Android Studio <https://developer.android.com/studio>`__ はサポートされていません

      -  **Blocks** と **OnBot Java** のみサポート

また、ソフトウェア開発中はアクティブなインターネット接続を持つことが推奨されます。https://github.com へのアクセスは、**REV Hardware Client** が必要なシーズンソフトウェア更新をダウンロードしてインストールするために必要であり、**Android Studio** ユーザーがソフトウェアテンプレートをダウンロードするためにも必要です。

**FIRST**\ :sup:`®` Robotics Competition の推奨コンピューターハードウェア
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**FIRST** Robotics Competition で使用される主要なハードウェアプラットフォームは、`NI roboRIO <https://www.ni.com/docs/en-US/bundle/roborio-20-specs/page/specs.html>`__ です。このプラットフォームには、プログラミング環境に応じて、ソフトウェア開発の要件とは異なる可能性のある競技におけるコンピューターハードウェアに対する独自の要件セットがあります。**FIRST** Tech Challenge と同様に、**FIRST** Robotics Competition のチームは、ソフトウェア開発と CAD という2つの基本的な目的でソフトウェア開発コンピューターを使用しており、この2つの使用法におけるチームの好みが必要なハードウェアを形成します。ただし、**FIRST** Robotics Competition では、コンピューターが果たすことができる2つの役割（ソフトウェアと設計開発プラットフォームおよび／または Driver Station プラットフォーム）があり、これらの役割もコンピューターハードウェアの要件を形成します。

必要に応じて1台のラップトップを両方の目的に使用できますが、Driver Station プラットフォーム用とソフトウェアおよび設計開発用の2台の別々のコンピューターを持つことが推奨されます。

Driver Station
^^^^^^^^^^^^^^

Driver Station コンピューターは、ロボットへの主要なインターフェースとして使用され、イベントで Field Management System（FMS）とのインターフェースに使用され、ロボット上のハードウェアおよびソフトウェアプラットフォームと通信するために使用されるソフトウェアツールによって制限されます。チームは、イベントでのシステムの義務と物理的要求を分離できるように、Driver Station の役割とソフトウェアおよび設計開発の役割に別々のコンピューターを持つことが有利であると感じています。予算を意識しているチームは、そのコンピューターが少なくとも Driver Station の役割の最小要件を満たしている場合、両方の役割に単一のコンピューターを確実に使用できます。Driver Station の役割には Windows オペレーティングシステムが必要であることに注意してください。これは、役割の義務を実行するために必要なアプリケーションが Windows 専用アプリケーションであるためです。

*Driver Station の役割に推奨：*

-  `Windows Standard Laptop`_


サポート対象：

-  `Windows Performance Laptop`_

ソフトウェア開発と設計
^^^^^^^^^^^^^^^^^^^^^^^

**FIRST** Tech Challenge と同様に、**FIRST** Robotics Competition チームは、ソフトウェア開発と設計ラップトップをソフトウェア開発と CAD に使用します。CAD の使用に応じて、ハードウェア要件は若干異なります：

*CAD を使用したソフトウェアおよび設計開発の役割に推奨：*

-  `Windows Performance Laptop`_


*ソフトウェア開発のみに推奨：*

-  `Windows Standard Laptop`_

   -  クラウド CAD ソリューションのみ推奨

      -  OnShape、SolidWorks 3D Experience など


サポート対象：

-  `MacOS Standard Laptop`_

   -  `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ はサポートされていません

   -  `LabVIEW <https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/labview-setup.html>`__ ソフトウェアはサポートされていません

また、ソフトウェア開発中はアクティブなインターネット接続を持つことが推奨されます。https://github.com へのアクセスは、**REV Hardware Client** が必要なシーズンソフトウェアとファームウェア更新をダウンロードしてインストールするために必要です。追加のソフトウェアにも同様の要件がある場合があります。

推奨ハードウェアセット
-------------------------

これらは、プログラム固有の要件によって参照される推奨ハードウェアセットです。すべてのハードウェアプラットフォームには、次のようないくつかの追加要件と推奨事項があります：

*Windows オペレーティングシステム*

-  Windows 10 のサポートは2025年半ばに終了するため、Windows 11 をサポートする Windows システムを購入することを強くお勧めします。すべてのソフトウェアが Windows 11 でサポートされていると明示的にラベル付けされているわけではありませんが、必要なソフトウェアのほぼすべてが Windows 11 で動作するようにテストされています。


*USB ポート*

-  ラップトップには少なくとも2つの利用可能な物理 USB-A ポートが必要です。

-  **FIRST** Tech Challenge の場合、ラップトップの USB-C ポートは **REV Control Hub** または **REV Driver Hub** で適切に動作できないため、USB-A ポートも利用できることが重要です。


*Bluetooth*

-  **FIRST** LEGO League の場合、ラップトップとタブレットが Bluetooth 4.0 以上をサポートすることが重要です。


*物理イーサネットポート*

-  ハードウェアとソフトウェアのほとんどの機能は Wi-Fi で簡単にサポートできますが、一部の状況（**FIRST** Robotics Competition の Driver Station など）では、システムに物理 RJ-45 イーサネットポートがあることが大きな利点です。


*SSD ハードドライブ*

-  特に必須ではありませんが、SSD 技術を使用するハードドライブ（回転ディスク技術と比較して）は、より速く起動し、電源を入れたまま持ち運んでいるときや、**FIRST** Robotics Competition Driver Station コンピューターで一般的な「予期しない衝撃」を経験したときに損傷する可能性が低くなります。

**Windows Performance Laptop**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

高性能プロセッサを含む高グラフィックス性能向けに設計されたラップトップ。`Dell G16 <https://www.dell.com/en-us/shop/dell-laptops/g16-gaming-laptop/spd/g-series-16-7630-laptop>`__ や `HP Omen <https://www.hp.com/us-en/shop/pdp/omen-gaming-laptop-16-xf0087nr>`__ など。以下の推奨仕様：

-  プロセッサー：Intel Core i7、AMD Ryzen 7、またはそれ以上

-  グラフィックス：NVIDIA GeForce RTX 4050 またはそれ以上

-  メモリー：16GB RAM 以上、32GB 推奨

-  ストレージ：512 GB SSD 以上、1TB SSD 推奨

-  イーサネット：RJ-45 イーサネットポート推奨

-  ポート：USB type A ポート2つ以上推奨

-  Bluetooth：Bluetooth 4.0 またはそれ以上

-  Wi-Fi：統合 Wi-Fi、Wi-Fi 6E 以上推奨

-  オペレーティングシステム：Windows 10 以上、Windows 11 推奨

**Windows Standard Laptop**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

スムーズなパフォーマンスと日常的なタスク向けに設計された標準的な Windows ラップトップ。`Dell Inspiron 15 <https://www.dell.com/en-us/shop/dell-laptops/inspiron-15-laptop/spd/inspiron-15-3530-laptop>`__ や `HP Pavilion Laptop <https://www.hp.com/us-en/shop/mdp/laptops/pavilion-15-344522--1>`__ など。

-  プロセッサー：Intel Core i5、AMD Ryzen 5、またはそれ以上

-  グラフィックス：Intel または AMD 組み込みグラフィックスアダプターまたはそれ以上

-  メモリー：8GB RAM 以上、16GB 推奨

-  ストレージ：256GB 以上、512 GB SSD 推奨

-  イーサネット：RJ-45 イーサネットポート推奨

-  ポート：USB type A ポート2つ以上推奨

-  Bluetooth：Bluetooth 4.0 またはそれ以上

-  Wi-Fi：統合 Wi-Fi、Wi-Fi 6E 以上推奨

-  オペレーティングシステム：Windows 10 以上、Windows 11 推奨

**MacOS Standard Laptop**
~~~~~~~~~~~~~~~~~~~~~~~~~

スムーズなパフォーマンスと日常的なタスク向けに設計された標準的な MacOS ラップトップ。`MacBook Air <https://www.apple.com/shop/buy-mac/macbook-air>`__ や `MacBook Pro <https://www.apple.com/shop/buy-mac/macbook-pro>`__ など。

-  プロセッサー：Apple M1 またはそれ以上、Apple M2 推奨

-  メモリー：4GB RAM 以上

-  ストレージ：2GB 以上の利用可能なストレージスペース

-  Bluetooth：Bluetooth 4.0 またはそれ以上

-  オペレーティングシステム：MacOS Mojave 10.14 以降

**iOS Standard Tablet**
~~~~~~~~~~~~~~~~~~~~~~~

iPad Air 2 または iPad Mini 4 以降などの標準的な iOS タブレット。

-  オペレーティングシステム：iOS 13 以降

**Chrome OS Standard Laptop**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Samsung Galaxy Chromebook 2 <https://www.google.com/chromebook/discover/pdp-samsung-galaxy-chromebook-2/sku-samsung-galaxy-chromebook-2-8gb-128gb/>`__ などの標準的な Chromebook、または類似のもの。

-  プロセッサー：1.40 GHz Intel Celeron 2955U デュアルコアプロセッサーまたはそれ以上

-  メモリー：4GB RAM 以上

-  ストレージ：3GB 以上の利用可能なストレージスペース

-  Bluetooth：Bluetooth 4.0 以上

-  オペレーティングシステム：Android 7.0 以降

**Android Standard Tablet**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Samsung Galaxy Tab A7 Lite <https://www.samsung.com/us/tablets/galaxy-tab-a/galaxy-tab-a7-10-4-inch-gray-64gb-wi-fi-sm-t500nzaexar/>`__ などの標準的な Android タブレット、または類似のもの。

-  8 インチ以上のディスプレイ

-  メモリー：3GB RAM 以上

-  ストレージ：3GB 以上の利用可能なストレージスペース

-  Bluetooth：Bluetooth 4.0 以上

-  オペレーティングシステム：Android 7.0 以降
