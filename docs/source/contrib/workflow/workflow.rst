FTC ドキュメントワークフロー
============================
.. note::
    このフローチャートは、FTC Docs リポジトリの*メンテナー*向けの参考用です。
    FTC Docs ドキュメントへの貢献のみを希望する方は、
    :doc:`FTC ドキュメントへの貢献 </contrib/tutorials/index>` ドキュメントを参照してください。

概要
--------

以下の図は、様々な GitHub リポジトリと、それらとビルド成果物の間のアクションとフローを示しています。
FTC Docs リポジトリへのプルリクエストは、HTML ページと PDF ファイルをビルドする GitHub アクションを実行します。
HTML ページは最終的に ftc-docs.firstinspires.org ウェブサイトに配置され、PDF ファイルは AWS S3 ファイルストレージに配置されます。

ウェブブラウザーでは、この図をマウスを使用してズームおよびパンできます。
スクロールホイールを使用してズームイン・ズームアウトできます。右クリックしてホールドし、ドラッグしてパンします。
この図はキーボードでアクセスできません。
スクリーンリーダーは、図の様々なノードとアクションを読み上げ、図の Translation セクションから開始します。

.. mermaid::
   :zoom:

    flowchart LR
        private[Private Github Repo]
        source[FTC Docs Github Repo]
        translation-repo[FTC Docs Translation Repo]
        transifex[Transifex]
        aws-s3[AWS S3]
        booklets[Booklet Builder]
        site[ftc-docs.firstinspires.org]
        cdn[ftc-docs-cdn.ftclive.org]
        contributors[Contributors]


        rtd-ftcdocs-en[RTD FTC Docs]
        rtd-ftcdocs-es[RTD FTC Docs Spanish]
        rtd-ftcdocs-fr[RTD FTC Docs French]

        private-->|Release Content|source
        contributors-->|Pull Request|source
        source-->|GitHub Action|translation-repo

        subgraph Translation
        direction BT
        transifex-->|.po files|translation-repo
        translation-repo-->|.pot files|transifex
        end
        
        source-->|GitHub Action|booklets
        booklets-->|Booklets in all languages|aws-s3
        aws-s3 --> cdn
        translation-repo-->booklets

        source-->|reST|rtd-ftcdocs-en
        translation-repo-->|Webhook|rtd-ftcdocs-es
        translation-repo-->|Webhook|rtd-ftcdocs-fr

        rtd-ftcdocs-en -->|HTML and Main PDF|site
        rtd-ftcdocs-es -->|HTML and Main PDF|site
        rtd-ftcdocs-fr -->|HTML and Main PDF|site
