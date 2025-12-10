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

2. :doc:`Intro to Codesapces <../codespaces/codespaces>` :bdg-secondary:`Information`

    * これは **Codespaces** の概要と使用方法を提供します。
3. :doc:`Getting to know the GitHub Repository <../github_repo/github-repo>` :bdg-secondary:`Information`

    * これは FTC Docs リポジトリの概要と構成方法を提供します。貢献作業を開始する前に理解することが重要です。 

4. :doc:`Fork the repository <../make_fork/make-fork>` :bdg-danger:`One Time Only` :bdg-info:`Codespaces` :bdg-warning:`Local`

    * これにより、あなたの **GitHub** アカウントに FTC Docs リポジトリのコピーが作成されます。

5. :doc:`Update the repository <../update_fork/update-fork>` :bdg-success:`Repeat` :bdg-info:`Codespaces` :bdg-warning:`Local`

    * これにより、フォークが FTC Docs リポジトリの最新の変更で更新されます。新しい貢献作業を開始する前にこれを行うことが重要です。

6. :doc:`Set up your environment <../setup/setup>` :bdg-danger:`One Time Only` :bdg-warning:`Local`

    * This will set up your local environment to work on FTC Docs. This step can be skipped for Codespaces users.

7. :doc:`Create a new branch <../make_branch/make-branch>` :bdg-success:`Repeat` :bdg-info:`Codespaces` :bdg-warning:`Local`

    * This will create a new branch for your change. You should create a new branch for each change you work on.

8. :doc:`Create a new codespace <../create_codespace/create-codespace>` :bdg-success:`Repeat` :bdg-info:`Codespaces`

    * This will create a new Codespace for your change. You should create a new Codespace for each change/branch you work on. 

9. :doc:`Switch to your branch <../switch_branch/switch-branch>` :bdg-success:`Repeat` :bdg-warning:`Local`

    * This will switch to the branch you created in step 7. You should switch to the branch you created for each change you work on.
  
10. :doc:`VS Code Tasks <../tasks/tasks>` :bdg-secondary:`Information`

    * This will provide an overview of the tasks for FTC Docs available in VS Code. This is important to understand before you start working on a contribution.

11. :doc:`Make your changes <../make_rst/index>` :bdg-success:`Repeat` :bdg-info:`Codespaces` :bdg-warning:`Local`

12. :doc:`Setup Git Credentials <../setup_credentials/setup-credentials>`  :bdg-danger:`One Time Only` :bdg-warning:`Local`

    * This will set up your Git credentials so you can push your changes.

13. :doc:`Submit your changes <../make_pr/make-pr>` :bdg-success:`Repeat` :bdg-info:`Codespaces` :bdg-warning:`Local`

    * Commit your changes and submit a pull request to the FTC Docs repository.