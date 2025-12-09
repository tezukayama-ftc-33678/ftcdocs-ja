はじめに
============

このチュートリアルでは、通常のBlocksプログラムで使用できる **カスタムブロック** の作成方法を説明します。
これらの **"myBlocks"** は、OnBot JavaまたはAndroid Studioを使用してJavaでプログラミングします。


.. figure:: images/a0100-introSample.png
    :align: center
    :alt: サンプルmyBlock、戻り値なし
    
    サンプルmyBlock: サーボを操作、戻り値なし


A myBlock can add **advanced capability** previously available only to
myBlockは、以前はJavaコードのみを使用するチームにしか利用できなかった **高度な機能** を追加できます。
または、単一のmyBlockを **「スーパー関数」** として機能させることができ、
以前は多くの通常のBlocksが必要だったロボットの命令を含めることができます。
これにより、チームのBlocksコードはより強力で、よりシンプルになります！


.. figure:: images/a0110-sampleInchesToDrive-circle.png
    :align: center
    :alt: サンプルmyBlock、エンコーダーカウントを返す

また、myBlocksプログラミングにより、チームの一部のメンバーはJavaの学習と使用を開始し、
貴重な新機能を提供できます。他のチームメンバーはBlocksで学習と作業を続け、
チームの公式コードを作成できます。誰も取り残されることはありません。
members can continue learning and working in Blocks, producing the
team’s official code. Nobody is held back, or left behind.

この主要な開発を行ったGoogleのエンジニア `Liz
Looney <https://github.com/lizlooney>`__ に敬意を表します！

Javaに関する注意事項
~~~~~~~~~~~~~

-  このチュートリアルでは、Control HubまたはRobot Controller (RC) 電話で実行されるプログラミングツールである
   :ref:`OnBot Java <programming_resources/onbot_java/onbot-java-tutorial:onbot java programming tutorial>`
   を使用してmyBlocksを構築します。既に :ref:`Android
   Studio <programming_resources/android_studio_java/android-studio-tutorial:android studio programming tutorial>`
   を使用している学生も、同じプログラミングを簡単に行うことができます。
-  このチュートリアルでは、基本的なmyBlocksに必要な最低限のもの以外は、
   `Java <https://en.wikipedia.org/wiki/Java_(programming_language)>`__
   またはOnBot Java (OBJ) については教えません。
