概要
=========

以下は、FTC Docs への貢献プロセスの概要です。

.. warning::

    Using **Codespace** and working **Locally** are two different ways to contribute to FTC Docs. 
    The steps for each are similar, but there are key differences in setup. After reading step 2, you should choose whether you want to use Codespaces or work locally.
    For the purposes of this guide, Local and Codespaces use will be mutually exclusive.

.. admonition:: Key 

    .. list-table::
        
        * - :bdg-danger:`One Time Only`
          - :bdg-success:`Repeat`
          - :bdg-info:`Codespaces`
          - :bdg-warning:`Local`
          - :bdg-secondary:`Information`
          
          
        * - Step only needs to be done once
          - Step must be repeated for each set of changes
          - Step specific to Codespaces users
          - Step specific to Local users
          - General information that provides context

2. :doc:`**Codespaces** 入門 <../codespaces/codespaces>` :bdg-secondary:`情報`

    * これは **Codespaces** の概要と使用方法を提供します。
3. :doc:`**GitHub** リポジトリを知る <../github_repo/github-repo>` :bdg-secondary:`情報`

    * これは FTC Docs リポジトリの概要と構成方法を提供します。貢献作業を開始する前に理解することが重要です。 

4. :doc:`リポジトリをフォークする <../make_fork/make-fork>` :bdg-danger:`1回のみ` :bdg-info:`Codespaces` :bdg-warning:`ローカル`

    * これにより、あなたの **GitHub** アカウントに FTC Docs リポジトリのコピーが作成されます。

5. :doc:`リポジトリを更新する <../update_fork/update-fork>` :bdg-success:`繰り返し` :bdg-info:`Codespaces` :bdg-warning:`ローカル`

    * これにより、フォークが FTC Docs リポジトリの最新の変更で更新されます。新しい貢献作業を開始する前にこれを行うことが重要です。

6. :doc:`環境をセットアップする <../setup/setup>` :bdg-danger:`1回のみ` :bdg-warning:`ローカル`

    * これにより、FTC Docs で作業するためのローカル環境がセットアップされます。**Codespaces** ユーザーはこのステップをスキップできます。

7. :doc:`新しいブランチを作成する <../make_branch/make-branch>` :bdg-success:`繰り返し` :bdg-info:`Codespaces` :bdg-warning:`ローカル`

    * これにより、変更用の新しいブランチが作成されます。作業する変更ごとに新しいブランチを作成する必要があります。

8. :doc:`Create a new codespace <../create_codespace/create-codespace>` :bdg-success:`Repeat` :bdg-info:`Codespaces`

    * これにより、変更用の新しい **Codespace** が作成されます。作業する変更/ブランチごとに新しい **Codespace** を作成する必要があります。 

9. :doc:`Switch to your branch <../switch_branch/switch-branch>` :bdg-success:`Repeat` :bdg-warning:`Local`

    * これにより、ステップ 7 で作成したブランチに切り替わります。作業する変更ごとに作成したブランチに切り替える必要があります。
  
10. :doc:`VS Code Tasks <../tasks/tasks>` :bdg-secondary:`Information`

    * これにより、**VS Code** で利用可能な FTC Docs のタスクの概要が提供されます。貢献作業を開始する前に理解することが重要です。

11. :doc:`Make your changes <../make_rst/index>` :bdg-success:`Repeat` :bdg-info:`Codespaces` :bdg-warning:`Local`

12. :doc:`Setup Git Credentials <../setup_credentials/setup-credentials>`  :bdg-danger:`One Time Only` :bdg-warning:`Local`

    * これにより、変更をプッシュできるように **Git** 認証情報がセットアップされます。

13. :doc:`Submit your changes <../make_pr/make-pr>` :bdg-success:`Repeat` :bdg-info:`Codespaces` :bdg-warning:`Local`

    * 変更をコミットし、FTC Docs リポジトリにプルリクエストを送信します。