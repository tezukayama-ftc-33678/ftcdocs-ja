開発者オプションの有効化 :bdg-success:`AS`
============================================

**Android** 端末を構成した後、**Android Studio** に含まれるツールを使用して端末にアプリをインストールできるようにする前に、端末が開発者モードになっていることを確認する必要があります。

.. important:: **Control Hub** ユーザーの方へ - **Control Hub** は工場出荷時に開発者オプションが自動的に有効になっているため、**Control Hub** に対してこのステップを実行する必要は** ありません** 。

**Android** Developer ウェブサイトには、端末で開発者オプションを有効にする方法に関する情報が含まれています。以下のリンクにアクセスし、「Enabling On-device Developer Options」というセクションを読むと、端末で **Settings** -> About phone に移動し、ビルド番号を7回タップすることで、**Android** 端末で開発者オプションを有効にできることがわかります。

*  https://developer.android.com/studio/run/device#setting-up

**Android Studio** ツールを使用して端末にアプリをインストールできるようにするには、両方の端末で開発者オプションと USB デバッグが有効になっていることを確認する必要があります。

.. image:: images/DeveloperOptions.jpg
   :align: center

|

**Android Studio** を実行しているコンピューターに端末を初めて接続すると、コンピューターが端末への USB デバッグアクセスを許可してもよいかどうかを端末が尋ねる場合があります。その場合は、「Always allow from this computer」オプションをチェックし、OK ボタンを押して USB デバッグを許可してください。

.. image:: images/AllowUSBDebugging.jpg
   :align: center

|

