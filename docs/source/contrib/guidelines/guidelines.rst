貢献ガイドライン
=======================

貢献者はプロジェクトの生命線です。貢献を歓迎しますが、すべての方に 
:doc:`Gracious Professional </gracious_professionalism/gp>` であることを思い出していただきたいと思います。

Issue の作成
------------------

まず、問題や希望する機能を説明する Issue を作成してください。
これにより、その段階で問題が解決するか、リクエストや実施すべき作業が明確になる可能性のある議論が可能になります。

Issue には2つのタイプがあります：バグと機能リクエストです。バグレポートは、ドキュメントの問題を説明する Issue です。機能リクエストは、ドキュメントに追加すべき新機能を説明する Issue です。

どちらを作成する場合も、必ず重複がないか確認してください。重複を見つけた場合は、その Issue にコメントし、可能な限り入力を追加してください。可能であれば、問題を修正するプルリクエストを見せていただけると嬉しいです。問題の修正方法がわからない場合は、それで問題ありません。 

バグレポート
-------------

* バグの説明
* 期待される動作
* バグを再現する手順（該当する場合）
* スクリーンショット（該当する場合）

機能リクエスト
------------------

* 機能の説明
* この機能を追加すべきだと思う理由
* スクリーンショット（該当する場合）

プルリクエストの作成
-----------------------

プルリクエスト（PR）は、あるブランチから別のブランチへの変更セットをマージする提案です。
プルリクエストでは、協力者が変更をメインコードベースに統合する前に、提案された変更セットをレビューして議論できます。
GitHub では、PR はソースブランチのコンテンツとターゲットブランチのコンテンツの違いを表示します。

PR は GitHub の `FTC Docs <https://github.com/FIRST-Tech-Challenge/ftcdocs>`_ リポジトリに作成する必要があります。タイトルは、PR の目的を*簡潔*に説明することを目指してください。PR の作成の詳細については、GitHub の 
`creating a pull request <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_
を参照してください。
変更を行うための具体的なガイダンスがあります。:doc:`変更の概要 </contrib/tutorials/overview/overview>` から始めてください。

奥付
--------

FTC Docs は、`Read the Docs <https://readthedocs.org/>`__ が提供する `テーマ <https://github.com/readthedocs/sphinx_rtd_theme>`__ を使用して `Sphinx <https://www.sphinx-doc.org/>`__ で構築されています。

Sphinx はドキュメント生成ツールです。
Sphinx は reStructuredText ファイルを HTML ウェブページに変換します。
Read the Docs はドキュメントホスティングプラットフォームであり、FTC Docs のベース Sphinx テーマを提供しています。

`ダークテーマ <https://github.com/FIRST-Tech-Challenge/ftcdocs-helper/tree/main/sphinx_rtd_dark_mode_v2>`__ は FTC Docs 開発チームによって提供されています。

.. We might wish to state what version of Sphinx we use and other version info.
   This is also where we could declare what versions of HTML, XML, CSS we target. Perhaps what browsers we target. 
   (X)HTML, CSS, or usability standards compliance information and links to website validation tests. This used to be a thing, not so much anymore.
   Perhaps that we are WCAG compliant someday.

