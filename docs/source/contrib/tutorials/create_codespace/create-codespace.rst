Codespace の作成
=====================
:bdg-success:`Repeat` :bdg-info:`Codespaces`

リポジトリで作成する新しいブランチごとに、新しい Codespace を作成する必要があります。
これは、メインブランチにマージする前にコードを実行してテストできる仮想環境です。
Codespace の作成には数分かかる場合がありますが、一度作成されると、ブラウザからアクセスでき、その後のアクセスははるかに高速になります。

Steps
-----

1. **GitHub** であなたの** フォークした** リポジトリを開きます。
2. ページの左側で、作業したいブランチを選択します。

   .. image:: images/select-branch.png
      :alt: Screen shot showing the Demo branch is selected.

3. 緑色の **Code** ボタンをクリックすると、**Local** と**Codespaces** タブが表示されるので、**Codespaces** タブをクリックします。

   .. image:: images/select-cs.png
      :alt: Screen shot showing the Codespace tab being clicked.

4. 「Create codespace on」と書かれた緑色のボタンをクリックします。

   .. image:: images/create-cs.png
      :alt: Screen shot showing the green button that says create codespace on.

5. Codespace が作成されるまで待ちます。これには数分かかる場合があります。
6. Codespace が作成されると、ブラウザで Codespace に移動します。
   これはブラウザベースの **VS Code** のバージョンで、変更を行い、HTML ページをビルドして変更を確認するために使用できます。
7. ``CTRL + SHIFT + B`` を入力してプロジェクトをビルドします。**Terminal** メニューからビルドタスクを実行することもできます。

   .. image:: images/run-build-task.png
      :alt: Screen shot of Terminal menu with Run Build Task selected.
      
8. ビルドメッセージが表示されます。「build succeeded」メッセージを確認してください。
   その後、アプリケーションが実行中であることを示すポップアップが表示されます。 
   
   .. image:: images/build-messages.png
      :alt: Screen shot of build messages with Open in Browser button.

9. **Open in Browser** ボタンをクリックすると、ビルドしたばかりの HTML ページを表示する新しいタブが開きます。

10. これで変更を加えることができます。:doc:`/contrib/tutorials/make_rst/index` のセクションを参照してください。
