**Android Studio** プロジェクトフォルダーのダウンロード :bdg-success:`AS`
=========================================================================

**SDK** は GitHub リポジトリからダウンロードできます。 GitHub は、個人や組織がオンラインでコンテンツをホストできるようにする Web ベースのバージョン管理会社です。 **Android Studio** ソフトウェアにアクセスするには、GitHub アカウントが必要です。 GitHub ウェブサイトにアクセスして無料でアカウントを作成できます：

*  https://github.com/

ソフトウェアは、**FIRST-Tech-Challenge** GitHub 組織の「FtcRobotController」というリポジトリに保存されています：

*  https://github.com/FIRST-Tech-Challenge/FtcRobotController

.. important:: **GitHub 上級ユーザー** - このチュートリアルは、ユーザーが GitHub と git バージョン管理ソフトウェアの使用に関して初心者であることを前提としています。 GitHub のパワーユーザーの場合は、git を使用してパブリック GitHub リポジトリのローカルコピーを *clone* できます。 ただし、このドキュメントでは、git を使用してリポジトリにアクセスする方法については説明していません。 代わりに、リポジトリを .ZIP ファイルとしてダウンロードする手順を説明します。

.. image:: images/ClickOnReleases.jpg
   :align: center

|

From the main repository web page, click on the “releases” link to jump
リポジトリの Releases ページにジャンプします。Releases ページには、リポジトリの利用可能なソフトウェアリリースが一覧表示されます。 最新のリリースがページの上部近くに表示されます。

.. image:: images/Releases.jpg
   :align: center

|

各ソフトウェアリリースには **Assets** セクションが含まれており、ロボットのプログラミングに必要なソフトウェアをダウンロードできます。この **Assets** セクションを展開するには、三角形のシンボルをクリックする必要がある場合があります。

.. image:: images/Assets.jpg
   :align: center

|

Source code (zip) リンクをクリックして、圧縮された **Android Studio** プロジェクトフォルダーをダウンロードします。

アーカイブプロジェクトファイルの内容の抽出
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

アーカイブ（.ZIP）プロジェクトファイルをダウンロードしたら、このファイルを任意の場所に移動できます。

.. image:: images/MoveDownloadedFile.jpg
   :align: center

|

プロジェクトを **Android Studio** にインポートする前に、まずアーカイブプロジェクトファイルの内容を抽出する必要があります。Windows ユーザーの場合は、ファイルを右クリックして、ポップアップメニューから「すべて展開」を選択します。Windows は、抽出されたプロジェクトフォルダーの保存先を選択するように求めます。表示されるダイアログは、下図に示すものと似ているはずです。

.. image:: images/ProvideName.jpg
   :align: center

|

保存先フォルダーの推奨名（上図では、推奨名は「FtcRobotController-6.0」）を強調表示し、保存先フォルダー名をよりユーザーフレンドリーな名前に変更します。この例では、保存先フォルダーの名前を「mycopy」に変更します。

.. image:: images/Rename.jpg
   :align: center

|

保存先フォルダーの名前を変更したら、アーカイブの内容をフォルダーに抽出します。抽出プロセスが完了したら、プロジェクトフォルダーがターゲットの保存先に正常に抽出されたことを確認します。

.. image:: images/Verify.jpg
   :align: center

|

アーカイブファイルの内容を正常に抽出したら、プロジェクトを **Android Studio** にインポートする準備が整いました。

プロジェクトを **Android Studio** にインポートする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

プロジェクトをインポートするには、コンピューターで **Android Studio** ソフトウェアを起動する必要があります。**Android Studio** のメイン Welcome 画面で、「Open」オプションを選択してインポートプロセスを開始します。

.. image:: images/SelectImport.jpg
   :align: center

|

**Android Studio** は、インポートするプロジェクトフォルダーを選択するように求めます。ポップアップダイアログボックスのファイルブラウザを使用して、このドキュメントの前のセクションで抽出したフォルダーを見つけてナビゲートします。抽出されたプロジェクトフォルダー（抽出されたフォルダーと似た名前の .ZIP ファイルではない）を選択していることを確認してください。「Select Folder」ボタンを押して、選択したプロジェクトを **Android Studio** にインポートします。

.. image:: images/SelectProjectFolder.jpg
   :align: center

|

プロジェクトを信頼するかどうかに関するポップアップが表示される場合があります。その場合は、青い「Trust Project」ボタンをクリックして続行します。

.. image:: images/TrustProject.jpg
   :align: center

|

In the figure above the project folder called “FtcRobotController”
**Android Studio** にインポートするために選択されています。プロジェクトのインポートには、
**Android Studio** が数分かかる場合があります。プロジェクトが正常にインポートされると、
画面は下図に示されているものと似たようになるはずです。
**Android Gradle Plugin (AGP)** の更新を求めるポップアップが表示された場合は、無視してください。
新しいバージョンは現在の ***FIRST* Tech Challenge SDK** と互換性がない可能性があるため、
AGP の更新を試みないでください。

.. image:: images/SuccessfullyImported.jpg
   :align: center

|

