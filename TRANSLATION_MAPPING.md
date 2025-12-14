# Translation Mapping Reference

This file contains extracted Japanese translations from RST files.
Use this as a reference when filling in .po files.


## apriltag/apriltag_tips/decode_apriltag/decode-apriltag.rst

### Block 1 (line 1)

```
RTX提供のDECODEにおけるAprilTagの課題
```

### Block 2 (line 4)

```
AprilTagとは？
```

### Block 3 (line 7)

```
`ミシガン大学 <https://april.eecs.umich.edu/software/apriltag>`_ で開発された **AprilTag** は、2Dバーコードや簡略化されたQRコードに似ています。数値の **ID コード** を含み、** 位置と向き** に使用できます。
```

### Block 4 (line 9)

```
RTX提供のDECODEシーズンの **FIRST** Tech Challenge では、**AprilTag** は3つの異なる方法で使用されます：
```

### Block 5 (line 11)

```
1. **OBELISK** 上では、**AprilTag** は各 **MATCH** でランダム化される3つの **MOTIF** の1つを識別するために使用されます。
2. **GOAL** 上では、**AprilTag** をターゲットに使用して、チームが **ARTIFACT** を正しい **GOAL** に正確に発射できます。
3. **GOAL** 上では、**AprilTag** はビジュアルオドメトリシステムとして使用でき、**AprilTag** が提供する情報を使用して **FIELD** 上の **ROBOT** の位置を計算します（ローカライゼーションと呼ばれるプロセス）。詳細については、:doc:`AprilTag ローカライゼーション <../../vision_portal/apriltag_localization/apriltag-localization>` ページを参照してください。
```

### Block 6 (line 18)

```
   :alt: DECODEフィールドとAprilTag位置を示す画像
```

### Block 7 (line 20)

```
   DECODEフィールド上のAprilTag IDと位置
```

### Block 8 (line 22)

```
困難な環境照明でのAprilTag
```

### Block 9 (line 25)

```
今シーズン、チームが直面する課題の1つは、カメラが **AprilTag** を正しく認識できるようにすることです。**AprilTag** は、**AprilTag** の白と黒の部分がコントラストの高い色であるという事実に依存しています - 環境の照明が十分なコントラストを許さない場合、**AprilTag** アルゴリズムは **AprilTag** を適切に検出できない可能性があります。幸いなことに、事実上すべてのウェブカメラで環境の問題を修正するのに役立つことができます。
```

### Block 10 (line 27)

```
優れた例の状況が倉庫で発生しました。**DECODE** フィールドが倉庫に設置され、``ConceptAprilTagEasy`` サンプルでデフォルト設定を使用していました。カメラストリームプレビューを表示すると、**OBELISK** 上の **AprilTag** は、晴れた日に **OBELISK** に直接当たる日光によって完全に白飛びし、**AprilTag** が見えませんでした。わずかに異なる角度の別のカメラが同じシーンの別の写真を撮りました。**AprilTag** は見えますが、**AprilTag** から反射する直接光が明らかに多すぎるため、認識できませんでした。このシナリオは、イベントが開催される可能性のある体育館に非常に似ており、晴れた日には光がカメラの **AprilTag** を表示する能力を妨げる可能性があります。何ができるでしょうか？
```

### Block 11 (line 38)

```
         画像 #1 - 例
```

### Block 12 (line 45)

```
            :alt: OBELISKのAprilTagが見えないDECODEフィールドの画像
```

### Block 13 (line 49)

```
         OBELISK上の白飛びしたAprilTag
```

### Block 14 (line 55)

```
         画像 #2 - 別の視点
```

### Block 15 (line 62)

```
            :alt: 別の視点からのDECODEフィールドの画像
```

### Block 16 (line 66)

```
         OBELISKの別の視点
```

### Block 17 (line 72)

```
         画像 #3 - 別の視点
```

### Block 18 (line 79)

```
            :alt: 倉庫の窓から入ってくる光を示す画像
```

### Block 19 (line 83)

```
         倉庫に入る日光
```

### Block 20 (line 94)

```
この環境照明に対抗する最良の方法は、**SDK** 内のウェブカメラ設定を使用して、ゲインと露出設定の両方を同時に調整することです。露出を最小化し（各画像フレームで光がセンサーに当たる時間を短縮）、ゲインを最大化する（センサーからの信号を増幅）ことで、結果の画像は通常の画像よりも暗くなりますが、**AprilTag** のような高コントラストの要素が強調され、認識できるようになります。これは ``ConceptAprilTagOptimizeExposure`` サンプルを使用して実験できます。
```

### Block 21 (line 96)

```
確かに、ウェブカメラの露出を最小化し、ゲインを最大化することで、ウェブカメラからの結果の画像を使用して、問題のある **AprilTag** を認識できました。さらに多くの例として、``RobotAutoDriveToAprilTag...`` サンプル **OpMode** もこの手法を使用して、カメラの露出とゲイン設定を調整し、ほとんどの条件下で **AprilTag** が読み取れるようにしています。
```

### Block 22 (line 99)

```
   大きな利点の1つは、この手法（露出を最小化しながらゲインを最大化）は、移動中の **AprilTag** を読み取る際のモーションブラーを減らすのにも非常に人気があることです - したがって、これには複数の利点があります！
```

### Block 23 (line 101)

```
露出とゲインが適切に設定された後の画像の例を次に示します。1つの画像は **AprilTag** 処理が有効になっており、**AprilTag** が適切に検出されていることを示しています。もう1つは処理が無効になっているため、ウェブカメラから返される生画像を見ることができます。
```

### Block 24 (line 112)

```
         画像 #4 - 処理済み画像
```

### Block 25 (line 119)

```
            :alt: OBELISKのAprilTagが処理されているDECODEフィールドの画像
```

### Block 26 (line 123)

```
         検出を示す処理済み画像
```

### Block 27 (line 129)

```
         画像 #5 - 生の処理済み画像
```

### Block 28 (line 136)

```
            :alt: 生の処理済みDECODEフィールドの画像
```

### Block 29 (line 140)

```
         AprilTag処理なしの画像
```

### Block 30 (line 150)

```
OBELISK上の複数のAprilTagの読み取り
```

### Block 31 (line 153)

```
**OBELISK** は正三角柱（実際のオベリスクには4つの面があることは知っています）で、**FIELD** の **GOAL** 側に、**FIELD** 境界の外側に長方形の面の1つが中央に配置されています。**ROBOT** が **ALLIANCE** の **GOAL** に接触してフィールドに配置されると、**ROBOT** のカメラが複数の **AprilTag** を認識して処理する可能性が非常に高くなります。
```

### Block 32 (line 156)

```
   両方の **AprilTag** を読み取り、それら2つのタグを使用して実際にどの **AprilTag** が見えているかを判断（および検証）することは論理的に見えるかもしれません。ただし、**OBELISK** 上の **AprilTag** には定義された順序がないため、これは信頼できません。
```

### Block 33 (line 162)

```
   :alt: 複数のAprilTagが見えるOBELISKを示す画像
```

### Block 34 (line 164)

```
   BLUE GOALからのOBELISK上のAprilTagの表示
```

### Block 35 (line 166)

```
**FIELD** に実際に表示されている **AprilTag** を判断する信頼できる方法は、**OBELISK** の正面の **AprilTag** のみが表示できる位置に **ROBOT** を移動することです。
```

### Block 36 (line 168)

```
今シーズンの幸運を祈ります！
```


## apriltag/opmode_test_images/opmode-test-images.rst

### Block 1 (line 1)

```
*FIRST* Tech Challenge AprilTag テストサンプル
```

### Block 2 (line 4)

```
はじめに
```

### Block 3 (line 7)

```
2023-2024 シーズンでは、`FIRST Tech Challenge が AprilTags を導入しました
<https://ftc-docs.firstinspires.org/en/latest/apriltag/vision_portal/apriltag_intro/apriltag-intro.html>`__。これはシーズン固有の競技に使用されます。AprilTags は、ミシガン大学の April Robotics Laboratory によって開発され、QR コードと同様の概念に基づいて構築された視覚的フィデューシャルタギングシステムで、拡張現実、ロボティクス、カメラキャリブレーションを含む幅広いタスクに有用です。適切にキャリブレーションされたカメラとタグライブラリを使用して、AprilTags を検出し、カメラに対するタグの範囲と方向情報（**ポーズ** データとも呼ばれる）などの情報を提供できます。*FIRST* Tech Challenge Software Development Kit (SDK) は、チームがこのリソースを利用できるように AprilTag 検出 API を追加するために更新されました。
```

### Block 4 (line 10)

```
このドキュメントには、SDK 内の *FIRST* Tech Challenge AprilTag サンプルで使用することを目的とした AprilTags の例が含まれています。2023-2024 シーズンで使用されるすべての AprilTags は、36h11 タグファミリーから来ています。これは、事前に決定されたタグのセットです。主要なタグ領域は、黒と白の *ピクセル* の 8x8 正方形マトリックスで構成されています。タグのサイズは、タグの全体の黒い正方形部分の物理的寸法に基づいて測定されます – 4 インチの AprilTag には、各辺が 4 インチを測定する黒い正方形部分があります。AprilTag のサイズを測定する際には使用されませんが、各タグには、主要なタグ領域を囲む 1 *ピクセル* 厚の白い境界線も必要です（合計タグサイズは 10x10 *ピクセル* になります）。追加された白い境界線により、たとえば、4 インチの AprilTag には各辺 5 インチのフットプリントが必要です。
```

### Block 5 (line 19)

```
*FIRST* Tech Challenge の AprilTag API は複数のタグサイズを処理できます；各個別のタグは独立してサイズを設定できますが、個別のタグに複数のサイズを設定することはできません。各タグに対して計算される一部のポーズ情報（カメラからタグまでの距離データなど）には、使用されるタグの正確なサイズを知る必要があります。SDK 内のサンプルプログラムで使用されるデフォルトのタグサイズは次のとおりです：
```

### Block 6 (line 22)

```
| **タグの説明**                       | **タグのサイズ（インチ）**           |
|                                      | **（ミリメートル）**                 |
```

### Block 7 (line 25)

```
| タグ ID: 583（別名「Nemo」）         | 4 in (101.6 mm)                      |
```

### Block 8 (line 27)

```
| タグ ID: 584（別名「Jonah」）        | 4 in (101.6 mm)                      |
```

### Block 9 (line 29)

```
| タグ ID: 585（別名「Cousteau」）     | 6 in (152.4 mm)                      |
```

### Block 10 (line 31)

```
| タグ ID: 586（別名「Ariel」）        | 6 in (152.4 mm)                      |
```

### Block 11 (line 34)

```
この :download:`ドキュメントの PDF バージョン
<files/FTCAprilTagSDK82SamplesExtended.pdf>` またはその一部を印刷する際は、
ページサイズの設定を「実際のサイズ」に設定して、タグが正しく印刷されるようにしてください。
すべてのプリンターは少しずつ異なるため、主要なタグ領域の黒い正方形部分の幅と高さを測定して、
ページが正しく印刷されたことを確認することもお勧めします。
```

### Block 12 (line 48)

```
AprilTag 検出値に関するより詳細な情報と、それらが何を意味するかをよりよく理解するには、次のウェブサイトにアクセスしてください：
```

### Block 13 (line 50)

```
:ref:`AprilTag 検出値の理解 <apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values:understanding apriltag detection values>`
- :download:`公式 PDF をダウンロードして印刷 <files/FTCAprilTagSDK82SamplesExtended.pdf>`
```

### Block 14 (line 57)

```
認識のためにこれらのタグにカメラを向けることができます - ftc-docs は画像の引き伸ばしを許可しているため、表示領域の幅が画像の幅よりも小さい場合、画像が明確かつ正確に表現されない可能性があります。
:download:`公式 PDF をダウンロードして印刷する <files/FTCAprilTagSDK82SamplesExtended.pdf>` ことをお勧めします。
```

### Block 15 (line 66)

```
   タグ 583、「Nemo」
```

### Block 16 (line 76)

```
   タグ 584、「Jonah」
```

### Block 17 (line 86)

```
   タグ 585、「Cousteau」
```

### Block 18 (line 96)

```
   タグ 586、「Ariel」
```


## apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values.rst

### Block 1 (line 1)

```
AprilTag 検出値の理解
```

### Block 2 (line 4)

```
*最終更新: 2023年7月5日*
```

### Block 3 (line 6)

```
はじめに
```

### Block 4 (line 9)

```
新しい **SDK** ビジョン処理システムによって**AprilTag** が検出されると、コアコードは容易に解釈できないことが多い生データのコレクションを返します。しかし、データはさらに馴染みのあるフレームワークに変換して、より簡単に利用できるようになります。**FIRST**Tech Challenge**SDK** では、**AprilTag API** はチームの**OpMode** に、3D空間でのタグの位置を表す変換値と回転値のコレクション（**ftcPose** と呼ばれる）を提示します。
```

### Block 5 (line 11)

```
これらの値を解釈する方法を理解するには、垂直成分を無視したより単純な2Dシナリオを考える方が簡単です。これを以下に説明します。
```

### Block 6 (line 13)

```
以下の** 図1** は、考えられる2Dシナリオの1つを表しています。
```

### Block 7 (line 17)

```
   :alt: 図1
```

### Block 8 (line 20)

```
   図1: AprilTag シナリオの上面図
```

### Block 9 (line 22)

```
この図は、カメラと**AprilTag** を上から見たものです。カメラの「前方」方向は、カメラから真っすぐ引かれた破線で識別されます。**AprilTag** 画像は図の左上に示されています。タグは、カメラから前方に100ユニット、左に36.4ユニット（前方視線に対して直角に測定）の位置にあります。**AprilTag** は、通常の「正面」向きから反時計回りに5度回転しています。
```

### Block 10 (line 24)

```
1つの考えられる検出シナリオを明確に理解したので、**SDK** によって**ftcPose** として返されるさまざまな値の意味を見ることができます。** 図2** は、図1に示されているカメラ/ターゲットシナリオに関連する測定値を示しています。
```

### Block 11 (line 28)

```
   :alt: 図2
```

### Block 12 (line 31)

```
   図2: ftcPose 値の測定
```

### Block 13 (line 33)

```
検出値
------**X 座標**: これは、カメラの前方視線に対して直角に測定された、タグの横方向の位置です。正の値は左、負の値は右を示します。**Y 座標**: これは、カメラの前方視線に沿って測定された、タグの前方距離です。正の値は前方、負の値は後方を示します。**Z 座標**: これは、カメラの中心線に対して直角に測定された、タグの垂直位置です。正の値は上、負の値は下を示します。この値は2Dシナリオでは無視されます。** 範囲**: これは、カメラの中心からタグの中心までの直線距離です。** 方位**: これは、カメラの前方視線からタグの中心までの角度です。正の値は左、負の値は右を示します。** 仰角**: これは、カメラの水平線からタグの中心までの角度です。正の値は上、負の値は下を示します。この値は2Dシナリオでは無視されます。** ヨー**: これは、タグの中心を通る垂直軸を中心としたタグの回転です。正の値は反時計回り、負の値は時計回りの回転を示します。** ピッチ**: これは、タグの中心を通る水平軸を中心としたタグの回転です。正の値は上方への傾き、負の値は下方への傾きを示します。この値は2Dシナリオでは無視されます。** ロール**: これは、カメラからタグへの視線を中心としたタグの回転です。正の値は反時計回り、負の値は時計回りの回転を示します。この値は2Dシナリオでは無視されます。
```

### Block 14 (line 36)

```
例
```

### Block 15 (line 39)

```
図1と図2のシナリオでは、次の値が**ftcPose** に返されます：
```

### Block 16 (line 43)

```
   x = 36.4 (左に36.4ユニット)
   y = 100.0 (前方に100ユニット)
   z = 0.0 (2Dシナリオでは無視)
   range = 106.4 (カメラから106.4ユニット)
   bearing = 20.0 (左に20度)
   elevation = 0.0 (2Dシナリオでは無視)
   yaw = 5.0 (反時計回りに5度)
   pitch = 0.0 (2Dシナリオでは無視)
   roll = 0.0 (2Dシナリオでは無視)
```

### Block 17 (line 53)

```
別の例を見てみましょう。** 図3** は、カメラとタグの異なる配置を示しています。
```

### Block 18 (line 57)

```
   :alt: 図3
```

### Block 19 (line 60)

```
   図3: 別のシナリオ
```

### Block 20 (line 62)

```
この例では、タグはカメラから右に移動し、時計回りに回転しています。**ftcPose** の値は次のようになります：
```

### Block 21 (line 66)

```
   x = -50.0 (右に50ユニット)
   y = 86.6 (前方に86.6ユニット)
   z = 0.0 (2Dシナリオでは無視)
   range = 100.0 (カメラから100ユニット)
   bearing = -30.0 (右に30度)
   elevation = 0.0 (2Dシナリオでは無視)
   yaw = -15.0 (時計回りに15度)
   pitch = 0.0 (2Dシナリオでは無視)
   roll = 0.0 (2Dシナリオでは無視)
```

### Block 22 (line 76)

```
3Dシナリオ
```

### Block 23 (line 79)

```
実際の競技では、カメラとタグは3D空間に配置されます。このシナリオでは、**Z 座標** 、** 仰角** 、** ピッチ** 、** ロール** の値が意味を持ちます。** 図4** は、カメラとタグの3D配置を示しています。
```

### Block 24 (line 83)

```
   :alt: 図4
```

### Block 25 (line 86)

```
   図4: 3Dシナリオ
```

### Block 26 (line 88)

```
この例では、タグはカメラの上方に配置され、下方に傾いています。**ftcPose** の値は次のようになります：
```

### Block 27 (line 92)

```
   x = 0.0 (横方向のオフセットなし)
   y = 100.0 (前方に100ユニット)
   z = 50.0 (上に50ユニット)
   range = 111.8 (カメラから111.8ユニット)
   bearing = 0.0 (左右のオフセットなし)
   elevation = 26.6 (上に26.6度)
   yaw = 0.0 (回転なし)
   pitch = -20.0 (下方に20度傾斜)
   roll = 0.0 (ロール回転なし)
```

### Block 28 (line 102)

```
まとめ
------**ftcPose** によって提供される値は、カメラに対する**AprilTag** の位置と向きを完全に記述します。これらの値を理解することで、ロボットのナビゲーションと位置決めに効果的に使用できます。
```

### Block 29 (line 105)

```
主なポイント：
```

### Block 30 (line 107)

```
-**X、Y、Z 座標** は、カメラに対するタグの位置を示します
-** 範囲** と** 方位** は、極座標系での位置を提供します
-** ヨー、ピッチ、ロール** は、タグの3D回転を記述します
- 2Dシナリオでは、**Z** 、** 仰角** 、** ピッチ** 、** ロール** は通常ゼロまたは無視されます
```

### Block 31 (line 112)

```
これらの値を適切に解釈することで、**OpMode** は**AprilTag** 検出を使用してロボットを正確に制御できます。
```


## apriltag/vision_portal/apriltag_intro/apriltag-intro.rst

### Block 1 (line 1)

```
AprilTag 入門
```

### Block 2 (line 4)

```
はじめに
```

### Block 3 (line 7)

```
カメラベースの技術として人気があるのが **AprilTag** です。これは QR コードに似たスキャン画像です。カスタム Signal Sleeves での効果的な動作と迅速なセットアップにより、POWERPLAY（2022-2023）シーズンでは、特に Java でプログラミングを行う *FIRST* Tech Challenge チームに **広く採用** されました。
```

### Block 4 (line 16)

```
FTC Blocks を使用するチームを含む POWERPLAY のチームは、いくつかのリソースの使い方を学びました：
```

### Block 5 (line 18)

```
-  AprilTag: フォーマットされた画像を評価するためのオープンソース技術
-  EasyOpenCV: *FIRST* Tech Challenge に最適化された OpenCV（画像処理ライブラリ）とのインターフェース
-  myBlocks: OnBot Java (OBJ) で作成されたカスタム Blocks
```

### Block 6 (line 22)

```
現在、これら3つの領域は *FIRST* **Tech Challenge Software Development Kit (SDK) のバージョン 8.2 以降** に提供、またはバンドルされています。
```

### Block 7 (line 24)

```
つまり、**AprilTag** と**EasyOpenCV** の主要な機能は、特別なダウンロードなしで Robot Controller (RC) と Driver Station (DS) アプリで利用できます。また、AprilTag の機能は、カスタム myBlocks を必要とせずに**FTC Blocks** に含まれています。
```

### Block 8 (line 26)

```
AprilTag の機能は、ウェブカメラと Android RC フォンカメラの両方で動作します。
単一の OpMode で AprilTag と Color Processing を使用できます。
```

### Block 9 (line 29)

```
*FIRST* Tech Challenge において、AprilTag はスポットライトを浴びる準備が整いました！
```

### Block 10 (line 31)

```
AprilTag とは？
```

### Block 11 (line 34)

```
`ミシガン大学 <https://april.eecs.umich.edu/software/apriltag>`__ で開発された AprilTag は、2D バーコードまたは簡略化された QR コードのようなものです。数値の **ID コード** を含み、** 位置と方向** の特定に使用できます。
```

### Block 12 (line 41)

```
   ロボットにおける AprilTags。Photo Credit: University of Michigan
```

### Block 13 (line 43)

```
AprilTag は **視覚的フィデューシャル（visual fiducial）** またはフィデューシャルマーカーの一種で、情報を含み、簡単に認識できるように設計されています。
```

### Block 14 (line 50)

```
   異なる AprilTag ファミリーのサンプル
```

### Block 15 (line 52)

```
上記のサンプルは、異なるフォーマット、つまり **ファミリー** を表しています。プロジェクトでは通常、単一の AprilTag ファミリーを使用します。
```

### Block 16 (line 54)

```
*FIRST* Tech Challenge では、**36h11** と呼ばれる一般的なファミリーを使用します。36h11 ファミリーの 0 から 20 までの番号を示す PDF は、ここからダウンロードできます：
```

### Block 17 (line 58)

```
各番号は、そのタグの ID コードです。
```

### Block 18 (line 60)

```
以下は **ID コード 2** を表す AprilTag です。SDK ソフトウェアは、ID コードを認識し、画像にオーバーレイ表示します（小さな青い矩形**ID 02** ）。
```

### Block 19 (line 67)

```
   検出されたタグ ID 02 を表示するストリーム出力
```

### Block 20 (line 69)

```
上記の画像は、Robot Controller デバイス（Control Hub または RC フォン）からのカメラプレビュー画像（LiveView と呼ばれる）を示しています。
```

### Block 21 (line 71)

```
AprilTag ファミリー 36h11 には、587 個の ID コードの容量があります。すべてを見るには、次のリンクをたどってください：
```

### Block 22 (line 75)

```
正方形の AprilTag パターンには、より小さな黒と白の正方形が含まれており、それぞれが **ピクセル** と呼ばれます。36h11 タグには、10 x 10 ピクセルが含まれており、**すべて白いピクセル** の外側の境界線と、**すべて黒いピクセル** の内側の境界線が含まれます。
```

### Block 23 (line 77)

```
**タグサイズ** は、36h11 の黒いピクセルで構成される**内側の境界線** の外側のエッジを横切って測定されます。
```

### Block 24 (line 84)

```
   タグサイズの測定を示す図
```

### Block 25 (line 86)

```
上記の画像は、外側の白い境界線を持つ完全な AprilTag を示しています。36h11 ファミリーから、その ID コードは 42 です。
```

### Block 26 (line 88)

```
AprilTag ポーズ
```

### Block 27 (line 91)

```
ID コードを超えて、新しい SDK は **ポーズ** データ、すなわち**カメラの視点** からの位置と方向（回転）も提供します。これには**平らな AprilTag** が必要であり、湾曲した POWERPLAY Signal Sleeves では不可能でした。
```

### Block 28 (line 93)

```
Robot Controller デバイス（Control Hub または RC フォン）からのカメラプレビュー画像（LiveView と呼ばれる）をもう一度見てみましょう。
```

### Block 29 (line 100)

```
   説明のための追加マーキングを含む LiveView 画像
```

### Block 30 (line 102)

```
カメラレンズの中心からまっすぐ外側を指すレーザービームを想像してください。その 3 次元パスは（カメラから見て）**緑色の星** で示される単一の点として表示されます。AprilTag の中心（**黄色の星** ）がその「レーザービーム」からオフセットされていることがわかります。
```

### Block 31 (line 104)

```
その **並進オフセット** は、互いに 90 度の角度にある軸に沿った 3 つの伝統的なコンポーネント（X、Y、Z 距離）に分解できます：
```

### Block 32 (line 106)

```
-  X 距離（水平のオレンジ色の線）は中心から右方向です
-  Y 距離（表示されていません）はレンズの中心から外側です
-  Z 距離（垂直のオレンジ色の線）は中心から上方向です
```

### Block 33 (line 110)

```
SDK は、これらの距離を画面上のピクセル数を報告するだけでなく、**実世界で** 提供します。非常に便利です！
```

### Block 34 (line 112)

```
また、AprilTag の平らな面がカメラの平面と平行でないこともわかります。その **回転オフセット** は、X、Y、Z 軸を中心とした 3 つの角度に分解できます。これについては、以下の**AprilTag 軸** と呼ばれるセクションでさらに説明します。
```

### Block 35 (line 114)

```
要約すると、SDK は AprilTag 画像を評価し、**「ポーズ推定」** を実行し、タグとカメラ間の推定 X、Y、Z**距離** と、これらの軸を中心とした推定回転**角度** を提供します。より近いまたはより大きな AprilTag は、より正確なポーズ推定をもたらすことができます。
```

### Block 36 (line 116)

```
良好なポーズ推定を提供するために、各 RC フォンカメラまたはウェブカメラには、特定の解像度に対する **キャリブレーションデータ** が必要です。SDK には、限られた数のウェブカメラと解像度のためのそのようなデータが含まれています。チームは、提供された手順を使用して、**レンズ固有パラメーター** と呼ばれる独自のデータを生成できます。
```

### Block 37 (line 118)

```
ナビゲーション
```

### Block 38 (line 121)

```
OpMode はナビゲーションを実現するために AprilTag ポーズを使用します：入力を評価し、目的地まで走行します。
```

### Block 39 (line 123)

```
OpMode はポーズデータを使用して、タグに向かって走行するか、タグに **対する** ターゲット位置と方向まで走行できます。（新しい SDK は Java**サンプル OpMode** ``RobotAutoDriveToAprilTagOmni.java`` と``RobotAutoDriveToAprilTagTank.java`` を提供します。）もう1つのナビゲーションの可能性については、以下の**高度な使用法** で言及されています。
```

### Block 40 (line 125)

```
ナビゲーションは、AprilTag がカメラの視野内に留まる場合、**継続的な** ポーズ推定で最も効果的です。つまり、OpMode の**「while() ループ」** は、ロボットの走行アクションをガイドするために、更新されたポーズデータを定期的に読み取る必要があります。
```

### Block 41 (line 127)

```
SDK は **複数のカメラ** をサポートしており、切り替え可能または同時使用が可能です。これは、ロボットが方向を変更する場合、または別の AprilTag（または Color Processing）を使用してナビゲートしたい場合に役立ちます。
```

### Block 42 (line 129)

```
ナビゲーションには、駆動モーターエンコーダー、REV Hub IMU、デッドホイールエンコーダー、カラー/距離センサー、超音波センサーなど、他のセンサーも使用できます。
```

### Block 43 (line 131)

```
同じカメラおよび/または2番目のカメラから **非 AprilTag 画像** を評価することも可能です。たとえば、SDK は、*FIRST* Tech Challenge で採用されているもう1つのビジョン技術である **Color Processing** で検出されたオブジェクトの水平角度（またはベアリング）を推定できます。高度なチームは、AprilTag または他のオブジェクトを視野内に保つために、アクティブカメラポインティング制御を検討するかもしれません。
```

### Block 44 (line 133)

```
アノテーション
```

### Block 45 (line 136)

```
プレビュー（RC フォン画面または DS Camera Stream）では、公式に認識された AprilTag は **色付きの境界線** とその数値**ID コード** を表示します。これらの** アノテーション** により、認識を視覚的に簡単に確認できます：
```

### Block 46 (line 143)

```
   異なるメタデータを持つ2つの AprilTags が検出され、アノテーションが表示されている
```

### Block 47 (line 145)

```
上記の :ref:`DS Camera Stream <hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam:image preview>` プレビューでは、左側の AprilTag はタグ **ライブラリ** （デフォルトまたはカスタマイズ）から認識されました。ライブラリタグには、タグサイズを含む事前にロードされた情報（**メタデータ** と呼ばれる）があり、**ポーズ推定** を可能にします。これらはデフォルトで**色付きの境界線** でアノテーションされます。
```

### Block 48 (line 147)

```
右側の AprilTag はタグライブラリにありませんでした。メタデータがないため、SDK は数値 **ID コード** のみを提供でき、ここでは**ID 03** として表示されています。このようなタグは、デフォルトでは色付きの境界線で** アノテーションされません** 。
```

### Block 49 (line 149)

```
注：**Camera Stream** は、Driver Station デバイスにカメラのビューのスナップショットを表示します。OpMode の INIT フェーズ中にのみ利用可能で、AprilTag（または Color Processing）アノテーションも表示されます。手順はここに掲載されています：
```

### Block 50 (line 153)

```
オプションのアノテーションには、タグ中心の **色付き軸** と、タグ画像から投影される**色付きボックス** が含まれます：
```

### Block 51 (line 160)

```
   追加のアノテーションが有効になっている LiveView
```

### Block 52 (line 162)

```
上記の画像は、Android Robot Controller (RC) フォン上のプレビュー（LiveView と呼ばれる）を示しています。REV Control Hub は RC プレビューを生成しますが、HDMI 外部モニターまたは ``scrcpy`` で見ることができます。``scrcpy`` はここで見つけることができます：
```

### Block 53 (line 166)

```
AprilTag 軸
```

### Block 54 (line 169)

```
SDK は、基礎となるポーズデータを次のように提供します：
```

### Block 55 (line 171)

```
-  位置は、**カメラレンズから AprilTag** への X、Y、Z 距離に基づいています。
-  方向は、右手の法則を使用して、これらの軸を中心とした回転に基づいています。
```

### Block 56 (line 175)

```
新しい SDK での軸の指定は次のとおりです：
```

### Block 57 (line 177)

```
- Y 軸はカメラレンズの中心から **まっすぐ外側** を指します
- X 軸は Y 軸に垂直に **右方向** を指します
- Z 軸は Y と X に垂直に **上方向** を指します
```

### Block 58 (line 181)

```
カメラがロボット上で直立して前方を向いている場合、これらの軸は次のために使用されるロボット座標系と一致しています
```

### Block 59 (line 184)

```
注：これらの軸は、カメラの参照フレームからでも、公式 AprilTag
```

### Block 60 (line 187)

```
SDK は AprilTag **回転** データを次のように提供します：
```

### Block 61 (line 189)

```
- **ピッチ** は X 軸を中心とした回転の測定値です
- **ロール** は Y 軸を中心とした回転の測定値です
- ヘディング、または **ヨー** は、Z 軸を中心とした回転の測定値です
```

### Block 62 (line 193)

```
回転は、伝統的な右手の法則に従います：親指が正の軸に沿って指している状態で、指は正の回転の方向に巻き付きます。
```

### Block 63 (line 195)

```
さらなる議論はここで提供されています：
```

### Block 64 (line 199)

```
注：この記事では、**FIRST Tech Challenge** の
:ref:`Field Coordinate System <game_specific_resources/field_coordinate_system/field-coordinate-system:scope>` について説明しています。
```

### Block 65 (line 202)

```
OpMode は、ナビゲーションのためにロボットの方向を全体のフィールドまたは
```

### Block 66 (line 205)

```
高度な使用法
```

### Block 67 (line 208)

```
**オプション 1**
```

### Block 68 (line 210)

```
タグの **ゲームフィールド上の** 位置と方向が事前に指定されている場合、タグのポーズデータは、高度な OpMode によって使用されて、フィールド上のロボットの位置を計算できます。この変換計算は、読者への演習として、リアルタイムでタグのポーズデータを使用してロボットがフィールド上の目的の場所にナビゲートすることを可能にします。
**オプション 2**
```

### Block 69 (line 213)

```
ビジョン処理は、重要な **CPU リソース** と USB 通信** 帯域幅** を消費する可能性があります。*FIRST* Tech Challenge チームは、CPU および帯域幅リソースの過負荷のリスクに対して、より高い解像度と速度（フレーム/秒）の利点のバランスをとることができます。SDK 8.2 以降は、このバランスを管理するための多数のツールを提供します：
```

### Block 70 (line 215)

```
- カメラの解像度を選択
- RC プレビュー（LiveView と呼ばれる）を無効化および有効化
- AprilTag（または Color Processing）プロセッサを無効化および有効化
- カメラストリームを閉じる
- 圧縮されたビデオストリーミング形式を選択
- フレーム/秒を測定
- デシメーション（ダウンサンプリング）を設定
- ポーズソルバーアルゴリズムを選択
```

### Block 71 (line 224)

```
**オプション 3**
```

### Block 72 (line 226)

```
より鮮明なカメラ画像は、AprilTag（および Color Processing）ビジョン処理を改善できます。SDK は、FTC Blocks でも利用可能な強力な **ウェブカメラコントロール** （露出、ゲイン、フォーカスなど）を提供します！これらのコントロールは、さまざまな照明条件下で適用できます。
```

### Block 73 (line 228)

```
露出とゲインは一緒に調整されます。SDK は Java サンプル OpMode ``ConceptAprilTagOptimizeExposure.java`` を提供します。
```

### Block 74 (line 230)

```
**オプション 4**
```

### Block 75 (line 232)

```
上記の **AprilTag 軸** で説明した参照フレームは、8.2 SDK 以降でデフォルトで計算および提供されます。高度なチームは、AprilTag/EasyOpenCV パイプラインからの** 生の値** に基づいて、独自のポーズ計算を実行することを好むかもしれません。
```

### Block 76 (line 234)

```
これらの生の値は、Java と Blocks プログラマーが利用できます。Java バージョンはここに示されています：
```

### Block 77 (line 252)

```
これらの生の値は、SDK によって次のようにデフォルトのインターフェースに変換されます：
```

### Block 78 (line 273)

```
再度、さらなる議論はここで提供されています：
```

### Block 79 (line 277)

```
まとめ
```

### Block 80 (line 280)

```
AprilTag は、QR コードに似たスキャン画像を使用する、人気のあるカメラベースの技術です。
```

### Block 81 (line 282)

```
SDK バージョン 8.2 以降には、AprilTag と EasyOpenCV の主要な機能が含まれています。EasyOpenCV は、画像処理のための OpenCV との *FIRST* Tech Challenge に最適化されたインターフェースです。これらの方法は、**Java と Blocks プログラマー** が便利に使用できるようにパッケージ化されています。
```

### Block 82 (line 284)

```
デフォルトでは、SDK は 36h11 ファミリーの任意の AprilTag の ID コードを検出できます。
```

### Block 83 (line 286)

```
デフォルトまたはカスタムタグライブラリの AprilTags の場合、インターフェースは **カメラの参照フレーム** から計算された**ポーズ** 推定（位置と回転）を提供します。ソースデータは、高度なチームでも利用できます。
```

### Block 84 (line 288)

```
AprilTag 機能は、Android RC フォンカメラとウェブカメラで動作します。各カメラは、良好なポーズ推定を提供するために、特定の解像度の **キャリブレーションデータ** を必要とします。
```

### Block 85 (line 290)

```
複数のカメラがサポートされており、単一の OpMode で AprilTag と Color Processing を使用できます。AprilTag 検出は、FTC Blocks でも利用可能なウェブカメラカメラコントロールで改善されます。
```

### Block 86 (line 292)

```
***FIRST* Tech Challenge において、AprilTag は CENTERSTAGE を飾る準備ができています！**
```

### Block 87 (line 296)

```
謝辞:
```

### Block 88 (line 303)

```
質問、コメント、訂正は westsiderobotics@verizon.net までお寄せください。
```


## apriltag/vision_portal/apriltag_library/apriltag-library.rst

### Block 1 (line 1)

```
AprilTag ライブラリ
```

### Block 2 (line 4)

```
**FIRST** Tech Challenge の競技では、**OpMode** は検出すべき既知の**AprilTag** セットを持っています。これらはデフォルトでプリロードされているか、カスタムタグの有無に関わらず、皆さんが指定することができます。
```

### Block 3 (line 6)

```
これらのタグは**AprilTag Library** を形成します。各ライブラリタグには4から6のプロパティがあり、**Metadata** ページで説明されています。
```

### Block 4 (line 8)

```
このページでは、**AprilTag** ライブラリを作成する多くの方法を示します。**Initialization** ページでは、これが**OpMode** で**AprilTag** を使用するための準備の** ステップ1** （オプション）であることを説明しました。**AprilTag** ライブラリの使用をマスターするために、** これらの例を順番に試してください** 。
```

### Block 5 (line 10)

```
簡単な方法
```

### Block 6 (line 13)

```
まず、ライブラリなしから始めましょう！**OpMode** が現在のシーズンのデフォルトのみを使用する場合、ライブラリの操作は不要です。
```

### Block 7 (line 15)

```
次のように**AprilTagProcessor** を作成するだけです：
```

### Block 8 (line 24)

```
         :alt: シンプルな AprilTag Processor
```

### Block 9 (line 26)

```
         シンプルな AprilTag Processor
```

### Block 10 (line 35)

```
         // AprilTag プロセッサを作成し、変数に割り当てます。
         myAprilTagProcessor = AprilTagProcessor.easyCreateWithDefaults();**AprilTag Processor** を作成するには、ライブラリの指定が必要です。この「簡単な方法」でも、背後でデフォルトのライブラリを指定しています。
```

### Block 11 (line 38)

```
デフォルトライブラリ
~~~~~~~~~~~~~~~~~~~~**SDK** は、事前定義された**AprilTag** の2つのコアライブラリを使用します：
```

### Block 12 (line 41)

```
-  サンプル**OpMode** でのみ使用されるタグ
-  ロボットゲーム（競技）でのみ使用されるタグ
```

### Block 13 (line 44)

```
最初のライブラリは ``SampleTagLibrary`` と呼ばれ、SDK 8.2で利用可能です。基本的な**Metadata** 値は次のとおりです：
```

### Block 14 (line 51)

```
2番目のライブラリは ``CenterStageTagLibrary`` と呼ばれ、将来の競技のみを対象としています。SDK 8.2で現在利用可能ですが、現在は3つの「プレースホルダー」タグを保持しています：
```

### Block 15 (line 57)

```
2023年9月のキックオフ後、これらは**CENTERSTAGE** の** 実際のタグ** に置き換えられます（SDK 9.0で）。
```

### Block 16 (line 59)

```
便宜上、3番目のライブラリには、これら2つのコアライブラリの** 両方** が含まれており、それ以外は何も含まれていません。これがデフォルトで、``CurrentGameTagLibrary`` と呼ばれます。
```

### Block 17 (line 62)

```
~~~~~~~~~~~~~~~~~~**Processor** の** 任意の側面** を指定するには、**Processor Builder** を使用します。少なくとも2つのコマンドが必要です：
```

### Block 18 (line 64)

```
-  Java キーワード ``new`` を使用して**Builder** を作成
```

### Block 19 (line 66)

```
-  機能を指定/追加した後、``.build()`` メソッドの呼び出しで完了
```

### Block 20 (line 68)

```
これらのアクション間で、**OpMode** は3つのライブラリのいずれかを**Processor Builder** に直接追加します。すべての事前定義タグを含むデフォルトの ``CurrentGameTagLibrary`` を使用するのが最も簡単です。
```

### Block 21 (line 74)

```
      まず、この式を作成します。最初のコンポーネントを ``AprilTagProcessor.Builder`` ツールボックス（またはパレット）から描画し、2番目のコンポーネントを ``AprilTagLibrary`` ツールボックスから描画します。
```

### Block 22 (line 79)

```
         :alt: 現在のゲームのタグライブラリを設定
```

### Block 23 (line 81)

```
         現在のゲームのタグライブラリを設定** これを囲むように** （前後に）、**Processor Builder** を** 作成** する1つのブロックと、``.build()`` でプロセスを** 完了** する別のブロックを配置します。
```

### Block 24 (line 86)

```
         :alt: Builder の完成
```

### Block 25 (line 88)

```
         Builder の完成
```

### Block 26 (line 90)

```
      これらは ``AprilTagProcessor.Builder`` ツールボックスの最初と最後のブロックです。残りのブロックは、**Processor** のオプション機能を設定するために使用されます。ここでは、ライブラリのみを設定しています。
```

### Block 27 (line 100)

```
         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
```

### Block 28 (line 103)

```
         // タグライブラリを設定します。
         // 現在のシーズンの AprilTagLibrary を取得します。
```

### Block 29 (line 107)

```
         // AprilTag プロセッサをビルドし、変数に割り当てます。
```

### Block 30 (line 111)

```
ライブラリ変数
```

### Block 31 (line 114)

```
別の方法として、まずライブラリを独自の変数名に格納することもできます。次に、**AprilTag Processor** にその名前を指定します。ここでは ``myAprilTagLibrary`` を使用します（他の名前でも問題ありません）。
```

### Block 32 (line 120)

```
      まず、この式を作成します。最初のコンポーネントを ``AprilTagLibrary`` ツールボックスから描画し、2番目のコンポーネントを ``AprilTagProcessor.Builder`` ツールボックスから描画します。
```

### Block 33 (line 125)

```
         :alt: タグライブラリを設定
```

### Block 34 (line 127)

```
         タグライブラリを設定
```

### Block 35 (line 129)

```
      前と同様に、** これを囲むように** （前後に）、**Processor Builder** を** 作成** する1つのブロックと、``.build()`` でプロセスを** 完了** する別のブロックを配置します。
```

### Block 36 (line 134)

```
         :alt: AprilTag Processor をビルド
```

### Block 37 (line 136)

```
         AprilTag Processor をビルド
```

### Block 38 (line 147)

```
         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
```

### Block 39 (line 150)

```
         // 現在のシーズンの AprilTagLibrary を取得します。
```

### Block 40 (line 153)

```
         // タグライブラリを設定します。
```

### Block 41 (line 156)

```
         // AprilTag プロセッサをビルドし、変数に割り当てます。
```

### Block 42 (line 160)

```
ライブラリ Builder、デフォルトを使用
```

### Block 43 (line 163)

```
次に、**Builder** パターンを試して、事前定義された**AprilTag** のみを含むライブラリを作成します。これは必要ではありませんが（ビルドする新しいものはありません！）、簡単な導入です。
```

### Block 44 (line 169)

```
      -**Library Builder** を作成します。**Processor Builder** とは異なります。
      -  次に ``addTags`` ブロックを使用します - 複数形の "tags" であり、"tag" ではないことに注意してください。
      -  ``.build`` コマンドでプロセスを完了します。
```

### Block 45 (line 173)

```
      ビルドされたライブラリは、ここでは ``myAprilTagLibrary`` と呼ばれる変数に割り当てられるか保存されます。
```

### Block 46 (line 178)

```
         :alt: タグライブラリをビルド
```

### Block 47 (line 180)

```
         タグライブラリをビルド
```

### Block 48 (line 182)

```
      次に、おなじみの手順が続きます：
```

### Block 49 (line 184)

```
      -**Processor Builder** を作成します。
      -  次に、前のシーケンスでビルドおよび保存されたライブラリを設定または追加します。
      -  ``.build`` コマンドでプロセスを完了します。
```

### Block 50 (line 191)

```
         :alt: タグプロセッサをビルド
```

### Block 51 (line 193)

```
         タグプロセッサをビルド
```

### Block 52 (line 195)

```
      最終結果は前の例と同じですが、今度は**Library Builder** の使用方法がわかります。
```

### Block 53 (line 207)

```
         // 新しい AprilTagLibrary.Builder オブジェクトを作成し、変数に割り当てます。
```

### Block 54 (line 210)

```
         // 指定された AprilTagLibrary からすべてのタグを AprilTagLibrary.Builder に追加します。
         // 現在のシーズンの AprilTagLibrary を取得します。
```

### Block 55 (line 214)

```
         // AprilTag ライブラリをビルドし、変数に割り当てます。
```

### Block 56 (line 217)

```
         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
```

### Block 57 (line 220)

```
         // タグライブラリを設定します。
```

### Block 58 (line 223)

```
         // AprilTag プロセッサをビルドし、変数に割り当てます。
```

### Block 59 (line 227)

```
カスタムタグ - 直接指定
```

### Block 60 (line 230)

```
最後に、ライブラリにカスタムタグを追加する準備が整いました。
```

### Block 61 (line 232)

```
各タグには**Metadata** が必要です。次のように、新しいタグに**Metadata** 値を直接入力できます。
```

### Block 62 (line 238)

```
      3番目のブロックは、カスタムタグをライブラリに追加します。他のすべてのブロックは前の例と同じです。
```

### Block 63 (line 243)

```
         :alt: カスタムタグライブラリ
```

### Block 64 (line 245)

```
         タグライブラリにカスタムタグを追加
```

### Block 65 (line 250)

```
      カスタムタグは**1行の新しいコード** で追加され、それ以外は前の例と同じです。
```

### Block 66 (line 259)

```
         // 新しい AprilTagLibrary.Builder オブジェクトを作成し、変数に割り当てます。
```

### Block 67 (line 262)

```
         // 指定された AprilTagLibrary からすべてのタグを AprilTagLibrary.Builder に追加します。
         // 現在のシーズンの AprilTagLibrary を取得します。
```

### Block 68 (line 266)

```
         // ポーズ情報なしでタグを AprilTagLibrary.Builder に追加します。
```

### Block 69 (line 269)

```
         // AprilTag ライブラリをビルドし、変数に割り当てます。
```

### Block 70 (line 272)

```
         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
```

### Block 71 (line 275)

```
         // タグライブラリを設定します。
```

### Block 72 (line 278)

```
         // AprilTag プロセッサをビルドし、変数に割り当てます。
```

### Block 73 (line 282)

```
カスタムタグ - 変数を使用
```

### Block 74 (line 285)

```
別の方法として、**Metadata** を変数に割り当て、その変数を使用して新しい**AprilTag** を作成できます。
```

### Block 75 (line 291)

```
      これら2つのブロックは、前の例の1つの新しいブロックを置き換えることができます。
```

### Block 76 (line 296)

```
         :alt: 変数 Metadata
```

### Block 77 (line 298)

```
         変数を使用した Metadata の設定
```

### Block 78 (line 300)

```
      これらのブロックは分離されており、**Metadata** 変数は**Library Builder** で追加される前のどこででも初期化/割り当てできることを示しています。使用の直前に表示する必要はありません。
```

### Block 79 (line 305)

```
      カスタムタグは**2行のコード** で追加され、前の例の**1行の新しいコード** を置き換えます。
```

### Block 80 (line 315)

```
         // 新しい AprilTagLibrary.Builder オブジェクトを作成し、変数に割り当てます。
```

### Block 81 (line 318)

```
         // 指定された AprilTagLibrary からすべてのタグを AprilTagLibrary.Builder に追加します。
         // 現在のシーズンの AprilTagLibrary を取得します。
```

### Block 82 (line 322)

```
         // 新しい AprilTagMetdata オブジェクトを作成し、変数に割り当てます。
```

### Block 83 (line 325)

```
         // タグを AprilTagLibrary.Builder に追加します。
```

### Block 84 (line 328)

```
         // AprilTag ライブラリをビルドし、変数に割り当てます。
```

### Block 85 (line 331)

```
         // 新しい AprilTagProcessor.Builder オブジェクトを作成し、変数に割り当てます。
```

### Block 86 (line 334)

```
         // タグライブラリを設定します。
```

### Block 87 (line 337)

```
         // AprilTag プロセッサをビルドし、変数に割り当てます。
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();**Blocks** または**Java** の場合、複数のタグを複数の（より短い！）変数名（``myTag1`` 、``myTag2`` など）で追加できます。
```

### Block 88 (line 340)

```
上書き
```

### Block 89 (line 343)

```
ライブラリに既に存在するタグと** 同じ ID コード** を持つカスタム**AprilTag** を作成する場合があります。これは** 上書き** であり、許可するかどうかを選択できます。
```

### Block 90 (line 345)

```
``setAllowOverwrite()`` が ``false`` （デフォルト）に設定されており、上書きが試みられると、**OpMode** は適切なエラーメッセージとともにクラッシュします。
```

### Block 91 (line 347)

```
``true`` に設定すると、カスタムタグが既存のタグを置き換えます。
```

### Block 92 (line 349)

```
なぜこれを行うのでしょうか？タグサイズが正確ではないとします。同じ**Metadata** で新しいタグを入力できますが、タグサイズを修正します。
```

### Block 93 (line 351)

```
または、独自のタグ名または距離単位を使用することを好む場合があります。
```

### Block 94 (line 353)

```
上級ユーザーは、** ゲームフィールド** 上の事前定義タグの** 位置** を指定したい場合があります。これは、オプションの**Vector** および**Quaternion** フィールドで行うことができます。
```


## apriltag/vision_portal/vision_multiportal/vision-multiportal.rst

### Block 1 (line 4)

```
**SDK** は2つのポータルを収容でき、それぞれに **AprilTag** および **TFOD** プロセッサを含む完全な機能があり、切り替え可能なカメラさえあります。USB帯域幅を考慮する必要があります。特に外部USBハブを共有するウェブカメラの場合です。
```

### Block 2 (line 9)

```
各ポータルには、Android オペレーティングシステムによって ``Viewport ID`` が割り当てられます。初期化時に、**OpMode** はこれらのID番号を ** キャプチャ** し、ポータルの操作に使用する必要があります。
```

### Block 3 (line 11)

```
Android は通常、**OpMode** の各実行ごとに異なる **Viewport ID** 番号を割り当てます。必要に応じて、**Telemetry** を **Driver Station** に送信することでこれを観察できます。
```

### Block 4 (line 13)

```
``makeMultiPortalView()`` ブロックまたはメソッドは、**Viewport ID** のリストを返します。各IDをリストから抽出し、``setCameraMonitorViewId()`` ブロックまたはメソッドを使用して各 **VisionPortal Builder** に提供する必要があります。
```

### Block 5 (line 15)

```
「デュアルカメラ」は以前（そして今でも）**EasyOpenCV** で利用可能でした。今では **SDK** 内でこれが可能です。
```

### Block 6 (line 17)

```
テスト OpMode
```

### Block 7 (line 20)

```
サンプルFTC **Blocks OpMode** は `こちら <https://gist.github.com/WestsideRobotics/587b5c74375429ac4a929f690ae40940>`__ に投稿されており、**2つのカメラから同時に** **AprilTag** 検出を実証しています。Java版については、**Blocks** 編集ウィンドウで ``Export to Java`` をクリックしてください。
```

### Block 8 (line 22)

```
以下は、そのテスト **OpMode** の画像です。注意深く研究すると、複数のカメラストリームを同時に作成および操作するための **Blocks** および **Java** メソッドをよりよく理解できます。
```

### Block 9 (line 24)

```
右クリックして新しいブラウザタブで画像を開き、大きなPCスクリーンで拡大表示してください。
```

### Block 10 (line 31)

```
   Blocks Multiportal OpMode の例
```

### Block 11 (line 33)

```
Moto e4 **RC** スマートフォンでは、**OpMode** は内蔵スマートフォンカメラとウェブカメラを一緒に実行できます。
```

### Block 12 (line 35)

```
**Control Hub** では、2つのウェブカメラを実行できます：
```

### Block 13 (line 37)

```
- 両方を **Hub** に直接接続、または
- 両方を非電源式USBハブに接続（より制限されたUSB帯域幅で）
```

### Block 14 (line 40)

```
デュアルプレビュー
```

### Block 15 (line 43)

```
デュアル **RC** プレビューは ``VERTICAL`` として表示するか、列挙型 ``HORIZONTAL`` で並べて表示できます：
```

### Block 16 (line 48)

```
   :alt: デュアル RC プレビュー
```

### Block 17 (line 50)

```
   デュアル RC プレビュー
```

### Block 18 (line 52)

```
**DS Camera Stream** プレビューは、1つのカメラのビューのみを表示できます（`既知の特性 <https://github.com/FIRST-Tech-Challenge/FtcRobotController/issues/585>`__ ）。
```

### Block 19 (line 54)

```
USB 帯域幅
```

### Block 20 (line 57)

```
**USB帯域幅** はデュアル ** ウェブカメラ** の懸念事項です。内部スマートフォンカメラには独立した高速相互接続（USBではない）があり、追加されたUSBウェブカメラの影響を受けません。
```

### Block 21 (line 59)

```
USB帯域幅の分析については、**Managing CPU and Bandwidth** ページを参照してください。
```

### Block 22 (line 61)

```
2つのウェブカメラは同じフォーマットまたは解像度を使用する *必要はありません* 。上記のテストでは、Logitech C920とLogitech C270に同じフォーマットと解像度が適用されました。
```

### Block 23 (line 66)

```
**Control Hub に直接接続された** デュアルウェブカメラの場合、USB 2.0およびUSB 3.0ポートは異なるバス上にあります。
```

### Block 24 (line 68)

```
これにより、USB帯域幅容量に関する懸念が軽減されますが、解像度が高いと自動最適化されたフレームレートが低下します（以下のテストデータを参照）。
```

### Block 25 (line 70)

```
ここでは、ストリームフォーマットの選択にはほとんど影響がありません。しかし、USB 2.0バスは **Control Hub** の **WiFiラジオ** も運ぶため、ウェブカメラを追加するとその信頼性に影響を与える可能性があります。
```

### Block 26 (line 72)

```
外部 USB Hub
```

### Block 27 (line 75)

```
一方、** 外部USBハブ**（CH 3.0ポートに接続）上の両方のウェブカメラは、**USB帯域幅制限** を超える可能性があります（ここでは定量化されていません）。
```

### Block 28 (line 77)

```
レガシー **YUY2フォーマット** では、1つのウェブカメラまたはもう1つのウェブカメラが、おおよそ640x360解像度を超えるとストリーミングを停止する場合があります。これは、検出がなく、``scrcpy`` 経由の **RC** プレビューで青い画面で示されます。
```

### Block 29 (line 79)

```
**MJPEGフォーマット** では、おおよそ432x240未満の解像度では、画像が劣化して少なくとも1つのウェブカメラで **AprilTag** 検出を防ぐ可能性があり、より高い解像度では **RC** アプリを停止するか、**Control Hub** をクラッシュさせる場合があります。
```

### Block 30 (line 81)

```
両方のフォーマットで、解像度が高いとフレームレートが低下します。**Managing CPU and Bandwidth** ページでは、テスト、トレードオフ、最適化について説明しています。
```

### Block 31 (line 83)

```
チームは、フレーム/秒（FPS）を提供する新しいレポート機能 ``getFps()`` の支援を受けて、これらのトレードオフを評価できます。これは **Blocks** および **Java** で利用できます。
```


## apriltag/vision_portal/visionportal_overview/visionportal-overview.rst

### Block 1 (line 1)

```
VisionPortal 概要
```

### Block 2 (line 4)

```
**FIRST Tech Challenge** は**VisionPortal** を導入しました。これは、ビジョン処理のための包括的な新しいインターフェースです。
```

### Block 3 (line 6)

```
-  **FTC Blocks と Java** チームの場合、VisionPortal は**AprilTag** と**EasyOpenCV** の主要な機能に加えて、**TensorFlow Object Detection (TFOD)** を同時に提供します！
```

### Block 4 (line 13)

```
      AprilTag と TensorFlow の両方を使用したデュアルプレビュー
```

### Block 5 (line 17)

```
-  **AprilTag** 検出には、ID コードと** ポーズ**: カメラに対するタグの位置と方向が含まれます。
```

### Block 6 (line 19)

```
-  ウェブカメラの AprilTag と TFOD のパフォーマンスを向上させることができる **Camera Controls** が、**FTC Blocks** ユーザーに完全に利用可能になりました。
```

### Block 7 (line 21)

```
-  **複数のカメラ** を同時に操作できます – フォンカメラおよび/またはウェブカメラ。
```

### Block 8 (line 28)

```
      複数カメラビュー
```

### Block 9 (line 32)

```
-  **サンプル OpModes** と新しいツールが、**Builder パターン** を含むこれらの機能の操作とカスタマイズに利用できます。
```

### Block 10 (line 34)

```
-  重いビデオ処理の場合、**CPU リソース** と**USB 帯域幅** を管理するための多くのオプションが利用可能です。
```

### Block 11 (line 36)

```
-  DS と RC のプレビューは **大きく** できます！
```

### Block 12 (line 43)

```
      フルスクリーンプレビュー
```

### Block 13 (line 45)

```
VisionPortal 以降には、他にも多くの新機能と改善された機能が `あなたの発見を待っています
```

### Block 14 (line 50)

```
2023-2024 CENTERSTAGE シーズンの準備として、新しい Software Development Kit (SDK) **VisionPortal** には**AprilTag 技術の組み込みサポート** が含まれています。以前は、チームは外部ライブラリをダウンロードして組み込む必要があり、プログラミング作業が複雑になっていました。
```

### Block 15 (line 52)

```
AprilTag は、**位置と方向** を推定するために使用される、シンプルな白黒タグを検出するための人気のあるビジョン技術です。2022-2023 POWERPLAY ゲームでは、多くのチームが Signal Sleeve 認識のための AprilTag の信頼性の高い Autonomous パフォーマンスを楽しみました。
```

### Block 16 (line 61)

```
**このガイドのすべてのセクションは、** :doc:`AprilTag 入門 <../apriltag_intro/apriltag-intro>` **を事前に読んでいることを前提としています。**
```

### Block 17 (line 63)

```
SDK はデフォルトで、**カメラに対する** AprilTag ポーズを記述します。この計算プロセスは**ポーズ推定** と呼ばれ、これは**カメラキャリブレーション** を含む多くの要因に基づく推定値のみであることを強調する用語です。目標を達成するために AprilTag の最適な使用法を決定する必要があります。
```

### Block 18 (line 65)

```
   :doc:`AprilTag 入門 <../apriltag_intro/apriltag-intro>`
   :doc:`ビジョンプロセッサの初期化 <../vision_processor_init/vision-processor-init>`
   **VisionPortal** の初期化 <../visionportal_init/visionportal-init>
   **VisionPortal** プレビュー <../visionportal_previews/visionportal-previews>
   **AprilTag ID** コード <../apriltag_id_code/apriltag-id-code>
   **AprilTag** メタデータ <../apriltag_metadata/apriltag-metadata>
   **AprilTag** 参照フレーム <../apriltag_reference_frame/apriltag-reference-frame>
   **AprilTag** カメラキャリブレーション <../apriltag_camera_calibration/apriltag-camera-calibration>
   **AprilTag** ポーズ <../apriltag_pose/apriltag-pose>
   **AprilTag** ライブラリ <../apriltag_library/apriltag-library>
   **VisionPortal** の CPU と帯域幅 <../visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth>
   **VisionPortal** カメラコントロール <../visionportal_camera_controls/visionportal-camera-controls>
   ビジョンマルチポータル <../vision_multiportal/vision-multiportal>
   **AprilTag** 高度な使用法 <../apriltag_advanced_use/apriltag-advanced-use>
```

### Block 19 (line 82)

```
謝辞
```

### Block 20 (line 89)

```
質問、コメント、訂正は westsiderobotics@verizon.net までお寄せください。
```


## color_processing/color-blob-concepts/color-blob-concepts.rst

### Block 1 (line 1)

```
Color Blob の概念
```

### Block 2 (line 4)

```
**Color Blob** は、画像内の類似した色のピクセルの連続した領域です。**Color Blob** 検出は、ロボットビジョンの多くのアプリケーションで重要です。
```

### Block 3 (line 6)

```
Color Blob とは？
-----------------**Color Blob** は、次の特性を持つピクセルのグループです：
```

### Block 4 (line 9)

```
- 類似した色（指定された色範囲内）
- 空間的に接続されている（隣接しているか近接している）
- 十分な大きさ（最小サイズのしきい値を超える）
```

### Block 5 (line 13)

```
たとえば、フィールド上の赤い**Team Prop** は、赤い**Color Blob** として検出できます。
```

### Block 6 (line 15)

```
Blob 検出プロセス
-----------------**Color Blob** を検出する基本的な手順は次のとおりです：
```

### Block 7 (line 18)

```
1.** 色の範囲を定義**: 検出したい色の範囲を指定します
2. ** 画像を変換**: 画像を適切な色空間に変換します（例：**RGB** から**HSV** ）
3.**しきい値処理**: 色範囲内のピクセルを識別します
4. ** 輪郭を検出**: 接続されたピクセルの領域を見つけます
5. **Blob をフィルタリング**: サイズ、形状、または他の基準で **Blob** をフィルタリングします
```

### Block 8 (line 24)

```
Blob のプロパティ
```

### Block 9 (line 27)

```
検出された**Color Blob** には、多くの有用なプロパティがあります：
```

### Block 10 (line 29)

```
-** 位置**: **Blob** の中心座標（X、Y）
-** サイズ**: **Blob** 内のピクセル数または面積
-** 境界ボックス**: **Blob** を囲む長方形
-** 形状**: アスペクト比、円形度、またはその他の形状記述子
```

### Block 11 (line 34)

```
これらのプロパティは、**Blob** を識別および追跡するために使用できます。
```

### Block 12 (line 36)

```
Blob Detection の課題
----------------------**Color Blob** 検出にはいくつかの課題があります：** 照明条件**
  照明の変化は、色の外観に影響を与える可能性があります。**HSV** 色空間を使用し、色範囲を慎重に選択することで、これを軽減できます。** ノイズ** 小さなピクセルグループがノイズとして検出される場合があります。最小サイズのしきい値を使用してこれらをフィルタリングします。** オクルージョン** オブジェクトが部分的に隠されている場合、複数の**Blob** として検出される可能性があります。** 類似した色** 複数のオブジェクトが類似した色を持つ場合、1つの大きな**Blob** として結合される可能性があります。
```

### Block 13 (line 41)

```
-------------**FTC SDK** は、**Color Blob** 検出を簡素化する**Color Locator** プロセッサを提供します。これは、次のような高度な機能を提供します：
```

### Block 14 (line 43)

```
- 複数の色範囲のサポート
- 自動**Blob** フィルタリング
- リアルタイムプレビュー
- 調整可能なパラメーター**Color Locator** の使用方法の詳細については、**Color Locator** シリーズのチュートリアルを参照してください。
```

### Block 15 (line 48)

```
実用的な応用
------------**Color Blob** 検出は、次のような多くの**FTC** アプリケーションに役立ちます：
```

### Block 16 (line 51)

```
-**Team Prop** の検出とローカライゼーション
- ゲームピースの識別と追跡
- フィールドエレメントのナビゲーション
- 色ベースの意思決定
```

### Block 17 (line 56)

```
適切な色範囲と検出パラメーターを選択することで、ロボットのビジョンシステムを堅牢で信頼性の高いものにできます。
```


## color_processing/color-spaces/color-spaces.rst

### Block 1 (line 1)

```
色空間
```

### Block 2 (line 4)

```
色空間は、色を表現するための数学的モデルです。最も一般的な色空間はRGB（赤、緑、青）ですが、画像処理には他にも便利な色空間があります。
```

### Block 3 (line 6)

```
RGB 色空間
```

### Block 4 (line 9)

```
**RGB** 色空間は、赤、緑、青の3つの原色を組み合わせて色を作成します。各ピクセルは、0から255の範囲の3つの値（赤、緑、青の強度）で表されます。**RGB** は、カメラセンサーとディスプレイが色を表現する方法であるため、最も一般的です。しかし、色を検出するには常に最適とは限りません。
```

### Block 5 (line 11)

```
HSV 色空間
----------**HSV** （色相、彩度、明度）色空間は、人間が色を知覚する方法により近い方法で色を表現します：
```

### Block 6 (line 14)

```
-** 色相（Hue）**: 色の種類（赤、緑、青など）。0から180の範囲の角度として表されます。
- ** 彩度（Saturation）**: 色の純度または強度。0（灰色）から255（純粋な色）の範囲です。
- ** 明度（Value）**: 色の明るさ。0（黒）から255（明るい）の範囲です。
```

### Block 7 (line 18)

```
**HSV** は、照明条件が変化する場合でも色を検出するのに役立ちます。色（色相）を明るさ（明度）から分離できるためです。
```

### Block 8 (line 20)

```
YCrCb 色空間
------------**YCrCb** 色空間は、輝度（明るさ）を色度（色情報）から分離します：
```

### Block 9 (line 23)

```
-**Y**: 輝度（明るさ）
- **Cr**: 赤色度
- **Cb**: 青色度
```

### Block 10 (line 27)

```
この色空間は、ビデオ圧縮で一般的に使用され、特定の色検出タスクに役立つ場合があります。
```

### Block 11 (line 29)

```
色空間の変換
```

### Block 12 (line 32)

```
**FTC SDK** は、色空間間の変換をサポートしています。**OpenCV** を使用して、画像をある色空間から別の色空間に変換できます。
```

### Block 13 (line 34)

```
色空間の選択
```

### Block 14 (line 37)

```
色検出に使用する色空間は、特定のアプリケーションによって異なります：
```

### Block 15 (line 39)

```
-**RGB**: デフォルトですが、照明変化に敏感です
- **HSV**: 変化する照明条件下での色検出に適しています
- **YCrCb**: 一部の高度なアプリケーションに役立ちます
```

### Block 16 (line 43)

```
実験して、特定のタスクに最適な色空間を見つけてください。
```

### Block 17 (line 45)

```
色の範囲
```

### Block 18 (line 48)

```
色空間で作業する場合、検出したい色の範囲を定義する必要があります。たとえば、**HSV** では、赤色の範囲を次のように定義できます：
```

### Block 19 (line 50)

```
- 最小色相: 0、最大色相: 10（明るい赤）
- または最小色相: 170、最大色相: 180（暗い赤）
- 彩度と明度の範囲は、照明条件に基づいて調整します**Color Locator** などのツールは、適切な色範囲を見つけるのに役立ちます。
```


## contrib/guidelines/guidelines.rst

### Block 1 (line 1)

```
貢献ガイドライン
```

### Block 2 (line 5)

```
   この章は主に上流の公式 FTC Docs への貢献について記述しています。
   この日本語翻訳リポジトリへの貢献については、このガイドラインを参照しつつも、
   リポジトリ上の翻訳ルール（TRANSLATION_GUIDE.md）を優先して参照してください。
```

### Block 3 (line 9)

```
貢献者はプロジェクトの生命線です。貢献を歓迎しますが、すべての方に
:doc:`Gracious Professional </gracious_professionalism/gp>` であることを思い出していただきたいと思います。
```

### Block 4 (line 12)

```
Issue の作成
```

### Block 5 (line 15)

```
まず、問題や希望する機能を説明する Issue を作成してください。
これにより、その段階で問題が解決するか、リクエストや実施すべき作業が明確になる可能性のある議論が可能になります。
```

### Block 6 (line 18)

```
Issue には2つのタイプがあります：バグと機能リクエストです。バグレポートは、ドキュメントの問題を説明する Issue です。機能リクエストは、ドキュメントに追加すべき新機能を説明する Issue です。
```

### Block 7 (line 20)

```
どちらを作成する場合も、必ず重複がないか確認してください。重複を見つけた場合は、その Issue にコメントし、可能な限り入力を追加してください。可能であれば、問題を修正するプルリクエストを見せていただけると嬉しいです。問題の修正方法がわからない場合は、それで問題ありません。
```

### Block 8 (line 22)

```
バグレポート
```

### Block 9 (line 25)

```
* バグの説明
* 期待される動作
* バグを再現する手順（該当する場合）
* スクリーンショット（該当する場合）
```

### Block 10 (line 30)

```
機能リクエスト
```

### Block 11 (line 33)

```
* 機能の説明
* この機能を追加すべきだと思う理由
* スクリーンショット（該当する場合）
```

### Block 12 (line 37)

```
プルリクエストの作成
```

### Block 13 (line 40)

```
プルリクエスト（PR）は、あるブランチから別のブランチへの変更セットをマージする提案です。
プルリクエストでは、協力者が変更をメインコードベースに統合する前に、提案された変更セットをレビューして議論できます。
GitHub では、PR はソースブランチのコンテンツとターゲットブランチのコンテンツの違いを表示します。
```

### Block 14 (line 44)

```
PR は GitHub の `FTC Docs <https://github.com/FIRST-Tech-Challenge/ftcdocs>`__ リポジトリに作成する必要があります。タイトルは、PR の目的を*簡潔*に説明することを目指してください。PR の作成の詳細については、GitHub の
```

### Block 15 (line 46)

```
を参照してください。
変更を行うための具体的なガイダンスがあります。:doc:`変更の概要 </contrib/tutorials/overview/overview>` から始めてください。
```

### Block 16 (line 49)

```
奥付
```

### Block 17 (line 52)

```
FTC Docs は、`Read the Docs <https://readthedocs.org/>`__ が提供する `テーマ <https://github.com/readthedocs/sphinx_rtd_theme>`__ を使用して `Sphinx <https://www.sphinx-doc.org/>`__ で構築されています。
```

### Block 18 (line 54)

```
Sphinx はドキュメント生成ツールです。
Sphinx は reStructuredText ファイルを HTML ウェブページに変換します。
Read the Docs はドキュメントホスティングプラットフォームであり、FTC Docs のベース Sphinx テーマを提供しています。
```

### Block 19 (line 58)

```
`ダークテーマ <https://github.com/FIRST-Tech-Challenge/ftcdocs-helper/tree/main/sphinx_rtd_dark_mode_v2>`__ は FTC Docs 開発チームによって提供されています。
```

### Block 20 (line 61)

```
   ここでは、ターゲットとする HTML、XML、CSS のバージョンを宣言することもできます。おそらく、ターゲットとするブラウザも含めます。
   (X)HTML、CSS、またはユーザビリティ標準への準拠情報と、ウェブサイト検証テストへのリンク。これは以前は重要でしたが、今はそれほどではありません。
   いつの日か WCAG に準拠することを目指しています。
```


## contrib/index.rst

### Block 1 (line 1)

```
FTC ドキュメントへの貢献
```

### Block 2 (line 13)

```
ミッションステートメント
```

### Block 3 (line 18)

```
- :doc:`貢献ガイドライン <guidelines/guidelines>`
- :doc:`スタイルガイド <style_guide/style-guide>`
- :doc:`FTC ドキュメントワークフロー <workflow/workflow>`
- :doc:`チュートリアル <tutorials/index>`
```

### Block 4 (line 26)

```
FTC ドキュメントは以下の方々によって提供されています：
```

### Block 5 (line 28)

```
- Daniel Alfredo Diaz, Jr — メンテナー
- Elizabeth Gilibert — プロジェクトマネージャー
- Uday Vidyadharan, 7350 Watt's NXT? — メンテナー
- Chris Johannesen, Westside Robotics — コントリビューター
- Mike Silversides, BC FTA — コントリビューター
- Miriam Sinton-Remes, 7182 Mechanical Paradox — コントリビューター
```

### Block 6 (line 35)

```
このプロジェクトに貢献してくださったすべての方に特別な感謝を申し上げます。
```


## contrib/style_guide/image-and-figure-details.rst

### Block 1 (line 1)

```
画像と図の詳細
```

### Block 2 (line 4)

```
このセクションには、画像と図に関する詳細情報と、FTC Docs での処理方法に関する詳細なアドバイスが含まれています。
```

### Block 3 (line 16)

```
コンテンツのブロックを区切るために使用される波線画像は、装飾的な画像です。
契約交渉に関するページに握手をしている人の写真が、見栄えを良くするために配置されている場合、それは装飾的である可能性があります。
画像がコンテンツに直接関連しておらず、視覚的な魅力のためだけに存在する場合、それは装飾的な画像です。
```

### Block 4 (line 21)

```
   これはマーケティングウェブサイトやビジュアルデザインウェブサイトではありません。
```

### Block 5 (line 23)

```
装飾的な画像はアクセシビリティの問題でもあります。スクリーンリーダーはそれらを処理する必要があります。
画像に代替テキストがある場合、それはコンテンツに関連していない可能性があるため、混乱を引き起こす可能性があります。
```

### Block 6 (line 26)

```
装飾的な画像が本当に必要な場合は、``.. image`` ディレクティブを使用し、**:alt:** オプションに空白のテキストを含めます。
空白の代替テキストにより、スクリーンリーダーは画像を無視します。これは、画像が視覚的なプレゼンテーションのためだけに存在する場合に適切です。
```

### Block 7 (line 39)

```
``.. image`` ディレクティブを使用して、キャプションが **不要な** 画像を含めます。
画像にキャプションが必要かどうかを判断します。写真のクレジットにはキャプションが必要です。複雑な画像にはおそらくキャプションが必要です。
画像をページのコンテンツに結び付けるために編集的または説明的な説明が必要なものはすべて、キャプションが必要です。
```

### Block 8 (line 43)

```
キャプションが不要な場合は、image ディレクティブを使用できます。
``:alt:`` オプションを追加し、画像を説明するテキストを提供します。
これは、基本的な画像に必要なすべてです。
```

### Block 9 (line 52)

```
代替テキストには機能的な説明が必要です。機能的な説明は、画像の中に正確に何があるかを説明します。
これらの説明は徹底的である必要がありますが、簡潔で、1 文または 2 文です。
長い説明が必要な場合は、`figure directive`_ を使用して、長い説明を提供します。
```

### Block 10 (line 59)

```
   HTML は ``<img alt="../_images/GoodStuff.png" src="../_images/GoodStuff.png">`` のようになります。
   スクリーンリーダーは代替テキスト **../_images/GoodStuff.png** を読み上げます。
```

### Block 11 (line 62)

```
   これは良好なアクセシビリティではありません。``:alt:`` オプションのない画像または図のディレクティブを含む既存のページを編集している場合は、
   画像の機能的な説明を含む ``:alt:`` オプションを追加することを検討してください。
```

### Block 12 (line 65)

```
image ディレクティブには多くのオプションがありますが、FTC Docs ではそのほとんどを推奨していません。
これは新しいガイダンスであり、多くの既存のページでは **width** と**align** が指定されています。
とにかくそのページのコンテンツを変更している場合は、それらを削除する価値があるかもしれません。
```

### Block 13 (line 105)

```
画像に関連する新しいガイダンスは、ウェブサイトのアクセシビリティを向上させることから来ています。
以下のオプションを避けることをお勧めします。
```

### Block 14 (line 110)

```
   アクセシビリティの問題は、画像がテキストが周囲に再配置される新しい位置に浮動できるために発生します。
   これにより、画像が周囲のテキストとのコンテキストから浮いてしまう可能性があります。画像は近くのテキストに関連しているべきであるため、これは大きなアクセシビリティの問題です。
   PDF バージョンでは、画像が次のページに浮動することがあり、空白のページに画像だけが単独で存在することがあります。
```

### Block 15 (line 115)

```
   Width は通常、画像がページの幅いっぱいにならないようにするために使用され、通常、HTML と PDF で問題なく見えます。
   ただし、モバイルブラウザで表示すると、画像が小さすぎて簡単に見ることができない場合があります。
   たとえば、50% の幅は大きな画面で表示すると問題なく見えますが、モバイルブラウザのポートレートモードでは、画像は画面の幅の半分になります。
   ただし、モバイルでは、通常、2 本の指を使用して画像をズームできます（指に身体的な障害がない限り）。
```

### Block 16 (line 120)

```
   これらのオプションのより大きなアクセシビリティの問題は、**Sphinx** が画像へのリンクを挿入することです。
```


## contrib/tutorials/create_codespace/create-codespace.rst

### Block 1 (line 1)

```
Codespace の作成
```

### Block 2 (line 5)

```
リポジトリで作成する新しいブランチごとに、新しい Codespace を作成する必要があります。
これは、メインブランチにマージする前にコードを実行してテストできる仮想環境です。
Codespace の作成には数分かかる場合がありますが、一度作成されると、ブラウザからアクセスでき、その後のアクセスははるかに高速になります。
```

### Block 3 (line 12)

```
1. **GitHub** であなたの** フォークした** リポジトリを開きます。
2. ページの左側で、作業したいブランチを選択します。
```

### Block 4 (line 18)

```
3. 緑色の **Code** ボタンをクリックすると、**Local** と**Codespaces** タブが表示されるので、**Codespaces** タブをクリックします。
```

### Block 5 (line 23)

```
4. 「Create codespace on」と書かれた緑色のボタンをクリックします。
```

### Block 6 (line 28)

```
5. Codespace が作成されるまで待ちます。これには数分かかる場合があります。
6. Codespace が作成されると、ブラウザで Codespace に移動します。
   これはブラウザベースの **VS Code** のバージョンで、変更を行い、HTML ページをビルドして変更を確認するために使用できます。
7. ``CTRL + SHIFT + B`` を入力してプロジェクトをビルドします。**Terminal** メニューからビルドタスクを実行することもできます。
```

### Block 7 (line 36)

```
8. ビルドメッセージが表示されます。「build succeeded」メッセージを確認してください。
   その後、アプリケーションが実行中であることを示すポップアップが表示されます。
```

### Block 8 (line 42)

```
9. **Open in Browser** ボタンをクリックすると、ビルドしたばかりの HTML ページを表示する新しいタブが開きます。
```

### Block 9 (line 44)

```
10. これで変更を加えることができます。:doc:`/contrib/tutorials/make_rst/index` のセクションを参照してください。
```


## contrib/tutorials/index.rst

### Block 1 (line 1)

```
チュートリアル
```

### Block 2 (line 4)

```
これらは、FTC Docs での作成と編集のプロセスを順を追って説明するいくつかのチュートリアルです。
```

### Block 3 (line 25)

```
チュートリアル
```


## contrib/tutorials/overview/overview.rst

### Block 1 (line 1)

```
概要
```

### Block 2 (line 4)

```
以下は、FTC Docs への貢献プロセスの概要です。
```

### Block 3 (line 29)

```
2. :doc:`**Codespaces** 入門 <../codespaces/codespaces>` :bdg-secondary:`情報`
```

### Block 4 (line 31)

```
    * これは **Codespaces** の概要と使用方法を提供します。
3. :doc:`**GitHub** リポジトリを知る <../github_repo/github-repo>` :bdg-secondary:`情報`
```

### Block 5 (line 34)

```
    * これは FTC Docs リポジトリの概要と構成方法を提供します。貢献作業を開始する前に理解することが重要です。
```

### Block 6 (line 36)

```
4. :doc:`リポジトリをフォークする <../make_fork/make-fork>` :bdg-danger:`1回のみ` :bdg-info:`Codespaces` :bdg-warning:`ローカル`
```

### Block 7 (line 38)

```
    * これにより、あなたの **GitHub** アカウントに FTC Docs リポジトリのコピーが作成されます。
```

### Block 8 (line 40)

```
5. :doc:`リポジトリを更新する <../update_fork/update-fork>` :bdg-success:`繰り返し` :bdg-info:`Codespaces` :bdg-warning:`ローカル`
```

### Block 9 (line 42)

```
    * これにより、フォークが FTC Docs リポジトリの最新の変更で更新されます。新しい貢献作業を開始する前にこれを行うことが重要です。
```

### Block 10 (line 44)

```
6. :doc:`環境をセットアップする <../setup/setup>` :bdg-danger:`1回のみ` :bdg-warning:`ローカル`
```

### Block 11 (line 46)

```
    * これにより、FTC Docs で作業するためのローカル環境がセットアップされます。**Codespaces** ユーザーはこのステップをスキップできます。
```

### Block 12 (line 48)

```
7. :doc:`新しいブランチを作成する <../make_branch/make-branch>` :bdg-success:`繰り返し` :bdg-info:`Codespaces` :bdg-warning:`ローカル`
```

### Block 13 (line 50)

```
    * これにより、変更用の新しいブランチが作成されます。作業する変更ごとに新しいブランチを作成する必要があります。
```

### Block 14 (line 54)

```
    * これにより、変更用の新しい **Codespace** が作成されます。作業する変更/ブランチごとに新しい**Codespace** を作成する必要があります。
```

### Block 15 (line 58)

```
    * これにより、ステップ 7 で作成したブランチに切り替わります。作業する変更ごとに作成したブランチに切り替える必要があります。
```

### Block 16 (line 62)

```
    * これにより、**VS Code** で利用可能な FTC Docs のタスクの概要が提供されます。貢献作業を開始する前に理解することが重要です。
```

### Block 17 (line 68)

```
    * これにより、変更をプッシュできるように **Git** 認証情報がセットアップされます。
```

### Block 18 (line 72)

```
    * 変更をコミットし、FTC Docs リポジトリにプルリクエストを送信します。
```


## contrib/tutorials/switch_branch/switch-branch.rst

### Block 1 (line 1)

```
ブランチの切り替え
```

### Block 2 (line 6)

```
   ローカルでサイトを開発することを選択した場合にのみ、これらの手順を完了してください。
   **GitHub Codespaces** を使用している場合は、このセクションをスキップする必要があります。
```

### Block 3 (line 9)

```
この手順は、作業しているブランチを変更するために必要です。ブランチで作業していて別のブランチに切り替えたい場合は、次のコマンドを使用できます：
```

### Block 4 (line 15)

```
``<branch_name>`` を、切り替えたいブランチの名前に置き換えてください。また、前の手順で作成したブランチの名前と一致していることを確認してください。
```

### Block 5 (line 17)

```
トラブルシューティング
```

### Block 6 (line 25)

```
このエラーは、切り替えようとしているブランチが存在しない場合に発生します。切り替えようとしているブランチを作成していること、タイプミスがないことを確認してください。ただし、
ローカルリポジトリがリモートリポジトリと同期していない場合にも発生する可能性があります。これを修正するには、次のコマンドを実行できます：
```

### Block 7 (line 32)

```
このコマンドは、ローカルリポジトリをリモートリポジトリで更新します。このコマンドを実行した後、ブランチの切り替えを再度試してください。
```

### Block 8 (line 39)

```
このエラーは、作業ディレクトリにコミットされていない変更がある場合に発生します。変更をコミットするか、スタッシュするか、削除することができます。変更をコミットするには、次のコマンドを使用できます：
```

### Block 9 (line 45)

```
このコマンドは、指定したメッセージで変更をコミットします。
```

### Block 10 (line 47)

```
変更をスタッシュするには、次のコマンドを使用できます：
```

### Block 11 (line 53)

```
スタッシュを使用すると、変更をコミットせずに後で保存できます。変更をスタッシュした後、ブランチを切り替えることができます。スタッシュした変更を適用するには、次のコマンドを使用できます：
```

### Block 12 (line 59)

```
変更をコミットする準備ができていないが、ブランチを切り替える必要がある場合は、``git stash`` を使用するのが最適です。
```

### Block 13 (line 61)

```
変更を削除するには、次のコマンドを使用できます：
```


## contrib/workflow/workflow.rst

### Block 1 (line 1)

```
FTC ドキュメントワークフロー
```

### Block 2 (line 4)

```
    このフローチャートは、FTC Docs リポジトリの*メンテナー*向けの参考用です。
    FTC Docs ドキュメントへの貢献のみを希望する方は、
    :doc:`FTC ドキュメントへの貢献 </contrib/tutorials/index>` ドキュメントを参照してください。
```

### Block 3 (line 8)

```
概要
```

### Block 4 (line 11)

```
以下の図は、様々な GitHub リポジトリと、それらとビルド成果物の間のアクションとフローを示しています。
FTC Docs リポジトリへのプルリクエストは、HTML ページと PDF ファイルをビルドする GitHub アクションを実行します。
HTML ページは最終的に ftc-docs.firstinspires.org ウェブサイトに配置され、PDF ファイルは AWS S3 ファイルストレージに配置されます。
```

### Block 5 (line 15)

```
ウェブブラウザーでは、この図をマウスを使用してズームおよびパンできます。
スクロールホイールを使用してズームイン・ズームアウトできます。右クリックしてホールドし、ドラッグしてパンします。
この図はキーボードでアクセスできません。
スクリーンリーダーは、図の様々なノードとアクションを読み上げ、図の Translation セクションから開始します。
```


## control_hard_compon/ds_components/components/components.rst

### Block 1 (line 1)

```
Driver Station コンポーネント
```

### Block 2 (line 4)

```
Android デバイス
```

### Block 3 (line 44)

```
**Driver Station** の中心は、**Driver Station App** を実行する Android デバイスです。
この Android デバイスの要件は、 `REV Driver Hub <https://www.revrobotics.com/rev-31-1596/>`__ の使用、または競技マニュアルに記載されている承認された Android スマートフォンのいずれかによって満たすことができます。
**Driver Station App** を、競技マニュアルで定義されている最小バージョン以上のバージョンに更新することが非常に重要です。
```

### Block 4 (line 48)

```
**USB-OTG** アダプター / ハブ
```

### Block 5 (line 105)

```
使用している Android デバイスが Android スマートフォンの場合、スマートフォンは
電話機の底部に単一の USB-Micro-B ポートのみを提供します。ゲームパッドなどの USB デバイスを
Android スマートフォンで使用するには、USB-OTG アダプターケーブルを使用する必要があります。
このケーブルは、ゲームパッドまたは周辺機器（複数のゲームパッドを使用できるようにする USB ハブなど）用の
USB Type A ポートを提供します。利用可能な場合は、 `REV UltraUSB（REV-31-1592）<https://www.revrobotics.com/UltraUSB-Hub-and-Cables/>`__ のような OTG ケーブルが組み込まれた USB ハブを使用することをお勧めします。
これにより、システムの接続数と障害ポイントが削減されます。
```

### Block 6 (line 112)

```
**REV Driver Hub** を使用する場合、OTG アダプターは必要ありません。
ゲームパッドはデバイスの 3 つの USB-A ポートのいずれかに直接接続できます。
```

### Block 7 (line 115)

```
市販の **USB** バッテリーパック
```

### Block 8 (line 138)

```
市販の USB バッテリーパックは、競技マニュアルに従って特定の状況で使用できる補助電源です。
USB バッテリーパックは、Android デバイスを充電するために使用することが許可されています。
使用中に充電できるのは **REV Driver Hub** のみで、USB-C ポートを介して充電します。
```

### Block 9 (line 250)

```
競技マニュアルでは、競技プレイで許可されているゲームパッドを定義しています。
許可されているタイプのゲームパッドの任意の組み合わせで、最大 2 つのゲームパッドを使用できます。
すべてのゲームパッドは、有線モードでのみ使用する必要があり、いかなる種類のワイヤレスも許可されていません。
一部のゲームパッドの特別な機能（振動、ライト）は、ロボットのドライバーへの通知と信号のために、
チームがプログラムして使用することができます。
```


## control_hard_compon/ds_components/index.rst

### Block 1 (line 2)

```
   :title: Driver Station 概要
   :description: FTC Driver Station のさまざまなコンポーネントの概要
```

### Block 2 (line 6)

```
Driver Station 概要
```

### Block 3 (line 9)

```
これらの画像は、**Driver Station** を作成するために通常使用されるコンポーネントの基本的な接続図を示しています。これらのコンポーネントは、通常 *FIRST* ストアフロント（「制御と通信」キット内）から購入されています。これらの構成はサンプル接続を示しており、これらのコンポーネントを接続する唯一可能な方法を示しているわけではありません。これらの画像は、チームがコンポーネント管理と輸送に使用することが推奨されている `Driver Station Carrier <https://www.thingiverse.com/thing:3386378>`__ の使用を表しているわけでもありません。**OPERATOR CONSOLE** の詳細については、競技マニュアルを参照してください。
```


## control_hard_compon/index.rst

### Block 1 (line 2)

```
   :title: ハードウェアコンポーネント概要
   :description: FTC制御システムに存在するハードウェアコンポーネントの詳細な概要
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, ハードウェアコンポーネント, 制御システム, 概要
```

### Block 2 (line 6)

```
ハードウェアコンポーネント概要
```

### Block 3 (line 9)

```
*FIRST* Tech Challenge 制御システムは、**Driver Station (DS)** と**Robot Controller (RC)** の2つの主要なコンポーネントに分かれています。このセクションでは、ハードウェアコンポーネント、そのさまざまな構成、および接続について簡単に紹介します。
```


## control_hard_compon/rc_components/encoders/encoders.rst

### Block 1 (line 1)

```
エンコーダー（回転カウンター）
```

### Block 2 (line 39)

```
エンコーダーは、軸の周りの回転変位を測定するデバイスです。ほとんどの合法的な **FIRST Tech Challenge** モーターには、
**REV Hub** と互換性のある直交エンコーダーが内蔵されています。また、上に示した**REV Through Bore Encoder** のような
スタンドアロンのインクリメンタルエンコーダーを使用することも可能です。インクリメンタルエンコーダーは、シャフトの部分的な回転ごとに
「ティック」を送出することで機能します。1 回転あたりに出力されるティック数の詳細については、製造元のウェブサイトで確認できます。
アブソリュートエンコーダーは、シャフトの開始位置からの変位と、「ゼロ」位置に対するシャフトの現在の正確な角度を示すことができます。
```

### Block 3 (line 46)

```
追加リソース
```


## control_hard_compon/rc_components/hub/hub.rst

### Block 1 (line 4)

```
**REV Hub** は、*FIRST* Tech Challenge ロボットのコア制御ユニットです。
```

### Block 2 (line 21)

```
**REV Control Hub** は、**REV Expansion Hub** に組み込まれた Android ドーターボードを組み合わせたものです。これは、ロボットのすべてのハードウェアコンポーネントを制御し、実際のロボットソフトウェアを実行できることを意味します。これは、ハードウェアデバイスのみを制御でき、SDK を解釈して実行することができなかった**REV Expansion Hub** とは対照的です。
```

### Block 3 (line 38)

```
**REV Expansion Hub** は、ロボットのすべてのハードウェアコンポーネントを制御するために使用される Hub です。**Expansion Hub** は、モーターを動かす命令を受け取り、実際にモーターに正しい方法で電力を送ります。ただし、いつこれを行うかはわからないため、Android デバイスが必要になります。このデバイスは、USB 経由で接続された従来の Android スマートフォン、または**Control Hub** に組み込まれたデバイスのいずれかです。複数の Hub を使用する場合、これらの Hub は ``RS485`` または USB 経由で接続できます。詳細については、:ref:`こちら <hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>` を参照してください。
```


## control_hard_compon/rc_components/hub/ports/ch-ports.rst

### Block 1 (line 1)

```
Control Hub ポート
```

### Block 2 (line 17)

```
    Control Hub フロントポート
```

### Block 3 (line 21)

```
USB ポート
```

### Block 4 (line 24)

```
Universal Serial Bus（USB）は、多くの種類の電子機器間でデータ交換と電力供給を可能にする業界標準です。**Control Hub** には、以下に説明する4つの USB ポートがあります。
```

### Block 5 (line 26)

```
USB 2.0 と USB 3.0 は、データ交換速度と電力供給に関連する USB 仕様を指します。
```

### Block 6 (line 28)

```
USB Type-A、USB-C、USB Mini-B は、コネクタのタイプを指します。
```

### Block 7 (line 30)

```
- USB Type-A は、より大きな長方形のコネクタです。
- USB-C は、より小さな楕円形のコネクタです。
- USB Mini-B は、面取りされた端を持つより小さな長方形のコネクタです。
```

### Block 8 (line 37)

```
これは、USB 2.0 を実装する メス USB Type-A ポートであり、競技マニュアルで許可されている USB デバイスの接続に使用できます。
```

### Block 9 (line 41)

```
   REV Control Hub には、USB 2.0 ポートに接続されたデバイスに関する `既知の ESD 問題 <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system#esd-mitigation-techniques>`__ があります。USB 2.0 ポートを使用すると、ESD が Control Hub の Wi-Fi チップに影響を与える可能性があります（Driver Hub との Wi-Fi 切断を引き起こします）。カメラなどの USB デバイスは、Control Hub の USB 3.0 ポートに接続してください。
```

### Block 10 (line 46)

```
これは、USB 3.0 を実装する メス USB Type-A ポートであり、主に USB ビデオデバイスクラス（UVC）カメラ（ウェブカメラ）の接続に使用されます。
```

### Block 11 (line 51)

```
**Control Hub** には、USB 2.0 を実装する メス USB-C ポートがあります。これは主に SDK をロードするためにラップトップに接続するために使用されますが、UVC カメラでも使用できます。
```

### Block 12 (line 56)

```
これは、USB 2.0 を実装する メス USB Mini-B ポートです。I/O システムと直接通信するためにのみ使用されます。この場合、デバイスにファームウェアをアップロードする目的のみです。
```

### Block 13 (line 61)

```
**Control Hub** は、完全な Android デバイスであるにもかかわらず、独自のディスプレイを欠いています。**Control Hub** には、デバイスのビデオ出力を提供する HDMI ポートがあります。この HDMI ポートは、外部ディスプレイに接続するために使用できます。
```

### Block 14 (line 66)

```
これは、Micro SD メモリカード用のポートです。通常は使用されません。
```


## control_hard_compon/rc_components/hub/ports/exh-ports.rst

### Block 1 (line 1)

```
Expansion Hub ポート
```

### Block 2 (line 12)

```
USB-B ポート
```

### Block 3 (line 15)

```
Android RC スマートフォンは、USB OTG ケーブルで接続されたこの USB-mini-B ポートを介して **Expansion Hub** を制御します。このポートで、ファームウェアの更新も可能です。
```


## control_hard_compon/rc_components/hub/ports/std-ports.rst

### Block 1 (line 1)

```
バッテリーポート
```

### Block 2 (line 5)

```
   バッテリー充電器をバッテリーポートに直接接続**しないでください** 。これにより、保証が無効になり、Hub が故障します。
```

### Block 3 (line 7)

```
黄色の `XT30 <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/xt-30-power-cable>`__ コネクタは、**REV Hub** とそれに接続されたすべてのデバイスに電力を供給するために使用されます。これらのポートの詳細については、`REV ドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#input-power-specifications>`__ を参照してください。これらのポートの1つは、アースストラップの接続にも使用できます。法的なアースストラップの詳細については、`競技マニュアル <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`__ の電源分配セクションを参照してください。
```

### Block 4 (line 9)

```
XT30 コネクタは脆弱性で知られているため、使用時には十分注意することを強くお勧めします。また、コネクタのピンを定期的に拡張することをお勧めします。REV には、XT30 コネクタのピンの拡張に関する `トラブルシューティング記事 <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting#xt30-pins-are-compressed>`__ があります。このプロセスの詳細については、この `YouTube ビデオ <https://www.youtube.com/watch?v=UYXTiSeVmB0>`__ をご覧ください。このビデオは XT30 の大型版である XT60 コネクタとドローンを取り上げていますが、アドバイスはほぼ同じです。
```

### Block 5 (line 11)

```
モーターポート
```

### Block 6 (line 14)

```
これらの `JST-VH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-vh-motor-power>`__ スタイルコネクタは、モーターに電力を供給するために使用されます。各 Hub にはこれらのポートが 4 つあり、0〜3 の番号が付けられています。ロボットごとに 8 つのモーターを使用できるため、これらの Hub が許可する以上のモーターを制御したい場合があります。その場合、:ref:`追加の Hub<hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>` を使用するか、`REV SPARKmini Motor Controller <https://www.revrobotics.com/rev-31-1230/>`__（REV-31-1230）を使用してより多くのモーターに電力を供給することができます。このポートの詳細については、`REV モーターポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#motor-port-specifications>`__ を参照してください。
```

### Block 7 (line 17)

```
エンコーダーポート
```

### Block 8 (line 20)

```
これらの 4 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`__ スタイルコネクタは、直交エンコーダーに使用されます。各 Hub にはこれらのポートが 4 つあり、隣接するモーターと組み合わせて使用できます。ただし、このポートを使用してスタンドアロンのインクリメンタルエンコーダーに接続することも可能です。4 つ以上のエンコーダーに接続するには、現在、追加の Hub を接続する必要があります。このポートの詳細については、`REV エンコーダーポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#encoder-port-specifications>`__ を参照してください。
```

### Block 9 (line 22)

```
サーボポート
```

### Block 10 (line 25)

```
これらの 0.1 インチヘッダーピンは、サーボに電力を供給し、制御するために使用されます。各 Hub には 6 つのポートがあり、0〜5 の番号が付けられています。コネクタを反転することが可能であるため、このポートに接続するデバイスの極性を一致させるように注意してください。これらのサーボに供給される電力を増やすには、サーボパワーモジュールを使用することができます。承認されたサーボ電源デバイスについては、`競技マニュアル <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`__ のモーター＆アクチュエーターセクションを参照してください。このポートの詳細については、`REV サーボポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#servo-port-specifications>`__ を参照してください。
```

### Block 11 (line 27)

```
+5V 電源ポート
```

### Block 12 (line 30)

```
これらの 0.1 インチヘッダーピンは、さまざまな機器に電力を供給し、制御するために使用されます。各 Hub には 2 つのポートがあります。これらのコネクタは、電源付き USB ハブへの電力供給など、*FIRST* Tech Challenge の限られた範囲のアプリケーションに使用できます。このポートの詳細については、`REV +5V 電源ポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#id-5v-power-port-specifications>`__ および `競技マニュアル <https://ftc-resources.firstinspires.org/file/ftc/game/manual>`__ の電力分配セクションを参照してください。
```

### Block 13 (line 32)

```
アナログポート
```

### Block 14 (line 35)

```
これらの 4 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`__ スタイルコネクタは、アナログ入力に使用されます。各 Hub にはこれらのポートが 4 つあり、0〜3 の番号が付けられています。アナログポートに接続されたデバイスは、2 つの状態のいずれかを交互に切り替えるデジタルではなく、値の範囲を提供します。このポートの詳細については、`REV アナログポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#analog-port-specifications>`__ を参照してください。
```

### Block 15 (line 37)

```
デジタルポート
```

### Block 16 (line 40)

```
これらの 4 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`__ スタイルコネクタは、デジタル入力に使用されます。各 Hub にはこれらのポートが 4 つあり、合計 8 つのチャンネルが `0-7` とラベル付けされています。デジタルポートに接続されたデバイスは、2 つの状態（例：オンとオフ）のいずれかを交互に切り替えます。そのようなデバイスの 1 つがボタンです。各ポートには 2 つのチャンネルがあり、`REV Touch Sensor <https://www.revrobotics.com/rev-31-1425/>`__ などのデバイスは 1 つのチャンネル（N+1）でのみ動作することに注意することが重要です。
```

### Block 17 (line 43)

```
I2C ポート
```

### Block 18 (line 50)

```
これらの 4 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`__ スタイルコネクタは、I2C センサーの接続に使用されます。各ポートは単一の I2C バスであり、複数のセンサーを接続できます。同じバス上で同一のアドレスを持つセンサーを使用すると、問題が発生する可能性があります。広範囲のセンサーを使用することは可能ですが、I2C センサーの大部分には SDK に組み込まれたドライバーがありません。コミュニティドライバーを使用するか、独自のドライバーを作成することができます。このポートの詳細については、`REV I2C ポートのドキュメント <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#i2c-port-specifications>`__ を参照してください。
```

### Block 19 (line 56)

```
これらの 3 ピン `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`__ スタイルコネクタは、REV Hub 間のシリアル通信に使用されます。:ref:`このチュートリアル <hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>` で説明されているように、2 つ目の REV Hub を使用する場合にこのポートを使用します。両方の RS485 ポートを使用して、REV Hub 間の両方のポートを接続する 2 本のケーブルを使用することで、冗長性を追加できます。
```

### Block 20 (line 61)

```
このコネクタは**開発者** （エンドユーザー以外）のデバッグにのみ使用されます。その使用は *FIRST* によってサポートされていません。
```


## control_hard_compon/rc_components/index.rst

### Block 1 (line 2)

```
   :title: FTC Robot Controller 概要, FTC Docs
   :description: FTC Robot Controller のビジュアル概要
```

### Block 2 (line 9)

```
Robot Controller 概要
```

### Block 3 (line 12)

```
これらの画像は、標準的なロボットスターターキットに通常含まれているコンポーネントと、*FIRST* ストアフロントから購入したコンポーネント（REV および Tetrix スターターキットのコンポーネントと、電子機器キットを含む）の基本的な接続図を示しています。これらの構成はサンプル接続を示しており、これらのコンポーネントを接続する唯一可能な方法を示しているわけではありません。両方の図には、標準スターターキットにも電子機器キットにも含まれていない追加のオプションの **REV Expansion Hub** が含まれています。これは、追加のオプションの**REV Expansion Hub** が利用可能で必要な場合に、それを接続する方法のサンプルとして図に含まれています。
```

### Block 4 (line 14)

```
以下のヘッダーをクリックして、異なる制御システム構成図を切り替えます。
```


## control_hard_compon/rc_components/motors/motors.rst

### Block 1 (line 1)

```
モーター
```

### Block 2 (line 92)

```
モーターはロボットの主要な駆動装置です。すべてのモーターは 12V ブラシ付き DC モーターであり、
競技マニュアルに記載されています。これらは、**REV Expansion Hub**、**REV Control Hub**、または**REV SPARKmini Motor Controller**
を介してのみ制御できます。
```

### Block 3 (line 96)

```
追加リソース
```


## control_hard_compon/rc_components/power_distr/power-distr.rst

### Block 1 (line 1)

```
電源分配
```

### Block 2 (line 4)

```
ロボットメインバッテリー
```

### Block 3 (line 61)

```
ロボットの主電源は 1 つの 12V バッテリーから供給されます。上記のバッテリーは
これらのバッテリーのサンプルです。バッテリーの完全なリストについては、競技マニュアルを確認してください。
バッテリーのインラインヒューズが保持されている限り、通常、バッテリーのコネクタを交換することが許可されていることに注意してください。
詳細については、競技マニュアルを再度確認してください。
```

### Block 4 (line 67)

```
   工場出荷時のデフォルトのバッテリーコネクタを交換する際には、ワイヤー/コネクタを切断する前に、必ずインラインヒューズホルダーから 20A ヒューズを取り外してください。
```

### Block 5 (line 69)

```
メインパワースイッチ
```

### Block 6 (line 145)

```
1 つのメインパワースイッチが、メインバッテリーによって供給されるすべての電力を制御する必要があります。
上記の合法的な電源スイッチは代表的な例です。完全なリストについては、競技マニュアルを確認してください。
```

### Block 7 (line 148)

```
電力配分ブロック
```

### Block 8 (line 189)

```
電力分配ブロックは、**Control Hub** 、SPARKmini などのデバイスに電力を分配するのに役立ちます。
合法的な電力分配方法の説明については、競技マニュアルを参照してください。
示されている電力分配ブロックは、電力分配用の唯一の合法的なデバイスではありません。
```

### Block 9 (line 216)

```
これは、3 線式サーボに供給される電力を増強する電子デバイスです（サーボパワーインジェクターとも呼ばれます）。
**REV Servo Power Module** には、6 つの入力サーボポートと 6 つの対応する出力ポートがあります。
12V 電源から電力を取得し、各出力サーボポートに 6V の電力を提供します。**REV Servo Power Module** は、
すべての出力サーボポートに最大 15A の電流を供給でき、モジュールあたり合計 90 ワットの電力を提供できます。
競技マニュアルでは、より多くのサーボパワーインジェクターが許可されています。
```

### Block 10 (line 222)

```
市販の **USB** バッテリーパック
```

### Block 11 (line 245)

```
市販品（COTS）USB バッテリーパックは、競技マニュアルに従って特定の状況で使用できる補助電源です。
2023-2024 シーズンでは、これらのバッテリーは LED に電力を供給することが許可され、
拡張として `REV Blinkin <https://www.revrobotics.com/rev-11-1105/>`__ のような COTS ライトコントローラーソースにも許可されました。
ただし、ロボットに COTS USB 外部バッテリーを搭載すると、追加の考慮事項が発生します。
すべてのチームは、COTS USB バッテリーパックが以下を満たしていることを確認する必要があります：
```

### Block 12 (line 251)

```
- 信頼できるブランドによって製造されていること。
- 許可されたワット時容量制限内であること。
- 標準的な安全機能が含まれていること。
- ロボットに固定されていること。
- 未使用のポートがカバーされていること。
- 常に適切に充電されていること。
- 損傷の兆候がないこと。
- ロボットの電源に接続されていないこと。
```

### Block 13 (line 260)

```
以下のセクションは、上記のリストを明確にすることを目的としています。
```

### Block 14 (line 262)

```
信頼できるブランド
```

### Block 15 (line 265)

```
COTS USB バッテリーパックの安全性に関して最も重要な要素は、
バッテリーパックが信頼できるブランドによって製造されていることを確認することです。
COTS USB バッテリーパックの国際的なテストにより、ブランドのないバッテリー、
またはあまり知られていない会社によって製造されたバッテリーは、
信頼できるブランドのバッテリーよりも故障する傾向があることが結論付けられています。
どのブランドが信頼できて、どのブランドがそうでないかをどのように知ることができますか？
それは常に簡単なことではありませんが、
```

### Block 16 (line 276)

```
などのブランドは、世界で最も使用されているブランドの 1 つです。
**FIRST Tech Challenge** は、あまり知られていないブランドよりも高価であっても、
国際的に信頼できるブランドを選択することをお勧めします。
これらのバッテリーは、安全性とパフォーマンスのガイドラインに従う可能性が高いためです。
価格だけで COTS USB バッテリー
```

### Block 17 (line 306)

```
信頼できる COTS USB バッテリーパックブランドを使用する主な利点は、
バッテリーパックに標準的な安全機能が含まれていることが保証されることです。これには以下が含まれますが、
これらに限定されません：
```

### Block 18 (line 310)

```
- 逆極性保護
- 短絡保護
- 過充電保護
- 過温度または過熱保護
- 過電流保護
```

### Block 19 (line 316)

```
バッテリーパックにこれらの安全機能が含まれているかどうかを誠実に判断する必要があります。
パックに付属のドキュメント内に、パックが提供する保護機能がリストされていることがよくあります。
バッテリーパックには、故障時に爆発または発火することが多いリチウムイオンまたはリチウムポリマーバッテリーが
含まれている可能性があることを忘れないでください。これらの保護機能は、バッテリーが早期に故障しないようにするために
不可欠です。これらの保護機能のない COTS USB バッテリーパックの使用は推奨されません。
```

### Block 20 (line 325)

```
バッテリー故障の主な原因は、バッテリーへの物理的な損傷です。COTS USB バッテリーパックの場合、
これは通常、バッテリーパックを落とすこと、バッテリーパックに過度の力を加えること、
パックを過度の衝撃にさらすこと（内部コンポーネントも損傷する可能性があります）に起因します。
損傷を防ぐために、バッテリーパックはロボット内に適切に固定する必要があります。
バッテリーを固定するためのヒントは次のとおりです：
```

### Block 21 (line 331)

```
- バッテリーを固定するために、フックアンドループまたは 3M DualLock ファスナーを使用する、**または**
- バッテリーを（冷却のために）空気にさらすことができるロボット内のぴったりフィットまたはカスタムフィットの
  エンクロージャーに保管する、**そして**
- 他のロボット、ゲームピース、またはロボットの周囲に侵入する可能性のあるフィールド要素からの
  接触からバッテリーを保護する。
```

### Block 22 (line 337)

```
COTS USB バッテリーパックを使用する場合、バッテリーが固定され、保護され、換気されていることを
確認することが最も重要です。すべてのバッテリー（メインバッテリーと COTS USB バッテリーパックの両方）は、
簡単にアクセスでき、緊急時にロボットから迅速に取り外すことができる必要があります。
```

### Block 23 (line 344)

```
一部の COTS USB バッテリーパックには複数のポートが含まれており、ロボットにしっかりと取り付けられている間、
すべてのポートが使用されているわけではないことがよくあります。たとえば、COTS USB バッテリーパックには、
複数の USB ポート、専用の充電ポート、およびその他の必要なポートがある場合があります。
使用されていないポート（USB コネクタが挿入されていないポート）は、短絡の大きなリスクがあります。
短絡の最も一般的な理由は、ポートに入る可能性のある金属片、特に金属がこすれ合うことによるスワーフ、
ギアの摩耗、または電子機器が存在する状態でのロボットメンテナンスです。使用されていないポートは、
電気テープ、Gaffers テープ、またはポートへの破片の侵入を防ぐその他の手段を使用してカバーする必要があります。
短絡は、過度の熱、火災、または爆発のリスクをもたらす可能性があり、それらを防ぐためにすべての合理的な努力を
払う必要があります。
```

### Block 24 (line 355)

```
   COTS USB バッテリーパックを濡らさないでください。濡れた場合は、
   使用を続ける前に、製造元の推奨手順に従ってバッテリーを清掃して乾燥させてください。
```

### Block 25 (line 361)

```
COTS USB バッテリーパックに付属のオーナーズマニュアル/取扱説明書には、
適切な充電を含む、バッテリーパックの適切なケアとメンテナンスの手順が記載されていることがよくあります。
常に製造元の推奨事項に従ってください。さらに、バッテリーの充電に関する一般的なベストプラクティスは次のとおりです：
```

### Block 26 (line 365)

```
- ベッドやバッグの中など、熱がこもる場所でパワーバンクを充電しないでください。
- ソーラーパワーバンクでない限り、バッテリーを太陽の下に放置しないでください！
- COTS USB バッテリーパックを完全に充電するために必要な時間に関する製造元のガイドラインに従ってください。
- COTS USB バッテリーパックを長時間充電したままにしておくと、過熱する可能性があるため、
  避けてください。
- COTS USB バッテリーパックが充電中または放電中に過度に熱くなった場合は、
  電源または電源供給デバイスからすぐにプラグを抜き、バッテリーで他の操作を行う前に冷却してください。
```

### Block 27 (line 376)

```
ほとんどの COTS USB バッテリーパックは、内部のバッテリーセルを保護してパッケージ化するために、
硬質プラスチックシェル内に収容されています。したがって、バッテリーが故障と損傷の兆候を示しているかどうかを
判断するのは難しい場合があります。故障しているバッテリーを識別するためのいくつかのヒントを次に示します：
```

### Block 28 (line 380)

```
- 電源セルの漏れを確認します。アルカリ電池の酸漏れと同様に、バッテリーパックから腐食または酸漏れの
  兆候があるかどうかを確認します。これは判断が難しい場合があるため、注意してください。酸または腐食の兆候が
  ある場合は、製造元の推奨事項に従って、すぐにバッテリーを極度の偏見を持って廃棄してください。
- バッテリーケーシング内の膨張を探します。リチウムバッテリーが故障すると、多くの場合、
  風船のように膨張し始めます。バッテリーのケースが内部からの圧力の兆候を示している場合は、
  製造元の推奨事項に従って、すぐにバッテリーを極度の偏見を持って廃棄してください。
- バッテリーパックに機能しないポートがないかテストします。機能しないポートは、
  内部損傷の初期の兆候である場合があります。損傷していると疑われるバッテリーは使用しないでください。
  製造元の推奨事項に従って、すぐにバッテリーを廃棄してください。
```

### Block 29 (line 393)

```
COTS USB バッテリーパックを、ロボットが使用するメイン（または任意の）電源システムに
接続しないように細心の注意を払う必要があります。COTS USB バッテリーパックと接続されたデバイスは、
競技マニュアルで提供される制御信号を除いて、ロボット電気システムから完全に分離する必要があります。
COTS USB バッテリーパックを使用する場合、パックによって電力を供給される LED の制御信号は、
許可された互換性のあるデバイスにのみ接続する必要があります。
```


## control_hard_compon/rc_components/sensors/sensors.rst

### Block 1 (line 1)

```
センサー
```

### Block 2 (line 4)

```
以下に、一般的なロボットセンサーの例をいくつか示します。*FIRST* Tech Challenge SDK は多くのセンサーをサポートしていますが、すべてがネイティブにサポートされているわけではありません。
```

### Block 3 (line 6)

```
例
```

### Block 4 (line 33)

```
超音波距離センサーは、物体とセンサー間の距離を測定できるデバイスです。
これは、音波を送出し、波が物体まで移動して戻ってくるまでの時間を測定することで行います。
これと音速を使用して、距離を計算できます。
```

### Block 5 (line 60)

```
光学式飛行時間（ToF）センサーは、物体とセンサー間の距離を測定できるデバイスです。
これは、光ビームを送出し、ビームが物体まで移動して戻ってくるまでの時間を測定することで行います。
この時間と既知の光速を使用して、距離を計算できます。
問題の物体が光とどのように相互作用するかによって、距離測定の精度が変わる可能性があることに注意してください。
フィールドパネルのような透明な物体は、しばしば不正確な測定を提供します。
```

### Block 6 (line 106)

```
カラーセンサーは、通常、物体の色を測定できるデジタル出力デバイスです。
ほとんどのカラーセンサーは、問題の物体がセンサーに比較的近い位置にあることを必要とします。
```

### Block 7 (line 132)

```
タッチセンサーは、ボタンのアクティベーションを検出するデジタル出力デバイスです。
これは、メカニズムの動作範囲を制限する方法であるリミットスイッチとして使用できます。
このようなデバイスは、通常、デジタルポートを使用します。
```

### Block 8 (line 160)

```
磁気リミットスイッチは、近接した位置にある磁石の存在を検出するために使用されます。
これは、指定された制限を超えると損傷を引き起こすメカニズムの移動範囲を制限するために一般的に使用されます。
これは、リミットスイッチをアクティブにする磁石を該当するメカニズムに配置することで行われます。
デジタルデバイスとして、これはブール値の出力のみを送信し、範囲は送信しないことに注意することが重要です。
磁場の強度を測定するには、磁力計を参照してください。
```

### Block 9 (line 207)

```
慣性測定ユニット（**IMU** ）は、ジャイロスコープ、加速度計、磁力計を組み合わせたセンサーです。
ジャイロスコープは、物体の 3 次元での `角度方向 <https://en.wikipedia.org/wiki/Orientation_(geometry)>`__ を報告するデバイスです。
加速度計は、物体の 3 次元での加速度を報告するデバイスです。加速度は、任意の瞬間における速度の変化率と考えることができます。
磁力計は、3 軸での磁場の強度を測定するデバイスです。これは、地球の極に対するロボットの方向を得るためのコンパスとして使用でき、
絶対的な測定値となります。
```

### Block 10 (line 253)

```
ポテンショメーターは、アジャスターが回転する程度に基づいて出力電圧を変更するデバイスです。
これは、車軸の絶対的な方向を測定する形式としてよく使用されます。出力電圧が変化する方法は、
使用されるポテンショメーターに基づいています。
このようなデバイスは、通常、**REV Hub** のアナログポートを介して接続されます。
```

### Block 11 (line 259)

```
センサー互換性チャート
```

### Block 12 (line 262)

```
センサー互換性に関するこの便利なチャートを提供してくれた **REV Robotics** の方々に感謝します。
```

### Block 13 (line 384)

```
追加リソース
```


## control_hard_compon/rc_components/servos/servos.rst

### Block 1 (line 1)

```
サーボ
```

### Block 2 (line 58)

```
サーボは、パルス幅変調（PWM）信号を入力として受け取り、組み込みコントローラーの助けを借りて、
入力信号に基づいて直線運動または回転運動を生成するタイプのデバイスです。サーボは、**REV Hub** （**Control Hub** または**Expansion Hub** ）
によって生成された入力信号を受け取ることができ、これ自体が 5V の電力と限られた電流を提供します（詳細については REV のドキュメントを参照してください）。
**REV Servo Power Module** （SPM）を使用して、サーボに供給される電力を、デバイスあたり最大 6 つのサーボに対して 6V で最大 90W まで増強することができます。
**FIRST Tech Challenge** のロボットは、合計最大 12 個のサーボを使用できます。
```

### Block 3 (line 64)

```
追加リソース
```


## control_hard_compon/rc_components/uvc/uvc.rst

### Block 1 (line 1)

```
UVC ウェブカメラ
```

### Block 2 (line 4)

```
ウェブカメラは、周囲の環境の視覚画像を提供するデバイスです。UVC（USB Video Class）は、ウェブカメラやデジタルカメラなどの USB デバイスが、特別なドライバーを必要とせずにビデオをコンピューターにストリーミングできるようにする標準です。*FIRST* Tech Challenge の一部として使用する場合、チームは市販の USB Video Class `(UVC) <https://www.usb.org/document-library/video-class-v15-document-set>`__ 互換カメラを使用する必要があります。このデバイスは、**REV Control Hub** に直接接続するか、USB ハブを介してロボット制御システムに接続できます。
```

### Block 3 (line 45)

```
ウェブカメラは、コンピュータービジョン関連のタスクで使用することを目的としています。
ウェブカメラの使用例には、以下が含まれます：
```

### Block 4 (line 48)

```
- **AprilTag** の :doc:`検出 <../../../apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values>`
- フィールド上でロボットが :doc:`どこにいるか <../../../apriltag/vision_portal/apriltag_localization/apriltag-localization>` の特定
- **OpenCV** を使用したゲーム要素の :doc:`色や形状の検出 <../../../color_processing/index>`
```

### Block 5 (line 52)

```
追加リソース
```

### Block 6 (line 55)

```
- **VisionPortal** と互換性があることが知られている :doc:`ウェブカメラのリスト <../../../apriltag/vision_portal/visionportal_webcams/visionportal-webcams>`
```


## devices/huskylens/huskylens.rst

### Block 1 (line 2)

```
*FIRST* Tech Challenge向け **HuskyLens** 入門
```

### Block 2 (line 5)

```
はじめに
```

### Block 3 (line 8)

```
このチュートリアルは、*FIRST* Tech Challenge で
`HuskyLens <https://www.dfrobot.com/product-1922.html>`__ を活用する方法を、すでにその可能性を探求することを決めたチームの皆さん向けにご紹介します。
```

### Block 4 (line 18)

```
この**ビジョンセンサー** の基本的なサポートは、2023年9月の CENTERSTAGE ロボットゲーム開始時に**FTC SDK** バージョン9.0 で追加されました。
```

### Block 5 (line 20)

```
**HuskyLens** は、** オンボードプログラミング** によって AI 支援の学習、画像処理、認識を行います。**REV Control Hub** または**REV Expansion Hub** の**I2C センサーポート** に接続します。
```

### Block 6 (line 22)

```
**HuskyLens** は**USB ウェブカメラ** ではなく、FTC の
```

### Block 7 (line 24)

```
ソフトウェアも使用しません。
```

### Block 8 (line 27)

```
電気的な接続
```

### Block 9 (line 30)

```
**HuskyLens** を**REV Control Hub** または**Expansion Hub** の I2C ポートに接続するには、** カスタムアダプターケーブル** が必要です。**HuskyLens** コネクタの4本のワイヤ／ピンは、REV Hub の4ピンと順番や位置が異なります。
```

### Block 10 (line 32)

```
3本のワイヤは、REV センサーケーブルのワイヤと**同じ色** です。カスタムケーブルでは、**赤は赤** 、**黒は黒** 、**青は青** で接続してください。残る**HuskyLens** の** 緑色のワイヤ** は、REV の** 白色のワイヤ** に接続します。とてもシンプルです！
```

### Block 11 (line 34)

```
このチュートリアルでは、
```

### Block 12 (line 36)

```
- 既存ケーブルのピン順変更、または
- 新規ケーブルの製作方法（はんだ付け、圧着コネクタ、レバーナットなど）
```

### Block 13 (line 39)

```
については扱いません。
```

### Block 14 (line 42)

```
**FTC 競技マニュアル** ではこの作業が認められていますが、チームは競技シーズンを通じて高品質なケーブルを確保してください。
```

### Block 15 (line 52)

```
配線方法が正しいか確認したい場合は、
`HuskyLens 公式ドキュメント <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336#target_3>`__
や `REV Hub 公式ドキュメント <https://docs.revrobotics.com/duo-control/sensors/i2c#wiring>`__
を参照してください。以下の「ピン配置」情報が得られます：
```

### Block 16 (line 57)

```
- HuskyLens **緑** ワイヤ 1（「T」）SDA（データ） == REV Hub**白** ワイヤ 3「SDA」（データ）
- HuskyLens **青** ワイヤ 2（「R」）SCL（クロック） == REV Hub**青** ワイヤ 4「SCL」（クロック）
- HuskyLens **黒** ワイヤ 3（「-」）GND（グラウンド） == REV Hub**黒** ワイヤ 1「GND」（グラウンド）
- HuskyLens **赤** ワイヤ 4（「+」）VCC（+3.3-5VDC） == REV Hub**赤** ワイヤ 2「3.3V」（Vcc）
```

### Block 17 (line 70)

```
構成方法
```

### Block 18 (line 73)

```
新しいアダプターケーブルを使い、**HuskyLens** を**REV Hub** の I2C ポートに接続します。I2C 接続は**Bus 1, 2, 3** のいずれかを推奨します（データトラフィックの過負荷を避けるため）。
```

### Block 19 (line 75)

```
ラベル「0」は I2C Bus 0 で、通常は Port 0 に**内蔵 IMU** が接続されています。I2C Bus には複数の I2C ポートがあり、トラフィックを共有します。
```

### Block 20 (line 77)

```
**Driver Station** で、三点メニューから ``Configure Robot`` を選択します。
```

### Block 21 (line 79)

```
既存の（正しい）構成を編集するか、``New`` をタップします。``Scan`` をタップし、Portal レベルを経由して **HuskyLens** が接続された``Expansion Hub`` または``Control Hub`` を選択します。
```

### Block 22 (line 81)

```
**HuskyLens** が接続されている Bus 番号（例：``I2C Bus 3`` ）を選択します。
```

### Block 23 (line 91)

```
``Add`` をタップし、Port 0（または最初の空きポート）のドロップダウンリストから「HuskyLens」を選択します。デバイス名は「huskylens」と入力してください（サンプル **OpMode** で期待される名前です）。
```

### Block 24 (line 93)

```
``Done`` を数回タップし、``Save`` で構成を保存・名前変更します。DS の「Back」矢印でホーム画面に戻ります。
```

### Block 25 (line 95)

```
新しい構成が画面上でアクティブ構成として表示されていることを確認してください。
```

### Block 26 (line 98)

```
サンプル **OpMode**
```

### Block 27 (line 101)

```
プログラミング用コンピューターを **Robot Controller** に接続し、プログラミングソフトウェアを開きます。このチュートリアルでは**FTC Blocks** を使用します。
```

### Block 28 (line 104)

```
   **OnBot Java** や**Android Studio** ユーザーも同じロジックで簡単に追従できます（Java サンプル**OpMode** はコメントも充実しています）。
```

### Block 29 (line 106)

```
**FTC Blocks** で、「SensorHuskyLens」というサンプルを使って新しい**OpMode** を作成します。
```

### Block 30 (line 115)

```
このサンプルでは、**OpMode** のタイプを ``TeleOp`` から``Autonomous`` に変更してください（ゲームパッドは使用しません）。
```

### Block 31 (line 126)

```
デフォルトのアルゴリズムは ``TAG_RECOGNITION`` で、センサーの視野内にある（一般的な）**AprilTag** を検出します。この認識は FTC ゲーム CENTERSTAGE の10個の**AprilTag** （メタデータ付き）とは関係ありません。ここでは、**HuskyLens** の動作確認のためのシンプルな内蔵機能です。
```

### Block 32 (line 128)

```
**AprilTag** の認識やナビゲーションには、UVC ウェブカメラと FTC の
```

### Block 33 (line 130)

```
ソフトウェアの方が有用な場合があります。FTC ロボットは **HuskyLens** と USB ウェブカメラの両方を使うことができます。
```

### Block 34 (line 132)

```
``Save OpMode`` をクリックし、Driver Station からこの **OpMode** を選択して実行します。Start 矢印をタップしたら、**HuskyLens** を一般的な 36h11 ファミリーの**AprilTag** に向けてください。
```

### Block 35 (line 143)

```
**HuskyLens** の小さな画面には、認識した**AprilTag** が細い白いバウンディングボックスで囲まれて表示されます。
```

### Block 36 (line 145)

```
対応する DS テレメトリーは以下の通りです：
```

### Block 37 (line 156)

```
データには以下が含まれます：
```

### Block 38 (line 158)

```
- 検出されたオブジェクト（「ブロック」と呼ばれる）の数
- オブジェクトの ID コード（正確でない場合や意味がない場合もあります）
- バウンディングボックスのサイズ（ピクセル単位）
- バウンディングボックスの中心位置（ピクセル単位、原点は左上）
```

### Block 39 (line 163)

```
**HuskyLens** の画面サイズは 320 x 240 ピクセル、中心は (160, 120) です。
```

### Block 40 (line 165)

```
**おめでとうございます！** これで**HuskyLens** デバイス、REV Hub への接続、サンプル**OpMode** の動作確認ができました。
```

### Block 41 (line 168)

```
**AprilTag** 検出
```

### Block 42 (line 171)

```
次に、**HuskyLens** が CENTERSTAGE の Spike Mark 上の**AprilTag** の位置を検出できるかテストします。これは実際のゲームシナリオではありません（**Team Prop** ＝チームゲームエレメントは**AprilTag** を使えません）。ここでは、ロボットが**HuskyLens** で2～3個の Spike Mark を一度に「見る」ことができるかを検証します。
```

### Block 43 (line 182)

```
この例では、**HuskyLens** をマットから約10インチ離れた、Spike Mark タイル手前のフォームタイル中央付近に配置しました。視野には3つの Spike Mark の中央がすべて含まれています。
```

### Block 44 (line 184)

```
3つの **AprilTag** がすべて認識されました：
```

### Block 45 (line 195)

```
これは、**HuskyLens** が訓練済みオブジェクトを既知の複数位置のいずれかで認識できる可能性を示しています。CENTERSTAGE ゲームの**Autonomous** フェーズで有用です。
```

### Block 46 (line 198)

```
単色の学習
```

### Block 47 (line 201)

```
次は ``COLOR_RECOGNITION`` という別のアルゴリズムを試しますが、その前に **HuskyLens** の内蔵 AI 機能で「単色」を学習させます。
```

### Block 48 (line 204)

```
3～4インチ程度の、完全に一色の物体を用意してください（色は何でも構いません）。ここでは、均一な**赤色** の平らな四角いコースター（LEGO!）を使います。
```

### Block 49 (line 207)

```
検出に使う予定の位置や照明環境でこの物体を配置します。CENTERSTAGE の Spike Mark 上でも構いません。
```

### Block 50 (line 218)

```
上記画像では、学習した色が **``Color:ID1``** として長方形のバウンディングボックスで表示されています。以下の手順で色の学習を行います。
```

### Block 51 (line 221)

```
**HuskyLens** の色学習手順は `公式オンライン <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336#target_19>`__ に掲載されています。そちらを参照するか、同等の説明を本チュートリアルでご確認ください。少し練習が必要かもしれません。
```

### Block 52 (line 224)

```
**HuskyLens** 上部の左側のダイヤルは「**Function ボタン**」（ダイヤル兼ボタン）、右側の小さいボタンは「**Learning ボタン**」です。
```

### Block 53 (line 227)

```
Function ボタンを左右に回し、画面下部に「Color Recognition」が表示されるまで操作します。
```

### Block 54 (line 230)

```
これは公式手順の ``Operation and Setting`` のステップ1です。今はステップ2～4で複数色を学習しようとしないでください。
```

### Block 55 (line 233)

```
**HuskyLens** 画面中央の「+」アイコンを物体の主な色領域に合わせます。白い枠が表示され、主色をターゲットします。枠内にターゲット色だけが入るように狙いましょう。
```

### Block 56 (line 236)

```
これは ``Learning and Detection`` のステップ1です。次はステップ2、色の学習です。
```

### Block 57 (line 239)

```
主色が枠内に入ったら、右側の小さい **Learning ボタン** を** 長押し** します。画面に黄色い枠が表示され、**HuskyLens** が色を学習中であることを示します。長押し中は、色領域を指しながら**HuskyLens** を動かし、様々な距離や角度から色を学習させます。終わったら Learning ボタンを離して学習を完了します。ボタンを再度押さず（プロンプトは無視）、5秒のタイムアウトを待ちます。
```

### Block 58 (line 242)

```
長押し学習は数秒で完了します。Learning ボタンを離した後、タイムアウトで学習終了となります。これで色の学習は完了です！
```

### Block 59 (line 245)

```
上記のように、学習した色は画面上で **``Color:ID1``** として長方形のバウンディングボックスで表示されます。この「ブロック」（色領域）は次のサンプル**OpMode** で報告されます。
```

### Block 60 (line 248)

```
再度学習したい場合は、Learning ボタンを短押し→もう一度短押しで学習済み色を**忘却** します。再び「+」アイコンが表示されるので、中心に合わせて長押しで学習を繰り返し、タイムアウトまで待ちます。
```

### Block 61 (line 251)

```
このセクションでは単色の学習方法を説明しました。チュートリアル完了後、**2色** （例：赤系と青系）を学習する方法も後半で解説します。
```

### Block 62 (line 254)

```
**HuskyLens** 公式ドキュメントでは色領域を「ブロック」と呼びますが、物理的なブロックやキューブとは異なります。認識領域も「ブロック」と呼ばれます。
```

### Block 63 (line 257)

```
公式の注意事項：
```

### Block 64 (line 260)

```
   「色認識は周囲の照明に大きく影響されます。**HuskyLens** は似た色を誤認識する場合があります。できるだけ照明環境を一定に保ってください。」
```

### Block 65 (line 263)

```
単色の検出
```

### Block 66 (line 266)

```
**HuskyLens** を色学習済みの物体に向けます。
```

### Block 67 (line 277)

```
上記のように、**HuskyLens** は色付き物体を**``Color:ID1``** として認識・ラベル付けします（ここでは赤色の物体2つが黄色矢印で示されています）。
```

### Block 68 (line 280)

```
プログラミングソフトウェア（同じ **OpMode** ）で、アルゴリズムを ``COLOR_RECOGNITION`` に変更します：
```

### Block 69 (line 291)

```
Java サンプル **OpMode** では、アルゴリズム選択を以下のように変更します：
```

### Block 70 (line 298)

```
この **OpMode** を保存し、Driver Station で選択・実行します。アクティブ構成に**HuskyLens** が含まれていることを確認してください。
```

### Block 71 (line 309)

```
上記のように、**OpMode** では白いバウンディングボックス（「ブロック」）のサイズと位置が表示されます。これは**FOR ループ** で処理され、複数認識が1つずつ処理されます。
```

### Block 72 (line 312)

```
Java サンプル **OpMode** の**FOR ループ内** では、現在認識されたバウンディングボックスの詳細情報（``blocks[i].width``、``blocks[i].height``、``blocks[i].left``、``blocks[i].top``、中心座標の``blocks[i].x``、``blocks[i].y`` ）を保存・評価できます。色 ID（``blocks[i].id`` ）は単色検出の場合常に1です。これらは Java の``int`` 型です。
```

### Block 73 (line 315)

```
**Team Prop** の色が Spike Mark の赤や青と近い場合でも、空の Spike Mark のバウンディングボックスの形状（アスペクト比）を判定して除外する**OpMode** コードを書くことができます。
```

### Block 74 (line 318)

```
以下は学習済み**青色物体** の例です：
```

### Block 75 (line 329)

```
両方の青色物体が **OpMode** で認識されました：
```

### Block 76 (line 339)

```
同様に、コードでバウンディングボックスのサイズや位置を評価し、物体の「本物の」認識かどうかを判定できます。
```

### Block 77 (line 342)

```
競技に関する注意事項
```

### Block 78 (line 348)

```
実際の **Team Prop** （チームゲームエレメント）の色認識実験が可能です。**Competition Manual** や `FTC Q&A <https://ftc-qa.firstinspires.org/>`__ で**Team Prop** の要件を確認し、「赤」「青」の色合いを選び、上記と同じ手順で学習・認識を行ってください。
```

### Block 79 (line 351)

```
2. 色
```

### Block 80 (line 354)

```
上記の学習済み**青色物体** は Spike Mark の青とは異なる色合いです。この違いにより、物体色の明確かつ正確な認識の可能性が高まります。
```

### Block 81 (line 356)

```
このゲームでは、**Competition Manual** で**Team Prop** の色が Spike Mark の公式テープ色と異なる赤・青でも認められています。
```

### Block 82 (line 359)

```
3. 照明
```

### Block 83 (line 362)

```
**HuskyLens** 公式ドキュメント（上記参照）では、周囲の照明が学習済み色の認識に影響する旨の注意があります。
```

### Block 84 (line 364)

```
そのため、競技用の学習は、**Team Prop** を Spike Mark 上に置き、**HuskyLens** を試合開始予定位置（ロボット上）に設置して行うのが理想です。
```

### Block 85 (line 366)

```
また、学習時の照明環境は試合本番に近いものにしてください。大会や試合準備の一環として最終色学習を行うのも良いでしょう。慣れれば数秒で完了します。
```

### Block 86 (line 369)

```
4. プログラミング
```

### Block 87 (line 372)

```
このサンプル **OpMode** では、メインループは DS の Stop ボタンを押すまで終了しません。競技用には、少なくとも以下2点で** コードを修正** してください：
```

### Block 88 (line 374)

```
- 重要な認識があった場合、FOR ループ内でアクションを起こすか重要情報を保存する
- 独自の基準でメインループを終了し、**OpMode** を継続する
```

### Block 89 (line 377)

```
例として、重要な認識があれば Boolean 変数 ``isPropDetected`` を``true`` に設定するなどが考えられます。
```

### Block 90 (line 379)

```
また、どの Spike Mark（赤・青テープ）に **Team Prop** があるかを判定・保存することもできます。
```

### Block 91 (line 381)

```
メインループは、**HuskyLens** が3つの Spike Mark をすべて見終えた時や、コードが高信頼度の結果を出した時に終了しても良いでしょう。複数 Spike Mark が視野に入る場合は、** バウンディングボックス** のサイズや位置が有用です。認識にかける時間や、認識できなかった場合の対応も検討してください。
```

### Block 92 (line 383)

```
いずれの場合も、**OpMode** はメインループを抜けて、保存した情報を使って処理を続行します。
```

### Block 93 (line 386)

```
複数色の学習
```

### Block 94 (line 389)

```
上記のチュートリアルで単色の学習が完了したら、**2色** （例：赤系と青系）を学習することもできます。
```

### Block 95 (line 391)

```
これにより、FTC トーナメント中に複数回色学習を行う必要がなくなります。単色の場合は、Red Alliance の試合前に赤を、Blue Alliance の試合前に青を学習します。
```

### Block 96 (line 393)

```
複数色の場合、Red Alliance の **Autonomous OpMode** では**``Color:ID1``** を、Blue Alliance の**Autonomous OpMode** では**``Color:ID2``** を探すことができます。
```

### Block 97 (line 395)

```
複数色学習の **HuskyLens** 公式手順は `オンライン <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336#target_19>`__ に掲載されています。そちらを参照するか、本チュートリアルの説明を参考にしてください。こちらも少し練習が必要です。
```

### Block 98 (line 397)

```
再確認：**HuskyLens** 上部の左側のダイヤルは「**Function ボタン**」（ダイヤル兼ボタン）、右側の小さいボタンは「**Learning ボタン**」です。
```

### Block 99 (line 399)

```
**ステップ1.** Function ボタンを左右に回し、画面下部に「Color Recognition」が表示されるまで操作します。
```

### Block 100 (line 401)

```
**Function ボタンを長押し** して Color Recognition を選択します。
```

### Block 101 (line 403)

```
**ステップ2.** 次のメニューで「Learn Multiple」を選択します。必要に応じて Function ボタンを回し、「Learn Multiple」をハイライトします。
```

### Block 102 (line 405)

```
**Function ボタンを短押し** して「Learn Multiple」を選択します。
```

### Block 103 (line 407)

```
「Learn Multiple」の ON/OFF スライダーが表示されます。必要に応じて Function ボタンを回し、青い四角をスライダーの**右側** に移動します（黄色矢印参照）：
```

### Block 104 (line 416)

```
**Function ボタンを短押し** して「Learn Multiple」を**ON** にします。
```

### Block 105 (line 418)

```
**ステップ3.** Function ボタンを左に回し、「Save & Return」を短押しで選択します。
```

### Block 106 (line 420)

```
画面の「Do you want to save the parameters?」や「Do you save data?」のプロンプトで、Function ボタンを短押しして「Yes」を選択します。これで「Learn Multiple」モードが保存され、設定メニューを終了します。
```

### Block 107 (line 422)

```
これで学習準備完了です！
```

### Block 108 (line 424)

```
**ステップ4.** 先ほどと同様に、**HuskyLens** 画面中央の「+」アイコンを物体の主な色領域に合わせます。** 白い枠** が表示され、主色をターゲットします。枠内にターゲット色だけが入るように狙いましょう。
```

### Block 109 (line 426)

```
主色が枠内に入ったら、右側の小さい **Learning ボタン** を** 長押し** します。** 黄色い枠** が表示され、**HuskyLens** が色を学習中であることを示します。
```

### Block 110 (line 428)

```
長押し中は、色領域を指しながら **HuskyLens** を動かし、様々な距離や角度から色を学習させます。終わったら Learning ボタンを離して学習を完了します。
```

### Block 111 (line 430)

```
長押し学習は数秒で完了します。Learning ボタンを離した後、**``Color:ID1``** が学習され、ラベルが画面に表示されます。簡単です！
```

### Block 112 (line 439)

```
**ステップ5.** 画面の指示に従い、Learning ボタンをもう一度短押しします（5秒タイムアウト前）。これで次の色の学習準備ができます。
```

### Block 113 (line 441)

```
**ステップ6.** レンズを2色目に向け、前述のステップ4を繰り返します。Learning ボタンを長押し、狙い・動かし、離して学習を完了します。
```

### Block 114 (line 444)

```
これで **``Color:ID2``** も学習され、ラベルが画面に表示されます。
```

### Block 115 (line 446)

```
**ステップ7.** 画面の指示に従い、もう一方のボタン（Function ボタン）を短押しするか、5秒のタイムアウトを待ちます。どちらでも複数色学習が完了します。お疲れさまでした！
```

### Block 116 (line 455)

```
すべてをやり直したい場合は、Learning ボタンを短押し→画面の指示に従いもう一度短押しで、学習済み色をすべて**忘却** します。
```

### Block 117 (line 457)

```
再び「+」アイコンが表示されるので、ステップ4から繰り返して色を再学習できます。
```

### Block 118 (line 460)

```
複数色の検出
```

### Block 119 (line 463)

```
例えば **``Color:ID2``** を**OpMode** コードで読み取るには、アルゴリズムを``COLOR_RECOGNITION`` に設定し、``HuskyLens.Block.id`` フィールドが「2」になります。これは上記サンプル**OpMode** のテレメトリー部分で確認できます。
```

### Block 120 (line 472)

```
上記サンプル **OpMode** （単色用、コード変更なし）での DS テレメトリー例：
```

### Block 121 (line 481)

```
IDコード1と2の2色が学習・認識されています（黄色矢印参照）。
```

### Block 122 (line 483)

```
これら2行のテレメトリーは、同じ FOR ループの異なるサイクルで生成されます。``Telemetry.update`` ブロックが FOR ループ終了後に実行されるため、両方が同時に表示されます。FOR ループは HuskyLens の「color block」リストをすべて処理します。
```

### Block 123 (line 485)

```
Java サンプル **OpMode** では、FOR ループ内に以下の行を追加します：
```

### Block 124 (line 489)

```
   int thisColorID = blocks[i].id;                      // 現在認識した色IDを保存
   telemetry.addData("This Color ID", thisColorID);     // 色IDを表示
```

### Block 125 (line 492)

```
``.id`` 以外にも、現在認識したバウンディングボックスの``.width``、``.height``、``.left``、``.top``、``.x``、``.y`` （中心座標）などのフィールドが利用できます。
```

### Block 126 (line 494)

```
色ID番号は**学習順** で割り当てられます。後から番号変更はできないので、学習順と**OpMode** コードの対応を計画してください。
```

### Block 127 (line 497)

```
   **応用ヒント：** 色認識が照明環境に大きく左右される場合、異なる照明条件ごとに別の HuskyLens 色として学習する方法もあります。例えば、赤系 Team Prop を明るい環境で**``Color:ID1``**、暗い環境や影で**``Color:ID2``** として学習し、**OpMode** でどちらのIDも「赤」として扱うことができます。青系も同様にID3・ID4など複数登録可能です。
```

### Block 128 (line 500)

```
オブジェクト学習
```

### Block 129 (line 503)

```
このチュートリアルは **HuskyLens** の「色学習」で終了です。これで**HuskyLens** の基本操作・学習・FTC プログラミング手順を習得できました。
```

### Block 130 (line 505)

```
今後は、**HuskyLens** で「実際の物体」を認識する学習にも挑戦してみてください。20種類のプリセットモデル（「Object Recognition」）や、独自に学習したモデル・画像（「Object Classification」）も利用できます。いずれも色学習と同様の手順で、`HuskyLens 公式ドキュメント <https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336>`__ を参考にしてください。
```

### Block 131 (line 507)

```
**HuskyLens** の「物体認識」は、AI・機械学習の教育的な体験や、色認識よりも高い信頼性を得られる場合があります。
```

### Block 132 (line 509)

```
皆さんの FTC シーズンの成功を祈っています！
```

### Block 133 (line 513)

```
ご質問・ご意見・修正依頼は westsiderobotics@verizon.net までお寄せください。
```


## faq/faqs.rst

### Block 1 (line 2)

```
   :title: FTC チーム よくある質問
   :description: FIRST Tech Challenge チームからよく寄せられる質問への回答
```

### Block 2 (line 6)

```
チーム よくある質問
```

### Block 3 (line 9)

```
登録から競技、審査に至るまで、チーム活動の様々な側面に関する簡潔な回答をお探しの場合は、これらの公式な質問と回答を参照してシーズンを乗り切ってください。さらに詳しい説明が必要な場合は、https://www.firstinspires.org/ にアクセスしてライブチャットを利用するか、`Game Q&A <https://ftc-qa.firstinspires.org/>`__ で競技固有の質問をしてください。
```

### Block 4 (line 11)

```
ダッシュボード/登録 FAQ
```

### Block 5 (line 19)

```
        各チームは、「ユースメンバーを招待する」連絡オプションを表示するために、2人のYPPスクリーニング済みリードコーチが必要です。
```

### Block 6 (line 23)

```
        Pitscoは電子的に支払いを送信します。このプロセスは完了までに24〜48時間かかる場合があります。
```

### Block 7 (line 25)

```
システム FAQ
```

### Block 8 (line 33)

```
        リードコーチ 1 & 2
```

### Block 9 (line 37)

```
        https://ftc-events.firstinspires.org/ が、*FIRST* Tech Challenge の FIRST 公式チーム、イベント、およびイベント結果情報の情報源です。
```

### Block 10 (line 39)

```
審査 FAQ
```

### Block 11 (line 47)

```
        チームは、ロボット、ポートフォリオ、およびプレゼンテーションに参加したいチームメンバーをできるだけ多く連れてくる必要があります。一部のイベントでは、チームがイベントにチェックインする際にポートフォリオが回収されることにご注意ください。
```

### Block 12 (line 51)

```
        審査員は、チームが Structured Interview を完了した直後にフィードバックフォームに記入します。フィードバックは最初の Structured Interview に限定されており、フォローアップのピットインタビューやポートフォリオにおけるチームのパフォーマンスは含まれません。
```

### Block 13 (line 55)

```
        チームは5分間のプレゼンテーションを準備する必要はありませんが、部屋に入る際にプレゼンテーションがないことを審査員に伝える必要があります。審査員はインタビューの冒頭からチームに質問を始めます。
```

### Block 14 (line 58)

```
競技 FAQ
```

### Block 15 (line 66)

```
        競技マニュアルによると、検査中は少なくとも1人の学生が立ち会う必要があります。
        ただし、検査員はロボットの機械的および電気的コンポーネントについて質問します。
        理想的には、そのような質問に答えられるチームメンバーが1人以上いることが望ましいです。
        さらに、ロボットと **Driver Station** の電源を入れ、サイジングなどの特定のルールにロボットが準拠していることを実演する必要がある場合があります。
        これには、メカニズムを操作したりロボットを開始構成に配置したりするためにゲームパッドを使用する必要がある場合、ドライブチームのメンバーが関与することがあります。
        自己検査チェックリストを確認してください。通常、チェックリストに基づいて何をしているかを判断できます。
```

### Block 16 (line 81)

```
        状況が異なっていました。必要であれば、チームは競技エリアのクエスチョンボックスでヘッドレフェリーと話すことができます。
```

### Block 17 (line 93)

```
        チームがマッチの結果について質問がある場合は、1人の学生代表をクエスチョンボックスに送り、ヘッドレフェリーと話す必要があります（この会話のためにマッチを中断しないでください）。レフェリーが間違いを犯したことに同意すれば、修正できます。レフェリーがスコアに自信を持っている場合、チームはその決定を受け入れる必要があります。主要なボランティアの役割、トーナメント運営、およびクエスチョンボックスの使用方法の詳細については、競技マニュアルを確認してください。
```

### Block 18 (line 95)

```
技術 FAQ
```

### Block 19 (line 103)

```
        ヘルプを得るのに最適な場所は `ftc-community プラットフォーム <https://ftc-community.firstinspires.org>`__ です。
        ftc-community プラットフォームは、様々な知識豊富な人々が監視しているコミュニティの質問場所であり、あなたの質問に答えてくれる可能性が高いです！
```

### Block 20 (line 108)

```
*FIRST* Tech Challenge ゲームデザイン委員会によるレビュー済み
```

### Block 21 (line 111)

```
   このドキュメントは非公式な日本語翻訳です。正式な情報については、英語版の公式ドキュメントを参照してください。
```


## ftc_sdk/overview/index.rst

### Block 1 (line 2)

```
   :title: FIRST Tech Challengeソフトウェア開発キット
   :description: FTC SDKの簡単な紹介
```

### Block 2 (line 6)

```
**FIRST Tech Challenge** ソフトウェア開発キット
```

### Block 3 (line 9)

```
ソフトウェア開発キット（SDK）は、**FIRST Tech Challenge** ロボット用のソフトウェアを開発し、実行するためのツールのコレクションです。SDKソフトウェアには以下が含まれます：
```

### Block 4 (line 13)

```
   *  セルフインスペクト、 :doc:`ロボット構成 </hardware_and_software_configuration/configuring/index>` などを含む
```

### Block 5 (line 17)

```
   *  :doc:`Blocksプログラミング環境 </programming_resources/blocks/Blocks-Tutorial>` を含む
   *  :doc:`OnBot Javaプログラミング環境 </programming_resources/onbot_java/OnBot-Java-Tutorial>` を含む
```

### Block 6 (line 20)

```
-  `Android Studioプロジェクト <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__
   :doc:`Android Studio </programming_resources/android_studio_java/Android-Studio-Tutorial>` でRobot Controller Appをビルドするため
-  `Javadocリファレンスドキュメント <https://javadoc.io/doc/org.firstinspires.ftc>`__
-  シーズン固有のアセット（TensorFlowモデル、Vuforiaデータベースなど）
```

### Block 7 (line 25)

```
すべてのリリース済みアプリ/ソースは、`SDK GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ にあります。
```

### Block 8 (line 27)

```
SDKリリース
```

### Block 9 (line 30)

```
ソフトウェア開発キットは、**FIRST Tech Challenge** **Technology Team** として知られるコアグループによって、プライベートGitHubリポジトリ内で開発および保守されています。このリポジトリは、将来の**FIRST Tech Challenge** ゲームの秘密、開発中の機能、およびその他の開発の側面の詳細を漏らさないようにするため、プライベートに保たれています。開発とメンテナンスは年間を通じて継続的に行われています。
```

### Block 10 (line 32)

```
リリースコンテンツ
```

### Block 11 (line 35)

```
SDKがリリースする準備が整うと、プライベートSDKリポジトリがビルドされ、エクスポートされます。このビルドは以下で構成されます：
```

### Block 12 (line 37)

```
-  ビルドされたDriver Stationアプリ（``FtcDriverStation-release.apk`` ）
-  ビルドされたRobot Controllerアプリ（``FtcRobotController-release.apk`` ）
-  Android Studioプロジェクトのソースコード（``vX.X.zip``、``vX.X.tar.gz`` ）
-  `Javadocリファレンスドキュメント <https://javadoc.io/doc/org.firstinspires.ftc>`__
-  シーズン固有のアセット（TensorFlowモデル、Vuforiaデータベースなど、別途ホスト）
```

### Block 13 (line 43)

```
エクスポートは、`FtcRobotController GitHubリポジトリ
<https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に `ソフトウェアリリース
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ としてプッシュされます。
```

### Block 14 (line 47)

```
`FtcRobotController GitHubリポジトリ
<https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ は、エクスポートされたAndroid Studioプロジェクトのソースでも更新され、変更を追跡でき、GitHubリポジトリをチームが `フォーク
```

### Block 15 (line 50)

```
または `クローン
```

### Block 16 (line 52)

```
できます。ただし、この更新は一方向のプッシュであるため、FtcRobotControllerリポジトリへの公開貢献（`プルリクエスト
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>`__）は受け付けられません。ただし、コミュニティは自由に、**Technology Team** が検討して対処するための課題をリポジトリで作成することが奨励されています。
```

### Block 17 (line 56)

```
   TensorFlowモデルやVuforiaデータベースなどの一部のシーズン固有のアセットは、FtcRobotController GitHubリポジトリに直接含まれていません。代わりに、Maven Centralでホストされている ``.AAR`` にパッケージ化されています。Robot Controller Appを使用する場合、これらのアセットはアプリに含まれています。Android Studioを使用する場合、これらのアセットはプロジェクトを最初にコンパイルするときにダウンロードされ、プロジェクトに含まれます（したがって、アクティブなインターネット接続が必要です）。
```

### Block 18 (line 58)

```
リリーススケジュール
```

### Block 19 (line 61)

```
これらのリリースは、正確な日付が明確に定義されていない場合でも、定期的なスケジュールで行われます：
```

### Block 20 (line 63)

```
-  **キックオフSDKリリース** - 通常、**FIRST Tech Challenge** キックオフから1〜2週間以内にリリースされます。キックオフSDKは、通常、シーズン中の使用に必要な最小ソフトウェアバージョンです。
-  **更新/パッチリリース** - これらは通常、**FIRST Tech Challenge** シーズン中に、重大な問題または有用な機能がチームで利用可能になったときにリリースされます。更新/パッチリリースは、重大なパッチまたはバグ修正が発行されない限り、競技には通常必要ありません。
-  **オフシーズンリリース** - オフシーズンリリースは、破壊的変更に対してチームを準備するため、または次のシーズンの新機能のテクノロジープレビューを提供するために使用されます。
```

### Block 21 (line 67)

```
ソフトウェアSDKの更新は、`FIRST Tech Challengeブログ <https://community.firstinspires.org/topic/ftc>`__ および
`チームメールブラスト <https://www.firstinspires.org/resources/library/ftc/team-email-blast-archive>`__ を通じて発表されます。
```

### Block 22 (line 71)

```
SDKリリースノート
```

### Block 23 (line 74)

```
SDKリリースの最も重要な要素の1つは、
`SDKリリースノート <https://github.com/FIRST-Tech-Challenge/FtcRobotController#release-information>`__ です。SDKリリースノートには、破壊的変更、機能強化、注目すべき重大なバグ修正など、各リリースの重要な側面が含まれています。
```

### Block 24 (line 77)

```
破壊的変更
```

### Block 25 (line 80)

```
破壊的変更は、その名前が示すとおり、SDKのAPIまたは一般的なアーキテクチャ内で行われた変更であり、既存のコードまたは構成を破壊する可能性があります。SDKのすべてのユーザーが、特定のリリースに破壊的変更セクションが存在する場合は、リリースノートの破壊的変更セクションを読み、既存のコードへの影響を判断することが特に重要です。
```

### Block 26 (line 82)

```
機能強化
```

### Block 27 (line 85)

```
機能強化は、SDKの新機能または既存機能の（非破壊的な）改善です。機能強化には、改善されたロギング、新しいユーザーインターフェース（UI）、より良いユーザーエクスペリエンス（UX）、新しいAPI、より良いパフォーマンス、または信頼性の向上などの項目が含まれる場合があります。SDKのすべての機能強化がリリースノートに記載されているわけではありませんが、ユーザーに直接影響を与えるものは記載されている必要があります。
```

### Block 28 (line 87)

```
バグ修正
```

### Block 29 (line 90)

```
SDKのほぼすべてのリリースにはバグ修正が含まれていますが、**Technology Team** が重要なバグ修正の可視性を高めたい場合、リリースノートのバグ修正セクションに含まれます。バグに回避策が必要だった場合、チームコードが影響を受ける可能性があり、リリースノートに記載されることは、**Technology Team** がチームに回避策が不要になったことを通知する方法です。
```

### Block 30 (line 92)

```
SDKソフトウェアの更新
```

### Block 31 (line 95)

```
チームがSDKソフトウェアを更新することは重要です。シーズン中の更新は必須ではない場合があります。チームは、競技マニュアルでゲームに必要な最小ソフトウェアバージョンを確認できます。64ビットWindowsコンピューターが利用可能な場合は、REV Hardware Clientを使用してハードウェアを更新することをお勧めします。そうでない場合は、提供される代替方法を使用してソフトウェアを更新できます。
```

### Block 32 (line 97)

```
-  :doc:`REV Hardware Clientの更新 </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
-  :doc:`Driver Stationアプリの更新 </ftc_sdk/updating/ds_app/Updating-the-DS-App>`
-  :doc:`Robot Controllerアプリの更新 </ftc_sdk/updating/rc_app/Updating-the-RC-App>`
-  :doc:`Driver Hub OSの更新 </ftc_sdk/updating/driverhub_os/Updating-the-Driver-Hub-OS>`
-  :doc:`Control Hub OSの更新 </ftc_sdk/updating/controlhub_os/Updating-the-Control-Hub-OS>`
-  :doc:`Hubファームウェアの更新 </ftc_sdk/updating/hub_firmware/Updating-Hub-Firmware>`
```


## ftc_sdk/updating/controlhub_os/Updating-the-Control-Hub-OS.rst

### Block 1 (line 1)

```
Control Hub OSの更新
```

### Block 2 (line 4)

```
オペレーティングシステム（OS）は、タスクのスケジューリング、アプリケーションの実行、周辺機器の制御など、コンピューターの基本機能をサポートするソフトウェアです。**REV Control Hub** では、これを更新する必要がある場合があります。このOS更新は厳密には :doc:`ソフトウェア開発キット（SDK） </ftc_sdk/overview/index>` の一部ではありませんが、SDKが正しく動作するためには、Control HubでこれらのOS更新が必要です。
```

### Block 3 (line 6)

```
**Control Hub** OS を更新する方法は2つあります：
```

### Block 4 (line 9)

```
2. コンピューター上の管理ページ
```

### Block 5 (line 11)

```
**Control Hub** OS の更新に関する詳細情報は、
`REV Robotics の優れたドキュメントサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system>`__ にあります。
```

### Block 6 (line 16)

```
   1. REV Control Hubに12Vロボット電源を供給します。
```

### Block 7 (line 18)

```
   2. USB-Cデータケーブルを使用して、Control HubをREV Hardware Clientを実行しているコンピューターに直接接続します。
```

### Block 8 (line 20)

```
   3. Hubの大きなアイコン/矩形をクリックします。「Control Hub Operating
      System」の下に、現在のバージョンと最新バージョンの不一致がある場合は表示されます（下の黄色の楕円）。
```

### Block 9 (line 24)

```
         :alt: Control Hub OSの更新
```

### Block 10 (line 28)

```
         Control Hub OSの更新
```

### Block 11 (line 30)

```
   ドロップダウンメニューで最新バージョンを確認し、青色の「Update」矩形をクリックします（上の緑色の矢印）。
   :doc:`REV Hardware Clientの更新 </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
   で必要な更新ファイルが事前にダウンロードされているため、この更新の速度は向上しています。
```

### Block 12 (line 34)

```
   完了です！Control HubのOSが更新されました。
```

### Block 13 (line 38)

```
   1. コンピューターをWi-Fi経由でControl Hubに接続します。Chromeブラウザで
      **FIRST Tech Challenge** インターフェースを開きます。
```

### Block 14 (line 41)

```
   2. Manageタブをクリックし、Update Control Hub Operating Systemまでスクロールします。
```

### Block 15 (line 44)

```
         :alt: Control Hub OSの更新
```

### Block 16 (line 48)

```
         Control Hub OSの更新
```

### Block 17 (line 50)

```
   3. 必要に応じて、REV Roboticsの `Control
      Hub OS Webページ <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system#using-the-robot-controller-console>`__ から最新のOSファイルをダウンロードします。
      このファイルは解凍または「unzip」しないでください。
```

### Block 18 (line 54)

```
   4. 管理ページで「Select Update File…」をクリックし、OSファイルをダウンロードしたコンピューターのフォルダーに移動します。
```

### Block 19 (line 56)

```
   5. そのファイルを選択し、「Update & Reboot」をクリックします（上の緑色の矢印）。
```

### Block 20 (line 58)

```
   以上です！Control HubのOSが更新されました。
```

### Block 21 (line 60)

```
質問、コメント、修正は westsiderobotics@verizon.net まで
```


## ftc_sdk/updating/driverhub_os/Updating-the-Driver-Hub-OS.rst

### Block 1 (line 1)

```
Driver Hub OSの更新
```

### Block 2 (line 4)

```
オペレーティングシステム（OS）は、タスクのスケジューリング、アプリケーションの実行、周辺機器の制御など、コンピューターの基本機能をサポートするソフトウェアです。**REV Driver Hub** では、これを更新する必要がある場合があります。このOS更新は厳密には :doc:`ソフトウェア開発キット（SDK） </ftc_sdk/overview/index>` の一部ではありませんが、SDKが正しく動作するためには、Driver HubでこれらのOS更新が必要です。
```

### Block 3 (line 6)

```
**Driver Hub** OS を更新する方法は2つあります：
```

### Block 4 (line 9)

```
2. **Driver Hub** 上のソフトウェアマネージャー
```

### Block 5 (line 11)

```
**Driver Hub** OS の更新に関する詳細情報は、
`REV Robotics の優れたドキュメントサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-the-driver-hub>`__ にあります。
```

### Block 6 (line 16)

```
   1. Driver Hubの電源を入れます。USB-Cデータケーブルを使用して、REV Hardware Clientを実行しているコンピューターに直接接続します。
```

### Block 7 (line 18)

```
   2. Driver Hubの大きなアイコン/矩形をクリックします。「Driver Hub
      Operating System」の下に、現在のバージョンと最新バージョンの不一致がある場合は表示されます（下の黄色の
      楕円）。
```

### Block 8 (line 23)

```
         :alt: Driver Hub OSの更新
```

### Block 9 (line 27)

```
         Driver Hub OSの更新
```

### Block 10 (line 29)

```
      ドロップダウンメニューで最新バージョンを確認します（ある場合）。次に、該当する場合は「Update」と表示された青色の矩形をクリックします。
      :doc:`REV Hardware Clientの更新
```

### Block 11 (line 32)

```
      で必要な更新ファイルが事前にダウンロードされているため、この更新の速度は向上しています。
```

### Block 12 (line 35)

```
   完了です！Driver HubのOSが更新されました。
```

### Block 13 (line 39)

```
   REV Driver Hubには、ソフトウェアマネージャーと呼ばれる組み込みアプリがあり、
   Driver Hub OS（およびその他の関連ソフトウェア）を自動的に更新できます。
   インターネット接続のみが必要です。
```

### Block 14 (line 43)

```
   1. すべてのアプリを閉じ、Driver HubのWi-Fiメニューを開きます（設定内、またはホーム画面の上部から2回スワイプダウン）。
      Driver Hubを一時的にWi-Fi経由でインターネットに接続します。
```

### Block 15 (line 46)

```
   2. Driver Hubのホーム画面でソフトウェアマネージャーアプリを開きます（下の左側の画像）。
```

### Block 16 (line 49)

```
         :alt: ソフトウェアマネージャーの更新
```

### Block 17 (line 53)

```
         ソフトウェアマネージャーの更新
```

### Block 18 (line 55)

```
   3. ソフトウェアマネージャーは、必要な更新を自動的にチェックし、
      結果を表示します（上の右側の画像）。グレーのボタンをタッチして、必要に応じてDriver Hub Operating System（OS）を含む更新を実行します。
```

### Block 19 (line 59)

```
         REV RoboticsはDriver Hub用のダウンロード可能なOSイメージファイルを提供していますが、
         このチュートリアルで利用可能なツールは、OSを更新するためにこのファイルを提供することを受け付けていません。
```

### Block 20 (line 62)

```
   4. すべてが完了したら、インターネットアクセスに使用したWi-Fiネットワークを「削除」します。
      これで、Driver Hubは通常の競技での使用準備が整いました。
```

### Block 21 (line 65)

```
質問、コメント、修正は westsiderobotics@verizon.net まで
```


## ftc_sdk/updating/ds_app/Updating-the-DS-App.rst

### Block 1 (line 1)

```
Driver Stationアプリの更新
```

### Block 2 (line 4)

```
**Driver Station App** は、**FIRST Tech Challenge**:doc:`ソフトウェア開発キット（SDK） </ftc_sdk/overview/index>` で提供されるアプリの1つです。**Driver Station** アプリは、ロボット構成、ゲームパッドのサポート、セルフインスペクト、チームコードの選択と実行などの主要なインターフェースです。このアプリは**REV Driver Hub** または承認されたAndroidスマートフォンで実行されます。
```

### Block 3 (line 6)

```
このページでは、以下のデバイスで**Driver Station** （**DS** ）アプリを更新する方法を示します：
```

### Block 4 (line 9)

```
-  承認されたAndroid DSスマートフォン
```

### Block 5 (line 11)

```
**Driver Station** アプリを更新するこれらの方法は、ロボットチームコードのプログラミングに使用されるプログラミング言語/環境に関係なく同じです。
```

### Block 6 (line 15)

```
   **REV Driver Hub** 上のDSアプリを更新する3つの方法があります：
```

### Block 7 (line 18)

```
   #. APKを使用した「サイドローディング」
   #. REV Driver Hub上のソフトウェアマネージャー
```

### Block 8 (line 23)

```
      **REV Driver Hub** をRHCがインストールされて開いているWindowsコンピューターにUSB-Cデータケーブルを使用して直接接続します。左上の「Hardware」タブがアクティブであることを確認してください。**Driver Hub** 上のDSアプリを開く必要は** ありません** 。
```

### Block 9 (line 25)

```
      ここでは、コンピューターをインターネットに接続する必要はありません。
      :doc:`REV Hardware Clientの更新
```

### Block 10 (line 28)

```
      で必要なDS更新ファイルが事前にダウンロードされているためです。
```

### Block 11 (line 30)

```
      RHCアプリは、ここに示すように**Driver Hub** を認識します：
```

### Block 12 (line 33)

```
         :alt: Driver Hubの認識
```

### Block 13 (line 37)

```
         Driver Hubの認識
```

### Block 14 (line 39)

```
      認識されたら、**Driver Hub** の大きなアイコン/矩形をクリックします。RHCアプリは、DSアプリの更新ステータスを表示します（ある場合）。
```

### Block 15 (line 42)

```
         :alt: Driver Hubの更新
```

### Block 16 (line 46)

```
         Driver Hubの更新
```

### Block 17 (line 48)

```
      青色のUpdate矩形（緑色の矢印）をクリックするだけです – 完了です！
```

### Block 18 (line 50)

```
      RHCにDSアプリを既にダウンロードしていたため、更新は高速でした。これは、青色のUpdate矩形の左側に「(Already Downloaded)」と表示されていました。
```

### Block 19 (line 52)

```
      青色のUpdate矩形のすぐ上のドロップダウンリストで、DSアプリの **古い** バージョンを選択することもできました。
```

### Block 20 (line 54)

```
      インストール後、必要に応じて、アプリメニューからDSアプリアイコンを**Driver Hub** のホーム画面にドラッグします。
```

### Block 21 (line 56)

```
      これで、**Driver Hub** をコンピューターから取り外し、RHCアプリを閉じることができます。更新されたDSアプリは使用準備が整いました。
```

### Block 22 (line 60)

```
      ここでは、Android Package または **APKファイル** を直接操作して、**Driver Hub** にDSアプリをインストールします。PCまたはMac、新旧を問わず、どのコンピューターでも使用できます。この方法は「サイドローディング」と呼ばれることがあります。
```

### Block 23 (line 62)

```
      1. コンピューターをインターネットに接続し、Webブラウザーを開いて、`SDK GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に移動します。
```

### Block 24 (line 65)

```
            :alt: SDK GitHubリポジトリ
```

### Block 25 (line 69)

```
            SDK GitHubリポジトリ
```

### Block 26 (line 71)

```
         右側の「Releases」の下にある「Latest」アイコン（上の黄色の楕円）をクリックします。
```

### Block 27 (line 73)

```
         次のページで、「Latest」セクションで少し下にスクロールして、「Assets」の短いリストを表示します。ファイル「FtcDriverStation-release.apk」をクリックして、コンピューターにダウンロードします。
```

### Block 28 (line 76)

```
            :alt: SDK GitHubリリース
```

### Block 29 (line 80)

```
            SDK GitHubリリース
```

### Block 30 (line 82)

```
      2. **Driver Hub** をUSB-Cデータケーブルでコンピューターに接続します。
```

### Block 31 (line 84)

```
      3. ブラウザーのファイル転送ウィンドウを使用するか、コンピューターのファイルマネージャーを使用して、ダウンロードしたAPKファイルを**Driver Hub** の**Downloads** フォルダーに転送します。
```

### Block 32 (line 86)

```
      4. **Driver Hub** で、ファイルマネージャーアプリを開き、**Downloads** フォルダーに移動します。
```

### Block 33 (line 88)

```
      5. APKファイルをタッチしてインストールプロセスを開始します。プロンプトに従ってインストールを完了します。
```

### Block 34 (line 91)

```
            初めてサイドローディングする場合、不明なソースからのアプリのインストールを許可する必要がある場合があります。
```

### Block 35 (line 93)

```
      6. インストール後、アプリメニューからDSアプリアイコンを**Driver Hub** のホーム画面にドラッグします。
```

### Block 36 (line 95)

```
      完了です！更新されたDSアプリは使用準備が整いました。
```

### Block 37 (line 99)

```
      **REV Driver Hub** には、ソフトウェアマネージャーと呼ばれる組み込みアプリがあり、DSアプリ（およびその他の関連ソフトウェア）を自動的に更新できます。インターネット接続のみが必要です。
```

### Block 38 (line 101)

```
      1. すべてのアプリを閉じ、**Driver Hub** のWi-Fiメニューを開きます（設定内、またはホーム画面の上部から2回スワイプダウン）。**Driver Hub** を一時的にWi-Fi経由でインターネットに接続します。
```

### Block 39 (line 103)

```
      2. **Driver Hub** のホーム画面でソフトウェアマネージャーアプリを開きます（下の左側の画像）。
```

### Block 40 (line 106)

```
            :alt: ソフトウェアマネージャーの更新
```

### Block 41 (line 110)

```
            ソフトウェアマネージャーの更新
```

### Block 42 (line 112)

```
      3. ソフトウェアマネージャーは、必要な更新を自動的にチェックし、結果を表示します（上の右側の画像）。グレーのボタンをタッチして、必要に応じてDSアプリを含む更新を実行します。
```

### Block 43 (line 114)

```
      4. すべてが完了したら、インターネットアクセスに使用したWi-Fiネットワークを「削除」します。これで、**Driver Hub** は通常の競技での使用準備が整いました。
```

### Block 44 (line 118)

```
   AndroidスマートフォンでDSアプリを更新する2つの方法があります：
```

### Block 45 (line 121)

```
   2. APKを使用した「サイドローディング」
```

### Block 46 (line 125)

```
      DSスマートフォンをRHCがインストールされて開いているコンピューターにUSBデータケーブルを使用して直接接続します。充電専用ケーブルではなく、USBデータケーブルを使用してください。左上の「Hardware」タブがアクティブであることを確認してください。スマートフォン上のDSアプリを開く必要は **ありません** 。
```

### Block 47 (line 127)

```
      ここでは、コンピューターをインターネットに接続する必要はありません。
      :doc:`REV Hardware Clientの更新
```

### Block 48 (line 130)

```
      で必要なDS更新ファイルが事前にダウンロードされているためです。
```

### Block 49 (line 132)

```
      RHCアプリは、ここに示すようにスマートフォンを認識します：
```

### Block 50 (line 135)

```
         :alt: スマートフォンの認識
```

### Block 51 (line 139)

```
         スマートフォンの認識
```

### Block 52 (line 141)

```
      スマートフォンが認識されない場合は、スマートフォンで :doc:`開発者オプション
```

### Block 53 (line 143)

```
      が有効になっていることを確認してください。必要に応じて、REV Hardware Clientアプリの左下にある「Scan for Devices」ボタンをクリックして、RHCにデバイスを再スキャンさせます。
```

### Block 54 (line 145)

```
      認識されたら、そのスマートフォンの大きなアイコン/矩形をクリックします。RHCアプリは更新ステータスを表示します。
```

### Block 55 (line 148)

```
         :alt: スマートフォンの更新ステータス
```

### Block 56 (line 152)

```
         スマートフォンの更新ステータス
```

### Block 57 (line 154)

```
      青色のUpdate矩形（緑色の矢印）をクリックするだけです – 完了です！
```

### Block 58 (line 156)

```
      RHCにDSアプリを既にダウンロードしていたため、更新は高速でした。これは、青色のUpdate矩形の左側に「(Already Downloaded)」と表示されていました。
```

### Block 59 (line 158)

```
      青色のUpdate矩形のすぐ上のドロップダウンリストで、DSアプリの **古い** バージョンを選択することもできました。
```

### Block 60 (line 160)

```
      インストール後、アプリメニューからDSアプリアイコンをスマートフォンのホーム画面にドラッグします。
```

### Block 61 (line 162)

```
      これで、スマートフォンをコンピューターから取り外し、RHCアプリを閉じることができます。更新されたDSアプリは使用準備が整いました。
```

### Block 62 (line 166)

```
      ここでは、Android Package または **APKファイル** を直接操作して、スマートフォンにDSアプリをインストールします。PCまたはMac、新旧を問わず、どのコンピューターでも使用できます。この方法は「サイドローディング」と呼ばれることがあります。
```

### Block 63 (line 168)

```
      1. コンピューターをインターネットに接続し、Webブラウザーを開いて、`SDK GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に移動します。
```

### Block 64 (line 171)

```
            :alt: SDK GitHubリポジトリ
```

### Block 65 (line 175)

```
            SDK GitHubリポジトリ
```

### Block 66 (line 177)

```
         右側の「Releases」の下にある「Latest」アイコン（上の黄色の楕円）をクリックします。
```

### Block 67 (line 179)

```
         次のページで、「Latest」セクションで少し下にスクロールして、「Assets」の短いリストを表示します。ファイル「FtcDriverStation-release.apk」をクリックして、コンピューターにダウンロードします。
```

### Block 68 (line 182)

```
            :alt: SDK GitHubリリース
```

### Block 69 (line 186)

```
            SDK GitHubリリース
```

### Block 70 (line 188)

```
      2. スマートフォンをUSBデータケーブルでコンピューターに接続します。充電専用ケーブルではなく、データケーブルを使用してください。
```

### Block 71 (line 190)

```
      3. ブラウザーのファイル転送ウィンドウを使用するか、コンピューターのファイルマネージャーを使用して、ダウンロードしたAPKファイルをスマートフォンの **Downloads** フォルダーに転送します。
```

### Block 72 (line 192)

```
      4. スマートフォンで、ファイルマネージャーアプリを開き、**Downloads** フォルダーに移動します。
```

### Block 73 (line 194)

```
      5. APKファイルをタッチしてインストールプロセスを開始します。プロンプトに従ってインストールを完了します。
```

### Block 74 (line 197)

```
            初めてサイドローディングする場合、不明なソースからのアプリのインストールを許可する必要がある場合があります。
```

### Block 75 (line 199)

```
      6. インストール後、アプリメニューからDSアプリアイコンをスマートフォンのホーム画面にドラッグします。
```

### Block 76 (line 201)

```
      完了です！更新されたDSアプリは使用準備が整いました。
```

### Block 77 (line 203)

```
質問、コメント、修正は westsiderobotics@verizon.net まで
```


## ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client.rst

### Block 1 (line 1)

```
REV Hardware Clientのインストールと更新
```

### Block 2 (line 4)

```
REV Hardware Clientは、**FIRST Tech Challenge** で使用されるデバイスのソフトウェア更新を簡素化するデスクトップアプリまたはソフトウェアツールです。残念ながら、REV Hardware ClientはWindows専用であり、Apple/Macユーザーはソフトウェア更新の代替方法を使用する必要があります。このチュートリアルでは、一部のステップでソフトウェアと更新をダウンロードするよう求められますが、これは必須ではありませんが、更新時に時間を節約できます。
```

### Block 3 (line 6)

```
インストールするには、Windows 7以降を実行している **64ビット** PCまたはラップトップで次の手順を実行します。
```

### Block 4 (line 8)

```
**Apple/Macユーザーはこれらの手順をスキップしてください。**
```

### Block 5 (line 11)

```
   64ビットかどうかわからない場合は、Windowsエクスプローラーで「コンピューター」（Win
   7）または「このPC」（Win 10）を右クリックし、プロパティを選択して「システムの種類」を確認してください。
```

### Block 6 (line 14)

```
RHCのインストール
```

### Block 7 (line 17)

```
1. コンピューターをインターネットに接続し、`REV RHCダウンロードページ <https://docs.revrobotics.com/rev-hardware-client/>`__ からRHCをダウンロードします。
   オレンジ色のDownloadボタンをクリックし、コンピューターのDownloadsフォルダーを選択してファイルを保存します。
```

### Block 8 (line 21)

```
      :alt: REV Hardware Clientのダウンロード
```

### Block 9 (line 25)

```
      REV Hardware Clientのダウンロード
```

### Block 10 (line 29)

```
2. 左下に表示されたダウンロードファイル（緑色の矢印）を確認します。そのファイル名をクリックしてRHCアプリのインストールを開始し、プロンプトに従います。
   完了すると、RHCアイコンがコンピューターのデスクトップに表示されます。
```

### Block 11 (line 32)

```
   コンピューターが64ビット **ではない** 場合、RHCのインストールは適切なエラーメッセージで失敗します。
```

### Block 12 (line 34)

```
初期更新のダウンロード
```

### Block 13 (line 37)

```
RHCアプリを開きます。これは、近いうちに必要になる可能性のあるさまざまなソフトウェアを **事前ダウンロード** する良い機会です。
```

### Block 14 (line 39)

```
なぜ今ダウンロードするのですか？後で、このコンピューターはWi-Fi経由でRobot Controllerに接続され、インターネットには接続されない可能性があります。または、緊急に必要なときに良いインターネット接続が利用できない可能性があります（マーフィーの法則）。
```

### Block 15 (line 41)

```
Downloadsタブ（左上）をクリックします。「Available Files」の下には、**FIRST Tech Challenge** 用のソフトウェアと、**FIRST Robotics Competition** と呼ばれる別のプログラム用のソフトウェアのリストがあります。
```

### Block 16 (line 44)

```
   :alt: 利用可能なファイル
```

### Block 17 (line 48)

```
   REV Hardware Client利用可能なファイル
```

### Block 18 (line 52)

```
オレンジ色のDownloadボタンをクリックして、5つの **FIRST Tech Challenge** 項目（黄色の矩形）のみをダウンロードします。これには数分かかる場合があります。OSファイルは大きいです。
```

### Block 19 (line 54)

```
これらのファイルがどこに保存されているかを追跡する必要はありません。デバイスの更新に必要なときにRHCアプリで利用できます。
```

### Block 20 (line 56)

```
完了すると、これら5つの項目は「Downloaded Files」という見出しの下に表示されます。
```

### Block 21 (line 58)

```
REV Hardware Clientの更新
```

### Block 22 (line 61)

```
1. インターネットに接続されたWindowsコンピューターで、REV Hardware Clientを開きます。
```

### Block 23 (line 64)

```
   :alt: 更新の更新
```

### Block 24 (line 68)

```
   REV Hardware Client利用可能な更新
```

### Block 25 (line 72)

```
2. 「About」タブをクリックし、次に「Check for Updates」をクリックします（上の緑色の矢印）。新しいバージョンが利用可能な場合は、クリックして更新します。
```

### Block 26 (line 74)

```
以上です！これらのファイルは後で、さまざまなデバイスを更新するときに使用します。RHCの詳細については、
`REV Roboticsの優れたドキュメントサイト <https://docs.revrobotics.com/rev-hardware-client/>`__ を参照してください。
```

### Block 27 (line 77)

```
質問、コメント、修正は westsiderobotics@verizon.net まで
```


## ftc_sdk/updating/hub_firmware/Updating-Hub-Firmware.rst

### Block 1 (line 1)

```
Hubファームウェアの更新
```

### Block 2 (line 4)

```
ファームウェアは、デバイスの回路基板または電子 **ハードウェア** を制御する低レベルのソフトウェアです。:doc:`ソフトウェア開発キット（SDK） </ftc_sdk/overview/index>` が正しく動作するためには、REV Expansion HubおよびREV Control Hubでこれを更新する必要がある場合があります。
```

### Block 3 (line 6)

```
以下の5つの方法があります：
```

### Block 4 (line 9)

```
2. **Driver Station** アプリ
3. **Robot Controller (RC)** アプリ - RC スマートフォン上
4. コンピューター上の管理ページ
5. **Driver Station** デバイス（DS スマートフォンまたは **Driver Hub** ）上の管理ページ
```

### Block 5 (line 16)

```
   1. REV Control Hubの場合は、12Vロボット電源を供給します。REV Expansion Hubの場合は、
      12V電源はオプションです。
```

### Block 6 (line 19)

```
   2. REV HubをUSBデータケーブル（充電専用ではないもの）を使用して、REV Hardware Clientを実行しているコンピューターに直接接続します。Expansion Hubのポートは
      Mini USB（microではない）です。Control Hubの場合は、Mini USBポートではなく、USB-C
      ポートのみを使用してください。
```

### Block 7 (line 23)

```
   3. Hubの大きなアイコン/矩形をクリックします。「Expansion/Control Hub
      Firmware」の下に、現在のバージョンと最新バージョンの不一致がある場合は表示されます（下の黄色の楕円）。
```

### Block 8 (line 27)

```
         :alt: ファームウェアの更新
```

### Block 9 (line 31)

```
         ファームウェアの更新
```

### Block 10 (line 33)

```
      Control Hubの例は次のとおりです：
```

### Block 11 (line 36)

```
         :alt: ファームウェアの更新
```

### Block 12 (line 40)

```
         ファームウェアの更新
```

### Block 13 (line 42)

```
      ドロップダウンメニューで最新バージョンを確認し、青色の「Re-install」矩形をクリックします（上の緑色の矢印）。これは迅速に実行されます。
      :doc:`REV Hardware Clientの更新
```

### Block 14 (line 45)

```
      で必要な更新ファイルが事前にダウンロードされているためです。
```

### Block 15 (line 47)

```
      完了です！Hubのファームウェアが更新されました。
```

### Block 16 (line 49)

```
   RHCを使用してHubファームウェアを更新する詳細については、`REV Roboticsの優れたドキュメントサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware>`__ を参照してください。
```

### Block 17 (line 53)

```
   この方法は、DSスマートフォンまたはDriver Hubで実行されているすべてのDSアプリに適用されます。
```

### Block 18 (line 55)

```
   1. REV Control Hubの場合は、12Vロボット電源を供給します。REV Expansion Hubの場合は、
      Robot Controller（RC）スマートフォンに直接接続し、RCアプリを開き、 **さらに**
      12V電源を供給します。更新するExpansion Hubは、中間のControl Hubや
      他の（プライマリ）Expansion Hubを介さずに、RCスマートフォンに **直接接続** する必要があります。更新後、必要に応じてそのHubをセカンダリ位置に戻すことができます。
```

### Block 19 (line 60)

```
   2. DSスマートフォンまたはDriver HubからDSアプリをRCデバイスに接続/ペアリングします。DS Settings、Advanced（Robot Controller）Settings、REV
      Hub Firmware Updateを選択します。
```

### Block 20 (line 64)

```
         :alt: ファームウェアの更新
```

### Block 21 (line 68)

```
         ファームウェアの更新
```

### Block 22 (line 70)

```
      RCデバイスに保存されているHubファームウェアおよび/またはアプリに「バンドル」されているHubファームウェアの利用可能なリストを確認します。
```

### Block 23 (line 72)

```
   3. 最新版がリストに表示 **されない** 場合は、コンピューターからRobot Controllerにファームウェアファイルを転送できます。USBデータケーブル（充電専用ケーブルではない）を使用して、ファームウェアファイルをRCデバイスのFIRST/updates/Expansion Hub Firmwareというサブフォルダーに保存します。
```

### Block 24 (line 74)

```
      現在および古いファームウェアファイルは、
      `REV RoboticsのWebサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware/firmware-changelog>`__ にあります。
```

### Block 25 (line 77)

```
      次に、この利用可能なファームウェアのリストに戻ります。
```

### Block 26 (line 79)

```
   4. 最新のファームウェアバージョンを選択し、「Update Hub
      Firmware」をタッチします（上の緑色の矢印）。プロセスが完了するまで待ちます。Hubのプラグを抜いたり、ロボットを再起動したりしないでください。
```

### Block 27 (line 82)

```
   以上です！Hubのファームウェアが更新されました。
```

### Block 28 (line 86)

```
   この方法は、上記の方法2と **全く同じ** です。
   DSアプリは単にRCアプリへのポータルまたはウィンドウを提供していたためです。
```

### Block 29 (line 89)

```
   ここに個別にリストされているのは、Control Hubには適用されず、**Expansion
   Hub** にのみ適用されるためです。Control HubはRCスマートフォンを使用しません。つまり、
   ユーザーは通常、Control Hub上のRCアプリと直接インターフェースすることはありません。
```

### Block 30 (line 93)

```
   繰り返しになりますが、Expansion Hubは、中間（プライマリ）Expansion Hubを介さずに、RCスマートフォンに **直接** 接続する必要があります。更新後、必要に応じてそのHubをセカンダリ位置に戻すことができます。
```

### Block 31 (line 97)

```
   1. コンピューターをWi-Fi経由でControl HubまたはRCスマートフォンに接続します。Chromeブラウザで管理インターフェースを開きます。
```

### Block 32 (line 99)

```
   2. Manageタブをクリックし、Update REV Hub Firmwareまでスクロールします。
```

### Block 33 (line 102)

```
         :alt: ファームウェアの更新
```

### Block 34 (line 106)

```
         ファームウェアの更新
```

### Block 35 (line 108)

```
      グレーのボックス（上の緑色の矢印を参照）が、RCアプリに含まれている、またはバンドルされている最新のファームウェアバージョンを提供しているかどうかを確認します。
```

### Block 36 (line 110)

```
   3. そうでない場合は、「Select Firmware…」ボックスをクリックします。コンピューターに保存されている目的のファームウェアファイルに移動し、選択します。
```

### Block 37 (line 112)

```
      更新プロセスの一環として、選択したファームウェアファイルは、FIRST/updates/Expansion Hub Firmwareというサブフォルダーに、Control HubまたはRCスマートフォンに保存されます。
```

### Block 38 (line 114)

```
      現在および古いファームウェアファイルは、
      `REV RoboticsのWebサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware/firmware-changelog>`__ にあります。
```

### Block 39 (line 117)

```
   4. 「Update to…」または「Update using…」というボックスをクリックします（上の緑色の矢印を参照）。
```

### Block 40 (line 120)

```
         :alt: ファームウェアの管理
```

### Block 41 (line 124)

```
         ファームウェアの管理
```

### Block 42 (line 126)

```
   5. 確認プロンプトで、青色のボックス「Update Hub Firmware」をクリックします。
      プロセスが完了するまで待ちます。Hubのプラグを抜いたり、ロボットを再起動したりしないでください。
```

### Block 43 (line 129)

```
   以上です！Hubのファームウェアが更新されました。
```

### Block 44 (line 133)

```
   1. DSアプリのSettingsメニューから（Android デバイスのWi-Fi設定では決して使用しない）、DSアプリをControl HubまたはRCスマートフォンに接続します。
```

### Block 45 (line 135)

```
   2. DSアプリのメニューから、「Program and Manage」を選択します。次に、右上の3本のバーをタッチし、「Manage」を選択します。
```

### Block 46 (line 137)

```
      これは、ラップトップブラウザに表示されるのと同じ管理ページです。したがって、以下の手順は上記の方法4と類似しています。
```

### Block 47 (line 139)

```
   3. Update REV Hub Firmwareまでスクロールします。
```

### Block 48 (line 142)

```
         :alt: Hubファームウェアの更新
```

### Block 49 (line 146)

```
         Hubファームウェアの更新
```

### Block 50 (line 148)

```
      グレーのボックス「Update to…」が、DSアプリに含まれている、またはバンドルされている最新のファームウェアバージョンを提供しているかどうかを確認します。
```

### Block 51 (line 150)

```
   3. そうでない場合は、目的のファームウェアファイルを **Driver
      Stationデバイス** に転送できます。
```

### Block 52 (line 153)

```
      はい、それは正しいです：RCデバイスではなく、DSデバイスに転送します。
      この方法5では、DSデバイス上のローカルファイルを使用しますが、方法2および3
      （上記）では、RCデバイス上のローカルファイルを使用します。
```

### Block 53 (line 157)

```
      USBデータケーブル（充電専用ケーブルではない）を使用して、ファームウェアファイルをDSデバイスのDownloadsフォルダーに保存します。
```

### Block 54 (line 159)

```
      現在および古いファームウェアファイルは、REV Robotics
      のWebサイトの
      `こちら <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware/firmware-changelog>`__ にあります。
```

### Block 55 (line 163)

```
      次に、「Select Firmware…」ボックスをクリックします。DSデバイスの
      Downloadsフォルダーに移動し、目的のファームウェアファイルを選択します。
```

### Block 56 (line 166)

```
   4. 「Update to…」または「Update using…」というボックスをクリックします（上の2番目の緑色の矢印）。
```

### Block 57 (line 169)

```
         :alt: Hubファームウェアの更新
```

### Block 58 (line 173)

```
         Hubファームウェアの更新
```

### Block 59 (line 175)

```
   5. 確認プロンプトで、下にスクロールして青色のボックス「Update Hub Firmware」をクリックします。プロセスが完了するまで待ちます。Hubのプラグを抜いたり、ロボットを再起動したりしないでください。
```

### Block 60 (line 177)

```
   以上です！Hubのファームウェアが更新されました。
```

### Block 61 (line 179)

```
質問、コメント、修正は westsiderobotics@verizon.net まで
```


## ftc_sdk/updating/index.rst

### Block 1 (line 2)

```
   :title: FTC制御システムのコンポーネント更新
   :description: FIRST Tech Challenge制御システムの主要コンポーネントを更新するための包括的なガイド
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, 制御システム, 更新
```

### Block 2 (line 6)

```
制御システムのコンポーネント更新
```

### Block 3 (line 9)

```
**FIRST Tech Challenge** 制御システムの特定のコンポーネントは、定期的に更新を受け取ります。チームは、制御システムの各コンポーネントを最新のリリースバージョンに更新するようにしてください。
```

### Block 4 (line 15)

```
    REV Hardware Clientの更新 <hardware_client/Updating-REV-Hardware-Client>
    Driver Stationアプリの更新 <ds_app/Updating-the-DS-App>
    Robot Controllerアプリの更新 <rc_app/Updating-the-RC-App>
    Driver Hub OSの更新 <driverhub_os/Updating-the-Driver-Hub-OS>
    Control Hub OSの更新 <controlhub_os/Updating-the-Control-Hub-OS>
    Hubファームウェアの更新 <hub_firmware/Updating-Hub-Firmware>
```


## ftc_sdk/updating/rc_app/Updating-the-RC-App.rst

### Block 1 (line 1)

```
**Robot Controller (RC)** アプリの更新
```

### Block 2 (line 4)

```
**Robot Controller** アプリは、**FIRST** **Tech Challenge**:doc:`ソフトウェア開発キット（SDK）</ftc_sdk/overview/index>` で提供されているアプリの1つです。**Robot Controller** アプリは、**Robot Controller** **Android** デバイス（**REV Control Hub** または承認された**Android**RC スマートフォン）で実行されるアプリケーションです。このアプリは**Driver Station** アプリと通信してロボットを制御します。
```

### Block 3 (line 6)

```
このページでは、以下のデバイスで **Robot Controller (RC)** アプリを更新する方法を説明します：
```

### Block 4 (line 9)

```
-  承認された **Android** RC スマートフォン
```

### Block 5 (line 11)

```
**Blocks**/**OnBot Java** 対**Android Studio**
```

### Block 6 (line 17)

```
**Robot Controller (RC)** アプリには、**Blocks** と**OnBot Java** のプログラミング環境が含まれており、これらの環境を使用して開発されたユーザープログラム（チームコード）は、RC アプリとは独立して、RC アプリと並行して保存されます。これにより、チームコードに影響を与えることなく、RC アプリを独立して更新することが可能になります。RC アプリ自体をアップグレード/ダウングレードするために*コード*を変更する必要がないため、RC アプリソフトウェアの更新が非常に簡単になります。ただし、これは **Blocks** と**OnBot Java** のユーザーがアプリに同梱されている「デフォルト」の RC アプリ依存関係に制限されることを意味します。ただし、**Blocks** と**OnBot Java** プログラムは**Android Studio** でビルドされた RC アプリでも実行できるため、上級ユーザーにとってはこの点でまだある程度の柔軟性があります。
```

### Block 7 (line 22)

```
**Android Studio** は、一般的に正反対の動作をします。**FtcRobotController** リポジトリ（**Android Studio** プロジェクト）には、完全な RC アプリをビルドするために必要な完全なソースコードが含まれています。**Android Studio** プロジェクトがコンパイルおよびデプロイされると、実際には完全な**Robot Controller** アプリをビルドして、RC**Android** デバイスにインストールしています。チームコード** と** **Robot Controller** コードは*一緒に*コンパイルされます。つまり、チームコードは RC アプリ内に埋め込まれており、RC アプリとは独立して更新/編集することはできません。**Android Studio** でデプロイされた RC アプリが**REV Hardware Client** または類似のプロセスを使用して置き換えられた場合、チームコードが埋め込まれた RC アプリは削除され、デフォルトの RC アプリに置き換えられます。したがって、**Android Studio** ユーザーは**Android Studio** 以外を使用して RC アプリを更新しないでください！ただし、これによりソフトウェアのアップグレードとダウングレードが複雑になる可能性があります。**Android Studio** コードの RC アプリ部分をアップグレード/ダウングレードするには、チームの :doc:`Android Studio プロジェクト <../../../programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub>` を、使用したい**Robot Controller** アプリのバージョンに対応する `FtcRobotController リポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ コードのソフトウェアリリースと適切にマージする必要があります。**Android Studio** の使用を決定する際には、これを慎重に検討する必要があります。
```

### Block 8 (line 24)

```
**Android Studio** 向けの RC アプリの更新
```

### Block 9 (line 27)

```
**Android Studio** ユーザーは、上記の理由により、このページの手順を使用して RC アプリを更新** しないでください**。**Android Studio** ユーザーは、**Android Studio** プロジェクトが `SDK GitHub リポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ の希望するバージョンで最新であることを確認する必要があります。
```

### Block 10 (line 29)

```
GitHub を使用して更新できる **Android Studio** プロジェクトを適切に作成および維持する方法については、:doc:`GitHub の Fork と Clone の使用 <../../../programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub>` を参照してください。
```

### Block 11 (line 31)

```
**Blocks**/**OnBot Java** 向けの RC アプリの更新
```

### Block 12 (line 34)

```
これらの手順は、独立した更新がサポートされている状況、つまり **Blocks** または**OnBot Java** 開発で RC アプリを独立して更新するためのものです。お使いの**Robot Controller** ハードウェアに適用される以下の手順を展開してください：
```

### Block 13 (line 38)

```
   **REV Control Hub** の RC アプリを更新する方法は3つあります：
```

### Block 14 (line 41)

```
   #. コンピューター上の Manage ページ
   #. DS スマートフォンまたは Driver Hub 上の Manage ページ
```

### Block 15 (line 45)

```
      「サイドローディング」は可能ですが、**Control Hub** では追加の機器が必要な煩雑な手順が必要なため、ここでは説明しません。
```

### Block 16 (line 49)

```
      USB データケーブルを使用して、**REV Control Hub** の USB-C ポートを Windows コンピューターに接続します。RHC の「Hardware」タブが左上でアクティブになっていることを確認してください。
```

### Block 17 (line 51)

```
      :doc:`REV Hardware Client の更新 </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>` で、必要な DS 更新ファイルが以前にダウンロードされているため、ここではコンピューターをインターネットに接続する必要はありません。
```

### Block 18 (line 53)

```
      RHC アプリは、次に示すように **Control Hub** を認識します：
```

### Block 19 (line 56)

```
         :alt: Control Hub を認識
```

### Block 20 (line 60)

```
         **Control Hub** を認識
```

### Block 21 (line 62)

```
      認識されたら、**Control Hub** の大きなアイコン/長方形をクリックします。RHC アプリは、RC アプリの更新ステータス（ある場合）を表示します。
```

### Block 22 (line 65)

```
         :alt: Control Hub を更新
```

### Block 23 (line 69)

```
         **Control Hub** を更新
```

### Block 24 (line 71)

```
      青い Update 長方形（緑色の矢印）をクリックするだけです – 完了！
```

### Block 25 (line 75)

```
      1. ラップトップをインターネットに接続し、Web ブラウザーを開いて、`SDK GitHub リポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に移動します。
```

### Block 26 (line 78)

```
            :alt: SDK GitHub リポジトリ
```

### Block 27 (line 82)

```
            SDK GitHub リポジトリ
```

### Block 28 (line 84)

```
         右側の「Releases」の下にある「Latest」アイコン（上の黄色の楕円）をクリックします。
```

### Block 29 (line 86)

```
         次のページで、「Latest」セクションを少し下にスクロールして、「Assets」の短いリストを表示します。「FtcRobotController-release.apk」ファイルをクリックして、コンピューターにダウンロードします。
```

### Block 30 (line 89)

```
            :alt: SDK GitHub リリース
```

### Block 31 (line 93)

```
            SDK GitHub リリース
```

### Block 32 (line 95)

```
         この時点で、現在のバージョン番号を反映するようにファイルの名前を変更できます。たとえば、``FtcRobotController-release-8.0.apk`` または単に``RC-8.0-release.apk`` です。これにより、その RC スマートフォンに後で保存される可能性のある他のバージョンとファイルを区別できます。
```

### Block 33 (line 97)

```
      2. **Control Hub** の電源を入れ（ロボットの電源を投入）、緑色の LED が点灯するまで待ちます。
```

### Block 34 (line 99)

```
      3. 同じラップトップを Wi-Fi 経由で **Control Hub** に接続します。Chrome ブラウザーを開き、通常のアドレス ``http://192.168.43.1:8080`` を入力します。
```

### Block 35 (line 101)

```
         Manage タブをクリックし、「Update Robot Controller App」まで下にスクロールします。
```

### Block 36 (line 104)

```
            :alt: RC アプリを更新
```

### Block 37 (line 108)

```
            RC アプリを更新
```

### Block 38 (line 110)

```
         「Select App…」をクリックします。RC APK ファイルが保存されているラップトップフォルダーに移動し、そのファイルを選択します。
```

### Block 39 (line 112)

```
         次に、「Update」ボタン（上の緑色の矢印）をクリックします。
```

### Block 40 (line 114)

```
         ソフトウェアは、既存の RC アプリを新しい更新された RC アプリに置き換えます。ラップトップと **Control Hub** 間の接続は一時的に失われ、その後自動的に復元されます。
```

### Block 41 (line 116)

```
      完了メッセージが表示されたら、更新された RC アプリが使用できる状態になります。
```

### Block 42 (line 120)

```
      この方法は、コンピューターが利用できない場合、または Wi-Fi 経由で **Control Hub** に接続できない場合に使用できます。たとえば、デスクトップコンピューターには有線（Ethernet）ネットワークポートしかなく、Wi-Fi がない場合があります。
```

### Block 43 (line 122)

```
      ただし、この方法では、RC APK ファイルを **Driver Hub** または DS スマートフォンの Download（または Downloads）フォルダーに保存する必要があります。つまり、**Driver Station** デバイスに保存された**Robot Controller APK** です。
```

### Block 44 (line 124)

```
      まず、方法2の手順1に示すように、GitHub リポジトリからコンピューターに RC APK ファイルをダウンロードします。次に、USB データケーブルを使用して、その APK ファイルをコンピューターから DS デバイスの Download フォルダーに転送します。完了したら、DS デバイスをコンピューターから抜くことができます。
```

### Block 45 (line 126)

```
      DS アプリを **Control Hub** に接続します。DS アプリの Settings メニューから（**Android** デバイスの Wi-Fi 設定では決して接続しないでください）。
```

### Block 46 (line 128)

```
      DS アプリのメニューから「Program and Manage」を選択します。次に、右上の3本のバーをタッチし、「Manage」を選択します。
```

### Block 47 (line 130)

```
      これは、ラップトップブラウザーに表示されるのと同じ Manage ページです。したがって、以下の手順は、上記の方法2と同じです。
```

### Block 48 (line 132)

```
      「Update Robot Controller App」まで下にスクロールします。
```

### Block 49 (line 135)

```
         :alt: RC アプリを更新
```

### Block 50 (line 139)

```
         RC アプリを更新
```

### Block 51 (line 141)

```
      「Select App…」をタッチします。DS デバイスの Download フォルダーに移動し、最新の RC APK ファイルを選択します。
```

### Block 52 (line 143)

```
      次に、「Update」ボタン（上の緑色の矢印）をタッチします。
```

### Block 53 (line 145)

```
      ソフトウェアは、既存の RC アプリを新しい更新された RC アプリに置き換えます。**Driver Station** と**Control Hub** 間の接続は一時的に失われ、その後自動的に復元されます。
```

### Block 54 (line 147)

```
      完了メッセージが表示されたら、更新された RC アプリが使用できる状態になります。
```

### Block 55 (line 151)

```
   **Robot Controller (RC)** スマートフォンの RC アプリを更新する方法は2つあります：
```

### Block 56 (line 154)

```
   2. APK による「サイドローディング」
```

### Block 57 (line 157)

```
      コンピューターまたは **Driver Station** デバイス上の Program and Manage の下の Manage ページでは、接続された**Robot Controller** スマートフォンの RC アプリの更新は** 提供されません** 。
```

### Block 58 (line 161)

```
      RHC がインストールされて開いているコンピューターに、RC スマートフォンを直接接続します。USB データケーブルを使用してください（充電専用ケーブルではありません）。「Hardware」タブが左上でアクティブになっていることを確認してください。RC スマートフォンの RC アプリは開いている必要は**ありません** 。
```

### Block 59 (line 163)

```
      :doc:`REV Hardware Client の更新 </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>` で、必要な DS 更新ファイルが以前にダウンロードされているため、ここではコンピューターをインターネットに接続する必要はありません。
```

### Block 60 (line 165)

```
      RHC アプリは、次に示すようにスマートフォンを認識します：
```

### Block 61 (line 168)

```
         :alt: スマートフォンを認識
```

### Block 62 (line 172)

```
         スマートフォンを認識
```

### Block 63 (line 174)

```
      スマートフォンが認識されない場合は、スマートフォンに :doc:`開発者オプション </programming_resources/tutorial_specific/android_studio/enabling_developer_options/Enabling-Developer-Options>` が有効になっていることを確認してください。必要に応じて、REV Hardware Client アプリの左下にある「Scan for Devices」ボタンをクリックして、RHC にデバイスの再スキャンを強制します。
```

### Block 64 (line 176)

```
      認識されたら、そのスマートフォンの大きなアイコン/長方形をクリックします。RHC アプリは、DS アプリの更新ステータス（ある場合）を表示します。
```

### Block 65 (line 179)

```
         :alt: スマートフォンの更新ステータス
```

### Block 66 (line 183)

```
         スマートフォンの更新ステータス
```

### Block 67 (line 185)

```
      青い Update 長方形（緑色の矢印）をクリックするだけです – 完了！
```

### Block 68 (line 187)

```
      更新は高速でした。RC アプリが既に RHC にダウンロードされていたためです。これは、青い Update 長方形の左側に「(Already Downloaded)」と記載されていました。
```

### Block 69 (line 189)

```
      青い Update 長方形のすぐ上のドロップダウンリストで、RC アプリの**古い** バージョンを選択することもできます。
```

### Block 70 (line 191)

```
      インストール後、RC アプリアイコンをメニューからスマートフォンのホーム画面にドラッグします。
```

### Block 71 (line 193)

```
      RC スマートフォンをコンピューターから抜き、RHC アプリを閉じることができます。更新された RC アプリが使用できる状態になります。
```

### Block 72 (line 197)

```
      ここでは、**Android Package** または**APK ファイル** を直接操作して、**Android** スマートフォンに RC アプリをインストールします。PC または Mac、古いまたは新しいコンピューターを使用できます。この方法は「サイドローディング」と呼ばれることがあります。
```

### Block 73 (line 199)

```
      1. コンピューターをインターネットに接続し、Web ブラウザーを開いて、`SDK GitHub リポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ に移動します。
```

### Block 74 (line 202)

```
            :alt: SDK GitHub リポジトリ
```

### Block 75 (line 206)

```
            SDK GitHub リポジトリ
```

### Block 76 (line 208)

```
         右側の「Releases」の下にある「Latest」アイコン（上の黄色の楕円）をクリックします。
```

### Block 77 (line 210)

```
         次のページで、「Latest」セクションを少し下にスクロールして、「Assets」の短いリストを表示します。「FtcRobotController-release.apk」ファイルをクリックして、コンピューターにダウンロードします。
```

### Block 78 (line 213)

```
            :alt: SDK GitHub リリース
```

### Block 79 (line 217)

```
            SDK GitHub リリース
```

### Block 80 (line 219)

```
         この時点で、現在のバージョン番号を反映するようにファイルの名前を変更できます。たとえば、``FtcRobotController-release-8.0.apk`` または単に``RC-8.0-release.apk`` です。これにより、その RC スマートフォンに後で保存される可能性のある他のバージョンとファイルを区別できます。
```

### Block 81 (line 221)

```
      2. APK ファイルをコンピューターから RC スマートフォンの Downloads（または Download）フォルダーに転送します。USB データケーブルを使用してください（充電専用ケーブルではありません）。完了したら、RC スマートフォンをコンピューターから抜くことができます。
```

### Block 82 (line 223)

```
      3. 既存の（古い）RC アプリをアンインストールするには、そのアイコンをゴミ箱/アンインストールアイコンにドラッグします。または、RC アイコンをタッチして長押しして「App info」を表示し、Uninstall を選択します。
```

### Block 83 (line 225)

```
      4. RC スマートフォンで、Downloads フォルダーに移動します。これはいくつかの方法で実行できます：
```

### Block 84 (line 227)

```
         -  メインアプリメニュー（上にスワイプ）で、Files アイコンまたは Downloads アイコン（存在する場合）をタッチします
         -  Settings/Storage の基本ファイルマネージャーを使用します：Explore または Files をタッチします
         -  FX File Explorer などのサードパーティアプリを使用します（Google Play ストアから）
```

### Block 85 (line 231)

```
         転送した APK ファイル名をタッチします。プロンプトに応答して、更新された RC アプリをインストールします。
```

### Block 86 (line 233)

```
         インストール後、RC アプリアイコンをアプリメニューから RC スマートフォンのホーム画面にドラッグします。
```

### Block 87 (line 235)

```
      完了！更新された RC アプリが使用できる状態になります。
```

### Block 88 (line 237)

```
RC アプリの更新に関する他の説明は、`REV Robotics の優れたドキュメントサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-robot-controller-application>`__ にあります。
```

### Block 89 (line 239)

```
質問、コメント、修正は westsiderobotics@verizon.net までお願いします。
```


## gracious_professionalism/gp.rst

### Block 1 (line 4)

```
*Gracious Professionalism®* は *FIRST* の精神の一部です。これは、高品質な仕事を奨励し、他者の価値を強調し、個人とコミュニティを尊重する行動様式です。*Gracious Professionalism* は意図的に明確に定義されていません。それは、すべての人にとって異なる意味を持つべきだからです。
```

### Block 2 (line 6)

```
*Gracious Professionalism* の可能な意味には、次のようなものがあります：
```

### Block 3 (line 8)

```
*  礼儀正しい態度と行動はwin-winです、
*  礼儀正しい人々は他者を尊重し、その尊重を行動で示します、
*  プロフェッショナルは特別な知識を持ち、その知識を責任を持って使用することを社会から信頼されています、そして
*  礼儀正しいプロフェッショナルは、他者にとっても自分自身にとっても心地よい方法で価値ある貢献をします。
```

### Block 4 (line 13)

```
*FIRST* の文脈において、これは次のことを意味します：
```

### Block 5 (line 15)

```
*  強力な競争相手になることを学びながらも、そのプロセスにおいて互いを尊重と親切さで扱い、そして
*  誰もが除外されたり、過小評価されたりしていると感じることがないようにします。
```

### Block 6 (line 18)

```
知識、プライド、共感が心地よく、そして真摯に融合されるべきです。最終的に、*Gracious Professionalism* は有意義な人生を追求することの一部です。プロフェッショナルが知識を礼儀正しい方法で使用し、個人が誠実さと感受性を持って行動するとき、全員が勝利し、社会が恩恵を受けます。
```

### Block 7 (line 30)

```
   *FIRST の精神は、すべての人を価値あるものとして扱う方法で、高品質で十分な情報に基づいた仕事を行うことを奨励します。Gracious Professionalism は、FIRST の精神の一部を表す良い表現のようです。それは、FIRST を異なるものにし、素晴らしいものにしている一部です。*
```

### Block 8 (line 32)

```
   - Dr. Woodie Flowers, (1943 – 2019), Distinguished Advisor to *FIRST* / *FIRST* 特別顧問
```

### Block 9 (line 34)

```
このコンセプトをチームと一緒に検討し、定期的に強化することは良いアイデアです。競技で後に対戦する相手チームに貴重な資材や専門知識を貸し出すなど、*Gracious Professionalism* を実践する実際の例をチームに提供することをお勧めします。イベントで *Gracious Professionalism* を表示する機会を定期的に強調し、チームメンバーがこの資質を自分自身や地域貢献活動を通じて示す方法を提案するよう奨励してください。
```

### Block 10 (line 36)

```
追悼
```

### Block 11 (line 39)

```
2019年10月、デザインとエンジニアリング教育の革新者であり、*FIRST* の特別顧問およびミッションの支援者であったDr. Woodie Flowers が逝去されました。世界中からWoodieへの心からの追悼が数千寄せられており、彼の遺産がコミュニティの礼儀正しい性質と、教育者に力を与え、グローバルシチズンを育成するという私たちの継続的なコミットメントを通じて、永遠に生き続けることは明らかです。
```


## hardware_and_software_configuration/configuring/configuring_color_sensor/configuring-color-sensor.rst

### Block 1 (line 1)

```
カラー距離センサーの構成
```

### Block 2 (line 4)

```
**REV Robotics カラー距離センサー** は I2C センサーです。実際には、2 つのセンサー機能を 1 つのデバイスに組み合わせています。これは、物体の色を判定できるカラーセンサーです。また、短距離を測定するために使用できる距離またはレンジセンサーでもあります。このチュートリアルでは、「distance（距離）」という言葉が「range（範囲）」という言葉と同じ意味で使用されていることに注意してください。
```

### Block 3 (line 6)

```
カラー距離センサーの構成手順
```

### Block 4 (line 9)

```
1. 画面の **I2C Bus 0** という言葉をタッチして、この I2C バスの I2C 構成画面を起動します。
```

### Block 5 (line 16)

```
**Control Hub** または**Expansion Hub** には、「0」から「3」とラベル付けされた 4 つの独立した I2C バスがあります。この例では、カラーセンサーを「0」とラベル付けされたポートに接続したため、I2C バス 0 に配置されます。
```

### Block 6 (line 18)

```
2. **I2C Bus 0** 画面を見てください。このバス用に既に構成されているセンサーがあるはずです。**Control Hub** または**Expansion Hub** には、独自の内蔵慣性測定ユニット（IMU）センサーがあります。このセンサーは、ロボットの方向を決定したり、ロボットの加速度を測定したりするために使用できます。
```

### Block 7 (line 25)

```
内蔵 IMU は、各 **Control Hub** または**Expansion Hub** の I2C バス 0 に内部的に接続されています。**Robot Controller** を使用して**Control Hub** または**Expansion Hub** を構成するたびに、アプリは I2C バス 0 の IMU を自動的に構成します。カラーセンサーを構成できるようにするには、このバス用に別の I2C デバイスを追加する必要があります。
```

### Block 8 (line 27)

```
3. **Add** ボタンを押して、このバスに別の I2C デバイスを追加します。
```

### Block 9 (line 34)

```
4. ドロップダウンセレクターから「REV Color/Range Sensor」を選択し、この新しいデバイスに名前を付けます。タッチスクリーンキーボードを使用して、このデバイスに「sensorColorRange」という名前を付けます。
```

### Block 10 (line 41)

```
5. **Done** ボタンを押して、I2C センサー構成を完了します。アプリは前の画面に戻るはずです。
```


## hardware_and_software_configuration/configuring/configuring_dc_motor/configuring-dc-motor.rst

### Block 1 (line 1)

```
DC モーターの構成
```

### Block 2 (line 4)

```
ファイルを作成したので、DC モーターを構成ファイルに追加する必要があります。
```

### Block 3 (line 8)

```
DC モーターの構成手順
```

### Block 4 (line 11)

```
1. 画面の **Motors** という単語をタッチして、モーター構成画面を表示します。
```

### Block 5 (line 18)

```
2. モーターを **Expansion Hub** のポート #0 に取り付けたので、ポート 0 のドロップダウンコントロールを使用して、モータータイプ（この例では Tetrix Motor）を選択します。
```

### Block 6 (line 25)

```
3. タッチスクリーンキーパッドを使用して、モーターの名前を指定します（この例では「motorTest」）。
```

### Block 7 (line 32)

```
4. **Done** ボタンを押して、モーター構成を完了します。アプリは前の画面に戻るはずです。
```


## hardware_and_software_configuration/configuring/configuring_digital_touch_sensor/configuring-digital-touch-sensor.rst

### Block 1 (line 1)

```
デジタルタッチセンサーの構成
```

### Block 2 (line 4)

```
**REV Robotics タッチセンサー** はデジタルセンサーです。**OpMode** は、タッチセンサーにクエリを実行して、ボタンが押されているかどうかを確認できます。
```

### Block 3 (line 6)

```
デジタルタッチセンサーの構成手順
```

### Block 4 (line 9)

```
1. 画面の **Digital Devices** をタップして、デジタル I/O 構成画面を表示します。
```

### Block 5 (line 16)

```
2. タッチスクリーンを使用して、ポート #1 に「REV Touch Sensor」を追加し、デバイスに「testTouch」という名前を付けます。
```

### Block 6 (line 23)

```
ポート #0 ではなくポート #1 でタッチセンサーを構成していることに注意してください。これは、標準の 4 線 JST センサーケーブルを使用して **REV Robotics タッチセンサー** をデジタルポートに接続すると、2 番目のデジタルピンが接続されるためです。最初のピンは接続されたままです。
```

### Block 7 (line 25)

```
3. **Done** ボタンを押して前の画面に戻ります。
```


## hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs.rst

### Block 1 (line 1)

```
Expansion Hub の追加
```

### Block 2 (line 4)

```
はじめに
```

### Block 3 (line 7)

```
単一の **REV Robotics Control Hub** または**Expansion Hub** には、限られた数の入出力（I/O）ポートしかありません。場合によっては、利用可能なポート数よりも多くのデバイスを使用したい場合があります。このような場合、最初の Hub に**Expansion Hub** を接続して、I/O ポートを追加する必要があるかもしれません。
```

### Block 4 (line 9)

```
このドキュメントでは、FIRST Tech Challenge で使用する追加の **Expansion Hub** を接続および構成する方法について説明します。FIRST Tech Challenge
競技マニュアルは、単一のロボット上の **Control Hub** または**Expansion Hub** の最大数を 2 つに制限しています。
```

### Block 5 (line 12)

```
必要な機器
```

### Block 6 (line 15)

```
このドキュメントの手順に従うには、次のアイテムが必要です。
```

### Block 7 (line 22)

```
   * - 必要なアイテム
     - 画像
```

### Block 8 (line 28)

```
   * - **REV Robotics** スイッチ、ケーブル、ブラケット（REV-31-1387）
```

### Block 9 (line 31)

```
   * - **REV Robotics** Tamiya to XT30 アダプターケーブル（REV-31-1382）
```

### Block 10 (line 34)

```
   * - **FIRST** 承認 12V バッテリー（Tetrix W39057 など）。
       **FIRST** 承認 12V バッテリーのリストについては、現在の競技マニュアルを参照してください。
```

### Block 11 (line 44)

```
   * - **REV Robotics** （または同等品）3 ピン JST PH ケーブル（REV-35-1414、3 本パックを表示していますが 1 本のみ必要）
```

### Block 12 (line 47)

```
   * - **REV Robotics** XT30 延長ケーブル（REV-31-1394）
```

### Block 13 (line 50)

```
**Expansion Hub** の接続
```

### Block 14 (line 53)

```
1. 最初のステップは、3 ピン JST PH ケーブルと XT30 ケーブルを使用して、
2 つの Hub をデイジーチェーン接続することです。これを行う前に、
どちらの Hub も電源が入っていないことを確認してください。
```

### Block 15 (line 57)

```
XT30 延長ケーブルを使用して、**Control Hub** の XT30 電源ポートを
もう一方の **Expansion Hub** の XT30 電源ポートに接続します。
```

### Block 16 (line 62)

```
2. **Control Hub** と**Expansion Hub** は、デバイス間の通信に RS-485 シリアルバス標準を使用します。
3 ピン JST PH ケーブルを使用して、**Control Hub** の「RS485」とラベル付けされたポートの 1 つを、
**Expansion Hub** の「RS485」とラベル付けされたポートの 1 つに接続できます。
```

### Block 17 (line 68)

```
**Expansion Hub** または**Control Hub** でどの「RS485」ポートを選択するかは重要ではありません。
どちらのポートでも機能するはずです。
```

### Block 18 (line 75)

```
3. 2 つのデバイスをデイジーチェーン接続したら（12V 電源と RS-485 信号）、
バッテリーと電源スイッチを接続し、デバイスの電源を入れることができます。
```

### Block 19 (line 80)

```
両方のデバイスの構成
```

### Block 20 (line 83)

```
**Expansion Hub** と**Control Hub** をデイジーチェーン接続できた場合、
両方のデバイスを含む新しい構成ファイルを作成できるはずです。
```

### Block 21 (line 86)

```
**注：** **Control Hub** のみを含む構成が既にある場合は、構成を編集して
「Scan」ボタンを押すことで **Expansion Hub** を追加できます。
```

### Block 22 (line 89)

```
**Driver Hub** を**Control Hub** の WiFi ネットワークに接続し、**Driver Station** アプリから
Configure Robot オプションを選択します。**New** ボタンを押して、新しい構成ファイルを作成します。
最初にハードウェアをスキャンすると、**Robot Controller** は組み込みの**Control Hub** を検出するはずです。
**Robot Controller** は、このデバイスに自動的に**Control Hub** 「Portal」とラベル付けします。
**Robot Controller** は、このポータルを介して個々の Hub と通信します。
```

### Block 23 (line 98)

```
構成画面の Portal アイテムをクリックすると、**Control Hub** と**Expansion Hub** の
両方がリストされているはずです。
```

### Block 24 (line 103)

```
この構成ファイルを保存して、**Driver Station** のメイン画面に戻ることができます。
ロボットが再起動された後、両方の Hub の LED が緑色に点灯するはずです。
**Expansion Hub** では、LED が約 5 秒ごとに青色に点滅するはずです。
```

### Block 25 (line 107)

```
おめでとうございます。**Control** と**Expansion Hub** の組み合わせを使用する準備が整いました！
これらの Hub を個々の Hub と同じように構成および操作できます。
```

### Block 26 (line 113)

```
**Control Hub** にアクセスできないチームは、ロボットで 2 つの**Expansion Hub** を使用できます。
```

### Block 27 (line 118)

```
ロボットで **Control Hub** を使用していないチームには、いくつかの追加機器が必要です。
```

### Block 28 (line 125)

```
   * - 必要なアイテム
     - 画像
```

### Block 29 (line 128)

```
   * - **FIRST** 承認の Android スマートフォンで、**FTC Robot Controller**
       アプリがインストールされているもの。**FIRST** 承認の Android スマートフォンのリストについては、
       現在の競技マニュアルを参照してください。
```

### Block 30 (line 133)

```
   * - USB Type A オス - Type mini-B オスケーブル
```

### Block 31 (line 136)

```
   * - Micro USB OTG アダプター
```

### Block 32 (line 139)

```
   * - 追加の **REV Robotics Expansion Hub** （REV-31-1153）
```

### Block 33 (line 148)

```
**重要な注意：** 両方の**Expansion Hub** が同じアドレスを持っている場合、
または箱から取り出したばかりの場合（デフォルトでは、アドレスは 2 に設定されています）、
それらを接続する _前に_ 一方のアドレスを変更する必要があります。
このガイドでは、2 番目の **Expansion Hub** を接続する前に、
最初の **Expansion Hub** のアドレスを設定することを前提としています。
```

### Block 34 (line 154)

```
最初の **Expansion Hub** を 12V バッテリーと**Robot Controller** に接続した状態で、
**Robot Controller** アプリから**Settings** メニューを起動します（**DRIVER STATION** が
**Robot Controller** とペアリングされている場合は、**Driver Station** アプリからこれを行うこともできます）。
```

### Block 35 (line 158)

```
1. **Advanced Settings** アイテムを選択して、Advanced Settings メニューを表示します。
```

### Block 36 (line 163)

```
2. 次に、**Expansion Hub Address Change** アイテムを選択して、
**Expansion Hub** アドレス画面を表示します。
```

### Block 37 (line 169)

```
3. **Expansion Hub** の USB シリアル番号と現在割り当てられているアドレスが表示されるはずです。
```

### Block 38 (line 171)

```
**重要な注意：** 物理的に接続され、電源が入っている**Expansion Hub** が表示されない場合、
アドレスの競合がある可能性があります。これが発生した場合は、
アドレスを変更したい Hub 以外のすべての **Expansion Hub** を切断してください。
```

### Block 39 (line 178)

```
4. 右側のドロップダウンリストコントロールを使用して、**Expansion Hub** の
アドレスを変更します。現在接続されている他の **Expansion Hub** と競合するアドレスは
使用できません。
```

### Block 40 (line 194)

```
5. Hub の 1 つのアドレスを変更した後、3 ピン JST PH ケーブルと XT30 ケーブルを使用して、
2 つの Hub をデイジーチェーン接続できます。これを行う前に、
最初の **Expansion Hub** から 12V バッテリーと電源スイッチを切断してください。
```

### Block 41 (line 198)

```
XT30 延長ケーブルを使用して、一方の **Expansion Hub** の XT30 電源ポートを
もう一方の Hub の XT30 電源ポートに接続します。
```

### Block 42 (line 220)

```
**Robot Controller** を接続し、デバイスの電源を入れます。
```

### Block 43 (line 228)

```
2 つの **Expansion Hub** をデイジーチェーン接続できた場合、
両方のデバイスを含む新しい構成ファイルを作成できるはずです。
```

### Block 44 (line 231)

```
**注：** USB 接続された**Expansion Hub** のみを含む構成が既にある場合は、
構成を編集して「Scan」ボタンを押すことで、2 番目の **Expansion Hub** を追加できます。
```

### Block 45 (line 246)

```
構成画面の Portal アイテムをクリックすると、2 つの **Expansion Hub** がリストされているはずです。
それぞれのデフォルトのデバイス名の一部として、それぞれのアドレスが表示されます。
```

### Block 46 (line 256)

```
おめでとうございます。デュアル **Expansion Hub** を使用する準備が整いました！
これらの Hub を個々の Hub と同じように構成および操作できます。
```


## hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam.rst

### Block 1 (line 2)

```
Control Hubで外部Webカメラを設定する方法
```

### Block 2 (line 6)

```
はじめに
```

### Block 3 (line 9)

```
**競技マニュアル** では、コンピュータビジョン関連のタスクにUSB Video Class（UVC）対応カメラの使用が認められています。
**REV Robotics Control Hub** を使用する場合、内蔵カメラが搭載されていないため、外部Webカメラを利用する必要があります。
このドキュメントでは、Control Hubに外部Webカメラを接続・設定し、使用する方法について説明します。
```

### Block 4 (line 13)

```
本ドキュメント作成にご協力いただいたWestside Robotics（ロサンゼルス）のChris Johannesen氏に感謝します。
```

### Block 5 (line 16)

```
外部カメラの種類
```

### Block 6 (line 19)

```
理論上、USB Video Class（UVC）対応カメラはどれでも動作しますが、**FIRST** ではLogitech製UVC Webカメラの使用を推奨しています。
以下のカメラはSDKソフトウェアで動作確認・キャリブレーション済みです：
```

### Block 7 (line 26)

```
UVCカメラのキャリブレーションは任意の高度な作業です。キャリブレーションファイルの作成方法は、
```

### Block 8 (line 28)

```
のコメント欄に記載されています（オンライン版は`こちら <https://github.com/ftctechnh/ftc_app/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__）。
```

### Block 9 (line 31)

```
カメラの接続方法
```

### Block 10 (line 34)

```
UVCカメラは**REV Control Hub** のUSB 3.0ポートに直接接続できます。**REV Robotics Expansion Hub** とは異なり、外部電源付きUSBハブは不要です。
```

### Block 11 (line 37)

```
   :alt: Control HubにUVCカメラを接続した様子。
```

### Block 12 (line 41)

```
   **REV Control Hub** には、USB 2.0ポートに接続したデバイスによる
   `ESD問題 <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system#esd-mitigation-techniques>`__
   が報告されています。
   USB 2.0ポートを使用すると、ESDがWi-Fiチップに影響し、**Driver Hub** とのWi-Fi接続が切れることがあります。
   カメラなどのUSB機器は必ずUSB 3.0ポートに接続してください。
```

### Block 13 (line 47)

```
2台のWebカメラを接続したい場合は「`カメラとUSBハブ <#cameras-and-usb-hubs>`__」をご参照ください。
```

### Block 14 (line 50)

```
カメラの構成
```

### Block 15 (line 53)

```
外部カメラを使用する前に、USB接続デバイスとしてアクティブな構成ファイルに追加する必要があります。
```

### Block 16 (line 55)

```
ペアリング済みの**DRIVER STATION** 端末で「Configure Robot」メニューを使用し、WebカメラをUSB接続デバイスとして既存または新規の構成ファイルに追加してください。
「Scan」操作でWebカメラが検出され、デフォルト名「Webcam 1」が割り当てられます。
```

### Block 17 (line 59)

```
   :alt: ScanボタンとWebcam 1が表示された画面。
```

### Block 18 (line 61)

```
このデフォルト名のままでも（サンプル**OpMode** はこの名前を参照します）、変更しても構いません。名前を変更した場合は、**OpMode** 内で新しい名前を参照するようにしてください。
```

### Block 19 (line 64)

```
サンプルOpMode
```

### Block 20 (line 67)

```
構成ファイルが保存・有効化されると、外部UVCカメラを使ったロボットビジョンのプログラムが可能になります。
```

### Block 21 (line 69)

```
SDKソフトウェアには、外部UVCカメラを**VisionPortal** で利用するための「webcam」版サンプル**Blocks** およびJava**OpMode** が用意されています。
```

### Block 22 (line 72)

```
   :alt: Webカメラ初期化のBlocksコード。
```

### Block 23 (line 74)

```
**OpMode** を編集する前に、カメラを含む構成が有効になっていること、**OpMode** で参照するカメラ名が構成ファイルの名前と一致していることを確認してください。
```

### Block 24 (line 79)

```
画像プレビュー
```

### Block 25 (line 82)

```
**FIRST Tech Challenge** アプリでは、**VisionPortal** を使った「ストリーム対応**OpMode**」でカメラプレビューが可能です。
```

### Block 26 (line 84)

```
ペアリング済みの**DRIVER STATION** 端末でカメラを接続・構成した状態で、ストリーム対応**OpMode** を選択します。INITボタンを押して、ストリーミングソフトウェアの初期化を待ちます（STARTボタンは押さないでください）。
画面右上のメニュー（三点アイコン）から「Camera Stream」を選択します。このオプションはこのタイミングのみ表示され、ゲームパッドやSTARTボタンは安全のため無効化されます。
```

### Block 27 (line 88)

```
   :alt: Camera Streamオプションが表示されたDriver Station画面。
```

### Block 28 (line 90)

```
カメラ画像が**DRIVER STATION** 画面に表示されます。画像を手動でタッチすると更新されます。帯域を節約するため、1フレームずつ送信されます。
```

### Block 29 (line 93)

```
   :alt: カメラ画像が表示されたDriver Station画面。
```

### Block 30 (line 95)

```
この機能を使ってカメラの調整が可能です。調整が終わったら、メニューから再度「Camera Stream」を選択してプレビューを終了します。プレビュー画像が閉じ、ゲームパッドが有効化され、STARTボタンを押して**OpMode** を実行できます。
```

### Block 31 (line 98)

```
   :alt: Camera Streamオプションが表示されたDriver Station画面。
```

### Block 32 (line 103)

```
   :alt: waitForStart前にWebカメラのINITコードが呼ばれているBlocksコード。
```

### Block 33 (line 105)

```
メインメニューにCamera Streamオプションが表示されない場合は、**OpMode** 内で**VisionPortal** が**waitForStart** 前に有効化されているか、VisionPortalソフトウェアの初期化に十分な時間を確保しているか確認してください。
```

### Block 34 (line 111)

```
**OpMode** 実行中にパソコンでカメラ映像を確認したい場合は、
`scrcpy <https://github.com/Genymobile/scrcpy>`__ を利用できます。
その際は、まず**Control Hub** とADB接続を確立する必要があります。
USB-A to USB-Cケーブルで**Control Hub** のUSB-Cポートに接続するか、Windowsの場合は**Control Hub** のWi-Fiネットワークに接続し、
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/gs/install>`__ を開いてください。
接続後、`こちらの手順 <https://github.com/Genymobile/scrcpy?tab=readme-ov-file#get-the-app>`__ でscrcpyをインストール・実行します。
```

### Block 35 (line 119)

```
   :alt: scrcpyでカメラ映像を表示した画面。
```

### Block 36 (line 122)

```
   **競技マニュアル** では、競技中に**DRIVER STATION** 以外のデバイスを**Control Hub** に接続することは禁止されています。
```

### Block 37 (line 125)

```
外部HDMIモニター
```

### Block 38 (line 128)

```
カメラ映像は、**REV Control Hub** のHDMIポートに接続したディスプレイモニター等でも表示できます。
```

### Block 39 (line 131)

```
   :alt: Control Hubに接続した外部HDMIモニターでカメラ映像を表示している様子。
```

### Block 40 (line 134)

```
   競技中に**Control Hub** へ接続することは禁止されています。
```

### Block 41 (line 137)

```
上級者向け情報
```

### Block 42 (line 140)

```
独自ストリームを作成したい上級者の方は、**Android Studio** の
`APIドキュメント <https://javadoc.io/doc/org.firstinspires.ftc>`__ を参照してください。
以下のクラスが参考になります：
```

### Block 43 (line 148)

```
カメラとUSBハブ
```

### Block 44 (line 151)

```
UVC Webカメラは**Control Hub** のUSB 3.0ポートに直接接続できます。
では、2台のWebカメラを使いたい場合はどうすればよいでしょうか？
例えば、ロボットが前方・後方両方を同時に見られるようにしたい場合などです。
USB 3.0ポートにUSBハブを追加することで、2台のWebカメラを接続できます。
これにより、USB 2.0ポートのESD問題も回避できます。
```

### Block 45 (line 159)

```
   ただし、Logitech C920のように消費電力が大きいWebカメラは、同時使用時にUSBポートから過剰な電力を消費する報告があります。
   C920を使う場合は電源付きUSBハブの利用を推奨します。
```

### Block 46 (line 162)

```
USBハブのもう一つの用途は、`Limelight 3A <https://limelightvision.io/products/limelight-3a>`__ カメラの接続です。
このデバイスは独自のプロセッサを搭載しており、**OpMode** が動作していない時でも常に電力を消費します。
電源付きUSBハブを使うことで、Limelightによるロボットバッテリーの消耗を防げます。
```

### Block 47 (line 166)

```
おすすめの電源付きUSBハブは「Acer ODK350 5-IN-1 USB 3.0 Hub」です。
USB Cポートから全ての接続機器に電力供給が可能です。
```

### Block 48 (line 171)

```
   すべてのUSBハブが電源付きとは限りません。
   一般的に、どのUSBポートにもモバイルバッテリーを接続できるわけではなく、電力供給専用ポートが必要です。
   電源付きUSBハブを探す際は、仕様欄に「*Note: This USB C port (with IN 5V printed) can not be used for data transfer and charge other devices. It can only supply power for the other 4 USB ports.*」のような記載があるか確認してください。
```

### Block 49 (line 176)

```
   :alt: 電源付きUSBハブと2台のWebカメラを接続したREV Control Hub。
```

### Block 50 (line 178)

```
   Acer ODK350 USBハブ
```

### Block 51 (line 180)

```
   USBハブは**Control Hub** のUSB 3.0ポートに接続します。
   USBハブのUSB Cポートにモバイルバッテリーを接続し、全ての機器に電力を供給します。
   2台のLogitech C920 WebカメラがUSBハブに接続されています。
```

### Block 52 (line 184)

```
2台のカメラを切り替えて**AprilTag** を検出するサンプルプログラムは、
`AprilTag Switchable Cameras <https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/ConceptAprilTagSwitchableCameras.java>`__ をご参照ください。
```

### Block 53 (line 187)

```
もう一つの用途は、Limelightと電源付きUSBハブを使ってロボットバッテリー消耗を抑えることです。
以下の例ではLimelightとWebカメラの両方を接続しています。
```

### Block 54 (line 191)

```
   :alt: USBハブにWebカメラとLimelight 3Aを接続したREV Control Hub。
```

### Block 55 (line 193)

```
   Acer ODK350 USBハブ
```

### Block 56 (line 195)

```
   USBハブは**Control Hub** のUSB 3.0ポートに接続します。
   USBハブのUSB Cポートにモバイルバッテリーを接続し、全ての機器に電力を供給します。
   Logitech C270 WebカメラとLimelight 3AがUSBハブに接続されています。
```

### Block 57 (line 199)

```
Limelight 3Aは**VisionPortal** 対応デバイスではないため、AprilTag切替サンプルコードは利用できません。
ただし、Limelightや**VisionPortal** Webカメラの結果を必要に応じて取得・活用することは可能です。
```


## hardware_and_software_configuration/configuring/configuring_servo/configuring-servo.rst

### Block 1 (line 1)

```
サーボの構成
```

### Block 2 (line 4)

```
構成ファイルにサーボも追加します。この例では、標準の 180 度サーボを使用しています。
```

### Block 3 (line 7)

```
サーボの構成手順
```

### Block 4 (line 10)

```
1. 画面の **Servos** という単語をタッチして、** サーボ構成** 画面を表示します。
```

### Block 5 (line 17)

```
2. ドロップダウンコントロールを使用して、ポート #0 のサーボタイプとして「Servo」を選択します。
```

### Block 6 (line 24)

```
3. タッチパッドを使用して、ポート #0 のサーボの名前（この例では「servoTest」）を指定します。
```

### Block 7 (line 31)

```
4. **Done** ボタンを押して、サーボ構成を完了します。アプリは前の画面に戻るはずです。
```


## hardware_and_software_configuration/configuring/configuring_uvc_camera/configuring-uvc-camera.rst

### Block 1 (line 1)

```
外部UVCカメラとパワード USB ハブの構成
```

### Block 2 (line 4)

```
はじめに
```

### Block 3 (line 7)

```
競技マニュアルでは、コンピュータビジョン関連のタスクにおいて、USB Video Class（UVC）互換のカメラの使用を認めています。
**Robot Controller** として Android スマートフォンを使用しているチームは、内蔵カメラの代わりに外部接続カメラを使用することで、コンピュータビジョンタスク用に使用することができます。
```

### Block 4 (line 10)

```
外部カメラを使用する利点は、カメラとロボットコントローラーをそれぞれ最適な位置に設置できることです。カメラはビジョン関連タスクに適した位置に、Android **Robot Controller** はロボット制御に適した位置に配置することが可能です。
```

### Block 5 (line 12)

```
外部カメラを使用する欠点として、USB接続されたカメラによる追加の複雑性が生じることが挙げられます。外部カメラはロボットにコストと重量を追加し、適切に動作するように正しく配線する必要があります。
```

### Block 6 (line 14)

```
どのような種類の外部カメラが使用できますか？
```

### Block 7 (line 17)

```
このシステムは UVC カメラに対応しています。
理論上、カメラが UVC に準拠していれば、このシステムで動作するはずです。ただし、**FIRST** Tech Challenge ソフトウェアでテストされ、このソフトウェアで正確に動作するようにキャリブレーションされた推奨ウェブカメラが数台あります：
```

### Block 8 (line 23)

```
:doc:`他の UVC ウェブカメラに関する記事 <../../../apriltag/vision_portal/visionportal_webcams/visionportal-webcams>`
がありますので、チームで使用することができます。
```

### Block 9 (line 26)

```
UVC カメラのキャリブレーションは高度なタスクです。キャリブレーションファイルの作成方法に関する詳細は、
ftc_app プロジェクトフォルダーの一部として利用可能な
*teamwebcamcalibrations.xml* ファイルのコメントに記載されています（ファイルのオンラインコピーについては、
`このリンク <https://github.com/ftctechnh/ftc_app/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__
をご覧ください）。
```

### Block 10 (line 32)

```
**REV Robotics Expansion Hub** とスマートフォン
```

### Block 11 (line 35)

```
Android スマートフォンと **Expansion Hub** を使用しているチームは、ウェブカメラを使用するために USB Hub を追加する必要があります。
```

### Block 12 (line 38)

```
   :alt: **REV Expansion Hub** が Android スマートフォンとウェブカメラに USB Hub 経由で接続されている図。
```

### Block 13 (line 43)

```
外部カメラを使用したいチームは、Android **Robot Controller** を外部カメラと**REV Robotics Expansion Hub** に接続するための USB ハブが必要です。適切に動作するために、USB ハブは以下の要件を満たす必要があります：
```

### Block 14 (line 45)

```
1. USB 2.0 との互換性があります。注：USB 3.0 ハブでも動作しますが、より高速な速度ではありません。
2. 480Mbps のデータ転送レートに対応しています。
```

### Block 15 (line 48)

```
Modern Robotics Core Power Distribution Module は、USB 接続ウェブカメラで動作するには十分な速度のデータ転送速度がないため、このタスクに使用することはできません。
```

### Block 16 (line 50)

```
また、競技マニュアルではこの接続にパワード USB ハブの使用を認めています。チームがパワード USB ハブを使用する場合、USB ハブを動作させるための電力は、次のいずれかのソースからのみ供給できます：
```

### Block 17 (line 52)

```
1. 競技マニュアルに準拠した、外部接続のオフザシェルフ（COTS）USB バッテリーパック。
2. **REV Robotics Expansion Hub** の 5V DC 補助電力ポート（この実装には高度なスキルが必要です）。
```

### Block 18 (line 55)

```
**FIRST** はいくつかの USB 2.0 パワード ハブをテストしており、Anker 製のハブを推奨しています。このドキュメント作成時点では、このハブは
`Anker.com <https://www.anker.com/products/a7516>`__ から入手できました。
```

### Block 19 (line 59)

```
   :alt: チャージャーとケーブル付きのハブ。
```

### Block 20 (line 61)

```
Anker 4ポート パワード ハブは、ハブを 5V 電源に接続するために使用される Micro USB ポート（下図のオレンジ色の円で強調表示）があるため便利です。
```

### Block 21 (line 64)

```
   :alt: Micro USB ポート付きの USB ハブ。
```

### Block 22 (line 66)

```
このポートにより、ユーザーは標準的な USB Type B Micro ケーブルをハブに接続してから、ケーブルの反対側（USB Type A コネクターが付いている）を外部 5V USB バッテリーパックの出力ポートに接続することができます。下の画像では、Anker 4 ポート ハブは標準的な Type A to Type B USB Micro ケーブルを使用して「limefuel」外部 5V バッテリーパックから電力を供給されています。バッテリーは下の図に黄色い枠で強調表示されています。
```

### Block 23 (line 69)

```
   :alt: スマートフォンとウェブカメラを使用するための完全なセットアップ。
```

### Block 24 (line 71)

```
   USB ハブはバッテリーパックから電力を供給されています。
```

### Block 25 (line 73)

```
USB ハブは Type A コネクターとケーブルを介して OTG ケーブルに接続されており、このケーブルがスマートフォンに接続されています。
バッテリーパックは USB ハブの USB Type B Micro ポートに接続されています。
ウェブカメラは USB ハブの USB Type A ポートの 1 つに接続されています。
USB Type A to USB Mini B ケーブルが USB ハブを **REV Expansion Hub** に接続しています。
```

### Block 26 (line 78)

```
USB ハブは **REV Robotics Expansion Hub** の 5V 補助ポートからも電力を供給できます。この構成では、一方の端が 5V 補助ポートにプラグできる特殊なケーブルが必要であり、もう一方の端が USB ハブのパワーポートにプラグできる必要があります。
```

### Block 27 (line 81)

```
   :alt: スマートフォンとウェブカメラを使用するための完全なセットアップ。
```

### Block 28 (line 83)

```
   USB ハブは 5V 補助ポートに接続されています。
```

### Block 29 (line 85)

```
チームは、サーボ延長ケーブルの一方の端（5V 補助ポートにプラグするため）と Micro USB ケーブルの一方の端（Anker ハブのパワーポートにプラグするため）を使用してこの特殊なケーブルを作成できることに注意してください。**このケーブルの作成は高度なタスクであり、電子機器と配線の専門知識を持つ成人メンターの指導を受けているチームのみが試みるべきです。このケーブルの極性が正しいことは非常に重要です。極性が逆転している場合、電子機器に損傷を与える可能性があります。**
```

### Block 30 (line 87)

```
サンプル **OpMode**
```

### Block 31 (line 90)

```
外部 UVC ウェブカメラを **VisionPortal** 操作で使用する方法を示すサンプル**Blocks** および Java**OpMode** があります。チームが外部 UVC カメラを使用する前に、外部カメラが USB 接続デバイスの 1 つとして定義された構成ファイルを構成する必要があります。
```

### Block 32 (line 92)

```
有効な構成ファイルが定義されてアクティブになると、プログラマーは内部 Android カメラの代わりに外部 UVC カメラを、ビジョン関連タスクに使用できます。
```

### Block 33 (line 95)

```
   :alt: サンプル **Blocks** コード
```


## hardware_and_software_configuration/configuring/getting_started/getting-started.rst

### Block 1 (line 2)

```
はじめに
```

### Block 2 (line 5)

```
構成ファイルの作成
```

### Block 3 (line 8)

```
**Control Hub** や**Expansion Hub** に接続されたモーター、サーボ、センサーと通信するためには、まず**Robot Controller** 上で構成ファイルを作成する必要があります。これにより、**Robot Controller** は**Control Hub** や**Expansion Hub** の外部ポートにどのハードウェアが接続されているかを認識できるようになります。
```

### Block 4 (line 10)

```
Control Hub の準備
```

### Block 5 (line 13)

```
**Control Hub** を使用する場合、追加の接続は不要です。**Control Hub** の電源が入っていて、**DRIVER STATION** とペアリングされていることを確認してください。
```

### Block 6 (line 15)

```
Android スマートフォンを Expansion Hub に接続する
```

### Block 7 (line 18)

```
Android スマートフォンを **Robot Controller** として使用する場合は、USB ケーブルと OTG（On-The-Go）アダプターを使って、スマートフォンを**Expansion Hub** に物理的に接続する必要があります。また、**DRIVER STATION** が現在**Robot Controller** とペアリングされていることも確認してください。
```

### Block 8 (line 20)

```
Android スマートフォンを Expansion Hub に接続する手順
```

### Block 9 (line 23)

```
1. **Expansion Hub** の電源スイッチを入れて、電源をオンにします。
```

### Block 10 (line 30)

```
2. USB ケーブルの Type B Mini 端子を **Expansion Hub** の USB mini ポートに接続します。
```

### Block 11 (line 37)

```
3. USB ケーブルの Type A 端子を OTG アダプターに接続します。
```

### Block 12 (line 44)

```
4. **Robot Controller** スマートフォンの電源が入っていて、ロック解除されていることを確認します。USB Micro OTG アダプターをスマートフォンの OTG ポートに接続します。
```

### Block 13 (line 51)

```
OTG アダプターをスマートフォンに接続すると、スマートフォンが **Expansion Hub** を検出し、**Robot Controller** アプリが起動します。
```

### Block 14 (line 53)

```
5. 初めて **Robot Controller** スマートフォンを**Expansion Hub** に接続した際、Android の OS から新しく検出された USB デバイス（**Expansion Hub** ）を**Robot Controller** アプリに関連付けてもよいか確認するメッセージが表示されます。
```

### Block 15 (line 61)

```
   USB ハードウェアの関連付けを求めるメッセージが複数回表示される場合があります。表示された際は、必ず「この USB デバイスにデフォルトで使用する」オプションを選択し、「OK」ボタンを押して **Robot Controller** アプリに関連付けてください。関連付けを行わないと、次回システム起動時に**Robot Controller** アプリがこの**Expansion Hub** に正常に接続できない場合があります。
```

### Block 16 (line 64)

```
DRIVER STATION を使った構成ファイルの作成
```

### Block 17 (line 67)

```
構成ファイルは **Robot Controller** に保存する必要がありますが、このチュートリアルでは**DRIVER STATION** アプリを使ってリモートで構成ファイルを作成します。**DRIVER STATION** は**Control Hub** や Android スマートフォン**Robot Controller** 用の構成ファイルを作成できます。
```

### Block 18 (line 70)

```
DRIVER STATION を使って Robot Controller に構成ファイルを作成する手順
```

### Block 19 (line 73)

```
1. **Driver Station** アプリ右上の縦三点（︙）をタッチします。ポップアップメニューが表示されます。
```

### Block 20 (line 80)

```
2. ポップアップメニューから「**Configure Robot**」を選択し、「**Configuration**」画面を表示します。
```

### Block 21 (line 87)

```
3. **Robot Controller** に既存の構成ファイルがない場合、ファイル作成が必要である旨のメッセージが表示されます。
```

### Block 22 (line 94)

```
「**New**」ボタンを押して、新しい構成ファイルを作成します。
```

### Block 23 (line 96)

```
4. 新しい構成画面が表示されると、**Robot Controller** アプリがシリアルバスをスキャンし、接続されているデバイスを検出します。
```

### Block 24 (line 103)

```
検出されたデバイスは「USB Devices in configuration.」の下にリスト表示されます。「Expansion Hub Portal 1」などのエントリが表示されるはずです。
```

### Block 25 (line 105)

```
**Expansion Hub** は、USB ケーブル（スマートフォンの場合）や内部シリアルバス（**Control Hub** の場合）を通じて**Robot Controller** に直接接続されているため「Portal」として表示されます。
```

### Block 26 (line 107)

```
スマートフォンを **Robot Controller** として使用していて「Expansion Hub Portal」が表示されない場合は、配線が確実に接続されているか確認し、「Scan」ボタンを1～2回押して再スキャンしてください。
```

### Block 27 (line 109)

```
5. 「Expansion Hub Portal 1」などの Portal リストをタッチすると、その Portal に接続されている **Expansion Hub** が表示されます。
```

### Block 28 (line 116)

```
**Expansion Hub** が1台だけ接続されている場合は、1つだけ「Expansion Hub 2」などのエントリが表示されます。
```

### Block 29 (line 118)

```
6. 「Expansion Hub 2」などの Expansion Hub リストをタッチすると、そのデバイスの入出力ポート一覧が表示されます。
```

### Block 30 (line 125)

```
選択した **Expansion Hub** に利用可能なモーター、サーボ、センサーのポートがすべて表示されます。
```


## hardware_and_software_configuration/configuring/index.rst

### Block 1 (line 1)

```
ハードウェアの構成
```

### Block 2 (line 4)

```
このページには、独自のプロジェクトで使用できるように、制御システムハードウェアを構成する方法に関する情報が含まれています。
```


## hardware_and_software_configuration/configuring/managing_esd/managing-esd.rst

### Block 1 (line 1)

```
静電気放電の影響の管理
```

### Block 2 (line 4)

```
はじめに
```

### Block 3 (line 7)

```
静電気放電（ESD）イベントは、競技ロボットの正常な動作を妨げる可能性があります。このセクションでは、ESD イベントの原因を調べ、ESD イベントがロボットの制御システムを無効にしたり損傷したりするリスクを軽減する方法について説明します。
```

### Block 4 (line 9)

```
このセクションは、ESD 障害を引き起こす物理現象の簡単な概要のみを提供していることに注意してください。次のリンクを使用して、*FIRST* 卒業生で 2018 年夏季エンジニアリングインターンである Eric Chin 氏が執筆した詳細なホワイトペーパーを閲覧できます。このホワイトペーパーは、さまざまな ESD 軽減技術の有効性を調査および定量化しています。
```

### Block 5 (line 13)

```
Doug Chin 氏、Eric Chin 氏、Greg Szczeszynski 氏が ESD によって引き起こされる問題をモデル化し、この現象によって引き起こされるリスクを軽減するためのさまざまな技術を評価した仕事に感謝します。また、*FIRST* Tech Challenge チーム 2844、8081、10523、10523a、10984、および Arizona のボランティアチーム（Robert Garduno、Susan Garduno、Richard Gomez、Matthew Rainey、Christine Sapio、Patricia Strones、David Thompson を含む）が、暑い砂漠の太陽の下でこれらの軽減技術の一部をテストするのを支援してくれたことに感謝します。
```

### Block 6 (line 15)

```
静電気放電イベントとは？
```

### Block 7 (line 18)

```
静電気放電（ESD）イベントは、高電荷を帯びた導電性オブジェクト（ロボットの金属フレームなど）が、無電荷または逆電荷の導電性オブジェクトに触れて放電するときに発生します。関与する電圧が高い（数万ボルトまで）ため、ESD イベントは、1つのオブジェクトに蓄積された電荷が導電経路を介して中性または逆電荷のオブジェクトに流れるときに、非常に高い電流を生成する可能性があります。
```

### Block 8 (line 24)

```
   ESD イベントの例、電流はロボットからフィールド壁に流れます。
```

### Block 9 (line 26)

```
ロボットが帯電する仕組み
```

### Block 10 (line 29)

```
ウールの靴下を履いてカーペットの上で足をこすり、次にドアノブに触れたときに何が起こるかを考えてみてください。ほぼ確実にショックを受けるでしょう。この現象の原因は何でしょうか？2つの表面が相互作用すると、少量の接着が発生します。これは、それらが電子を共有することを意味し、異なる材料で作られている場合、電子の共有が不均等になる可能性があります。表面が分離されると、帯電する可能性があります。これは摩擦帯電効果と呼ばれます。
```

### Block 11 (line 35)

```
   ロボットは摩擦帯電効果により帯電します。
```

### Block 12 (line 37)

```
フィールドタイル上を移動するロボットの車輪は、カーペット上を移動するウールの靴下が体に電荷を蓄積するのと同じように、ロボットフレームに電荷を蓄積します。他の多くのプラスチックやゴム素材も同様の挙動を示します。摩擦帯電は、1つのオブジェクトから電荷を取り、別のオブジェクトに与えるため、電荷はミラーリングされることに注意することが重要です。*FIRST* Tech Challenge ロボットの場合、正電荷が車輪に蓄積され、負電荷がタイルに蓄積されます。
```

### Block 13 (line 39)

```
競技フィールドの柔らかいタイルを横切って滑る車輪を持つロボットは、タイルを横切って転がる車輪を持つロボットよりも、そのフレームに静電気を急速に蓄積することに注意してください。
```

### Block 14 (line 41)

```
ロボットの放電
```

### Block 15 (line 44)

```
電流は、高電位のオブジェクトから低電位のオブジェクトに流れて、それらの間の電圧差を均等化したいと「望んでおり」、そうするための導電経路（絶縁されていないワイヤーなど）が与えられればそうします。ロボット競技の場合、ロボットが別の金属オブジェクト（ゲームフィールドの一部など）よりも高い電位にある場合、帯電したロボットのフレームが他のオブジェクトに接触すると ESD イベントが発生します。
```

### Block 16 (line 46)

```
電位差が十分に大きい場合、電流が電気アークの形で空気を通って流れることも可能です。アークは、2つの異なる電荷を持つ導体間の空気がイオン化され、1つの導体から別の導体への電流の流れを可能にするときに発生します。*FIRST* Tech Challenge ロボットで見られる電圧でのアークは、3/8インチ（1 cm）以上の空隙を飛び越えることができます。アークは直接接触とほぼ同じように動作するため、かなりの量の電流を運ぶことができます。目に見える火花は大きな静電アークを伴います。
```

### Block 17 (line 52)

```
   逆電荷の2つの球体間の電気アーク。
```

### Block 18 (line 54)

```
ESD 障害のリスクを軽減するためにどのような手順を実行できますか？
```

### Block 19 (line 57)

```
ステップ 1: タイル床を帯電防止スプレーで処理する（イベントホストのみ）
```

### Block 20 (line 60)

```
ESD イベントによる障害のリスクを軽減する最も効果的な方法の1つは、競技フィールドのタイル床を帯電防止スプレーで処理することです。帯電防止スプレーは、タイル表面の電気伝導性を高めます。これにより、ロボットがタイル床を横切って移動するときに、ロボット上の静電荷の蓄積を防ぐのに役立ちます。
```

### Block 21 (line 68)

```
*FIRST* は、タイルを処理するために `ACL Heavy Duty Staticide <https://www.aclstaticide.com/products/heavy-duty-staticide>`__ スプレーの使用を推奨しています。このスプレーは、ロボット上の電荷蓄積を防ぐのに非常に効果的です。また、このスプレーは1回だけ適用すればよく、イベント全体を通して持続します（複数日にわたって機能します）。
```

### Block 22 (line 70)

```
タイル床の処理は、**イベントホストのみが許可されていること** に注意してください。チームが自分でタイル床を処理することは** 許可されていません** 。
```

### Block 23 (line 72)

```
ステップ 2: 信号線にフェライトチョークを追加する
```

### Block 24 (line 75)

```
フェライトチョークは、ESD イベント中に見られるような大きな電流変化をブロックします。これにより、センサーやその他の周辺デバイスがショックを受けたときに、電気部品への損傷や障害のリスクを軽減できます。
```

### Block 25 (line 81)

```
フェライトチョークの使用は、ESD の影響を軽減する非常に効果的な方法です。
```

### Block 26 (line 83)

```
1. 内蔵またはスナップオン式フェライトチョークを備えた USB ケーブルを使用します。
2. 信号ケーブルにスナップオン式フェライトチョークを取り付けます。
```

### Block 27 (line 86)

```
   -  センサーケーブル
   -  エンコーダーケーブル
   -  サーボケーブル
```

### Block 28 (line 90)

```
ステップ 3: ロボットの金属フレームから電子機器を電気的に絶縁する
```

### Block 29 (line 93)

```
*FIRST* Tech Challenge マッチ中にロボットがタイル床を行き来するとき、摩擦帯電効果によりロボットの金属フレームに電荷が蓄積される可能性があります。ロボットのフレームに電荷が蓄積されるが、制御システムを構成する電子機器が異なる電圧にある場合、制御システムの露出した部分または絶縁が不十分な部分が金属フレームに近づく（3/8インチまたは10mm未満）とショックが発生する可能性があります。
```

### Block 30 (line 95)

```
フレームから電子機器を電気的に絶縁または隔離することで、このタイプのショックによる障害を回避できます。
```

### Block 31 (line 97)

```
サブステップ A: 非導電性材料に電子機器を取り付ける
```

### Block 32 (line 100)

```
薄い合板シートや PVC タイプ A シートなどの非導電性材料に制御システム電子機器を取り付けることで、フレームと電子機器の間の ESD イベントのリスクを軽減できます。非導電性の硬質パネルを使用すると、ワイヤー管理やストレインリリーフにも役立ちます。
```

### Block 33 (line 106)

```
   合板シートには穴が開けられており、ワイヤーはケーブルタイで合板に固定されています。
```

### Block 34 (line 108)

```
サブステップ B: 電子機器の露出した部分または絶縁が不十分な部分を隔離する
```

### Block 35 (line 111)

```
制御システムの電子機器の特定の部分には、露出した金属があるか、絶縁が不十分です。これらの部分が金属フレームに近すぎると、フレームに電荷が蓄積された場合にショックが発生する可能性があります。
```

### Block 36 (line 117)

```
   電子機器の絶縁が不十分または露出した部分で静電ショックが発生する可能性があります。
```

### Block 37 (line 119)

```
たとえば、REV Robotics Expansion Hub で使用される 4 線式センサーケーブルには、絶縁が不十分なプラスチックコネクタがあります。ロボットの金属フレームに電荷が蓄積され、センサーケーブルの端がフレームに近く配置されている場合、ショックが発生する可能性があり、このショックは Expansion Hub の I2C ポートを妨害したり損傷したりする可能性があります。
```

### Block 38 (line 121)

```
同様に、一部のサーボ延長ケーブルには、適切に絶縁または隔離されていない限り ESD に対して脆弱な露出した金属部分があります。
```

### Block 39 (line 123)

```
電子システムのこれらの脆弱な領域をフレームから遠ざける（3/8インチまたは10mmを超える空隙で）ことで、ESD 障害のリスクを軽減できます。
```

### Block 40 (line 129)

```
   電子機器の露出した部分をフレームから遠ざけます。
```

### Block 41 (line 131)

```
電気テープを使用してこれらの領域を絶縁することも同様に効果的で、実装が容易な場合があります。
```

### Block 42 (line 137)

```
   電気テープで露出した部分を覆います。
```

### Block 43 (line 139)

```
ステップ 3: 電気絶縁材料で外部の金属機能を覆う
```

### Block 44 (line 142)

```
別の ESD 軽減戦略は、ロボット上の金属物体の露出した部分を、ロボットがフィールド壁やゲーム要素に接触したときにアークが発生しないように、電気絶縁材料（電気テープなど）で覆うことです。
```

### Block 45 (line 148)

```
   電気テープでロボットの露出した金属の端を覆います。
```

### Block 46 (line 150)

```
過去のシーズンでこれを行ったチームは、ESD イベントによる障害の減少を観察しています。
```

### Block 47 (line 152)

```
ステップ 4: 承認されたケーブルで電子機器を金属フレームに接地する
```

### Block 48 (line 155)

```
電気システムを完全に隔離することは困難であるため、制御システムを金属フレームに接地することで、それらの間の電位差を排除し、フレームと制御システムの間のアークのリスクを軽減することが推奨されます。
```

### Block 49 (line 161)

```
   XT30 からスペード端子ケーブルを使用して金属フレームに接地された Control Hub。
```

### Block 50 (line 163)

```
接地は、**FIRST 承認の市販ケーブル** のみを使用して行う必要があることが重要です。カスタムメイドまたは自作のケーブルは、適切なサイズのワイヤーを使用していない可能性があり、電流に過負荷がかかった場合に火災の危険性があるため、** 許可されていません** 。
```

### Block 51 (line 165)

```
*FIRST* 承認のケーブルには、ケーブルが設計されている電流容量に適したゲージのワイヤーがあります。詳細については、競技マニュアルを参照してください。
```

### Block 52 (line 167)

```
Anderson Powerpole コネクタを使用する場合は、XT30 から Anderson Powerpole へのアダプターが必要になることに注意してください。
```

### Block 53 (line 173)

```
   Anderson Powerpole への XT30 アダプター。
```

### Block 54 (line 175)

```
電子機器を接地するには、*FIRST* 承認のケーブルの一端を Expansion Hub または Control Hub の XT30 バッテリーポートの 1 つに接続します。もう一方の端をロボットの金属フレームに接続します（スペード端子を使用している場合は、フレームのボルトの周りに端子を配置してボルトをしっかりと締めます）。
```

### Block 55 (line 177)

```
電気システムを絶縁し、**かつ** 金属フレームに接地することは、最初は矛盾しているように見えるかもしれません。ただし、電子機器が損傷したり障害が発生したりするのは、電子機器とフレームの間で電流が制御不能な方法で流れるときです。電気システムをフレームに直接接地することで、チームは電流が流れる制御された経路を提供しています。大きなワイヤーゲージの接地ケーブルは、スパイクやサージからフレームへのより直接的な経路を提供できます（電位を均等化します）。
```

### Block 56 (line 179)

```
異なる ESD 軽減技術を組み合わせると、異なる方法でリスクを軽減するため、より優れた全体的な保護が提供されることに注意してください。
```


## hardware_and_software_configuration/configuring/saving_config/saving-config.rst

### Block 1 (line 1)

```
構成情報の保存
```

### Block 2 (line 3)

```
ハードウェアを構成したら、情報を構成ファイルに保存する必要があります。この情報を保存しないと、情報が失われ、**Robot Controller** がハードウェアと通信できなくなります。
```

### Block 3 (line 5)

```
構成情報の保存手順
```

### Block 4 (line 8)

```
1. **Done** ボタンを押して、構成画面の1つ上のレベルに移動します。
```

### Block 5 (line 15)

```
2. **Done** ボタンをもう一度押して、構成画面の最上位レベルに戻ります。
```

### Block 6 (line 22)

```
3. **Save** ボタンを押します。
```

### Block 7 (line 29)

```
4. プロンプトが表示されたら、タッチスクリーンのキーパッドを使用して構成ファイル名を指定します（この例では「into_the_deep」）。
```

### Block 8 (line 36)

```
5. **OK** ボタンを押して、そのファイル名を使用して構成情報を保存します。
```

### Block 9 (line 43)

```
6. 構成ファイルが保存されたら、Android の戻る矢印ボタンをタッチして、アプリのメイン画面に戻ります。
```

### Block 10 (line 50)

```
7. 構成ファイルがメイン **DRIVER STATION** 画面のアクティブな構成ファイルであることを確認します。
```


## hardware_and_software_configuration/connecting_devices/connecting_color/connecting-color.rst

### Block 1 (line 1)

```
Hub へのカラー距離センサーの接続
```

### Block 2 (line 4)

```
Hub には 4 つの独立した I2C バスがあります。各バスには Hub に独自のポートがあります。**REV Robotics カラー距離センサー** を Hub の I2C バス #0 に接続します。
```

### Block 3 (line 6)

```
このタスクを完了するには、推定 2.5 分かかります。
```

### Block 4 (line 9)

```
Hub へのカラー距離センサーの接続手順
```

### Block 5 (line 12)

```
1. 4 ピン JST PH ケーブルの一端を **REV Robotics カラー距離センサー** に接続します。
```

### Block 6 (line 19)

```
2. 4 ピン JST PH ケーブルのもう一方の端を Hub の「0」とラベル付けされた I2C ポートに差し込みます。
```


## hardware_and_software_configuration/connecting_devices/connecting_motor/connecting-motor.rst

### Block 1 (line 1)

```
Hub へのモーターの接続
```

### Block 2 (line 4)

```
Hub は Hub あたり最大 4 つの 12V DC モーターを駆動できます。Hub は、2 ピン JST VH コネクタとして知られる電気コネクタの種類を使用しています。*FIRST* 承認の 12V DC モーターの多くは、Anderson Powerpole コネクタを装備しています。アダプターケーブルを使用して、Anderson Powerpole コネクタを Hub モーターポートに接続できます（詳細については `FIRST Tech Challenge Robot Wiring Guide (PDF) <https://ftc-resources.firstinspires.org/ftc/team/robot-wires>`__ を参照してください）。
```

### Block 3 (line 12)

```
このチュートリアルの例では、*FIRST* は、テスト実行中にモーターを固定し、動き回るのを防ぐために、シンプルなリグを構築することをユーザーに推奨しています。上の画像は、Tetrix モーターマウントといくつかの Tetrix C チャンネルで構築されたリグに取り付けられた Tetrix モーターを示しています。ギアがモーターシャフトに取り付けられており、ユーザーがシャフトの回転を確認しやすくなっています。
```

### Block 4 (line 14)

```
このタスクを完了するには、推定 2.5 分かかります。
```

### Block 5 (line 17)

```
Hub への 12V モーターの接続手順
```

### Block 6 (line 20)

```
1. モーターの電源ケーブルの Anderson Powerpole 端を、Anderson to JST VH アダプターケーブルの Powerpole 端に接続します。
```

### Block 7 (line 30)

```
2. JST VH 白色コネクタを Hub の「0」とラベル付けされたモーターポートに接続します。
```


## hardware_and_software_configuration/connecting_devices/connecting_power/connecting-power.rst

### Block 1 (line 1)

```
Hub への 12V 電源の接続
```

### Block 2 (line 4)

```
Hub は 12V 充電式バッテリーから電力を引き出します。安全上の理由から、バッテリーには 20A ヒューズが内蔵されています。メカニカルスイッチを使用して電源をオン/オフします。
```

### Block 3 (line 6)

```
このタスクを完了するには、推定 5 分かかります。
```

### Block 4 (line 9)

```
Hub への 12V 電源の接続手順
```

### Block 5 (line 12)

```
1. 12V バッテリーに Tamiya スタイルコネクタがある場合は、Tamiya to XT30 アダプターケーブルをスイッチケーブルの対応する端に接続します。
```

### Block 6 (line 21)

```
2. スイッチケーブルのもう一方の端を Hub の対応する XT30 ポートに接続します。
```

### Block 7 (line 28)

```
3. スイッチが OFF 位置にあることを確認します。
```

### Block 8 (line 35)

```
4. 12V バッテリーを Tamiya to XT30 ケーブルに接続します。
```

### Block 9 (line 42)

```
5. スイッチをオンにして、Hub がバッテリーから電力を引き出していることを確認します。Hub の LED が点灯している必要があります（下の画像の Hub の右上隅にある青い LED に注目してください）。
```

### Block 10 (line 49)

```
6. スイッチをオフにして、Hub がオフになっていることを確認します。Hub の LED は点灯していないはずです。
```


## hardware_and_software_configuration/connecting_devices/connecting_servo/connecting-servo.rst

### Block 1 (line 1)

```
Hub へのサーボの接続
```

### Block 2 (line 4)

```
Hub には 6 つの組み込みサーボポートがあります。サーボポートは、サーボに一般的に見られる標準の 3 線ヘッダースタイルコネクタを受け入れます。グランドピンはサーボポートの左側にあることに注意してください。
```

### Block 3 (line 6)

```
このタスクを完了するには、推定 2.5 分かかります。
```

### Block 4 (line 8)

```
Hub へのサーボの接続手順
```

### Block 5 (line 11)

```
1. サーボケーブルを Hub の「0」とラベル付けされたサーボポートに接続します。グランドピンはサーボポートの左側にあることに注意してください。
```

### Block 6 (line 18)

```
2. サーボケーブルの黒いグランド線が、サーボポートのグランドピン（ポートの左側に配置されている）と一致することを確認します。
```


## hardware_and_software_configuration/connecting_devices/connecting_touch/connecting-touch.rst

### Block 1 (line 1)

```
Hub へのタッチセンサーの接続
```

### Block 2 (line 4)

```
Hub には 4 つの独立したデジタル入出力（I/O）ポートがあります。各ポートには 2 つのデジタル I/O ピンがあり、Hub には合計 8 つのデジタル I/O ピンがあります。**REV Robotics タッチセンサー** をデジタル I/O ポートの 1 つに接続します。
```

### Block 3 (line 6)

```
**REV Robotics タッチセンサー** の場合、デバイスには 4 ピンセンサーケーブル用のコネクタポートがあります。ただし、デバイスは利用可能な 2 つのデジタル I/O ピンの 1 つにのみ接続する必要があります。**REV Robotics タッチセンサー** の場合、標準の**REV Robotics** 4 ピン JST PH ケーブルを使用すると、ポートの 2 番目のデジタル I/O ピンが接続されます。「0-1」ポートの場合、4 ピンケーブルを介して接続されるのは「1」とラベル付けされたピンです。同様に、「2-3」ポートの場合、4 ピンケーブルを介して接続されるのは「3」とラベル付けされたピンです。
```

### Block 4 (line 8)

```
このタスクを完了するには、推定 2.5 分かかります。
```

### Block 5 (line 10)

```
Hub へのタッチセンサーの接続手順
```

### Block 6 (line 13)

```
1. 4 ピン JST PH ケーブルの一端を **REV Robotics タッチセンサー** に接続します。
```

### Block 7 (line 20)

```
2. 4 ピン JST PH ケーブルのもう一方の端を Hub の「0」とラベル付けされたデジタル I/O ポートに差し込みます。
```


## hardware_and_software_configuration/connecting_devices/index.rst

### Block 1 (line 1)

```
Control Hub または Expansion Hub へのデバイス接続
```

### Block 2 (line 4)

```
このセクションでは、モーター、サーボ、およびいくつかのセンサーを **REV Robotics Control Hub** または**REV Robotics Expansion Hub** に接続する方法について説明します。**Control Hub** は組み込みの Android デバイスがあるため**Expansion Hub** とは異なりますが、外部モーター、サーボ、センサーポートのレイアウトは**Control Hub** と**Expansion Hub** で同じです。
```

### Block 3 (line 6)

```
このセクションの画像は、デバイスの接続方法を示すために **Expansion Hub** を使用しています。ただし、プロセスは**Control Hub** でも同じです。
```

### Block 4 (line 8)

```
このセクションの指示で「Hub」という言葉を使用する場合、**Control Hub** または**Expansion Hub** を指しています。
```


## hardware_and_software_configuration/index.rst

### Block 1 (line 2)

```
   :title: ハードウェアとソフトウェアの構成
```

### Block 2 (line 4)

```
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, 構成
```

### Block 3 (line 6)

```
ハードウェアとソフトウェアの構成
```

### Block 4 (line 9)

```
制御システムのハードウェアとソフトウェアの構成
```


## hardware_and_software_configuration/self_inspect/new-self-inspect.rst

### Block 1 (line 5)

```
はじめに
```

### Block 2 (line 8)

```
このページでは、**Driver Station** （DS）アプリと**Robot Controller** （RC）アプリにおける Self Inspect 画面について説明します。
```

### Block 3 (line 10)

```
Self Inspect 画面は、FTCの制御システムに関するルールに基づき、デバイスの状態をスナップショットとして表示します。
これらのルールは、競技マニュアル（Competition Manual）に記載されており、
`Current Game and Season Materials page <https://ftc-resources.firstinspires.org/files/ftc/game>`__ （**FIRST** 公式サイト）で確認できます。
```

### Block 4 (line 15)

```
   `Inspection Checklist (PDF) <https://ftc-resources.firstinspires.org/ftc/event/inspection-check>`__ を使うことで、イベント前にロボットのセルフ検査が可能です。イベント前のセルフ検査を強く推奨します。
```

### Block 5 (line 17)

```
   また、`Inspection Quick Reference (PDF) <https://ftc-resources.firstinspires.org/ftc/event/inspection-reference>`__ には合法・非合法部品の例が掲載されています（ただし競技マニュアルの代用にはなりません）。
```

### Block 6 (line 19)

```
Self Inspect 画面は、制御システムの各要素が最新かつ正しく構成されているかをチームが確認するための、簡易的な参考情報として提供されています。
```

### Block 7 (line 21)

```
各検査画面は、ロボットの再起動有無にかかわらず自動で更新されるため、問題が解決されたかをすばやく確認できます。
```

### Block 8 (line 23)

```
限られた画面スペースで有用な情報を最大限に表示することが課題です。Self Inspect のレイアウトやグラフィックはFTCの要件に合わせて進化しており、本ページでは簡潔ながら意味のあるキャプションを解説します。
```

### Block 9 (line 26)

```
ロボット検査
```

### Block 10 (line 29)

```
Self Inspect レポートはFTC大会のロボット検査時に参照されることがありますが、FTCルールへの完全な準拠や公式基準を示すものでは**ありません** 。
ロボットと**Driver Station** が起動・接続された状態で、検査員は紙またはタブレットの**Inspection Checklist** フォームを使って確認します。
**Driver Station Inspection Report** と**Robot Controller Inspection Report** の両方をDSから表示できます。
多くのFTCイベントでは、RCインスペクトレポートに表示されるQRコードをスキャンします。
```

### Block 11 (line 35)

```
バージョン情報
```

### Block 12 (line 38)

```
競技マニュアルには、デバイスのファームウェア、Android OS、FTCアプリの推奨最小バージョンが記載されています。
チームは、ロボット検査の合否に影響なく、古いバージョンを使用することも可能です。
これは、競技会場で急いでアップグレードし、失敗してロボットが動かなくなる事態を避けるためです。
```

### Block 13 (line 43)

```
   本ページの画像はFTCアプリのバージョン10.3以降のものです。
   Driver HubとControl Hubのペアのみを例示しています。スマートフォンを**Driver Station** や**Robot Controller** として使う場合は若干異なる場合があります。
   バージョン10.2以前の画面は :doc:`old self-inspect<self-inspect>` を参照してください。
```

### Block 14 (line 47)

```
**FIRST** は、ファームウェア・Android OS・FTCアプリの最新版使用を推奨しますが、必須ではありません。
最新版にはバグ修正や機能強化が含まれています。例えば、**Control Hub Android OS** のバージョン1.1.6ではWi-Fi関連の修正が含まれています。
```

### Block 15 (line 50)

```
FTCの各シーズンでFTCアプリのメジャーバージョンがリリースされます。INTO THE DEEPのメジャーバージョンは10、DECODEは11です。
ゲームに**AprilTag** が含まれる場合、SDKには :doc:`localization<../../apriltag/vision_portal/apriltag_localization/apriltag-localization>` 情報が含まれ、ロボットのフィールド上の位置を特定できます。
シーズン中は、マイナーバージョン（例：11.1、11.2など）でバグ修正や機能追加が行われます。
```

### Block 16 (line 54)

```
どのバージョンを選択しても、インストールされている**Robot Controller** アプリと**Driver Station** アプリのメジャー・マイナーバージョンが一致していることを強く推奨します。すべてのバージョンが互換性を持つわけではありません。
```

### Block 17 (line 56)

```
チームは、ロボット検査の合否に影響なく、古いバージョンを使用することも可能です。
```

### Block 18 (line 59)

```
    一部のFTCアプリバージョンではロボット通信プロトコルが異なり、互いに接続できない場合があります。
```

### Block 19 (line 61)

```
    推奨バージョン未満のソフトウェアを使用しているチームに対して、フィールドスタッフは十分なサポートを提供できません。
```

### Block 20 (line 64)

```
Driver Station Self Inspect レポート
```

### Block 21 (line 67)

```
以下は、Driver Hubを縦向きにして、すべての項目がスクロールなしで1画面に表示される**Driver Station** Self Inspect レポートのスクリーンショットです。
```

### Block 22 (line 74)

```
   すべての項目が正常
```

### Block 23 (line 76)

```
-  項目1：三点リーダーはメニューで、``Disconnect from Wi-Fi Direct`` と``Disable Bluetooth`` の2つの選択肢があります。
   Control HubとペアになっているDriver Hubでは通常不要ですが、スマートフォンを**Driver Station** や**Robot Controller** として使う場合に利用します。
   ``Disconnect from Wi-Fi Direct`` は動作しますが、アプリが自動で再ペアリングすることがあります。
   ``Disable Bluetooth`` は、DSでBluetoothが有効になっている場合以外は不要です。
-  項目2：``Manufacturer`` はREV Driver Hubの場合、**REV Robotics** である必要があります。
-  項目3：``Model`` は**Driver Hub** である必要があります。
-  項目4：``Driver Hub OS Version`` は通常1.2.0です。
-  項目5：``Android Version`` はDriver Hubの場合、通常10です。
-  項目6：``Battery Level`` はデバイスのバッテリー残量を表示します。豆知識：残量が減るとパーセンテージの緑色が**オレンジ** に近づきます。
-  項目7：``Bluetooth`` は**Disabled** （無効）である必要があります。
-  項目8：``Location services`` は**Enabled** （有効）である必要がありますが、**Android 8** 以上のデバイスのみ表示されます。これはSDK/Androidの技術要件であり、FTCルールではありません。
-  項目9：``Wi-Fi Enabled`` は**Yes** （はい）である必要があります。DSデバイスのWi-Fiが**ON** であることを示します。
-  項目10：``Standard Wi-Fi Connected`` は**Yes** （はい）である必要があります。Driver HubがControl Hubなどの標準Wi-Fiに接続されていることを示します。
-  項目11：``Driver Station Name`` はFTCの命名規則に合致している必要があります。チーム番号＋-DS（例：99999-DS）です。
   予備デバイスの場合は、<チーム番号>-<英字>-DS（例：12345-A-DS、12345-B-DS）となります。命名規則は競技マニュアルを参照してください。
-  項目12：``Robot Controller Name`` を表示します。未接続の場合は**None** となります。Robot ControllerとDriver Stationのチーム番号部分が一致しない場合はエラーが表示されます。
   RC名がFTC命名規則に合致しているかはチェックしません。詳細はRobot Controller Self Inspect レポートを参照してください。
-  項目13：Apps Installed ``Robot Controller`` は**Not installed** （未インストール）である必要があります。Driver StationデバイスにRobot Controllerアプリがインストールされていないことを確認します。
   各デバイスにはFTCアプリを1つだけインストールしてください。両方インストールすると正常に動作しない場合があります。
-  項目14：Apps Installed ``Driver Station`` はDriver Stationアプリのバージョン番号を表示します。**FIRST** は最新版の使用を推奨しますが、必須ではありません。
   デバイスの日付が不正または未来日付の場合、「The Driver Station app is obsolete」と表示され、検査項目が無効になることがあります。日付を修正すれば正常に戻ります。
```

### Block 24 (line 100)

```
以下は、Self Inspect で一部項目が**不合格** となったDriver Stationのレポート例です。
問題は赤丸の感嘆符アイコン、またはオレンジ三角の感嘆符アイコンで示されます。
```

### Block 25 (line 103)

```
このDriver Hubはファームウェアリセットされ、DSバージョンが7に戻り、すべてのシステム・DSアプリ設定が初期化されました。
その後、`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client>`__ でDSバージョン10.3にアップデートし、FTCRobotControllerアプリもAndroid StudioからDSデバイスにインストールしました。
```

### Block 26 (line 111)

```
   Self Inspect に問題あり！
```

### Block 27 (line 113)

```
-  項目10：``Standard Wi-Fi Connected`` が**No** （いいえ）で不合格。
   DSがまだロボットに接続されていません。デバイス接続前にDriver Station Nameを修正してください。
-  項目11：``Driver Station Name`` がFTC命名規則に合致していないため不合格。**Android_a301** は新規DSの例です。
   DSアプリ設定でDriver Station Nameを競技マニュアルのルールに従い設定してください（例：99999-DS）。
-  項目12：``Robot Controller Name`` がDS名と一致しないため不合格。**None** はDSがRCに接続されていないことを示します。
   RC名の形式が有効かどうかはチェックせず、RC名とDS名のチーム番号部分が一致しているかのみ確認します。
-  項目13：DSデバイスにRCアプリがインストールされている場合は不合格。Driver StationデバイスからRCアプリをアンインストールしてください。
```

### Block 28 (line 121)

```
各問題を修正すると、検査レポートが自動で更新され、最新状態が表示されます。
```

### Block 29 (line 124)

```
   Self Inspect 画面の赤丸やオレンジ三角の感嘆符アイコンをタップすると、問題に関するメッセージが一時的に表示されます。
```

### Block 30 (line 126)

```
Robot Controller Self Inspect レポート
```

### Block 31 (line 129)

```
次は**Robot Controller** Self Inspect レポートです。
通常は**Driver Station** のInspection Reports画面から「Inspect Robot Controller」メニューを選択して表示します。
参考：Control HubのHDMIポートに外部モニター、USBポートにマウスを接続すれば、Control HubからRCインスペクトレポートを直接表示できます。
```

### Block 32 (line 138)

```
   RC Password以外はすべて正常
```

### Block 33 (line 140)

```
-  項目1：三点リーダーはメニューで、``Disable Bluetooth`` のみ選択可能です。
   Control HubでBluetoothが有効になっている場合以外は不要です。
-  項目2：``Manufacturer`` はREV Control Hubの場合、**REV Robotics** である必要があります。
-  項目3：``Model`` は**Control Hub v1.0** である必要があります。
-  項目4：``Control Hub OS Version`` は最低でも1.1.6である必要があります。**FIRST** は最新版の使用を推奨しますが、必須ではありません。
-  項目5：``Android Version`` はControl Hubの場合、通常7.1.2です。
-  項目6：``Hub Firmware`` はハブのアドレスとファームウェアバージョンを表示します。
   この例ではControl Hubのみですが、Expansion Hubも表示可能です。
   チェックマークはRCアプリのバージョンに基づき、すべてのファームウェアが最新であることを示します。
   **FIRST** は最新版の使用を推奨しますが、必須ではありません。
-  項目7：``Battery Level`` はデバイスのバッテリー残量を表示します。
-  項目8：``Bluetooth`` は**Disabled** （無効）である必要があります。
-  項目9：``RC Password`` は RC Self Inspect のみに表示されます。この項目が不合格の場合、Control Hubの初期パスワード（"password"）から変更されていないことを示します。
   Program and ManageページでManageを選択し、RCパスワードを更新してください。
   DSとRCの再ペアリング後、新しいパスワードを入力して再接続する必要があります。
-  項目10：``Wi-Fi Enabled`` は**Yes** （はい）である必要があります。Control HubのWi-Fiが**ON** であることを示します。
-  項目11：``Standard Wi-Fi Connected`` は**Yes** （はい）である必要があります。
-  項目12：``Robot Controller Name`` はFTC命名規則に合致している必要があります。チーム番号＋-RC（例：99999-RC）です。
   予備デバイスの場合は、<チーム番号>-<英字>-RC（例：12345-A-RC、12345-B-RC）となります。命名規則は競技マニュアルを参照してください。
-  項目13：Apps Installed ``Robot Controller`` はRCアプリのバージョンを表示します。**FIRST** は最新版の使用を推奨しますが、必須ではありません。
-  項目14：``Matches DS Version`` は**Yes** （はい）である必要があります。**No** の場合はバージョンの小数点以下（例：10.0と10.1）が一致していないことが原因です。バージョン不一致は許容されますが、推奨されません。
-  項目15：Apps Installed ``Driver Station`` は**Not installed** （未インストール）である必要があります。Robot ControllerデバイスにDriver Stationアプリがインストールされていないことを確認します。
   各デバイスにはFTCアプリを1つだけインストールしてください。両方インストールすると正常に動作しない場合があります。
-  項目16：RCインスペクトレポートの最下部にはQRコードが表示され、検査員がタブレットを使って検査チェックリスト項目を自動入力できます。
```

### Block 34 (line 170)

```
   検査員は検査時にQRコードをスキャンする場合があります
```

### Block 35 (line 172)

```
まとめ
```

### Block 36 (line 175)

```
Self Inspect 画面は、制御システムの各要素が最新かつ正しく構成されているかをチームが確認するための、簡易的な参考情報です。
```

### Block 37 (line 177)

```
Self Inspect はFTC大会のロボット検査時に参照されることがありますが、FTCルールへの完全な準拠や公式基準を示すものでは**ありません** 。
```

### Block 38 (line 179)

```
各検査画面は、ロボットの再起動有無にかかわらず自動で更新されるため、問題が解決されたかをすばやく確認できます。
```


## hardware_and_software_configuration/self_inspect/self-inspect.rst

### Block 1 (line 1)

```
旧 Self-Inspect
```

### Block 2 (line 4)

```
はじめに
```

### Block 3 (line 7)

```
このページでは、FTC Driver Station（DS）アプリと FTC Robot Controller（RC）アプリにある旧式の Self Inspect 画面について説明します。
バージョン 10.3 以降の画面画像は :doc:`new self-inspect<new-self-inspect>` を参照してください。
```

### Block 4 (line 10)

```
Self Inspect 画面は、制御システムに関する FTC ルールとの関連で、デバイスの状態をスナップショットとして示します。
これらのルールは *FIRST* ウェブサイトの `Current Game and Season Materials page <https://ftc-resources.firstinspires.org/files/ftc/game>`__ に掲載されている Competition Manual に記載されています。
```

### Block 5 (line 15)

```
Self Inspect 画面は、制御システムの要素が最新かつ正しく設定されているかをチームがすぐに確認するための簡易リファレンスとして提供されています。
FTC 大会の Robot Inspection で確認されることはありますが、FTC ルールへの準拠を網羅的に、あるいは公式に保証するものでは **ありません** 。
```

### Block 6 (line 18)

```
各検査画面は、Restart Robot の有無にかかわらず自動で更新されます。これにより、問題が解消されたことを素早く確認できます。
```

### Block 7 (line 20)

```
小さな画面に有用な情報を最大限に詰め込むことが課題です。Self Inspect のレイアウトとグラフィックは FTC の要件に合わせて進化しており、このページでは簡潔ながら重要なキャプションを補足します。
```

### Block 8 (line 23)

```
  ここに示す画像は FTC アプリのバージョン 7.0 です。使用が認められるソフトウェアのバージョンは Competition Manual を参照してください。これらの画像は FTC アプリのバージョン 10.2 まで有効です。バージョン 10.3 以降の画面画像は :doc:`new self-inspect<new-self-inspect>` を参照してください。
```

### Block 9 (line 25)

```
デバイスのペアリング
```

### Block 10 (line 28)

```
ペアリングの方法は Self Inspect の結果に大きく関わります。RC スマホは **Wi-Fi Direct** でホストし、Control Hub は**Standard（インフラストラクチャ）Wi-Fi** でホストすることを覚えておいてください。
```

### Block 11 (line 30)

```
DS アプリの Settings で選択した Pairing Method（Wi-Fi Direct または Control Hub）が、DS Self Inspect レポートでの合否判定に影響します。以下の例で説明します。
```

### Block 12 (line 32)

```
RC スマホと DS スマホはともに Airplane Mode を **ON**、Wi-Fi を**ON** としつつ、インターネットルーターやホットスポットなど Standard/infra Wi-Fi ホストには接続しないでください。近くの Wi-Fi は**Forget** に設定しておく必要があります。
```

### Block 13 (line 34)

```
FTC 制御デバイスの組み合わせは次のとおりです。
```

### Block 14 (line 36)

```
- **DS** スマホ +**RC** スマホ
- **DS** スマホ +**Control Hub**
- **Driver Hub**+**RC** スマホ
```

### Block 15 (line 41)

```
DS デバイス（スマホまたは Driver Hub）は自分自身の DS Self Inspect **と** 、ペアになっている RC スマホまたは Control Hub の RC Self Inspect を表示できます。RC スマホは自分自身の RC Self Inspect のみ表示できます。
```

### Block 16 (line 43)

```
つまり Self Inspect 画面は次のように表示されます。
```

### Block 17 (line 47)

```
- `DS Self Inspect 1 <#ds-self-inspect-1-on-ds-phone-paired-to-rc-phone>`__ （**DS** スマホ +**RC** スマホ）
- `DS Self Inspect 2 <#ds-self-inspect-2-on-ds-phone-paired-to-control-hub>`__ （**DS** スマホ +**Control Hub** ）
- `DS Self Inspect 3 <#ds-self-inspect-3-on-driver-hub-paired-to-rc-phone>`__ （**Driver Hub**+**RC** スマホ）
```

### Block 18 (line 54)

```
- `RC Self Inspect 1 <#rc-self-inspect-1-appearing-on-rc-phone-paired-with-ds-phone>`__ （RC スマホ上、DS スマホとペア）
- `RC Self Inspect 2 <#rc-self-inspect-2-appearing-on-ds-phone-paired-to-rc-phone>`__ （DS スマホ上、RC スマホとペア）
- `RC Self Inspect 3 <#rc-self-inspect-3-appearing-on-rc-phone-paired-with-driver-hub>`__ （RC スマホ上、Driver Hub とペア）
- `RC Self Inspect 4 <#rc-self-inspect-4-appearing-on-driver-hub-paired-to-rc-phone>`__ （Driver Hub 上、RC スマホとペア）
- `RC Self Inspect 5 <#rc-self-inspect-5-appearing-on-ds-phone-paired-to-control-hub>`__ （DS スマホ上、Control Hub とペア）
- `RC Self Inspect 6 <#rc-self-inspect-6-appearing-on-driver-hub-paired-to-control-hub>`__ （Driver Hub 上、Control Hub とペア）
```

### Block 19 (line 61)

```
これらの組み合わせでは、Self Inspect のカテゴリや表示文言、合否結果が**わずかに異なる** ことがあります。各デバイスと組み合わせの Self Inspect 画面は、以下の**青いリンク** をクリックして確認してください。
```

### Block 20 (line 65)

```
DS Self Inspect 1（DS スマホ + RC スマホ）
```

### Block 21 (line 73)

```
   DS Self Inspect 1（DS スマホ + RC スマホ）
```

### Block 22 (line 75)

```
- 項目 1 は 1 つだけ選べるメニューで、“Disconnect from Wi-Fi Direct” です。機能しますが、アプリが自動で再ペアリングする場合があります。
- 項目 5 には対象デバイスのバッテリー残量が表示されます。豆知識として、パーセンテージの緑色は残量が減るにつれて **オレンジ** に変わっていきます。
- 項目 8 の ``Location services`` は **Android 8** 以上のデバイスにだけ表示されます。これは SDK/Android の技術要件であり、FTC ルールではありません。
- 項目 9 と 10 は「Yes」「No」である必要があります。``Wi-Fi Enabled`` は DS デバイスの Wi-Fi 無線が Wi-Fi Direct を使うために **ON** であることを意味します。RC スマホとペアにする際は、インターネットルーターや Control Hub など Standard/インフラ Wi-Fi には** 接続しない** でください。
- 項目 11 は **デバイスの Wi-Fi Direct 名** が FTC の形式要件を満たしているかを示します。ペア相手の RC 名（チーム番号）が一致しているかは確認しません。この例では 2468-A-DS と 2468-A-RC という合法名です。DS Settings（Driver Station Name）では FTC 合法名のみ入力できますが、DS スマホの Android Wi-Fi Direct 設定では任意の名前を入力できます。
- 項目 12 は DS デバイスに RC アプリが **インストールされていない** ことを確認します。
- 項目 13 は、デバイスのシステム日付に基づき、DS アプリが **当該 FTC シーズンの最小バージョン** を満たしているかを確認します。ここが「incorrect」で赤く表示された場合は、**Android の設定** で日付を修正すると解消します。
```

### Block 23 (line 83)

```
同じ電話で Self Inspect が多くの項目を**不合格** とした例がこちらです。
```

### Block 24 (line 90)

```
   DS Self Inspect 1（DS スマホ）– 不合格例
```

### Block 25 (line 92)

```
- 項目 6 は ``Airplane Mode`` が **OFF** であるため不合格です。FTC 用の電話では ON にする必要があります。これは Android システム設定で、設定メニューから、または画面上部を 2 回スワイプダウンして簡単にアクセスできます。Airplane Mode を ON にすると Android の「便利機能」として自動で Wi-Fi 無線が OFF になります。FTC ユーザーは手動で Wi-Fi 無線を ON に戻してください（ローカルホットスポットやインターネットルーターには接続しないでください）。
- 項目 7 は ``Bluetooth`` が **ON** なので不合格です。FTC では OFF にする必要があります。これも Android システム設定で、2 回スワイプダウンするか設定メニューを開いてください。
- 項目 8 は ``Location services`` が **OFF** なので不合格です。**Android 8** 以上では FTC アプリが位置情報を必要とします。これも Android システム設定で、2 回スワイプダウンするか設定メニューを確認してください。
- 項目 9 は DS スマホの Wi-Fi 無線が **ON** であることを示し、RC への Wi-Fi Direct 接続または Standard Wi-Fi 接続に必要です。
- 項目 10 は、DS の Pairing Method が Wi-Fi Direct（RC スマホと接続する前提）なのに、DS スマホが Standard/インフラ Wi-Fi に接続しているため不合格です。この例では家庭用 Wi-Fi に接続しています。こうしたネットワークはデバイスの Android Wi-Fi メニューで **Forget** に設定してください。一時的にインターネットが必要な場合は、使用後に必ず Forget に戻します。また、インターネット利用中に使った Google などのアカウントは**Remove Account** してください。そうしたアカウントはバックグラウンドでの通信や通知、アップデートを引き起こし、最悪のタイミングで妨げになることがあります。
- 項目 11 はデバイスの **Wi-Fi Direct 名** が FTC の形式要件を満たしていないため不合格です。この不適切な名前は DS スマホの Android Wi-Fi Direct 設定で付けたもので、アプリの DS Settings（Driver Station Name）では設定できません。
- 項目 12 は、この DS デバイスに RC アプリがインストールされているため不合格です。不合格の理由は旧バージョン（6.2）であることではなく、RC アプリが存在すること自体です。
```

### Block 26 (line 102)

```
DS Self Inspect 2（DS スマホ + Control Hub）
```

### Block 27 (line 110)

```
   DS Self Inspect 2（DS スマホ + Control Hub）
```

### Block 28 (line 112)

```
基本的なポイントは DS Self Inspect 1 と同じですが、次の点が異なります。
```

### Block 29 (line 114)

```
- 項目 9 と 10 はどちらも Yes である必要があります。DS スマホの Wi-Fi 無線は **ON** で、Standard/インフラ Wi-Fi に接続しています。何に接続しているかは項目 11 で示されます。
- DS の Pairing Method が Wi-Fi Direct（RC スマホと接続する前提）に設定されていると、項目 10 の Yes は **不合格** になります。
- 項目 11 には DS スマホが接続している Standard Wi-Fi の **ネットワーク名（Access Point, AP）** が表示されます。チェックマークは、その AP が FTC 合法デバイス（Control Hub）であり、名前が正しい形式であることを示します。DS 名と RC 名（チーム番号）が一致しているかは確認しません。この例では DS スマホは 2468-A-DS、Control Hub は 9999-A-RC であり、FTC チームまたは Robot Inspector が指摘すべき**違反の組み合わせ** です。
```

### Block 30 (line 120)

```
DS Self Inspect 3（Driver Hub + RC スマホ）
```

### Block 31 (line 128)

```
   DS Self Inspect 3（Driver Hub + RC スマホ）
```

### Block 32 (line 130)

```
- 項目 4 は Driver Hub のみに表示されます。チェックマークは、Operating System が FTC Competition Manual の最小バージョン要件を満たしていることを示します。
- Driver Hub では DS 側の検査から ``Airplane Mode`` が省かれています。FTC ルールでは Driver Hub と Control Hub は Airplane Mode 要件の対象外です。
- 項目 8 の ``Location services`` は **Android 8** 以上のデバイスにだけ表示されます。これは SDK/Android の技術要件であり、FTC ルールではありません。
- 項目 9 と 10 は「Yes」「No」である必要があります。``Wi-Fi Enabled`` は Driver Hub の Wi-Fi 無線が RC スマホとの Wi-Fi Direct 用に **ON** であることを意味します。Driver Hub は技術的には Standard/インフラ Wi-Fi（インターネットルーターや Control Hub を含む）にも** 同時接続できてしまう** ため、項目 10 で接続していないことを確認します。次の例を参照してください。
- DS の Pairing Method が Control Hub に設定されている場合、項目 10 の No は **不合格** になります。
- 項目 11 は **デバイス名** が FTC の形式要件を満たしているかを示します。ペア相手の RC 名（チーム番号）が一致しているかは確認しません。
- 項目 12 は Driver Hub に RC アプリが **インストールされていない** ことを確認します。
- 項目 13 は、デバイスのシステム日付に基づき、DS アプリが **当該 FTC シーズンの最小バージョン** を満たしているかを確認します。この例では DS アプリ 7.0.1 が RC スマホの 7.0 と完全一致していませんが、こうした「Point mismatch」は FTC の最新ルール（2021-2022 シーズンの Q&A #176）で許容されています。それ以外で赤い「incorrect」になる場合は**Android の設定** で日付を修正してください。
```

### Block 33 (line 144)

```
   DS Self Inspect 3（Driver Hub + RC スマホ）
```

### Block 34 (line 146)

```
この Self Inspect 画面は、Driver Hub が RC スマホとペアリングされている最中に、さらに Standard Wi-Fi 経由で Control Hub に *同時接続* した際に表示されました。DS のホーム画面は一時的に「Connected」（RC スマホ）と「No Heartbeat」を示しましたが、その後 RC スマホとのペアリングに戻りました。
```

### Block 35 (line 148)

```
- 項目 10 がこの不整合を示しています。DS アプリはまもなくこの Standard Wi-Fi 接続を切断し、Driver Hub が RC スマホとのみペアを維持するようにします。
```

### Block 36 (line 162)

```
- 項目 1 には引き続き “Disconnect from Wi-Fi Direct” しかありませんが、選択すると “There was an error disconnecting from Wi-Fi Direct” と表示されます。Driver Hub は Control Hub とペアになっており、Wi-Fi Direct ではないためです。
- DS の Pairing Method が Wi-Fi Direct（RC スマホと接続する前提）に設定されていると、項目 10 の Yes は **不合格** になります。
- 項目 11 には Driver Hub が接続している Standard Wi-Fi の **ネットワーク名（AP）** が表示されます。チェックマークは、その AP が FTC 合法デバイス（Control Hub）であり、名前が正しい形式であることを示します。DS 名と RC 名（チーム番号）が一致しているかは確認しません。この例では Driver Hub は 1234-A-DS、Control Hub は 9999-A-RC であり、FTC チームまたは Robot Inspector が指摘すべき**違反の組み合わせ** です。
```

### Block 37 (line 173)

```
この Self Inspect 画面は Driver Hub を Control Hub とペアリングした後、Wi-Fi インターネットルーターに接続した際に表示されました。
```

### Block 38 (line 175)

```
- 項目 11 がエラーを示しています。Driver Hub が Standard Wi-Fi で接続できる AP は同時に 1 つだけで、このネットワークは FTC の RC デバイスではありません。
```

### Block 39 (line 179)

```
RC Self Inspect 1（RC スマホ + DS スマホ）
```

### Block 40 (line 182)

```
ここからは **Robot Controller** の Self Inspect 画面です。RC 画面は DS デバイス** または** RC スマホから表示できますが、細かな違いがあります。
```

### Block 41 (line 189)

```
   RC Self Inspect 1（RC スマホ + DS スマホ）
```

### Block 42 (line 191)

```
- 項目 5 には Expansion Hub のアドレスとファームウェアバージョンが一覧表示されます。この例では 1 台ですが、2 台まで表示されます。チェックマークは RC アプリの現行バージョンに対して全ファームウェアが最新であることを示します。Hub が接続されていない場合は “N/A” と表示されます。
- 項目 10 の ``RC Password`` は RC Self Inspect のみに表示され、DS Self Inspect にはありません。Control Hub のパスワードを工場出荷時の “password” から変更するという FTC 要件をチェックします。Control Hub 向けの項目ですが、デフォルトパスワードを持たない RC スマホにも表示され、常にチェックマークになります。
- 項目 14 は、デバイスのシステム日付に基づき、RC アプリが **当該 FTC シーズンの最小バージョン** を満たしているかを確認します。DS アプリとのバージョン一致は確認しません。ここが赤い「incorrect」の場合は**Android の設定** で日付を修正してください。
- 項目 15 は RC デバイスに DS アプリが **インストールされていない** ことを確認します。
```

### Block 43 (line 198)

```
RC Self Inspect 2（DS スマホ上、RC スマホとペア）
```

### Block 44 (line 206)

```
   RC Self Inspect 2（DS スマホ上、RC スマホとペア）
```

### Block 45 (line 208)

```
この RC Self Inspect は、ペアリングしている DS スマホ上に表示されたもので、直前の RC スマホ上の画面と「同じ」ですが、2 点だけ異なります。
```

### Block 46 (line 210)

```
- ヘッダーの三点メニューがありません。このメニューは Wi-Fi Direct を切断する 1 つの選択肢を提供しますが、同じ Wi-Fi Direct 接続を使っている DS スマホから RC 側の操作として切断することはできません。
- 項目 14 は RC スマホ上の画面にはありませんでした。ここでは DS アプリと RC アプリのバージョンが一致していることを確認しており、この例では両方とも 7.0 です。7.0 と 7.0.1 のような「Point mismatch」は FTC の最新ルール（2021-2022 シーズンの Q&A #176）で許容されています。
```

### Block 47 (line 215)

```
RC Self Inspect 3（RC スマホ + Driver Hub）
```

### Block 48 (line 223)

```
   RC Self Inspect 3（RC スマホ + Driver Hub）
```

### Block 49 (line 225)

```
この画面は RC Self Inspect 1（DS デバイスが DS スマホ）の場合と同じです。そちらの説明を参照してください。
```

### Block 50 (line 232)

```
   RC Self Inspect 3（RC スマホ + Driver Hub）
```

### Block 51 (line 234)

```
こちらも同じ画面ですが、RC スマホが Driver Hub とペアになったままインターネットルーターに接続した例です。Standard Wi-Fi 接続により RC スマホは一時的にペアリングを失いましたが、復旧できました。
```

### Block 52 (line 236)

```
- 項目 12 が不合格を示しています。Standard Wi-Fi には接続していますが、接続先が FTC の DS デバイス **ではありません** 。
```

### Block 53 (line 240)

```
RC Self Inspect 4（Driver Hub 上、RC スマホとペア）
```

### Block 54 (line 248)

```
   RC Self Inspect 4（Driver Hub 上、RC スマホとペア）
```

### Block 55 (line 250)

```
Driver Hub 上に表示されたこの画面は直前のものと「同じ」ですが、2 点異なります。
```

### Block 56 (line 252)

```
- ヘッダーの三点メニューがありません。このメニューは Wi-Fi Direct を切断する 1 つの選択肢を提供しますが、同じ Wi-Fi Direct 接続を使っている Driver Hub から RC 側の操作として切断することはできません。
- 項目 14 は RC スマホ上の画面にはありませんでした。ここでは DS アプリと RC アプリのバージョン一致を確認しており、この例では DS アプリ 7.0.1、RC アプリ 7.0 で不一致として表示されています。こうした「Point mismatch」は FTC の最新ルール（2021-2022 シーズンの Q&A #176）で許容されています。
```

### Block 57 (line 257)

```
RC Self Inspect 5（DS スマホ上、Control Hub とペア）
```

### Block 58 (line 260)

```
ここから **Control Hub** の例です。Self Inspect 画面にいくつか違いがあります。この例ではロボットに**2 台** の Hub が構成されています。
```

### Block 59 (line 267)

```
   RC Self Inspect 5（DS スマホ上、Control Hub とペア）
```

### Block 60 (line 269)

```
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
```

### Block 61 (line 284)

```
RC Self Inspect 6（Driver Hub 上、Control Hub とペア）
```

### Block 62 (line 287)

```
Control Hub の場合、Driver Hub に表示される Self Inspect のカテゴリは直前の DS スマホの場合と同じです。
```

### Block 63 (line 294)

```
   RC Self Inspect 6（Driver Hub 上、Control Hub とペア）
```

### Block 64 (line 296)

```
ここで唯一異なる報告は、Driver Hub の DS アプリ 7.0.1 と Control Hub の 7.0 との「不一致」です。Driver Hub は自動更新されることが多く、古い Android 6 向けの DS バージョンが入る場合があります。こうした「Point mismatch」は FTC の最新ルール（2021-2022 シーズンの Q&A #176）で許容されています。
```

### Block 65 (line 303)

```
   RC Self Inspect 6（過去に Control Hub とペアだった Driver Hub）
```

### Block 66 (line 305)

```
最後に、アクティブな接続がない場合、DS デバイスは RC デバイスの状態を何も表示できません。
```

### Block 67 (line 307)

```
まとめ
```

### Block 68 (line 310)

```
Self Inspect 画面は、制御システムの要素が最新かつ正しく設定されていることをチームが確認するための、手早く便利なリファレンスです。
```

### Block 69 (line 312)

```
Self Inspect は FTC 大会の Robot Inspection で確認されることがありますが、FTC ルールへの準拠を網羅的または公式に保証するものでは **ありません** 。
```

### Block 70 (line 314)

```
各検査画面は Restart Robot の有無にかかわらず自動更新されるため、問題が解消されたことを素早く確認できます。
```

### Block 71 (line 318)

```
ご質問・ご意見・修正提案は westsiderobotics@verizon.net までお寄せください。
```


## index.rst

### Block 1 (line 2)

```
   :title: FIRST Tech Challenge ドキュメント
   :description: FIRST Tech Challenge ドキュメントの公式ホーム。
```

### Block 2 (line 6)

```
*FIRST* Tech Challenge ドキュメント
```

### Block 3 (line 9)

```
*FIRST®* Tech Challenge ドキュメントへようこそ！このウェブサイトには、競技用ロボットを作成するために必要なすべての情報が含まれています！
*FIRST* Tech Challenge のソフトウェアとロボット制御システムの使用方法に関する情報とチュートリアルがあります。
また、コーチやメンターのための情報も提供しています。
```

### Block 4 (line 13)

```
*FIRST* Tech Challenge は中高生向けのロボティクスプログラムです。
単にロボットを作るだけではありません。その理由については :doc:`FIRST Tech Challenge について <overview/ftcoverview>` と :doc:`gracious_professionalism/gp` をご覧ください。
```

### Block 5 (line 24)

```
   :caption: 始め方
```

### Block 6 (line 34)

```
   :caption: ゲームとシーズン固有のリソース
```

### Block 7 (line 41)

```
   競技マニュアル <manuals/game_manuals/game_manuals>
   ゲーム Q&A システム <game_specific_resources/ftcqa/ftcqa>
```

### Block 8 (line 44)

```
   フィールド座標系 <game_specific_resources/field_coordinate_system/field-coordinate-system>
```

### Block 9 (line 47)

```
   :caption: ソフトウェア開発キット (SDK)
```

### Block 10 (line 51)

```
   ラップトップ要件 <programming_resources/laptops/laptops>
   SDK 概要 <ftc_sdk/overview/index>
   コンポーネントの更新 <ftc_sdk/updating/index>
```

### Block 11 (line 56)

```
   :caption: ロボット製作リソース
```

### Block 12 (line 62)

```
   :caption: 制御システムリソース
```

### Block 13 (line 74)

```
   :caption: AprilTag リソース
```

### Block 14 (line 78)

```
   AprilTag 入門 </apriltag/vision_portal/apriltag_intro/apriltag-intro>
   VisionPortal 概要 </apriltag/vision_portal/visionportal_overview/visionportal-overview>
   VisionPortal 用ウェブカメラ </apriltag/vision_portal/visionportal_webcams/visionportal-webcams>
   AprilTag 値の理解 </apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values>
   AprilTag ローカリゼーション </apriltag/vision_portal/apriltag_localization/apriltag-localization>
   AprilTag テスト画像 </apriltag/opmode_test_images/opmode-test-images>
   AprilTag 高度な使用法 </apriltag/vision_portal/apriltag_advanced_use/apriltag-advanced-use>
   AprilTag カメラキャリブレーション </apriltag/vision_portal/apriltag_camera_calibration/apriltag-camera-calibration>
   AprilTag ID とコード </apriltag/vision_portal/apriltag_id_code/apriltag-id-code>
   AprilTag ライブラリ </apriltag/vision_portal/apriltag_library/apriltag-library>
   AprilTag メタデータ </apriltag/vision_portal/apriltag_metadata/apriltag-metadata>
   AprilTag ポーズ </apriltag/vision_portal/apriltag_pose/apriltag-pose>
   AprilTag 参照フレーム </apriltag/vision_portal/apriltag_reference_frame/apriltag-reference-frame>
   Vision マルチポータル </apriltag/vision_portal/vision_multiportal/vision-multiportal>
   Vision プロセッサーの初期化 </apriltag/vision_portal/vision_processor_init/vision-processor-init>
   VisionPortal カメラコントロール </apriltag/vision_portal/visionportal_camera_controls/visionportal-camera-controls>
   VisionPortal CPU と帯域幅 </apriltag/vision_portal/visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth>
   VisionPortal 初期化 </apriltag/vision_portal/visionportal_init/visionportal-init>
   VisionPortal プレビュー </apriltag/vision_portal/visionportal_previews/visionportal-previews>
```

### Block 15 (line 99)

```
   :caption: CAD リソース
```

### Block 16 (line 103)

```
   コンピューター支援設計 (CAD) <cad_resources/index>
```

### Block 17 (line 106)

```
   :caption: 静電気放電
```

### Block 18 (line 110)

```
   ESD 影響の管理 <hardware_and_software_configuration/configuring/managing_esd/managing-esd>
```

### Block 19 (line 113)

```
   :caption: 製造
```

### Block 20 (line 117)

```
   製造方法 <manufacturing/index>
```

### Block 21 (line 120)

```
   :caption: チームリソース
```

### Block 22 (line 125)

```
   チーム無償ソフトウェア<sponsors/software/software>
   チーム割引<sponsors/discounts/discounts>
```

### Block 23 (line 130)

```
   :caption: FTC ドキュメント
```

### Block 24 (line 134)

```
   ブックレット<booklets/index>
   アーカイブ <https://ftc-docs.firstinspires.org/projects/ftcdocs-archive/en/latest/index.html>
   サイトフィードバックフォーム<ftc_docs/form/form>
   FTC Docs への貢献<contrib/index>
```

### Block 25 (line 141)

```
**私は...**
```

### Block 26 (line 143)

```
- :doc:`新規チーム <persona_pages/rookie_teams/rookie_teams>` 新規チームの皆さんは、どこから始めればよいか分からないかもしれません。こちらから始めましょう！
```

### Block 27 (line 145)

```
- :doc:`既存チーム <persona_pages/veteran_teams/veteran_teams>` リソースをお探しの既存チームの皆さんはこちらをご覧ください。
```

### Block 28 (line 147)

```
- :doc:`コーチ <persona_pages/coach_admin/coach_admin>` ヘルプやチーム管理リソースをお探しのコーチの皆さんはこちらをご覧ください。
```

### Block 29 (line 149)

```
- :doc:`メンター <persona_pages/mentor_tech/mentor_tech>` 技術リソースをお探しの技術メンターの皆さんは、まずこちらをご覧ください！
```

### Block 30 (line 151)

```
メインメニューには、トップレベルのコンテンツへのリンクが含まれています。以下は、トピック別に整理されたクイックリンクです。
```

### Block 31 (line 160)

```
      プログラミングリンク
```

### Block 32 (line 164)

```
      プログラミング言語リソースへのクイックリンク
```

### Block 33 (line 218)

```
               すべてのリソース
```

### Block 34 (line 224)

```
      制御システムリンク
```

### Block 35 (line 228)

```
      *FIRST* Tech Challenge 制御システムについて学びましょう！
```

### Block 36 (line 262)

```
               デバイス接続
```

### Block 37 (line 272)

```
               ハードウェア構成
```

### Block 38 (line 278)

```
      ソフトウェア開発キット (SDK)
```

### Block 39 (line 282)

```
      ソフトウェア開発キット (SDK) は、ソフトウェアを開発し、ロボット上で実行するためのツール群です。
```

### Block 40 (line 296)

```
               SDK について
```

### Block 41 (line 306)

```
               SDK GitHub リポジトリ
```

### Block 42 (line 315)

```
               SDK リリース
```

### Block 43 (line 324)

```
               Javadoc ドキュメント
```

### Block 44 (line 330)

```
      ゲームリンク
```

### Block 45 (line 334)

```
      競技のすべてのルールに従っていることを確認してください！
      競技マニュアルは必須のドキュメントです。
```

### Block 46 (line 349)

```
               競技マニュアル
```

### Block 47 (line 366)

```
               ゲーム Q&A システム
```

### Block 48 (line 369)

```
   このプロジェクトは活発に開発中です。ここに含まれる情報はすべて参考目的のみです。このドキュメントはチームをサポートし、ゲームルールに対する文脈を提供することを目的としていますが、ゲームルールがここで見つかるすべてのドキュメントに優先します。このプロジェクトに関するフィードバックがある場合は、:doc:`フィードバックフォーム <ftc_docs/form/form>` をご利用ください。
   また、これは非公式日本語訳です。不正確な翻訳や解釈の誤りについては責任を負いかねます。公式な情報は必ず英語版ドキュメントをご参照ください。
```


## overview/ftcoverview.rst

### Block 1 (line 1)

```
*FIRST* Tech Challenge について
```

### Block 2 (line 4)

```
単にロボットを作るだけではありません。*FIRST* Tech Challenge チーム（最大15名のチームメンバー、中学1年生～高校3年生）は、ロボットを設計、製作、プログラム、操作し、アライアンス形式の対戦競技に挑戦します。
```

### Block 3 (line 6)

```
大人のコーチやメンターの指導のもと、学生たちはSTEMスキルを習得し、エンジニアリングの原理を実践しながら、努力、革新、チームワークの価値を実感します。
```

### Block 4 (line 8)

```
ロボットキットは毎年使い回すことができ、様々なレベルのグラフィカルプログラミングやJavaベースのプログラミングを使用してコーディングできます。チームはロボットを設計・製作し、資金を調達し、チームブランドを設計・マーケティングし、地域貢献活動を行って特定の賞を獲得します。参加者は、将来の教育、就職、その他の雇用経路を探求することが奨励されています。
```

### Block 5 (line 13)

```
各シーズンは、地域チャンピオンシップイベントとエキサイティングな |text|_ で締めくくられます。
```

### Block 6 (line 21)

```
*FIRST* Tech Challenge チームを始める
```

### Block 7 (line 24)

```
*FIRST* Tech Challenge チームは、再利用可能なパーツキットを使用してロボットを設計・製作し、共通のゲームルールのもとでエキサイティングなフィールドゲームをプレイし、特定のシーズンチャレンジを達成します。ロボットゲームは毎シーズン変わり、常に楽しいものです！
```

### Block 8 (line 26)

```
学生と大人のチームメンバーは、プログラミング、電子工学、金属加工、グラフィックデザイン、ウェブ制作、スピーチ、ビデオ撮影など、すでに持っているスキルを持ち寄ることが奨励されています。**FIRST Tech Challenge** は、特別なスキルの有無に関わらず、すべての学生を歓迎します。
```

### Block 9 (line 28)

```
**FIRST** を教室やアフタースクールプログラムに組み込むことを検討している場合は、最大24名の学生向けの柔軟な実施オプションである**FIRST Class Pack** について詳しく学んでください。
```

### Block 10 (line 33)

```
**FIRST** Tech Challenge チームを始めるための |text2|_ について学びましょう。
```

### Block 11 (line 39)

```
*FIRST* Tech Challenge Kahoot について
```

### Block 12 (line 42)

```
これは、*FIRST* Tech Challenge の知識をテストし、構築するための楽しい自習式 `Kahoot
<https://create.kahoot.it/course/f79560a1-df68-44dd-bbef-d8c9bf5a27f5>`__ です。
*FIRST* Tech Challenge の多くの側面と *FIRST* のコアバリューについて学びましょう。*FIRST* Tech Challenge `Kahoot
<https://create.kahoot.it/course/f79560a1-df68-44dd-bbef-d8c9bf5a27f5>`__ でお楽しみください。
```


## persona_pages/coach_admin/coach_admin.rst

### Block 1 (line 1)

```
コーチ（管理）リソース
```

### Block 2 (line 4)

```
*FIRST* Tech Challenge コーチのページへようこそ！リソースは種類別に整理されており、チームがシーズンを通して組織的かつ円滑に活動できるようになっています。これらのリソースは、*FIRST* の理念を推進しながらチームを管理するコーチや管理者のニーズに焦点を当てています。探したいリソースのボタンをクリックするだけです！
```

### Block 3 (line 62)

```
      *FIRST* ダッシュボードリンク
```

### Block 4 (line 66)

```
      登録と購入に関するFAQをご覧ください。チーム登録には firstinspires.org の *FIRST*
      ダッシュボードアカウントアクセスが必要です。
```

### Block 5 (line 80)

```
               チームを登録する（外部ログイン）
```

### Block 6 (line 89)

```
               ユース登録（外部リンク）
```

### Block 7 (line 95)

```
      チームマネジメント
```

### Block 8 (line 99)

```
      チームにペース配分の取れた成功するシーズンを提供するためのリソースです。
```

### Block 9 (line 112)

```
               チームマネジメントリソース（外部リンク）
```

### Block 10 (line 118)

```
      コーチガイダンス
```

### Block 11 (line 122)

```
      新人コーチ向けのベストプラクティスをご紹介します。
```

### Block 12 (line 135)

```
               メンターマニュアル（外部PDF）
```

### Block 13 (line 141)

```
      イベント前チェックリスト
```

### Block 14 (line 145)

```
      競技に備えるためのシンプルなチェックリストです。リンク先のページの「競技への準備」の見出しをご覧ください。
```

### Block 15 (line 158)

```
               競技への準備（外部リンク）
```


## persona_pages/mentor_tech/mentor_tech.rst

### Block 1 (line 1)

```
技術メンターリソース
```

### Block 2 (line 4)

```
*FIRST* Tech Challenge へ技術メンターの皆さん、ようこそ！リソースは種類別に整理されており、シーズンを通してチームと一緒に組織的かつ円滑に活動できるようになっています。これらのリソースは、技術分野で経験があり、スキルを向上させたいチームやメンター向けにカスタマイズされています。技術リソースは、業界標準の認定取得への足がかりにもなります。探したいリソースのボタンをクリックするだけです！
```

### Block 3 (line 13)

```
      制御システムリソース
```

### Block 4 (line 17)

```
      制御システムのリソースはこちらです。
```

### Block 5 (line 31)

```
               FTC 制御システム
```

### Block 6 (line 37)

```
      機械リソース
```

### Block 7 (line 41)

```
      機械工学とロボット構築のリソースです。
```

### Block 8 (line 54)

```
               ロボット構築リソース（外部リンク）
```

### Block 9 (line 60)

```
      プログラミングリソース
```

### Block 10 (line 64)

```
      プログラミングリソースへのリンクです。
```

### Block 11 (line 83)

```
      CAD リソース
```

### Block 12 (line 87)

```
      コンピューター支援設計（CAD）ソフトウェアのリソースはこちらです。
```


## persona_pages/rookie_teams/rookie_teams.rst

### Block 1 (line 1)

```
新規チーム
```

### Block 2 (line 4)

```
*FIRST* Tech Challenge へようこそ！リソースは種類別に整理されており、チームがシーズンを通して組織的かつ円滑に活動できるようになっています。まずはロボット構築リソース、制御システム、競技について調べてみましょう。また、チームマネジメントの下にあるコーチのプレイブック（週間活動スケジュール）も、チーム全体を整理するのに役立ちます。探したいリソースのボタンをクリックするだけです！
```

### Block 3 (line 13)

```
      *FIRST* コアバリュー
```

### Block 4 (line 17)

```
      私たちは *FIRST* の理念である **Gracious Professionalism**
      と **Coopertition** をコアバリューを通じて表現しています。
```

### Block 5 (line 32)

```
               Gracious Professionalism（グレイシャス・プロフェッショナリズム）
```

### Block 6 (line 44)

```
               Coopertition（クーペティション）（外部リンク）
```

### Block 7 (line 56)

```
               コアバリュー（外部リンク）
```

### Block 8 (line 62)

```
      プログラミングリソース
```

### Block 9 (line 66)

```
      プログラミングリソースはこちらです。
```

### Block 10 (line 80)

```
               プログラミングツールの選択
```

### Block 11 (line 90)

```
               Blocks プログラミングチュートリアル
```

### Block 12 (line 100)

```
               プログラミングリソース
```

### Block 13 (line 107)

```
      ロボット構築と制御
```

### Block 14 (line 111)

```
      ロボットと制御システムのリソースはこちらです。
```

### Block 15 (line 125)

```
               FTC 制御システム
```

### Block 16 (line 135)

```
               Robot Controller（ロボットコントローラー）
```

### Block 17 (line 145)

```
               Driver Station（ドライバーステーション）
```

### Block 18 (line 154)

```
               ハードウェアコンポーネント概要
```

### Block 19 (line 163)

```
               チームリソース（外部リンク）
```

### Block 20 (line 169)

```
      競技マニュアル
```

### Block 21 (line 173)

```
      競技のすべてのルールに従っていることを確認してください！
      競技マニュアルは必要不可欠なドキュメントです。
```

### Block 22 (line 188)

```
               競技マニュアル
```

### Block 23 (line 198)

```
               競技フィールドリソース
```

### Block 24 (line 207)

```
               競技Q&Aシステム（外部リンク）
```

### Block 25 (line 213)

```
      チームマネジメント
```

### Block 26 (line 217)

```
      チーム登録、メンター研修/リソース、チーム予算と資金調達、競技への準備など、チームマネジメントリソースへのリンクです。
```

### Block 27 (line 231)

```
               チームマネジメント（外部リンク）
```

### Block 28 (line 237)

```
      CAD リソース
```

### Block 29 (line 241)

```
      コンピューター支援設計（CAD）ソフトウェアのリソースはこちらです。
```

### Block 30 (line 255)

```
               CAD リソース
```

### Block 31 (line 261)

```
      イベント情報
```

### Block 32 (line 265)

```
      FTC イベントとイベント結果です。
```

### Block 33 (line 279)

```
               FTC イベント（外部リンク）
```

### Block 34 (line 289)

```
      イベント前に Awards 基準を知っておきましょう。
```

### Block 35 (line 303)

```
               FTC Awards（外部PDF）
```

### Block 36 (line 309)

```
      よくある質問
```

### Block 37 (line 313)

```
      チームからよく寄せられる質問です。
```

### Block 38 (line 327)

```
               よくある質問
```


## persona_pages/veteran_teams/veteran_teams.rst

### Block 1 (line 1)

```
既存チーム
```

### Block 2 (line 4)

```
*FIRST* Tech Challenge へおかえりなさい！リソースは種類別に整理されており、チームがシーズンを通して組織的かつ円滑に活動できるようになっています。これらのリソースは、ロボティクスの経験があり、スキルを向上させたいチーム向けにカスタマイズされています。技術リソースは、業界標準の認定取得への足がかりとなります。探したいリソースのボタンをクリックするだけです！
```

### Block 3 (line 13)

```
      プログラミングリソース
```

### Block 4 (line 17)

```
      Java プログラミングリソースはこちらです。
```

### Block 5 (line 31)

```
               OnBot Java チュートリアル
```

### Block 6 (line 41)

```
               Android Studio チュートリアル
```

### Block 7 (line 51)

```
               AprilTag 入門
```

### Block 8 (line 67)

```
      CAD リソース
```

### Block 9 (line 71)

```
      コンピューター支援設計（CAD）ソフトウェアのリソースはこちらです。
```

### Block 10 (line 91)

```
      チームマネジメント
```

### Block 11 (line 95)

```
      マーケティング、地域および業界へのアウトリーチを含むチームマネジメントリソースです。
```

### Block 12 (line 119)

```
      イベント前に Awards 基準を知っておきましょう。
```

### Block 13 (line 133)

```
               FTC Awards（外部PDF）
```


## programming_resources/android_studio_java/Android-Studio-Tutorial.rst

### Block 1 (line 1)

```
Android Studio プログラミングチュートリアル
```

### Block 2 (line 6)

```
   <h3>はじめに</h3>
```

### Block 3 (line 9)

```
このチュートリアルでは、制御システムの構成、プログラミング、操作のプロセスを段階的に説明します。このチュートリアルでは、**Android Studio** を使用して、ロボットのプログラミングを始める方法を学びます。
```

### Block 4 (line 11)

```
**Android Studio** は、Android アプリを作成するための高度な統合開発環境です。このツールは、プロフェッショナルな Android アプリ開発者が使用しているものと同じツールです。**Android Studio** は、** 豊富な Java プログラミング経験** を持つ** 上級ユーザー** にのみ推奨されます。
```

### Block 5 (line 19)

```
   :bdg-success:`AS` は、そのコンテンツが Android Studio プログラミングに固有であることを示します
```


## programming_resources/android_studio_java/config/config.rst

### Block 1 (line 1)

```
ハードウェアの構成 :bdg-success:`AS`
```


## programming_resources/android_studio_java/install/install.rst

### Block 1 (line 1)

```
**Android Studio** のインストール :bdg-success:`AS`
```


## programming_resources/android_studio_java/intro/intro.rst

### Block 1 (line 1)

```
はじめに :bdg-success:`AS`
```


## programming_resources/android_studio_java/manage/manage.rst

### Block 1 (line 1)

```
**Android Studio** プロジェクトの管理 :bdg-success:`AS`
```


## programming_resources/android_studio_java/opmode/opmode.rst

### Block 1 (line 1)

```
**Op Mode** の作成 :bdg-success:`AS`
```


## programming_resources/blocks/Blocks-Tutorial.rst

### Block 1 (line 1)

```
Blocks プログラミングチュートリアル
```

### Block 2 (line 8)

```
   <h3>はじめに</h3>
```

### Block 3 (line 10)

```
このチュートリアルでは、制御システムの構成、プログラミング、操作のプロセスを
ステップバイステップで説明します。このチュートリアルでは、**Blocks Programming Tool** を
使用して、素早く開始できるようにします。
```

### Block 4 (line 14)

```
**Blocks Programming Tool** は、プログラマーがウェブブラウザを使用して
**op modes** を作成、編集、保存できるビジュアルデザインツールです。
```

### Block 5 (line 17)

```
**FIRST** では、経験豊富なプログラマーであっても、まず**Blocks** から
始めることを推奨しています。**Blocks** を使用することが、制御システムに
慣れるための*最も簡単*で*最も速い*方法です！
```

### Block 6 (line 27)

```
   :bdg-warning:`Blocks` は、コンテンツが Blocks プログラミングに特化していることを示します
```


## programming_resources/blocks/config/config.rst

### Block 1 (line 1)

```
ハードウェアの構成 :bdg-warning:`Blocks`
```


## programming_resources/blocks/connecting/connecting.rst

### Block 1 (line 1)

```
Program & Manage サーバーへの接続 :bdg-warning:`Blocks`
```


## programming_resources/blocks/intro/intro.rst

### Block 1 (line 1)

```
はじめに :bdg-warning:`Blocks`
```


## programming_resources/blocks/opmode/opmode.rst

### Block 1 (line 1)

```
**Op Mode** の作成 :bdg-warning:`Blocks`
```


## programming_resources/blocks/reference/reference.rst

### Block 1 (line 1)

```
リファレンスドキュメント :bdg-warning:`Blocks`
```


## programming_resources/index.rst

### Block 1 (line 2)

```
   :title: プログラミングリソース、FTC Docs
   :description: FIRST Tech Challenge の公式プログラミングリソース
```

### Block 2 (line 6)

```
プログラミングリソース
```

### Block 3 (line 9)

```
このページには、制御システムコンポーネントの構成とプログラミングに役立つプログラミングチュートリアルおよび関連する制御システムドキュメントが含まれています。
```

### Block 4 (line 11)

```
プログラミングチュートリアル
```

### Block 5 (line 14)

```
**FIRST** **Tech Challenge** プログラミングチュートリアル
```

### Block 6 (line 16)

```
-  :doc:`プログラミングツールの選択 <shared/choosing_program_lang/choosing-program-lang>`
-  :doc:`Blocks チュートリアル <blocks/Blocks-Tutorial>`
-  :doc:`Onbot Java チュートリアル <onbot_java/OnBot-Java-Tutorial>`
-  :doc:`Android Studio チュートリアル <android_studio_java/Android-Studio-Tutorial>`
```

### Block 7 (line 22)

```
   :caption: チュートリアル
```

### Block 8 (line 33)

```
サポートドキュメント
```

### Block 9 (line 36)

```
制御システムサポートドキュメント
```

### Block 10 (line 38)

```
-  :doc:`制御システム入門 <shared/control_system_intro/The-FTC-Control-System>`
-  :doc:`必要な材料 <shared/required_materials/Required-Materials>`
-  :doc:`Android デバイスの使用 <shared/using_android_device/Using-Your-Android-Device>`
-  :doc:`スマートフォンのペアリング <shared/phone_pairing/phone-pairing>`
-  :doc:`Android デバイスの構成 <shared/configuring_android/Configuring-Your-Android-Devices>`
-  :doc:`デバイスを Control または Expansion Hub に接続する </hardware_and_software_configuration/connecting_devices/index>`
-  :doc:`ハードウェアの構成 </hardware_and_software_configuration/configuring/index>`
-  :doc:`ラップトップを Program & Manage Wi-Fi ネットワークに接続する <shared/program_and_manage_network/Connecting-a-Laptop-to-the-Program-&-Manage-Network>`
-  :doc:`Javascript 対応ブラウザーのインストール <shared/installing_javascript_browser/Installing-a-Javascript-Enabled-Browser>`
-  :doc:`Control Hub の管理 <shared/managing_control_hub/Managing-a-Control-Hub>`
-  :doc:`Driver Hub の管理 <shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station>`
-  :doc:`スマートフォン Robot Controller (RC) の管理 <shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller>`
```

### Block 11 (line 52)

```
   :caption: 補足
```

### Block 12 (line 67)

```
**AprilTag** プログラミング
```

### Block 13 (line 70)

```
**AprilTag** を使用したプログラミングのトピック
```

### Block 14 (line 76)

```
   AprilTag 入門 <../apriltag/vision_portal/apriltag_intro/apriltag-intro>
   VisionPortal 概要 <../apriltag/vision_portal/visionportal_overview/visionportal-overview>
   VisionPortal 用 Webcam </apriltag/vision_portal/visionportal_webcams/visionportal-webcams>
   AprilTag 値の理解 <../apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values>
   AprilTag 位置推定 <../apriltag/vision_portal/apriltag_localization/apriltag-localization>
   AprilTag テスト画像 <../apriltag/opmode_test_images/opmode-test-images>
```

### Block 15 (line 86)

```
ビジョンプログラミング
```

### Block 16 (line 89)

```
ビジョンの使用についての詳細
```

### Block 17 (line 97)

```
   カメラ較正 <vision/camera_calibration/camera-calibration>
```

### Block 18 (line 99)

```
カメラカラー処理
```

### Block 19 (line 102)

```
シンプルな Webcam またはスマートフォンカメラを使用してカラー処理を実行する方法の詳細
```

### Block 20 (line 117)

```
高度なトピック
```

### Block 21 (line 120)

```
プログラマー向けの高度なトピック
```

### Block 22 (line 135)

```
追加の **FIRST** ウェブサイトリソース
```

### Block 23 (line 138)

```
-  `FIRST ウェブサイト プログラミングリソースリンク <https://www.firstinspires.org/resources/library/ffc/programming-resources>`__
```


## programming_resources/laptops/laptops.rst

### Block 1 (line 1)

```
**FIRST** プログラムのコンピューター要件
```

### Block 2 (line 4)

```
**FIRST**\ :sup:`®` LEGO\ :sup:`®` League、**FIRST**\ :sup:`®` Tech Challenge、**FIRST**\ :sup:`®` Robotics Competition などの **FIRST**\ :sup:`®` プログラムは、参加するチームと同じくらいユニークです。このユニークさは、プログラムに技術を提供するさまざまなベンダー、各プログラムの独自の目標を管理するために必要なハードウェアとソフトウェア、そしてチームが参加し優れた成果を上げるために役立つツールと技術の絶えず進化する状況に一部起因しています。プログラム間の共通点の1つは、チームがソフトウェア開発、設計、およびコラボレーションのためのコンピュータープラットフォームを必要とすることです。このドキュメントは、そのコンピューターシステムのハードウェアとオペレーティングシステムの要件に関する推奨事項として機能します。
```

### Block 3 (line 6)

```
コンピューターの最小要件に影響を与える可能性のある多くの要因のうち、これらが最も大きく影響します：
```

### Block 4 (line 8)

```
-  プログラム内でコンピューターが実行する可能性のある役割固有のタスク
```

### Block 5 (line 10)

```
-  コンピューターで使用される可能性のあるコンピューター支援設計（CAD）ソフトウェアのタイプ
```

### Block 6 (line 12)

```
-  ソフトウェア開発とハードウェア更新の要件
```

### Block 7 (line 14)

```
-  ベンダー固有のアプリケーション要件と制限
```

### Block 8 (line 16)

```
プログラム固有の要件
```

### Block 9 (line 19)

```
各プログラムには独自の要件セットがありますが、それらの各要件は最小限のコンピューター構成で満たすことができます。このセクションでは、各プログラムの役割の最小要件を特定しようとしています。各要件を満たす具体的な推奨ハードウェアは、「推奨ハードウェアセット」セクションに記載されています。
```

### Block 10 (line 21)

```
**FIRST**\ :sup:`®` LEGO\ :sup:`®` League の推奨コンピューターハードウェア
```

### Block 11 (line 24)

```
**FIRST** LEGO League には、プログラム可能なプラットフォームを使用する2つのディビジョンがあります：`LEGO\ ® Education SPIKE\ ™ Prime <https://education.lego.com/en-us/product-resources/spike-prime/downloads/system-requirements/>`__ プラットフォームを使用する **FIRST** LEGO League Challenge と、`LEGO\ ® Education SPIKE\ ™ Essential <https://education.lego.com/en-us/products/lego-education-spike-essential-set/45345/>`__ プラットフォームを使用する **FIRST** LEGO League Explore です。両方のプラットフォームは、ほぼ同じコンピューター要件を持っており、違いは以下に記載されています。これらのプラットフォームは、ほとんどのコンピューター構成でサポートされているため、最もアクセスしやすいものの1つです。
```

### Block 12 (line 26)

```
*ソフトウェア開発に推奨：*
```

### Block 13 (line 30)

```
サポート対象：
```

### Block 14 (line 38)

```
   -  LEGO\ :sup:`®` Education SPIKE™ Essential hub は iPad では更新できません
```

### Block 15 (line 42)

```
   -  LEGO\ :sup:`®` Education SPIKE™ Essential はサポートされていません
```

### Block 16 (line 44)

```
また、Google Play ストア（Chromebook Android アプリ用）へのアクセス、アプリ内コンテンツのダウンロード、教師サポート資料へのアクセス、ライブ気象データなどの特定の機能を使用するために、アクティブなインターネット接続を持つことも推奨されます。
```

### Block 17 (line 46)

```
**FIRST**\ :sup:`®` Tech Challenge の推奨コンピューターハードウェア
```

### Block 18 (line 49)

```
**FIRST** Tech Challenge で使用される主要なハードウェアプラットフォームは、`REV Control Hub <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics>`__ と `REV Driver Hub <https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications>`__ です。これらのプラットフォームには独自のオペレーティングシステムとアプリケーション要件がありますが、ほとんどのハードウェアプラットフォームで基本的な機能のほとんどを実行できます（ただし、より多くの手動手順が必要です）。**FIRST** Tech Challenge のチームは、ソフトウェア開発と CAD という2つの基本的な目的でコンピューターを使用しており、この2つの使用法におけるチームの好みが必要なハードウェアを形成します。
```

### Block 19 (line 51)

```
*ソフトウェア開発と CAD に推奨：*
```

### Block 20 (line 57)

```
*ソフトウェア開発のみに推奨：*
```

### Block 21 (line 61)

```
   -  クラウド CAD ソリューションのみ推奨
```

### Block 22 (line 63)

```
      -  OnShape、SolidWorks 3D Experience など
```

### Block 23 (line 66)

```
サポート対象：
```

### Block 24 (line 70)

```
   -  `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ はサポートされていません
```

### Block 25 (line 72)

```
      -  ブラウザベースのインターフェースを使用して手動で更新する必要があります
```

### Block 26 (line 76)

```
   -  `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ はサポートされていません
```

### Block 27 (line 78)

```
      -  ブラウザベースのインターフェースを使用して手動で更新する必要があります
```

### Block 28 (line 80)

```
   -  `Android Studio <https://developer.android.com/studio>`__ はサポートされていません
```

### Block 29 (line 82)

```
      -  **Blocks** と **OnBot Java** のみサポート
```

### Block 30 (line 84)

```
また、ソフトウェア開発中はアクティブなインターネット接続を持つことが推奨されます。https://github.com へのアクセスは、**REV Hardware Client** が必要なシーズンソフトウェア更新をダウンロードしてインストールするために必要であり、**Android Studio** ユーザーがソフトウェアテンプレートをダウンロードするためにも必要です。
```

### Block 31 (line 86)

```
**FIRST**\ :sup:`®` Robotics Competition の推奨コンピューターハードウェア
```

### Block 32 (line 89)

```
**FIRST** Robotics Competition で使用される主要なハードウェアプラットフォームは、`NI roboRIO <https://www.ni.com/docs/en-US/bundle/roborio-20-specs/page/specs.html>`__ です。このプラットフォームには、プログラミング環境に応じて、ソフトウェア開発の要件とは異なる可能性のある競技におけるコンピューターハードウェアに対する独自の要件セットがあります。**FIRST** Tech Challenge と同様に、**FIRST** Robotics Competition のチームは、ソフトウェア開発と CAD という2つの基本的な目的でソフトウェア開発コンピューターを使用しており、この2つの使用法におけるチームの好みが必要なハードウェアを形成します。ただし、**FIRST** Robotics Competition では、コンピューターが果たすことができる2つの役割（ソフトウェアと設計開発プラットフォームおよび／または Driver Station プラットフォーム）があり、これらの役割もコンピューターハードウェアの要件を形成します。
```

### Block 33 (line 91)

```
必要に応じて1台のラップトップを両方の目的に使用できますが、**Driver Station** プラットフォーム用とソフトウェアおよび設計開発用の2台の別々のコンピューターを持つことが推奨されます。
```

### Block 34 (line 96)

```
Driver Station コンピューターは、ロボットへの主要なインターフェースとして使用され、イベントで Field Management System（FMS）とのインターフェースに使用され、ロボット上のハードウェアおよびソフトウェアプラットフォームと通信するために使用されるソフトウェアツールによって制限されます。チームは、イベントでのシステムの義務と物理的要求を分離できるように、Driver Station の役割とソフトウェアおよび設計開発の役割に別々のコンピューターを持つことが有利であると感じています。予算を意識しているチームは、そのコンピューターが少なくとも Driver Station の役割の最小要件を満たしている場合、両方の役割に単一のコンピューターを確実に使用できます。Driver Station の役割には Windows オペレーティングシステムが必要であることに注意してください。これは、役割の義務を実行するために必要なアプリケーションが Windows 専用アプリケーションであるためです。
```

### Block 35 (line 98)

```
*Driver Station の役割に推奨：*
```

### Block 36 (line 103)

```
サポート対象：
```

### Block 37 (line 107)

```
ソフトウェア開発と設計
```

### Block 38 (line 110)

```
**FIRST** Tech Challenge と同様に、**FIRST** Robotics Competition チームは、ソフトウェア開発と設計ラップトップをソフトウェア開発と CAD に使用します。CAD の使用に応じて、ハードウェア要件は若干異なります：
```

### Block 39 (line 112)

```
*CAD を使用したソフトウェアおよび設計開発の役割に推奨：*
```

### Block 40 (line 117)

```
*ソフトウェア開発のみに推奨：*
```

### Block 41 (line 121)

```
   -  クラウド CAD ソリューションのみ推奨
```

### Block 42 (line 123)

```
      -  OnShape、SolidWorks 3D Experience など
```

### Block 43 (line 126)

```
サポート対象：
```

### Block 44 (line 130)

```
   -  `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ はサポートされていません
```

### Block 45 (line 132)

```
   -  `LabVIEW <https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/labview-setup.html>`__ ソフトウェアはサポートされていません
```

### Block 46 (line 134)

```
また、ソフトウェア開発中はアクティブなインターネット接続を持つことが推奨されます。https://github.com へのアクセスは、**REV Hardware Client** が必要なシーズンソフトウェアとファームウェア更新をダウンロードしてインストールするために必要です。追加のソフトウェアにも同様の要件がある場合があります。
```

### Block 47 (line 136)

```
推奨ハードウェアセット
```

### Block 48 (line 139)

```
これらは、プログラム固有の要件によって参照される推奨ハードウェアセットです。すべてのハードウェアプラットフォームには、次のようないくつかの追加要件と推奨事項があります：
```

### Block 49 (line 141)

```
*Windows オペレーティングシステム*
```

### Block 50 (line 143)

```
-  Windows 10 のサポートは2025年半ばに終了するため、Windows 11 をサポートする Windows システムを購入することを強くお勧めします。すべてのソフトウェアが Windows 11 でサポートされていると明示的にラベル付けされているわけではありませんが、必要なソフトウェアのほぼすべてが Windows 11 で動作するようにテストされています。
```

### Block 51 (line 146)

```
*USB ポート*
```

### Block 52 (line 148)

```
-  ラップトップには少なくとも2つの利用可能な物理 USB-A ポートが必要です。
```

### Block 53 (line 150)

```
-  **FIRST** Tech Challenge の場合、ラップトップの USB-C ポートは **REV Control Hub** または **REV Driver Hub** で適切に動作できないため、USB-A ポートも利用できることが重要です。
```

### Block 54 (line 155)

```
-  **FIRST** LEGO League の場合、ラップトップとタブレットが Bluetooth 4.0 以上をサポートすることが重要です。
```

### Block 55 (line 158)

```
*物理イーサネットポート*
```

### Block 56 (line 160)

```
-  ハードウェアとソフトウェアのほとんどの機能は Wi-Fi で簡単にサポートできますが、一部の状況（**FIRST** Robotics Competition の Driver Station など）では、システムに物理 RJ-45 イーサネットポートがあることが大きな利点です。
```

### Block 57 (line 163)

```
*SSD ハードドライブ*
```

### Block 58 (line 165)

```
-  特に必須ではありませんが、SSD 技術を使用するハードドライブ（回転ディスク技術と比較して）は、より速く起動し、電源を入れたまま持ち運んでいるときや、**FIRST** Robotics Competition Driver Station コンピューターで一般的な「予期しない衝撃」を経験したときに損傷する可能性が低くなります。
```

### Block 59 (line 170)

```
高性能プロセッサを含む高グラフィックス性能向けに設計されたラップトップ。`Dell G16 <https://www.dell.com/en-us/shop/dell-laptops/g16-gaming-laptop/spd/g-series-16-7630-laptop>`__ や `HP Omen <https://www.hp.com/us-en/shop/pdp/omen-gaming-laptop-16-xf0087nr>`__ など。以下の推奨仕様：
```

### Block 60 (line 172)

```
-  プロセッサー：Intel Core i7、AMD Ryzen 7、またはそれ以上
```

### Block 61 (line 174)

```
-  グラフィックス：NVIDIA GeForce RTX 4050 またはそれ以上
```

### Block 62 (line 176)

```
-  メモリー：16GB RAM 以上、32GB 推奨
```

### Block 63 (line 178)

```
-  ストレージ：512 GB SSD 以上、1TB SSD 推奨
```

### Block 64 (line 180)

```
-  イーサネット：RJ-45 イーサネットポート推奨
```

### Block 65 (line 182)

```
-  ポート：USB type A ポート2つ以上推奨
```

### Block 66 (line 184)

```
-  Bluetooth：Bluetooth 4.0 またはそれ以上
```

### Block 67 (line 186)

```
-  Wi-Fi：統合 Wi-Fi、Wi-Fi 6E 以上推奨
```

### Block 68 (line 188)

```
-  オペレーティングシステム：Windows 10 以上、Windows 11 推奨
```

### Block 69 (line 193)

```
スムーズなパフォーマンスと日常的なタスク向けに設計された標準的な Windows ラップトップ。`Dell Inspiron 15 <https://www.dell.com/en-us/shop/dell-laptops/inspiron-15-laptop/spd/inspiron-15-3530-laptop>`__ や `HP Pavilion Laptop <https://www.hp.com/us-en/shop/mdp/laptops/pavilion-15-344522--1>`__ など。
```

### Block 70 (line 195)

```
-  プロセッサー：Intel Core i5、AMD Ryzen 5、またはそれ以上
```

### Block 71 (line 197)

```
-  グラフィックス：Intel または AMD 組み込みグラフィックスアダプターまたはそれ以上
```

### Block 72 (line 199)

```
-  メモリー：8GB RAM 以上、16GB 推奨
```

### Block 73 (line 201)

```
-  ストレージ：256GB 以上、512 GB SSD 推奨
```

### Block 74 (line 203)

```
-  イーサネット：RJ-45 イーサネットポート推奨
```

### Block 75 (line 205)

```
-  ポート：USB type A ポート2つ以上推奨
```

### Block 76 (line 207)

```
-  Bluetooth：Bluetooth 4.0 またはそれ以上
```

### Block 77 (line 209)

```
-  Wi-Fi：統合 Wi-Fi、Wi-Fi 6E 以上推奨
```

### Block 78 (line 211)

```
-  オペレーティングシステム：Windows 10 以上、Windows 11 推奨
```

### Block 79 (line 216)

```
スムーズなパフォーマンスと日常的なタスク向けに設計された標準的な MacOS ラップトップ。`MacBook Air <https://www.apple.com/shop/buy-mac/macbook-air>`__ や `MacBook Pro <https://www.apple.com/shop/buy-mac/macbook-pro>`__ など。
```

### Block 80 (line 218)

```
-  プロセッサー：Apple M1 またはそれ以上、Apple M2 推奨
```

### Block 81 (line 220)

```
-  メモリー：4GB RAM 以上
```

### Block 82 (line 222)

```
-  ストレージ：2GB 以上の利用可能なストレージスペース
```

### Block 83 (line 224)

```
-  Bluetooth：Bluetooth 4.0 またはそれ以上
```

### Block 84 (line 226)

```
-  オペレーティングシステム：MacOS Mojave 10.14 以降
```

### Block 85 (line 231)

```
iPad Air 2 または iPad Mini 4 以降などの標準的な iOS タブレット。
```

### Block 86 (line 233)

```
-  オペレーティングシステム：iOS 13 以降
```

### Block 87 (line 238)

```
`Samsung Galaxy Chromebook 2 <https://www.google.com/chromebook/discover/pdp-samsung-galaxy-chromebook-2/sku-samsung-galaxy-chromebook-2-8gb-128gb/>`__ などの標準的な Chromebook、または類似のもの。
```

### Block 88 (line 240)

```
-  プロセッサー：1.40 GHz Intel Celeron 2955U デュアルコアプロセッサーまたはそれ以上
```

### Block 89 (line 242)

```
-  メモリー：4GB RAM 以上
```

### Block 90 (line 244)

```
-  ストレージ：3GB 以上の利用可能なストレージスペース
```

### Block 91 (line 246)

```
-  Bluetooth：Bluetooth 4.0 以上
```

### Block 92 (line 248)

```
-  オペレーティングシステム：Android 7.0 以降
```

### Block 93 (line 253)

```
`Samsung Galaxy Tab A7 Lite <https://www.samsung.com/us/tablets/galaxy-tab-a/galaxy-tab-a7-10-4-inch-gray-64gb-wi-fi-sm-t500nzaexar/>`__ などの標準的な Android タブレット、または類似のもの。
```

### Block 94 (line 255)

```
-  8 インチ以上のディスプレイ
```

### Block 95 (line 257)

```
-  メモリー：3GB RAM 以上
```

### Block 96 (line 259)

```
-  ストレージ：3GB 以上の利用可能なストレージスペース
```

### Block 97 (line 261)

```
-  Bluetooth：Bluetooth 4.0 以上
```

### Block 98 (line 263)

```
-  オペレーティングシステム：Android 7.0 以降
```


## programming_resources/onbot_java/OnBot-Java-Tutorial.rst

### Block 1 (line 1)

```
OnBot Java プログラミングチュートリアル
```

### Block 2 (line 6)

```
   <h3>はじめに</h3>
```

### Block 3 (line 9)

```
このチュートリアルでは、制御システムの構成、プログラミング、操作のプロセスを段階的に説明します。このチュートリアルでは、**OnBot Java** プログラミングツールを使用して、ロボットのプログラミングを始めるのに役立ちます。
```

### Block 4 (line 11)

```
**OnBot Java** プログラミングツールは、プログラマーがWebブラウザを使用してJavaの**Op Mode** を作成、編集、保存できるテキストベースのプログラミングツールです。このツールは、基本から高度なJavaスキルを持ち、テキストベースの**Op Mode** を作成したいプログラマーにお勧めです。
```

### Block 5 (line 19)

```
   :bdg-info:`OBJ` は、**OnBot Java** プログラミングに固有のコンテンツであることを示します。
```


## programming_resources/onbot_java/config/config.rst

### Block 1 (line 1)

```
ハードウェアの構成 :bdg-info:`OBJ`
```


## programming_resources/onbot_java/connecting/connecting.rst

### Block 1 (line 1)

```
Program & Manage サーバーへの接続 :bdg-info:`OBJ`
```


## programming_resources/onbot_java/intro/intro.rst

### Block 1 (line 1)

```
はじめに :bdg-info:`OBJ`
```


## programming_resources/onbot_java/opmode/opmode.rst

### Block 1 (line 1)

```
**Op Mode** の作成 :bdg-info:`OBJ`
```


## programming_resources/onbot_java/reference/reference.rst

### Block 1 (line 1)

```
リファレンスドキュメント :bdg-info:`OBJ`
```


## programming_resources/shared/auto_load_opmode/auto-load-opmode.rst

### Block 1 (line 1)

```
ドライバー制御 **Op Mode** の自動ロード
```

### Block 2 (line 4)

```
**FIRST** **Tech Challenge** の試合は、30秒の自律期間と、その後の2分間のドライバー制御（すなわち、テレオペレートまたは teleop）期間で構成されます。以前は、チームは自律部分の試合が終了した後、手動で teleop**op mode** を選択する必要がありました。
```

### Block 3 (line 6)

```
チームは現在、teleop **op mode** を事前選択でき、自律実行が完了するとすぐに**Driver Station** がこの**op mode** を自動的にロードするようにできます。この機能は、チームが試合中に間違った**op mode** を選択するのを避けるのに役立ちます。
```

### Block 4 (line 8)

```
この機能を使用するには、**SDK** ソフトウェア（**Robot Controller** と**Driver Station** ）のバージョン 6.1 以降を使用していることを確認してください。
```

### Block 5 (line 10)

```
試合中に使用する自律プログラムを選択します。事前選択ボタンが画面の左下隅に表示されます。半透明で、隣接するテキストがなく、機能が非アクティブであることを示しています。
```

### Block 6 (line 16)

```
   横向きモードで自律 **OpMode** が選択されると、事前選択ボタンが表示されます。
```

### Block 7 (line 21)

```
   縦向きモードで自律 **OpMode** が選択されると、事前選択ボタンが表示されます。
```

### Block 8 (line 24)

```
事前選択ボタンを表示するには、選択された **op mode** が、Java を使用して記述されている場合は \_@Autonomous\_ アノテーションを使用するか、**Blocks** エディターで *Autonomous* オプションを選択することによって、自律 **op mode** として指定されている必要があることに注意してください。事前選択ボタンが表示されない場合は、現在選択されている**op mode** が自律として指定されていることを確認してください。
```

### Block 9 (line 29)

```
   事前選択ボタンを表示するには、選択された **op mode** が Autonomous として指定されている必要があります。
```

### Block 10 (line 31)

```
アクティブ化するには、（半透明の）ボタンをタップして、**op mode** を選択するだけです。その後、ボタンは完全に不透明になり、事前選択された**op mode** の名前がボタンの隣に表示されます。これは、機能がアクティブであることを示しています。
```

### Block 11 (line 36)

```
   横向きモードで自動ロードされるドライバー制御 **OpMode** 。
```

### Block 12 (line 41)

```
   縦向きモードで自動ロードされるドライバー制御 **OpMode** 。
```

### Block 13 (line 43)

```
その後、無効にしたい場合は、事前選択ボタンを長押しするだけです。ボタンは再び半透明になり、隣接するテキストが消えます。
```

### Block 14 (line 45)

```
自律プログラムが終了すると、**Driver Station** は、キューに入れられた**OpMode** を、自律開始前に事前選択された TeleOp プログラムに変更します。ユーザーが停止を押す（メイン停止または init 停止ボタンのいずれか）と、自動事前選択は中止されます。**OpMode** が自己終了するか、30秒タイマーによって終了された場合にのみ、遷移します。安全上の理由から、ドライブチームは依然として手動で Init を押して**op mode** を開始する必要があります。
```

### Block 15 (line 47)

```
自律プログラムを実行するたびに、手動で事前選択機能を有効にして構成する必要がない場合は、**OpMode** アノテーションを編集して ``preselectTeleOp="My TeleOp Name"`` を含めることができます。その後、**Driver Station** は自動的に事前選択機能をアクティブ化し、アノテーションで指定された**OpMode** を事前選択するように構成します。
```

### Block 16 (line 50)

```
   :caption: preselectTeleOp パラメーターを使用して、事前選択された op mode を指定します。
```

### Block 17 (line 55)

```
**Blocks** ユーザーも、**Blocks** プログラムエディターの新しいドロップダウンを通じて、この機能を使用できます。
```

### Block 18 (line 60)

```
   **Blocks** エディターを使用して、teleop**op mode** を事前選択できます。
```

### Block 19 (line 62)

```
**Driver Station** アプリの Settings メニューに「OpMode Auto Queue」というオプションがあることに注意してください。このオプションが有効になっている場合、**Driver Station** は、``preselectTeleOp`` パラメーターで指定されたとおり、自律**op mode** の事前選択された teleop**op mode** を自動的にロードします。このオプションが無効になっている場合、**Driver Station** は事前選択された teleop**op mode** を自動的にロードしません。「Op Mode Auto Queue」オプションが無効になっている場合でも、チームはメインの**Driver Station** アクティビティの事前選択ボタンを使用して、teleop**op mode** を選択できます。
```

### Block 20 (line 67)

```
   OpMode Auto Queue オプションが有効になっている場合、**Driver Station** は横向きモードで preselectTeleOp**op mode** を自動的にロードします。
```

### Block 21 (line 72)

```
   OpMode Auto Queue オプションが有効になっている場合、**Driver Station** は縦向きモードで preselectTeleOp**op mode** を自動的にロードします。
```


## programming_resources/shared/choosing_program_lang/choosing-program-lang.rst

### Block 1 (line 1)

```
プログラミングツールの選択
```

### Block 2 (line 4)

```
競技ロボット用の **Op Mode** を作成できるようにするには、プログラミングツールを選択する必要があります。
**Op Mode** または Operational Mode は、ロボットに何をすべきかを指示するプログラムです。使用できる 3 つのプログラミングツールがあります。
```

### Block 3 (line 7)

```
**FIRST** は、** すべてのユーザー** が最初に :ref:`Blocks プログラミングツール <programming_resources/blocks/blocks-tutorial:blocks programming tutorial>` の使用方法を学ぶことを強く推奨しています。
```

### Block 4 (line 9)

```
**Blocks** プログラミングツール
```

### Block 5 (line 12)

```
プログラマーがウェブブラウザを使用して **Op Mode** を作成、編集、保存できるビジュアルプログラミングツールです。このツールは、初心者プログラマーや、ドラッグアンドドロップインターフェースを使用して**Op Mode** を視覚的に設計することを好むユーザーに推奨されます。
```

### Block 6 (line 17)

```
**OnBot Java** プログラミングツール
```

### Block 7 (line 19)

```
プログラマーがウェブブラウザを使用して **Op Mode** を作成、編集、保存できるテキストベースのプログラミングツールです。
このツールは、基本から高度な Java スキルを持ち、テキストベースの **Op Mode** を作成したいプログラマーに推奨されます。
```

### Block 8 (line 27)

```
**Android** アプリを作成するための高度な統合開発環境です。このツールは、プロの**Android** アプリ開発者が使用するのと同じツールです。**Android Studio** は、豊富な Java プログラミング経験を持つ上級ユーザーにのみ推奨されます。
```

### Block 9 (line 32)

```
推奨事項
```

### Block 10 (line 35)

```
各ツールには独自の長所と短所があります。多くのユーザー（特に新規チームや初心者プログラマー）にとって、**Blocks プログラミングツールが全体的に使用する最適なツールです**。**Blocks** プログラミングツールは直感的で習得が簡単です。** これは、ロボットのプログラミングを始める最も速い方法です。**
```

### Block 11 (line 37)

```
**OnBot Java** プログラミングツールは**Blocks** プログラミングツールに似ています。ただし、**OnBot Java** はテキストベースのツールであり、ユーザーが Java プログラミング言語をしっかり理解している必要があります。
```

### Block 12 (line 42)

```
**Blocks** プログラミングツールと**OnBot Java** プログラミングツールでは、ユーザーはロボットの**Op Mode** を作成、編集、ビルドするためにウェブブラウザだけが必要であることに注意することが重要です。ユーザーは、iPad、**Android** 端末、または Chromebook を使用して**Op Mode** を作成、編集、ビルドすることもできます。
```

### Block 13 (line 44)

```
**Android Studio** は強力な開発ツールです。ただし、豊富な Java プログラミング知識が必要です。また、**Android Studio** ソフトウェアを実行するための専用ラップトップも必要です。**Android Studio** は、**OnBot Java** プログラミングツールでは利用できない拡張編集およびデバッグ機能を提供します。ただし、より複雑なツールであり、使用方法を学ぶために時間を費やす必要があります。上級ユーザーにのみ推奨されます。
```


## programming_resources/shared/configuring_android/Configuring-Your-Android-Devices.rst

### Block 1 (line 1)

```
Androidデバイスの構成
```

### Block 2 (line 4)

```
制御システムに必要な構成は何ですか？
```

### Block 3 (line 7)

```
Driver Hubの構成
```

### Block 4 (line 10)

```
**REV Robotics Driver Hub** を**DRIVER STATION** として使用しているチームは、**REV Robotics Driver Hub** のセットアップと使用方法については、`REV Roboticsの公式ドキュメント <https://docs.revrobotics.com/duo-control/driver-hub-gs>`__ を参照してください。
```

### Block 5 (line 12)

```
Control Hubの構成
```

### Block 6 (line 16)

```
   **DRIVER STATION** スマートフォンへの参照は、**Driver Station** （**DS** ）アプリがプリインストールされている `REV Robotics Driver Hub <https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications>`__ にも適用される場合があります。
```

### Block 7 (line 18)

```
**Control Hub** （統合されたAndroidデバイスを備えている）を使用しているチームは、**DRIVER STATION** として使用する単一のスマートフォンを構成するだけで済みます。プロセスは次のとおりです：
```

### Block 8 (line 20)

```
*  スマートフォンの名前を「<TEAM NUMBER>-DS」に変更します（<TEAM NUMBER>はチーム番号に置き換えます）。
*  **Driver Station** （**DS** ）アプリを**DRIVER STATION** デバイスにインストールします。（**DS** アプリは**REV Robotics Driver Hub** にプリインストールされています。）
*  スマートフォンを機内モードにします（WiFi無線はオンのまま）。
*  **DRIVER STATION** を**Control Hub** にペアリングします（つまり、ワイヤレスで接続します）。
```

### Block 9 (line 32)

```
2台のAndroidスマートフォンの構成
```

### Block 10 (line 35)

```
2台のスマートフォンを持っており、**Control Hub** を使用していないチームは、1台のスマートフォンを**Robot Controller** として、もう1台のスマートフォンを**DRIVER STATION** として構成する必要があります。プロセスは次のとおりです：
```

### Block 11 (line 37)

```
*  1台のスマートフォンの名前を「<TEAM NUMBER>-RC」に変更します（<TEAM NUMBER>はチーム番号に置き換えます）。
*  **Robot Controller** アプリを**Robot Controller** スマートフォンにインストールします。
*  2台目のスマートフォンの名前を「<TEAM NUMBER>-DS」に変更します（<TEAM NUMBER>はチーム番号に置き換えます）。
*  **Driver Station** アプリを**DRIVER STATION** デバイスにインストールします。（**DS** アプリは**REV Robotics Driver Hub** にプリインストールされています。）
*  スマートフォンを機内モードにします（WiFi無線はオンのまま）。
*  **DRIVER STATION** を**Robot Controller** にペアリングします（つまり、ワイヤレスで接続します）。
```

### Block 12 (line 51)

```
スマートフォンの名前変更
```

### Block 13 (line 54)

```
**FIRST**Tech Challengeの公式ルール（R707を参照）では、スマートフォンのWi-Fi名を、チーム番号と、スマートフォンが**Robot Controller** の場合は「-RC」、**DRIVER STATION** の場合は「-DS」を含むように変更する必要があります。チームが複数のAndroidスマートフォンのセットを持っている場合は、追加のダッシュと文字（「A」、「B」、「C」など）を挿入できます。
```

### Block 14 (line 56)

```
たとえば、チームのチーム番号が9999で、チームが複数のスマートフォンのセットを持っている場合、チームは1台のスマートフォンを **Robot Controller** 用に「9999-C-RC」、もう1台のスマートフォンを**DRIVER STATION** 用に「9999-C-DS」と名付けることを決定する場合があります。「-C」は、これらのデバイスがこのチームの3番目のスマートフォンセットに属していることを示します。
```

### Block 15 (line 58)

```
**Robot Controller** スマートフォンの名前は、:ref:`ここにある <programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller:changing the name>` 手順を使用して、**RC** アプリで変更できます。また、**RC** アプリ、ペアリングされた**DS** アプリ、または接続されたラップトップから *Manage* ページで変更することもできます。完了したら ``Apply Wi-Fi Settings`` をクリックしてください。
```

### Block 16 (line 60)

```
**DRIVER STATION** デバイスの名前は、:ref:`ここにある <programming_resources/shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station:changing the name>` 手順を使用して、**DS** アプリで変更できます。
```

### Block 17 (line 62)

```
または、以下に説明するように、Androidシステムレベルでデバイス名を変更することもできます。
```

### Block 18 (line 81)

```
   * - 手順
     - 画像
```

### Block 19 (line 84)

```
   * - 1. スマートフォンで利用可能なアプリのリストを参照し、**Settings** アイコンを見つけます。**Settings** アイコンをクリックして、Settings画面を表示します。
```

### Block 20 (line 87)

```
   * - 2. **Wi-Fi** をクリックして、Wi-Fi画面を起動します。
```

### Block 21 (line 90)

```
   * - 3. 縦に並んだ3つのドットをタッチして、ポップアップメニューを表示します。
```

### Block 22 (line 93)

```
   * - 4. ポップアップメニューから **Advanced** を選択します。
```

### Block 23 (line 96)

```
   * - 5. **Advanced Wi-Fi** 画面から**Wi-Fi Direct** を選択します。
```

### Block 24 (line 99)

```
   * - 6. 縦に並んだ3つのドットをタッチして、ポップアップメニューを表示します。
```

### Block 25 (line 102)

```
   * - 7. ポップアップメニューから **Configure Device** を選択します。
```

### Block 26 (line 105)

```
   * - 8. タッチパッドを使用して、デバイスの新しい名前を入力します。デバイスが **Robot Controller** になる場合は、チーム番号と「-RC」を指定します。デバイスが**DRIVER STATION** になる場合は、チーム番号と「-DS」を指定します。また、Wi-Fi Directの非アクティブタイムアウトを *Never disconnect* に設定してから、**SAVE** ボタンを押して変更を保存することもできます。右に示すスクリーンショットでは、チーム番号は9999です。「-C」は、これがこのチームの3番目のスマートフォンペアからのものであることを示します。「-RC」は、このスマートフォンが**Robot Controller** になることを示します。
```

### Block 27 (line 108)

```
   * - 9. スマートフォンの名前を変更した後、デバイスの電源を入れ直します。
```

### Block 28 (line 114)

```
FIRST Tech Challengeアプリのインストール
```

### Block 29 (line 117)

```
アプリのインストールと更新に関する詳細な手順については、以下の他のページを参照してください：
```

### Block 30 (line 119)

```
:ref:`ROBOT CONTROLLERアプリ <ftc_sdk/updating/rc_app/updating-the-rc-app:updating the robot controller (rc) app>`
```

### Block 31 (line 121)

```
:ref:`DRIVER STATIONアプリ <ftc_sdk/updating/ds_app/updating-the-ds-app:updating the driver station app>`
```

### Block 32 (line 124)

```
**2021年現在、SDKアプリ（v 6.1以降）はGoogle Playで入手できなくなりました。**
```

### Block 33 (line 126)

```
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアを使用すると、デバイス（**REV Robotics Control Hub**、**REV Robotics Expansion Hub**、**REV Robotics Driver Hub** 、およびその他の承認されたAndroidデバイス）にアプリをダウンロードできます（*以下の「Androidスマートフォンでのアプリの更新」というセクションを参照*）。以下は、いくつかの利点です：
```

### Block 34 (line 128)

```
*  WiFi経由で **REV Robotics Control Hub** に接続します。
*  接続されたデバイス上のすべてのソフトウェアをワンクリックで更新します。
*  接続されたデバイスなしでソフトウェアアップデートを事前ダウンロードします。
*  **Control Hub** からユーザーデータをバックアップおよび復元します。
*  Androidデバイスに **DS** と**RC** アプリケーションをインストールして切り替えます。
*  **Control Hub** の**Robot Control** コンソールにアクセスします。
```

### Block 35 (line 135)

```
アプリリリースは、`FtcRobotController GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ でも入手できます。**Robot Controller** （**RC** ）および**Driver Station** （**DS** ）スマートフォンにアプリを「サイドロード」することは可能です。ただし、このドキュメントのこのセクションには、そのような手順は含まれて** いません** 。他のドキュメントページでは、:ref:`RCアプリ <programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller:Updating the Robot Controller App>` と :ref:`DSアプリ <programming_resources/shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station:Updating the Driver Station App>` のサイドローディングについて説明しています。
```

### Block 36 (line 137)

```
REV Roboticsデバイス（REV Robotics Expansion Hub、REV Robotics Control Hub、REV Robotics Driver Hub）でのアプリとファームウェアの更新
```

### Block 37 (line 140)

```
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、REV Roboticsのデバイスにアプリ、ファームウェア、および/またはオペレーティングシステムをインストールおよび更新するために使用されます。REV Hardware Clientをインストールして実行しているPCにUSB経由でデバイスを接続するだけで、ソフトウェアが接続されたハードウェアを検出します。検出後、REV Hardware Clientは、`REV Robotics Control HubでRobot Controller（RC）アプリを更新 <https://docs.revrobotics.com/rev-hardware-client/control-hub/updating-control-hub>`__ したり、`REV Robotics Driver HubでDriver Station（DS）アプリを更新 <https://docs.revrobotics.com/rev-hardware-client/driver-hub/updating-a-driver-hub>`__ したり、`ファームウェアを更新 <https://docs.revrobotics.com/rev-hardware-client/expansion-hub/updating-expansion-hub>`__ したりできます。
```

### Block 38 (line 142)

```
Androidスマートフォンでのアプリの更新
```

### Block 39 (line 145)

```
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、`Androidスマートフォンでのアプリのインストール、アンインストール、更新 <https://docs.revrobotics.com/rev-hardware-client/android-device/installing-rc-ds-applications>`__ に使用されます。ただし、REV Hardware Clientソフトウェアによってスマートフォンが適切に認識および更新されるためには、スマートフォンで **Developer Options** （開発者オプション）を有効にする必要があります。Developer Optionsを有効にするプロセスは次のとおりです：
```

### Block 40 (line 158)

```
   * - 手順
     - 画像
```

### Block 41 (line 161)

```
   * - 1. 「Settings」に移動し、「About device」または「About phone」をタップします。
```

### Block 42 (line 164)

```
   * - 2. 下にスクロールして、「Build number」を7回タップします。デバイスとオペレーティングシステムによっては、「Software information」をタップしてから、「Build number」を7回タップする必要がある場合があります。
```

### Block 43 (line 167)

```
   * - 3. パターン、PIN、またはパスワードを入力して、Developer optionsメニューを有効にします。
```

### Block 44 (line 170)

```
   * - 4. 「Developer options」メニューがSettingsメニューに表示されるようになります。デバイスによっては、Settings > General > Developer optionsの下に表示される場合があります。
```

### Block 45 (line 173)

```
   * - 5. Developer optionsをいつでも無効にするには、スイッチをタップします。
```

### Block 46 (line 177)

```
スマートフォンをWi-Fiオンの機内モードにする
```

### Block 47 (line 180)

```
**FIRST**Tech Challenge競技会では、**Robot Controller** と**DRIVER STATION** デバイスを機内モードにする一方で、Wi-Fi無線はオンのままにしておくことが重要です。これは、マッチ中に携帯電話機能を有効にしたくないためです。携帯電話機能は、マッチ中のロボットの機能を妨げる可能性があります。
```

### Block 48 (line 192)

```
   * - 手順
     - 画像
```

### Block 49 (line 195)

```
   * - 1. 各スマートフォンのメインAndroid画面で、指を使って画面の上部から下部に向かってスライドして、クイック構成画面を表示します。一部のスマートフォンでは、特に画面の上部にメッセージや通知が表示されている場合、クイック構成画面を表示するために複数回下にスワイプする必要がある場合があることに注意してください。機内モードアイコン（飛行機の形をしています）を探し、アイコンがアクティブになっていない場合は、アイコンをタッチしてスマートフォンを機内モードにします。
```

### Block 50 (line 198)

```
   * - 2. スマートフォンを機内モードにすると、Wi-Fi無線がオフになります。Wi-Fiアイコンに斜線が入っている場合（上記の手順1を参照）、Wi-Fi無線は無効になっています。クイック構成画面の **Wi-Fi** アイコンをタッチして、Wi-Fi無線を再びオンにする必要があります。
```

### Block 51 (line 202)

```
DRIVER STATIONをRobot Controllerにペアリングする
```

### Block 52 (line 207)

```
Control Hubのペアリング
```

### Block 53 (line 210)

```
**REV Robotics Control Hub** には、**Robot Controller** アプリがプリインストールされています。Androidスマートフォンに**Driver Station** を正常にインストールしたら、**Control Hub** と**DRIVER STATION** の間にセキュアなワイヤレス接続を確立します。この接続により、**DRIVER STATION** デバイスは**Robot Controller** で**Op Mode** を選択し、これらのプログラムにゲームパッド入力を送信できます。同様に、**Robot Controller** で実行されている**Op Mode** は、**DRIVER STATION** スマートフォンにテレメトリデータを送信でき、そこでドライバー用に表示できます。2つのデバイスを接続するプロセスは「ペアリング」として知られています。
```

### Block 54 (line 214)

```
また、このタスクを完了するには約10分かかることに注意してください。
```

### Block 55 (line 237)

```
   * - 手順
     - 画像
```

### Block 56 (line 240)

```
   * - 1. 承認された12Vバッテリーを電源スイッチ（REV-31-1387）に接続し、スイッチがオフ位置にあることを確認します。スイッチを **Control Hub** のXT30ポートに接続し、スイッチをオンにします。**Control Hub** のLEDは最初は青色になります。
```

### Block 57 (line 243)

```
   * - 2. **Control Hub** の電源が入るまでに約18秒かかります。LEDが緑色に変わると、**Control Hub** は**Driver Station** とのペアリングの準備ができています。注：ライトは約5秒ごとに青色で点滅して、**Control Hub** が正常であることを示します。
```

### Block 58 (line 246)

```
   * - 3. **Driver Station** デバイスで、利用可能なアプリを参照し、**FTC Driver Station** アイコンを見つけます。アイコンをタップして、**Driver Station** アプリを起動します。初めてアプリを起動するときは、アプリが正しく実行するために必要な権限をAndroidデバイスが要求する場合があることに注意してください。プロンプトが表示されたら、**Allow** を押して要求された権限を付与します。
```

### Block 59 (line 249)

```
   * - 4. **Driver Station** アプリのメイン画面の右上隅にある縦に並んだ3つのドットをタッチします。これにより、ポップアップメニューが起動します。
```

### Block 60 (line 252)

```
   * - 5. ポップアップメニューから **Settings** を選択します。
```

### Block 61 (line 255)

```
   * - 6. **Settings** 画面から、**Pairing Method** を探して選択し、**Pairing Method** 画面を起動します。
```

### Block 62 (line 258)

```
   * - 7. **Control Hub** という言葉をタッチして、この**DRIVER STATION** が**Control Hub** とペアリングすることを示します。
```

### Block 63 (line 261)

```
   * - 8. **Settings** 画面から、**Pair with Robot Controller** を探して選択し、**Pair with Robot Controller** 画面を起動します。
```

### Block 64 (line 264)

```
   * - 9. **Pair with Robot Controller** 画面から、**Wifi Settings** ボタンを探して押し、デバイスのAndroid WifiSettings画面を起動します。
```

### Block 65 (line 267)

```
   * - 10. 利用可能なWiFiネットワークのリストから、**Control Hub** のワイヤレスネットワークの名前を見つけます。ネットワーク名をクリックして、ネットワークを選択します。**Control Hub** に初めて接続する場合、デフォルトのネットワーク名はプレフィックスFTC-で始まるはずです（この例ではFTC-1Ybr）。デフォルトのネットワーク名は、**Control Hub** の底面に貼られたステッカーに記載されています。
```

### Block 66 (line 270)

```
   * - 11. プロンプトが表示されたら、**Control Hub** のWiFiネットワークのパスワードを指定し、**Connect** を押してHubに接続します。**Control Hub** ネットワークのデフォルトパスワードは ``password`` であることに注意してください。また、**Control Hub** のWiFiネットワークに正常に接続すると、**DRIVER STATION** はインターネットにアクセスできなくなることに注意してください。
```

### Block 67 (line 273)

```
   * - 12. Hubに正常に接続したら、戻る矢印を使用して前の画面に戻ります。「Current Robot Controller:」の下にWiFiネットワークの名前が表示されるはずです。戻る矢印キーを使用してSettings画面に戻ります。次に、戻る矢印キーをもう一度押して、メインの **DRIVER STATION** 画面に戻ります。
```

### Block 68 (line 276)

```
   * - 13. **DRIVER STATION** 画面が変更され、**Control Hub** に接続されていることが示されていることを確認します。**Control Hub** のWiFiネットワークの名前（この例ではFTC-1Ybr）が、**Driver Station** のNetworkフィールドに表示されます。
```

### Block 69 (line 282)

```
2台のAndroidスマートフォンのペアリング
```

### Block 70 (line 287)

```
Androidスマートフォンにアプリを正常にインストールしたら、2つのデバイス間にセキュアなワイヤレス接続を確立します。この接続により、**DRIVER STATION** デバイスは**Robot Controller** スマートフォンで**Op Mode** を選択し、これらのプログラムにゲームパッド入力を送信できます。同様に、**Robot Controller** スマートフォンで実行されている**Op Mode** は、**DRIVER STATION** デバイスにテレメトリデータを送信でき、そこでドライバー用に表示できます。2台のスマートフォンを接続するプロセスはペアリングとして知られています。
```

### Block 71 (line 289)

```
このタスクを完了するには約10分かかることに注意してください。
```

### Block 72 (line 312)

```
   * - 手順
     - 画像
```

### Block 73 (line 315)

```
   * - 1. **Robot Controller** デバイスで、利用可能なアプリを参照し、**FTC Robot Controller** アイコンを見つけます。アイコンをタップして、**Robot Controller** アプリを起動します。初めてアプリを起動するときは、アプリが正しく実行するために必要な権限をAndroidデバイスが要求する場合があることに注意してください。プロンプトが表示されたら、**Allow** を押して要求された権限を付与します。
```

### Block 74 (line 318)

```
   * - 2. **Robot Controller** アプリが実行されていることを確認します。正しく動作している場合、**Robot Status** フィールドにはrunningと表示されるはずです。
```

### Block 75 (line 321)

```
   * - 3. **DRIVER STATION** デバイスで、利用可能なアプリを参照し、**FTC Driver Station** アイコンを見つけます。アイコンをタップして、**Driver Station** アプリを起動します。初めてアプリを起動するときは、アプリが正しく実行するために必要な権限をAndroidデバイスが要求する場合があることに注意してください。プロンプトが表示されたら、**Allow** を押して要求された権限を付与します。
```

### Block 76 (line 324)

```
   * - 4. **Driver Station** アプリのメイン画面の右上隅にある縦に並んだ3つのドットをタッチします。これにより、ポップアップメニューが起動します。
```

### Block 77 (line 327)

```
   * - 5. ポップアップメニューから **Settings** を選択します。
```

### Block 78 (line 330)

```
   * - 6. **Settings** 画面から、**Pairing Method** を探して選択し、**Pairing Method** 画面を起動します。
```

### Block 79 (line 333)

```
   * - 7. **Wifi Direct** モードが選択されていることを確認します。これは、この**DRIVER STATION** が別のAndroidデバイスとペアリングすることを意味します。
```

### Block 80 (line 336)

```
   * - 8. **Settings** 画面から、**Pair with Robot Controller** を探して選択し、**Pair with Robot Controller** 画面を起動します。
```

### Block 81 (line 339)

```
   * - 9. リストから **Robot Controller** の名前を見つけて選択します。選択したら、戻る矢印キーを使用してSettings画面に戻ります。次に、戻る矢印キーをもう一度押して、メインの**DRIVER STATION** 画面に戻ります。
```

### Block 82 (line 342)

```
   * - 10. **DRIVER STATION** がメイン画面に戻ると、**Robot Controller** への接続を初めて試みるときに、**Robot Controller** 画面にプロンプトが表示されます。**ACCEPT** ボタンをクリックして、**DRIVER STATION** からの接続リクエストを受け入れます。
```

### Block 83 (line 345)

```
   * - 11. **DRIVER STATION** 画面が変更され、**Robot Controller** に接続されていることが示されていることを確認します。**Robot Controller** のリモートネットワークの名前（この例では9999-C-RC）が、**DRIVER STATION** のNetworkフィールドに表示されます。
```

### Block 84 (line 348)

```
   * - 12. **Robot Controller** 画面が変更され、**DRIVER STATION** に接続されていることが示されていることを確認します。**Robot Controller** のメイン画面で、Network statusにはactive、connectedと表示されるはずです。
```


## programming_resources/shared/control_system_intro/The-FTC-Control-System.rst

### Block 1 (line 1)

```
制御システム入門
```

### Block 2 (line 4)

```
*FIRST* Tech Challenge について
```

### Block 3 (line 7)

```
*FIRST* Tech Challenge は、メンター指導による競技ロボットへの参加を通じて、若者が次世代のSTEMリーダーやイノベーターになるよう刺激することを目指しています。*FIRST* Tech Challenge に参加するチームは、さまざまなタスクを実行するロボットを構築する必要があります。タスクはシーズンごとに異なり、各シーズンの開始時に公開されるゲームルールに基づいています。ロボットが完了できるタスクが多いほど、チームはより多くのポイントを獲得できます。
```

### Block 4 (line 16)

```
AUTO と TELEOP
```

### Block 5 (line 19)

```
*FIRST* Tech Challenge のマッチには、**AUTO** フェーズと**TELEOP** フェーズがあります。マッチの**AUTO** フェーズでは、ロボットは人間の入力や制御なしで動作します。**TELEOP** フェーズでは、ロボットは最大2人の人間ドライバーから入力を受け取ることができます。
```

### Block 6 (line 21)

```
ポイントツーポイント制御システム
```

### Block 7 (line 24)

```
*FIRST* Tech Challenge では、Android デバイスを使用してロボットを制御します。競技中、各チームは2つの Android デバイスを使用します。
```

### Block 8 (line 31)

```
1つの Android デバイスはロボットに搭載され、**Robot Controller** と呼ばれます。ほとんどの場合、**Robot Controller** は**REV Robotics Control Hub** に統合されています。**Robot Controller** はロボットの「頭脳」として機能します。ロボットのすべての思考を行い、ロボットに何をすべきかを指示します。**Robot Controller** アプリを実行する Android デバイスで構成されています。多くのチームは、モーター、サーボ、センサーをロボットに接続するための追加ポートとして、**REV Robotics Expansion Hub** も接続します。
```

### Block 9 (line 33)

```
2つ目の Android デバイスは、チームのドライバーと一緒に配置され、1つまたは2つのゲームパッドが接続されます。この2つ目のデバイスは **Driver Station** として知られています。**Driver Station** は、テレビを制御するために使用するリモコンのようなものです。**Driver Station** により、チームは（安全なワイヤレス接続を使用して）**Robot Controller** とリモート通信し、**Robot Controller** にコマンドを発行できます。**Driver Station** は、**Driver Station** アプリを実行する Android デバイスで構成されています。ほとんどのチームは**REV Robotics Driver Hub** を使用しますが、一部の Android スマートフォンもサポートされています。
```

### Block 10 (line 35)

```
REV Robotics Control Hub と Expansion Hub
```

### Block 11 (line 38)

```
**REV Robotics Control Hub** または**Expansion Hub** は、**Robot Controller** がロボットのモーター、サーボ、センサーと通信できるようにする電子入出力（「I/O」）モジュールです。**Robot Controller** は**Control Hub** に統合されており、シリアル接続を介して**Expansion Hub** と通信します。Android スマートフォンを**Robot Controller** として使用する場合は、USB ケーブルを使用してシリアル接続を確立します。
```

### Block 12 (line 40)

```
**Control Hub** と**Expansion Hub** は、12V バッテリーにも接続されており、**Control Hub**、**Expansion Hub**、モーター、サーボ、センサーに電力を供給します。Android スマートフォンを**Robot Controller** として使用する場合、スマートフォンには独自の独立したバッテリーがあります。
```

### Block 13 (line 47)

```
Android スマートフォン
```

### Block 14 (line 50)

```
チームは、Android スマートフォンを **Driver Station**、**Robot Controller**、またはその両方として使用することを選択できます。**Driver Station** のスマートフォンには、**FTC Driver Station** アプリをインストールする必要があり、ゲームパッドを接続するには OTG アダプター USB ハブが必要です。
```

### Block 15 (line 57)

```
Android スマートフォンを **Robot Controller** として使用するチームは、モーター、サーボ、センサーを接続するために追加の**REV Robotics Expansion Hub** を必要とします。スマートフォンは、USB-A to USB-Mini ケーブルと OTG アダプターを介して**Expansion Hub** に接続されます。
```

### Block 16 (line 64)

```
OpMode とは？
```

### Block 17 (line 67)

```
*FIRST* Tech Challenge のマッチでは、チームのロボットは得点を獲得するためにさまざまなタスクを実行する必要があります。たとえば、競技フィールド上の白い線をロボットに追従させ、マッチ中に自律的にゲーム要素（ボールなど）をゴールに得点させたいと考えるかもしれません。チームは、ロボットの動作を指定するために「**OpMode**」（「operational mode（動作モード）」の略）を作成します。
```

### Block 18 (line 69)

```
**OpMode** は、競技ロボットの動作をカスタマイズするために使用されるコンピュータプログラムです。**Robot Controller** は、選択された**OpMode** を実行して、マッチ中に特定のタスクを実行できます。
```

### Block 19 (line 71)

```
*FIRST* Tech Challenge に参加しているチームは、独自の **OpMode** を作成するために使用できるさまざまなプログラミングツールを持っています。チームは、**Blocks Programming Tool** と呼ばれるビジュアル（「ドラッグアンドドロップ」）プログラミングツールを使用して**OpMode** を作成できます。チームは、**OnBot Java Programming Tool** として知られるテキストベースの Java ツール、または Google の**Android Studio** 統合開発環境（「IDE」としても知られる）を使用して**OpMode** を作成することもできます。
```


## programming_resources/shared/installing_javascript_browser/Installing-a-Javascript-Enabled-Browser.rst

### Block 1 (line 1)

```
JavaScript 対応ブラウザのインストール
```

### Block 2 (line 4)

```
**Blocks** プログラミングツールまたは**OnBot Java** プログラミングツールを使用して**Robot Controller** をプログラムできるようにするには、ラップトップに JavaScript 対応ブラウザが必要です。両方のツールは、**Robot Controller** の Program and Manage サーバーによって提供される JavaScript アプリケーションです。
```

### Block 3 (line 6)

```
**Blocks** プログラミングツールと**OnBot Java** プログラミングツールは、ほとんどの最新のウェブブラウザで動作するはずです。ただし、**FIRST** は、これらのツールで Google Chrome を使用することを強く推奨しています。ブラウザとして Google Chrome を使用したい場合は、Google Chrome ウェブサイトから無料でダウンロードできます。
```

### Block 4 (line 8)

```
JavaScript 対応ブラウザのダウンロードとインストールには、推定 15 分（インターネット接続の速度による）かかることに注意してください。
```

### Block 5 (line 11)

```
JavaScript 対応ブラウザのインストール手順
```

### Block 6 (line 14)

```
1. `Google Chrome ブラウザウェブサイト <https://www.google.com/chrome>`__ にアクセスし（コンピューターの既存のブラウザを使用）、画面の指示に従って Chrome をダウンロードしてインストールします。
```

### Block 7 (line 23)

```
2. インストールプロセス中に、コンピューターがセキュリティ警告を表示する場合があることに注意してください。この警告が表示された場合は、「Run」ボタンをクリックしてインストールを続行します。
```


## programming_resources/shared/installing_kotlin/Installing-Kotlin.rst

### Block 1 (line 1)

```
**Kotlin** プログラミング言語の使用
```

### Block 2 (line 5)

```
**Kotlin** とは？
```

### Block 3 (line 9)

```
**Kotlin** プログラミング言語は、Java Virtual Machine（JVM）でコンパイルおよび実行される Java プログラミング言語の現代的な代替であり、Android アプリケーションの開発に使用できます。これは、IntelliJ IDE（**Android Studio** の基礎）を開発した同じ会社である JetBrains によって開発されました。
```

### Block 4 (line 13)

```
Java に基づいているため、**Kotlin** は多くの同じ機能と構文を共有しています。ただし、コードを書きやすく、エラーが発生しにくくする多くの新しい機能と構文も追加しています。**Kotlin** の機能には次のものがあります：
```

### Block 5 (line 15)

```
* Java との完全な相互運用性。**Kotlin** から Java クラスとライブラリを使用でき、その逆も可能です。
* 型推論。**Kotlin** では、必要に応じて型推論を使用できます。つまり、コンテキストから推論できる場合、変数の型を指定する必要はありません（``var myString = "Hi!"`` ）。
* セミコロンなし。**Kotlin** では、ステートメントを終了するためにセミコロンは必要ありません。
* データクラス。**Kotlin** には、データを保存するために使用されるクラスを作成するための簡潔な構文があります。
* 拡張関数。**Kotlin** では、元のクラスを変更することなく、既存のクラスに関数を追加できます。
* Null 安全性。**Kotlin** には、null ポインター例外を排除するのに役立つ型システムがあります。
* 演算子のオーバーロード。**Kotlin** では、``+`` や``*`` などの演算子が独自のクラスでどのように機能するかを定義できます。
* その他多数！
```

### Block 6 (line 24)

```
さらに、**Kotlin** でゼロからコーディングする方法を学びたくない場合、**Android Studio**IDE には、コードのセクションまたは Java ファイル全体を**Kotlin** ファイルに変換するツールがあります。これは、特定の Java コードが**Kotlin** でどのように記述されているかを学ぶのに非常に役立ちます。
```

### Block 7 (line 26)

```
**Kotlin** は完全に相互運用可能であるため、既存のすべての Java コードを変換することなく、**Kotlin** プロジェクトで使用することもできます。
```

### Block 8 (line 29)

```
**FIRST** **Tech Challenge** での**Kotlin** の使用
```

### Block 9 (line 33)

```
このドキュメントの執筆時点では、**FIRST** **Tech Challenge** でプログラミングオプションとして**Kotlin** を禁止する規則はありませんが、公式にサポートまたは推奨されている言語ではありません。**Kotlin** を使用するチームは、自己責任で使用し、ソフトウェアの問題が発生した場合、イベントでテクニカルヘルプ/サポートが利用できないことを予期する必要があります。
```

### Block 10 (line 36)

```
プロジェクトへの **Kotlin** のインストール
```

### Block 11 (line 40)

```
Android プロジェクトで **Kotlin** を使用するには、プロジェクトに**Kotlin** プラグインを追加する必要があります。これは、``buildscript`` セクションのルート``build.gradle`` ファイルに次の行を追加することによって行われます：
```

### Block 12 (line 55)

```
次に、``TeamCode`` モジュールの``build.gradle`` ファイルに次の行を追加します：
```

### Block 13 (line 63)

```
        // 他の依存関係...
```

### Block 14 (line 66)

```
これで、プロジェクトで **Kotlin** を使用する準備が整いました！
```

### Block 15 (line 69)

```
**Kotlin** **OpMode** の作成
```

### Block 16 (line 73)

```
**Kotlin** で**OpMode** を作成するには、``TeamCode`` フォルダーに新しい**Kotlin** ファイルを作成し、Java**OpMode** と同じ方法で作成します。主な違いは、**Kotlin** 構文を使用することです。
```

### Block 17 (line 75)

```
Java の例：
```

### Block 18 (line 95)

```
**Kotlin** の同等のもの：
```

### Block 19 (line 114)

```
**Kotlin** について詳しく知りたい場合は、公式の**Kotlin** ドキュメント https://kotlinlang.org/docs/home.html を参照してください。
```


## programming_resources/shared/managing_control_hub/Managing-a-Control-Hub.rst

### Block 1 (line 1)

```
Control Hubの管理
```

### Block 2 (line 4)

```
名前の変更
```

### Block 3 (line 7)

```
デフォルトでは、**Control Hub** は「FTC-」で始まり、工場で割り当てられた4文字で終わる名前を持っています。競技マニュアルに準拠するため、名前を変更する必要があります。
```

### Block 4 (line 9)

```
**Control Hub** （または**Robot Controller** スマートフォン）の名前は、ペアリングされた**DS** アプリから変更できます。詳細は :ref:`名前の変更<programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller:changing the name>` を参照してください。
```

### Block 5 (line 11)

```
または、接続された **Driver Station** またはラップトップから *Manage* ページで **Control Hub** の名前を変更することもできます。以下に説明します。変更後は ``Apply Wi-Fi Settings`` をクリックしてください。
```

### Block 6 (line 15)

```
Control Hubの名前を変更する手順
```

### Block 7 (line 18)

```
1. ラップトップまたはChromebookが **Control Hub** のProgram & Manageワイヤレスネットワークに接続されていることを確認します。ネットワークに接続されている場合、アドレス「192.168.43.1:8080」にアクセスすると、*Robot Controller Connection Info* ページが表示されるはずです：
```

### Block 8 (line 25)

```
   ラップトップまたはChromebookが接続されておらず、*Robot Controller Connection Info* ページにアクセスできない場合は、以下のチュートリアルの手順を読んで、Program & Manageネットワークへの接続方法を学んでください。
```

### Block 9 (line 29)

```
2. *Robot Controller Connection Info* ページの上部にある *Manage* リンクをクリックして、Manageページに移動します。
```

### Block 10 (line 36)

```
3. *Robot Controller Name* フィールドで名前を変更し、*Change Name* ボタンをクリックして **Control Hub** の名前を変更します。
```

### Block 11 (line 43)

```
4. *Change Name* ボタンを押すと、ダイアログボックスが表示され、名前が変更されたこと、および新しいワイヤレスネットワークに接続して現在のページを更新する必要があることが示されます。
```

### Block 12 (line 50)

```
パスワードの変更
```

### Block 13 (line 53)

```
デフォルトでは、**Control Hub** のパスワードは工場出荷時に「password」に設定されています。**Control Hub** の使用を開始する前に、パスワードをデフォルト値から変更することをお勧めします。
```

### Block 14 (line 55)

```
**Control Hub** のProgram & ManagementページにHubに接続されたラップトップまたはChromebookを使用して、**Control Hub** のパスワードを変更できます。
```

### Block 15 (line 59)

```
Control Hubのパスワードを変更する手順
```

### Block 16 (line 62)

```
1. **Control Hub** ユーザーインターフェースの *Manage* ページで、ページの *Access Point Password* セクションに新しいパスワードを指定し、この新しいパスワードを確認します。*Change Password* ボタンを押してパスワードを変更します。
```

### Block 17 (line 69)

```
2. *Change Password* ボタンを押すと、ダイアログボックスが表示され、パスワードが変更されたこと、および新しいパスワードを使用してワイヤレスネットワークに再接続する必要があることが示されます。
```

### Block 18 (line 76)

```
Control Hubのリセット
```

### Block 19 (line 79)

```
**Control Hub** のネットワーク名またはパスワードを忘れた場合、Hubの名前とパスワードを工場出荷時のデフォルト値にリセットできます。
```

### Block 20 (line 83)

```
リセット手順
```

### Block 21 (line 86)

```
1. **Control Hub** の電源を5秒間オフにします。
2. **Control Hub** のボタンを押し続けます（下の画像を参照）。
```

### Block 22 (line 94)

```
3. ボタンを押し続けながら、**Control Hub** の電源を入れます。**Control Hub** が再起動している間、LEDを監視します。最終的に、LEDは青色の点灯から、複数色の点滅パターンに切り替わります。
```

### Block 23 (line 96)

```
   リセットが開始されると、LEDは紫、黄、青、赤の順に点滅します。このパターンは5回連続して高速に発生します。
```

### Block 24 (line 98)

```
   複数色の点滅パターンが完了したら、ボタンを離すことができます。**Control Hub** のネットワーク名とパスワードが工場出荷時の値に復元されます。再起動とリセットのプロセスは、完了するまでに約30秒かかることに注意してください。
```

### Block 25 (line 100)

```
WiFiチャンネルの変更
```

### Block 26 (line 103)

```
**Control Hub** は、**Driver Station** とプログラミング用ラップトップまたはChromebook用のワイヤレスアクセスポイントとして機能します。デフォルトでは、**Control Hub** は動作するWiFiチャンネルを自動的に選択します。ただし、Hubの動作チャンネルを指定する必要がある場合があります。
```

### Block 27 (line 105)

```
たとえば、大規模な競技会では、会場に存在するワイヤレス干渉を避けるために、FTAが指定されたチャンネルに切り替えるように要求する場合があります。同様に、FTAが干渉やその他のワイヤレス障害のために指定されたチャンネルを監視しているため、特定のチャンネルに切り替えるように要求する場合があります。
```

### Block 28 (line 107)

```
*Manage* ページから **Control Hub** の動作チャンネルを選択できます。
```

### Block 29 (line 109)

```
WiFiチャンネルを変更する手順
```

### Block 30 (line 112)

```
1. **Control Hub** ユーザーインターフェースの *Manage* ページで、ドロップダウンセレクターを使用して、希望する動作チャンネルを選択します。**Control Hub** は2.4 GHzと5 GHzの両方のバンドをサポートしていることに注意してください。
```

### Block 31 (line 119)

```
2. *Change Channel* ボタンを押して、新しいチャンネルに変更します。チャンネル変更が発生すると、**Driver Station** が**Control Hub** から一時的に切断される場合があることに注意してください。ただし、最終的には**Control Hub** のワイヤレスネットワークに再接続されます。
```

### Block 32 (line 121)

```
3. **Driver Station** で、**Control Hub** が希望するWiFiチャンネルで動作していることを確認します。動作チャンネルは、メインの**Driver Station** 画面の *Network* セクションのネットワーク名の下に表示されます。
```

### Block 33 (line 128)

```
ログファイルのダウンロード
```

### Block 34 (line 131)

```
制御システムの問題をトラブルシューティングする際に、**Control Hub** からログファイルをダウンロードすることが役立つことがよくあります。これは *Manage* ページから行うことができます。デフォルトでは、ログファイル名は *robotControllerLog.txt* です。
```

### Block 35 (line 133)

```
ログファイルをダウンロードする手順
```

### Block 36 (line 136)

```
1. **Control Hub** ユーザーインターフェースの *Manage* ページで、*Download Logs* ボタンを押して、**Robot Controller** ログファイルをダウンロードします。
```

### Block 37 (line 143)

```
2. **Robot Controller** ログファイルがコンピューターのDownloadsディレクトリにダウンロードされたことを確認します。
```

### Block 38 (line 145)

```
3. `Notepad++ <https://notepad-plus-plus.org/>`__ やMicrosoftのWordPadなどのテキストエディタを使用して、ログファイルの内容を開いて表示します。WindowsアプリのNotepadは、ログファイルの内容を正しく表示しないことに注意してください。
```

### Block 39 (line 152)

```
Expansion Hubファームウェアの更新
```

### Block 40 (line 155)

```
**Control Hub** には、独自の組み込み**REV Robotics Expansion Hub** があります。**Expansion Hub** ボードの目的は、**Control Hub** のAndroidコントローラーとロボットのモーター、サーボ、センサー間の通信を容易にすることです。REV Roboticsは定期的に、**Expansion Hub** の修正と改善を含むファームウェアの新しいバージョンをリリースします。ファームウェアリリースはバイナリ（.bin）ファイルの形式です。
```

### Block 41 (line 157)

```
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、**Control Hub** の組み込み**Expansion Hub** のファームウェアを更新できます。
```

### Block 42 (line 159)

```
または、接続されたラップトップまたは **Driver Station** （**DS** ）アプリから *Manage* インターフェースを使用して、**Control Hub** のファームウェアをアップロードしたり、含まれているバージョンまたはアップロードされたバージョンを使用して更新したりできます。新しいファームウェアイメージは、`REV Robotics ウェブサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware#using-the-robot-controller-console>`__ から入手できます。
```

### Block 43 (line 161)

```
また、含まれているまたはアップロードされた **Control Hub** ファームウェアは、ペアリングされた**Driver Station** （**DS** ）アプリから**Robot Controller** の詳細設定で更新できます（以下に示します）。
```

### Block 44 (line 163)

```
これらの3つの方法は、RS485データワイヤを介して **Control Hub** に接続された**Expansion Hub** のファームウェアを更新する場合には適用されません。スタンドアロンの**Expansion Hub** は、REV Hardware Clientを実行しているラップトップまたは**Robot Controller** スマートフォンに直接USB接続して更新する必要があります。
```

### Block 45 (line 165)

```
Expansion Hubファームウェアのアップロードと更新
```

### Block 46 (line 168)

```
1. **Control Hub** ユーザーインターフェースの *Manage* ページで、*Select Firmware* ボタンを押して、アップロードするファームウェアファイルを選択します。
```

### Block 47 (line 175)

```
   ファイルが正常に選択されると、*Upload* ボタンが表示されます。
```

### Block 48 (line 177)

```
2. *Upload* ボタンを押して、ファームウェアファイルをコンピューターから **Control Hub** にアップロードします。
```

### Block 49 (line 184)

```
   ファイルが正常にアップロードされると、「Firmware upload complete」という言葉が表示されます。
```

### Block 50 (line 186)

```
3. **Driver Station** で、右上隅の3つのドットをタッチして、ポップアップメニューを表示します。
```

### Block 51 (line 193)

```
4. ポップアップメニューから *Settings* を選択して、Settings アクティビティを表示します。
```

### Block 52 (line 200)

```
5. **Driver Station** で、下にスクロールして、*Advanced Settings* 項目（*ROBOT CONTROLLER SETTINGS* カテゴリの下）を選択します。
```

### Block 53 (line 207)

```
6. *ADVANCED ROBOT CONTROLLER SETTINGS* アクティビティで、*Expansion Hub Firmware Update* 項目を選択します。
```

### Block 54 (line 214)

```
7. **Expansion Hub** に現在インストールされているバージョンとは異なるファームウェアファイルが正常にアップロードされた場合、**Driver Station** には現在のファームウェアバージョンと新しいファームウェアバージョンに関する情報が表示されます。*Update Expansion Hub Firmware* ボタンを押して、更新プロセスを開始します。
```

### Block 55 (line 221)

```
8. ファームウェアが更新されている間、進行状況バーが表示されます。このプロセス中に **Control Hub**/**Expansion Hub** の電源を切らないでください。更新プロセスが完了すると、**Driver Station** にメッセージが表示されます。
```

### Block 56 (line 228)

```
Robot Controllerアプリの更新
```

### Block 57 (line 231)

```
**Control Hub** にインストールされている**Robot Controller** アプリを更新する方法を知っておくことは重要です。**FIRST** は、改善と修正、およびシーズン固有のデータと機能を含む、このアプリの新しいバージョンを定期的にリリースします。
```

### Block 58 (line 233)

```
**Driver Station** ユーザーインターフェースを通じて、**Robot Controller** アプリのバージョン番号を確認できます。**Driver Station** で *About* メニューオプションを選択し、*ABOUT ROBOT CONTROLLER* セクションの下のApp Version番号を確認してください。
```

### Block 59 (line 240)

```
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、**Control Hub** の**Robot Controller** （**RC** ）アプリを更新できます。
```

### Block 60 (line 242)

```
または、**Control Hub** ユーザーは、**FIRST Tech Challenge**`Githubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ から**RC** アプリをダウンロードし、*Manage* ページを使用して更新を完了できます。
```

### Block 61 (line 244)

```
**Android Studio** ユーザーの場合は、**Android Studio** プロジェクトフォルダーの最新バージョンに更新することで、プロジェクトをビルドして**Control Hub** にインストールするときに**Robot Controller** アプリが更新されます。
```

### Block 62 (line 248)

```
Robot Controllerアプリを更新する手順
```

### Block 63 (line 251)

```
1. `GitHubリポジトリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ にアクセスします。
```

### Block 64 (line 253)

```
2. *FtcRobotController-release.apk* ファイルを見つけます。
```

### Block 65 (line 260)

```
3. ファイル名（または *Download* ボタン）をクリックして、**Robot Controller** アプリをAPKファイルとしてコンピューターにダウンロードします。
```

### Block 66 (line 267)

```
4. *Manage* ページで、*Select App* ボタンをクリックして、**Control Hub** にアップロードする**Robot Controller** アプリを選択します。
```

### Block 67 (line 274)

```
   APKファイルが正常に選択されると、*Update* ボタンが表示されます。
```

### Block 68 (line 276)

```
5. *Update* ボタンをクリックして、更新プロセスを開始します。
```

### Block 69 (line 283)

```
6. 更新プロセス中に、**Control Hub** がインストールされるAPKのデジタル署名が既にインストールされているAPKのデジタル署名と異なることを検出した場合、Hubは現在のアプリをアンインストールして新しいアプリに置き換えてもよいかを尋ねるプロンプトを表示する場合があります。
```

### Block 70 (line 285)

```
   このデジタル署名の違いは、たとえば、以前のバージョンのアプリが **Android Studio** を使用してビルドおよびインストールされたが、新しいアプリがGitHubリポジトリからダウンロードされた場合に発生する可能性があります。
```

### Block 71 (line 287)

```
   *OK* を押して、古いアプリをアンインストールし、更新プロセスを続行します。
```

### Block 72 (line 294)

```
7. 更新プロセスで以前のバージョンの **Robot Controller** アプリをアンインストールする必要があった場合、**Control Hub** のネットワーク名とパスワードは工場出荷時の値にリセットされます。この場合、工場出荷時のデフォルト値を使用して、コンピューターを**Control Hub** に再接続する必要があります。
```

### Block 73 (line 301)

```
8. 更新プロセスが完了し、コンピューターが **Control Hub** のネットワークに正常に再接続されると、*Manage* ウェブページに *installed successfully* メッセージが表示されます。
```

### Block 74 (line 308)

```
カスタムウェブカメラキャリブレーションファイルのアップロード
```

### Block 75 (line 311)

```
**Robot Controller** アプリには、一般的に利用可能なさまざまなウェブカメラ用の組み込みキャリブレーション情報があります。ユーザーは独自のカスタムキャリブレーションファイルを作成し、これらのファイルを**Control Hub** にアップロードすることもできます。
```

### Block 76 (line 313)

```
キャリブレーションファイルの内容がどのようになるべきかについての注釈付きの例は、**Android Studio** プロジェクトフォルダーに含まれている *teamwebcamcalibrations.xml* というファイルにあります。
この例のキャリブレーションファイルは `こちら <https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__ にあります。
```

### Block 77 (line 316)

```
カスタムウェブカメラキャリブレーションファイルをアップロードする手順
```

### Block 78 (line 319)

```
1. *Manage* ページで、*Select Webcam Calibration File* ボタンをクリックして、キャリブレーションファイルを選択します。
```

### Block 79 (line 326)

```
   ファイルが正常に選択されると、*Upload* ボタンが表示されます。
```

### Block 80 (line 328)

```
2. *Upload* ボタンをクリックして、選択したファイルをアップロードします。アップロードが成功した場合、*Manage* ページにアップロードが完了したことを示すメッセージが表示されます。
```

### Block 81 (line 335)

```
Control Hub OSの更新
```

### Block 82 (line 338)

```
REV Roboticsは、**Control Hub** オペレーティングシステム（OS）の新しいバージョンを定期的にリリースします。これらの新しいバージョンには、修正、改善、および新機能が組み込まれています。
```

### Block 83 (line 340)

```
**Driver Station** ユーザーインターフェースを通じて、**Control Hub**OSのバージョン番号を確認できます。**Driver Station** で *About* メニューオプションを選択し、*ABOUT ROBOT CONTROLLER* セクションの下のOperating System Version番号を確認してください。
```

### Block 84 (line 347)

```
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、**Control Hub** オペレーティングシステムを更新できます。
```

### Block 85 (line 349)

```
または、**Control Hub** ユーザーは、REV Roboticsウェブサイトから新しい**Control Hub** OSファイルをダウンロードし、*Manage* ページを使用してOSの更新を完了できます。
```

### Block 86 (line 351)

```
Control Hub OSを更新する手順
```

### Block 87 (line 354)

```
1. `REV Roboticsウェブサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system>`__ から新しい **Control Hub** OS更新ファイルをダウンロードします。
```

### Block 88 (line 356)

```
2. *Manage* ページで、*Select Update File* ボタンをクリックして、アップロードするOS更新ファイルを選択します。
```

### Block 89 (line 363)

```
   更新ファイルが正常に選択されると、*Update & Reboot* ボタンが表示されます。
```

### Block 90 (line 365)

```
3. *Update & Reboot* ボタンをクリックして、更新プロセスを開始します。
OSファイルが **Control Hub** にアップロードされるまでお待ちください。ファイルが比較的大きいため、アップロードが完了するまでに数分かかる場合があることに注意してください。プロセスが進行中の間は、**Control Hub** の電源を切らないでください。
```

### Block 91 (line 373)

```
4. アップロードが成功した場合、*Manage* ページにデバイスが再起動中で、更新がインストールされていることを示すメッセージが表示されます。
```

### Block 92 (line 380)

```
5. OS更新が完了すると、**Control Hub**LEDは青色から通常の点滅パターン（緑色、次にHubのシリアルアドレス番号を示すために1回青色で点滅し、そのパターンが繰り返されます）に戻ります。コンピューターを**Control Hub** ネットワークに再接続し、更新が成功したことを確認します。
```

### Block 93 (line 387)

```
   **Control Hub**OSの更新されたバージョン番号を確認するには、（**Driver Station** アプリを通じて）Aboutページでも確認できます。
```

### Block 94 (line 394)

```
ワイヤレスADBを使用してControl Hubに接続する
```

### Block 95 (line 397)

```
**Android Studio** を使用して**Robot Controller** アプリを**Control Hub** にビルドしてインストールする上級ユーザーは、Android Debug Bridge（**adb** ）ユーティリティに精通している必要があります。**adb** は、Android開発プラットフォームツールに含まれています。**Control Hub** などのAndroidデバイスと通信するために使用できます。
```

### Block 96 (line 399)

```
従来、プログラマーは、**adb** を使用してAndroidデバイスと通信するために、有線USB接続を使用します。**adb** は、ワイヤレス接続を介してコマンドを送受信するモードもサポートしています。
```

### Block 97 (line 401)

```
**Control Hub** は、ポート5555で**adb** ワイヤレス接続リクエストを自動的にサポートするように構成されています。
```

### Block 98 (line 403)

```
ワイヤレスADBを使用してControl Hubに接続する手順
```

### Block 99 (line 406)

```
1. ラップトップが **Control Hub** のProgram & Manageワイヤレスネットワークに接続されていることを確認します。ネットワークに接続されている場合、アドレス「192.168.43.1:8080」にアクセスすると、*Robot Controller Connection Info* ページが表示されるはずです：
```

### Block 100 (line 413)

```
   ラップトップが接続されておらず、*Robot Controller Connection Info* ページにアクセスできない場合は、以下のチュートリアル（Connecting-a-Laptop-to-the-Program-&-Manage-Network）の手順を読んで、Program & Manageネットワークへの接続方法を学んでください。
```

### Block 101 (line 417)

```
2. Windowsコンピューターのパス環境変数に、adb.exe実行可能ファイルへのパスが含まれていることを確認します。`Android Developerウェブサイト <https://developer.android.com/tools/adb>`__ には、Android SDKインストールのどこでadb.exeファイルを見つけることができるかが記載されています。`HelpDeskGeek.com <https://helpdeskgeek.com/add-windows-path-environment-variable/>`__ からの `この投稿 <https://helpdeskgeek.com/add-windows-path-environment-variable/>`__ は、Windowsのパス環境変数にディレクトリを追加する方法を示しています。
```

### Block 102 (line 419)

```
3. Windowsコマンドプロンプトを開き、「adb.exe connect 192.168.43.1:5555」と入力します。これにより、**adb** サーバーがワイヤレス接続を介して**Control Hub** に接続されます。
```


## programming_resources/shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station.rst

### Block 1 (line 1)

```
**Driver Hub** の管理
```

### Block 2 (line 7)

```
`REV Driver Hub <https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications>`__ には、**Driver Station (DS)** アプリがプリロードされています。以下の**REV Driver Hub** について説明する手順は、**Android** スマートフォンを DS として使用する場合にも適用されます。
```

### Block 3 (line 9)

```
名前の変更
```

### Block 4 (line 12)

```
**Competition Manual** に準拠するために、**Driver Station (DS)** の名前を変更する必要があります。チーム番号に合わせてデバイスを構成します。使用する**ROBOT CONTROLLER**、**DRIVER STATION** 、および予備は、次のように正しいチーム番号に対応するように構成/名前を付ける必要があります：
```

### Block 5 (line 14)

```
A.     **ROBOT CONTROLLER** は <チーム番号>-RC（例：12345-RC）という名前にする必要があります。
```

### Block 6 (line 16)

```
B.     **DRIVER STATION** は <チーム番号>-DS（例：12345-DS）という名前にする必要があります。
```

### Block 7 (line 18)

```
C.     予備の **ROBOT CONTROLLER** または**DRIVER STATION** が構成されている場合、文字指定子を追加できます <チーム番号>-<文字>-RC/DS（例：12345-A-DS、12345-B-DS）
```

### Block 8 (line 20)

```
*Control, Command & Signals System* に関連する規則については、現在の **Competition Manual** を確認してください。
```

### Block 9 (line 22)

```
**Driver Hub** の名前は、以下に説明するように DS アプリで変更できます。
```

### Block 10 (line 26)

```
   制御システムにスマートフォンを使用している場合、:ref:`このリンク <programming_resources/shared/configuring_android/Configuring-Your-Android-Devices:Renaming Your Smartphones>` は、スマートフォンの Android Settings アクティビティを使用してスマートフォンの名前を変更する方法を示しています。
```

### Block 11 (line 30)

```
   DS 画面に黄色の丸い感嘆符アイコンが表示され、それをタッチすると、「*DS* does not match *DS*, see the FTC Competition Manual」というメッセージが一時的にポップアップ表示されます。
   注：*DS* は **Driver Station** の現在の名前で、*RC* は現在の **Robot Controller** の名前です。
```

### Block 12 (line 33)

```
   これは、DS と RC の名前が一致しないためです。**Competition Manual** で要求されているように、上記のように両方の名前をチーム番号を含むように変更する必要があります。
```

### Block 13 (line 37)

```
      :alt: 黄色のアイコンの不一致と名前の不一致ポップアップメッセージを示す Driver Station 画面。
```

### Block 14 (line 39)

```
**Driver Station** の名前を変更する手順
```

### Block 15 (line 42)

```
1. **Driver Station** アプリで、右上隅の3つのドットをタッチして、ポップアップメニューを表示します。
```

### Block 16 (line 46)

```
   :alt: 3つのドットがオレンジ色の円で強調表示された Driver Station メイン画面。
```

### Block 17 (line 50)

```
2. ポップアップメニューから *Settings* メニュー項目を選択します。
```

### Block 18 (line 54)

```
   :alt: Settings オプションが強調表示されたポップアップメニュー。
```

### Block 19 (line 58)

```
3. *Driver Station Name* をタッチします。
```

### Block 20 (line 62)

```
   :alt: Driver Station Name が強調表示された Settings 画面。
```

### Block 21 (line 66)

```
4. 新しい **Driver Station** 名を入力し、OK をタッチして変更を保存します。
```

### Block 22 (line 70)

```
   :alt: 新しい名前を入力するためのダイアログボックス。
```

### Block 23 (line 74)

```
5. 変更を確認します。
```

### Block 24 (line 78)

```
   :alt: 新しい名前を表示する Settings 画面。
```

### Block 25 (line 81)

```
プログラムと管理ページへのアクセス
```

### Block 26 (line 84)

```
**Driver Hub** には、**Program & Manage**Web サーバーへのアクセスを提供する専用ボタンはありません。ただし、**Driver Station** アプリを使用して、**Robot Controller** の**Program & Manage** ページにアクセスできます。
```

### Block 27 (line 86)

```
1. **Driver Station** アプリで、右上隅の3つのドットをタッチします。
```

### Block 28 (line 88)

```
2. *Program & Manage* を選択します。
```

### Block 29 (line 90)

```
3. Web ブラウザーが開き、**Robot Controller** の**Program & Manage** ページが表示されます（**Robot Controller** がペアリングされ、アクティブである場合）。
```

### Block 30 (line 95)

```
バッテリーレベルの確認
```

### Block 31 (line 98)

```
**Driver Hub** のバッテリーレベルは、デバイスの上部に表示されます。バッテリーアイコンは、現在の充電レベルを示します。
```

### Block 32 (line 103)

```
まとめ
```

### Block 33 (line 106)

```
**Driver Hub** は、**Driver Station** アプリを実行するための専用デバイスです。使いやすく、スマートフォンを**Driver Station** として使用するよりも堅牢です。名前の変更、**Program & Manage** ページへのアクセス、バッテリーレベルの確認は、すべて**Driver Station** アプリから直接実行できます。
```


## programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller.rst

### Block 1 (line 1)

```
スマートフォンRobot Controllerの管理
```

### Block 2 (line 4)

```
名前の変更
```

### Block 3 (line 7)

```
競技マニュアルに準拠するため、**Robot Controller** （**RC** ）スマートフォンの名前を変更する必要があります。
```

### Block 4 (line 9)

```
これは、以下に説明するように、**RC** アプリまたはペアリングされた**DS** アプリで行うことができます。（これらの手順は、ペアリングされた**DS** アプリから**Control Hub** の名前を変更する場合にも機能します。）
```

### Block 5 (line 11)

```
または、:ref:`デバイスの名前変更<programming_resources/shared/configuring_android/Configuring-Your-Android-Devices:renaming your smartphones>` では、スマートフォンのAndroid設定アクティビティを使用してスマートフォンの名前を変更する方法を示しています。
```

### Block 6 (line 15)

```
Robot Controllerの名前を変更する手順
```

### Block 7 (line 18)

```
1. **Robot Controller** スマートフォンまたはペアリングされた**Driver Station** スマートフォンで、右上隅の3つのドットをタッチして、ポップアップメニューを表示します。
```

### Block 8 (line 25)

```
2. ポップアップメニューから *Settings* メニュー項目を選択します。
```

### Block 9 (line 32)

```
3. *ROBOT CONTROLLER SETTINGS* ページで、*Robot Controller Name* をクリックします。
```

### Block 10 (line 39)

```
4. 新しい **Robot Controller** 名を指定し、*OK* を押して変更を受け入れます。
```

### Block 11 (line 46)

```
WiFiチャンネルの変更
```

### Block 12 (line 49)

```
デフォルトでは、スマートフォン **Robot Controller** は自動的に独自の動作WiFiチャンネルを選択します。ただし、デバイスの動作チャンネルを指定する必要がある場合があります。
```

### Block 13 (line 51)

```
たとえば、大規模な競技会では、会場に存在するワイヤレス干渉を避けるために、FTAが指定されたチャンネルに切り替えるように要求する場合があります。同様に、FTAが干渉やその他のワイヤレス障害のために指定されたチャンネルを監視しているため、特定のチャンネルに切り替えるように要求する場合があります。
```

### Block 14 (line 53)

```
**Robot Controller** または**Driver Station** の詳細設定メニューを使用して、動作チャンネルを変更できます。
```

### Block 15 (line 57)

```
WiFiチャンネルを変更する手順
```

### Block 16 (line 60)

```
1. **Driver Station** が**Robot Controller** に接続されていることを確認します。
```

### Block 17 (line 62)

```
2. **Driver Station** のメイン画面の右上隅にある3つのドットをタップして、ポップアップメニューを表示し、メニューから *Settings* を選択します。
```

### Block 18 (line 64)

```
3. *Settings* 画面の *ROBOT CONTROLLER SETTINGS* セクションまで下にスクロールし、*Advanced Settings* という言葉をクリックして、*ADVANCED ROBOT CONTROLLER SETTINGS* アクティビティを表示します。
```

### Block 19 (line 71)

```
4. *Change Wifi Channel* リンクをクリックして、利用可能なチャンネルのリストを表示します。
```

### Block 20 (line 78)

```
5. 希望する動作チャンネルを選択します。チャンネル変更が成功した場合、スマートフォンにトーストメッセージが表示されます。
```

### Block 21 (line 85)

```
6. Androidの戻る矢印を使用して、メインの **Driver Station** 画面に戻ります。新しい動作チャンネルが、**Robot Controller** の名前の下の Network: セクションに表示されます。
```

### Block 22 (line 93)

```
ログファイルのダウンロード
```

### Block 23 (line 96)

```
制御システムの問題をトラブルシューティングする際に、**Robot Controller** からログファイルをダウンロードすることが役立つことがよくあります。これは *Manage* ページから行うことができます。デフォルトでは、ログファイル名は *robotControllerLog.txt* です。
```

### Block 24 (line 98)

```
ログファイルをダウンロードする手順
```

### Block 25 (line 101)

```
1. ラップトップまたはChromebookがスマートフォン **Robot Controller** のProgram & Manageワイヤレスネットワークに接続されていることを確認します。ネットワークに接続されている場合、アドレス「192.168.49.1:8080」にアクセスすると、*Robot Controller Connection Info* ページが表示されるはずです：
```

### Block 26 (line 108)

```
   ラップトップまたはChromebookが接続されておらず、*Robot Controller Connection Info* ページにアクセスできない場合は、以下のチュートリアルの手順を読んで、Program & Manageネットワークへの接続方法を学んでください。
```

### Block 27 (line 112)

```
2. *Robot Controller Connection Info* ページの上部にある *Manage* リンクをクリックして、Manageページに移動します。
```

### Block 28 (line 119)

```
3. *Download Logs* ボタンをクリックして、**Robot Controller** ログファイルをダウンロードします。
```

### Block 29 (line 126)

```
4. **Robot Controller** ログファイルがコンピューターのDownloadsディレクトリにダウンロードされたことを確認します。
```

### Block 30 (line 129)

```
5. `Notepad++ <https://notepad-plus-plus.org/>`__ やMicrosoftのWordPadなどのテキストエディタを使用して、ログファイルの内容を開いて表示します。WindowsアプリのNotepadは、ログファイルの内容を正しく表示しないことに注意してください。
```

### Block 31 (line 137)

```
Expansion Hubファームウェアの更新
```

### Block 32 (line 140)

```
**Robot Controller** スマートフォンは、USB接続を使用してスタンドアロンの**REV Robotics Expansion Hub** に接続します。**Expansion Hub** の目的は、**Robot Controller** とロボットのモーター、サーボ、センサー間の通信を容易にすることです。REV Roboticsは定期的に、**Expansion Hub** の修正と改善を含むファームウェアの新しいバージョンをリリースする場合があります。ファームウェアリリースはバイナリ（「.bin」）ファイルの形式です。
```

### Block 33 (line 142)

```
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__ ソフトウェアは、USBケーブルでコンピューターに直接接続された **Expansion Hub** のファームウェアを更新できます。
```

### Block 34 (line 144)

```
または、**Expansion Hub** がUSB経由で接続された**Robot Controller** スマートフォンに接続されたラップトップまたは**Driver Station** （**DS** ）から *Manage* インターフェースを使用できます。Manageページでは、**Expansion Hub** のファームウェアをアップロードしたり、含まれているバージョンまたはアップロードされたバージョンを使用して更新したりできます。新しいファームウェアイメージは、`REV Roboticsウェブサイト <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware#using-the-robot-controller-console>`__ から入手できます。
```

### Block 35 (line 146)

```
また、含まれているまたはアップロードされた **Expansion Hub** ファームウェアは、ペアリングされた**Driver Station** （**DS** ）アプリから**Robot Controller** の詳細設定で更新できます（以下に示します）。
```

### Block 36 (line 148)

```
これらの3つの更新方法は、RS485データワイヤを介して接続された **Expansion Hub** には適用されません。スタンドアロンの**Expansion Hub** は、直接USB接続で更新する必要があります。
```

### Block 37 (line 150)

```
Expansion Hubファームウェアを更新する手順
```

### Block 38 (line 153)

```
1. **Robot Controller** ユーザーインターフェースの *Manage* ページで、*Select Firmware* ボタンを押して、アップロードするファームウェアファイルを選択します。
```

### Block 39 (line 160)

```
   ファイルが正常に選択されると、*Upload* ボタンが表示されます。
```

### Block 40 (line 162)

```
2. *Upload* ボタンを押して、ファームウェアファイルをコンピューターから **Robot Controller** にアップロードします。
```

### Block 41 (line 169)

```
   ファイルが正常にアップロードされると、「Firmware upload complete」という言葉が表示されます。
```

### Block 42 (line 171)

```
3. **Expansion Hub** の電源がオンになっていて、新しく充電された12Vバッテリーで電源が供給されていること、および**Robot Controller** スマートフォンがUSB接続を介して**Expansion Hub** に接続されていることを確認します。更新が機能するために、**Robot Controller** はアクティブな構成ファイルに**Expansion Hub** を含める必要が** ない** ことに注意してください。
```

### Block 43 (line 178)

```
4. **Driver Station** で、右上隅の3つのドットをタッチして、ポップアップメニューを表示します。
```

### Block 44 (line 185)

```
5. ポップアップメニューから *Settings* を選択して、Settingsアクティビティを表示します。
```

### Block 45 (line 192)

```
6. **Driver Station** で、下にスクロールして、*Advanced Settings* 項目（*ROBOT CONTROLLER SETTINGS* カテゴリの下）を選択します。
```

### Block 46 (line 199)

```
7. *ADVANCED ROBOT CONTROLLER SETTINGS* アクティビティで、*Expansion Hub Firmware Update* 項目を選択します。
```

### Block 47 (line 206)

```
8. **Expansion Hub** に現在インストールされているバージョンとは異なるファームウェアファイルが正常にアップロードされた場合、**Driver Station** には現在のファームウェアバージョンと新しいファームウェアバージョンに関する情報が表示されます。*Update Expansion Hub Firmware* ボタンを押して、更新プロセスを開始します。
```

### Block 48 (line 213)

```
9. ファームウェアが更新されている間、進行状況バーが表示されます。このプロセス中に **Robot Controller**/**Expansion Hub** の電源を切らないでください。更新プロセスが完了すると、**Driver Station** にメッセージが表示されます。
```

### Block 49 (line 221)

```
Robot Controllerアプリの更新
```

### Block 50 (line 224)

```
スマートフォンにインストールされている **Robot Controller** アプリを更新する方法を知っておくことは重要です。**FIRST** は、改善と修正、およびシーズン固有のデータと機能を含む、このアプリの新しいバージョンを定期的にリリースします。
```

### Block 51 (line 226)

```
**Robot Controller** または**Driver Station** ユーザーインターフェースを通じて、**Robot Controller** アプリのバージョン番号を確認できます。**Robot Controller** または**Driver Station** で *About* メニューオプションを選択し、*ABOUT ROBOT CONTROLLER* セクションの下のApp Version番号を確認してください。
```

### Block 52 (line 233)

```
2021年現在、アプリ（v 6.1以降）はGoogle Playで入手できなくなりました。
```

### Block 53 (line 235)

```
`REV Hardware Clientソフトウェア <https://docs.revrobotics.com/rev-hardware-client/>`__ を使用すると、承認されたデバイス（**REV Control Hub**、**REV Expansion Hub**、**REV Driver Hub** 、および承認されたAndroidデバイス）にアプリをダウンロードできます。以下は、いくつかの利点です：
```

### Block 54 (line 237)

```
*  WiFi経由で **REV Control Hub** に接続します。
*  接続されたデバイス上のすべてのソフトウェアをワンクリックで更新します。
*  接続されたデバイスなしでソフトウェアアップデートを事前ダウンロードします。
*  **Control Hub** からユーザーデータをバックアップおよび復元します。
*  Androidデバイスに **DS** と**RC** アプリケーションをインストールして切り替えます。
*  **Control Hub** の**Robot Control** コンソールにアクセスします。
```

### Block 55 (line 244)

```
プログラミングに **Blocks** または**OnBot Java** を使用しているチームは、REV Hardware Clientを使用して**RC** スマートフォンの**Robot Controller** （**RC** ）アプリを更新できます。
```

### Block 56 (line 246)

```
このタスクを完了するには、デバイスごとに約7.5分かかることに注意してください。
```

### Block 57 (line 248)

```
または、アプリリリースは `FTCRobotController Github <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ で入手できます。**Robot Controller**APKファイルをコンピューターにダウンロードし、**RC** スマートフォンのDownloadsフォルダーに転送してから、そのファイルを開いて**RC** アプリをインストールします。このプロセスは「サイドローディング」と呼ばれます。
```

### Block 58 (line 254)

```
カスタムウェブカメラキャリブレーションファイルのアップロード
```

### Block 59 (line 257)

```
**Robot Controller** アプリには、一般的に利用可能なさまざまなウェブカメラ用の組み込みキャリブレーション情報があります。ユーザーは独自のカスタムキャリブレーションファイルを作成し、これらのファイルを**Control Hub** にアップロードすることもできます。
```

### Block 60 (line 259)

```
キャリブレーションファイルの内容がどのようになるべきかについての注釈付きの例は、**Android Studio** プロジェクトフォルダーに含まれている *teamwebcamcalibrations.xml* というファイルにあります。
この例のキャリブレーションファイルは `こちら <https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/TeamCode/src/main/res/xml/teamwebcamcalibrations.xml>`__ にあります。
```

### Block 61 (line 262)

```
カスタムウェブカメラキャリブレーションファイルをアップロードする手順
```

### Block 62 (line 265)

```
1. *Manage* ページで、*Select Webcam Calibration File* ボタンをクリックして、キャリブレーションファイルを選択します。
```

### Block 63 (line 272)

```
   ファイルが正常に選択されると、*Upload* ボタンが表示されます。
```

### Block 64 (line 274)

```
2. *Upload* ボタンをクリックして、選択したファイルをアップロードします。アップロードが成功した場合、*Manage* ページにアップロードが完了したことを示すメッセージが表示されます。
```


## programming_resources/shared/myblocks/annotation/annotation.rst

### Block 1 (line 1)

```
アノテーションの詳細
```

### Block 2 (line 4)

```
必須の**アノテーション**``@ExportToBlocks`` には、任意の順序でリストできるオプションのフィールドがあります。これらのフィールドにより、**myBlock** にカスタムの** コメント**、** ツールチップ**、および** パラメーターラベル** を設定できます。
```

### Block 3 (line 9)

```
コメント
```

### Block 4 (line 12)

```
-  **comment** テキストは、**Blocks** ユーザーが青い疑問符アイコンをクリックすると、バルーンに表示されます。ユーザーに**myBlock の使用方法** を伝えます。
-  「改行」なしで**単一行** で入力する必要があります。この要件は、**テキスト文字列を結合する** ことで満たすことができます。例は :ref:`こちら <programming_resources/shared/myblocks/hardware_example/hardware-example:hardware example: control a servo>` にあります。
-  青いアイコンは、カスタムコメントが指定されている場合にのみ表示されます。**Blocks** ユーザーは青いアイコンを追加および削除でき、（サイズ変更可能な）バルーン内のテキストを編集できます。
```

### Block 5 (line 16)

```
ツールチップ
```

### Block 6 (line 19)

```
-  **tooltip** は** マウスオーバー** で表示されます：マウスカーソルを画像またはアイコンの上に置くと表示されます。すべてのブロックには、** その目的を示す** 短いツールチップがあります。
-  改行なしで**単一行** で入力する必要があります。
-  カスタムツールチップが指定されていない場合、デフォルトのツールチップはメソッド、その囲んでいるクラス、および戻り値の型を示します。
-  灰色の入力ソケット（右側）の別のツールチップは、パラメータータイプに基づいて自動生成されます。
```

### Block 7 (line 24)

```
パラメーターラベル
```

### Block 8 (line 27)

```
-  **parameterLabels** テキストは**myBlock** に表示され、それぞれが灰色の入力** ソケット** の隣に表示されます。
-  複数のラベルはカンマで区切られます。ラベル間で改行を使用できます。
-  単一のパラメーターの場合、これも機能します：``parameterLabels = "sampleParameter"`` 。
```

### Block 9 (line 31)

```
Hello World の例では、パラメーターラベル **Recipient** が Java 入力パラメーター名**greetingRecipient** と同じではないことに気づいたかもしれません。これらは同じである必要はありません。1つは**Blocks** ユーザー用、もう1つは Java プログラマー用です。意味が対応するように、正しい/同じ順序でリストするだけです。
```

### Block 10 (line 33)

```
実際、すべての入力にラベルを付ける必要はありません。デフォルトのラベルは、代わりに宣言された型（String、boolean、int、double など）を表示します。いずれの場合も、各灰色のソケットには、適切なツールチップを持つ必要な型のサンプル（A、false、0 など）が含まれます。
```

### Block 11 (line 35)

```
パラメーターラベルの数が実際の Java パラメーターの数と一致しない場合、**すべての** カスタムラベルは無視されます。代わりに、デフォルトのラベルが表示されます。
```

### Block 12 (line 37)

```
**myBlock** は最大21のパラメーターを持つことができます…推奨されません！シンプルに保ちます。
```

### Block 13 (line 39)

```
繰り返しますが、アノテーション ``@ExportToBlocks`` は、オプションのフィールドを使用しない場合でも、各 **myBlock** メソッドの直前に** 必ず** 表示する必要があります。
```

### Block 14 (line 41)

```
ここでは説明されていない、さらに2つのオプションのアノテーションラベルがあります：
```

### Block 15 (line 43)

```
-  ``heading`` 、「My Amazing myBlock」など。デフォルトの見出しは「call Java method」です。
-  ``color`` 、引用符なし、色番号（色相）のみ。たとえば、155は緑、255は青です。デフォルトは289です。試してみてください！
```


## programming_resources/shared/myblocks/driving_example/driving-example.rst

### Block 1 (line 1)

```
ドライブの例
```

### Block 2 (line 4)

```
ここでは、**インチでの走行距離** ターゲットを** エンコーダーカウント** ターゲットに変換するための Java コード（メソッドのみ）を示します。変換は、ドライブモーターのローテーションあたりのカウント（CPR）とドライブホイールの直径に依存します。この例では、モーターとホイールの間のギア比が 1:1 であることを前提としています。
```

### Block 3 (line 8)

```
このメソッドは **Blocks** ユーザーから 3つの入力を受け取り、**myBlock** を** 呼び出す** 通常の Block に 1つの出力（``int`` または整数型）を** 返します** 。
```

### Block 4 (line 12)

```
典型的な使用例を以下に示します。
```

### Block 5 (line 18)

```
プログラマーとして、この例をさまざまな方法で変更できます。たとえば：
- ドライブモーターとホイール間の**ギア比** を処理する
- 2番目と3番目のパラメーターは、変更されない場合は **myBlock** に** ハードコード** できます
- これらの 2つの変数は、**myBlock ではないメソッド** で初期化し、同じ Java クラスの複数の**myBlock** メソッドで使用できます
```


## programming_resources/shared/myblocks/editing/editing.rst

### Block 1 (line 1)

```
**myBlock** の編集
```

### Block 2 (line 4)

```
**myBlock** の Java コードを編集して再ビルドする場合、**Blocks** **OpMode** でその**myBlock** を** 置き換える** 必要がある場合があります。これは、**myBlock** の表示または外部機能（アノテーションフィールド、入力パラメーター、または返される出力）を変更するかどうかによって異なります。
```

### Block 3 (line 6)

```
Java の変更が外部機能に影響する場合、更新された **myBlock** は**Blocks** の Java Classes メニューからのみ使用できます。**OpMode に既に配置されている** そのような**myBlock** は古くなっており、**Blocks 警告** が生成される可能性があります。新しい**myBlock** に置き換えてください。場合によっては、トップレベルの**Blocks** リストから**OpMode** を再度開く必要があります。
```

### Block 4 (line 10)

```
編集が **myBlock** の** 内部** 処理のみに影響する場合、「Build Everything」の後、Java Classes メニューからの新しい置き換えを必要とせずに自動的に更新される可能性があります。場合によっては、**Blocks** 画面で Save OpMode をクリックする必要さえない場合があります。**Driver Station** で INIT と Start を使用して**OpMode** を再実行するだけです。これにより、**myBlock** へのマイナーまたは内部の変更を非常に高速にテストできます。
```

### Block 5 (line 12)

```
いずれの場合も、**myBlock** 名に**myGreeting_v01** などの** バージョン** を追加することを検討してください。編集する前にコピーして貼り付けて、関連するすべての**myBlock** メソッドを** 同じ Java クラス** に保持します。**Blocks** では、一意に名前が付けられたすべてのバージョンが、その単一のクラス名の下の Java Classes メニューで使用できます。
```

### Block 6 (line 14)

```
クラス名は **MyBlocks、SampleMyBlocks、Team8604MyBlocks、DrivingMyBlocks** などのように** 短く汎用的** に保ちます。上記の簡単な例のように**myBlock** ごとに1つではなく、すべてまたは多くの関連する**myBlocks** が含まれます。
```

### Block 7 (line 16)

```
その単一のクラスでは、各 **myBlock** メソッドは独自のアノテーション ``@ExportToBlocks`` の後に表示される必要があります。そのクラスには、**myBlocks** ではない他のメソッドが含まれている場合があります。**myBlock** ではないメソッドの前にアノテーションを省略します。そのようなメソッドは、変数の初期化に使用されるか、1つ以上の**myBlocks** によって呼び出される（共有）サブメソッドである可能性があります。例は :ref:`こちら <programming_resources/shared/myblocks/method_example/method-example:example: non-myblock methods>` に示されています。
```

### Block 8 (line 18)

```
このチュートリアルでは、これまでに次の基本要件を説明しました：
- **org.firstinspires.ftc.teamcode** フォルダー/パッケージに作成/保存
- クラスは **BlocksOpModeCompanion** を** 拡張** する
- 各 **myBlock** メソッドにはアノテーション**@ExportToBlocks** が必要
- メソッドは **public** および**static** である必要があります（abstract であってはなりません）
- 外部編集後に **myBlocks** を置き換える
```

### Block 9 (line 25)

```
このチュートリアルの残りの部分では、**OnBot Java で再入力** して**Blocks でテスト** できる** 例** を示します。変更を加えて機能を追加してみてください！
```


## programming_resources/shared/myblocks/hardware_example/hardware-example.rst

### Block 1 (line 1)

```
ハードウェアの例：サーボの制御
```

### Block 2 (line 4)

```
ここでは、**myBlock** が** ロボットハードウェア** にアクセスする方法を示す非常に簡単な例を示します。ここで、**Blocks** ユーザーはサーボの名前を**myBlock** の** パラメーター** として入力します。
```

### Block 3 (line 16)

```
10-11行目には、 **「+」** 文字で結合されて**単一のテキスト文字列** を形成する2つのテキスト文字列（それぞれ引用符内）が含まれています。これは、コメントフィールドが「改行」なしで**単一行** のテキストである必要があるという要件を満たす別の方法です。短い文字列により、横にスクロールすることなく、すべてのテキストを画面上に表示できます。
```

### Block 4 (line 18)

```
15行目：このメソッドには3つの入力があり、出力はありません（キーワード **void** ）。
```

### Block 5 (line 20)

```
17行目は、**BlocksOpModeCompanion** から提供される構成されたデバイスリストである**hardwareMap** にアクセスする方法を示しています。その単一の Java 行は次のことを行います：
- myServo という新しい変数を、型（クラス）Servo として宣言します
- hardwareMap から名前付きサーボのプロパティ（メソッドと変数）を**取得** します
- それらのプロパティを新しい変数 myServo に割り当てます
```

### Block 6 (line 25)

```
20行目は **for ループ** で、`こちら <https://www.w3schools.com/java/java_for_loop.asp>`__ または `こちら <https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html>`__ で学習できます。指定された期間とサイクル数を使用して、指定されたサーボを前後に動かします。この**for ループ** には、**OpMode** が停止されていないことを監視および検証するための追加条件 ``opModeIsActive()`` があります。
```

### Block 7 (line 27)

```
22行目と24行目：オブジェクト myServo は、Servo クラスのメソッド ``setPosition()`` を使用します。
```

### Block 8 (line 29)

```
23行目と25行目：オブジェクト linearOpMode は、**BlocksOpModeCompanion** から継承されたクラスのメソッド ``sleep()`` を使用します。
```

### Block 9 (line 31)

```
**Blocks** ユーザーは、** アクティブな構成** から正確なデバイス名を入力する必要があります。ハードウェアデバイス名（モーター、サーボ、センサー）は、RC アプリまたはペアリングされた DS アプリの Configure Robot メニューにあります。または、これらのデバイスタイプを含む任意の**Blocks** ドロップダウンリストから名前を再入力する方が簡単な場合があります。たとえば、緑色の Servo**Set** ブロックのドロップダウンリストです。
```

### Block 10 (line 35)

```
このサンプル myBlock は、**Blocks** メニューの Java Classes をクリックし、次に SampleMyBlocks サブメニューをクリックして見つけることができます。
```

### Block 11 (line 37)

```
注：**OnBot Java** でのタイプミスやその他のエラーにより、Java Classes メニューに myBlock が表示されない場合があります。これは、**Blocks** の**Settings** メニューオプション Advanced > Developer Options を有効にすることで修正できます。次に、Browser Console から診断情報を読み取ります（以下のリンクを参照）。
```

### Block 12 (line 39)

```
詳細については、**Blocks** `Programming
Tutorial <https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Writing-an-Op-Mode-with-FTC-Blocks>`__ で、「ステップ12：Java クラスに属するブロック」を参照してください。
```

### Block 13 (line 42)

```
ここに Blocks OpMode 全体があります。**Blocks** エディターの Java Classes タブに myBlock を配置できます。
```

### Block 14 (line 48)

```
**次の例に進む前に** 、ここでコードを**OnBot Java** に入力し、**Blocks** でテストしてください。正常に動作するようになったら、**Blocks** の OpMode を保存し、上記のバージョンを簡単に復元できるように、わかりやすい名前を付けます。
```


## programming_resources/shared/myblocks/ideas/ideas.rst

### Block 1 (line 1)

```
その他の **myBlocks** のアイデア
```

### Block 2 (line 4)

```
**MyBlocks** は、創造性とロボットの機能に大きな可能性を提供します。既存の**Blocks** グループができるタスクのために**myBlocks** をプログラムすることから始めます。後で、通常の**Blocks** では** 利用できない** 機能を追加します。以下は、両方の例です：
```

### Block 3 (line 6)

```
-  INIT 中に、**ゲームパッドを使用して**1つ以上のプログラム変数を設定します。これは通常の**Blocks** で実行できますが、優れたユーザーインターフェイス（UI）には複数の長く複雑な関数が必要です。
```

### Block 4 (line 8)

```
-  **複数のセンサー制御** を使用してドライブアクションを作成します。たとえば、距離ゴール（超音波またはビジョンターゲット）に向かうジャイロベースのステアリング。または、ラインに沿って Run_To_Position を実行します。**myBlock** は、以前は複雑すぎると考えられていた制御を**Blocks** ユーザーに提供できます。
```

### Block 5 (line 10)

```
-  **外部ライブラリ** へのアクセスを提供します（**SDK** 7.0 の新機能）。詳細は :ref:`こちら <programming_resources/shared/external_libraries_blocks/external-libraries-blocks:external libraries in onbot java and blocks>` を参照してください。
```

### Block 6 (line 12)

```
-  上記の例の1つは、**Blocks** ユーザーによって指定されたサーボを制御します。これは、1つのデバイス、2つのデバイスなどと対話する** 個別の myBlocks のファミリー** につながる可能性があります。または、汎用の単一**myBlock** が、たとえば最大4つの DC モーターと対話できます。Java メソッドは、パラメーター名が入力されている DC モーターのみを処理します。
```

### Block 7 (line 14)

```
-  RC スマートフォンの **LED フラッシュライト** を制御しますか？
```

### Block 8 (line 16)

```
-  **telemetry.speak** にブール値 ``AndroidTextToSpeech.isSpeaking()`` に相当する**myBlock** はありますか？
```

### Block 9 (line 18)

```
アイデアをお探しですか？**SDK** のトップレベル API ドキュメントは `こちら <https://javadoc.io/doc/org.firstinspires.ftc>`__ です。**RobotCore** をクリックすると、左側のメニューに一般的に使用される多くのクラスが表示され、他のセクションも確認できます。
```

### Block 10 (line 20)

```
   提案または共有する良い例がありますか？westsiderobotics@verizon.net に送信してください。
```

### Block 11 (line 22)

```
開発者 Liz Looney からの効率に関するヒントは次のとおりです：
```

### Block 12 (line 24)

```
-  メソッド呼び出しの数を制限します。5つのタスクを実行する単一の **myBlock** を呼び出すと、それぞれ1つのタスクを実行する5つの**myBlocks** を呼び出すよりもオーバーヘッドが少なくなります。
```

### Block 13 (line 26)

```
-  パラメーターの数を制限します。**myBlock** が**OpMode** 中に変更されない特定の情報を必要とする場合は、**OpMode** の開始時に1回呼び出される** 初期化メソッド** を使用します。初期化メソッドはその情報を保存し、**myBlock** が呼び出されるたびに同じパラメーターを繰り返し渡すことを回避します。
```


## programming_resources/shared/myblocks/index.rst

### Block 1 (line 1)

```
カスタムブロック（**myBlocks** ）
```

### Block 2 (line 21)

```
この重要な開発を行った Google エンジニアの `Liz Looney <https://github.com/lizlooney>`__ さんに敬意を表します！
```

### Block 3 (line 25)

```
質問、コメント、修正は westsiderobotics@verizon.net までお願いします。
```


## programming_resources/shared/myblocks/intro/intro.rst

### Block 1 (line 1)

```
はじめに
```

### Block 2 (line 4)

```
このチュートリアルでは、通常の **Blocks** プログラムで使用する** カスタムブロック** の作成方法を示します。これらの** 「myBlocks」** は、**OnBot Java** または**Android Studio** を使用して Java でプログラムされます。
```

### Block 3 (line 9)

```
    :alt: サンプル myBlock、void を返す
```

### Block 4 (line 11)

```
    サンプル myBlock：サーボを操作、値を返さない
```

### Block 5 (line 14)

```
**myBlock** は、以前はすべて Java コードを使用するチームのみが利用できた** 高度な機能** を追加できます。または、単一の**myBlock** は、以前は多くの通常の Blocks が必要だったロボット命令を含む** 「スーパー関数」** として機能できます。これで、チームの**Blocks** コードがより強力で、よりシンプルになります！
```

### Block 6 (line 20)

```
    :alt: サンプル myBlock、エンコーダーカウントを返す
```

### Block 7 (line 22)

```
    サンプル myBlock：入力に基づいてエンコーダーターゲット値を返す
```

### Block 8 (line 24)

```
また、**myBlocks** プログラミングにより、一部のチームメンバーが Java の学習と使用を開始し、貴重な新機能に貢献できるようになります。他のチームメンバーは**Blocks** での学習と作業を続け、チームの公式コードを作成できます。誰も足を引っ張られたり、取り残されたりすることはありません。
```

### Block 9 (line 26)

```
この重要な開発を行った Google エンジニアの `Liz Looney <https://github.com/lizlooney>`__ さんに敬意を表します！
```

### Block 10 (line 28)

```
Java に関する注意事項
```

### Block 11 (line 31)

```
-  このチュートリアルでは、**Control Hub** または**Robot Controller (RC)** スマートフォン上で実行されるプログラミングツールである :ref:`OnBot Java <programming_resources/onbot_java/onbot-java-tutorial:onbot java programming tutorial>` を使用して**myBlocks** を作成します。すでに :ref:`Android Studio <programming_resources/android_studio_java/android-studio-tutorial:android studio programming tutorial>` を使用している学生は、同じプログラミングを簡単に実行できます。
-  このチュートリアルでは、基本的な **myBlocks** に必要な最小限を超えて、`Java <https://en.wikipedia.org/wiki/Java_(programming_language)>`__ または**OnBot Java (OBJ)** を教えることはありません。
```


## programming_resources/shared/myblocks/method_example/method-example.rst

### Block 1 (line 1)

```
例：**myBlock** ではないメソッド
```

### Block 2 (line 4)

```
Java クラスには、**myBlocks** ではないメソッドも含めることができます。複数の**myBlocks** が共有の内部プロセスまたは計算を実行する場合は、これを検討してください。これは**myBlocks** に特有ではなく、一般的に優れたプログラミング手法です。
```

### Block 3 (line 6)

```
これを説明するために、上記のドライブの例を考えてみましょう。**2つ** の異なるロボットをサポートする**myBlocks** を作成したいと想像してください。
- ロボット A には **AndyMark** **NeveRest 40** モーター付きの**4インチ** ドライブホイールがあります。
- ロボット B には **NeveRest** **Orbital 20** モーター付きの**3インチ** ドライブホイールがあります。
- **Blocks** プログラミングチームメイトにとって、**myBlocks** が** 非常にシンプル** であることを望みます。
```

### Block 4 (line 11)

```
解決策：
- ロボットごとに1つの **MyBlock** 。
- 各 **Blocks** ユーザーは、インチ単位で走行距離のみを指定する必要があります。
- 各 **myBlock** は、適切なホイールサイズとモーターエンコーダー CPR を使用します。
- **myBlocks** は、距離をエンコーダーカウントに変換する「ユーティリティ」メソッドを共有します。
```

### Block 5 (line 19)

```
34行目は、**myBlock** で** ない** 共有メソッドを示しています。アノテーション @ExportToBlocks を単に省略します。キーワード ``private`` は、メソッドが同じクラス内からのみ呼び出すことができることを意味します。可能な限りこれを使用してください。
```

### Block 6 (line 21)

```
17行目と29行目は共有メソッドを呼び出します。メソッド呼び出しは3つのパラメーターを提供しますが、これらは「ユーティリティ」メソッドの入力パラメーターと同じ**名前** を持っていません - しかし、それらの型は一致する必要があります。
```

### Block 7 (line 23)

```
38行目では、**(int)** が10進数を整数型に変換、または** キャスト** します。これは** 型キャスト** と呼ばれます。プログラマーは互換性のあるデータ型に細心の注意を払う必要があります。たとえば、DC モーター ``set .TargetPosition`` ブロックには、10進数ではなく、単純な整数としてエンコーダー値を指定する必要があります。
```

### Block 8 (line 25)

```
15行目などでは、キーワード ``final`` は Java **定数** を示します：値を変更できない変数。Java 定数は伝統的にすべて大文字です。このプログラムで Math 定数を見つけることができますか？
```

### Block 9 (line 27)

```
ロボット A とロボット B の **myBlocks** は次のとおりで、それぞれに** コメント** バルーンと** ツールチップ** があります。あなたが望んだように、非常にシンプルです！
```


## programming_resources/shared/myblocks/parameter/parameter.rst

### Block 1 (line 1)

```
パラメータータイプの詳細
```

### Block 2 (line 4)

```
次の **myBlock** の例は入力または実行しないでください。そのダミー入力は、単にさまざまな** パラメータータイプ** を示しています。この**myBlock** はロボットのバッテリー電圧を正しく読み取りますが、**Blocks** は現在、**Sensors** メニューに**VoltageSensor** ブロックを提供しています。
```

### Block 3 (line 7)

```
   :alt: バッテリー電圧
```

### Block 4 (line 11)

```
Java **パラメーター** ``uno``、``parola``、``verita`` には**myBlock ラベル**``One``、``Word``、``Truth`` があることに注意してください。これらは異なっていても構いません。
```

### Block 5 (line 13)

```
**comment** フィールドは、この**myBlock** を**Blocks** ユーザーに説明します。ユーザーはコメントを編集または削除できます。ここでの表示のみのために、このサンプルテキストは複数行に表示されます。通常は、単一行のテキストとして、または結合された引用符として入力する必要があります（例は :ref:`こちら <programming_resources/shared/myblocks/hardware_example/hardware-example:hardware example: control a servo>`）。
```

### Block 6 (line 15)

```
**myBlock** の**tooltip** は簡潔である必要があります。注：4つのツールチップはすべて同時に表示されるわけではありません。それぞれがマウスオーバーで表示されます。1つはカスタム、3つは入力タイプに基づいて自動生成されます。
```

### Block 7 (line 17)

```
各入力ソケットには、対応するツールチップを持つパラメータータイプのデフォルト値が表示されます。メソッドシグネチャに示されているように、パラメーター ``uno`` は Java タイプ``double`` （数値）、``parola`` はタイプ``String`` （テキスト）、``verita`` はタイプ``boolean`` （true または false）です。
```

### Block 8 (line 19)

```
   プログラミングのヒント：プリミティブ型とは異なり、String は ``==`` ではなく``Object.equals()`` で比較する必要があります。これは、**text** パラメーターが実際には String クラスのオブジェクトまたはインスタンスであり、``==``、``>``、``<`` などの基本的な Java 演算子と同等の独自のメソッドを持っているためです。
```

### Block 9 (line 23)

```
   プログラミングのヒント：この例では、変数 ``batteryVoltage`` はメソッドの**外部** で宣言および初期化されているため、このクラスの他のメソッドでも使用できます。
```

### Block 10 (line 25)

```
**パラメータータイプ** に関するいくつかの最終的な注意事項：
- **myBlock** メソッドが ``boolean`` または``java.lang.Boolean`` として宣言されたパラメーターを使用する場合、**myBlock** の入力ソケットはブール値を返す（提供する）任意のブロックを受け入れます。
- ``float``、``java.lang.Float``、``double``、または``java.lang.Double`` として宣言されたメソッドパラメーターの場合、**myBlock** は数値を返す任意の入力ブロックを受け入れます。
- ``byte``、``java.lang.Byte``、``short``、``java.lang.Short``、``int``、``java.lang.Integer``、``long``、または``java.lang.Long`` として宣言されたメソッドパラメーターの場合、**myBlock** は数値を返す任意の入力ブロックを受け入れ、その値を最も近い整数に丸めます。
- **myBlock** メソッドが**1つのテキスト文字** のみを持つパラメーターを使用する場合、タイプ ``String`` の代わりにタイプ``char`` または``java.lang.Character`` を使用できます。その場合、**myBlock** の入力ソケットはテキストを返す任意のブロックを受け入れ、テキスト文字列の** 最初の文字のみ** を使用します。
```


## programming_resources/shared/myblocks/rw_example/rw-example.rst

### Block 1 (line 1)

```
例：ファイルの読み書きアクセス
```

### Block 2 (line 4)

```
通常の **Blocks** の現在のバージョン（**SDK**7.0）では、自動ログまたはマッチログファイルエントリ以外に、** 外部ファイルへの読み書きアクセス** を提供していません。ファイルアクセスは有用な機能であり、これまでのところ Java プログラマーのみが利用できます。**myBlocks** を使用すれば可能です！
```

### Block 3 (line 6)

```
ここでは、**myBlocks** のペアの例を示します。1つの**myBlock** は数値を指定されたファイル名に** 書き込み**、コンパニオン**myBlock** は後でその値を同じファイルから** 読み取る** ことができます。
```

### Block 4 (line 10)

```
ファイルは **Control Hub** または RC スマートフォンの FIRST/settings フォルダーに保存されます。RC アプリ、**OpModes** 、およびその他のファイルとは別に存在します。
```

### Block 5 (line 12)

```
書き込みおよび読み取りアクションは、同じ **OpMode** または** 異なる OpModes** で発生でき、さまざまなシナリオが可能です：
```

### Block 6 (line 14)

```
-  **Autonomous** が**TeleOp** に情報を渡します。たとえば、センサーまたはエンコーダーの最新の値は何でしたか？
```

### Block 7 (line 16)

```
-  特別な**セットアップ OpMode** により、ゲームパッド入力で自律戦略を選択し、重要なパラメーターを調整できます。ロボットはその後長時間アイドル状態になり、電源がオフになる可能性もあります。試合が始まると、**Autonomous** **OpMode** はそれらの設定を読み取り、選択/調整されたアクションを実装します。
```

### Block 8 (line 18)

```
-  **専用ログファイル** は、オプションのタイムスタンプを使用して、カスタム形式で主要なセンサーデータを報告します。プログラム開発とデバッグの場合、これは大規模な標準ログまたはマッチログを操作するよりも効率的です。
```

### Block 9 (line 20)

```
この例の Java コードは、いくつかの馴染みのない Java 式を説明する**広範なコメント** とともに、以下で入手できます。コードは**OnBot Java** または**Android Studio** に直接コピーして貼り付けることができます。
```

### Block 10 (line 22)

```
   プログラミングのヒント：可能なすべての Java コマンドを暗記する代わりに、プログラマーは類似のタスクの既存のコードを研究および変更することがよくあります。馴染みのないコマンドは、インターネット検索、参考書、`Javadoc リファレンス <https://javadoc.io/doc/org.firstinspires.ftc>`__、または公式の `Oracle Javadoc <https://docs.oracle.com/javase/7/docs/api/>`__ で調べられます。
```

### Block 11 (line 24)

```
この簡単な例では、ファイル名ごとに単一の数値のみをサポートしています。より良いバージョンでは、複数の値とデータ型が可能になります - 優れたプログラミングの課題です！
```

### Block 12 (line 26)

```
**ループ内に myBlocks を配置する** ことに注意してください。現在の例を拡張すると、**myBlock** はファイルから大量の（変更されない）データを読み取る可能性があります。**OpMode** がそのデータを一度だけ必要とする場合、ループ内でファイルを読み取ると、サイクル時間が無駄に追加され、破損または中断された読み取り操作のリスクが高まる可能性があります。
```

### Block 13 (line 30)

```
代わりに、ファイルを一度読み取り、関連するデータを変数または配列に保存します。次に、ループ内で必要に応じて変数を処理します。
```

### Block 14 (line 34)

```
データが変化せず、一度だけ必要な場合、同じ提案がセンサーとエンコーダーの読み取りにも適用される可能性があります。
```


## programming_resources/shared/myblocks/simple_example/simple-example.rst

### Block 1 (line 1)

```
シンプルな例：**myGreeting** の作成
```

### Block 2 (line 4)

```
「Hello World」（もちろん！）という挨拶を作成するシンプルな **myBlock** から始めます。
```

### Block 3 (line 6)

```
Wi-Fi 経由で **Control Hub** または RC スマートフォンに接続された Chrome ブラウザーを開きます。アドレス**http://192.168.43.1:8080** （CH）または**http://192.168.49.1:8080** （RC）にアクセスし、**OnBot Java** タブをクリックします。
```

### Block 4 (line 10)

```
大きな**プラス記号アイコン** をクリックして新しいファイルを開きます。**SampleMyBlocks.java** と呼びます。デフォルトの「teamcode」フォルダーの場所を使用します。Sample OpMode を選択せず、デフォルト設定の「Not an OpMode」を使用します。OK をクリックします。
```

### Block 5 (line 14)

```
作業領域にシンプル/空の Java プログラムが表示されます。
```

### Block 6 (line 18)

```
1行目はデフォルトのストレージフォルダー「teamcode」を示し、4行目は**クラス名** を示します（ファイル名と同じ）。これは ``public`` なので、他のクラスがアクセスできます。4行目の**左中括弧** と7行目の**右中括弧** に注意してください。すべてのコードをこれらの中括弧の間に配置します。
```

### Block 7 (line 20)

```
2つの順スラッシュマーク **//** は** コメント行** を示し、すべて Java ソフトウェアによって無視されます。優れたプログラマーは、チームメイトや** 将来の自分** とコミュニケーションをとるために、多くのコメントを使用します！プログラムのすべての細部を覚えているわけではありません…大量にコメントを付けたことに後で感謝するでしょう！
```

### Block 8 (line 22)

```
   プログラミングに関する注意：**class** は、**objects** （クラスの例または** インスタンス** ）で使用できる** メソッド** （アクション）と** フィールド** （プロパティ）を記述します。「dogs」というクラスには、メソッド「run」と「sleep」、およびフィールド「friendliness」と「appetite」が含まれる場合があります。ペットの Spot と Rover は、「dogs」クラスのオブジェクトまたはインスタンスです。
```

### Block 9 (line 24)

```
クラス名の後に、``extends BlocksOpModeCompanion`` と入力します。これは、新しいクラスを、より高い**スーパークラス** または**親** の**サブクラス** または**子** として宣言します。親クラス**BlocksOpModeCompanion** には、新しいサブクラスによって** 継承** される便利なツールが含まれています。
```

### Block 10 (line 28)

```
その行を入力すると、OBJ ソフトウェアは**自動的** に ``import`` 文を作成し、親クラスを使用可能にします。便利です！
```

### Block 11 (line 30)

```
   プログラミングに関する注意：**BlocksOpModeCompanion** から継承されたクラスには、**OpMode**、**LinearOpMode**、**Telemetry**、**HardwareMap**、および**Gamepad** が含まれます。すべて非常に便利です！**myBlock** メソッドは、これらのクラスの** オブジェクト** または** インスタンス** を宣言せずに直接使用できます。以下に例を示します。
```

### Block 12 (line 32)

```
中括弧内に、次のように新しい行を入力します：
```

### Block 13 (line 42)

```
これらは、新しい **myBlock** に表示されるオプションのラベルです。以下で説明します。これらの機能のいずれも使用したくない場合でも、** アノテーション** 行 ``@ExportToBlocks`` は必要です。
```

### Block 14 (line 44)

```
そのアノテーションを入力すると、OBJ は自動的に ``import`` 文を追加しました。
```

### Block 15 (line 46)

```
これで、メソッド、つまり最初の **myBlock** を作成する準備が整いました。次の行を入力します：
```

### Block 16 (line 54)

```
メソッドの名前は ``myGreeting`` です。これは``public`` メソッドなので、他のクラスから使用または**呼び出す** ことができます。そして、これは``static`` メソッドで、すべての**myBlock** メソッドに必要です。
```

### Block 17 (line 56)

```
このメソッドには、1つの入力または**パラメーター** があり、タイプは ``String`` （テキスト）で、名前は``greetingRecipient`` です。これは、挨拶の対象者または対象グループです。
```

### Block 18 (line 58)

```
メソッドには、1つの出力または**戻り値** もあります。タイプは ``String`` （テキスト）です。出力値は、``return`` コマンドで記述されているように、文字「Hello」、続いてスペース、続いて入力されたパラメーター、続いて感嘆符です。
```

### Block 19 (line 60)

```
プログラムで、キーワード ``return`` が最初の文字位置にあることに注意してください。このサンプルではインデント（タブ）が使用されており、複数のレベルの中括弧がある場合にコードを読みやすくします。
```

### Block 20 (line 62)

```
また、プラス記号 ``+`` が3つのテキスト要素を結合または**連結** して、単一の``String`` を形成していることにも注意してください。
```

### Block 21 (line 64)

```
**コードは完成しました！** 全体は次のようになります：
```

### Block 22 (line 68)

```
左上隅の Build Everything ボタンをクリックします。
```

### Block 23 (line 72)

```
正常にビルドされるはずです。エラーがある場合は、上記のコードとまったく同じようにタイプミスがないか注意深く確認してください。大文字と小文字を区別し、引用符、セミコロン、中括弧を区別します。
```

### Block 24 (line 74)

```
正常にビルドされたら、**OnBot Java** から Chrome ブラウザーの**Blocks** タブに移動します。**Create New Op Mode** を選択するか、既存の OpMode を開いて編集します。
```

### Block 25 (line 76)

```
左側のメニューツールボックスで、**Java Classes** タブを選択します。
```

### Block 26 (line 80)

```
**SampleMyBlocks** サブメニューをクリックすると、新しい**myBlock** が表示されます！
```

### Block 27 (line 84)

```
**myBlock** を作業領域にドラッグすると、入力ソケットにカーソルを合わせると、** ツールチップ** 「Greet a person or group.」が表示されます。
```

### Block 28 (line 88)

```
青い疑問符アイコンをクリックすると、 **コメント** 「Here is a greeting for you.」が表示されます。
```

### Block 29 (line 92)

```
カスタムラベル「Recipient」が、灰色の入力ソケットの左側に表示されます。これらのオプション機能はすべて、Java コードのアノテーション ``@ExportToBlocks`` から取得されます。
```

### Block 30 (line 94)

```
ここで、このシンプルな **myBlock** の動作を確認するために、2つのコマンドで**Blocks** プログラムを作成できます：
```

### Block 31 (line 98)

```
任意のテキストを入力できます。ボタン ``ABC`` をクリックして、それを入力します。この例では「World」を使用しています。
```

### Block 32 (line 100)

```
OpMode を保存して実行すると、**Driver Station** に挨拶が表示されます！
```

### Block 33 (line 102)

```
**おめでとうございます - 最初の myBlock が完成しました！**
```

### Block 34 (line 113)

```
次の例では、上記の Java クラスにより多くの **myBlock** メソッドを追加します。それらは、ここで作成した SampleMyBlocks.java ファイルを編集して追加されます。
```


## programming_resources/shared/myblocks/summary/summary.rst

### Block 1 (line 1)

```
まとめ：**myBlocks** の利点
```

### Block 2 (line 4)

```
1. **myBlocks** により、ソフトウェア開発キット（**SDK** ）の Java の全機能にアクセスできるようになりました。**Blocks** プログラミングで、**Blocks** のみのチームには** 以前は利用できなかった** タスクを実行できるようになりました。これには :ref:`外部ライブラリ <programming_resources/shared/external_libraries_blocks/external-libraries-blocks:external libraries in onbot java and blocks>` が含まれます。
```

### Block 3 (line 6)

```
2. **myBlocks** は、以前は**Blocks** で** 長く複雑だった関数** をきちんとパッケージ化できます。
```

### Block 4 (line 8)

```
3. **myBlocks** プログラミングにより、一部のチームメンバーが Java の学習と使用を開始し、貴重な新機能に貢献できるようになります。他のチームメンバーは**Blocks** での学習と作業を続け、チームの公式コードを作成できます。誰も足を引っ張られたり、取り残されたりすることはありません。
```

### Block 5 (line 10)

```
4. **myBlocks** は、RC スマートフォンまたは**Control Hub** 上で実行される**OnBot Java** で作成できます。ビルドとテストは非常に高速です。多くのチームは、学校のコンピューターでソフトウェアのインストールが禁止されているなどの理由で、**Android Studio** に簡単にアクセスできません。
```

### Block 6 (line 12)

```
5. **myBlocks** を開発および共有することで、経験豊富なチームは、単に Java ライブラリへのリンクを投稿する以上に、** 新しいチームを支援** できます。**FIRST** **Tech Challenge** コミュニティは、最終的には、テスト済みで十分に文書化された**myBlocks** の厳選されたリポジトリから恩恵を受ける可能性があります。おそらく「**Blocks Store**」でしょうか？
```


## programming_resources/shared/myblocks/telem_example/telem-example.rst

### Block 1 (line 1)

```
例：**Telemetry** 設定の変更
```

### Block 2 (line 4)

```
**Telemetry** メッセージは、デフォルトでは**Robot Controller** から**Driver Station** に** 毎秒最大4回** 送信されます。この最大更新レートは**Android Studio** または**OnBot Java** で変更できますが、通常の**Blocks** では変更** できません**。**myBlock** を使用すれば、この機能も提供できます！
```

### Block 3 (line 6)

```
この簡単な例では、**Blocks** ユーザーが標準の時間間隔を 250 ミリ秒から他の間隔に変更できます。
```

### Block 4 (line 10)

```
時間間隔を短くすると、センサーまたはエンコーダーデータの更新を高速化できます。間隔を長くすると、RC-DS 通信帯域幅の負荷を軽減できます。
```

### Block 5 (line 12)

```
メソッドのみの Java コードは次のとおりです：
```

### Block 6 (line 26)

```
これが実際に機能することを確認したいですか？別の、やや高度な **myBlock** により、**Telemetry** 更新間の時間を測定できます。以下に投稿されています。その**myBlock** は、以下に添付されているような**Blocks** プログラムで使用できます。生の**.blk ファイル** をダウンロードし、メインの**Blocks** メニューで**Upload Op Mode** ボタンをクリックしてください。すべてのコメントと指示をお読みください。
```


## programming_resources/shared/myblocks/timer_example/timer-example.rst

### Block 1 (line 1)

```
タイマーの例
```

### Block 2 (line 4)

```
FTC **タイマー** は、馴染みのある ``.sleep`` ブロックよりもはるかに多くの機能を提供します。Java プログラマーは、`この Blocks チュートリアル <https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Timers-in-FTC-Blocks>`__ からタイマーについて学ぶことができます。そのレッスンは Java プログラムに簡単に適用できます。
```

### Block 3 (line 6)

```
**myBlocks** を作成する際、既存の Java コードのセクションを**myBlock** メソッドに変換または「パッケージ化」するときは注意してください。プログラマーとして、**myBlock** が**OpMode** のどこに配置されるかを検討する必要があります。たとえば、**myBlock** が**repeat while ループ** 内に配置されている場合、Java メソッドは何度も呼び出されます - これは意図したものである場合とそうでない場合があります。**Blocks** ユーザーに、ループを含む（または含まない）**myBlock** の実行方法を伝えるために、アノテーション**comment** を使用します。
```

### Block 4 (line 8)

```
タイマーに関する特別な注意：新しい FTC タイマーを作成または**インスタンス化** すると、そのタイマーも開始または**リセット** されます。**Blocks** の**repeat ループ** で使用される**myBlock** 内でタイマーが作成されると、そのタイマーは常にリセットされ、意図した時間制限に到達することはありません。
```

### Block 5 (line 10)

```
次の例では、 **タイマーの作成** タスクを**タイマーのリセット** タスクから分離しています。
```

### Block 6 (line 14)

```
15行目：この単一の Java 行は、次のすべてを実行します：
- myStopwatch というフィールドを、型（クラス）ElapsedTime として宣言します
- フィールドは **private** で、このクラス SampleMyBlocks でのみ使用できます
- フィールドは **static** で、**myBlocks** などの static メソッドで使用できます
- **コンストラクター** メソッド ElapsedTime() を呼び出して、**新しい** ElapsedTime インスタンスを**インスタンス化** します
- その**インスタンス** をフィールド myStopwatch に割り当てます
```

### Block 7 (line 21)

```
18-19行目は、 **「+」** 文字で結合されて**単一のテキスト文字列** を形成する2つのテキスト文字列（それぞれ引用符内）を再度示しています。これは、コメントフィールドが「改行」なしで**単一行** のテキストである必要があるという要件を満たす別の方法です。
```

### Block 8 (line 23)

```
22行目：このメソッドには**入力がありません** （空の括弧）と**出力がありません** （キーワード**void** ）。これが、アノテーション @ExportToBlocks に**parameterLabels** フィールドがなかった理由です。
```

### Block 9 (line 25)

```
24行目では、パーセント記号で示される**フォーマットコード** を使用してデータが表示されます。**.2f** は、小数点の右側に2桁の数値を表示します。
```

### Block 10 (line 27)

```
また、24行目では、オブジェクト myStopwatch がメソッド ``time()`` を使用して、そのタイマーの現在の値を秒単位で取得します。
```

### Block 11 (line 29)

```
28行目：二重ストローク演算子 **\|\|** は「OR」を意味します。他の Java 論理演算子は `こちら <https://www.w3schools.com/java/java_operators.asp>`__ にあります。
```

### Block 12 (line 31)

```
ブール値「true」または「false」の出力、つまり**戻り値の型** に注意してください。このメソッドの場合、タイマーが指定された時間に達したときに、**return** コマンドは値「true」を**Blocks** プログラムに渡します。それ以外の場合は「false」を渡します。
```

### Block 13 (line 33)

```
このようなブール値の出力を持つ **myBlock** は、``.repeat while`` や``.if/then`` などの**Blocks** 制御構造で使用できます。
```

### Block 14 (line 37)

```
上記の最初の **Blocks** 関数では、myStopwatch 変数を作成して開始します。再度停止するまで、タイマーは実行され続けます。
```

### Block 15 (line 39)

```
次の関数は、タイマーが 5.5秒に達するまで、ループを繰り返し実行します。その時点で、関数からのブール値出力により、繰り返しループが停止します。この例では、ループは空です。実際のアプリケーションでは、ループにはロボットアクションが含まれます。
```

### Block 16 (line 50)

```
必要に応じて、リセット機能を備えた3番目の **myBlock** を追加できます。これにより、**Blocks** ユーザーは、OpMode 中にタイマーを再度ゼロにすることができます。これは、``.reset()`` メソッドで簡単に行えます。
```


## programming_resources/shared/phone_pairing/phone-pairing.rst

### Block 1 (line 1)

```
スマートフォンのペアリング
```

### Block 2 (line 4)

```
はじめに
```

### Block 3 (line 7)

```
**Robot Controller** および**Driver Station** アプリは、** すべてのモデルの合法的なスマートフォン** 間を含め、ペアリングにおいて非常に信頼性があります。**FIRST** **Tech Challenge** イベントで現在使用が合法的なスマートフォンモデルのリストについては、`Competition Manual <https://ftc-resources.firstinspires.org/ftc/game/manual>`__ を参照してください。
```

### Block 4 (line 9)

```
Android スマートフォンが適切に準備されている場合、Wi-Fi Direct 経由のペアリングは**高速** で、通常は**自動** です。ここでは、ペアリングを妨げる可能性のあるさまざまな**既存の条件** に対処する手順を示します。
```

### Block 5 (line 11)

```
この記事では、**REV Control Hub** または**REV Driver Hub** については説明していません。
```

### Block 6 (line 13)

```
スマートフォンのクリーンアップと準備
```

### Block 7 (line 16)

```
1. RC スマートフォン：必要に応じて、Settings/Accounts/Google/select/3 dots/Remove account/confirm を選択します。他のアカウントについても繰り返します。また、バックグラウンドで実行されたり、更新を試みたりする可能性のある、**FIRST** **Tech Challenge** 以外のアプリ/ゲームを削除します。
```

### Block 8 (line 18)

```
2. RC スマートフォン：RC アプリを含むすべてのアプリを強制終了（スワイプして削除）します。
```

### Block 9 (line 20)

```
3. RC スマートフォン、Apps/Settings/Wi-Fi。保存されているネットワークを手動で選択して忘れます。
```

### Block 10 (line 22)

```
4. RC スマートフォン、まだ WiFi メニュー内：Wi-Fi Direct メニューに移動します（More Settings または Advanced 経由）。
```

### Block 11 (line 24)

```
-  Peer Devices との接続を選択して忘れる/切断します。これには現在のスマートフォンのペアリングが含まれます。これには数回の試行が必要な場合があります。切断が確認されない場合は、あきらめても問題ありません。
```

### Block 12 (line 26)

```
   -  最上部の項目に「Created Group」と表示されている場合は、切断します。
   -  誤って他のスマートフォンで招待ポップアップを作成した場合は、他のスマートフォンで Decline し、このスマートフォンで Cancel します。まれに、招待プロンプトが RC スマートフォンの開いているウィンドウの下にある場合があります。
   -  ペアリングは後でアプリで行われます。以下を参照してください。
```

### Block 13 (line 30)

```
-  ANY スマートフォンのペアリングを含むすべての Remembered Groups を選択して忘れます。（これは、いずれかのアプリから Advanced RC Settings から実行することもできます。）ステップ d1 と d2 の後の目標：「Not visible」、「Peer devices」なし、「Remembered groups」なし。
```

### Block 14 (line 32)

```
-  必要に応じて、`Competition Manual <https://ftc-resources.firstinspires.org/ftc/game/manual>`__ に従って、スマートフォンを合法的な名前に Rename/Configure します（これは、各アプリの Settings から実行することもできます。）
```

### Block 15 (line 34)

```
-  Configure device/Limit 2 devices、「Inactivity timeout」Never、チェックボックス「Auto connect remembered groups」。（注：timeout は永続的ではないため、時々再確認してください。）
```

### Block 16 (line 36)

```
5. デバイスのホーム画面に強制終了します。上から2回スワイプして、次の順序で実行します：
```

### Block 17 (line 39)

```
-  **Wi-Fi ON** （通常、**Airplane Mode** がオンになると切り替わります）、次に Done
```

### Block 18 (line 41)

```
-  Location OFF、Android 7.x のみ
```

### Block 19 (line 43)

```
6. DS スマートフォンで上記の手順を繰り返します。
```

### Block 20 (line 46)

```
ペアリング
```

### Block 21 (line 49)

```
1. RC スマートフォン：現在のシーズンの RC アプリを開きます。Self Inspect で RC の問題を確認します。
```

### Block 22 (line 51)

```
2. DS スマートフォン：現在のシーズンの DS アプリを開きます。Self Inspect で DS の問題を確認します。
```

### Block 23 (line 53)

```
3. DS スマートフォン：Menu（3つのドット）/Settings。「Pairing Method」が Wi-Fi Direct であることを確認します。「Pair with Robot Controller」を開きます。（スマートフォン/Android メニューを使用してペアリングしないでください。）
```

### Block 24 (line 55)

```
4. フィルターはオンのままにして、アプリが一致するデバイスを見つけるまで辛抱強く待ちます。または、フィルターをオフにして数秒以内にすべてのデバイスを表示します。対応する RC スマートフォンを選択し、Back をタッチし、もう一度 Back をタッチして DS ホーム画面に戻ります。
```

### Block 25 (line 57)

```
5. RC スマートフォンを見て、そこで招待を受け入れます。まれに、招待プロンプトが RC スマートフォンの開いているウィンドウの下にある場合があります。ペアリングは数秒以内に行われます。
```

### Block 26 (line 59)

```
まとめ
```

### Block 27 (line 62)

```
上記の手順は長く見えるかもしれませんが、そもそも存在すべきではない状態をカバーしています。今後、ペアリングは**高速で信頼性が高く、通常は自動的に** 行われます。
```

### Block 28 (line 66)

```
質問、コメント、修正は westsiderobotics@verizon.net までお願いします。
```


## programming_resources/shared/pid_coefficients/pid-coefficients.rst

### Block 1 (line 1)

```
PID 係数の変更
```

### Block 2 (line 4)

```
**REV Robotics Control Hub** および**REV Robotics Expansion Hub** を使用すると、ユーザーは閉ループモーター制御に使用される PID 係数を変更できます。PID 係数はチャネルとモードに固有です。
```

### Block 3 (line 6)

```
次の **op mode** は、拡張または強化された**DcMotor** クラス（「**DcMotorEx**」と呼ばれる）を使用して、「left_drive」という名前のモーターの RUN_USING_ENCODER モードの PID 係数を変更します。**op mode** は、**DcMotorEx** クラスの setPIDCoefficients メソッドを使用して値を変更します。このメソッドは、標準の**DcMotor** クラスでは使用できません。
```

### Block 4 (line 8)

```
PID 係数に加えた変更は、**REV Robotics Control Hub** または**REV Robotics Expansion Hub** の電源を入れ直すと保持されないことに注意してください。PID への変更を保持する必要がある場合は、**op mode** を変更して、**Control Hub** または**Android** スマートフォンに状態情報を保存することを検討する必要があります。Android Developer Web サイトには、アプリから**Android** デバイスにデータを保存する方法に関するチュートリアルがあります `こちら <https://developer.android.com/training/data-storage>`__
```

### Block 5 (line 22)

```
    * これは、DC モーターコントローラーとして REV Robotics Control Hub または
    * REV Robotics Expansion Hub を使用していることを前提としています。
    * この op mode は、DcMotorEx クラスの拡張/強化された PID 関連機能を使用します。
```

### Block 6 (line 30)

```
       // DC モーター
```

### Block 7 (line 38)

```
           // DC モーターへの参照を取得
           // Control Hub または Expansion Hub を使用しているため、
           // このモーターを DcMotorEx オブジェクトにキャストします
```

### Block 8 (line 43)

```
           // 開始コマンドを待ちます
```

### Block 9 (line 46)

```
           // RUN_USING_ENCODER モードの PID 係数を取得
```

### Block 10 (line 49)

```
           // DcMotorEx クラスに含まれるメソッドを使用して係数を変更
```

### Block 11 (line 53)

```
           // 係数を再読み取りして変更を確認
```

### Block 12 (line 56)

```
           // ユーザーに情報を表示
```

### Block 13 (line 69)

```
PID 制御とは？
```

### Block 14 (line 72)

```
PID（比例-積分-微分）制御は、制御システムで使用されるフィードバックメカニズムです。モーター制御のコンテキストでは、PID コントローラーは、望ましい速度または位置（セットポイント）と実際の速度または位置の間の誤差を計算し、その誤差を最小化するようにモーター出力を調整します。
```

### Block 15 (line 74)

```
**PID 係数の説明：**
```

### Block 16 (line 76)

```
- **P（比例）**: 現在の誤差に比例する制御出力を生成します。P 値が大きいほど、セットポイントへの応答が速くなりますが、オーバーシュートや振動が発生する可能性があります。
```

### Block 17 (line 78)

```
- **I（積分）**: 時間の経過とともに蓄積された誤差に基づいて制御出力を生成します。これは、定常状態誤差を排除するのに役立ちますが、I 値が大きすぎると、システムの不安定性につながる可能性があります。
```

### Block 18 (line 80)

```
- **D（微分）**: 誤差の変化率に基づいて制御出力を生成します。これは、オーバーシュートを減らし、システムの安定性を向上させるのに役立ちますが、D 値が大きすぎると、ノイズ感度が増す可能性があります。
```

### Block 19 (line 83)

```
PID 係数の調整
```

### Block 20 (line 86)

```
PID 係数の調整は、特定のモーターとアプリケーションに最適なパフォーマンスを達成するための反復プロセスです。開始点として：
```

### Block 21 (line 88)

```
1. すべての係数をゼロに設定することから始めます。
2. P 係数を増やして、システムが応答するまで確認します。
3. システムが振動または不安定になり始めるまで、P を増やし続けます。
4. P を最後の安定値の約半分に減らします。
5. I 係数を小さな値から増やして、定常状態誤差を排除します。
6. 必要に応じて D 係数を追加して、オーバーシュートを減らし、システムの応答を改善します。
```

### Block 22 (line 95)

```
**注意**: PID 調整は複雑なプロセスであり、各ロボットとアプリケーションに固有です。最適な結果を得るには、実験とテストが必要です。
```

### Block 23 (line 98)

```
デフォルトの PID 値
```

### Block 24 (line 101)

```
**REV Robotics Control Hub** および**Expansion Hub** には、ほとんどのアプリケーションでうまく機能する各モーターチャネルのデフォルト PID 値があります。これらのデフォルト値は、**REV Robotics** によって広範なテストを通じて決定されています。
```

### Block 25 (line 103)

```
カスタム PID 係数が必要な場合のみ、デフォルト値を変更することをお勧めします。
```

### Block 26 (line 106)

```
追加リソース
```

### Block 27 (line 109)

```
PID 制御の詳細については、次のリソースを参照してください：
```

### Block 28 (line 113)

```
- `FIRST Tech Challenge フォーラム <https://ftc-community.firstinspires.org/>`__
```


## programming_resources/shared/pidf_coefficients/pidf-coefficients.rst

### Block 1 (line 1)

```
PIDF 係数の変更
```

### Block 2 (line 4)

```
**REV Robotics Control Hub** または**REV Robotics Expansion Hub** を使用すると、ユーザーは閉ループモーター制御に使用される PIDF 係数を変更できます。PIDF 係数は、各チャネル（モーターポート）と各 RunMode に固有です。
```

### Block 3 (line 6)

```
次のサンプル **OpMode** は、拡張または強化された**DcMotor** クラス（「**DcMotorEx**」と呼ばれる）を使用して、「left_drive」という名前のモーターの RUN_USING_ENCODER RunMode の PIDF 係数を変更します。**OpMode** は、**DcMotorEx** クラスの setPIDFCoefficients メソッドを使用して値を変更します。このメソッドは、標準の**DcMotor** クラスでは使用できません。
```

### Block 4 (line 8)

```
PIDF 係数に加えた変更は、**REV Robotics Control Hub** または**REV Robotics Expansion Hub** の電源を入れ直すと保持されないことに注意してください。変更を保持する必要がある場合は、**OpMode** を変更して、**Control Hub** または**Android** スマートフォンに状態情報を保存することを検討してください。Android Developer Web サイトには、アプリから**Android** デバイスにデータを保存する方法に関するチュートリアルがあります `こちら <https://developer.android.com/training/data-storage>`__
```

### Block 5 (line 22)

```
    * これは、DC モーターコントローラーとして REV Robotics Control Hub または
    * REV Robotics Expansion Hub を使用していることを前提としています。
    * この OpMode は、DcMotorEx クラスの拡張/強化された PIDF 関連機能を使用します。
```

### Block 6 (line 30)

```
       // DC モーター
```

### Block 7 (line 37)

```
       // これらの値は説明のみを目的としています。
       // 各モーターの計画された使用法に基づいて設定および調整する必要があります。
```

### Block 8 (line 41)

```
           // DC モーターへの参照を取得
           // Control Hub または Expansion Hub を使用しているため、
           // このモーターを DcMotorEx オブジェクトにキャストします
```

### Block 9 (line 46)

```
           // 開始コマンドを待ちます
```

### Block 10 (line 49)

```
           // RUN_USING_ENCODER RunMode の PIDF 係数を取得
```

### Block 11 (line 52)

```
           // DcMotorEx クラスに含まれるメソッドを使用して係数を変更
```

### Block 12 (line 56)

```
           // 係数を再読み取りして変更を確認
```

### Block 13 (line 59)

```
           // ユーザーに情報を表示
```

### Block 14 (line 72)

```
PIDF 制御とは？
```

### Block 15 (line 75)

```
PIDF（比例-積分-微分-フィードフォワード）制御は、PID 制御の拡張版で、フィードフォワード（F）項が追加されています。フィードフォワード項は、システムのダイナミクスの既知の情報に基づいて制御出力を予測的に調整し、応答性と精度を向上させます。
```

### Block 16 (line 77)

```
**PIDF 係数の説明：**
```

### Block 17 (line 79)

```
- **P（比例）**: 現在の誤差に比例する制御出力を生成します。
```

### Block 18 (line 81)

```
- **I（積分）**: 時間の経過とともに蓄積された誤差に基づいて制御出力を生成します。
```

### Block 19 (line 83)

```
- **D（微分）**: 誤差の変化率に基づいて制御出力を生成します。
```

### Block 20 (line 85)

```
- **F（フィードフォワード）**: システムの既知の特性（重力、摩擦など）を補償するための追加の制御出力を提供します。フィードフォワード項は、望ましい速度または位置を達成するために必要な出力を予測するのに役立ちます。
```

### Block 21 (line 88)

```
PIDF 係数の調整
```

### Block 22 (line 91)

```
PIDF 係数の調整は、PID 調整と似ていますが、フィードフォワード項が追加されています：
```

### Block 23 (line 93)

```
1. PID 係数を調整します（前述の PID セクションを参照）。
2. F 係数を追加して、定常状態のパフォーマンスを向上させます。
3. F 値は通常、望ましい速度を達成するために必要なモーター電力に基づいて計算されます。
4. 実験を通じて F 値を微調整して、最適なパフォーマンスを達成します。
```

### Block 24 (line 98)

```
**注意**: PIDF 調整は高度なトピックであり、モーター制御システムの深い理解が必要です。
```

### Block 25 (line 101)

```
PID と PIDF の使い分け
```

### Block 26 (line 104)

```
- **PID** は、ほとんどの基本的なモーター制御アプリケーションに適しています。
- **PIDF** は、より高い精度と応答性が必要な高度なアプリケーションに推奨されます。
- フィードフォワード項（F）は、既知のシステムダイナミクス（重力、摩擦など）を補償する場合に特に役立ちます。
```

### Block 27 (line 109)

```
デフォルトの PIDF 値
```

### Block 28 (line 112)

```
**REV Robotics Control Hub** および**Expansion Hub** には、各モーターチャネルのデフォルト PIDF 値があります。これらのデフォルト値は、ほとんどのアプリケーションでうまく機能しますが、特定の要件に基づいて調整できます。
```

### Block 29 (line 115)

```
追加リソース
```

### Block 30 (line 118)

```
PIDF 制御の詳細については、次のリソースを参照してください：
```

### Block 31 (line 122)

```
- `FIRST Tech Challenge フォーラム <https://ftc-community.firstinspires.org/>`__
- `REV Robotics ドキュメント <https://docs.revrobotics.com/>`__
```


## programming_resources/shared/program_and_manage_network/Connecting-a-Laptop-to-the-Program-&-Manage-Network.rst

### Block 1 (line 1)

```
ラップトップを Program & Manage ネットワークに接続する
```

### Block 2 (line 4)

```
**Op Mode** を作成するには、プログラミングラップトップを Program & Manage Wi-Fi ネットワークに接続する必要があります。Program & Manage Wi-Fi ネットワークは、**Robot Controller** によって作成されるワイヤレスネットワークです。この演習を開始する前に、Windows ラップトップに Microsoft の最新のサービスパックとシステム更新プログラムがインストールされていることを確認してください。
```

### Block 3 (line 6)

```
この例では、ユーザーが Windows 10 ラップトップを使用していることを前提としています。Windows 10 ラップトップを使用していない場合、Programming & Manage Wi-Fi ネットワークに接続する手順は異なります。Wi-Fi ネットワークへの接続方法の詳細については、デバイスのドキュメントを参照してください。
```

### Block 4 (line 8)

```
ラップトップを Program & Manage ネットワークに接続する手順
```

### Block 5 (line 11)

```
1. **DRIVER STATION** で、画面の右上隅にある 3 つのドットをタッチしてポップアップメニューを起動します。ポップアップメニューから**Program & Manage** を選択して、**Program & Manage** アクセス情報を表示します。
```

### Block 6 (line 18)

```
2. Program & Manage 画面には、ラップトップを **Blocks** または**OnBot Java** プログラミングモードサーバーに接続するために使用できる**Robot Controller** への接続に必要な重要な情報が表示されます。
```

### Block 7 (line 25)

```
3. Program & Manage ワイヤレスネットワークのネットワーク名とパスフレーズを確認します。画面の上部に、Program & Manage ワイヤレスネットワークの名前が表示されます。**Robot Controller** として**Android** スマートフォンを使用している場合、ワイヤレスネットワーク名は「DIRECT-」という語句で始まります。
```

### Block 8 (line 27)

```
   この例では、Wi-Fi ネットワークの名前は「DIRECT-XK-9999-C-RC」で、セキュアパスフレーズは「ZU7if0hB」です。
```

### Block 9 (line 34)

```
**Control Hub** を使用している場合、ワイヤレスネットワーク名は**Control Hub** を構成したときに指定したものになります。**Control Hub** の名前をまだ変更していない場合、デフォルトではワイヤレスネットワークの名前は「FTC-」で始まります。パスワードをまだ変更していない場合、デフォルトではワイヤレスネットワークのパスフレーズは「password」になります。
```

### Block 10 (line 36)

```
以下のスクリーンショットでは、**Control Hub** のワイヤレスネットワーク名は「FTC-1Ybr」で、セキュアパスフレーズは「password」です。
```

### Block 11 (line 43)

```
4. Windows 10 コンピューターで、デスクトップの右下隅にある Wi-Fi シンボルを探します。Wi-Fi シンボルをクリックして、近くの利用可能な Wi-Fi ネットワークのリストを表示します。
```

### Block 12 (line 50)

```
5. Program & Manage 画面に表示されている名前と一致するワイヤレスネットワークを探します。
```

### Block 13 (line 57)

```
   この例では、**Android** **Robot Controller** のワイヤレスネットワークの名前は「DIRECT-XK-9999-C-RC」で、Windows 10 コンピューターに表示されるリストにネットワークが表示されています。
```

### Block 14 (line 59)

```
6. リストでターゲットネットワークを見つけたら、それをクリックして選択します。
```

### Block 15 (line 66)

```
   「Connect」ボタンを押してネットワークに接続します。
```

### Block 16 (line 68)

```
7. プロンプトが表示されたら、ネットワークパスフレーズ（この例では「ZU7if0hB」）を入力し、「Next」を押して続行します。
```

### Block 17 (line 75)

```
パスフレーズは大文字と小文字を区別することに注意してください。スペルと大文字小文字の使い方が、Program & Manage 画面に表示されている元のスペルと大文字小文字の使い方と一致していることを確認してください。
```

### Block 18 (line 77)

```
8. Windows 10 ラップトップと **Robot Controller** **Android** デバイス間のワイヤレス接続が正常に確立されると、ラップトップのワイヤレス設定にステータスが表示されます。
```

### Block 19 (line 84)

```
数秒後に表示が更新されない場合は、Wi-Fi 接続を示す青いボックスの下部にある「Network Connections」をクリックしてみてください。これにより、「Show available networks」へのリンクを含む Setting ダイアログボックスが表示され、Wi-Fi 接続のリストを強制的に更新できます。
```

### Block 20 (line 89)

```
ワイヤレス接続のトラブルシューティング
```

### Block 21 (line 92)

```
利用可能なネットワークのリストにプログラミングモードワイヤレスネットワークが表示されない場合、またはラップトップを Program & Manage ワイヤレスネットワークに接続する際に問題がある場合は、以下の質問に答えてください：
```

### Block 22 (line 94)

```
1. **Robot Controller** は実行中で、**DRIVER STATION** に接続されていますか？
2. Windows ラップトップは最新のシステム更新プログラムとサービスパックで更新されていますか？たとえば、古いバージョンの Windows 8 や 10 には、ラップトップが利用可能なネットワークのリストに Program & Manage ワイヤレスネットワークを表示できなくなる問題がありました。
```


## programming_resources/shared/required_materials/Required-Materials.rst

### Block 1 (line 1)

```
必要な材料
```

### Block 2 (line 4)

```
この Wiki には、**FIRST** **Tech Challenge** 制御システムの構成、プログラミング、操作方法を示すチュートリアルが含まれています。チュートリアルを完了するには、以下の材料が必要です：
```

### Block 3 (line 48)

```
   * - 必要な項目
     - 画像
```

### Block 4 (line 51)

```
   * - ROBOT CONTROLLER として使用する **REV Robotics Control Hub** 。
       または、競技マニュアルでは、チームが **REV Robotics Expansion Hub** と選択された**Android** 端末のリストを代わりに使用することを許可しています。
```

### Block 5 (line 55)

```
   * - DRIVER STATION デバイスとして使用する **REV Robotics Driver Hub** 。
       または、競技マニュアルでは、チームが選択された **Android** 端末のリストを代わりに使用することを許可しています。詳細については、ルール R901 を参照してください。
```

### Block 6 (line 59)

```
   * - ワイヤレスインターネットアクセス。
```

### Block 7 (line 62)

```
   * - Microsoft Windows 7、8、10、または 11 を搭載し、Wi-Fi 機能を備えたPC。PCには、Microsoft からの最新のサービス パックとシステム アップデートが適用されている必要があります。プログラミング デバイスとして別の種類のマシン（Chromebook、Android タブレットなど）を使用している場合、ロボット コントローラーのプログラミング サーバーにアクセスする手順が若干異なる場合があります。Wi-Fi ネットワークに接続する方法の詳細については、ご使用のデバイスのユーザー ドキュメントを参照してください。
```

### Block 8 (line 65)

```
   * - JavaScript 対応のウェブブラウザ（Google Chrome を推奨）。
```

### Block 9 (line 68)

```
   * - **REV Robotics** スイッチ、ケーブル、およびブラケット（REV-31-1387）。
```

### Block 10 (line 71)

```
   * - **FIRST** 承認\* 12V バッテリー（Tetrix W39057 または **REV Robotics** REV-31-1302 など）。\*\ ****FIRST**承認 12V バッテリーのリストについては、現在の競技マニュアルを参照してください。**\
```

### Block 11 (line 74)

```
   * - **FIRST** 承認\* 12V DC モーター（Tetrix W39530、電源ケーブル W41352 など）。\*\ ****FIRST**承認 12V モーターのリストについては、現在の競技マニュアルを参照してください。**\
```

### Block 12 (line 78)

```
   * - Tamiya コネクタを持つ承認された 12V バッテリー（Tetrix W39057 バッテリーなど）を使用している場合は、**REV Robotics**Tamiya to XT30 アダプターケーブル（REV-31-1382）が必要です。**REV Robotics** Slim Battery（REV-31-1302）を使用している場合、REV バッテリーにはすでに XT30 コネクタが付いているため、このアダプターは必要ありません。
```

### Block 13 (line 81)

```
   * - **REV Robotics** Anderson to JST VH ケーブル（REV-31-1381）。
```

### Block 14 (line 84)

```
   * - 180 度標準スケールサーボ（Hitec HS-485HB など）。
```

### Block 15 (line 87)

```
   * - 4 ピンケーブル付き **REV Robotics Color Sensor** （REV-31-1154）。
```

### Block 16 (line 90)

```
   * - 4 ピンケーブル付き **REV Robotics Touch Sensor** （REV-31-1425）。
```

### Block 17 (line 93)

```
   * - Logitech F310 USB ゲームパッド。
```

### Block 18 (line 96)

```
   * - **Robot Controller** としてスマートフォンを使用している場合は、USB Type A オス - Type mini-B オスケーブルが必要です。**Control Hub** ユーザーは、このケーブルは必要ありません。
```

### Block 19 (line 99)

```
   * - **Robot Controller** としてスマートフォンを使用している場合は、micro USB OTG アダプターが 2 個必要です。**Robot Controller** として**Control Hub** を使用している場合は、micro USB OTG アダプターが 1 個必要です。
```


## programming_resources/shared/using_android_device/Using-Your-Android-Device.rst

### Block 1 (line 1)

```
**Android** デバイスの使用
```

### Block 2 (line 4)

```
制御システムを始める前に、**Android** デバイスの基本的な操作に慣れることが役立ちます。
```

### Block 3 (line 9)

```
DRIVER STATION として **REV Robotics Driver Hub** を使用しているチームは、`REV Robotics の公式ドキュメント <https://docs.revrobotics.com/duo-control/driver-hub-gs>`__ を参照して、**REV Robotics Driver Hub** のセットアップと使用方法の手順を確認してください。
```

### Block 4 (line 11)

```
**Android** スマートフォン
```

### Block 5 (line 14)

```
推奨されませんが、競技マニュアルでは、一部の **Android** スマートフォンを DRIVER STATION または ROBOT CONTROLLER として使用することを許可しています。詳細については、ルール R704 を参照してください。
```

### Block 6 (line 16)

```
画面のロック解除
```

### Block 7 (line 19)

```
**Android** 端末の電源を初めて入れると、通常、画面は「ロック」状態で始まります。**FIRST** **Tech Challenge** で使用される Motorola スマートフォンでは、ロック画面をタッチしてから、画面に沿って指を上方向にスライドして端末のロックを解除する必要があります。デバイスによっては、画面のロックを解除するために若干異なる手順が必要な場合があることに注意してください。
```

### Block 8 (line 26)

```
**Android** のセキュリティ設定によっては、ロック解除時にパスコードまたは PIN 番号の入力を求められる場合があります。タッチスクリーンを使用してパスコードまたは PIN 値を入力し、チェックマークをタップしてデバイスにログインします。
```

### Block 9 (line 33)

```
**Android** でのナビゲーション
```

### Block 10 (line 36)

```
端末の電源を入れてロックを解除したばかりの場合、ホーム画面が表示されるはずです。実際のスマートフォンの画面は、このガイドに表示されている画像とは異なる場合があることに注意してください。
```

### Block 11 (line 48)

```
画面の下部には、**Android** デバイスの画面をナビゲートするために使用できるボタンがいくつかあります。
```

### Block 12 (line 55)

```
左端のボタン（上の画像を参照）は「Back」ボタンです。このボタンを使用して、**Android** デバイスの前の画面に戻ることができます。
```

### Block 13 (line 57)

```
中央のボタンは「Home」ボタンです。このボタンを押すと、**Android** デバイスのホーム画面または開始画面に戻ります。
```

### Block 14 (line 59)

```
右端のボタンは「Recent Apps」ボタンです。このボタンをクリックすると、最近実行されてバックグラウンドで休止しているアプリが表示されます。アプリのリストの「X」ボタンをタップして、最近のアプリを閉じることができます。
```

### Block 15 (line 66)

```
一部の **Android** スマートフォンには、下部のナビゲーションボタンを自動的に非表示にする自動非表示機能があることに注意してください。スマートフォンにこの機能がある場合は、画面の下部から上にスワイプしてナビゲーションボタンを表示する必要がある場合があります。
```

### Block 16 (line 68)

```
**Android** 端末で利用可能なアプリを表示する
```

### Block 17 (line 71)

```
**Android**Nougat（7.x）以降のデバイスを使用している場合は、タッチスクリーンの下部から上にスワイプするだけで、利用可能なアプリを表示できます。新しいバージョンの**Android** には、*App Drawer* 機能がなくなりました。
```


## programming_resources/tutorial_specific/android_studio/controlling_a_servo/Controlling-a-Servo-(Android-Studio).rst

### Block 1 (line 1)

```
サーボの制御 :bdg-success:`AS`
```

### Block 2 (line 4)

```
このセクションでは、ゲームパッドのボタンでサーボモーターを制御するように **Op Mode** を変更します。
```

### Block 3 (line 6)

```
サーボモーターとは何ですか？
```

### Block 4 (line 9)

```
サーボモーターは特殊なタイプのモーターです。サーボモーターは精密な動作を実現するために設計されています。一般的なサーボモーターは、可動範囲が限られています。
```

### Block 5 (line 11)

```
以下の図には、「標準スケール」の180度サーボが示されています。このタイプのサーボは、ホビイストや **FIRST Tech Challenge** チームに人気があります。このサーボモーターは、シャフトを180度の範囲で回転させることができます。サーボコントローラーとして知られる電子モジュールを使用すると、サーボモーターを特定の位置に移動させる**Op Mode** を作成できます。モーターがこの目標位置に到達すると、サーボのシャフトに外力が加えられても、その位置を保持します。
```

### Block 6 (line 18)

```
サーボモーターは、正確な動きを実現したい場合に便利です（たとえば、センサーでエリアをスキャンしてターゲットを探したり、リモートコントロール飛行機の操縦舵面を動かしたりする場合）。
```

### Block 7 (line 20)

```
サーボを制御するための **Op Mode** の変更
```

### Block 8 (line 23)

```
サーボモーターを制御するために必要なロジックを追加するように **Op Mode** を変更しましょう。この例では、Logitech F310ゲームパッドのボタンを使用して、サーボモーターの位置を制御します。
```

### Block 9 (line 25)

```
一般的なサーボでは、サーボの目標位置を指定できます。サーボはモーターシャフトを回転させて目標位置に移動し、その後、その位置を乱そうとする適度な力が加えられても、その位置を保持します。
```

### Block 10 (line 27)

```
**FIRST Tech Challenge** 制御システムでは、サーボの目標位置を0から1の範囲で指定できます。目標位置0は回転角度0度に対応し、目標位置1は一般的なサーボモーターの回転角度180度に対応します。
```

### Block 11 (line 34)

```
この例では、F310コントローラーの右側にある色付きボタンを使用して、サーボの位置を制御します。最初に、**Op Mode** はサーボを中間位置（180度範囲の90度）に移動させます。黄色の「Y」ボタンを押すと、サーボは0度の位置に移動します。青色の「X」ボタンまたは赤色の「B」ボタンを押すと、サーボは90度の位置に移動します。緑色の「A」ボタンを押すと、サーボは180度の位置に移動します。
```

### Block 12 (line 41)

```
次のコードを追加するように **Op Mode** を変更します：
```

### Block 13 (line 69)

```
この追加されたコードは、F310ゲームパッドの色付きボタンのいずれかが押されているかどうかをチェックします。Yボタンが押されている場合、サーボは0度の位置に移動します。XボタンまたはBボタンのいずれかが押されている場合、サーボは90度の位置に移動します。Aボタンが押されている場合、サーボは180度の位置に移動します。また、**Op Mode** はサーボ位置に関するテレメトリーデータを**Driver Station** に送信します。
```

### Block 14 (line 71)

```
**Op Mode** を変更した後、ビルドして実行できます。ゲームパッド#1がまだ構成されていることを確認してから、色付きボタンを使用してサーボの位置を移動します。
```


## programming_resources/tutorial_specific/android_studio/creating_op_modes/Creating-and-Running-an-Op-Mode-(Android-Studio).rst

### Block 1 (line 1)

```
OpMode の作成と実行 :bdg-success:`AS`
```

### Block 2 (line 4)

```
TeamCode モジュール
```

### Block 3 (line 7)

```
Android Studio プロジェクトフォルダーを正常にインポートした場合、プロジェクトブラウザーに ``TeamCode`` という名前の Android モジュールが表示されます。Android Studio プロジェクトフォルダーは、競技用ロボットを制御するために作成するカスタム **OpMode** を含む**Robot Controller** アプリのバージョンをビルドするために使用されます。
```

### Block 4 (line 14)

```
クラスと **OpMode** を作成する際は、TeamCode モジュールに存在する ``org.firstinspires.ftc.teamcode`` パッケージ内に作成します。このパッケージは、Android Studio プロジェクトフォルダー内であなたが使用するために予約されています。
```

### Block 5 (line 16)

```
Javadoc リファレンス情報
```

### Block 6 (line 19)

```
SDK の Javadoc リファレンスドキュメントはオンラインで利用できます。
SDK ドキュメントを表示するには、次の URL にアクセスしてください。
```

### Block 7 (line 24)

```
自動インポートの有効化
```

### Block 8 (line 27)

```
**Android Studio** の自動インポート機能は、**OpMode** を記述する際の時間を節約するのに役立つ便利な機能です。この機能を有効にする場合は、Android Studio 設定画面から Editor->General->Auto Import 項目を選択します。これにより、エディターの自動インポート設定が表示されます。
```

### Block 9 (line 29)

```
「Add unambiguous imports on the fly」をチェックすると、**Android Studio** が**OpMode** で使用したいクラスに必要なインポート文を自動的に追加します。
```

### Block 10 (line 36)

```
サンプル OpMode
```

### Block 11 (line 39)

```
ロボットのプログラミング方法を学ぶ優れた方法は、Android Studio プロジェクトフォルダーに含まれているサンプル **OpMode** を調べることです。これらのファイルは、FtcRobotController モジュールの ``org.firstinspires.ftc.robotcontroller.external.samples`` パッケージにあります。
```

### Block 12 (line 46)

```
サンプル **OpMode** を使用したい場合は、``org.firstinspires.ftc.robotcontroller.external.samples`` パッケージからコピーして、``org.firstinspires.ftc.teamcode`` パッケージに移動します。
```

### Block 13 (line 48)

```
新しくコピーした **OpMode** で、次のアノテーションを探します。
```

### Block 14 (line 52)

```
この行をコメントアウトして **OpMode** を有効にし、**Robot Controller** で実行できるようにします。
```

### Block 15 (line 56)

```
最初の OpMode の作成
```

### Block 16 (line 59)

```
``org.firstinspires.ftc.teamcode`` パッケージを右クリックし、ポップアップメニューから New->Java Class を選択します。Create New Class ダイアログボックスが表示されます。新しいクラスの名前を``MyFIRSTJavaOpMode`` と指定します。
```

### Block 17 (line 66)

```
OK ボタンを押して新しいクラスを作成します。新しいクラスのソースコードが Android Studio ユーザーインターフェースの編集ペインに表示されます。
```

### Block 18 (line 73)

```
**OpMode** のメイン部分を次のコードのように変更します（次のソースコードでは、パッケージ定義といくつかのインポート文が省略されていることに注意してください）。
```

### Block 19 (line 109)

```
このソースコードを、最初の **OpMode** のフレームワークとして使用します。
**Android Studio** は、編集中にソースコードを自動的に保存することに注意してください。
```

### Block 20 (line 112)

```
おめでとうございます！**OpMode** を作成しました。まだあまり機能はありませんが、より便利にするために変更を加えていきます。
```

### Block 21 (line 114)

```
OpMode の構造を理解する
```

### Block 22 (line 117)

```
**OpMode** を、**Robot Controller** が実行するタスクのリストと考えると役立ちます。線形**OpMode** の場合、**Robot Controller** はこのタスクのリストを順次処理します。ユーザーは、制御ループ（while ループなど）を使用して、**Robot Controller** に線形**OpMode** 内の特定のタスクを繰り返し（または反復）させることもできます。
```

### Block 23 (line 124)

```
**OpMode** をロボットへの命令のリストと考えると、作成したこの一連の命令は、チームメンバーがこの**Robot Controller** で利用可能な**OpMode** のリストから ``MyFIRSTJavaOpMode`` という**OpMode** を選択すると、ロボットによって実行されます。
```

### Block 24 (line 126)

```
新しく作成した **OpMode** の構造を見てみましょう。以下は**OpMode** テキストのコピーです（一部のコメント、パッケージ定義、およびいくつかのインポートパッケージステートメントは省略されています）。
```

### Block 25 (line 162)

```
**OpMode** の開始時には、クラス定義の前にアノテーションがあります。このアノテーションは、これが遠隔操作（つまり、ドライバーが制御する）**OpMode** であることを示しています。
```

### Block 26 (line 166)

```
この **OpMode** を自律**OpMode** に変更したい場合は、``@TeleOp`` を``@Autonomous`` アノテーションに置き換えます。
```

### Block 27 (line 168)

```
サンプルコードから、**OpMode** が Java クラスとして定義されていることがわかります。この例では、**OpMode** 名は ``MyFIRSTJavaOpMode`` と呼ばれ、**LinearOpMode** クラスから特性を継承しています。
```

### Block 28 (line 174)

```
また、OnBot Java エディターがこの **OpMode** 用に5つのプライベートメンバー変数を作成したことがわかります。これらの変数は、OnBot Java エディターが**Robot Controller** の構成ファイルで検出した5つの構成済みデバイスへの参照を保持します。
```

### Block 29 (line 184)

```
次に、``runOpMode`` と呼ばれるオーバーライドされたメソッドがあります。``LinearOpMode`` 型のすべての **OpMode** は、このメソッドを実装する必要があります。このメソッドは、ユーザーが**OpMode** を選択して実行したときに呼び出されます。
```

### Block 30 (line 191)

```
``runOpMode`` メソッドの開始時に、**OpMode** は``hardwareMap`` という名前のオブジェクトを使用して、**Robot Controller** の構成ファイルにリストされているハードウェアデバイスへの参照を取得します。
```

### Block 31 (line 201)

```
``hardwareMap`` オブジェクトは、``runOpMode`` メソッド内で使用できます。これは **HardwareMap** クラスのタイプのオブジェクトです。
```

### Block 32 (line 203)

```
**OpMode** で特定のデバイスへの参照を取得しようとする場合、``HardwareMap.get`` メソッドの2番目の引数として指定する名前は、構成ファイルでデバイスを定義するために使用された名前と一致する必要があることに注意してください。例えば、``motorTest`` という名前の DC モーターを持つ構成ファイルを作成した場合、``hardwareMap`` オブジェクトからこのモーターを取得するには、同じ名前（大文字と小文字が区別されます）を使用する必要があります。名前が一致しない場合、**OpMode** はデバイスが見つからないことを示す例外をスローします。
```

### Block 33 (line 205)

```
例の次のいくつかのステートメントで、**OpMode** はユーザーに続行するためのスタートボタンを押すように促します。``runOpMode`` メソッドで使用できる別のオブジェクトを使用します。このオブジェクトは telemetry と呼ばれ、**OpMode** は``addData`` メソッドを使用して**Driver Station** に送信するメッセージを追加します。次に、**OpMode** は update メソッドを呼び出してメッセージを**Driver Station** に送信します。その後、``waitForStart`` メソッドを呼び出して、ユーザーがドライバーステーションのスタートボタンを押して**OpMode** の実行を開始するまで待機します。
```

### Block 34 (line 214)

```
すべての線形 **OpMode** には、ドライバーがスタートボタンを押すまでロボットが**OpMode** の実行を開始しないようにするために、``waitForStart`` ステートメントが必要であることに注意してください。
```

### Block 35 (line 216)

```
スタートコマンドを受信した後、**OpMode** は while ループに入り、**OpMode** がアクティブでなくなるまで（つまり、ユーザーが**Driver Station** の停止ボタンを押すまで）このループで反復を続けます。
```

### Block 36 (line 227)

```
**OpMode** が while ループで反復する際、インデックスが「Status」でメッセージが「Running」のテレメトリメッセージを**Driver Station** に表示し続けます。
```

### Block 37 (line 229)

```
OpMode のビルドとインストール
```

### Block 38 (line 232)

```
**Robot Controller** スマートフォンがラップトップに接続されており、ラップトップがスマートフォンに対する USB デバッグ権限を持っていることを確認します。
```

### Block 39 (line 239)

```
または、**Control Hub** を使用している場合は、**Control Hub** が新しく充電された 12V バッテリーで駆動されており、USB Type C ポートを介してラップトップに接続されていることを確認します。**Control Hub** には USB デバッグ権限が自動的に有効になっている必要があることに注意してください。
```

### Block 40 (line 246)

```
**Control Hub** を使用する場合は、**Control Hub** を開発用ラップトップに接続する際に、Type C ポート（USB Mini ポートではなく）を使用するようにしてください。
```

### Block 41 (line 253)

```
Android Studio ユーザーインターフェースの上部を見て、``TeamCode`` という単語の横にある小さな緑色の再生または実行ボタン（緑色の円形の矢印で表されます）を見つけます。正しいデバイスが選択されていることを確認してから、この緑色のボタンを押して **Robot Controller** アプリをビルドし、**Control Hub** （または RC スマートフォン）にインストールします。
```

### Block 42 (line 260)

```
以前に Google Play ストアから **Robot Controller** アプリのコピーをインストールしていた場合、新しくビルドされたアプリのインストールは最初の試行時に失敗します。これは、**Android Studio** が、今ビルドしたアプリが Google Play からインストールされた公式バージョンの**Robot Controller** アプリとは異なるデジタル署名を持っていることを検出するためです。
```

### Block 43 (line 267)

```
これが発生した場合、**Android Studio** は、デバイスから以前の（公式）バージョンのアプリをアンインストールし、更新されたバージョンのアプリに置き換えても良いかどうかを尋ねます。``OK`` を選択して以前のバージョンをアンインストールし、新しく作成した**Robot Controller** アプリに置き換えます（上の画像を参照）。
```

### Block 44 (line 274)

```
インストールが成功すると、**Robot Controller** アプリがターゲット Android デバイスで起動されるはずです。**Robot Controller** として Android スマートフォンを使用している場合は、スマートフォンにメインの**Robot Controller** アプリ画面が表示されます。
```

### Block 45 (line 276)

```
**Control Hub** には組み込みの画面がありませんが、**Control Hub** ユーザーの場合、**Driver Station** を確認することで、アプリが**Control Hub** に正しくインストールされたことを確認できます。**Driver Station** が**Control Hub** に正常に接続されていることを示している場合（更新の発生中に一時的に切断された後）、アプリは正常に更新されました。
```

### Block 46 (line 278)

```
OpMode の実行
```

### Block 47 (line 281)

```
新しい **OpMode** を含む更新された Android アプリを正常にビルドおよびインストールした場合、**OpMode** を実行する準備が整いました。**Driver Station** がまだ **Robot Controller** に接続されていることを確認します。サンプルの **OpMode** を遠隔操作 **OpMode** として指定したため、``TeleOp`` **OpMode** としてリストされます。
```

### Block 48 (line 283)

```
**Driver Station** で、``TeleOp`` ドロップダウンリストコントロールを使用して、使用可能な**OpMode** のリストを表示します。リストから**OpMode** （「MyFIRSTJavaOpMode」）を選択します。
```

### Block 49 (line 295)

```
「INIT」ボタンを押して **OpMode** を初期化します。
```

### Block 50 (line 307)

```
**OpMode** は、runOpMode メソッド内のステートメントを waitForStart ステートメントまで実行します。その後、続行するためにスタートボタン（三角形の記号で表されます）を押すまで待機します。
```

### Block 51 (line 319)

```
スタートボタンを押すと、**OpMode** は反復を続け、「Status: Running」メッセージを**Driver Station** に送信します。**OpMode** を停止するには、四角形の停止ボタンを押します。
```

### Block 52 (line 331)

```
おめでとうございます！最初の Java **OpMode** を実行しました！
```

### Block 53 (line 333)

```
モーターを制御するための OpMode の変更
```

### Block 54 (line 336)

```
**REV Robotics Control Hub** または**REV Robotics Expansion Hub** 用に接続および構成した DC モーターを制御するために、**OpMode** を変更しましょう。プログラムループのコードを次のように変更します。
```

### Block 55 (line 352)

```
追加されたコードを見ると、while ループに入る前に、target power という新しい変数を定義したことがわかります。
```

### Block 56 (line 358)

```
while ループの開始時に、変数 tgtPower を gamepad1 の左ジョイスティックの負の値に設定します。
```

### Block 57 (line 364)

```
``gamepad1`` オブジェクトは、``runOpMode`` メソッド内でアクセスできます。これは、**Driver Station** 上のゲームパッド #1 の状態を表します。
競技中に使用される F310 ゲームパッドでは、ジョイスティックの Y 値は、ジョイスティックが最上部の位置にあるときは -1 から、最下部の位置にあるときは +1 までの範囲であることに注意してください。
上のサンプルコードでは、``left_stick_y`` 値を否定して、左ジョイスティックを前方に押すとモーターに正の電力が適用されるようにします。この例では、モーターの前進と後退の概念は任意であることに注意してください。ただし、ジョイスティックの y 値を否定する概念は、実際には非常に有用です。
```

### Block 58 (line 373)

```
次の一連のステートメントは、motorTest の電力を変数 tgtPower で表される値に設定します。次に、目標電力と実際のモーター電力の値が、テレメトリメカニズムを介して **Driver Station** に送信されるデータのセットに追加されます。
```

### Block 59 (line 382)

```
これらの新しいステートメントを含めるように **OpMode** を変更したら、ビルドボタンを押して**OpMode** が正常にビルドされたことを確認します。
```

### Block 60 (line 384)

```
ゲームパッドを接続して OpMode を実行する
```

### Block 61 (line 387)

```
**OpMode** は、ゲームパッドから入力を受け取り、この入力を使用して DC モーターを制御します。**OpMode** を実行するには、Logitech F310 または他の承認されたゲームパッドを**Driver Station** に接続する必要があります。
```

### Block 62 (line 389)

```
ゲームパッドを **Driver Station** に接続します。**REV Robotics Driver Hub** を使用している場合、ゲームパッドを USB-A ポートの1つに直接接続できます。**DRIVER STATION** スマートフォンの場合、Micro USB OTG アダプターケーブルが必要です。
```

### Block 63 (line 401)

```
サンプル **OpMode** は、ユーザーまたはドライバー #1 として指定されたゲームパッドからの入力を探しています。Logitech F310 コントローラーの Start ボタンと A ボタンを同時に押して、ゲームパッドをユーザー #1 として指定します。Start ボタンと B ボタンを同時に押すと、ゲームパッドがユーザー #2 として指定されることに注意してください。PS4 スタイルのゲームパッドでは、ユーザー #1 の場合は Options ボタンと Cross を、ユーザー #2 の場合は Options と Circle を使用します。
```

### Block 64 (line 408)

```
ゲームパッドをユーザー #1 として正常に指定した場合、**Driver Station** 画面の右上隅にある「User 1」というテキストの上に小さなゲームパッドアイコンが表示されます。ゲームパッド #1 でアクティビティがあるたびに、小さなアイコンが緑色で強調表示されます。アイコンが表示されない場合、またはゲームパッドを使用したときに緑色で強調表示されない場合は、ゲームパッドへの接続に問題があります。
```

### Block 65 (line 410)

```
``MyFIRSTJavaOpMode`` **OpMode** を選択、初期化、実行します。
```

### Block 66 (line 412)

```
ゲームパッドを正しく構成した場合、左ジョイスティックでモーターの動きを制御できるはずです。**OpMode** を実行する際は、回転するモーターに何もが巻き込まれないように注意してください。ジョイスティックを動かすたびに、ユーザー #1 ゲームパッドアイコンが緑色で強調表示されることに注意してください。また、目標電力と実際のモーター電力の値が**Driver Station** のテレメトリエリアに表示されることにも注意してください。
```


## programming_resources/tutorial_specific/android_studio/disable_instant_run/disable-instant-run.rst

### Block 1 (line 1)

```
**Android Studio** の Instant Run を無効にする :bdg-warning:`Legacy` :bdg-success:`AS`
```

### Block 2 (line 5)

```
   *Instant Run* は **Android Studio** バージョン 3.5 で削除されました。
   **Android Studio** 3.5 以降のバージョンでは問題になりません。
   ただし、この記事は **FIRST** **Tech Challenge** ソフトウェア開発キット
   （**SDK** ）v7.1 以前のバージョンを古いバージョンの**Android Studio** で
   使用している方のために残されています。
```

### Block 3 (line 11)

```
はじめに
```

### Block 4 (line 14)

```
**Android Studio** を使用する場合、** 最も重要なステップの1つ** は**Android Studio** の Instant Run を無効にすることです。Instant Run は、アプリへのコード変更を適用する時間を短縮することで開発プロセスを合理化するように設計された機能です。残念ながら、Instant Run は機能が制限されており、**FIRST** **Tech Challenge** の**Android Studio** プロジェクトフォルダーで使用すると、** 重大な** 問題や** トラブルシューティングが困難な** 問題を引き起こす可能性があります。
```

### Block 5 (line 16)

```
**Android Studio** を使用するチームは、Instant Run を** 必ず** 無効にしてください。
```

### Block 6 (line 18)

```
Instant Run 設定の場所
```

### Block 7 (line 21)

```
**Android Studio** を初めて起動すると、Welcome 画面が表示されます。この Welcome 画面から Instant Run**Settings** に移動するには、画面右下隅の「Configure」ドロップダウンリストから「Configure->Settings」項目を選択します。
```

### Block 8 (line 25)

```
**Settings** ウィンドウの左側に、「Build, Execution, Deployment」というカテゴリーがあります。このカテゴリー内で、「Instant Run」サブカテゴリーをクリックすると、**Android Studio** インストールの Instant Run 設定が表示されます。デフォルトでは、**Android Studio** を初めてインストールすると Instant Run が有効になっています。「Enable Instant Run to hot swap code/resource changes on deploy (default enabled)」オプションのチェックを外し、「OK」ボタンをクリックして Instant Run を無効にしてください。
```

### Block 9 (line 29)

```
追加情報
```

### Block 10 (line 32)

```
Google **Android** Developer ウェブサイトには、Instant Run に関する追加情報があります。また、この機能を無効にする方法の説明もあります：
```


## programming_resources/tutorial_specific/android_studio/downloading_as_project_folder/Downloading-the-Android-Studio-Project-Folder.rst

### Block 1 (line 1)

```
**Android Studio** プロジェクトフォルダーのダウンロード :bdg-success:`AS`
```

### Block 2 (line 4)

```
**SDK** は GitHub リポジトリからダウンロードできます。 GitHub は、個人や組織がオンラインでコンテンツをホストできるようにする Web ベースのバージョン管理会社です。**Android Studio** ソフトウェアにアクセスするには、GitHub アカウントが必要です。 GitHub ウェブサイトにアクセスして無料でアカウントを作成できます：
```

### Block 3 (line 8)

```
ソフトウェアは、**FIRST-Tech-Challenge** GitHub 組織の「FtcRobotController」というリポジトリに保存されています：
```

### Block 4 (line 20)

```
リポジトリの Releases ページにジャンプします。Releases ページには、リポジトリの利用可能なソフトウェアリリースが一覧表示されます。 最新のリリースがページの上部近くに表示されます。
```

### Block 5 (line 27)

```
各ソフトウェアリリースには **Assets** セクションが含まれており、ロボットのプログラミングに必要なソフトウェアをダウンロードできます。この**Assets** セクションを展開するには、三角形のシンボルをクリックする必要がある場合があります。
```

### Block 6 (line 34)

```
Source code (zip) リンクをクリックして、圧縮された **Android Studio** プロジェクトフォルダーをダウンロードします。
```

### Block 7 (line 36)

```
アーカイブプロジェクトファイルの内容の抽出
```

### Block 8 (line 39)

```
アーカイブ（.ZIP）プロジェクトファイルをダウンロードしたら、このファイルを任意の場所に移動できます。
```

### Block 9 (line 46)

```
プロジェクトを **Android Studio** にインポートする前に、まずアーカイブプロジェクトファイルの内容を抽出する必要があります。Windows ユーザーの場合は、ファイルを右クリックして、ポップアップメニューから「すべて展開」を選択します。Windows は、抽出されたプロジェクトフォルダーの保存先を選択するように求めます。表示されるダイアログは、下図に示すものと似ているはずです。
```

### Block 10 (line 53)

```
保存先フォルダーの推奨名（上図では、推奨名は「FtcRobotController-6.0」）を強調表示し、保存先フォルダー名をよりユーザーフレンドリーな名前に変更します。この例では、保存先フォルダーの名前を「mycopy」に変更します。
```

### Block 11 (line 60)

```
保存先フォルダーの名前を変更したら、アーカイブの内容をフォルダーに抽出します。抽出プロセスが完了したら、プロジェクトフォルダーがターゲットの保存先に正常に抽出されたことを確認します。
```

### Block 12 (line 67)

```
アーカイブファイルの内容を正常に抽出したら、プロジェクトを **Android Studio** にインポートする準備が整いました。
```

### Block 13 (line 69)

```
プロジェクトを **Android Studio** にインポートする
```

### Block 14 (line 72)

```
プロジェクトをインポートするには、コンピューターで **Android Studio** ソフトウェアを起動する必要があります。**Android Studio** のメイン Welcome 画面で、「Open」オプションを選択してインポートプロセスを開始します。
```

### Block 15 (line 79)

```
**Android Studio** は、インポートするプロジェクトフォルダーを選択するように求めます。ポップアップダイアログボックスのファイルブラウザを使用して、このドキュメントの前のセクションで抽出したフォルダーを見つけてナビゲートします。抽出されたプロジェクトフォルダー（抽出されたフォルダーと似た名前の .ZIP ファイルではない）を選択していることを確認してください。「Select Folder」ボタンを押して、選択したプロジェクトを**Android Studio** にインポートします。
```

### Block 16 (line 86)

```
プロジェクトを信頼するかどうかに関するポップアップが表示される場合があります。その場合は、青い「Trust Project」ボタンをクリックして続行します。
```

### Block 17 (line 94)

```
**Android Studio** にインポートするために選択されています。プロジェクトのインポートには、
**Android Studio** が数分かかる場合があります。プロジェクトが正常にインポートされると、
画面は下図に示されているものと似たようになるはずです。
**Android Gradle Plugin (AGP)** の更新を求めるポップアップが表示された場合は、無視してください。
新しいバージョンは現在の ***FIRST* Tech Challenge SDK** と互換性がない可能性があるため、
AGP の更新を試みないでください。
```


## programming_resources/tutorial_specific/android_studio/enabling_developer_options/Enabling-Developer-Options.rst

### Block 1 (line 1)

```
開発者オプションの有効化 :bdg-success:`AS`
```

### Block 2 (line 4)

```
**Android** 端末を構成した後、**Android Studio** に含まれるツールを使用して端末にアプリをインストールできるようにする前に、端末が開発者モードになっていることを確認する必要があります。
```

### Block 3 (line 8)

```
**Android**Developer ウェブサイトには、端末で開発者オプションを有効にする方法に関する情報が含まれています。以下のリンクにアクセスし、「Enabling On-device Developer Options」というセクションを読むと、端末で**Settings**-> About phone に移動し、ビルド番号を7回タップすることで、**Android** 端末で開発者オプションを有効にできることがわかります。
```

### Block 4 (line 12)

```
**Android Studio** ツールを使用して端末にアプリをインストールできるようにするには、両方の端末で開発者オプションと USB デバッグが有効になっていることを確認する必要があります。
```

### Block 5 (line 19)

```
**Android Studio** を実行しているコンピューターに端末を初めて接続すると、コンピューターが端末への USB デバッグアクセスを許可してもよいかどうかを端末が尋ねる場合があります。その場合は、「Always allow from this computer」オプションをチェックし、OK ボタンを押して USB デバッグを許可してください。
```


## programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.rst

### Block 1 (line 1)

```
GitHub からフォークとクローンを行う :bdg-success:`AS`
```

### Block 2 (line 5)

```
   このアプローチは、`git <https://docs.github.com/en/get-started/learning-about-github/github-glossary#git>`__ と `GitHub <https://github.com/>`__ の基本的な知識があることを前提としています。git に関連することのほとんどについて、目的を達成するための方法は数多くあります。このドキュメントでは、Windows ユーザー向けの方法の一つを説明します。
   コマンドラインツールや git に不慣れなユーザーは、:doc:`SDK を zip アーカイブとしてダウンロード
   <../downloading_as_project_folder/Downloading-the-Android-Studio-Project-Folder>` する方法で SDK を入手してください。
```

### Block 3 (line 9)

```
フォーク vs. クローン
```

### Block 4 (line 12)

```
GitHub 上の `フォーク <https://docs.github.com/en/get-started/learning-about-github/github-glossary#fork>`__ とは、GitHub 上のある `リポジトリ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#repository>`__ を、あるアカウントから別のアカウントにコピーすることです。新しくフォークされたリポジトリは、`origin <https://docs.github.com/en/get-started/learning-about-github/github-glossary#origin>`__ リポジトリとの親子関係を保持します。フォークは通常、ソフトウェアが独立した開発ラインを持つ場合に使用されます。例えば、FTC チームが `FIRST-Tech-Challenge/FtcRobotController <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ リポジトリをベースに独自のチームコードを開発する場合などです。FTC チームは、ソフトウェア開発プロセスを管理する便利な方法として、`FIRST-Tech-Challenge/FtcRobotController <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ リポジトリのフォークを作成する必要があります。親子関係のおかげで、親リポジトリに変更が加えられた場合、それらの変更を簡単に追跡し、フォークされたリポジトリに `フェッチ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#fetch>`__ / `マージ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#merge>`__ することができ、フォークされたリポジトリを最新の状態に保つことができます。
```

### Block 5 (line 15)

```
   チームは、`upstream <https://docs.github.com/en/get-started/learning-about-github/github-glossary#upstream>`__ の親である FIRST-Tech-Challenge/FtcRobotContoller リポジトリに対してプルリクエストを発行しないでください。FIRST-Tech-Challenge/FtcRobotContoller リポジトリのフォークは、常に変更をフェッチすることはできますが、リポジトリに変更をプッシュすることは決して試みないでください。
```

### Block 6 (line 17)

```
`クローン <https://docs.github.com/en/get-started/learning-about-github/github-glossary#clone>`__ は、通常はローカルコンピューター上のリポジトリのコピーです。チームメンバーは、機能開発のためにチームのリポジトリの `機能ブランチ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#clone>`__ を作成し、そのブランチをローカルコンピューターにクローンします。ソフトウェアの開発とテストは、ローカルクローン内で完全に行われます。作業が完了するか、チェックポイントに到達したら、ローカルクローン内の変更をローカルクローンからチームのフォークにプッシュバックすることができます。その機能ブランチは、チームによって承認されると、チームのメインリポジトリブランチにマージすることができます。このプロセスを使用することで、複数の異なる開発者がシームレスに作業できます。
```

### Block 7 (line 23)

```
   :alt: フォークとクローンの関係を示す図
```

### Block 8 (line 25)

```
   フォークとクローンの関係。クローンはローカルのラップトップ上に存在し、フォークは GitHub サーバー上に存在します。
```

### Block 9 (line 27)

```
ブランチ戦略
```

### Block 10 (line 30)

```
`ブランチ <https://docs.github.com/en/get-started/learning-about-github/github-glossary#branch>`__は、他の開発ラインから独立した一連の`コミット <https://docs.github.com/en/get-started/learning-about-github/github-glossary#commit>`__であり、通常はリポジトリの新機能を開発するために使用されます。FtcRobotController リポジトリとそのフォークおよびクローンのデフォルトブランチは、`master <https://docs.github.com/en/get-started/learning-about-github/github-glossary#master>`__ です（ただし、GitHub で作成されたすべての新しいリポジトリでは、デフォルトブランチは `main <https://docs.github.com/en/get-started/learning-about-github/github-glossary#main>`__ と呼ばれます）。ブランチを賢明に使用することで、変更を分離し、デフォルトブランチをクリーンに保ち、「本番環境対応」と見なされたソフトウェアから独立して機能開発を反復するためのスペースを提供することにより、開発者が共通のソフトウェアセットで協力することを支援できます。
```

### Block 11 (line 34)

```
   :alt: 1つのブランチ
```

### Block 12 (line 36)

```
   master というデフォルト名を持つ単一のブランチ
```

### Block 13 (line 38)

```
各円は、ブランチへのコミットを表します。ブランチの名前は常に最新のコミットを指しており、これは `HEAD <https://docs.github.com/en/get-started/learning-about-github/github-glossary#head>`__ としても知られています。多くのブランチが存在する場合でも、HEAD は1つしかなく、`デタッチド状態 <https://git-scm.com/docs/git-checkout#_detached_head>`__ でない限り、常に現在チェックアウトされているブランチの最新のコミットを指します。他のすべてのコミットは、その直接の親を指します。
```

### Block 14 (line 40)

```
コミットは、ある時点でのワークスペース全体の `スナップショット <https://docs.github.com/en/get-started/learning-about-github/github-glossary#snapshot>`__ です。Git は `差分 <https://docs.github.com/en/get-started/learning-about-github/github-glossary#diff>`__ を保存しません。ファイルに変更を加え、変更されたファイルで新しいコミットを作成すると、変更されたファイル全体がコミットに保存されます。ファイルの不必要な重複を避けるために、リポジトリが3つのファイルで構成されており、1つが変更され、他の2つが変更されていない場合、スナップショットは変更されていないデータを含むのではなく、変更されていないファイルを指すだけです。
```

### Block 15 (line 42)

```
各コミットには親があり、これにより git は異なるブランチからのコミットの到達可能性を判断できます。また、2つのブランチの共通祖先コミットを判断することもでき、これはブランチをマージする際に重要です。詳細については後述します。
```

### Block 16 (line 44)

```
では、ブランチとは何でしょうか？ブランチは、単にコミットへの名前付きポインタです。ブランチが作成されると、git に名前を作成し、それをコミットに向けるように指示するだけです。ブランチ上にいるということは、新しいコミットを追加すると、git がブランチ名を新しいコミットに移動し、新しいコミットの親は、ブランチ名が以前指していたコミットになることを意味します。これにより親から独立した開発ラインが作成されるため、開発者は他のチームメンバーの作業を妨げることなく、実験し、変更を加え、新機能を開発できます。開発者がブランチが共有できるほど安定していると判断したら、ブランチを親にマージバックできます。
```

### Block 17 (line 48)

```
   :alt: 2つのブランチ
```

### Block 18 (line 50)

```
   同じコミットを指す2つのブランチ。
```

### Block 19 (line 52)

```
ブランチを作成した直後、新しいブランチ名は、新しいブランチが作成されたブランチの最新のコミットを単に指します。今、そのブランチに新しいコミットを作成すると想像してください。
```

### Block 20 (line 56)

```
   :alt: 2つのブランチ
```

### Block 21 (line 58)

```
   機能ブランチの新しいコミット。
```

### Block 22 (line 60)

```
新しいコミットにより、機能ブランチの名前ポインタが新しいコミットに移動した一方で、master ブランチの名前ポインタは以前のコミットに留まっていますが、新しいコミットの親は master の名前ポインタが指すコミットであることに注意してください。master ブランチに新しいコミットが追加されると、新しいコミットの親も master が指すコミットであり、これにより独立した開発ラインが作成されます。
```

### Block 23 (line 64)

```
   :alt: 独立した開発ライン
```

### Block 24 (line 66)

```
   2つの独立した開発ライン。
```

### Block 25 (line 68)

```
最終的には、通常、その機能ブランチを master ブランチで表されるメイン開発ラインにマージバックしたいと考えます。あるブランチを別のブランチにマージすると、git はブランチの祖先コミットをトラバースして、共通の`祖先 <https://stackoverflow.com/questions/55203122/what-do-people-mean-when-they-say-ancestor-with-regards-to-git>`__を見つけます。次に、共通の祖先から各ブランチの先頭までに何が変更されたかを判断し、それらの変更を*マージコミット*と呼ばれる新しいコミットに適用します。このプロセスの結果として、マージコミットには2つの親が存在します。
```

### Block 26 (line 72)

```
   :alt: マージコミットのデモンストレーション
```

### Block 27 (line 74)

```
   機能ブランチを master ブランチにマージバックする。
```

### Block 28 (line 76)

```
上記のように、機能ブランチはまだ存在しています。機能ブランチに追加された新しいコミットは、master ブランチから再び分岐します。ただし、機能の開発が完了した場合、ブランチを削除できます。ブランチの削除は、名前ポインタが削除されるだけです。ブランチの削除により、そのブランチで行われたコミットが削除されることはありません。ここでわかるように、機能ブランチ上にあったコミットは依然として存在し、マージブランチから正しい親を参照することでアクセスできます。
```

### Block 29 (line 78)

```
チームのフォークとクローンのデフォルトブランチが FIRST-Tech-Challenge/FtcRobotController のデフォルトブランチと一致していることを確認することは有用です。ただし、典型的な開発パターンでは、チーム開発者が機能ブランチからのマージまたは master への直接コミットのいずれかを介して、チームソフトウェアを master ブランチにコミットバックします。
```

### Block 30 (line 82)

```
   :alt: FTC master vs チーム master
```

### Block 31 (line 84)

```
   FIRST-Tech-Challenge/FtcRobotController の master と典型的なチームリポジトリの master の比較。
```

### Block 32 (line 86)

```
チームのコミットは青い円で表され、SDK アップデートを含むコミットは緑の円で表されます。紫色の円はマージコミットです。マージについては後述します。この例では、チームのコミットが SDK アップデート (1) と混在しており、2つのデフォルトブランチが一致しない状況を生み出しています。
```

### Block 33 (line 88)

```
   (1) 実際にはそうではないか、コミットの親子関係がどのように配置されているかによります。
   これは非常に単純化された見方ですが、論理的概念を示すには十分であり、単に `git log <https://www.atlassian.com/git/tutorials/git-log>`__ を実行した場合に得られる見方です。
   ブランチに関連するコミットで正確に何が起こっているかについての詳細でわかりやすい説明については、`このチュートリアルを参照してください <https://www.biteinteractive.com/picturing-git-conceptions-and-misconceptions/>`__。
```

### Block 34 (line 92)

```
これは完全に受け入れ可能であり、非常に一般的なブランチ管理戦略ですが、デフォルトブランチを分離して常に親と一致するようにすると、特定の利点が得られます。次の図は、master ブランチが FIRST-Tech-Challenge/FtcRobotController の master ブランチを追跡しているクローンを示しています。
```

### Block 35 (line 96)

```
   :alt: ブランチを同期させる
```

### Block 36 (line 98)

```
   チームリポジトリの master は常に FIRST-Tech-Challenge/FtcRobotController の master ブランチと一致します。
```

### Block 37 (line 100)

```
紫色のコミットは、v7.1 を competition ブランチにマージしたものです。この図では、v7.2 と v8.0 はマージされておらず、competition ブランチは SDK の v7.1 に対してビルドされます。
```

### Block 38 (line 102)

```
このモデルに従うということは、チームのリポジトリの master ブランチのコミット履歴が、常に FIRST-Tech-Challenge/FtcRobotController の master ブランチのコミット履歴と一致することを意味します。チームが競技で使用する予定のすべてのソフトウェアは、competition ブランチにマージされます。機能、新しいソフトウェア、実験などは、competition ブランチの子ブランチで作業され、master ブランチではなく competition ブランチにマージバックされます。チームクローンの master ブランチへの SDK アップデートは常に競合が発生せず、アップデートは competition ブランチへのマージとは独立して実行でき、開発への SDK アップデートのマージで問題が発生した場合、ブランチが一致しない master に直接アップデートをバックアウトする場合と比較して、復旧がより簡単になります。
```

### Block 39 (line 104)

```
ブランチの仕組みに関する詳細情報は、こちらを参照してください
`ブランチの使用 <https://www.atlassian.com/git/tutorials/using-branches>`__
```

### Block 40 (line 107)

```
はじめに（クイックスタートガイド）
```

### Block 41 (line 111)

```
   以下では、すべての操作がローカルリポジトリの master ブランチで行われることを前提としています。
```

### Block 42 (line 113)

```
#. `GitForWindows <https://gitforwindows.org/>`__ を入手してインストールします。このソフトウェアには、bash シェルとともに git クライアントが含まれています。以下のすべてのコマンドラインスニペットは、bash シェルを使用しており、git がパスに含まれていることを前提としています。GitForWindows は、Windows マシンにこれを提供する最も簡単な方法です。Mac には terminal と呼ばれる組み込みの bash シェルがありますが、git は個別にインストールする必要があります。
```

### Block 43 (line 115)

```
#. `FIRST-Tech-Challenge/FtcRobotController <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ リポジトリを GitHub 上のあなたのアカウントにフォークします。
```

### Block 44 (line 118)

```
      この手順には GitHub アカウントが必要であり、リポジトリをフォークするには GitHub にログインしている必要があります。
```

### Block 45 (line 123)

```
      :alt: リポジトリのフォーク
```

### Block 46 (line 125)

```
      GitHub リポジトリのフォーク。
```

### Block 47 (line 127)

```
   リポジトリのフォークは、上の画像に示されている ":octicon:`repo-forked;1em;sd-text-info` Fork" ボタンをクリックするだけで簡単に行えます。これにより「新しいフォークを作成」ページに移動し、「所有者」と「リポジトリ名」のフィールドが自動入力されます。説明を入力し（オプション）、「``master`` ブランチのみをコピー」オプションをチェックしたままにして、緑色の「フォークを作成」ボタンをクリックするだけです。
```

### Block 48 (line 129)

```
   作成されると、フォーク名を編集しない限り、新しいフォークは ``github.com/<ユーザー名>/FtcRobotController`` に配置されます。
```

### Block 49 (line 131)

```
#. フォークからローカルコンピューターにクローンします。下の画像ではアカウントが FIRST-Tech-Challenge になっていますが、フォーク後は、アカウントはチームアカウントになる必要があります。他のすべての点で、ユーザーインターフェースは同じです。
```

### Block 50 (line 136)

```
      :alt: リポジトリのクローン
```

### Block 51 (line 138)

```
      フォークされたリポジトリのクローン。
```

### Block 52 (line 140)

```
   FtcRobotController のフォークをクローンするには、次の手順に従います。
```

### Block 53 (line 142)

```
   #. 上の画像に示されている緑色の ":octicon:`code;1em;sd-text-info` Code" ボタンをクリックします。
   #. 「Local」と「HTTPS」のサブタブが選択されていることを確認します。
   #. ":octicon:`copy;1em;sd-text-info`" ボタンをクリックして、テキスト入力ボックス内の URL をコピーします。
   #. 適切なディレクトリで「Git Bash」シェルを開きます。Windows では、ファイルエクスプローラーを開き、リポジトリをクローンするディレクトリを見つけ、そのディレクトリフォルダを右クリックして「Git Bash here」を選択することで簡単に行えます。
   #. Git Bash シェル内で、次のコマンドを実行します
```

### Block 54 (line 150)

```
         git clone <コピーしたURL>
```

### Block 55 (line 152)

```
#. Git がリポジトリのクローンをダウンロードします。完了したら、コーディングを始めましょう...
```

### Block 56 (line 154)

```
#. これは、必要に応じて機能開発用のブランチを作成できるポイントです。ブランチを作成するには、次の `git-checkout <https://git-scm.com/docs/git-checkout>`__ コマンドを使用して、新しいブランチを作成して切り替えることができます。
```

### Block 57 (line 158)

```
      git checkout -b <ブランチ名>
```

### Block 58 (line 160)

```
   ``-b`` オプションを使用すると、``<ブランチ名>`` で指定された新しいブランチが作成され、自動的にそのブランチに切り替わります。``-b`` オプションを省略すると、既存のブランチがある場合、単にそのブランチに*切り替わります*。
```

### Block 59 (line 162)

```
ベストプラクティス
```

### Block 60 (line 165)

```
- リポジトリ内の FtcRobotController ディレクトリのソフトウェアに変更を加えないでください。FtcRobotController ディレクトリ内の何も変更しない場合、SDK のアップデートがはるかに簡単になります。
- 長期間存続するブランチの使用を制限してください。ブランチは機能を実装する必要があります。ブランチはマイルストーンを追跡すべきではありません。例えば、'league-meet-1' という名前のブランチはマイルストーンを追跡しています。ブランチがより小さな開発単位を追跡する方がはるかに良いです。'detect-target'、'drive-to-parking'、'drop-game-element' など。ソフトウェアをロボットが行うタスクに分解し、それらのタスクを実装するためにブランチを使用してください。これにより、共同開発がはるかに簡単になり、マージ時の変更セットがはるかに小さくなり、フェッチとマージがはるかに簡単になります。
- `git index <http://shafiul.github.io/gitbook/1_the_git_index.html>`__ をクリーンに保つようにしてください。これにより、フェッチとマージが簡単になります。``git status`` は、ここでの最良の友です。``git status`` を頻繁に使用して、ローカルワークスペースで何が変更されたかを確認してください。論理的なチャンクで頻繁にコミットして、最新の変更を簡単に確認できるようにしてください。
- 短く、意味のあるコミットメッセージを使用してください。コミットメッセージにスラング、不快な表現、または個人的なメッセージを使用しないでください。ソフトウェアを GitHub にプッシュすると、それらのコミットメッセージは公開されます。最終的にプロフェッショナルなソフトウェア開発者になることを計画しており、既存の GitHub アカウントを保持している場合、潜在的な雇用主はあなたのコミットメッセージを確認できます。ここでは慎重に進んでください。
```

### Block 61 (line 170)

```
フォークとローカルクローンの更新
```

### Block 62 (line 173)

```
SDK の更新には、ローカルクローンとフォークの両方に新しくリリースされたソフトウェアをプルすることが含まれます。これを行うには2つの方法があります。親から github 上のフォークに直接ソフトウェアをフェッチしてマージし、次にローカルにフェッチしてマージするか、親からローカルクローンにフェッチし、ローカルでマージしてからフォークにプッシュします。
```

### Block 63 (line 175)

```
この著者は後者を好みます。なぜなら、開発者がフォークにプッシュする前に新しいソフトウェアをテストする機会を与えるからです。また、GitHub の UI を介してではなく、ローカルでマージの競合を解決することができます。
```

### Block 64 (line 177)

```
最新のソフトウェアの取得
```

### Block 65 (line 180)

```
リポジトリを更新する方法を説明する際、多くの基本的なチュートリアルでは ``git pull`` コマンドを使用します。``git pull`` コマンドは実際には、ユーザーの背後で *fetch* と *merge* を実行しています。これで問題ない場合もありますが、 *フェッチ* と *マージ* の概念を独立した操作として理解することは有用です。問題が発生した場合、基礎となるメカニズムをよく理解していれば、その後の問題を修正できる可能性がはるかに高くなります。
```

### Block 66 (line 182)

```
リモート
```

### Block 67 (line 185)

```
Git は基本的に、リポジトリの多くのコピーがインターネット上、他の人のマシン上、企業のファイルサーバー上、またはその他多数の場所に浮遊している可能性があるという考えを中心に構築されています。そして、これらのリポジトリはリモートで相互にリンクできます。リモートリポジトリは、単にどこか他の場所でホストされているリポジトリのバージョンとして定義されます。前述の例では、FtcRobotController のフォークはローカルクローンのリモートです。
```

### Block 68 (line 189)

```
      :alt: origin という名前のリモート
```

### Block 69 (line 191)

```
      `origin` という名前のリモートとしての FtcRobotController の図。
```

### Block 70 (line 193)

```
リモートは git コマンドで参照でき、リポジトリには任意の数のリモートを持つことができます。クローンされたリポジトリのリモートのデフォルト名は 'origin' です。フォークの親を追跡するリモートの慣習的な名前は 'upstream' です。
```

### Block 71 (line 197)

```
      :alt: 2つのリモートを持つリポジトリ
```

### Block 72 (line 199)

```
      2つのリモートを持つローカルリポジトリ。
```

### Block 73 (line 201)

```
特定のリポジトリに対して確立されているリモートを確認するには
```

### Block 74 (line 207)

```
チームのフォークの親をローカルクローンのリモートとして追加するには
```

### Block 75 (line 214)

```
   FIRST Tech Challenge FtcRobotController リポジトリをローカルクローンの upstream リモートとして設定すると、エイリアス名 'upstream' を使用して FIRST-Tech-Challenge/FtcRobotController からローカルクローンに変更をフェッチできます。これは非常に強力です。
   なぜこれが重要なのかがすぐにわからない場合は、上記の ``フォークとローカルクローンの更新`` というヘッダーの下の2つの段落を再度お読みください。
```

### Block 76 (line 217)

```
**このチュートリアルの残りの部分では、ローカルクローンに upstream として FIRST-Tech-Challenge/FtcRobotController を追加したことを前提としています。**
```

### Block 77 (line 219)

```
フェッチ
```

### Block 78 (line 222)

```
フェッチは、リモートリポジトリからソフトウェアの変更をダウンロードするプロセスです。フェッチは、フェッチ先のリポジトリ内の既存のソフトウェアを**変更しない** ことに特に注意してください。git はローカルリポジトリ内の変更を分離します。
```

### Block 79 (line 224)

```
チームで作業していて、チームメイトが FtcRobotController フォークにソフトウェアをプッシュした場合、次のコマンドを実行してそのソフトウェアをローカルクローンにフェッチできます
```

### Block 80 (line 230)

```
これにより、origin という名前のリモート上のすべてのブランチで、ローカルリポジトリに存在しない変更がダウンロードされます。
```

### Block 81 (line 234)

```
      :alt: origin からの変更のフェッチ
```

### Block 82 (line 236)

```
      origin からの変更のフェッチ。
```

### Block 83 (line 238)

```
マージ
```

### Block 84 (line 241)

```
マージは、フェッチされたソフトウェアをブランチ（最も一般的にはリポジトリの現在のブランチ）にマージするプロセスです。マージは、物事が最も混乱しやすい場所です。ただし、リモート master からローカル master に単純にマージしており、ローカル master が常にリモートを追跡している場合、マージはスムーズに進むはずです。
```

### Block 85 (line 245)

```
      :alt: フェッチされた変更のマージ
```

### Block 86 (line 247)

```
      origin リポジトリからフェッチされた変更のマージ。
```

### Block 87 (line 249)

```
``master`` ブランチにいることを確認し、次のコマンドを実行します。
```

### Block 88 (line 255)

```
この操作を実行するときは、``master`` ブランチが*クリーン*である必要があります（つまり、``master`` ブランチで``git status`` を実行したときに、変更されているがコミットされていないファイルが表示されない）。チームメンバーは、``master`` ブランチではなく、機能ブランチで開発作業を行う必要があります。
```

### Block 89 (line 257)

```
競合
```

### Block 90 (line 260)

```
競合、または「特定のコードに対して複数の変更が保留されている場合に何が起こるか」。`Git マージの競合 <https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts>`__ に関するこの優れたチュートリアルを読むのが最善です。
マージの競合はチームで作業する際の通常の一部であり、経験を積むことによってのみ、競合を効果的に管理する方法を学ぶことができます。常に忍耐強く、プロセスに深い敬意を払ってアプローチしてください。
```

### Block 91 (line 263)

```
SDK を最新バージョンに更新する
```

### Block 92 (line 267)

```
   ``git remote -v`` を使用して、クローンに upstream がリモートとして設定されていることを確認してください。設定されていない場合は、「リモート」セクションを再度確認して、クローンの upstream リモートに FtcRobotController リポジトリを追加してください。
```

### Block 93 (line 269)

```
SDK から更新するには、チームフォークの親である upstream、FIRST-Tech-Challenge/FtcRobotController からフェッチし、次にマージして origin にプッシュすることで更新を完了します。
```

### Block 94 (line 273)

```
      :alt: upstream からの変更のフェッチ
```

### Block 95 (line 275)

```
      upstream リポジトリからの変更のフェッチ。
```

### Block 96 (line 277)

```
origin からではなく upstream からフェッチします。これにより、ローカルクローンにまだ存在しないコミットがコピーされます。上の図では、それは v8.0 コミットです。ローカルの master は変更されません。まだ v7.2 コミットを指しており、それを表しています。コミットはある時点でのワークスペースの完全なスナップショットであるため、ワークスペースでは何も変更されませんが、リポジトリには upstream/master というブランチ名の新しいコミットがあります。
```

### Block 97 (line 285)

```
      :alt: リモート
```

### Block 98 (line 287)

```
      upstream リポジトリからフェッチされた変更のマージ。
```

### Block 99 (line 289)

```
フェッチした後、upstream/master ブランチを master にマージします。ローカルの master が upstream の master と一致している場合、マージは master ブランチラベルを upstream/master が指しているコミットに移動するだけの簡単なものです。これは早送りマージと呼ばれます。そして、コミットはある時点でのワークスペースの完全なスナップショットであるため、ローカルワークスペースには v8.0 で表されるスナップショットが含まれるようになります。
```

### Block 100 (line 297)

```
      :alt: フェッチされた変更のプッシュ
```

### Block 101 (line 299)

```
      フェッチおよびマージされた変更をチームフォークにプッシュバック。
```

### Block 102 (line 301)

```
upstream/master をローカルクローンの master ブランチにマージしたら、それらの変更を GitHub にプッシュして、GitHub クローンが upstream リポジトリを反映するようにします。
```

### Block 103 (line 307)

```
機能ブランチで作業していて、その機能ブランチに新しい SDK の変更を取り込みたい場合は、ブランチをチェックアウトしてマージコマンドを実行することで、master からブランチにマージします。これは、マージの競合が発生する可能性が最も高い場所であり、事態が複雑になる可能性があります。
```

### Block 104 (line 311)

```
      $ git checkout <機能ブランチ>
```

### Block 105 (line 315)

```
SDK を以前のバージョンにダウングレードする
```

### Block 106 (line 318)

```
通常、ローカルリポジトリの作業ブランチ（master であろうと competition ブランチであろうと）は、最終的に SDK アップデートコミットと混在した一連のチームコミットを含むようになります。このシナリオでは、チームはすべてのチームコミットもロールバックせずに、単に以前の SDK バージョンにロールバックすることはできません。次の図を考えてみましょう。
```

### Block 107 (line 322)

```
      :alt: サンプルリポジトリ
```

### Block 108 (line 324)

```
      チームコミットと SDK アップデートコミットの両方を含むリポジトリ。
```

### Block 109 (line 326)

```
M7.2 でブランチを単に切り取ると、3つの青いチームコミットが失われます。チームの作業を保持するために、代わりに 8.0 コミットを元に戻す新しいマージコミットを作成します。M8.0 などのマージコミットは元に戻さないでください。マージコミット自体には、マージされた2つのブランチの分岐を表す作業が含まれている可能性があります。これはあなたが望むものではありません。新しい（古い）SDK バージョンを表すマージコミットの親を元に戻したいのです。
```

### Block 110 (line 328)

```
タグに関する短い余談
```

### Block 111 (line 331)

```
タグは、ブランチポインタや HEAD とは異なり、決して移動しないコミットへの名前付きポインタです。コミットはワークスペース全体のある時点でのスナップショットであるため、これにより開発者はある時点を不変の方法で*タグ付け*できます。
*FIRST* は、標準的な`セマンティックバージョニング <https://semver.org/>`__ 命名スキームを通じて SDK バージョンを追跡するためにタグを使用します。新しい SDK バージョンがリリースされると、FTC エンジニアリングチームはリリース候補ブランチを FIRST-Tech-Challenge/FtcRobotController にプッシュし、次にそのブランチを master にマージします。これにより、すべての良いものが含まれる新しい SDK バージョンコミットと、候補ブランチから master へのマージを表すマージコミットの2つのコミットが作成されます。その後、リリースが正式にカットされ、マージコミットにタグが作成されます。
```

### Block 112 (line 334)

```
リモートからのタグは、クローン時にリポジトリに自動的にコピーされません。タグを取得するには、次を実行します。
```

### Block 113 (line 340)

```
--all オプションはすべてのリモートから一度にフェッチし、--tags オプションは git にタグをフェッチするよう指示します。
タグは常にセマンティックバージョニングルールに従います。例: v7.0、v7.1、v7.2、v8.0 など。
```

### Block 114 (line 343)

```
`^ 構文 <https://medium.com/@gabicle/git-ancestry-references-explained-bd3a84a0b821>`__ を使用すると、コミットの親を参照でき、タグ名に適用できます。tag^ は、タグが指すコミットの直接の親です。マージコミットなどの複数の親を持つコミットの場合、数字を適用して特定の親を参照できます。
tag^1 は tag^ と同じで、コミットの最初の親です。tag^2 はコミットの2番目の親です。
```

### Block 115 (line 346)

```
SDK アップデートの逆のマージ
```

### Block 116 (line 349)

```
下の図は、v8.0 タグが v8.0 マージコミットを指しており、v8.0 の親への参照も示しています。
```

### Block 117 (line 353)

```
      :alt: タグ
```

### Block 118 (line 355)

```
      v8.0 マージコミットを指す v8.0 タグ。
```

### Block 119 (line 359)

```
Git はコミットを削除しない（いくつかの例外を除いて）ことを覚えておいてください。したがって、コミットを元に戻すには、元に戻したいコミット*から*の逆のコミットを作成する必要があります。そして、元に戻したいすべてのバージョンについて、逆の順序でこれを行う必要があります。以下のコマンドのターゲットは、元に戻したいバージョンのタグであり、元に戻す先のバージョンのタグではありません。
```

### Block 120 (line 363)

```
      :alt: 元に戻すことのデモンストレーション
```

### Block 121 (line 365)

```
      元に戻した結果 - v8.0 から v7.2 への元に戻しを表す新しいマージコミット。
```

### Block 122 (line 367)

```
マージコミットには2つの親があり、SDK バージョンコミットを参照したいため、ロールバックしたいタグ名を使用し、^2 を追加します。例えば、v8.0 をロールバックし、SDK が v7.2 に対してコンパイルされるようにするには、次を使用します。
```

### Block 123 (line 373)

```
-Xtheirs オプションは、「競合がある場合は、v8.0^2 側からソフトウェアを自動的に取得する」という便利なオプションです。
```

### Block 124 (line 376)

```
   `こちら <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__ にあります）、v8.1.1 を元に戻し、次に v8.1 を元に戻す必要があります。この順序に従わないと、v8.1 と重複しない v8.1.1 の変更がワークスペースに残り、それは望ましくありません。
```

### Block 125 (line 378)

```
まとめ
```

### Block 126 (line 381)

```
すべてのコマンドは、ローカルクローンのルートディレクトリから実行されることを前提としています。また、ローカルの master ブランチにチームコードをコミットするのではなく、competition ブランチで作業していることを前提としています。
```

### Block 127 (line 383)

```
FIRST-Tech-Challenge/FtcRobotController をリモートとして追加
```

### Block 128 (line 390)

```
最新の SDK バージョンに更新
```


## programming_resources/tutorial_specific/android_studio/installing_android_studio/Installing-Android-Studio.rst

### Block 1 (line 1)

```
**Android Studio** のインストール :bdg-success:`AS`
```

### Block 2 (line 4)

```
**Android** Developer ウェブサイト
```

### Block 3 (line 7)

```
**Android Studio** は Google によって無料で配布されており、**Android Studio** ソフトウェアのインストールと使用に関する最新のリファレンスは、**Android** Developer ウェブサイトで見つけることができます：
```

### Block 4 (line 11)

```
**Android Studio** は、Windows、MacOS、Linux オペレーティングシステムで利用可能です。
```

### Block 5 (line 13)

```
システム要件
```

### Block 6 (line 16)

```
**Android Studio** をダウンロードしてインストールする前に、まず**Android** Developer のウェブサイトでシステム要件のリストを確認し、システムが最小要件のリストを満たしていることを確認してください：
```

### Block 7 (line 25)

```
   **Android Studio Ladybug** の導入により、**Android Studio** にパッケージ化されている JDK は FtcRobotController ワークスペースと互換性がありません。**Android Studio Ladybug** をインストールまたは既存のインストールを更新する場合は、JDK 17 を別途インストールする必要があります。
```

### Block 8 (line 27)

```
   **Android Studio Ladybug** を使用して FtcRobotController ワークスペースを初めてロードすると、Gradle 同期中にエラーが表示され、**Android Studio** が Gradle をアップグレードすることを推奨します。Gradle をアップグレードしないでください。
```

### Block 9 (line 29)

```
   詳細な手順については、Configuring を参照してください。
```

### Block 10 (line 33)

```
**Android Studio** のダウンロードとインストール
```

### Block 11 (line 36)

```
ラップトップが最小システム要件を満たしていることを確認したら、**Android**Developer のウェブサイトにアクセスして**Android Studio** をダウンロードおよびインストールできます：
```

### Block 12 (line 40)

```
白い「Download Android Studio <latest version>」ボタンをクリックして、ダウンロードプロセスを開始します。
```

### Block 13 (line 48)

```
ライセンス条項に同意してから、**Android** Developer ウェブページの白い「Download Android Studio <latest version> for <operating system>」ボタンを押してソフトウェアをダウンロードします。
```

### Block 14 (line 50)

```
セットアップパッケージがダウンロードされたら、アプリケーションを起動し、画面上の指示に従って **Android Studio** をインストールします。
```


## programming_resources/tutorial_specific/android_studio/using_sensors/Using-Sensors-(Android-Studio).rst

### Block 1 (line 1)

```
センサーの使用 :bdg-success:`AS`
```

### Block 2 (line 4)

```
カラー距離センサー
```

### Block 3 (line 7)

```
センサーは、**Robot Controller** がその環境に関する情報を取得できるようにするデバイスです。この例では、**REV Robotics** のカラー距離センサーを使用して、範囲（物体からの距離）情報を**Driver Station** に表示します。
```

### Block 4 (line 9)

```
カラー距離センサーは、反射光を使用してセンサーからターゲット物体までの距離を測定します。このセンサーは、近距離（最大5インチ程度）を適切な精度で測定できます。このドキュメントが最後に編集された時点では、**REV** カラー距離センサーは約2インチ（5cm）で飽和することに注意してください。これは、2インチ以下の距離では、センサーが約2インチに等しい測定距離を返すことを意味します。
```

### Block 5 (line 11)

```
距離情報（センチメートル単位）を **Driver Station** に送信するテレメトリーステートメントを追加するように、**Op Mode** を変更します。
```

### Block 6 (line 22)

```
**Op Mode** を変更した後、更新された**Robot Controller** アプリをビルドしてインストールし、**Op Mode** を実行して、**Driver Station** に距離が表示されることを確認します。距離が「NaN」（「Not a Number」の略）と表示される場合は、おそらくセンサーがターゲットから遠すぎる（反射がゼロ）ことを意味します。また、センサーは約5cmで飽和することに注意してください。
```

### Block 7 (line 24)

```
タッチセンサー
```

### Block 8 (line 27)

```
**REV Robotics** のタッチセンサーは、**Control Hub** または**Expansion Hub** のデジタルポートに接続できます。タッチセンサーは、押されていない場合はHIGH（TRUEを返す）です。押されると、LOW（FALSEを返す）になります。
```

### Block 9 (line 34)

```
**Control Hub** または**Expansion Hub** のデジタルポートには、1つのポートあたり2つのデジタルピンが含まれています。4線式JSTケーブルを使用して**REV Robotics** のタッチセンサーを**Control Hub** または**Expansion Hub** のデジタルポートに接続すると、タッチセンサーはポート内の2つのデジタルピンの2番目に配線されます。4線式ケーブルの最初のデジタルピンは接続されないままになります。
```

### Block 10 (line 36)

```
たとえば、タッチセンサーを **Control Hub** または**Expansion Hub** の「0,1」デジタルポートに接続する場合、タッチセンサーはポートの2番目のピン（「1」とラベル付けされている）に接続されます。最初のピン（「0」とラベル付けされている）は接続されないままになります。
```

### Block 11 (line 38)

```
デジタルチャンネルを入力モードに設定するために、**waitForStart** コマンドの前に発生する**Op Mode** のコードを変更します。
```

### Block 12 (line 50)

```
また、whileループ内のコードを変更して、デジタル入力チャンネルの状態をチェックするif-else文を追加します。チャンネルがLOW（false）の場合、タッチセンサーボタンが押されており、グラウンドにLOWで引かれています。それ以外の場合は、タッチセンサーボタンは押されていません。
```

### Block 13 (line 66)

```
更新された **Robot Controller** アプリをビルドしてインストールし、**Op Mode** を再初期化して再起動します。**Op Mode** は、ボタンの状態（「PRESSED」または「NOT PRESSED」）を表示するようになります。
```


## programming_resources/tutorial_specific/blocks/blocks_reference/Blocks-Reference-Material.rst

### Block 1 (line 1)

```
Blocks リファレンス資料 :bdg-warning:`Blocks`
```

### Block 2 (line 4)

```
**Blocks** リファレンスマニュアル
```

### Block 3 (line 7)

```
より複雑な **Op Mode** を作成するようになると、**FIRST Tech Challenge** ソフトウェア開発キット（**SDK** ）のより多くの機能を使用する必要が出てきます。Oregon Robotics Tournament & Outreach Program（ORTOP）のBruce Schafer氏は、**Blocks** プログラミングツールで利用可能なプログラミングブロックについて説明する有用なリファレンスドキュメントを作成しました：
```

### Block 4 (line 11)

```
サンプル Op Mode
```

### Block 5 (line 14)

```
**Blocks** プログラミングツールには、**FIRST Tech Challenge** 制御システムでさまざまなタスクを実行する方法を示す、組み込みのサンプル**Op Mode** がいくつか含まれています。新しいファイルを作成する際、Sampleドロップダウンリストコントロールを使用して、利用可能なサンプル**Op Mode** やテンプレートのリストを表示できます：
```

### Block 6 (line 21)

```
テクノロジーフォーラム
```

### Block 7 (line 24)

```
登録済みチームは、**FIRST Tech Challenge** コミュニティフォーラムでユーザーアカウントを作成できます。チームはフォーラムを使用して質問し、**FIRST Tech Challenge** コミュニティからサポートを受けることができます。
```

### Block 8 (line 26)

```
テクノロジーフォーラムは以下のアドレスにあります：
```

### Block 9 (line 30)

```
**REV Robotics Control Hub** ドキュメント（英語）
```

### Block 10 (line 35)

```
**REV Robotics Expansion Hub** ドキュメント（英語）
```

### Block 11 (line 40)

```
**REV Robotics Driver Hub** ドキュメント（英語）
```


## programming_resources/tutorial_specific/blocks/controlling_a_servo/Controlling-a-Servo-(Blocks).rst

### Block 1 (line 1)

```
サーボの制御 :bdg-warning:`Blocks`
```

### Block 2 (line 4)

```
:doc:`Blocks で Op Mode を作成する <../creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks>` セクションでは、**Blocks** プログラミングツールを使用して12V DCモーターを制御する**Op Mode** を作成する方法を学びました。このセクションでは、サーボモーターを制御する**Op Mode** を作成する方法を学びます。
```

### Block 3 (line 6)

```
サーボモーターとは？
```

### Block 4 (line 9)

```
サーボモーターは、精密な動きのために設計された特殊なタイプのモーターです。典型的なサーボモーターは、動作範囲が制限されています。
```

### Block 5 (line 11)

```
以下の図では、「標準スケール」の180度サーボが示されています。このタイプのサーボは、ホビイストや **FIRST Tech Challenge** チームに人気があります。このサーボモーターは、シャフトを180度の範囲で回転させることができます。サーボコントローラーとして知られる電子モジュールを使用すると、サーボモーターを特定の位置に移動させる**Op Mode** を作成できます。モーターがこのターゲット位置に到達すると、サーボのシャフトに外力が加えられても、その位置を保持します。
```

### Block 6 (line 18)

```
サーボモーターは、精密な動きをしたい場合に便利です（たとえば、ターゲットを探すためにセンサーでエリアをスイープしたり、遠隔操作の飛行機の制御面を動かしたりする場合など）。
```

### Block 7 (line 20)

```
サーボを制御するための Op Mode の変更
```

### Block 8 (line 23)

```
サーボモーターを制御するために必要なロジックを追加するために、**Op Mode** を変更しましょう。この例では、Logitech F310ゲームパッドのボタンを使用してサーボモーターの位置を制御します。
```

### Block 9 (line 25)

```
典型的なサーボでは、サーボのターゲット位置を指定できます。サーボはモーターシャフトを回転させてターゲット位置に移動し、その位置を乱そうとする中程度の力が加えられても、その位置を維持します。
```

### Block 10 (line 27)

```
**Blocks** のProgram & Manageサーバーでは、サーボのターゲット位置を0から1の範囲で指定できます。ターゲット位置0は0度の回転に対応し、ターゲット位置1は典型的なサーボモーターの180度の回転に対応します。
```

### Block 11 (line 34)

```
この例では、F310コントローラーの右側にあるカラーボタンを使用してサーボの位置を制御します。最初に、**Op Mode** はサーボを中間位置（180度範囲の90度）に移動します。黄色の「Y」ボタンを押すと、サーボが0度の位置に移動します。青色の「X」ボタンまたは赤色の「B」ボタンを押すと、サーボが90度の位置に移動します。緑色の「A」ボタンを押すと、サーボが180度の位置に移動します。
```

### Block 12 (line 42)

```
サーボモーターを制御するための Op Mode の変更手順
```

### Block 13 (line 45)

```
1. ラップトップが **Robot Controller** のProgram & Manage Wi-Fiネットワークにまだ接続されていることを確認します。
```

### Block 14 (line 47)

```
2. 「MyFIRSTOpMode」が編集用に開かれていることを確認します。開かれていない場合は、ラップトップのブラウザウィンドウの左上隅にある **FIRST** ロゴをクリックします。これにより、メインの**Blocks** 開発ツールプロジェクト画面に移動します。
```

### Block 15 (line 54)

```
   まだ開かれていない場合は、「MyFIRSTOpMode」プロジェクトをクリックして編集用に開きます。
```

### Block 16 (line 56)

```
3. 画面の左側にある「Actuators」カテゴリをクリックし、「Servos」サブカテゴリを探します。
```

### Block 17 (line 63)

```
4. 利用可能なServoブロックのリストから「set **servoTest.Position** to」ブロックを選択します。
```

### Block 18 (line 70)

```
5. 「set **servoTest.Position** to」ブロックを「Put initialization blocks here.」と書かれたコメントブロックのすぐ下にドラッグします。ブロックは所定の位置にクリックして収まるはずです。
```

### Block 19 (line 77)

```
6. 数値ブロック「0」をクリックし、ブロックの値を「0.5」に変更します。
```

### Block 20 (line 84)

```
   ユーザーがこの **Op Mode** を選択すると、サーボ位置は最初に中間点（90度の位置）に設定されます。
```

### Block 21 (line 86)

```
7. プログラミングブロックの「Logic」カテゴリをクリックし、利用可能なブロックのリストから「if do」ブロックを選択します。ブロックを「Put loop blocks here.」と書かれたコメントブロックの直後の位置にドラッグします。
```

### Block 22 (line 93)

```
   ブロックは所定の位置にクリックして収まるはずです。
```

### Block 23 (line 95)

```
8. プログラミングブロックの「Gamepad」カテゴリをクリックし、利用可能なブロックのリストから「**gamepad1.Y**」ブロックを選択します。
```

### Block 24 (line 102)

```
   注：このブロックはブロックのリストの下部にあります。このブロックを選択する前に、リストの最後までスクロールダウンする必要がある場合があります。
```

### Block 25 (line 104)

```
9. 「**gamepad1.Y**」ブロックを「if do」ブロックの右側にドラッグします。ブロックは所定の位置にクリックして収まるはずです。
```

### Block 26 (line 111)

```
   「if do」ブロックは、**gamepad1.Y** 値の状態をテスト条件として使用します。「Y」ボタンが押されると、ブロックの「do」部分内のステートメントが実行されます。
```

### Block 27 (line 113)

```
10. 画面の左側にある「Actuators」カテゴリをクリックし、「Servos」サブカテゴリを探します。
```

### Block 28 (line 120)

```
11. 利用可能なServoブロックのリストから「set **servoTest.Position** to」ブロックを選択します。
```

### Block 29 (line 127)

```
12. 「set **servoTest.Position** to」ブロックを「if do」ブロックの「do」部分にスナップするようにドラッグします。
```

### Block 30 (line 134)

```
   ゲームパッド#1で「Y」ボタンが押されると、**Op Mode** はサーボの位置を0度の位置に移動します。
```

### Block 31 (line 136)

```
13. 「if do」ブロックの青と白のSettingsアイコンをクリックします。これにより、「if do」ブロックを変更できるポップアップメニューが表示されます。
```

### Block 32 (line 143)

```
14. ポップアップメニューの左側から「else if」ブロックをドラッグし、「if」ブロックの下に所定の位置にスナップします。
```

### Block 33 (line 150)

```
   2番目の「else if」ブロックを左側からドラッグし、最初の「else if」ブロックの下の右側に所定の位置にスナップします。
```

### Block 34 (line 152)

```
15. Settingsアイコンをクリックして、「if do」ブロックのポップアップメニューを非表示にします。「if do」ブロックに2つの「else if」テスト条件が追加されているはずです。
```

### Block 35 (line 159)

```
16. 「Logic」カテゴリをクリックし、論理「and」ブロックを選択します。
```

### Block 36 (line 166)

```
17. 「and」ブロックを最初の「else if」ブロックのテスト条件として所定の位置にクリックするようにドラッグします。
```

### Block 37 (line 173)

```
18. 「and」という単語をクリックし、ポップアップメニューから「or」を選択して、ブロックを論理「or」ブロックに変更します。
```

### Block 38 (line 180)

```
19. 「Gamepad」カテゴリをクリックし、「**gamepad1.X**」ブロックを選択します。ブロックを論理「or」ブロックの最初のテスト条件として所定の位置にクリックするようにドラッグします。
```

### Block 39 (line 187)

```
20. 「Gamepad」カテゴリをクリックし、「**gamepad1.B**」ブロックを選択します。ブロックを論理「or」ブロックの2番目のテスト条件として所定の位置にクリックするようにドラッグします。
```

### Block 40 (line 194)

```
21. 「set **servoTest.Position** to」ブロックを選択し、最初の「else-if」ブロックの「do」句に配置します。
```

### Block 41 (line 201)

```
22. 数値「0」をハイライトし、「0.5」に変更します。この変更により、ユーザーがゲームパッド#1で「X」ボタンまたは「B」ボタンを押すと、**Op Mode** はサーボを中間（90度）の位置に移動します。
```

### Block 42 (line 208)

```
23. 2番目の「else if」ブロックのテスト条件として「**gamepad1.A**」ブロックを使用します。「set**servoTest.position** to」ブロックを2番目の「else if」ブロックの「do」句にドラッグし、サーボの位置が値1に設定されるように数値を変更します。
```

### Block 43 (line 215)

```
   この句では、#1ゲームパッドで「A」ボタンが押されると、**Op Mode** はサーボを180度の位置に移動します。
```

### Block 44 (line 217)

```
24. 「call **Telemetry.update**」ブロックの前に「call**telemetry.addData**」ブロック（数値版）を挿入します。キーフィールドを「Servo Position」に変更し、数値フィールドに「**servoTest.Position**」ブロックを挿入します。
```

### Block 45 (line 224)

```
   このブロックのセットは、**Op Mode** の実行中に現在のサーボ位置の値を**DRIVER STATION** に送信します。
```

### Block 46 (line 226)

```
25. **Op Mode** を保存し、**Robot Controller** に正常に保存されたことを確認します。
```

### Block 47 (line 233)

```
26. :doc:`Op Mode の実行 <../running_op_modes/Running-Your-Op-Mode>` セクションで説明されている手順に従って、更新された **Op Mode** を実行します。また、**Op Mode** を実行する前に、ゲームパッドがユーザー#1として指定されていることを確認してください。
```

### Block 48 (line 240)

```
   これで、カラーボタンでサーボの位置を制御できるようになります。サーボの位置は **DRIVER STATION** に表示されるはずです。
```


## programming_resources/tutorial_specific/blocks/creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks.rst

### Block 1 (line 1)

```
Op Mode の作成 :bdg-warning:`Blocks`
```

### Block 2 (line 5)

```
Op Mode とは？
```

### Block 3 (line 8)

```
典型的な **FIRST** Tech Challenge のマッチでは、チームのロボットは得点を獲得するために
さまざまなタスクを実行する必要があります。例えば、チームは競技フロアの白線をロボットが
追従し、マッチ中に自律的にゲーム要素をゴールに入れることを望むかもしれません。チームは
ロボットの動作を指定するために **op modes** （「operational modes」の略）と呼ばれる
プログラムを作成します。これらの **op modes** は、**DRIVER STATION** で選択された後、
**Robot Controller** 上で実行されます。
```

### Block 4 (line 15)

```
**FIRST**Tech Challenge に参加するチームは、独自の**op modes** を作成するために
使用できるさまざまなプログラミングツールを利用できます。このセクションでは、
**Blocks Programming Tool** を使用してロボット用の**op mode** を作成する方法を説明します。
```

### Block 5 (line 22)

```
**Blocks Programming Tool** は、**Robot Controller** によって提供されるユーザーフレンドリーな
プログラミングツールです。ユーザーはこのツールを使用してロボット用のカスタム **op modes** を
作成し、これらの **op modes** を**Robot Controller** に直接保存できます。ユーザーは
ジグソーパズル型のプログラミングブロックをデザイン「キャンバス」上にドラッグ＆ドロップし、
これらのブロックを配置して **op mode** のプログラムロジックを作成します。**Blocks Programming Tool** は
Google の Blockly ソフトウェアを利用しており、Google のサポートを受けて開発されました。
```

### Block 6 (line 34)

```
このセクションの例では、Windows ラップトップコンピューターを使用して **Robot Controller** に
接続します。この Windows ラップトップコンピューターには、**Blocks Programming Tool** に
アクセスするために使用される JavaScript 対応のウェブブラウザがインストールされています。
```

### Block 7 (line 43)

```
**Robot Controller** として**Control Hub** を使用している場合でも、**op mode** を作成および
編集するプロセスは同じです。
```

### Block 8 (line 51)

```
なお、Windows コンピューターの代わりに、Apple Mac ラップトップ、Apple iPad、Android タブレット、
または Chromebook などの代替デバイスを使用して **Blocks Programming Tool** にアクセスすることも
できます。ただし、このドキュメントに含まれる手順は、Windows ラップトップを使用していることを
前提としています。
```

### Block 9 (line 56)

```
また、このセクションでは、Android デバイスとロボットハードウェアのセットアップと構成が既に
完了していることを前提としています。また、ラップトップが **Robot Controller** の
Program & Manage ワイヤレスネットワークに正常に接続されていることも前提としています。
```

### Block 10 (line 60)

```
最初の Op Mode の作成
```

### Block 11 (line 63)

```
ラップトップが **Robot Controller** の Program & Manage ワイヤレスネットワークに正常に
接続できた場合、最初の **op mode** を作成する準備が整いました。このセクションでは、
**Blocks Programming Tool** を使用して、最初の**op mode** のプログラムロジックを作成します。
```

### Block 12 (line 67)

```
なお、最初の **op mode** の作成には約 10 分かかります。
```

### Block 13 (line 69)

```
最初の Op Mode の作成手順
```

### Block 14 (line 72)

```
1. ラップトップでウェブブラウザを起動し（**FIRST** では Google Chrome の使用を推奨）、
**Robot Controller** の Program & Manage 画面に表示されているウェブアドレスを確認します。
```

### Block 15 (line 89)

```
   このウェブアドレスをブラウザのアドレスフィールドに入力し、RETURN キーを押して Program & Manage ウェブサーバーに移動します。
```

### Block 16 (line 96)

```
2. ウェブブラウザがプログラミングモードサーバーに接続されていることを確認します。
プログラミングモードサーバーに正常に接続されている場合、Robot Controller Console が
表示されます。
```

### Block 17 (line 105)

```
3. Console の上部にある **Blocks** リンクをクリックして、メインの**Blocks** プログラミング画面に移動します。
```

### Block 18 (line 112)

```
   メインの Blocks Programming 画面は、新しい **op modes** を作成する場所です。また、**Robot Controller** 上の既存の Blocks Op Modes のリストを表示する画面でもあります。最初の**op mode** を作成して保存するまで、このリストは空です。
```

### Block 19 (line 119)

```
4. ブラウザウィンドウの左上隅に表示されている "Create New Op Mode" ボタンをクリックします。
```

### Block 20 (line 126)

```
   プロンプトが表示されたら、**op mode** の名前を指定し、"OK" をクリックして続行します。
```

### Block 21 (line 128)

```
5. 新しい **op mode** が作成されたことを確認します。ウェブブラウザのメイン画面に、
新しく作成された **op mode** が編集用に開かれているはずです。
```

### Block 22 (line 136)

```
   ブラウザ画面の左側には、カテゴリ別に分類されたプログラミングブロックのリストが表示されています。カテゴリをクリックすると、ブラウザに関連する利用可能なプログラミングブロックのリストが表示されます。
```

### Block 23 (line 138)

```
   画面の右側は、プログラミングブロックを配置して **op mode** のロジックを作成する場所です。
```

### Block 24 (line 141)

```
Op Mode の構造の確認
```

### Block 25 (line 144)

```
新しい **op mode** を作成すると、デザインキャンバス上に既にプログラミングブロックの
セットが配置されているはずです。これらのブロックは、作成する各新規 **op mode** に
自動的に含まれます。これらは、**op mode** の基本構造を作成します。
```

### Block 26 (line 153)

```
上図では、**op mode** のメイン本体は、上部に "to runOpMode" という文字が付いた
外側の紫色のブラケットによって定義されています。ヘルプのヒントが示すように、
この関数は、この **op mode** （この例では "MyFIRSTOpMode"）が**DRIVER STATION** から
選択されたときに実行されます。
```

### Block 27 (line 158)

```
**op mode** を、**Robot Controller** が実行するタスクのリストと考えると役立ちます。
**Robot Controller** は、このタスクのリストを順次処理します。ユーザーは、制御ループ
（while ループなど）を使用して、**op mode** 内の特定のタスクを**Robot Controller** に
繰り返し（または反復）させることもできます。
```

### Block 28 (line 168)

```
**op mode** をロボットへの命令リストと考えると、この命令セットは、チームメンバーが
この **Robot Controller** で利用可能な**op modes** のリストから "MyFIRSTOpMode" という
**op mode** を選択するたびに、ロボットによって実行されます。
```

### Block 29 (line 172)

```
疑問符（"?"）が付いた青いボタンをクリックすると、ヘルプテキストを非表示にできます。
この基本的な **op mode** のフローを見てみましょう。"Put initialization blocks here" という
文字が付いた青色のブロックはコメントです。コメントは、人間のユーザーのために **op mode** に
配置されます。ロボットは、**op mode** 内のコメントを無視します。
```

### Block 30 (line 182)

```
"Put initialization blocks here" コメントの後（および "call MyFIRSTOpMode.waitForStart"
ブロックの前）に配置されたプログラミングブロックは、ユーザーが **DRIVER STATION** で
**op mode** を最初に選択したときに実行されます。
```

### Block 31 (line 186)

```
**Robot Controller** が "call MyFIRSTOpMode.waitForStart" というラベルの付いたブロックに
到達すると、**DRIVER STATION** から Start コマンドを受信するまで停止して待機します。
Start コマンドは、ユーザーが **DRIVER STATION** の Start ボタンを押すまで送信されません。
"call MyFIRSTOpMode.waitForStart" ブロックの後のコードは、Start ボタンが押された後に
実行されます。
```

### Block 32 (line 197)

```
"call MyFIRSTOpMode.waitForStart" の後には、条件付き "if" ブロック
（"if call MyFIRSTOpMode.isActive"）があり、**op mode** がまだアクティブな場合
（つまり、停止コマンドが受信されていない場合）にのみ実行されます。
```

### Block 33 (line 206)

```
"Put run blocks here" コメントの後、"repeat while call MyFirstOpMode.opModeIsActive" という
ラベルの付いた緑色のブロックの前に配置されたブロックは、Start ボタンが押された後、
**Robot Controller** によって順次実行されます。
```

### Block 34 (line 210)

```
"repeat while call MyFirstOpMode.opModeIsActive" というラベルの付いた緑色のブロックは、
反復またはループ制御構造です。
```

### Block 35 (line 218)

```
この緑色の制御ブロックは、"call MyFIRSTOpMode.opModeIsActive" の条件が true である限り、
ブロックの "do" 部分にリストされているステップを実行します。これは、**op mode**
"MyFIRSTOpMode" が実行されている限り、ブロックの "do" 部分に含まれるステートメントが
繰り返し実行されることを意味します。ユーザーが Stop ボタンを押すと、
"call MyFIRSTOpMode.opModeIsActive" 句は true ではなくなり、"repeat while" ループは
繰り返しを停止します。
```

### Block 36 (line 225)

```
DC モーターの制御
```

### Block 37 (line 228)

```
このセクションでは、ゲームパッドで DC モーターを制御できるようにするブロックを
**op mode** に追加します。
```

### Block 38 (line 231)

```
なお、このタスクを完了するには約 15 分かかります。
```

### Block 39 (line 235)

```
まだ :doc:`構成ファイルを作成してアクティブ化していない </hardware_and_software_configuration/connecting_devices/index>` 場合は、
:doc:`このリンク </hardware_and_software_configuration/connecting_devices/index>` に従って実行してください。
構成ファイルを作成してアクティブ化した後、**op mode** を閉じて再度開くと、新しく構成された
デバイスのプログラミングブロックが表示されます。
```

### Block 40 (line 240)

```
DC モーターを制御するための Op Mode の変更手順
```

### Block 41 (line 243)

```
1. 画面の左側にある "Variables" というカテゴリをクリックして、**op mode** 内で
変数を作成および変更するために使用されるブロックコマンドのリストを表示します。
```

### Block 42 (line 251)

```
   "Create variable..." をクリックして、**op mode** のターゲットモーター出力を表す新しい変数を作成します。
```

### Block 43 (line 253)

```
2. プロンプトが表示されたら、新しい変数の名前（"tgtPower"）を入力します。
```

### Block 44 (line 260)

```
3. 新しい変数を作成すると、"Variables" ブロックカテゴリの下に追加の
プログラミングブロックが表示されます。
```

### Block 45 (line 268)

```
4. "set tgtPower to" プログラミングブロックをクリックし、マウスを使用して
"Put loop blocks here" コメントブロックの直後の位置にブロックをドラッグします。
```

### Block 46 (line 276)

```
   "set tgtPower to" ブロックは、正しい位置にスナップされます。
```

### Block 47 (line 278)

```
5. プログラミングブロックの "Gamepad" カテゴリをクリックし、利用可能な
ブロックのリストから "gamepad1.LeftStickY" ブロックを選択します。
```

### Block 48 (line 286)

```
   制御システムでは、最大 2 つのゲームパッドでロボットを制御できます。"gamepad1" を選択することで、ドライバー #1 として指定されたゲームパッドからの制御入力を使用するように **op mode** に指示しています。
```

### Block 49 (line 288)

```
6. "gamepad1.LeftStickY" ブロックをドラッグして、"set tgtPower to" ブロックの
右側にスナップするように配置します。このブロックセットは、継続的にループして
ゲームパッド #1 の左ジョイスティック（y 位置）の値を読み取り、変数 tgtPower を
左ジョイスティックの Y 値に設定します。
```

### Block 50 (line 298)

```
   F310 ゲームパッドの場合、ジョイスティックの Y 値は、ジョイスティックが最上位置にあるときは -1 から、最下位置にあるときは +1 までの範囲です。
```

### Block 51 (line 305)

```
   これは、例に示されているブロックの場合、左ジョイスティックを上に押すと、変数 tgtPower の値は -1 になることを意味します。
```

### Block 52 (line 307)

```
7. プログラミングブロックの "Math" カテゴリをクリックし、負の記号（"-"）を
選択します。
```

### Block 53 (line 315)

```
8. 負の記号（「否定演算子」とも呼ばれます）を "gamepad1.LeftStickY" ブロックの
左側にドラッグします。"set tgtPower to" ブロックの後、"gamepad1.LeftStickY"
ブロックの前にクリックして配置されます。
```

### Block 54 (line 324)

```
この変更により、左ジョイスティックが最上位置にある場合、変数 tgtPower は +1 に設定され、ジョイスティックが最下位置にある場合は -1 に設定されます。
```

### Block 55 (line 326)

```
9. ブロックの "Actuators" カテゴリをクリックします。次に、"DcMotor" カテゴリの
ブロックをクリックします。
```

### Block 56 (line 334)

```
10. "set motorTest.Power to 1" プログラミングブロックを選択します。
```

### Block 57 (line 341)

```
11. "set motorTest.Power to 1" ブロックをドラッグして、"set tgtPower to" ブロックの
すぐ下にスナップするように配置します。
```

### Block 58 (line 349)

```
12. "Variables" ブロックカテゴリをクリックし、"tgtPower" ブロックを選択します。
```

### Block 59 (line 356)

```
13. "tgtPower" ブロックをドラッグして、"set motor1.Power to" ブロックの
すぐ右側にスナップするように配置します。
```

### Block 60 (line 364)

```
   "tgtPower" ブロックは、デフォルト値の "1" ブロックを自動的に置き換えます。
```

### Block 61 (line 366)

```
テレメトリステートメントの挿入
```

### Block 62 (line 369)

```
**op mode** はほぼ実行準備が整いました。ただし、続行する前に、**Robot Controller** から
**DRIVER STATION** に情報を送信し、**DRIVER STATION** のユーザーインターフェースに
表示するテレメトリステートメントをいくつか追加します。このテレメトリメカニズムは、
ロボットからの状態情報を **DRIVER STATION** に表示するための便利な方法です。
このメカニズムを使用して、センサーデータ、モーターの状態、ゲームパッドの状態などを
**Robot Controller** から**DRIVER STATION** に表示できます。
```

### Block 63 (line 376)

```
なお、このタスクを完了するには約 15 分かかります。
```

### Block 64 (line 378)

```
テレメトリステートメントの挿入手順
```

### Block 65 (line 381)

```
1. ブラウザウィンドウの左側にある "Utilities" カテゴリをクリックします。
"Telemetry" サブカテゴリを選択し、"call telemetry.addData(key, number)" ブロックを
選択します。
```

### Block 66 (line 390)

```
2. "call telemetry.addData(key, number)" ブロックをドラッグして、
"set motor1.Power to" ブロックの下に配置します。緑色のテキストブロック "key" を
クリックしてテキストをハイライトし、"Target Power" と読めるように変更します。
```

### Block 67 (line 399)

```
   "call telemetry.update" ブロックは重要なブロックです。テレメトリバッファに追加されたデータは、"telemetry.update" メソッドが呼び出されるまで **DRIVER STATION** に送信されません。
```

### Block 68 (line 401)

```
3. "Variables" ブロックカテゴリをクリックし、"tgtPower" ブロックを選択します。
ブロックをドラッグして、テレメトリプログラミングブロックの "number" パラメーターの
隣にクリックして配置します。
```

### Block 69 (line 410)

```
   **Robot Controller** は、変数 tgtPower の値を "Target Power" というキーまたはラベルとともに**DRIVER STATION** に送信します。キーは、**DRIVER STATION** の値の左側に表示されます。
```

### Block 70 (line 412)

```
4. このプロセスを繰り返し、新しいキーに "Motor Power" という名前を付けます。
```

### Block 71 (line 419)

```
5. "DcMotor" サブカテゴリを見つけてクリックします。"motorTest.Power" という
ラベルの付いた緑色のプログラミングブロックを探します。
```

### Block 72 (line 427)

```
6. "motorTest.Power" ブロックを 2 番目のテレメトリブロックの "number" パラメーターに
ドラッグします。
```

### Block 73 (line 435)

```
   これで、**op mode** はモーター出力情報も**Robot Controller** から送信して、**DRIVER STATION** に表示されるようになります。
```

### Block 74 (line 437)

```
Op Mode の保存
```

### Block 75 (line 440)

```
**op mode** を変更した後、**op mode** を**Robot Controller** に保存することが非常に重要です。
```

### Block 76 (line 442)

```
なお、このタスクを完了するには約 1 分かかります。
```

### Block 77 (line 444)

```
Op Mode の保存手順
```

### Block 78 (line 447)

```
1. "Save Op Mode" ボタンをクリックして、**op mode** を**Robot Controller** に保存します。
保存が成功すると、ボタンの右側に "Save completed successfully" という文字が表示されます。
```

### Block 79 (line 456)

```
Program & Manage 画面の終了
```

### Block 80 (line 459)

```
**op mode** を変更して保存した後、**DRIVER STATION** がまだ Program & Manage 画面に
ある場合は、この画面を終了してメインの **DRIVER STATION** 画面に戻る必要があります。
```

### Block 81 (line 462)

```
なお、このタスクを完了するには約 1 分かかります。
```

### Block 82 (line 465)

```
プログラミングモードの終了手順
```

### Block 83 (line 468)

```
1. Android の戻る矢印をクリックして、Program & Manage 画面を終了します。
**op mode** を実行する前に、Program & Manage 画面を終了する必要があります。
```

### Block 84 (line 476)

```
おめでとうございます！**Blocks Programming Tool** を使用して最初の**op mode** を
作成しました！**op mode** の実行方法については、
:doc:`Running Your Op Mode <../running_op_modes/Running-Your-Op-Mode>` という
セクションで学習します。
```


## programming_resources/tutorial_specific/blocks/managing_opmodes/managing-opmodes.rst

### Block 1 (line 1)

```
Blocks での Op Mode 管理 :bdg-warning:`Blocks`
```

### Block 2 (line 4)

```
**Blocks** は、グラフィカルなプログラミング要素を使用してプログラムを作成するプログラミング言語です。そのため、そのファイルフォーマットは、JAVAや他のテキストベースのプログラミング言語ファイルとは異なります。**Blocks** プログラムは**.blk** 拡張子で保存されますが、その内容は実際にはXML（Extensible Markup Language）としてフォーマットされています。**Blocks** プログラムの実際のXMLフォーマットは、このドキュメントの範囲を超えていますが、**Blocks** 以外のプログラムで読み取り/表示/解釈されることを意図していないことだけは言っておきます。MACやPCで**Blocks** プログラムを表示または編集できる一般的なプログラムは存在せず、常に**Robot Controller** アプリ（**REV Control Hub** または認可されたAndroid スマートフォン上で実行される）内の**Blocks** インターフェースを通じて行う必要があります。つまり、ファイルをダブルクリックして、コンピューター上のエディタープログラムで開くことはできません。
```

### Block 3 (line 6)

```
Op Mode の作成
```

### Block 4 (line 9)

```
:doc:`Op Mode 作成のための優れたチュートリアル
<../creating_op_modes/Writing-an-Op-Mode-with-FTC-Blocks>` があり、**Blocks** インターフェースについて多くのことを説明し、**Blocks** プログラムが何をするのかを理解するのに役立ちます。**Blocks** の**Op Mode** の使い方を学ぶために、このドキュメントを確認することをお勧めします。
```

### Block 5 (line 12)

```
Op Mode の保存
```

### Block 6 (line 15)

```
**Op Mode** の** 「保存」** が何を意味するかを理解することが重要です。**Op Mode** をプログラミング/編集する際、Webブラウザ（Chromeなど）を使用するか、Webブラウザとして *動作する* プログラム（REV Hardware Clientなど）を使用します。作成/編集しているプログラムは、Webブラウザ内に *一時的に* のみ存在します。自動保存機能や、プログラムが最終的にデバイス（**REV Control Hub** または承認されたスマートフォン）に保存されることを保証する機能はありません。*保存* 操作のみが、実際に **Op Mode** を**.blk** ファイルとしてデバイスに保存します。したがって、**Blocks** プログラマーは頻繁に作業を *保存* し、特に作業が完了したら必ず保存することが不可欠です。**Op Mode** を *保存* するメカニズムは、ソフトウェアの編集ウィンドウ内の「**Save Op Mode**」ボタンを使用します。
```

### Block 7 (line 22)

```
   Blocks エディター内での Op Mode の保存
```

### Block 8 (line 24)

```
プログラムが保存されると、プログラムが保存されたことを示すメッセージが同じ行の右側に表示されます。
```

### Block 9 (line 31)

```
   Op Mode が保存されたことを示すメッセージ
```

### Block 10 (line 33)

```
Op Mode のダウンロード
```

### Block 11 (line 36)

```
**Op Mode** がデバイスに保存されると、**DRIVER STATION** を介して**Op Mode** を選択したり、プログラミングインターフェースを介して再度編集したりできます。ただし、その**Blocks** プログラムは、デバイス上の**Blocks** ファイル（**.blk** ）としてのみ存在します。多くの場合、ラップトップ（または別のデバイス、または他の安全な場所）にプログラムのコピーを保存したり、他の人（チームメート、別のロボット、他のチーム、オンラインで提供するなど）が使用できるようにプログラムを提供したりすることが望ましいです。
```

### Block 12 (line 38)

```
デバイスから **Blocks** プログラムのコピーを取得するには、デバイスからプログラムを *ダウンロード* する必要があります。これは、編集インターフェースまたはメインの **Blocks** 管理インターフェースのいずれかを使用して、2つの方法のいずれかで実行できます。
```

### Block 13 (line 40)

```
編集インターフェースを通じた Op Mode のダウンロード
```

### Block 14 (line 43)

```
**Op Mode** を編集している間、**Op Mode** は *保存* でき、また *ダウンロード* もできます（他のオプションもありますが、今のところこの2つに焦点を当てます）。**Op Mode** が保存されると、プログラムは**Blocks** ファイル（**.blk** ）として** デバイス上に** 保存されます。プログラムのコピーをローカルコンピューター（安全な保管または共有のため）に保存するには、プログラムを *ダウンロード* する必要があります。プログラムをダウンロードすると、現在のプログラムに対して保存アクションが *実行されます* が、これに依存すべきではありません。プログラマーは常にダウンロードする前にプログラムを保存する必要があります。**Op Mode** のダウンロードは、編集インターフェース内の「**Download Op Mode**」ボタンを介して実行されます。
```

### Block 15 (line 50)

```
   Blocks プログラムのダウンロード
```

### Block 16 (line 52)

```
「Download Op Mode」ボタンを押すと、ファイルがWebブラウザで利用可能になり、Webブラウザは通常の方法でファイルを管理します（たとえば、Chromeではファイルがコンピューターの「Downloads」フォルダーに保存されます）。
```

### Block 17 (line 54)

```
管理インターフェースを通じた Op Mode のダウンロード
```

### Block 18 (line 57)

```
「Blocks」メニュー項目をクリックすると、**Blocks** 管理インターフェースに移動します。このインターフェースには、現在デバイス上にあるすべての**Blocks** の**Op Mode** が表示され、それらの**Op Mode** を管理するためのオプションが提供されます。
```

### Block 19 (line 64)

```
   Blocks 管理インターフェース
```

### Block 20 (line 66)

```
**Op Mode** はこのインターフェースを通じてダウンロードできます。最初、このインターフェースの「**Download Selected Op Modes**」ボタンはグレーアウトされています。このインターフェースで1つ以上の**Op Mode** を選択し、それらをすべて一度にダウンロードできます。以下の例では、「Mecanum Drive」**Op Mode** が選択され、「**Download Selected Op Modes**」ボタンを介してダウンロードされます。
```

### Block 21 (line 73)

```
   管理インターフェースを介した Blocks のダウンロード
```

### Block 22 (line 75)

```
Blocks のアップロード
```

### Block 23 (line 78)

```
以前にダウンロードした **Blocks** ファイルがある場合、または他のソース（たとえば、REVからのサンプル**Blocks** など）から**Blocks** ファイルを受け取った場合、**Blocks** ファイル（**.blk** ）をデバイス（**REV Control Hub** またはAndroid スマートフォン）に *アップロード* する必要があります。**Blocks** 管理インターフェース内には、「**Upload Op Mode**」とマークされたトップメニューのボタンがあります。
```

### Block 24 (line 80)

```
「**Upload Op Mode**」を押すと、アップロードするファイルを選択できるポップアップウィンドウが表示されます。「**Choose File**」ボタンをクリックして、ローカルコンピューターのファイルブラウザを開き、アップロードする**.blk** **Blocks** ファイルを選択します。アップロードされると、**Blocks** プログラムは**Blocks** インターフェース内で開きます。
```

### Block 25 (line 87)

```
   管理インターフェースを介した Blocks ファイルのアップロード
```

### Block 26 (line 89)

```
ブロックがアップロードされると、他の **Op Mode** と同じように編集および変更できます！
```


## programming_resources/tutorial_specific/blocks/running_op_modes/Running-Your-Op-Mode.rst

### Block 1 (line 1)

```
Op Mode の実行（全言語共通）
```

### Block 2 (line 4)

```
**Op Mode** がゲームパッドからの入力を必要とする場合は、Logitech F310または他の承認されたゲームパッドを**DRIVER STATION** に接続する必要があります。**DRIVER STATION** には最大2つのゲームパッドを接続できます。スマートフォンを使用する場合は、USBハブが必要です。ただし、この例では、1つのゲームパッドのみを接続します。
```

### Block 3 (line 6)

```
このタスクの完了には約10分かかります。
```

### Block 4 (line 8)

```
Op Mode の実行手順
```

### Block 5 (line 11)

```
1. ゲームパッドを **DRIVER STATION** に接続します。スマートフォンを使用する場合は、Micro USB OTGアダプターケーブルが必要です。
```

### Block 6 (line 23)

```
2. このWikiの例では、**Op Mode** はユーザーまたはドライバー#1として指定されたゲームパッドからの入力を探します。Logitech F310コントローラーのStartボタンとAボタンを同時に押して、ゲームパッドをユーザー#1として指定します。PS4スタイルのゲームパッドを使用している場合は、OptionsボタンとCrossボタンを使用してゲームパッドをユーザー#1として指定します。
```

### Block 7 (line 30)

```
   注：StartボタンとBボタンを同時に押すと、ゲームパッドがユーザー#2として指定されます。
```

### Block 8 (line 32)

```
3. **DRIVER STATION** 画面で、三角形の「**TeleOp**」ドロップダウンリストボタンをタッチして、利用可能な**Op Mode** のリストを表示します。**Robot Controller** 上にある利用可能な**Op Mode** のリストの中に、最近保存した**Op Mode** が表示されるはずです。
```

### Block 9 (line 44)

```
   注：「**TeleOp**」は「Tele-Operated」の略で、ドライバーが制御する**Op Mode** （つまり、人間のドライバーから入力を受け取る**Op Mode** ）を意味します。
```

### Block 10 (line 46)

```
4. 「MyFIRSTOpMode」を選択して、**Robot Controller** に**Op Mode** をロードします。
```

### Block 11 (line 58)

```
   注：**DRIVER STATION** を使用して**Op Mode** を選択していますが、実際の**Op Mode** の命令は**Robot Controller** で実行されます。
```

### Block 12 (line 60)

```
5. INITボタンを押して、**Op Mode** を初期化します。
```

### Block 13 (line 72)

```
6. Startボタン（三角形の記号で示される）を押して、**Op Mode** の実行を開始します。
```

### Block 14 (line 84)

```
7. ゲームパッドの左ジョイスティックを使用して、DCモーターの動作を制御します。左ジョイスティックを上下に操作すると、ターゲットパワーとモーターパワーが画面の右上隅に表示されるはずです。
```

### Block 15 (line 96)

```
   **Op Mode** を停止したい場合は、**DRIVER STATION** の四角形のStopボタンを押します。
```


## programming_resources/tutorial_specific/blocks/using_sensors/Using-Sensors-(Blocks).rst

### Block 1 (line 1)

```
センサーの使用 :bdg-warning:`Blocks`
```

### Block 2 (line 4)

```
カラー距離センサー
```

### Block 3 (line 7)

```
センサーは、**Robot Controller** が環境に関する情報を取得できるようにするデバイスです。この例では、**REV Robotics** のカラー距離センサーを使用して、範囲（物体からの距離）情報を**DRIVER STATION** に表示します。
```

### Block 4 (line 9)

```
カラー距離センサーは、反射光を使用してセンサーから対象物体までの距離を判断します。比較的正確に近距離（最大5インチ以上）を測定するために使用できます。このドキュメントが最近編集された時点では、**REV** のカラー距離センサーは約2インチ（5cm）で飽和します。これは、2インチ以下の距離の場合、センサーは約2インチに等しい測定距離を返すことを意味します。
```

### Block 5 (line 11)

```
このタスクの完了には約15分かかります。
```

### Block 6 (line 13)

```
距離を表示するための Op Mode の変更手順
```

### Block 7 (line 16)

```
1. ラップトップが **Robot Controller** のProgram & Manage Wi-Fiネットワークにまだ接続されていることを確認します。
```

### Block 8 (line 18)

```
2. 「MyFIRSTOpMode」が編集用に開かれていることを確認します。開かれていない場合は、ラップトップのブラウザウィンドウの左上隅にある **FIRST** ロゴをクリックします。これにより、メインの**Blocks** 開発ツールプロジェクト画面に移動します。
```

### Block 9 (line 25)

```
   まだ開かれていない場合は、「MyFIRSTOpMode」プロジェクトをクリックして編集用に開きます。
```

### Block 10 (line 27)

```
3. ブラウザの左側にある「Utilities」カテゴリをクリックします。「**Telemetry**」サブカテゴリを見つけてクリックします。
```

### Block 11 (line 34)

```
4. 「call **telemetry.addData**」ブロック（数値版）を選択し、「while」ループブロック内の「**telemetry.update**」ブロックの直前の位置にドラッグします。
```

### Block 12 (line 41)

```
5. 「key」テキストをクリックしてハイライトし、テキストを「Distance (cm)」に変更します。
```

### Block 13 (line 48)

```
6. 「Sensors」カテゴリをクリックして展開します。「**REV Color/Range Sensor**」サブカテゴリをクリックします。「call**sensorColorRange.getDistance**」プログラミングブロックをクリックして選択します。
```

### Block 14 (line 55)

```
   注：**Blocks** プログラミングツールの以前のバージョンでは、**REV Robotics** カラー距離センサーを「LynxI2cColorRangeSensor」と呼んでいました。ソフトウェアの新しいバージョンでは、デバイスを「**REV Color/Range Sensor**」と呼びます。
```

### Block 15 (line 57)

```
7. 「call **sensorColorRange.getDistance**」プログラミングブロックを「call**telemetry.addData**」プログラミングブロックの「number」フィールドにドラッグします。
```

### Block 16 (line 64)

```
   これにより、ターゲットまでの測定距離がセンチメートル単位で **DRIVER STATION** に送信されます。
```

### Block 17 (line 66)

```
8. **Op Mode** を保存し、**Robot Controller** に正常に保存されたことを確認します。
```

### Block 18 (line 73)

```
9. :doc:`Op Mode の実行 <../running_op_modes/Running-Your-Op-Mode>` セクションで説明されている手順に従って、更新された **Op Mode** を実行します。
```

### Block 19 (line 80)

```
   **Op Mode** を実行中、カラー光センサーの上に手をかざすと、測定距離が**DRIVER STATION** 画面で変化するはずです。**DRIVER STATION** に「NaN」（数値ではない）という表現が表示される場合、ターゲットは範囲外である可能性が高いです（センサーは反射光を検出しません）。
```

### Block 20 (line 82)

```
タッチセンサー
```

### Block 21 (line 85)

```
この例では、**REV Robotics** のタッチセンサーが**Robot Controller** のアクティブな構成ファイルでデジタルタッチセンサーとして構成されていると仮定します。「**isPressed**」プログラミングブロックを使用して、センサー上のボタンが現在押されているかどうかを判断します。
```

### Block 22 (line 92)

```
**Control Hub** または**Expansion Hub** のデジタルポートには、ポートあたり2つのデジタルピンが含まれています。4線JSTケーブルを使用して**REV Robotics** のタッチセンサーを**Control Hub** または**Expansion Hub** のデジタルポートに接続すると、タッチセンサーはポート内の2つのデジタルピンのうち2番目に配線されます。4線ケーブルの最初のデジタルピンは接続されません。
```

### Block 23 (line 94)

```
たとえば、タッチセンサーを **Control Hub** または**Expansion Hub** の「0,1」デジタルポートに接続すると、タッチセンサーはポートの2番目のピン（「1」とラベル付け）に接続されます。最初のピン（「0」とラベル付け）は接続されません。
```

### Block 24 (line 96)

```
このタスクの完了には約15分かかります。
```

### Block 25 (line 98)

```
ボタン（タッチセンサー）状態を表示するための Op Mode の変更手順
```

### Block 26 (line 101)

```
1. ラップトップが **Robot Controller** のプログラミングモードWi-Fiネットワークにまだ接続されていることを確認します。
```

### Block 27 (line 103)

```
2. 「MyFIRSTOpMode」が編集用に開かれていることを確認します。開かれていない場合は、ラップトップのブラウザウィンドウの左上隅にある **FIRST** ロゴをクリックします。これにより、メインの**Blocks** 開発ツールプロジェクト画面に移動します。
```

### Block 28 (line 110)

```
   まだ開かれていない場合は、「MyFIRSTOpMode」プロジェクトをクリックして編集用に開きます。
```

### Block 29 (line 112)

```
3. 「Logic」カテゴリをクリックします。「if do else」ブロックを見つけてクリックします。
```

### Block 30 (line 119)

```
4. 「if do else」ブロックを「**telemetry.update**」ブロックの前の位置にドラッグします。
```

### Block 31 (line 126)

```
5. 「Sensors」カテゴリをクリックして展開します（まだ展開されていない場合）。「Touch Sensor」サブカテゴリをクリックし、「.**isPressed**」ブロックを見つけて選択します。
```

### Block 32 (line 133)

```
6. 「**isPressed**」ブロックを「if do else」プログラミングブロックのテスト条件にドラッグします。
```

### Block 33 (line 140)

```
7. ブラウザの左側にある「Utilities」カテゴリをクリックします。「**Telemetry**」サブカテゴリを見つけてクリックします。
```

### Block 34 (line 147)

```
   「call **telemetry.addData**」ブロック（テキスト版）を選択し、「if do else」ブロックの「do」句にドラッグします。
```

### Block 35 (line 149)

```
8. 「key」値を「testTouch」に、「text」値を「is pressed」に変更します。
```

### Block 36 (line 156)

```
9. 別の「**telemetry.addData**」ブロック（テキスト版）を「if do else」ブロックの「else」句に挿入します。「key」値を「testTouch」に、「text」値を「is NOT pressed」に変更します。
```

### Block 37 (line 163)

```
10. **Op Mode** を保存し、**Robot Controller** に正常に保存されたことを確認します。
```

### Block 38 (line 170)

```
11. :doc:`Op Mode の実行 <../running_op_modes/Running-Your-Op-Mode>` セクションで説明されている手順に従って、更新された **Op Mode** を実行します。
```

### Block 39 (line 177)

```
   **Op Mode** を実行してボタンを押したり離したりすると、**DRIVER STATION** のテレメトリメッセージがデジタルタッチセンサーの現在の状態を反映して更新されるはずです。
```


## programming_resources/tutorial_specific/onbot_java/controlling_a_servo/Controlling-a-Servo-(OnBot-Java).rst

### Block 1 (line 1)

```
サーボの制御 :bdg-info:`OBJ`
```

### Block 2 (line 4)

```
このセクションでは、ゲームパッドのボタンでサーボモーターを制御するように **Op Mode** を変更します。
```

### Block 3 (line 6)

```
サーボモーターとは？
```

### Block 4 (line 9)

```
サーボモーターは特殊なタイプのモーターです。サーボモーターは精密な動作を目的として設計されています。一般的なサーボモーターは可動範囲が制限されています。
```

### Block 5 (line 11)

```
下の図には、「標準スケール」の180度サーボが示されています。このタイプのサーボは、ホビイストや **FIRST Tech Challenge** チームに人気があります。このサーボモーターは、シャフトを180度の範囲で回転させることができます。サーボコントローラーと呼ばれる電子モジュールを使用して、サーボモーターを特定の位置に移動する**Op Mode** を作成できます。モーターが目標位置に達すると、サーボのシャフトに外力が加わっても、その位置を保持します。
```

### Block 6 (line 18)

```
サーボモーターは、精密な動作を行いたい場合に便利です（例えば、ターゲットを探すためにセンサーで範囲をスキャンしたり、ラジコン飛行機の操縦翼面を動かしたりする場合など）。
```

### Block 7 (line 20)

```
サーボを制御するための Op Mode の変更
```

### Block 8 (line 23)

```
サーボモーターを制御するために必要なロジックを追加するために、**Op Mode** を変更しましょう。この例では、Logitech F310 ゲームパッドのボタンを使用して、サーボモーターの位置を制御します。
```

### Block 9 (line 25)

```
一般的なサーボでは、サーボの目標位置を指定できます。サーボはモーターシャフトを回転させて目標位置に移動し、その位置を乱そうとする適度な力が加えられても、その位置を維持します。
```

### Block 10 (line 27)

```
**FIRST Tech Challenge** 制御システムでは、サーボの目標位置を 0 から 1 の範囲で指定できます。目標位置 0 は回転角度 0 度に対応し、目標位置 1 は一般的なサーボモーターの回転角度 180 度に対応します。
```

### Block 11 (line 34)

```
この例では、F310 コントローラーの右側にあるカラーボタンを使用して、サーボの位置を制御します。最初に、**Op Mode** はサーボを中間位置（180度範囲の90度）に移動します。黄色の「Y」ボタンを押すと、サーボは 0 度の位置に移動します。青色の「X」ボタンまたは赤色の「B」ボタンを押すと、サーボは 90 度の位置に移動します。緑色の「A」ボタンを押すと、サーボは 180 度の位置に移動します。
```

### Block 12 (line 41)

```
**Op Mode** を変更して、以下のコードを追加します：
```

### Block 13 (line 69)

```
この追加されたコードは、F310 ゲームパッドのカラーボタンのいずれかが押されているかどうかをチェックします。Y ボタンが押されると、サーボは 0 度の位置に移動します。X ボタンまたは B ボタンのいずれかが押されると、サーボは 90 度の位置に移動します。A ボタンが押されると、サーボは 180 度の位置に移動します。**Op Mode** は、サーボの位置に関するテレメトリデータを**Driver Station** に送信します。
```

### Block 14 (line 71)

```
**Op Mode** を変更した後、ビルドして実行できます。ゲームパッド #1 がまだ構成されていることを確認してから、カラーボタンを使用してサーボの位置を移動させます。
```


## programming_resources/tutorial_specific/onbot_java/creating_op_modes/Creating-and-Running-an-Op-Mode-(OnBot-Java).rst

### Block 1 (line 1)

```
Op Mode の作成と実行 :bdg-info:`OBJ`
```

### Block 2 (line 4)

```
Java プログラミング言語
```

### Block 3 (line 7)

```
このチュートリアルは、Javaプログラミング言語について十分な理解があることを前提としています。Javaを知らない場合は、ビジュアル開発ツールである **Blocks** プログラミングツールの使用を検討してください。**Blocks** プログラミングツールに関する情報は、以下のリンクで確認できます：
```

### Block 4 (line 9)

```
:doc:`Blocks チュートリアル <../../../blocks/Blocks-Tutorial>`
```

### Block 5 (line 11)

```
または、以下のアドレスで入手可能なOracle Javaチュートリアルを完了することで、Javaプログラミング言語を学ぶことができます：
```

### Block 6 (line 15)

```
Op Mode とは？
```

### Block 7 (line 18)

```
典型的な **FIRST Tech Challenge** のマッチでは、チームのロボットはポイントを獲得するために様々なタスクを実行する必要があります。例えば、チームはロボットに競技フィールド上の白い線を追従させ、マッチ中に自律的にゲーム要素をゴールに入れることを望むかもしれません。チームは、ロボットの動作を指定するために *Op Mode*（「operational modes」の略）と呼ばれるプログラムを作成します。これらの **Op Mode** は、**DRIVER STATION** デバイスで選択された後、**Robot Controller** スマートフォン上で実行されます。
```

### Block 8 (line 20)

```
**FIRST Tech Challenge** に参加しているチームは、独自の**Op Mode** を作成するために使用できる様々なプログラミングツールを持っています。このドキュメントでは、**OnBot Java** プログラミングツールを使用してロボット用の**Op Mode** を作成する方法を説明します。
```

### Block 9 (line 22)

```
OnBot Java プログラミングツール
```

### Block 10 (line 25)

```
**OnBot Java** プログラミングツールは、**Robot Controller** スマートフォンによって提供されるユーザーフレンドリーなプログラミングツールです。ユーザーはこのツールを使用してロボット用のカスタム**Op Mode** を作成し、それらの**Op Mode** を**Robot Controller** に直接保存できます。ユーザーはJavaを使用して**Op Mode** を作成します。**Op Mode** は**Robot Controller** 上で非常に迅速にコンパイルされ、実行時に**Robot Controller** によって動的にロードされます。
```

### Block 11 (line 32)

```
このドキュメントの例では、Windowsのノートパソコンを使用して **Robot Controller** に接続します。このWindowsノートパソコンには、**OnBot Java** プログラミングツールにアクセスするために使用されるJavaScript対応のWebブラウザがインストールされています。
```

### Block 12 (line 39)

```
なお、**Robot Controller** としてAndroidスマートフォンを使用している場合も、**Op Mode** の作成と編集に使用するプロセスは同じです。
```

### Block 13 (line 46)

```
なお、Windowsコンピューターの代わりに、Apple Macノートパソコン、Chromebook、またはiPadなどの代替デバイスを使用して **OnBot Java** プログラミングツールにアクセスすることもできます。ただし、このドキュメントに含まれる手順は、Windowsノートパソコンを使用していることを前提としています。
```

### Block 14 (line 48)

```
なお、このwikiのこのセクションは、Androidデバイスとロボットハードウェアをすでにセットアップおよび構成していることを前提としています。また、ノートパソコンを **Robot Controller** デバイスのProgam & Manageサーバーに正常に接続していることも前提としています。
```

### Block 15 (line 50)

```
最初の Op Mode の作成
```

### Block 16 (line 53)

```
ノートパソコンを **Robot Controller** のProgram & Manageワイヤレスネットワークに正常に接続できた場合、最初の**Op Mode** を作成する準備が整いました。このセクションでは、**OnBot Java** プログラミングツールを使用して、最初の**Op Mode** のプログラムロジックを作成します。
```

### Block 17 (line 56)

```
最初の Op Mode を作成する手順
```

### Block 18 (line 59)

```
1. ノートパソコン上でWebブラウザを起動し（**FIRST** はGoogle Chromeの使用を推奨しています）、**Robot Controller** のProgram & Manage画面に表示されているWebアドレスを見つけます。
```

### Block 19 (line 73)

```
   このWebアドレスをブラウザのアドレスフィールドに入力し、RETURNキーを押してProgram & Manage Webサーバーに移動します。
```

### Block 20 (line 81)

```
2. Webブラウザがプログラミングモードサーバーに接続されていることを確認します。プログラミングモードサーバーに正常に接続されている場合、**Robot Controller** コンソールが表示されます。
```

### Block 21 (line 88)

```
3. 画面上部にある *OnBotJava* という単語をクリックします。これにより、ブラウザが **OnBot Java** プログラミングモードに切り替わります。
```

### Block 22 (line 95)

```
4. **OnBot Java** ユーザーインターフェースを確認します。左側にはプロジェクトブラウザペインがあります。右上隅にはソースコード編集ペインがあります。右下隅にはメッセージペインがあります。
```

### Block 23 (line 102)

```
5. プロジェクトブラウザペインで「+」記号を押して、新しいファイルを作成します。このボタンを押すと、新規ファイルダイアログボックスが起動します。このダイアログボックスには、新しいファイルをカスタマイズするために構成できるいくつかのパラメーターがあります。
```

### Block 24 (line 109)

```
   この例では、新規ファイルダイアログボックスでファイル名として「MyFIRSTJavaOpMode」を指定します。
```

### Block 25 (line 111)

```
   サンプルドロップダウンリストコントロールを使用して、利用可能なサンプル **Op Mode** のリストから「BlankLinearOpMode」を選択します（上の画像を参照）。「BlankLinearOpMode」を選択すると、**OnBot Java** エディタが基本的な**LinearOpMode** フレームワークを自動的に生成します。
```

### Block 26 (line 113)

```
   「TeleOp」とラベル付けされたオプションをチェックして、この新しいファイルがテレオペレーション（つまり、ドライバー制御）**Op Mode** として構成されるようにします。
```

### Block 27 (line 115)

```
   また、「Setup Code for Configured Hardware」オプションもチェックしてください。このオプションを有効にすると、**OnBot Java** エディタは**Robot Controller** のハードウェア構成ファイルを確認し、**Op Mode** で構成されたデバイスにアクセスするために必要なコードを自動的に生成します。
```

### Block 28 (line 117)

```
   「OK」ボタンを押して、新しい **Op Mode** を作成します。
```

### Block 29 (line 119)

```
6. **OnBot Java** ユーザーインターフェースの編集ペインに、新しく作成された**Op Mode** が表示されるはずです。
```

### Block 30 (line 126)

```
おめでとうございます、最初の **Op Mode** を作成しました！この**Op Mode** は現在あまり機能しませんが、最終的にはより便利にするために修正します。
```

### Block 31 (line 133)

```
なお、**OnBot** **Op Mode** を作成すると、**Robot Controller** に保存される .java ファイルが作成されます。保存された**Op Mode** には、画面の左側にあるプロジェクトブラウザを使用してアクセスできます。また、プロジェクトブラウザを右クリックして、ファイルとフォルダーを作成、編集、または削除するオプションのリストを表示することで、保存された**Op Mode** を整理することもできます。
```

### Block 32 (line 135)

```
また、Program & Manageサーバーに接続されている限り、**OnBot Java** エディタは編集中に**Op Mode** を自動的に保存することにも注意してください。
```

### Block 33 (line 137)

```
Op Mode の構造を調べる
```

### Block 34 (line 140)

```
**Op Mode** を、**Robot Controller** が実行するタスクのリストと考えると便利です。リニア**Op Mode** の場合、**Robot Controller** はこのタスクのリストを順次処理します。ユーザーは、制御ループ（whileループなど）を使用して、リニア**Op Mode** 内で特定のタスクを**Robot Controller** に繰り返し（または反復）実行させることもできます。
```

### Block 35 (line 147)

```
**Op Mode** をロボットへの命令のリストと考えると、この作成した命令のセットは、チームメンバーがこの**Robot Controller** の利用可能な**Op Mode** のリストから「MyFIRSTJavaOpMode」という**Op Mode** を選択するたびに、ロボットによって実行されます。
```

### Block 36 (line 149)

```
新しく作成した **Op Mode** の構造を見てみましょう。以下は、**Op Mode** テキストのコピーです（いくつかのコメント、パッケージ定義、およびいくつかのインポートパッケージステートメントを除く）：
```

### Block 37 (line 185)

```
**Op Mode** の開始時に、クラス定義の前にアノテーションがあります。このアノテーションは、これがテレオペレーション（つまり、ドライバー制御）**Op Mode** であることを示しています：
```

### Block 38 (line 191)

```
この **Op Mode** を自律**Op Mode** に変更したい場合は、``@TeleOp`` を``@Autonomous`` アノテーションに置き換えます。
```

### Block 39 (line 193)

```
サンプルコードから、**Op Mode** がJavaクラスとして定義されていることがわかります。この例では、**Op Mode** 名は「MyFIRSTJavaOpMode」と呼ばれ、**LinearOpMode** クラスから特性を継承しています。
```

### Block 40 (line 199)

```
また、**OnBot Java** エディタがこの**Op Mode** 用に5つのプライベートメンバー変数を作成したこともわかります。これらの変数は、**OnBot Java** エディタが**Robot Controller** の構成ファイルで検出した5つの構成済みデバイスへの参照を保持します。
```

### Block 41 (line 209)

```
次に、runOpModeと呼ばれるオーバーライドされたメソッドがあります。**LinearOpMode** 型のすべての**Op Mode** は、このメソッドを実装する必要があります。このメソッドは、ユーザーが**Op Mode** を選択して実行したときに呼び出されます。
```

### Block 42 (line 216)

```
runOpModeメソッドの開始時に、**Op Mode** はhardwareMapという名前のオブジェクトを使用して、**Robot Controller** の構成ファイルにリストされているハードウェアデバイスへの参照を取得します：
```

### Block 43 (line 226)

```
hardwareMapオブジェクトは、runOpModeメソッドで使用できます。これは **HardwareMap** クラス型のオブジェクトです。
```

### Block 44 (line 228)

```
なお、**Op Mode** で特定のデバイスへの参照を取得しようとする場合、**HardwareMap.get** メソッドの第2引数として指定する名前は、構成ファイルでデバイスを定義するために使用した名前と一致する必要があります。例えば、「motorTest」という名前のDCモーターを持つ構成ファイルを作成した場合、hardwareMapオブジェクトからこのモーターを取得するには、この同じ名前（大文字と小文字を区別）を使用する必要があります。名前が一致しない場合、**Op Mode** はデバイスを見つけることができないことを示す例外をスローします。
```

### Block 45 (line 230)

```
例の次のいくつかのステートメントでは、**Op Mode** はユーザーにスタートボタンを押して続行するように促します。runOpModeメソッドで使用できる別のオブジェクトを使用します。このオブジェクトは**telemetry** と呼ばれ、**Op Mode** は**addData** メソッドを使用して**DRIVER STATION** に送信するメッセージを追加します。次に、**Op Mode** は**update** メソッドを呼び出して、メッセージを**DRIVER STATION** に送信します。次に、**waitForStart** メソッドを呼び出して、ユーザーがDriver Stationのスタートボタンを押して**Op Mode** の実行を開始するまで待機します。
```

### Block 46 (line 239)

```
なお、すべてのリニア **Op Mode** には、ドライバーがスタートボタンを押すまでロボットが**Op Mode** の実行を開始しないようにするために、waitForStartステートメントが必要です。
```

### Block 47 (line 241)

```
スタートコマンドを受信した後、**Op Mode** はwhileループに入り、**Op Mode** がアクティブでなくなるまで（つまり、ユーザーが**DRIVER STATION** のストップボタンを押すまで）このループで反復を続けます：
```

### Block 48 (line 252)

```
**Op Mode** がwhileループで反復すると、「Status」というインデックスと「Running」というメッセージを含むテレメトリメッセージを**DRIVER STATION** に表示するために送信し続けます。
```

### Block 49 (line 254)

```
Op Mode のビルド
```

### Block 50 (line 257)

```
**Op Mode** を作成または編集すると、**OnBot Java** エディタは .java ファイルを**Robot Controller** のファイルシステムに自動保存します。ただし、**Robot Controller** で変更を実行する前に、まず**Op Mode** をビルドして、Javaテキストファイルから**Robot Controller** アプリに動的にロードできるバイナリに変換する必要があります。
```

### Block 51 (line 259)

```
**Op Mode** に満足してビルドする準備ができている場合は、ビルドボタン（レンチ記号のあるボタン、下の画像を参照）を押してビルドプロセスを開始します。なお、ビルドプロセスは**Robot Controller** 上の** すべての .java ファイル** をビルドします。
```

### Block 52 (line 266)

```
ウィンドウの右下にあるメッセージペインにメッセージが表示されるはずです。ビルドが成功した場合、メッセージペインに「Build succeeded!」というメッセージが表示されるはずです。
```

### Block 53 (line 273)

```
更新された **Op Mode** でバイナリファイルをビルドしたら、**Robot Controller** で実行する準備が整いました。例の**Op Mode** を実行する前に、ビルドプロセス中に問題が発生した場合に何が起こるかを見てみましょう。
```

### Block 54 (line 275)

```
ビルドメッセージのトラブルシューティング
```

### Block 55 (line 278)

```
前のセクションでは、ビルドプロセスが順調に進みました。**Op Mode** を少し修正して、ビルドプロセスでエラーを発生させてみましょう。
```

### Block 56 (line 280)

```
**OnBot Java** ウィンドウの編集ペインで、``private Servo servoTest;`` と記述されている行を探します。これは、**Op Mode** クラス定義の先頭近くに表示されるはずです。「Servo」という単語を「Zervo」という単語に変更します：
```

### Block 57 (line 286)

```
また、**Op Mode** が初期化されたことをユーザーに通知するテレメトリステートメントを変更し、2つの引数のうちの1つを削除して、ステートメントが次のようになるようにしましょう：
```

### Block 58 (line 292)

```
なお、2番目の引数を削除すると、変更された addData ステートメントの行の横に小さな「x」が表示されるはずです。この「x」は、ステートメントに構文エラーがあることを示しています。
```

### Block 59 (line 299)

```
**Op Mode** を変更したら、ビルドボタンを押して、どのようなエラーメッセージが表示されるかを確認できます。
```

### Block 60 (line 306)

```
**Op Mode** を最初にビルドしようとすると、「illegal start of expression error」が表示されるはずです。これは、addData メソッドに2番目の引数がないためです。**OnBot Java** システムは、エラーがあるファイルと、ファイル内でエラーが発生した場所も示します。
```

### Block 61 (line 308)

```
この例では、問題のファイルは「``org/firstinspires/ftc/teamcode/MyFIRSTJavaOpMode.java`` 」と呼ばれ、エラーは62行37列で発生します。ビルドプロセスは **Robot Controller** 上のすべての .java ファイルをビルドすることに注意することが重要です。別のファイル（現在編集していないファイル）にエラーがある場合は、ファイル名を確認して、どのファイルが問題を引き起こしているかを判断する必要があります。
```

### Block 62 (line 310)

```
このステートメントを元の正しい形式に戻しましょう：
```

### Block 63 (line 316)

```
addData ステートメントを修正した後、ビルドボタンをもう一度押して、何が起こるかを確認します。**OnBot Java** システムは、「``org/firstinspires/ftc/teamcode/MyFIRSTJavaOpMode.java``」というソースファイルの51行13列で、シンボル「``Zervo`` 」を見つけることができないと文句を言うはずです。
```

### Block 64 (line 323)

```
ステートメントを元の形式に戻してから、ビルドボタンを押して、**Op Mode** が適切にビルドされることを確認する必要があります。
```

### Block 65 (line 329)

```
Op Mode の実行
```

### Block 66 (line 332)

```
*  **Op Mode** のリビルドに成功した場合、**Op Mode** を実行する準備が整いました。**DRIVER STATION** がまだ**Robot Controller** に接続されていることを確認します。例の**Op Mode** をテレオペレーション**Op Mode** として指定したため、「TeleOp」**Op Mode** としてリストされます。
```

### Block 67 (line 334)

```
*  **DRIVER STATION** で、「TeleOp」ドロップダウンリストコントロールを使用して、利用可能な**Op Mode** のリストを表示します。リストから**Op Mode** （「MyFIRSTJavaOpMode」）を選択します。
```

### Block 68 (line 346)

```
   INITボタンを押して、**Op Mode** を初期化します。
```

### Block 69 (line 358)

```
**Op Mode** は、waitForStart ステートメントまで runOpMode メソッド内のステートメントを実行します。その後、スタートボタン（三角形の記号で表される）を押して続行するまで待機します。
```

### Block 70 (line 370)

```
スタートボタンを押すと、**Op Mode** は反復を続け、「Status: Running」メッセージを**DRIVER STATION** に送信します。**Op Mode** を停止するには、四角形のストップボタンを押します。
```

### Block 71 (line 382)

```
おめでとうございます！最初のJava **Op Mode** を実行しました！
```

### Block 72 (line 384)

```
Op Mode を変更してモーターを制御する
```

### Block 73 (line 387)

```
**REV Expansion Hub** に接続して構成したDCモーターを制御するように**Op Mode** を変更しましょう。プログラムループのコードを次のように変更します：
```

### Block 74 (line 403)

```
追加されたコードを見ると、whileループに入る前に、target powerという新しい変数を定義していることがわかります。
```

### Block 75 (line 409)

```
whileループの開始時に、変数 tgtPower を gamepad1 の左ジョイスティックの負の値と等しく設定します：
```

### Block 76 (line 415)

```
オブジェクト gamepad1 は、runOpMode メソッドでアクセスできます。これは、**OPERATOR CONSOLE** のゲームパッド #1 の状態を表します。なお、競技中に使用されるF310ゲームパッドの場合、ジョイスティックのY値は、ジョイスティックが最上位置にあるときは -1 から、最下位置にあるときは +1 までの範囲です。上記の例のコードでは、left_stick_y 値を否定して、左ジョイスティックを前方に押すとモーターに正のパワーが適用されるようにしています。なお、この例では、モーターの前方と後方の概念は任意です。ただし、ジョイスティックのy値を否定する概念は、実際には非常に便利です。
```

### Block 77 (line 422)

```
次のステートメントのセットは、motorTest のパワーを変数 tgtPower で表される値に設定します。次に、目標パワーと実際のモーターパワーの値が、**telemetry** メカニズムを介して**DRIVER STATION** に送信されるデータのセットに追加されます。
```

### Block 78 (line 431)

```
**Op Mode** を変更してこれらの新しいステートメントを含めた後、ビルドボタンを押して、**Op Mode** が正常にビルドされたことを確認します。
```

### Block 79 (line 433)

```
ゲームパッドを接続して Op Mode を実行する
```

### Block 80 (line 436)

```
*  **Op Mode** はゲームパッドから入力を受け取り、この入力を使用してDCモーターを制御します。**Op Mode** を実行するには、Logitech F310 ゲームパッドを**DRIVER STATION** に接続する必要があります。
```

### Block 81 (line 438)

```
ゲームパッドを **DRIVER STATION** に接続します。スマートフォンを使用している場合は、Micro USB OTG アダプターケーブルが必要です。
```

### Block 82 (line 450)

```
例の **Op Mode** は、ユーザーまたはドライバー #1 として指定されたゲームパッドからの入力を探しています。Logictech F310 コントローラーのスタートボタンとAボタンを同時に押して、ゲームパッドをユーザー #1 として指定します。なお、スタートボタンとBボタンを同時に押すと、ゲームパッドがユーザー #2 として指定されます。
```

### Block 83 (line 457)

```
ゲームパッドをユーザー #1 として正常に指定した場合、**DRIVER STATION** 画面の右上隅にある「User 1」というテキストの上に小さなゲームパッドアイコンが表示されるはずです。ゲームパッド #1 でアクティビティがあるたびに、小さなアイコンが緑色で強調表示されるはずです。アイコンが表示されない場合、またはゲームパッドを使用しても緑色で強調表示されない場合は、ゲームパッドへの接続に問題があります。
```

### Block 84 (line 459)

```
「MyFIRSTJavaOpMode」**Op Mode** を選択、初期化、実行します。なお、**Op Mode** をリビルドするたびに、現在の**Op Mode** 実行を停止してから再起動する必要があります。これにより、作成した変更が有効になります。
```

### Block 85 (line 461)

```
ゲームパッドを正しく構成した場合、左ジョイスティックでモーターの動きを制御できるはずです。**Op Mode** を実行するときは、注意して、回転するモーターに何も巻き込まれないようにしてください。なお、ジョイスティックを動かすたびに、ユーザー #1 ゲームパッドアイコンが緑色で強調表示されるはずです。また、目標パワーと実際のモーターパワーの値が**DRIVER STATION** のテレメトリエリアに表示されるはずです。
```


## programming_resources/tutorial_specific/onbot_java/onbot_java_reference/OnBot-Java-Reference-Info.rst

### Block 1 (line 1)

```
OnBot Java リファレンス情報 :bdg-info:`OBJ`
```

### Block 2 (line 4)

```
Javadoc リファレンスページ
```

### Block 3 (line 7)

```
より複雑な **Op Mode** を作成し始めると、**FIRST Tech Challenge** ソフトウェア開発キット（SDK）のより多くの機能を使用する必要が出てきます。以下のウェブアドレスで、利用可能な**FIRST Tech Challenge** 関連のクラスとメソッドの説明を提供するオンライン Javadoc 資料を参照できます：
```

### Block 4 (line 11)

```
サンプル Op Mode
```

### Block 5 (line 14)

```
**OnBot Java** プログラミングツールには、**FIRST Tech Challenge** 制御システムでさまざまなタスクを実行する方法を示す、いくつかの組み込みサンプル**Op Mode** があります。新しいファイルを作成する際、Sample ドロップダウンリスト コントロールを使用して、利用可能なサンプル**Op Mode** やテンプレートのリストを表示できます。これらのサンプルのコメントは、プログラム文が何をするかを説明するのに役立ちます。
```

### Block 6 (line 21)

```
テクノロジーフォーラム
```

### Block 7 (line 24)

```
登録されたチームは、**FIRST Tech Challenge** フォーラムでユーザーアカウントを作成できます。チームはフォーラムを使用して質問をし、**FIRST Tech Challenge** コミュニティからサポートを受けることができます。
```

### Block 8 (line 26)

```
テクノロジーフォーラムは以下のアドレスにあります：
```

### Block 9 (line 30)

```
REV Robotics Control Hub ドキュメント
```

### Block 10 (line 33)

```
`REV Robotics Control Hub 入門ガイド <https://docs.revrobotics.com/duo-control/control-hub-gs>`__
```

### Block 11 (line 35)

```
REV Robotics Expansion Hub ドキュメント
```

### Block 12 (line 38)

```
`REV Robotics Expansion Hub 入門ガイド <https://docs.revrobotics.com/duo-control/control-system-overview/expansion-hub-basics>`__
```

### Block 13 (line 40)

```
REV Robotics Driver Hub ドキュメント
```

### Block 14 (line 43)

```
`REV Robotics Driver Hub 入門ガイド <https://docs.revrobotics.com/duo-control/driver-hub-gs>`__
```


## programming_resources/tutorial_specific/onbot_java/using_sensors/Using-Sensors-(OnBot-Java).rst

### Block 1 (line 1)

```
センサーの使用 :bdg-info:`OBJ`
```

### Block 2 (line 4)

```
Color-Distance センサー
```

### Block 3 (line 7)

```
センサーは、**Robot Controller** が環境に関する情報を取得できるようにするデバイスです。この例では、**REV Robotics**Color-Distance センサーを使用して、範囲（オブジェクトからの距離）情報を**Driver Station** に表示します。
```

### Block 4 (line 9)

```
Color-Range センサーは反射光を使用して、センサーからターゲットオブジェクトまでの距離を測定します。合理的な精度で近距離（5インチ以上）を測定するために使用できます。このドキュメントが最後に編集された時点で、REV Color-Range センサーは約2インチ（5cm）で飽和することに注意してください。これは、2インチ以下の距離では、センサーが約2インチに等しい測定距離を返すことを意味します。
```

### Block 5 (line 11)

```
**Op Mode** を変更して、距離情報（センチメートル単位）を**Driver Station** に送信するテレメトリステートメントを追加します。
```

### Block 6 (line 22)

```
**Op Mode** を変更した後、ビルドボタンを押してから**Op Mode** を実行し、**Driver Station** に距離が表示されることを確認します。距離が「NaN」（「Not a Number」の略）と表示される場合は、センサーがターゲットから遠すぎる（反射がゼロ）ことを意味している可能性があります。また、センサーは約5cmで飽和することにも注意してください。
```

### Block 7 (line 24)

```
タッチセンサー
```

### Block 8 (line 27)

```
**REV Robotics** タッチセンサーは、**Control Hub** または**Expansion Hub** のデジタルポートに接続できます。タッチセンサーは、押されていない場合は HIGH（TRUE を返す）です。押されると LOW（FALSE を返す）に引き下げられます。
```

### Block 9 (line 34)

```
**Control Hub** または**Expansion Hub** のデジタルポートには、ポートごとに2つのデジタルピンが含まれています。4線式 JST ケーブルを使用して**REV Robotics** タッチセンサーを**Control Hub** または**Expansion Hub** のデジタルポートに接続すると、タッチセンサーはポート内の2つのデジタルピンのうち2番目のピンに配線されます。4線式ケーブルの最初のデジタルピンは未接続のままです。
```

### Block 10 (line 36)

```
例えば、タッチセンサーを **Control Hub** または**Expansion Hub** の「0,1」デジタルポートに接続すると、タッチセンサーはポートの2番目のピン（「1」とラベル付けされている）に接続されます。最初のピン（「0」とラベル付けされている）は未接続のままです。
```

### Block 11 (line 38)

```
**Op Mode** 内の waitForStart コマンドの前に発生するコードを変更して、デジタルチャネルを入力モードに設定します。
```

### Block 12 (line 50)

```
また、while ループ内のコードを変更して、デジタル入力チャネルの状態をチェックする if-else ステートメントを追加します。チャネルが LOW（false）の場合、タッチセンサーボタンが押されており、グラウンドに LOW に引き下げられています。それ以外の場合、タッチセンサーボタンは押されていません。
```

### Block 13 (line 66)

```
**Op Mode** を再ビルドしてから、**Op Mode** を再初期化して再起動します。**Op Mode** は、ボタンの状態（「PRESSED」または「NOT PRESSED」）を表示するようになります。
```


## programming_resources/vision/camera_calibration/camera-calibration.rst

### Block 1 (line 1)

```
**FIRST** **Tech Challenge** のカメラ較正
```

### Block 2 (line 4)

```
カメラ較正とは何か、なぜ必要なのか？
```

### Block 3 (line 7)

```
カメラは、カメラが最終的に「見る」実際の画像に変動をもたらす可能性のある多くの異なるコンポーネントで構成されています。カメラ較正は、カメラとレンズの組み合わせが最終的に世界をどのように見るかを数学的にモデル化するプロセスです。たとえば、視野がどれだけ広いかなどです。カメラを使用して高精度タスクを実行する場合、たとえばカメラを使用して精密測定を実行したり、**AprilTags** などの基準マーカーシステムから正確な 6DOF ポーズデータを取得したりする場合は、カメラを較正する必要があります。較正は、カメラとレンズに固有であるだけでなく、特定のカメラで使用される解像度にも固有であることに注意することが重要です！
```

### Block 4 (line 10)

```
   屈折率の違いにより、空気中と液体中（たとえば水中）で実行された較正は転送できません。較正は、カメラが動作する媒体内で実行する必要があります。
```

### Block 5 (line 12)

```
カメラ較正方法
```

### Block 6 (line 15)

```
**OpenCV**、**MATLAB**、**MRCAL** など、カメラを較正する方法は多数あります。
```

### Block 7 (line 17)

```
-  上級チームの場合、`MRCAL <https://mrcal.secretsauce.net/>`__ を使用するのが最良の選択肢です - これは NASA JPL によって開発されたツールで、較正がどれだけ優れているか、および最適なパラメーターに到達するための数値最適化に何が含まれるかに関する広範なデータを提供します。
-  その他の私たちのために、ここでは `3DF Zephyr <https://www.3dflow.net/3df-zephyr-free/>`__ を使用してカメラを較正する方法を説明します。これは非常に使いやすく、妥当な結果を提供できます。
```

### Block 8 (line 21)

```
   **3DF Zephyr** は Microsoft Windows 64ビットアプリケーションです。32ビットバージョンの Windows ではサポートされておらず、Mac または Linux プラットフォームでもサポートされていません。
```

### Block 9 (line 24)

```
**3DF Zephyr** を使用した較正
```

### Block 10 (line 27)

```
1. `3DF Zephyr Free Edition <https://www.3dflow.net/3df-zephyr-free/>`__ をダウンロードしてインストールします。
2. サンプル ``UtilityCameraFrameCapture`` **OpMode** を teamcode フォルダーにコピーし、ニーズに応じて上部のパラメーターを変更します。このサンプルは Java でのみ記述されていることに注意することが重要です。
3. **3DF Zephyr** で、次の場所に移動します：
```

### Block 11 (line 33)

```
   そして指示に従います。フレームキャプチャ **OpMode** を使用して写真を撮ります。
4. **Robot Controller** デバイスを USB ケーブルでコンピューターに接続し、キャプチャされたフレームをコンピューターにコピーします。それらは USB ストレージのルートにあり、名前の前に ``VisionPortal-`` が付いています。
5. **3DF Zephyr** で *Add Images* ボタンを押し、コンピューターにコピーした画像を指定します。
6. **3DF Zephyr** で較正ターゲット分析を実行します。完了すると、``fx, fy, cx, cy`` が提供されます。これらは、**AprilTagProcessor** に適用するために必要な較正パラメーターです。
```


## programming_resources/vision/vision_overview/vision-overview.rst

### Block 1 (line 1)

```
コンピュータービジョンの概要
```

### Block 2 (line 4)

```
はじめに
```

### Block 3 (line 7)

```
**FIRST** **Tech Challenge** 制御システムソフトウェアには、2つのコンピュータービジョン技術の組み込みサポートがあります：
```

### Block 4 (line 11)

```
   は、識別とローカライゼーションに使用できる QR コードに似た設計の基準マーカーです。**AprilTags** は、自律ナビゲーションおよびゲームフィールド上の関心点の支援ナビゲーションと識別の参照点として使用されます。
```

### Block 5 (line 13)

```
   -  各シーズン、**FIRST** はナビゲーション参照点として使用できる 2D 画像ターゲットを提供します。
   -  **AprilTag** システムが**AprilTag** 画像を認識すると、ターゲットに対するロボットの位置に関する非常に正確なポーズ情報を提供します（使用されるカメラに作業解像度の較正パラメーターがあると仮定）。
   -  ロボットはこの情報を使用して、フィールド上で自律的にナビゲートできます。
```

### Block 6 (line 17)

```
2. カラー処理 -
   :doc:`カラー処理 </color_processing/index>` は、**FIRST** **Tech Challenge** **SDK** の機能で、`OpenCV <https://opencv.org/>`__ を使用して色を処理する機能を提供します。
```

### Block 7 (line 20)

```
   -  **Color Sensor** は、画像内の正確な色を検出でき、ロボットの前にあるものを判断するのに役立ちます。
   -  **Color Locator** は、特定の色を探し、カメラフレーム内の色のサイズ、形状、位置に関する情報を返すことができます。
   -  ロボットはこの情報を使用して、認識されたオブジェクトにナビゲートできます。
```

### Block 8 (line 24)

```
**AprilTags** 対 カラー処理
```

### Block 9 (line 27)

```
**AprilTag** の利点
```

### Block 10 (line 30)

```
-  高速検出レート（デシメーションとターゲットサイズに応じて、推定毎秒 15 ～ 20 回の検出）で非常に効率的です。
-  フィールド座標でカメラからターゲットへの正確な相対ポーズ情報を提供します。
-  フィールドの変動または変化する照明条件の影響を受けにくいです。
```

### Block 11 (line 38)

```
   **AprilTag** はターゲットへの正確なポーズ情報を提供できます
```

### Block 12 (line 41)

```
**AprilTag** の欠点
```

### Block 13 (line 44)

```
-  正確なポーズ情報を得るには、カメラを較正する必要があります（通常、このプロセスでは、チェッカーボードパターンの複数の画像をキャプチャする必要があります）。
-  **AprilTag** システムは、事前に印刷および配置された**AprilTag** 画像のみを認識します。
-  **AprilTag** は、ゲームエレメントやフィールド上の他のカスタムオブジェクトを識別するために使用することはできません。
```

### Block 14 (line 48)

```
カラー処理の利点
```

### Block 15 (line 51)

```
-  カメラの較正は不要です。
-  ゲーム固有のゲームエレメントやフィールド上のカスタムオブジェクトを識別できます。
```

### Block 16 (line 54)

```
カラー処理の欠点
```

### Block 17 (line 57)

```
-  変動する照明条件の影響を受けやすい可能性があります。
-  フレーム内のオブジェクトの正確なフィールド位置を計算するには、追加の作業が必要です。
```

### Block 18 (line 60)

```
どのシステムを使用するべきか？
```

### Block 19 (line 63)

```
-  **AprilTag** またはカラー処理の両方のシステムを使用して、自律ナビゲーションとオブジェクト識別のタスクを実行できます。
-  **AprilTag** システムは、ロボットがナビゲートして正確に配置する必要がある定義済みの場所がある場合に適しています。
-  カラー処理は、ロボットがゲームエレメントまたはカスタムオブジェクトを識別して応答する必要がある場合に適しています。
```

### Block 20 (line 67)

```
次のステップ
```

### Block 21 (line 70)

```
-  **AprilTag** について詳しく知りたい場合は、:doc:`AprilTag のページ </apriltag/vision_portal/apriltag_intro/apriltag-intro>` を参照してください。
-  カラー処理について詳しく知りたい場合は、:doc:`カラー処理のページ </color_processing/index>` を参照してください。
```


## programming_resources/vision/webcam_controls/eval/eval.rst

### Block 1 (line 1)

```
Webcam の評価
```

### Block 2 (line 4)

```
特定の Webcam のファームウェアは、ここで説明されている特定の機能をサポートする場合としない場合があります。**SDK** は、Webcam にクエリを実行したり、有効な応答が利用可能かどうかを示す値を返したりするいくつかのメソッドを提供します。
```

### Block 3 (line 6)

```
露出サポート
```

### Block 4 (line 9)

```
露出および特定の露出モードをクエリする2つのメソッドを次に示します：
```

### Block 5 (line 14)

```
   -  *mode* には、テストしている特定のモード名を入力します
```

### Block 6 (line 16)

```
次のメソッドでは、露出が利用できない場合、long 型の ``unknownExposure`` というフィールドが返されます：
```

### Block 7 (line 22)

```
露出とモードを設定するメソッドは、Boolean を返すこともできます。おそらく、操作が成功したかどうかを示しています。オプションの例として：
```

### Block 8 (line 27)

```
同様に、AE Priority 機能も Boolean を返すことができます。例：
```

### Block 9 (line 31)

```
ゲインサポート
```

### Block 10 (line 34)

```
ゲインを設定するメソッドは、操作が成功したかどうかを示す Boolean を返すこともできます。オプションの例として：
```

### Block 11 (line 38)

```
ホワイトバランスサポート
```

### Block 12 (line 41)

```
温度とモードを設定するメソッドは、操作が成功したかどうかを示す Boolean を返すこともできます。オプションの例として：
```

### Block 13 (line 46)

```
フォーカスサポート
```

### Block 14 (line 49)

```
フォーカスおよび特定のフォーカスモードをクエリする2つのメソッドを次に示します：
```

### Block 15 (line 54)

```
次のメソッドは、要求されたフォーカス値が利用できない場合、**負の値** を返します。たとえば、Logitech C270 と Microsoft LifeCam VX-5000 は -1 を返します。Javadoc には、double 型の ``unknownFocusLength`` フィールドについても記載されています。
```

### Block 16 (line 60)

```
フォーカス長とモードを設定するメソッドは、おそらく操作が成功したかどうかを示す Boolean を返すこともできます。オプションの例として：
```

### Block 17 (line 65)

```
PTZ サポート
```

### Block 18 (line 68)

```
パン/チルトペアとズーム値を設定するメソッドは、おそらく操作が成功したかどうかを示す Boolean を返すこともできます。オプションの例として：
```

### Block 19 (line 73)

```
PTZ の get() メソッドでは、一部の Webcam はサポートされていない値に対して単に**ゼロを返す** だけです。
```

### Block 20 (line 75)

```
いくつかの注意事項
```

### Block 21 (line 78)

```
-  **SDK** は、`UVC 標準 <https://en.wikipedia.org/wiki/USB_video_device_class>`__ に準拠する Webcam をサポートしています
```

### Block 22 (line 80)

```
   -  多くの非 UVC Webcam は、UVC 認証がなくても、競技会でうまく機能します
   -  一部の非 UVC Webcam は Configure Robot にリストされますが、実行時に RC アプリをクラッシュさせます
```

### Block 23 (line 83)

```
-  Webcam は、プラグを抜いても、割り当てられた露出モードまたはフォーカスモードを保持する場合があります
```

### Block 24 (line 85)

```
   -  常に現在のモードを確認してください
```

### Block 25 (line 87)

```
-  特定の露出値の場合、あるモードのプレビューは、別のモードのプレビューとは大きく異なる場合があります
-  一部の Webcam は、**サポートされていないモード** を**accept**/ ``set()`` し、**confirm** /``get()`` します
-  Logitech C270 のプレビューは、露出 655 まで**明るく** なり、656 で**暗く** なります
```

### Block 26 (line 91)

```
   -  この Webcam の最小値は 0、最大値は 1000 です。
```

### Block 27 (line 93)

```
-  Logitech V-UAX16 のプレビューは、露出 = 0 で正常に見えますが、30-40 まで**暗く** なります
-  Logitech C920 の**ゲイン** 値（0-255）は、プレビュー品質に大きく影響し、**露出** （0-204）に匹敵します
-  Webcam **OpMode** がクラッシュした後、RC アプリの再起動が必要になる場合があります
-  ファームウェアバージョンは、同じモデル番号の Webcam 間で異なる場合があります
```

### Block 28 (line 98)

```
最後に、ここでの一部の機能は、`OpenCV <https://opencv.org/>`__ や `EasyOpenCV <https://github.com/OpenFTC/EasyOpenCV>`__ などの外部ライブラリの助けを借りて実装または強化される可能性があります。その可能性は、この基本チュートリアルでは説明されていません。別のチュートリアルでは、**Blocks** と**OnBot Java** での `外部ライブラリ <https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/External-Libraries-in-OnBot-Java-and-Blocks>`__ の一般的な使用について説明しています。
```


## programming_resources/vision/webcam_controls/exposure/auto_exposure/auto-exposure.rst

### Block 1 (line 1)

```
自動露出優先度
```

### Block 2 (line 4)

```
**AE Priority** （自動露出優先度）は、特定の露出時間を選択する際にガイドとして使用できる設定です。
```

### Block 3 (line 6)

```
AE Priority を ``true`` に設定すると、カメラは手動で設定された露出時間をより重視し、同時にフレームレートをより柔軟に扱うことができます。これは、高速シャッタースピードが必要な場合（モーションブラーを削減するため）や、長い露出時間が必要な場合（暗い環境で）に役立ちます。
```

### Block 4 (line 8)

```
AE Priority を ``false`` に設定すると（デフォルト）、カメラはフレームレートをより重視し、露出時間を調整してフレームレートを維持します。
```

### Block 5 (line 14)

```
   exposureControl.setAePriority(true);  // または false
```

### Block 6 (line 16)

```
このメソッドは **SDK** 7.0 で導入されました。これは**Vuforia** カメラでのみ機能します（**AprilTag** プロセッサーまたは TFOD プロセッサーと組み合わせて使用する場合）。
```

### Block 7 (line 18)

```
**VisionPortal** では、AE Priority は ``VisionPortal.Builder.setCameraMonitorViewId()`` を使用してカメラモニター（DS プレビュー）が有効になっている場合にのみ機能します。
```

### Block 8 (line 20)

```
実験によると、AE Priority が ``true`` に設定されている場合、より長い露出時間（約 40 ミリ秒まで）を設定できます。AE Priority が ``false`` に設定されている場合（デフォルト）、露出時間は約 16 ミリ秒に制限されるようです。
```

### Block 9 (line 22)

```
注：露出時間の設定方法については、:doc:`露出制御 </programming_resources/vision/webcam_controls/exposure/control/control>` を参照してください。
```


## programming_resources/vision/webcam_controls/exposure/control/control.rst

### Block 1 (line 1)

```
露出時間の設定
```

### Block 2 (line 4)

```
露出時間は、カメラのセンサーが光にさらされる時間の長さです。露出時間が長いほど、より多くの光がセンサーに到達し、画像が明るくなります。
```

### Block 3 (line 6)

```
手動で露出時間を設定するには、次の手順を実行します：
```

### Block 4 (line 8)

```
1. 露出モードを手動に設定
2. 希望する露出時間（ナノ秒単位）を設定
```

### Block 5 (line 16)

```
   // 手動モードに設定
```

### Block 6 (line 19)

```
   // 露出時間を 10 ミリ秒（10,000,000 ナノ秒）に設定
```

### Block 7 (line 22)

```
現在の露出時間を取得するには：
```

### Block 8 (line 28)

```
**サポートされる露出範囲を確認する：**
```

### Block 9 (line 35)

```
**重要な注意事項：**
```

### Block 10 (line 37)

```
- 露出時間はナノ秒単位で指定されますが、``TimeUnit`` を使用してミリ秒、マイクロ秒などの他の単位を使用できます。
- サポートされる露出範囲はカメラによって異なります。
- AE Priority が ``true`` に設定されている場合、より長い露出時間を設定できます。詳細については、:doc:`自動露出優先度 </programming_resources/vision/webcam_controls/exposure/auto_exposure/auto-exposure>` を参照してください。
```


## programming_resources/vision/webcam_controls/exposure/index.rst

### Block 1 (line 1)

```
露出制御
```


## programming_resources/vision/webcam_controls/exposure/mode/mode.rst

### Block 1 (line 1)

```
露出モード
```

### Block 2 (line 4)

```
露出モードは、カメラが画像の明るさをどのように調整するかを決定します。
```

### Block 3 (line 6)

```
**自動露出** モードでは、カメラがシーンに基づいて露出時間を自動的に調整します。このモードは、照明条件が変化する場合や、カメラが異なる場所を見ている場合に便利です。
```

### Block 4 (line 8)

```
**手動露出** モードでは、特定の露出時間を設定できます。このモードは、一貫した画像品質が必要な場合や、カメラが静的なシーンを見ている場合に役立ちます。
```

### Block 5 (line 10)

```
露出モードを設定するには、次のコードを使用します：
```

### Block 6 (line 17)

```
   // 手動モードに設定
```

### Block 7 (line 20)

```
   // または自動モードに設定
```

### Block 8 (line 23)

```
露出モードを取得するには：
```

### Block 9 (line 29)

```
**注意** ：手動露出時間を設定する前に、まず手動モードに切り替える必要があります。詳細については、:doc:`露出制御 </programming_resources/vision/webcam_controls/exposure/control/control>` を参照してください。
```


## programming_resources/vision/webcam_controls/exposure/samples/samples.rst

### Block 1 (line 1)

```
露出制御のサンプル
```

### Block 2 (line 4)

```
以下は、露出制御を使用する方法の例です：
```

### Block 3 (line 6)

```
**例1：手動露出時間の設定**
```

### Block 4 (line 13)

```
   // 手動モードに設定
```

### Block 5 (line 16)

```
   // 露出時間を 15 ミリ秒に設定
```

### Block 6 (line 19)

```
**例2：サポートされる範囲の確認**
```

### Block 7 (line 26)

```
   telemetry.addData("最小露出", "%d ms", minExp);
   telemetry.addData("最大露出", "%d ms", maxExp);
```

### Block 8 (line 29)

```
**例3：AE Priority を使用した長い露出時間**
```

### Block 9 (line 33)

```
   // AE Priority を有効化
```

### Block 10 (line 36)

```
   // 手動モードに設定
```

### Block 11 (line 39)

```
   // より長い露出時間（30 ミリ秒）を設定
```

### Block 12 (line 42)

```
詳細については、:doc:`サンプル OpModes </programming_resources/vision/webcam_controls/samples/samples>` を参照してください。
```


## programming_resources/vision/webcam_controls/focus/control/control.rst

### Block 1 (line 1)

```
フォーカス制御
```

### Block 2 (line 6)

```
「フォーカス長」と呼ばれる距離で、被写体の画像（光線）がレンズから収束して、Webcam センサー上に鮮明な画像を形成します。
```

### Block 3 (line 8)

```
Webcam でサポートされている場合、フォーカスは次の **FocusControl** メソッドで管理できます：
```

### Block 4 (line 13)

```
距離単位はここでは指定されていません。許可された範囲内の無次元値である場合があります。たとえば、Logitech C920 は 0 から 250 までの値を許可し、**より高い** 値は**より近い** オブジェクトにフォーカスします。
```

### Block 5 (line 15)

```
Webcam は、フォーカス長の最小値と最大値をサポートする場合があります。これらは次の方法で取得できます：
```

### Block 6 (line 20)

```
最小フォーカス長と最大フォーカス長の ``set()`` メソッドはありません。これらは Webcam のファームウェアにハードコードされています。ファームウェア設定は、同じ Webcam モデルの異なるバージョン間で異なる場合があることに注意してください。
```

### Block 7 (line 22)

```
これらおよび他のフォーカスメソッドは、露出について上記で説明したように、**FocusControl** オブジェクトで呼び出されます。
```


## programming_resources/vision/webcam_controls/focus/index.rst

### Block 1 (line 1)

```
フォーカス制御
```


## programming_resources/vision/webcam_controls/focus/mode/mode.rst

### Block 1 (line 1)

```
フォーカス制御モード
```

### Block 2 (line 6)

```
Webcam は、さまざまなフォーカスモードのいずれかで動作する場合があります。フォーカス長を直接制御するには、Webcam を Fixed モードに設定します。
```

### Block 3 (line 8)

```
**SDK** は、**FocusControl.Mode** の次の値をサポートしています：
```

### Block 4 (line 17)

```
モードは、これらの **FocusControl** メソッドで管理されます：
```

### Block 5 (line 22)

```
Logitech C920 Webcam は、**ContinuousAuto** と**Fixed** の2つのモードを提供し、**FocusControl** メソッドに応答します。Logitech C270（古いモデル）は**Fixed** モードのみを提供しますが、プログラムによる制御は許可されません。
```

### Block 6 (line 24)

```
詳細は、`FocusControl Javadoc <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/org/firstinspires/ftc/robotcore/external/hardware/camera/controls/FocusControl.html>`__ に記載されています。
```


## programming_resources/vision/webcam_controls/gain/control/control.rst

### Block 1 (line 1)

```
ゲイン制御
```

### Block 2 (line 6)

```
ゲインは、Webcam センサーからの信号の増幅を制御するデジタルカメラ設定です。これにより、関連するバックグラウンドノイズを含む信号全体が増幅されます。
```

### Block 3 (line 8)

```
ゲインは露出と連携して管理できます。露出を上げてゲインを低く保つと、明るい画像と低ノイズを実現できます。一方、長い露出はモーションブラーを引き起こす可能性があり、ターゲット追跡パフォーマンスに影響を与える可能性があります。場合によっては、露出時間を短縮してゲインを増やすと、ノイズは多くなりますが、よりシャープな画像が得られる可能性があります。
```

### Block 4 (line 10)

```
インターフェイス **GainControl** は、単一の値を使用してゲインを制御します。これは増幅に使用されるため、単位はありません - 整数型の単なる数値です。そのメソッドは次のとおりです：
```

### Block 5 (line 15)

```
露出と同様に、Webcam はゲインの最小値と最大値をサポートする場合があります。これらは次の方法で取得できます：
```

### Block 6 (line 20)

```
最小ゲインと最大ゲインの ``set()`` メソッドはありません。これらは Webcam のファームウェアにハードコードされています。ファームウェア設定は、同じ Webcam モデルの異なるバージョン間で異なる場合があることに注意してください。
```

### Block 7 (line 22)

```
これらおよび他のゲインメソッドは、露出について上記で説明したように、**GainControl** オブジェクトで呼び出されます。
```


## programming_resources/vision/webcam_controls/gain/ex1/ex1.rst

### Block 1 (line 1)

```
例1：露出の TFOD への影響
```

### Block 2 (line 4)

```
このチュートリアルを中断して、これまでに説明した2つの Webcam インターフェイス：**ExposureControl** と**GainControl** を実証します。
```

### Block 3 (line 6)

```
これらの2つの例では、**Freight Frenzy** ゲームで**TensorFlow Object Detection (TFOD)** を既に使用していることを前提としています。つまり、**TFOD** モデルと、適度にうまく機能する**OpMode** があります。ここでは、Duck ゲームエレメントのみについて説明します。** 露出および/またはゲイン制御により、高速で正確な TFOD 検出の可能性が向上しますか？**
```

### Block 4 (line 8)

```
この取り組みを別の方法でフレーム化すると、これらの制御は **TFOD** モデルトレーニングに使用される照明条件をシミュレートできますか？つまり、競技フィールドに認識に影響を与える異なる照明がある場合、** 元の（トレーニング済み）TFOD パフォーマンス** に近い状態を達成できますか？
```

### Block 5 (line 10)

```
まず、露出のみを試します。ゲインをゼロに設定し、さまざまな露出値で Webcam 画像に **TFOD** を適用します。
```

### Block 6 (line 15)

```
   ゲイン 0、露出 0 -> 20
```

### Block 7 (line 20)

```
   ゲイン 0、露出 23 -> 40
```

### Block 8 (line 25)

```
   ゲイン 0、露出 45 -> 55
```

### Block 9 (line 27)

```
各露出設定で**5回の新しい読み取り** が行われました。つまり、テスト**OpMode** が毎回開かれ（INIT）、新しい**TFOD** 初期化と Webcam 画像処理が行われました。
```

### Block 10 (line 29)

```
このチャートは **TFOD** 信頼度レベルを示しています。ここでの「instant」は、1秒以内の認識として定義されています。
```

### Block 11 (line 35)

```
   各露出レベルでの5回の読み取り
```

### Block 12 (line 37)

```
露出を高くすると認識が向上しますが、その後パフォーマンスが突然低下します。その後、より高いレベルでは、この **TFOD** モデルは Duck ではなく Cube を「見る」ようになります。良くありません！
```

### Block 13 (line 39)

```
したがって、より良い結果を提供する露出値の範囲があるようです。範囲の両端での急激な低下に注意してください：25 未満と 40 以上。エンジニアリングでは、**堅牢な** ソリューションは変動に耐えることができます。改善された範囲の中央の値を使用すると、予期しない変動の影響を減らすことができます。ただし、この範囲は周囲の照明条件によって異なり、トーナメント会場では大きく異なる場合があります。
```

### Block 14 (line 41)

```
このデータは、Webcam モデル（Logitech C270）、距離（12インチ）、俯角（30度）、**TFOD** モデル（**SDK** 7.0 デフォルト）、周囲照明、背景などの非常に特定の組み合わせの結果です。**結果は、おそらく大幅に異なります。**
```


## programming_resources/vision/webcam_controls/gain/ex2/ex2.rst

### Block 1 (line 1)

```
例2：ゲインの TFOD への影響
```

### Block 2 (line 4)

```
次に、ゲインのみを調整します。露出を 15 の固定値に設定します。これは、例1でパフォーマンスが悪かったため選択されました。**ゲインは役立ちますか？**
```

### Block 3 (line 9)

```
   露出 15、ゲイン 000 -> 035
```

### Block 4 (line 14)

```
   露出 15、ゲイン 040 -> 060
```

### Block 5 (line 19)

```
   露出 15、ゲイン 070 -> 100
```

### Block 6 (line 22)

```
各ゲイン設定で5回の新しい読み取りが行われました。
```

### Block 7 (line 27)

```
   各ゲインレベルでの5回の読み取り
```

### Block 8 (line 29)

```
ゲインを高くすると認識が向上しますが、その後パフォーマンスが低下します。その後、より高いレベルでは、この **TFOD** モデルは Duck ではなく Cube を「見る」ようになります。ゲインの効果は露出の効果と似ていました。
```

### Block 9 (line 31)

```
これら2つのチャートは、**TFOD** の結果が影響を受け、露出とゲインの特定の値を設定することで最適化できる可能性があることを示唆しています。チームは、これを予想される試合条件の全範囲で、ロボットと Webcam のデフォルトまたは自動パフォーマンスと比較する必要があります。
```


## programming_resources/vision/webcam_controls/gain/ex3/ex3.rst

### Block 1 (line 1)

```
例3：奇妙なプレビュー
```

### Block 2 (line 7)

```
   **TFOD** はこの認識を行いましたか？
```

### Block 3 (line 10)

```
これはどうしてでしょうか？答え：この画像は「instant」の結果ではありませんでした。**TFOD** が Duck を認識した** 後** 、露出が非常に低く減らされました。
```

### Block 4 (line 12)

```
**TensorFlow Lite** （および**Vuforia** ）の実装は、現在識別されているオブジェクト（または画像）を、平行移動、回転、部分的なブロッキング、さらには露出の極端な変化を通じて** 追跡** するのが得意です。
```


## programming_resources/vision/webcam_controls/gain/index.rst

### Block 1 (line 1)

```
ゲイン制御
```


## programming_resources/vision/webcam_controls/index.rst

### Block 1 (line 1)

```
Webcam 制御
```

### Block 2 (line 4)

```
この基本チュートリアルでは、**SDK** で利用可能な 8つの Webcam 制御について説明します。これには、**Freight Frenzy** で**TensorFlow** 認識を改善する可能性がある、これらの制御のうち 2つを使用する例が含まれています。
```

### Block 3 (line 6)

```
これらの Webcam 制御を開発した `rgatkinson <https://github.com/rgatkinson>`__ さんと `Windwoes <https://github.com/Windwoes>`__ さんに敬意を表します。
```

### Block 4 (line 21)

```
まとめ
```

### Block 5 (line 24)

```
**SDK** の一部の Webcam 制御は、**TFOD** 認識を改善する可能性があります。露出、ゲイン、その他の値は、チームの**Autonomous** **OpMode** で事前にプログラムできます。また、予想される照明、開始位置、その他の試合時の要因に基づいて、試合が始まる前にそのような値を手動で入力することもできます。
```

### Block 6 (line 26)

```
役に立った他の Webcam レポートと例を提出することをお勧めします。
```

### Block 7 (line 30)

```
質問、コメント、修正は westsiderobotics@verizon.net までお願いします。
```


## programming_resources/vision/webcam_controls/overview/overview.rst

### Block 1 (line 1)

```
ソフトウェアの概要
```

### Block 2 (line 4)

```
**SDK** には、**CameraControl** と呼ばれるスーパーインターフェイスが含まれており、5つのインターフェイスが含まれています：
```

### Block 3 (line 8)

```
- :doc:`WhiteBalanceControl </programming_resources/vision/webcam_controls/white_balance/index>` （**SDK** 7.1 の新機能）
```

### Block 4 (line 12)

```
Java クラスと同様に、Java インターフェイスはメソッドを提供します。Webcam は、これら5つのインターフェイスのメソッドを使用して制御できます。
```

### Block 5 (line 14)

```
**PtzControl** では、仮想パン、チルト、ズームの3つの関連機能を制御できます。**ExposureControl** には、自動露出優先度、または AE Priority と呼ばれる機能も含まれています。このチュートリアルでは、合わせて**8つの Webcam 制御** について説明します。
```

### Block 6 (line 16)

```
公式ドキュメントは `Javadocs <https://javadoc.io/doc/org.firstinspires.ftc>`__ にあります。**RobotCore** のリンクをクリックし、左側の列の**CameraControl** リンクをクリックします。
```

### Block 7 (line 23)

```
そのページには、上記の5つのインターフェイスへのリンクがあります。
```

### Block 8 (line 25)

```
ここで説明するメソッドは、**Android Studio** または**OnBot Java** で使用できます。また、別の :ref:`Blocks プログラミングチュートリアル <programming_resources/blocks/blocks-tutorial:blocks programming tutorial>` で説明されている**myBlocks** を作成することで、**Blocks** プログラマーに提供することもできます。
```

### Block 9 (line 27)

```
ここと、以下の `サンプル OpModes <#sample-opmodes>`__ で **Vuforia** について言及されています。** なぜ Vuforia なのか？** **FIRST** **Tech Challenge** の Google の**TensorFlow Lite** の実装は、**Vuforia** ビデオストリームからカメラ画像を受信します。**SDK** にはすでに**Vuforia** がナビゲーション用に含まれており、使用されているため、カメラストリームを**TFOD** に渡すための便利なツールです。
```

### Block 10 (line 29)

```
これらの **CameraControl** インターフェイスにより、独自のパフォーマンスのための**Vuforia** の要件または設定内で、Webcam をある程度制御できます。このような設定には、ここでは説明しない解像度とフレームレートが含まれます。
```


## programming_resources/vision/webcam_controls/ptz/index.rst

### Block 1 (line 1)

```
PTZ 制御
```

### Block 2 (line 4)

```
PTZ は、パン（Pan）、チルト（Tilt）、ズーム（Zoom）の略です。
```


## programming_resources/vision/webcam_controls/ptz/pan_tilt/pan-tilt.rst

### Block 1 (line 1)

```
パンとチルト
```

### Block 2 (line 4)

```
Webcam は通常、パンとチルトの値を*ピクセル*（Webcam センサーによる画像キャプチャの最小単位）で表現しません。たとえば、Logitech C920 と Microsoft LifeCam VX-5000 の範囲は +/-36,000 ユニットで、各軸のピクセル数よりもはるかに大きくなっています。
```

### Block 3 (line 6)

```
Webcam は、パンとチルトを (x, y) 値のペアとして受け入れます。したがって、**SDK** のパンおよびチルトメソッドは、これらの値を**PanTiltHolder** という名前の特別なクラスで** ペアとしてのみ** 処理します。このクラスには、整数型の pan と tilt という2つのフィールドがあります。
```

### Block 4 (line 8)

```
基本メソッドの使用を説明する例を次に示します：
```

### Block 5 (line 12)

```
   myHolder.pan = 5;                  // pan フィールドを割り当てる
   myHolder.tilt = 10;                // tilt フィールドを割り当てる
   myPtzControl.setPanTilt(myHolder);         // (x, y) ペアで Webcam にコマンドを送る
```

### Block 6 (line 16)

```
Webcam から値を取得するには：
```

### Block 7 (line 20)

```
   newHolder = myPtzControl.getPanTilt();      // Webcam から (x, y) ペアを取得
   int currentPanValue = newHolder.pan;        // pan 値にアクセス
   int currentTiltValue = newHolder.tilt;      // tilt 値にアクセス
```

### Block 8 (line 24)

```
上記の例では、これらのオブジェクトが既に存在することを前提としています：
```

### Block 9 (line 28)

```
   PtzControl myPtzControl = vuforia.getCamera().getControl(PtzControl.class); // PTZ Webcam 制御オブジェクトを作成
   PtzControl.PanTiltHolder myHolder = new PtzControl.PanTiltHolder();         // 入力ホルダーオブジェクトをインスタンス化
   PtzControl.PanTiltHolder newHolder;                                 // 出力ホルダーオブジェクトを宣言
```

### Block 10 (line 32)

```
Webcam は、許可された最小および最大のパン/チルトペア値をサポートする場合があります。上記の制御オブジェクトのガイドラインに従って、これらは次のように取得できます：
```

### Block 11 (line 37)

```
最小および最大のパン/チルト値の ``set()`` メソッドはありません。これらは Webcam のファームウェアにハードコードされています。ファームウェア設定は、同じ Webcam モデルの異なるバージョン間で異なる場合があることに注意してください。
```

### Block 12 (line 39)

```
これらのパンおよびチルトメソッドは、露出について上記で説明したように、**PtzControl** オブジェクトで呼び出されます。
```


## programming_resources/vision/webcam_controls/ptz/zoom/zoom.rst

### Block 1 (line 1)

```
ズーム
```

### Block 2 (line 4)

```
仮想ズームは、整数型の単一の無次元値で記述されます。上記で説明したインターフェイスと同様に、仮想ズームは次のメソッドで管理できます：
```

### Block 3 (line 11)

```
Logitech C920 は、100 から 500 までのズーム値を許可しますが、250-280 より高い値は、プレビュー画像にさらなる影響を与えません（**Vuforia** の影響を受けます）。
```

### Block 4 (line 13)

```
これらのズームメソッドは、露出について上記で説明したように、**PtzControl** オブジェクトで呼び出されます。
```


## programming_resources/vision/webcam_controls/samples/samples.rst

### Block 1 (line 1)

```
サンプル **OpModes**
```

### Block 2 (line 4)

```
このチュートリアルの目的は、利用可能な Webcam 制御について説明し、プログラマーが **SDK** API（Javadoc）に基づいて**独自のソリューションを開発** できるようにすることです。
```

### Block 3 (line 6)

```
以下のサンプル **OpModes** は、参照のみを目的としてここにリンクされています。これらの初歩的な **OpModes** は、Webcam に適用されない場合があり、一般的にニーズを満たさない場合があります。
```


## programming_resources/vision/webcam_controls/white_balance/control/control.rst

### Block 1 (line 1)

```
ホワイトバランス制御
```

### Block 2 (line 6)

```
他のインターフェイスに続いて、**SDK** （バージョン 7.1 の新機能）は、ホワイトバランス制御のメソッドを提供します。
```

### Block 3 (line 8)

```
ホワイトバランスは、画像内の**色温度** のバランスをとるデジタルカメラ設定です。色温度はケルビン度（K）の単位で測定され、光の物理的特性です。
```

### Block 4 (line 10)

```
たとえば、正午の日光は 5200-6000 K の間で測定されます。白熱電球（暖かい/オレンジ）の色温度は約 3000 K ですが、日陰（涼しい/青）は約 8000 K で測定されます。
```

### Block 5 (line 12)

```
自動で実行されると、ホワイトバランスは色温度を中立に戻すために、画像に反対の色を追加します。このインターフェイス **WhiteBalanceControl** により、色温度をユーザーが直接プログラムできます。
```

### Block 6 (line 14)

```
ここでは、ホワイトバランス温度を制御するために、Java タイプの整数で、ケルビン度の単位で単一の値が使用されます。メソッドは次のとおりです：
```

### Block 7 (line 19)

```
露出やゲインと同様に、Webcam はホワイトバランス温度の最小値と最大値をサポートする場合があります。これらは次の方法で取得できます：
```

### Block 8 (line 24)

```
最小温度値と最大温度値の ``set()`` メソッドはありません。これらは Webcam のファームウェアにハードコードされています。ファームウェア設定は、同じ Webcam モデルの異なるバージョン間で異なる場合があることに注意してください。
```

### Block 9 (line 26)

```
Logitech C920 Webcam の最小値は 2000、最大値は 6500 です。
```


## programming_resources/vision/webcam_controls/white_balance/index.rst

### Block 1 (line 1)

```
ホワイトバランス制御
```


## programming_resources/vision/webcam_controls/white_balance/mode/mode.rst

### Block 1 (line 1)

```
ホワイトバランス制御モード
```

### Block 2 (line 6)

```
このインターフェイスは、**WhiteBalanceControl.Mode** の3つの値をサポートしています：
```

### Block 3 (line 12)

```
カラーバランス温度を直接制御するには、Webcam を Manual モードに設定します。モードは、これらの **WhiteBalanceControl** メソッドで管理されます：
```

### Block 4 (line 17)

```
Logitech C920 は、ホワイトバランス制御のデフォルトとして Auto モードになっており、前のセッションで Manual に設定された後でも、新しいセッションでは Auto に戻ります。他の **CameraControl** 設定では、一部の Webcam はデフォルト値に戻り、一部は最後にコマンドされた値を保持します。
```


## team_resources/team_resources.rst

### Block 1 (line 1)

```
チームリソース
```

### Block 2 (line 4)

```
*FIRST* Tech Challenge シーズンを通じて、チームがアクセスしたいと思ういくつかのリソースがあります。
```

### Block 3 (line 6)

```
ページとリンク
```

