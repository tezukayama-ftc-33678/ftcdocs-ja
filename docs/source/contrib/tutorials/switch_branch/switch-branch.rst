ブランチの切り替え
==================
:bdg-success:`Repeat` :bdg-warning:`Local`

.. warning::
   ローカルでサイトを開発することを選択した場合にのみ、これらの手順を完了してください。
   **GitHub Codespaces** を使用している場合は、このセクションをスキップする必要があります。

この手順は、作業しているブランチを変更するために必要です。ブランチで作業していて別のブランチに切り替えたい場合は、次のコマンドを使用できます：

.. code-block:: bash

    git checkout <branch_name>

``<branch_name>`` を、切り替えたいブランチの名前に置き換えてください。また、前の手順で作成したブランチの名前と一致していることを確認してください。

Troubleshooting
---------------

Branch Not Found
~~~~~~~~~~~~~~~~

``error: pathspec '<branch-name>' did not match any file(s) known to git``

このエラーは、切り替えようとしているブランチが存在しない場合に発生します。切り替えようとしているブランチを作成していること、タイプミスがないことを確認してください。ただし、
ローカルリポジトリがリモートリポジトリと同期していない場合にも発生する可能性があります。これを修正するには、次のコマンドを実行できます：

.. code-block:: bash

    git fetch

このコマンドは、ローカルリポジトリをリモートリポジトリで更新します。このコマンドを実行した後、ブランチの切り替えを再度試してください。

Uncommitted Changes
~~~~~~~~~~~~~~~~~~~~

``error: Your local changes to the following files would be overwritten by checkout:``

This error occurs when you have uncommitted changes in your working directory. You can either commit your changes, stash them, or delete them. To commit your changes, you can use the following command:

.. code-block:: bash

    git commit -m "Your commit message"

This command will commit your changes with the message you provide.

To stash your changes, you can use the following command:

.. code-block:: bash

    git stash

Stashing allows you to save your changes for later without committing them. After stashing your changes, you can switch branches. To apply your stashed changes, you can use the following command:

.. code-block:: bash

    git stash apply

It is best to use ``git stash`` when you are not ready to commit your changes but need to switch branches.

To delete your changes, you can use the following command:

.. warning:: This command will delete all uncommitted changes in your working directory. It is not recommended to use this command unless you are sure you want to delete your changes.
.. code-block:: bash

    git reset --hard
