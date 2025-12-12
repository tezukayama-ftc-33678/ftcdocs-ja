はじめに
============

このチュートリアルでは、通常の **Blocks** プログラムで使用する**カスタムブロック**の作成方法を示します。これらの **「myBlocks」** は、**OnBot Java** または **Android Studio** を使用して Java でプログラムされます。


.. figure:: images/a0100-introSample.png
    :align: center
    :alt: サンプル myBlock、void を返す
    
    サンプル myBlock：サーボを操作、値を返さない


**myBlock** は、以前はすべて Java コードを使用するチームのみが利用できた**高度な機能**を追加できます。または、単一の **myBlock** は、以前は多くの通常の Blocks が必要だったロボット命令を含む**「スーパー関数」**として機能できます。これで、チームの **Blocks** コードがより強力で、よりシンプルになります！



.. figure:: images/a0110-sampleInchesToDrive-circle.png
    :align: center
    :alt: サンプル myBlock、エンコーダーカウントを返す

    サンプル myBlock：入力に基づいてエンコーダーターゲット値を返す

また、**myBlocks** プログラミングにより、一部のチームメンバーが Java の学習と使用を開始し、貴重な新機能に貢献できるようになります。他のチームメンバーは **Blocks** での学習と作業を続け、チームの公式コードを作成できます。誰も足を引っ張られたり、取り残されたりすることはありません。

この重要な開発を行った Google エンジニアの `Liz Looney <https://github.com/lizlooney>`__ さんに敬意を表します！

Java に関する注意事項
~~~~~~~~~~~~~

-  このチュートリアルでは、**Control Hub** または **Robot Controller (RC)** スマートフォン上で実行されるプログラミングツールである :ref:`OnBot Java <programming_resources/onbot_java/onbot-java-tutorial:onbot java programming tutorial>` を使用して **myBlocks** を作成します。すでに :ref:`Android Studio <programming_resources/android_studio_java/android-studio-tutorial:android studio programming tutorial>` を使用している学生は、同じプログラミングを簡単に実行できます。
-  このチュートリアルでは、基本的な **myBlocks** に必要な最小限を超えて、`Java <https://en.wikipedia.org/wiki/Java_(programming_language)>`__ または **OnBot Java (OBJ)** を教えることはありません。
