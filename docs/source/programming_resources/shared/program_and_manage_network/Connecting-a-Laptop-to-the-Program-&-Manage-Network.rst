ラップトップを Program & Manage ネットワークに接続する
======================================================

ラップトップを Program & Manage ネットワークに接続する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Op Mode** を作成するには、プログラミングラップトップを Program & Manage Wi-Fi ネットワークに接続する必要があります。Program & Manage Wi-Fi ネットワークは、**Robot Controller** によって作成されるワイヤレスネットワークです。この演習を開始する前に、Windows ラップトップに Microsoft の最新のサービスパックとシステム更新プログラムがインストールされていることを確認してください。

この例では、ユーザーが Windows 10 ラップトップを使用していることを前提としています。Windows 10 ラップトップを使用していない場合、Programming & Manage Wi-Fi ネットワークに接続する手順は異なります。Wi-Fi ネットワークへの接続方法の詳細については、デバイスのドキュメントを参照してください。

ラップトップを Program & Manage ネットワークに接続する手順
-------------------------------------------------------------------

1. **DRIVER STATION** で、画面の右上隅にある 3 つのドットをタッチしてポップアップメニューを起動します。ポップアップメニューから**Program & Manage** を選択して、**Program & Manage** アクセス情報を表示します。                                                   

.. image:: images/SelectProgramAndManageDriverStation.jpg
   :align: center

|

2. Program & Manage 画面には、ラップトップを **Blocks** または**OnBot Java** プログラミングモードサーバーに接続するために使用できる**Robot Controller** への接続に必要な重要な情報が表示されます。                                              

.. image:: images/ProgramAndManageScreen.jpg
   :align: center

|

3. Program & Manage ワイヤレスネットワークのネットワーク名とパスフレーズを確認します。画面の上部に、Program & Manage ワイヤレスネットワークの名前が表示されます。**Robot Controller** として**Android** スマートフォンを使用している場合、ワイヤレスネットワーク名は「DIRECT-」という語句で始まります。 

   この例では、Wi-Fi ネットワークの名前は「DIRECT-XK-9999-C-RC」で、セキュアパスフレーズは「ZU7if0hB」です。                                              

.. image:: images/ProgramAndManagePassphrase.jpg
   :align: center

|

**Control Hub** を使用している場合、ワイヤレスネットワーク名は**Control Hub** を構成したときに指定したものになります。**Control Hub** の名前をまだ変更していない場合、デフォルトではワイヤレスネットワークの名前は「FTC-」で始まります。パスワードをまだ変更していない場合、デフォルトではワイヤレスネットワークのパスフレーズは「password」になります。

以下のスクリーンショットでは、**Control Hub** のワイヤレスネットワーク名は「FTC-1Ybr」で、セキュアパスフレーズは「password」です。

.. image:: images/ProgramAndManagePassphraseControlHub.jpg
   :align: center

|

4. Windows 10 コンピューターで、デスクトップの右下隅にある Wi-Fi シンボルを探します。Wi-Fi シンボルをクリックして、近くの利用可能な Wi-Fi ネットワークのリストを表示します。          

.. image:: images/ConnectingLaptopStep4.jpg
   :align: center

|

5. Program & Manage 画面に表示されている名前と一致するワイヤレスネットワークを探します。                                          

.. image:: images/screengrabwirelessnetworks.jpg
   :align: center

|

   この例では、**Android** **Robot Controller** のワイヤレスネットワークの名前は「DIRECT-XK-9999-C-RC」で、Windows 10 コンピューターに表示されるリストにネットワークが表示されています。

6. リストでターゲットネットワークを見つけたら、それをクリックして選択します。                                                            

.. image:: images/screengrabconnectautomatically.jpg
   :align: center

|

   「Connect」ボタンを押してネットワークに接続します。

7. プロンプトが表示されたら、ネットワークパスフレーズ（この例では「ZU7if0hB」）を入力し、「Next」を押して続行します。                             

.. image:: images/screengrabsecuritykey.jpg
   :align: center

|

パスフレーズは大文字と小文字を区別することに注意してください。スペルと大文字小文字の使い方が、Program & Manage 画面に表示されている元のスペルと大文字小文字の使い方と一致していることを確認してください。

8. Windows 10 ラップトップと **Robot Controller** **Android** デバイス間のワイヤレス接続が正常に確立されると、ラップトップのワイヤレス設定にステータスが表示されます。                                                          

.. image:: images/screengrabnointernet.jpg
   :align: center

|

数秒後に表示が更新されない場合は、Wi-Fi 接続を示す青いボックスの下部にある「Network Connections」をクリックしてみてください。これにより、「Show available networks」へのリンクを含む Setting ダイアログボックスが表示され、Wi-Fi 接続のリストを強制的に更新できます。

.. attention:: **Robot Controller** の**Blocks** プログラミングモードサーバーに接続している場合、ラップトップは** インターネットにアクセスできません**。**Robot Controller** への直接アクセスのみが可能です。


ワイヤレス接続のトラブルシューティング
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

利用可能なネットワークのリストにプログラミングモードワイヤレスネットワークが表示されない場合、またはラップトップを Program & Manage ワイヤレスネットワークに接続する際に問題がある場合は、以下の質問に答えてください：

1. **Robot Controller** は実行中で、**DRIVER STATION** に接続されていますか？
2. Windows ラップトップは最新のシステム更新プログラムとサービスパックで更新されていますか？たとえば、古いバージョンの Windows 8 や 10 には、ラップトップが利用可能なネットワークのリストに Program & Manage ワイヤレスネットワークを表示できなくなる問題がありました。


