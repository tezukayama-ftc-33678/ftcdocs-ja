旧 Self-Inspect
================

はじめに
--------

このページでは、FTC Driver Station（DS）アプリと FTC Robot Controller（RC）アプリにある旧式の Self Inspect 画面について説明します。
バージョン 10.3 以降の画面画像は :doc:`new self-inspect<new-self-inspect>` を参照してください。

Self Inspect 画面は、制御システムに関する FTC ルールとの関連で、デバイスの状態をスナップショットとして示します。
これらのルールは *FIRST* ウェブサイトの `Current Game and Season Materials page <https://ftc-resources.firstinspires.org/files/ftc/game>`__ に掲載されている Competition Manual に記載されています。

.. tip:: イベント前に ROBOT をセルフチェックするための `Inspection Checklist PDF <https://ftc-resources.firstinspires.org/ftc/event/inspection-check>`__ が利用できます。大会前にセルフチェックすることを強く推奨します。

Self Inspect 画面は、制御システムの要素が最新かつ正しく設定されているかをチームがすぐに確認するための簡易リファレンスとして提供されています。
FTC 大会の Robot Inspection で確認されることはありますが、FTC ルールへの準拠を網羅的に、あるいは公式に保証するものでは **ありません** 。

各検査画面は、Restart Robot の有無にかかわらず自動で更新されます。これにより、問題が解消されたことを素早く確認できます。

小さな画面に有用な情報を最大限に詰め込むことが課題です。Self Inspect のレイアウトとグラフィックは FTC の要件に合わせて進化しており、このページでは簡潔ながら重要なキャプションを補足します。

.. note::
  ここに示す画像は FTC アプリのバージョン 7.0 です。使用が認められるソフトウェアのバージョンは Competition Manual を参照してください。これらの画像は FTC アプリのバージョン 10.2 まで有効です。バージョン 10.3 以降の画面画像は :doc:`new self-inspect<new-self-inspect>` を参照してください。

デバイスのペアリング
--------------------

ペアリングの方法は Self Inspect の結果に大きく関わります。RC スマホは **Wi-Fi Direct** でホストし、Control Hub は**Standard（インフラストラクチャ）Wi-Fi** でホストすることを覚えておいてください。

DS アプリの Settings で選択した Pairing Method（Wi-Fi Direct または Control Hub）が、DS Self Inspect レポートでの合否判定に影響します。以下の例で説明します。

RC スマホと DS スマホはともに Airplane Mode を **ON**、Wi-Fi を**ON** としつつ、インターネットルーターやホットスポットなど Standard/infra Wi-Fi ホストには接続しないでください。近くの Wi-Fi は**Forget** に設定しておく必要があります。

FTC 制御デバイスの組み合わせは次のとおりです。

- **DS** スマホ +**RC** スマホ
- **DS** スマホ +**Control Hub**
- **Driver Hub**+**RC** スマホ
- **Driver Hub**+**Control Hub**

DS デバイス（スマホまたは Driver Hub）は自分自身の DS Self Inspect **と** 、ペアになっている RC スマホまたは Control Hub の RC Self Inspect を表示できます。RC スマホは自分自身の RC Self Inspect のみ表示できます。

つまり Self Inspect 画面は次のように表示されます。

**DRIVER STATION**

- `DS Self Inspect 1 <#ds-self-inspect-1-on-ds-phone-paired-to-rc-phone>`__（**DS** スマホ +**RC** スマホ）
- `DS Self Inspect 2 <#ds-self-inspect-2-on-ds-phone-paired-to-control-hub>`__（**DS** スマホ +**Control Hub** ）
- `DS Self Inspect 3 <#ds-self-inspect-3-on-driver-hub-paired-to-rc-phone>`__（**Driver Hub**+**RC** スマホ）
- `DS Self Inspect 4 <#ds-self-inspect-4-on-driver-hub-paired-to-control-hub>`__（**Driver Hub**+**Control Hub** ）

**ROBOT CONTROLLER**

- `RC Self Inspect 1 <#rc-self-inspect-1-appearing-on-rc-phone-paired-with-ds-phone>`__（RC スマホ上、DS スマホとペア）
- `RC Self Inspect 2 <#rc-self-inspect-2-appearing-on-ds-phone-paired-to-rc-phone>`__（DS スマホ上、RC スマホとペア）
- `RC Self Inspect 3 <#rc-self-inspect-3-appearing-on-rc-phone-paired-with-driver-hub>`__（RC スマホ上、Driver Hub とペア）
- `RC Self Inspect 4 <#rc-self-inspect-4-appearing-on-driver-hub-paired-to-rc-phone>`__（Driver Hub 上、RC スマホとペア）
- `RC Self Inspect 5 <#rc-self-inspect-5-appearing-on-ds-phone-paired-to-control-hub>`__（DS スマホ上、Control Hub とペア）
- `RC Self Inspect 6 <#rc-self-inspect-6-appearing-on-driver-hub-paired-to-control-hub>`__（Driver Hub 上、Control Hub とペア）

これらの組み合わせでは、Self Inspect のカテゴリや表示文言、合否結果が**わずかに異なる** ことがあります。各デバイスと組み合わせの Self Inspect 画面は、以下の**青いリンク** をクリックして確認してください。

.. _ds-self-inspect-1-on-ds-phone-paired-to-rc-phone:

DS Self Inspect 1（DS スマホ + RC スマホ）
------------------------------------------

.. figure:: images/nDS-1.png
   :align: center
   :width: 85%
   :alt: DS 1

   DS Self Inspect 1（DS スマホ + RC スマホ）

- 項目 1 は 1 つだけ選べるメニューで、“Disconnect from Wi-Fi Direct” です。機能しますが、アプリが自動で再ペアリングする場合があります。
- 項目 5 には対象デバイスのバッテリー残量が表示されます。豆知識として、パーセンテージの緑色は残量が減るにつれて **オレンジ** に変わっていきます。
- 項目 8 の ``Location services`` は **Android 8** 以上のデバイスにだけ表示されます。これは SDK/Android の技術要件であり、FTC ルールではありません。
- 項目 9 と 10 は「Yes」「No」である必要があります。``Wi-Fi Enabled`` は DS デバイスの Wi-Fi 無線が Wi-Fi Direct を使うために **ON** であることを意味します。RC スマホとペアにする際は、インターネットルーターや Control Hub など Standard/インフラ Wi-Fi には** 接続しない** でください。
- 項目 11 は **デバイスの Wi-Fi Direct 名** が FTC の形式要件を満たしているかを示します。ペア相手の RC 名（チーム番号）が一致しているかは確認しません。この例では 2468-A-DS と 2468-A-RC という合法名です。DS Settings（Driver Station Name）では FTC 合法名のみ入力できますが、DS スマホの Android Wi-Fi Direct 設定では任意の名前を入力できます。
- 項目 12 は DS デバイスに RC アプリが **インストールされていない** ことを確認します。
- 項目 13 は、デバイスのシステム日付に基づき、DS アプリが **当該 FTC シーズンの最小バージョン** を満たしているかを確認します。ここが「incorrect」で赤く表示された場合は、**Android の設定** で日付を修正すると解消します。

同じ電話で Self Inspect が多くの項目を**不合格** とした例がこちらです。

.. figure:: images/tDS-1-BAD.png
   :align: center
   :width: 85%
   :alt: DS 1 Bad

   DS Self Inspect 1（DS スマホ）– 不合格例

- 項目 6 は ``Airplane Mode`` が **OFF** であるため不合格です。FTC 用の電話では ON にする必要があります。これは Android システム設定で、設定メニューから、または画面上部を 2 回スワイプダウンして簡単にアクセスできます。Airplane Mode を ON にすると Android の「便利機能」として自動で Wi-Fi 無線が OFF になります。FTC ユーザーは手動で Wi-Fi 無線を ON に戻してください（ローカルホットスポットやインターネットルーターには接続しないでください）。
- 項目 7 は ``Bluetooth`` が **ON** なので不合格です。FTC では OFF にする必要があります。これも Android システム設定で、2 回スワイプダウンするか設定メニューを開いてください。
- 項目 8 は ``Location services`` が **OFF** なので不合格です。**Android 8** 以上では FTC アプリが位置情報を必要とします。これも Android システム設定で、2 回スワイプダウンするか設定メニューを確認してください。
- 項目 9 は DS スマホの Wi-Fi 無線が **ON** であることを示し、RC への Wi-Fi Direct 接続または Standard Wi-Fi 接続に必要です。
- 項目 10 は、DS の Pairing Method が Wi-Fi Direct（RC スマホと接続する前提）なのに、DS スマホが Standard/インフラ Wi-Fi に接続しているため不合格です。この例では家庭用 Wi-Fi に接続しています。こうしたネットワークはデバイスの Android Wi-Fi メニューで **Forget** に設定してください。一時的にインターネットが必要な場合は、使用後に必ず Forget に戻します。また、インターネット利用中に使った Google などのアカウントは**Remove Account** してください。そうしたアカウントはバックグラウンドでの通信や通知、アップデートを引き起こし、最悪のタイミングで妨げになることがあります。
- 項目 11 はデバイスの **Wi-Fi Direct 名** が FTC の形式要件を満たしていないため不合格です。この不適切な名前は DS スマホの Android Wi-Fi Direct 設定で付けたもので、アプリの DS Settings（Driver Station Name）では設定できません。
- 項目 12 は、この DS デバイスに RC アプリがインストールされているため不合格です。不合格の理由は旧バージョン（6.2）であることではなく、RC アプリが存在すること自体です。

.. _ds-self-inspect-2-on-ds-phone-paired-to-control-hub:

DS Self Inspect 2（DS スマホ + Control Hub）
--------------------------------------------

.. figure:: images/tDS-2.png
   :align: center
   :width: 85%
   :alt: DS 2

   DS Self Inspect 2（DS スマホ + Control Hub）

基本的なポイントは DS Self Inspect 1 と同じですが、次の点が異なります。

- 項目 9 と 10 はどちらも Yes である必要があります。DS スマホの Wi-Fi 無線は **ON** で、Standard/インフラ Wi-Fi に接続しています。何に接続しているかは項目 11 で示されます。
- DS の Pairing Method が Wi-Fi Direct（RC スマホと接続する前提）に設定されていると、項目 10 の Yes は **不合格** になります。
- 項目 11 には DS スマホが接続している Standard Wi-Fi の **ネットワーク名（Access Point, AP）** が表示されます。チェックマークは、その AP が FTC 合法デバイス（Control Hub）であり、名前が正しい形式であることを示します。DS 名と RC 名（チーム番号）が一致しているかは確認しません。この例では DS スマホは 2468-A-DS、Control Hub は 9999-A-RC であり、FTC チームまたは Robot Inspector が指摘すべき**違反の組み合わせ** です。

.. _ds-self-inspect-3-on-driver-hub-paired-to-rc-phone:

DS Self Inspect 3（Driver Hub + RC スマホ）
-------------------------------------------

.. figure:: images/tDS-3a.png
   :align: center
   :width: 85%
   :alt: DS 3a

   DS Self Inspect 3（Driver Hub + RC スマホ）

- 項目 4 は Driver Hub のみに表示されます。チェックマークは、Operating System が FTC Competition Manual の最小バージョン要件を満たしていることを示します。
- Driver Hub では DS 側の検査から ``Airplane Mode`` が省かれています。FTC ルールでは Driver Hub と Control Hub は Airplane Mode 要件の対象外です。
- 項目 8 の ``Location services`` は **Android 8** 以上のデバイスにだけ表示されます。これは SDK/Android の技術要件であり、FTC ルールではありません。
- 項目 9 と 10 は「Yes」「No」である必要があります。``Wi-Fi Enabled`` は Driver Hub の Wi-Fi 無線が RC スマホとの Wi-Fi Direct 用に **ON** であることを意味します。Driver Hub は技術的には Standard/インフラ Wi-Fi（インターネットルーターや Control Hub を含む）にも** 同時接続できてしまう** ため、項目 10 で接続していないことを確認します。次の例を参照してください。
- DS の Pairing Method が Control Hub に設定されている場合、項目 10 の No は **不合格** になります。
- 項目 11 は **デバイス名** が FTC の形式要件を満たしているかを示します。ペア相手の RC 名（チーム番号）が一致しているかは確認しません。
- 項目 12 は Driver Hub に RC アプリが **インストールされていない** ことを確認します。
- 項目 13 は、デバイスのシステム日付に基づき、DS アプリが **当該 FTC シーズンの最小バージョン** を満たしているかを確認します。この例では DS アプリ 7.0.1 が RC スマホの 7.0 と完全一致していませんが、こうした「Point mismatch」は FTC の最新ルール（2021-2022 シーズンの Q&A #176）で許容されています。それ以外で赤い「incorrect」になる場合は**Android の設定** で日付を修正してください。

.. figure:: images/tDS-3b.png
   :align: center
   :width: 85%
   :alt: DS 3b

   DS Self Inspect 3（Driver Hub + RC スマホ）

この Self Inspect 画面は、Driver Hub が RC スマホとペアリングされている最中に、さらに Standard Wi-Fi 経由で Control Hub に *同時接続* した際に表示されました。DS のホーム画面は一時的に「Connected」（RC スマホ）と「No Heartbeat」を示しましたが、その後 RC スマホとのペアリングに戻りました。

- 項目 10 がこの不整合を示しています。DS アプリはまもなくこの Standard Wi-Fi 接続を切断し、Driver Hub が RC スマホとのみペアを維持するようにします。

.. _ds-self-inspect-4-on-driver-hub-paired-to-control-hub:

**DS Self Inspect 4** （**Driver Hub**+**Control Hub** ）
-----------------------------------------------------------

.. figure:: images/tDS-4b.png
   :align: center
   :width: 85%
   :alt: DS 4b

   DS Self Inspect 4（Driver Hub + Control Hub）

- 項目 1 には引き続き “Disconnect from Wi-Fi Direct” しかありませんが、選択すると “There was an error disconnecting from Wi-Fi Direct” と表示されます。Driver Hub は Control Hub とペアになっており、Wi-Fi Direct ではないためです。
- DS の Pairing Method が Wi-Fi Direct（RC スマホと接続する前提）に設定されていると、項目 10 の Yes は **不合格** になります。
- 項目 11 には Driver Hub が接続している Standard Wi-Fi の **ネットワーク名（AP）** が表示されます。チェックマークは、その AP が FTC 合法デバイス（Control Hub）であり、名前が正しい形式であることを示します。DS 名と RC 名（チーム番号）が一致しているかは確認しません。この例では Driver Hub は 1234-A-DS、Control Hub は 9999-A-RC であり、FTC チームまたは Robot Inspector が指摘すべき**違反の組み合わせ** です。

.. figure:: images/tDS-4a.png
   :align: center
   :width: 85%
   :alt: DS 4a

   DS Self Inspect 4（Driver Hub + Control Hub）

この Self Inspect 画面は Driver Hub を Control Hub とペアリングした後、Wi-Fi インターネットルーターに接続した際に表示されました。

- 項目 11 がエラーを示しています。Driver Hub が Standard Wi-Fi で接続できる AP は同時に 1 つだけで、このネットワークは FTC の RC デバイスではありません。

.. _rc-self-inspect-1-appearing-on-rc-phone-paired-with-ds-phone:

RC Self Inspect 1（RC スマホ + DS スマホ）
------------------------------------------

ここからは **Robot Controller** の Self Inspect 画面です。RC 画面は DS デバイス** または** RC スマホから表示できますが、細かな違いがあります。

.. figure:: images/tRC-1.png
   :align: center
   :width: 85%
   :alt: RC 1

   RC Self Inspect 1（RC スマホ + DS スマホ）

- 項目 5 には Expansion Hub のアドレスとファームウェアバージョンが一覧表示されます。この例では 1 台ですが、2 台まで表示されます。チェックマークは RC アプリの現行バージョンに対して全ファームウェアが最新であることを示します。Hub が接続されていない場合は “N/A” と表示されます。
- 項目 10 の ``RC Password`` は RC Self Inspect のみに表示され、DS Self Inspect にはありません。Control Hub のパスワードを工場出荷時の “password” から変更するという FTC 要件をチェックします。Control Hub 向けの項目ですが、デフォルトパスワードを持たない RC スマホにも表示され、常にチェックマークになります。
- 項目 14 は、デバイスのシステム日付に基づき、RC アプリが **当該 FTC シーズンの最小バージョン** を満たしているかを確認します。DS アプリとのバージョン一致は確認しません。ここが赤い「incorrect」の場合は**Android の設定** で日付を修正してください。
- 項目 15 は RC デバイスに DS アプリが **インストールされていない** ことを確認します。

.. _rc-self-inspect-2-appearing-on-ds-phone-paired-to-rc-phone:

RC Self Inspect 2（DS スマホ上、RC スマホとペア）
---------------------------------------------------

.. figure:: images/tRC-2.png
   :align: center
   :width: 85%
   :alt: RC 2

   RC Self Inspect 2（DS スマホ上、RC スマホとペア）

この RC Self Inspect は、ペアリングしている DS スマホ上に表示されたもので、直前の RC スマホ上の画面と「同じ」ですが、2 点だけ異なります。

- ヘッダーの三点メニューがありません。このメニューは Wi-Fi Direct を切断する 1 つの選択肢を提供しますが、同じ Wi-Fi Direct 接続を使っている DS スマホから RC 側の操作として切断することはできません。
- 項目 14 は RC スマホ上の画面にはありませんでした。ここでは DS アプリと RC アプリのバージョンが一致していることを確認しており、この例では両方とも 7.0 です。7.0 と 7.0.1 のような「Point mismatch」は FTC の最新ルール（2021-2022 シーズンの Q&A #176）で許容されています。

.. _rc-self-inspect-3-appearing-on-rc-phone-paired-with-driver-hub:

RC Self Inspect 3（RC スマホ + Driver Hub）
-------------------------------------------

.. figure:: images/tRC-3a.png
   :align: center
   :width: 85%
   :alt: RC 3a

   RC Self Inspect 3（RC スマホ + Driver Hub）

この画面は RC Self Inspect 1（DS デバイスが DS スマホ）の場合と同じです。そちらの説明を参照してください。

.. figure:: images/tRC-3b.png
   :align: center
   :width: 85%
   :alt: RC 3b

   RC Self Inspect 3（RC スマホ + Driver Hub）

こちらも同じ画面ですが、RC スマホが Driver Hub とペアになったままインターネットルーターに接続した例です。Standard Wi-Fi 接続により RC スマホは一時的にペアリングを失いましたが、復旧できました。

- 項目 12 が不合格を示しています。Standard Wi-Fi には接続していますが、接続先が FTC の DS デバイス **ではありません** 。

.. _rc-self-inspect-4-appearing-on-driver-hub-paired-to-rc-phone:

RC Self Inspect 4（Driver Hub 上、RC スマホとペア）
---------------------------------------------------

.. figure:: images/tRC-4.png
   :align: center
   :width: 85%
   :alt: RC 4

   RC Self Inspect 4（Driver Hub 上、RC スマホとペア）

Driver Hub 上に表示されたこの画面は直前のものと「同じ」ですが、2 点異なります。

- ヘッダーの三点メニューがありません。このメニューは Wi-Fi Direct を切断する 1 つの選択肢を提供しますが、同じ Wi-Fi Direct 接続を使っている Driver Hub から RC 側の操作として切断することはできません。
- 項目 14 は RC スマホ上の画面にはありませんでした。ここでは DS アプリと RC アプリのバージョン一致を確認しており、この例では DS アプリ 7.0.1、RC アプリ 7.0 で不一致として表示されています。こうした「Point mismatch」は FTC の最新ルール（2021-2022 シーズンの Q&A #176）で許容されています。

.. _rc-self-inspect-5-appearing-on-ds-phone-paired-to-control-hub:

RC Self Inspect 5（DS スマホ上、Control Hub とペア）
-----------------------------------------------------

ここから **Control Hub** の例です。Self Inspect 画面にいくつか違いがあります。この例ではロボットに**2 台** の Hub が構成されています。

.. figure:: images/tRC-5b.png
   :align: center
   :width: 85%
   :alt: RC 5b

   RC Self Inspect 5（DS スマホ上、Control Hub とペア）

- ヘッダーの三点メニューが再びありません。このメニューは Wi-Fi Direct を切断する 1 つの選択肢を提供しますが、Control Hub は Wi-Fi Direct ではなく Standard Wi-Fi でホストします。いずれにせよ、同じ接続を使っている DS スマホから RC 側の操作として切断することはできません。
- 項目 3 は Control Hub の RC Self Inspect にのみ表示されます。Operating System が RC アプリの現行バージョンに対して最新であることを確認します。
- Control Hub の Android バージョン（項目 4）が **Android 8 未満** のため、``Location services`` は表示されません。
- 項目 5 は Control Hub に内蔵された Expansion Hub のファームウェアバージョンを示し、RC アプリの現行バージョンに対して最新であることを確認します。
- 項目 6 は単体接続されている Expansion Hub のファームウェアバージョンとアドレスを示し、こちらも最新です。
- 項目 7 は常に高いバッテリー残量を示すべきで、ロボットバッテリーの公称 12V が供給されていることを意味します。
- Control Hub では RC 側の検査から ``Airplane Mode`` が省かれています。FTC ルールでは Driver Hub と Control Hub は Airplane Mode 要件の対象外です。
- 項目 9 は Control Hub でも適用され、工場出荷時のパスワード “password” から変更されていることを確認します。
- Control Hub は Standard/インフラ Wi-Fi のみを使用するため、項目 10 と 11 は Yes/Yes である必要があります。項目 11 は Control Hub が何に接続しているかは示さず（この画面を表示している DS スマホである必要があります）。
- 項目 12 は Control Hub がブロードキャストしている Standard Wi-Fi の **ネットワーク名（AP）** を示します。チェックマークはその AP が FTC の命名規則を満たしていることを示します。DS 名と RC 名（チーム番号）が一致しているかは確認しません。この例では DS スマホが 2468-A-DS、Control Hub が 9999-A-RC であり、FTC チームまたは Robot Inspector が指摘すべき**違反の組み合わせ** です。
- 項目 14 は DS デバイス上の RC Self Inspect にのみ表示されます。ここでは DS アプリと RC アプリのバージョン一致を確認しており、この例では両方とも 7.0 です。7.0 と 7.0.1 のような「Point mismatch」は FTC の最新ルール（2021-2022 シーズンの Q&A #176）で許容されています。
- 項目 15 は RC デバイスに DS アプリが **インストールされていない** ことを確認します。画面のない Control Hub に DS アプリが入っているのは大きなミスです。

.. _rc-self-inspect-6-appearing-on-driver-hub-paired-to-control-hub:

RC Self Inspect 6（Driver Hub 上、Control Hub とペア）
------------------------------------------------------

Control Hub の場合、Driver Hub に表示される Self Inspect のカテゴリは直前の DS スマホの場合と同じです。

.. figure:: images/tRC-6b.png
   :align: center
   :width: 85%
   :alt: RC 6b

   RC Self Inspect 6（Driver Hub 上、Control Hub とペア）

ここで唯一異なる報告は、Driver Hub の DS アプリ 7.0.1 と Control Hub の 7.0 との「不一致」です。Driver Hub は自動更新されることが多く、古い Android 6 向けの DS バージョンが入る場合があります。こうした「Point mismatch」は FTC の最新ルール（2021-2022 シーズンの Q&A #176）で許容されています。

.. figure:: images/tRC-6a.png
   :align: center
   :width: 85%
   :alt: RC 6a

   RC Self Inspect 6（過去に Control Hub とペアだった Driver Hub）

最後に、アクティブな接続がない場合、DS デバイスは RC デバイスの状態を何も表示できません。

まとめ
------

Self Inspect 画面は、制御システムの要素が最新かつ正しく設定されていることをチームが確認するための、手早く便利なリファレンスです。

Self Inspect は FTC 大会の Robot Inspection で確認されることがありますが、FTC ルールへの準拠を網羅的または公式に保証するものでは **ありません** 。

各検査画面は Restart Robot の有無にかかわらず自動更新されるため、問題が解消されたことを素早く確認できます。

=============

ご質問・ご意見・修正提案は westsiderobotics@verizon.net までお寄せください。
