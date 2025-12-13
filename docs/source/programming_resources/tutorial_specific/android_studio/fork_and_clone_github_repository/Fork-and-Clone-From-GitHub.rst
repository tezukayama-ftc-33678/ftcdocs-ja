GitHub からフォークとクローンを行う :bdg-success:`AS`
======================================================

.. important:: 
   このアプローチは、`git <https://docs.github.com/en/get-started/learning-about-github/github-glossary#git>`__ と `GitHub <https://github.com/>`__ の基本的な知識があることを前提としています。git に関連することのほとんどについて、目的を達成するための方法は数多くあります。このドキュメントでは、Windows ユーザー向けの方法の一つを説明します。
   コマンドラインツールや git に不慣れなユーザーは、:doc:`SDK を zip アーカイブとしてダウンロード
   <../downloading_as_project_folder/Downloading-the-Android-Studio-Project-Folder>` する方法で SDK を入手してください。

フォーク vs. クローン 
----------------------

GitHub 上の`フォーク <https://docs.github.com/en/get-started/learning-about-github/github-glossary#fork>`__とは、GitHub 上のある`リポジトリ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#repository>`__を、あるアカウントから別のアカウントにコピーすることです。新しくフォークされたリポジトリは、`origin <https://docs.github.com/en/get-started/learning-about-github/github-glossary#origin>`__ リポジトリとの親子関係を保持します。フォークは通常、ソフトウェアが独立した開発ラインを持つ場合に使用されます。例えば、FTC チームが `FIRST-Tech-Challenge/FtcRobotController <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ リポジトリをベースに独自のチームコードを開発する場合などです。FTC チームは、ソフトウェア開発プロセスを管理する便利な方法として、`FIRST-Tech-Challenge/FtcRobotController <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ リポジトリのフォークを作成する必要があります。親子関係のおかげで、親リポジトリに変更が加えられた場合、それらの変更を簡単に追跡し、フォークされたリポジトリに`フェッチ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#fetch>`__/`マージ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#merge>`__することができ、フォークされたリポジトリを最新の状態に保つことができます。

.. warning:: 
   チームは、`upstream <https://docs.github.com/en/get-started/learning-about-github/github-glossary#upstream>`__ の親である FIRST-Tech-Challenge/FtcRobotContoller リポジトリに対してプルリクエストを発行しないでください。FIRST-Tech-Challenge/FtcRobotContoller リポジトリのフォークは、常に変更をフェッチすることはできますが、リポジトリに変更をプッシュすることは決して試みないでください。

`クローン <https://docs.github.com/en/get-started/learning-about-github/github-glossary#clone>`__は、通常はローカルコンピューター上のリポジトリのコピーです。チームメンバーは、機能開発のためにチームのリポジトリの`機能ブランチ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#clone>`__を作成し、そのブランチをローカルコンピューターにクローンします。ソフトウェアの開発とテストは、ローカルクローン内で完全に行われます。作業が完了するか、チェックポイントに到達したら、ローカルクローン内の変更をローカルクローンからチームのフォークにプッシュバックすることができます。その機能ブランチは、チームによって承認されると、チームのメインリポジトリブランチにマージすることができます。このプロセスを使用することで、複数の異なる開発者がシームレスに作業できます。


.. figure:: images/fork-clone-diagram.png 
   :align: center 
   :width: 70% 
   :alt: フォークとクローンの関係を示す図

   フォークとクローンの関係。クローンはローカルのラップトップ上に存在し、フォークは GitHub サーバー上に存在します。

ブランチ戦略 
-------------

`ブランチ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#branch>`__は、他の開発ラインから独立した一連の`コミット <https://docs.github.com/en/get-started/learning-about-github/github-glossary#commit>`__であり、通常はリポジトリの新機能を開発するために使用されます。FtcRobotController リポジトリとそのフォークおよびクローンのデフォルトブランチは、`master <https://docs.github.com/en/get-started/learning-about-github/github-glossary#master>`__ です（ただし、GitHub で作成されたすべての新しいリポジトリでは、デフォルトブランチは `main <https://docs.github.com/en/get-started/learning-about-github/github-glossary#main>`__ と呼ばれます）。ブランチを賢明に使用することで、変更を分離し、デフォルトブランチをクリーンに保ち、「本番環境対応」と見なされたソフトウェアから独立して機能開発を反復するためのスペースを提供することにより、開発者が共通のソフトウェアセットで協力することを支援できます。

.. figure:: images/single-branch.*
   :align: center
   :alt: 1つのブランチ

   master というデフォルト名を持つ単一のブランチ

各円は、ブランチへのコミットを表します。ブランチの名前は常に最新のコミットを指しており、これは `HEAD <https://docs.github.com/en/get-started/learning-about-github/github-glossary#head>`__ としても知られています。多くのブランチが存在する場合でも、HEAD は1つしかなく、`デタッチド状態 <https://git-scm.com/docs/git-checkout#_detached_head>`__でない限り、常に現在チェックアウトされているブランチの最新のコミットを指します。他のすべてのコミットは、その直接の親を指します。

コミットは、ある時点でのワークスペース全体の`スナップショット <https://docs.github.com/en/get-started/learning-about-github/github-glossary#snapshot>`__です。Git は `差分 <https://docs.github.com/en/get-started/learning-about-github/github-glossary#diff>`__を保存しません。ファイルに変更を加え、変更されたファイルで新しいコミットを作成すると、変更されたファイル全体がコミットに保存されます。ファイルの不必要な重複を避けるために、リポジトリが3つのファイルで構成されており、1つが変更され、他の2つが変更されていない場合、スナップショットは変更されていないデータを含むのではなく、変更されていないファイルを指すだけです。

各コミットには親があり、これにより git は異なるブランチからのコミットの到達可能性を判断できます。また、2つのブランチの共通祖先コミットを判断することもでき、これはブランチをマージする際に重要です。詳細については後述します。

では、ブランチとは何でしょうか？ブランチは、単にコミットへの名前付きポインタです。ブランチが作成されると、git に名前を作成し、それをコミットに向けるように指示するだけです。ブランチ上にいるということは、新しいコミットを追加すると、git がブランチ名を新しいコミットに移動し、新しいコミットの親は、ブランチ名が以前指していたコミットになることを意味します。これにより親から独立した開発ラインが作成されるため、開発者は他のチームメンバーの作業を妨げることなく、実験し、変更を加え、新機能を開発できます。開発者がブランチが共有できるほど安定していると判断したら、ブランチを親にマージバックできます。

.. figure:: images/two-branches.png
   :align: center
   :alt: 2つのブランチ

   同じコミットを指す2つのブランチ。

ブランチを作成した直後、新しいブランチ名は、新しいブランチが作成されたブランチの最新のコミットを単に指します。今、そのブランチに新しいコミットを作成すると想像してください。

.. figure:: images/new-commit-on-feature.png
   :align: center
   :alt: 2つのブランチ

   機能ブランチの新しいコミット。

新しいコミットにより、機能ブランチの名前ポインタが新しいコミットに移動した一方で、master ブランチの名前ポインタは以前のコミットに留まっていますが、新しいコミットの親は master の名前ポインタが指すコミットであることに注意してください。master ブランチに新しいコミットが追加されると、新しいコミットの親も master が指すコミットであり、これにより独立した開発ラインが作成されます。

.. figure:: images/new-commit-on-master.png
   :align: center
   :alt: 独立した開発ライン

   2つの独立した開発ライン。

最終的には、通常、その機能ブランチを master ブランチで表されるメイン開発ラインにマージバックしたいと考えます。あるブランチを別のブランチにマージすると、git はブランチの祖先コミットをトラバースして、共通の`祖先 <https://stackoverflow.com/questions/55203122/what-do-people-mean-when-they-say-ancestor-with-regards-to-git>`__を見つけます。次に、共通の祖先から各ブランチの先頭までに何が変更されたかを判断し、それらの変更を*マージコミット*と呼ばれる新しいコミットに適用します。このプロセスの結果として、マージコミットには2つの親が存在します。

.. figure:: images/merge-commit.png
   :align: center
   :alt: マージコミットのデモンストレーション

   機能ブランチを master ブランチにマージバックする。

上記のように、機能ブランチはまだ存在しています。機能ブランチに追加された新しいコミットは、master ブランチから再び分岐します。ただし、機能の開発が完了した場合、ブランチを削除できます。ブランチの削除は、名前ポインタが削除されるだけです。ブランチの削除により、そのブランチで行われたコミットが削除されることはありません。ここでわかるように、機能ブランチ上にあったコミットは依然として存在し、マージブランチから正しい親を参照することでアクセスできます。

チームのフォークとクローンのデフォルトブランチが FIRST-Tech-Challenge/FtcRobotController のデフォルトブランチと一致していることを確認することは有用です。ただし、典型的な開発パターンでは、チーム開発者が機能ブランチからのマージまたは master への直接コミットのいずれかを介して、チームソフトウェアを master ブランチにコミットバックします。

.. figure:: images/master-comparison.*
   :align: center 
   :alt: FTC master vs チーム master

   FIRST-Tech-Challenge/FtcRobotController の master と典型的なチームリポジトリの master の比較。

チームのコミットは青い円で表され、SDK アップデートを含むコミットは緑の円で表されます。紫色の円はマージコミットです。マージについては後述します。この例では、チームのコミットが SDK アップデート (1) と混在しており、2つのデフォルトブランチが一致しない状況を生み出しています。

   (1) 実際にはそうではないか、コミットの親子関係がどのように配置されているかによります。
   これは非常に単純化された見方ですが、論理的概念を示すには十分であり、単に `git log <https://www.atlassian.com/git/tutorials/git-log>`__ を実行した場合に得られる見方です。
   ブランチに関連するコミットで正確に何が起こっているかについての詳細でわかりやすい説明については、`このチュートリアルを参照してください <https://www.biteinteractive.com/picturing-git-conceptions-and-misconceptions/>`__。

これは完全に受け入れ可能であり、非常に一般的なブランチ管理戦略ですが、デフォルトブランチを分離して常に親と一致するようにすると、特定の利点が得られます。次の図は、master ブランチが FIRST-Tech-Challenge/FtcRobotController の master ブランチを追跡しているクローンを示しています。

.. figure:: images/clean-master.*
   :align: center 
   :alt: ブランチを同期させる

   チームリポジトリの master は常に FIRST-Tech-Challenge/FtcRobotController の master ブランチと一致します。

紫色のコミットは、v7.1 を competition ブランチにマージしたものです。この図では、v7.2 と v8.0 はマージされておらず、competition ブランチは SDK の v7.1 に対してビルドされます。

このモデルに従うということは、チームのリポジトリの master ブランチのコミット履歴が、常に FIRST-Tech-Challenge/FtcRobotController の master ブランチのコミット履歴と一致することを意味します。チームが競技で使用する予定のすべてのソフトウェアは、competition ブランチにマージされます。機能、新しいソフトウェア、実験などは、competition ブランチの子ブランチで作業され、master ブランチではなく competition ブランチにマージバックされます。チームクローンの master ブランチへの SDK アップデートは常に競合が発生せず、アップデートは competition ブランチへのマージとは独立して実行でき、開発への SDK アップデートのマージで問題が発生した場合、ブランチが一致しない master に直接アップデートをバックアウトする場合と比較して、復旧がより簡単になります。

ブランチの仕組みに関する詳細情報は、こちらを参照してください
`ブランチの使用 <https://www.atlassian.com/git/tutorials/using-branches>`__

はじめに（クイックスタートガイド） 
------------------------------------

.. important:: 
   以下では、すべての操作がローカルリポジトリの master ブランチで行われることを前提としています。

#. `GitForWindows <https://gitforwindows.org/>`__ を入手してインストールします。このソフトウェアには、bash シェルとともに git クライアントが含まれています。以下のすべてのコマンドラインスニペットは、bash シェルを使用しており、git がパスに含まれていることを前提としています。GitForWindows は、Windows マシンにこれを提供する最も簡単な方法です。Mac には terminal と呼ばれる組み込みの bash シェルがありますが、git は個別にインストールする必要があります。

#. `FIRST-Tech-Challenge/FtcRobotController <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ リポジトリを GitHub 上のあなたのアカウントにフォークします。

   .. tip::
      この手順には GitHub アカウントが必要であり、リポジトリをフォークするには GitHub にログインしている必要があります。

   .. figure:: images/fork.png 
      :align: center 
      :width: 80% 
      :alt: リポジトリのフォーク

      GitHub リポジトリのフォーク。

   リポジトリのフォークは、上の画像に示されている ":octicon:`repo-forked;1em;sd-text-info` Fork" ボタンをクリックするだけで簡単に行えます。これにより「新しいフォークを作成」ページに移動し、「所有者」と「リポジトリ名」のフィールドが自動入力されます。説明を入力し（オプション）、「``master`` ブランチのみをコピー」オプションをチェックしたままにして、緑色の「フォークを作成」ボタンをクリックするだけです。

   作成されると、フォーク名を編集しない限り、新しいフォークは ``github.com/<ユーザー名>/FtcRobotController`` に配置されます。

#. フォークからローカルコンピューターにクローンします。下の画像ではアカウントが FIRST-Tech-Challenge になっていますが、フォーク後は、アカウントはチームアカウントになる必要があります。他のすべての点で、ユーザーインターフェースは同じです。

   .. figure:: images/clone.png 
      :align: center 
      :width: 80% 
      :alt: リポジトリのクローン

      フォークされたリポジトリのクローン。

   FtcRobotController のフォークをクローンするには、次の手順に従います。

   #. 上の画像に示されている緑色の ":octicon:`code;1em;sd-text-info` Code" ボタンをクリックします。
   #. 「Local」と「HTTPS」のサブタブが選択されていることを確認します。
   #. ":octicon:`copy;1em;sd-text-info`" ボタンをクリックして、テキスト入力ボックス内の URL をコピーします。
   #. 適切なディレクトリで「Git Bash」シェルを開きます。Windows では、ファイルエクスプローラーを開き、リポジトリをクローンするディレクトリを見つけ、そのディレクトリフォルダを右クリックして「Git Bash here」を選択することで簡単に行えます。
   #. Git Bash シェル内で、次のコマンドを実行します

      .. code-block:: bash

         git clone <コピーしたURL>

#. Git がリポジトリのクローンをダウンロードします。完了したら、コーディングを始めましょう...

#. これは、必要に応じて機能開発用のブランチを作成できるポイントです。ブランチを作成するには、次の `git-checkout <https://git-scm.com/docs/git-checkout>`__ コマンドを使用して、新しいブランチを作成して切り替えることができます。

   .. code-block:: bash

      git checkout -b <ブランチ名>

   ``-b``オプションを使用すると、``<ブランチ名>``で指定された新しいブランチが作成され、自動的にそのブランチに切り替わります。``-b`` オプションを省略すると、既存のブランチがある場合、単にそのブランチに*切り替わります*。

ベストプラクティス 
^^^^^^^^^^^^^^^^^^^

- リポジトリ内の FtcRobotController ディレクトリのソフトウェアに変更を加えないでください。FtcRobotController ディレクトリ内の何も変更しない場合、SDK のアップデートがはるかに簡単になります。  
- 長期間存続するブランチの使用を制限してください。ブランチは機能を実装する必要があります。ブランチはマイルストーンを追跡すべきではありません。例えば、'league-meet-1' という名前のブランチはマイルストーンを追跡しています。ブランチがより小さな開発単位を追跡する方がはるかに良いです。'detect-target'、'drive-to-parking'、'drop-game-element' など。ソフトウェアをロボットが行うタスクに分解し、それらのタスクを実装するためにブランチを使用してください。これにより、共同開発がはるかに簡単になり、マージ時の変更セットがはるかに小さくなり、フェッチとマージがはるかに簡単になります。  
- `git index <http://shafiul.github.io/gitbook/1_the_git_index.html>`__ をクリーンに保つようにしてください。これにより、フェッチとマージが簡単になります。``git status``は、ここでの最良の友です。``git status`` を頻繁に使用して、ローカルワークスペースで何が変更されたかを確認してください。論理的なチャンクで頻繁にコミットして、最新の変更を簡単に確認できるようにしてください。  
- 短く、意味のあるコミットメッセージを使用してください。コミットメッセージにスラング、不快な表現、または個人的なメッセージを使用しないでください。ソフトウェアを GitHub にプッシュすると、それらのコミットメッセージは公開されます。最終的にプロフェッショナルなソフトウェア開発者になることを計画しており、既存の GitHub アカウントを保持している場合、潜在的な雇用主はあなたのコミットメッセージを確認できます。ここでは慎重に進んでください。

フォークとローカルクローンの更新  
----------------------------------

SDK の更新には、ローカルクローンとフォークの両方に新しくリリースされたソフトウェアをプルすることが含まれます。これを行うには2つの方法があります。親から github 上のフォークに直接ソフトウェアをフェッチしてマージし、次にローカルにフェッチしてマージするか、親からローカルクローンにフェッチし、ローカルでマージしてからフォークにプッシュします。

この著者は後者を好みます。なぜなら、開発者がフォークにプッシュする前に新しいソフトウェアをテストする機会を与えるからです。また、GitHub の UI を介してではなく、ローカルでマージの競合を解決することができます。

最新のソフトウェアの取得
^^^^^^^^^^^^^^^^^^^^^^^^

リポジトリを更新する方法を説明する際、多くの基本的なチュートリアルでは ``git pull``コマンドを使用します。``git pull`` コマンドは実際には、ユーザーの背後で *fetch* と *merge* を実行しています。これで問題ない場合もありますが、*フェッチ*と*マージ*の概念を独立した操作として理解することは有用です。問題が発生した場合、基礎となるメカニズムをよく理解していれば、その後の問題を修正できる可能性がはるかに高くなります。

リモート 
"""""""""

Git は基本的に、リポジトリの多くのコピーがインターネット上、他の人のマシン上、企業のファイルサーバー上、またはその他多数の場所に浮遊している可能性があるという考えを中心に構築されています。そして、これらのリポジトリはリモートで相互にリンクできます。リモートリポジトリは、単にどこか他の場所でホストされているリポジトリのバージョンとして定義されます。前述の例では、FtcRobotController のフォークはローカルクローンのリモートです。

   .. figure:: images/origin-remote.*
      :align: center 
      :alt: origin という名前のリモート

      `origin` という名前のリモートとしての FtcRobotController の図。

リモートは git コマンドで参照でき、リポジトリには任意の数のリモートを持つことができます。クローンされたリポジトリのリモートのデフォルト名は 'origin' です。フォークの親を追跡するリモートの慣習的な名前は 'upstream' です。

   .. figure:: images/two-remotes.*
      :align: center 
      :alt: 2つのリモートを持つリポジトリ

      2つのリモートを持つローカルリポジトリ。

特定のリポジトリに対して確立されているリモートを確認するには

   .. code-block:: console

      $ git remote -v

チームのフォークの親をローカルクローンのリモートとして追加するには

   .. code-block:: console

      $ git remote add upstream https://github.com/FIRST-Tech-Challenge/FtcRobotController.git

.. important::
   FIRST Tech Challenge FtcRobotController リポジトリをローカルクローンの upstream リモートとして設定すると、エイリアス名 'upstream' を使用して FIRST-Tech-Challenge/FtcRobotController からローカルクローンに変更をフェッチできます。これは非常に強力です。
   なぜこれが重要なのかがすぐにわからない場合は、上記の ``フォークとローカルクローンの更新`` というヘッダーの下の2つの段落を再度お読みください。

**このチュートリアルの残りの部分では、ローカルクローンに upstream として FIRST-Tech-Challenge/FtcRobotController を追加したことを前提としています。**

フェッチ 
"""""""""

フェッチは、リモートリポジトリからソフトウェアの変更をダウンロードするプロセスです。フェッチは、フェッチ先のリポジトリ内の既存のソフトウェアを**変更しない** ことに特に注意してください。git はローカルリポジトリ内の変更を分離します。

チームで作業していて、チームメイトが FtcRobotController フォークにソフトウェアをプッシュした場合、次のコマンドを実行してそのソフトウェアをローカルクローンにフェッチできます

   .. code-block:: console

      $ git fetch origin

これにより、origin という名前のリモート上のすべてのブランチで、ローカルリポジトリに存在しない変更がダウンロードされます。

   .. figure:: images/fetch-from-origin.*
      :align: center 
      :alt: origin からの変更のフェッチ

      origin からの変更のフェッチ。

マージ
""""""

マージは、フェッチされたソフトウェアをブランチ（最も一般的にはリポジトリの現在のブランチ）にマージするプロセスです。マージは、物事が最も混乱しやすい場所です。ただし、リモート master からローカル master に単純にマージしており、ローカル master が常にリモートを追跡している場合、マージはスムーズに進むはずです。

   .. figure:: images/merge-from-origin.png 
      :align: center 
      :alt: フェッチされた変更のマージ

      origin リポジトリからフェッチされた変更のマージ。

``master`` ブランチにいることを確認し、次のコマンドを実行します。

   .. code-block:: console

      $ git merge origin/master

この操作を実行するときは、``master``ブランチが*クリーン*である必要があります（つまり、``master``ブランチで``git status``を実行したときに、変更されているがコミットされていないファイルが表示されない）。チームメンバーは、``master`` ブランチではなく、機能ブランチで開発作業を行う必要があります。

競合 
"""""

競合、または「特定のコードに対して複数の変更が保留されている場合に何が起こるか」。`Git マージの競合 <https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts>`__ に関するこの優れたチュートリアルを読むのが最善です。
マージの競合はチームで作業する際の通常の一部であり、経験を積むことによってのみ、競合を効果的に管理する方法を学ぶことができます。常に忍耐強く、プロセスに深い敬意を払ってアプローチしてください。

SDK を最新バージョンに更新する
-------------------------------

.. important::
   ``git remote -v`` を使用して、クローンに upstream がリモートとして設定されていることを確認してください。設定されていない場合は、「リモート」セクションを再度確認して、クローンの upstream リモートに FtcRobotController リポジトリを追加してください。

SDK から更新するには、チームフォークの親である upstream、FIRST-Tech-Challenge/FtcRobotController からフェッチし、次にマージして origin にプッシュすることで更新を完了します。

   .. figure:: images/fetch-from-upstream.*
      :align: center 
      :alt: upstream からの変更のフェッチ

      upstream リポジトリからの変更のフェッチ。

origin からではなく upstream からフェッチします。これにより、ローカルクローンにまだ存在しないコミットがコピーされます。上の図では、それは v8.0 コミットです。ローカルの master は変更されません。まだ v7.2 コミットを指しており、それを表しています。コミットはある時点でのワークスペースの完全なスナップショットであるため、ワークスペースでは何も変更されませんが、リポジトリには upstream/master というブランチ名の新しいコミットがあります。

   .. code-block:: console

      $ git fetch upstream

   .. figure:: images/merge-from-upstream.png
      :align: center
      :alt: リモート

      upstream リポジトリからフェッチされた変更のマージ。

フェッチした後、upstream/master ブランチを master にマージします。ローカルの master が upstream の master と一致している場合、マージは master ブランチラベルを upstream/master が指しているコミットに移動するだけの簡単なものです。これは早送りマージと呼ばれます。そして、コミットはある時点でのワークスペースの完全なスナップショットであるため、ローカルワークスペースには v8.0 で表されるスナップショットが含まれるようになります。

   .. code-block:: console

      $ git merge upstream/master

   .. figure:: images/push-to-origin.png 
      :align: center 
      :alt: フェッチされた変更のプッシュ

      フェッチおよびマージされた変更をチームフォークにプッシュバック。

upstream/master をローカルクローンの master ブランチにマージしたら、それらの変更を GitHub にプッシュして、GitHub クローンが upstream リポジトリを反映するようにします。

   .. code-block:: console

      $ git push origin master

機能ブランチで作業していて、その機能ブランチに新しい SDK の変更を取り込みたい場合は、ブランチをチェックアウトしてマージコマンドを実行することで、master からブランチにマージします。これは、マージの競合が発生する可能性が最も高い場所であり、事態が複雑になる可能性があります。

   .. code-block:: console

      $ git checkout <機能ブランチ> 
      $ git merge master


SDK を以前のバージョンにダウングレードする
------------------------------------------

通常、ローカルリポジトリの作業ブランチ（master であろうと competition ブランチであろうと）は、最終的に SDK アップデートコミットと混在した一連のチームコミットを含むようになります。このシナリオでは、チームはすべてのチームコミットもロールバックせずに、単に以前の SDK バージョンにロールバックすることはできません。次の図を考えてみましょう。

   .. figure:: images/sample-rollback.png
      :align: center
      :alt: サンプルリポジトリ

      チームコミットと SDK アップデートコミットの両方を含むリポジトリ。

M7.2 でブランチを単に切り取ると、3つの青いチームコミットが失われます。チームの作業を保持するために、代わりに 8.0 コミットを元に戻す新しいマージコミットを作成します。M8.0 などのマージコミットは元に戻さないでください。マージコミット自体には、マージされた2つのブランチの分岐を表す作業が含まれている可能性があります。これはあなたが望むものではありません。新しい（古い）SDK バージョンを表すマージコミットの親を元に戻したいのです。

タグに関する短い余談
^^^^^^^^^^^^^^^^^^^^

タグは、ブランチポインタや HEAD とは異なり、決して移動しないコミットへの名前付きポインタです。コミットはワークスペース全体のある時点でのスナップショットであるため、これにより開発者はある時点を不変の方法で*タグ付け*できます。
*FIRST* は、標準的な`セマンティックバージョニング <https://semver.org/>`__ 命名スキームを通じて SDK バージョンを追跡するためにタグを使用します。新しい SDK バージョンがリリースされると、FTC エンジニアリングチームはリリース候補ブランチを FIRST-Tech-Challenge/FtcRobotController にプッシュし、次にそのブランチを master にマージします。これにより、すべての良いものが含まれる新しい SDK バージョンコミットと、候補ブランチから master へのマージを表すマージコミットの2つのコミットが作成されます。その後、リリースが正式にカットされ、マージコミットにタグが作成されます。

リモートからのタグは、クローン時にリポジトリに自動的にコピーされません。タグを取得するには、次を実行します。

   .. code-block:: console

      $ git fetch --all --tags

--all オプションはすべてのリモートから一度にフェッチし、--tags オプションは git にタグをフェッチするよう指示します。
タグは常にセマンティックバージョニングルールに従います。例: v7.0、v7.1、v7.2、v8.0 など。

`^ 構文 <https://medium.com/@gabicle/git-ancestry-references-explained-bd3a84a0b821>`__ を使用すると、コミットの親を参照でき、タグ名に適用できます。tag^ は、タグが指すコミットの直接の親です。マージコミットなどの複数の親を持つコミットの場合、数字を適用して特定の親を参照できます。
tag^1 は tag^ と同じで、コミットの最初の親です。tag^2 はコミットの2番目の親です。

SDK アップデートの逆のマージ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

下の図は、v8.0 タグが v8.0 マージコミットを指しており、v8.0 の親への参照も示しています。

   .. figure:: images/tags.png
      :align: center
      :alt: タグ

      v8.0 マージコミットを指す v8.0 タグ。

.. important:: 元に戻されたバージョンで導入された新機能または API に依存するコミットがある場合、ビルドは失敗します。ソフトウェアが元に戻されたソフトウェアに依存しなくなるように、ソフトウェアを修正する方法を手動で見つける必要があります。

Git はコミットを削除しない（いくつかの例外を除いて）ことを覚えておいてください。したがって、コミットを元に戻すには、元に戻したいコミット*から*の逆のコミットを作成する必要があります。そして、元に戻したいすべてのバージョンについて、逆の順序でこれを行う必要があります。以下のコマンドのターゲットは、元に戻したいバージョンのタグであり、元に戻す先のバージョンのタグではありません。

   .. figure:: images/revert.png
      :align: center
      :alt: 元に戻すことのデモンストレーション

      元に戻した結果 - v8.0 から v7.2 への元に戻しを表す新しいマージコミット。

マージコミットには2つの親があり、SDK バージョンコミットを参照したいため、ロールバックしたいタグ名を使用し、^2 を追加します。例えば、v8.0 をロールバックし、SDK が v7.2 に対してコンパイルされるようにするには、次を使用します。

   .. code-block:: console

      $ git revert -Xtheirs v8.0^2

-Xtheirs オプションは、「競合がある場合は、v8.0^2 側からソフトウェアを自動的に取得する」という便利なオプションです。

.. warning:: 複数のリビジョンをダウングレードする場合、各リビジョンを順番に元に戻す必要があります。そうしないと、最新バージョンと参照しているターゲットの間の SDK バージョンからの元に戻し後に変更が残る可能性があります。例えば、v8.1.1 から v8.0 にダウングレードする必要がある場合（参考までに、すべての SDK バージョンは
   `こちら <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ にあります）、v8.1.1 を元に戻し、次に v8.1 を元に戻す必要があります。この順序に従わないと、v8.1 と重複しない v8.1.1 の変更がワークスペースに残り、それは望ましくありません。

まとめ
------

すべてのコマンドは、ローカルクローンのルートディレクトリから実行されることを前提としています。また、ローカルの master ブランチにチームコードをコミットするのではなく、competition ブランチで作業していることを前提としています。

FIRST-Tech-Challenge/FtcRobotController をリモートとして追加
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code-block:: console

      $ git remote add upstream https://github.com/FIRST-Tech-Challenge/FtcRobotController.git

最新の SDK バージョンに更新
^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code-block:: console

      $ git checkout master
      $ git fetch upstream
      $ git merge upstream/master
      $ git push origin master
      $ git checkout competition
      $ git merge master
