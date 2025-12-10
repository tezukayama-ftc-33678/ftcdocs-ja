# FTC ドキュメント 翻訳指示書（AI翻訳ツール向け）

このドキュメントは、AI翻訳ツール（DeepL、ChatGPT、Claude等）を使用してFTCドキュメントを日本語化する際に、**翻訳AIに直接渡すための統合指示書**です。

---

## 📚 必読：関連ドキュメント

このドキュメントは以下の既存ドキュメントに基づいています。翻訳作業前に必ず参照してください：

### 1. **TRANSLATION_GUIDE.md** - 翻訳ガイドライン
- 翻訳の基本方針（文体、固有名詞の扱い、著作権）
- 用語の取り扱いルール
- ブランチ運用とコミットルール
- **必読項目:** セクション1（翻訳の基本方針）、セクション2（用語の取り扱いルール）

### 2. **GLOSSARY.md** - 翻訳用語集
- 和訳しない用語の完全リスト（API名、製品名、組織名等）
- 和訳・カタカナ表記する用語の統一リスト
- 用語の使用例と備考
- **必読項目:** 全セクション（特に「和訳しない用語」）

### 3. **TRANSLATION_WORKFLOW_TOOLS.md** - 作業効率化ツール
- 推奨ツールとワークフロー
- 翻訳進捗チェックスクリプトの使用方法
- 品質保証プロセス
- **参考項目:** セクション2（作業支援Pythonスクリプト）

**このドキュメントは上記3つのドキュメントを「AI翻訳実践向け」にまとめた簡易版です。**
**詳細な背景やルールの根拠については、必ず元のドキュメントを参照してください。**

---

## 📋 翻訳の基本ルール

### 1. 文体
- **「です・ます」調**で統一してください
- 読者への呼びかけは「皆さん」または「読者の方」を使用してください
- 「あなた」「君」などの二人称は使用しないでください

### 2. 句読点
- 読点：「、」（全角）
- 句点：「。」（全角）
- コロン：「：」（全角）
- セミコロン：「；」（全角）

### 3. 長音符号
- カタカナ語の長音符号（ー）は**省略しないでください**
  - 正: コンピューター、パラメーター、ユーザー
  - 誤: コンピュータ、パラメータ、ユーザ

---

## ⚠️ 重要：英語を残すべき用語の扱い

### 【最重要ルール】英語を残す用語は必ず太字（**用語**）で表記

以下のカテゴリに該当する用語は**翻訳せず、英語のまま太字で残してください**。
この太字表記は、翻訳品質チェックスクリプトが技術用語を正しく認識するために必須です。

**書式例：**
```markdown
**OpMode** を使用してロボットを制御します。
**Control Hub** に接続してください。
**AprilTag** による位置認識を実装します。
```

---

## 📚 和訳しない用語リスト（必ず太字で残す）

### API/クラス名
| 英語（太字で残す） | 使用例 |
|------|------|
| **OpMode** | **OpMode** を作成します |
| **Op Mode** | この **Op Mode** を実行します |
| **LinearOpMode** | **LinearOpMode** を継承します |
| **Telemetry** | **Telemetry** でデータを表示します |
| **HardwareMap** | **HardwareMap** を使用します |
| **VisionPortal** | **VisionPortal** を初期化します |

### 制御モード
| 英語（太字で残す） | 使用例 |
|------|------|
| **Autonomous** | **Autonomous** モードで動作します |
| **TeleOp** | **TeleOp** プログラムを作成します |

### ハードウェア製品名
| 英語（太字で残す） | 使用例 |
|------|------|
| **Control Hub** | **Control Hub** に接続します |
| **Expansion Hub** | **Expansion Hub** を設定します |
| **REV Robotics Control Hub** | **REV Robotics Control Hub** を使用します |
| **REV Robotics Expansion Hub** | **REV Robotics Expansion Hub** を接続します |
| **Driver Hub** | **Driver Hub** の電源を入れます |
| **Driver Station** | **Driver Station** アプリを開きます |
| **DRIVER STATION** | **DRIVER STATION** に接続します |
| **Robot Controller** | **Robot Controller** を起動します |
| **IMU** | **IMU** センサーを較正します |
| **HuskyLens** | **HuskyLens** を設定します |

### アプリ/ソフトウェア名
| 英語（太字で残す） | 使用例 |
|------|------|
| **Blocks** | **Blocks** でプログラミングします |
| **OnBot Java** | **OnBot Java** を使用します |
| **Android Studio** | **Android Studio** をインストールします |
| **Robot Controller App** | **Robot Controller App** を更新します |
| **Driver Station App** | **Driver Station App** を開きます |

### ビジョン/画像処理
| 英語（太字で残す） | 使用例 |
|------|------|
| **AprilTag** | **AprilTag** を検出します |
| **OpenCV** | **OpenCV** ライブラリを使用します |
| **EasyOpenCV** | **EasyOpenCV** を実装します |
| **VisionPortal** | **VisionPortal** を初期化します |
| **Camera Stream** | **Camera Stream** を確認します |
| **Color Locator** | **Color Locator** を使用します |

### 組織名/プログラム名
| 英語（太字で残す） | 使用例 |
|------|------|
| **FIRST** | **FIRST** の理念に基づきます |
| **FIRST Tech Challenge (FTC)** | **FIRST Tech Challenge (FTC)** に参加します |
| **Gracious Professionalism** | **Gracious Professionalism** を実践します |

### UI/機能名
| 英語（太字で残す） | 使用例 |
|------|------|
| **Settings** | **Settings** を開きます |
| **Camera Stream** | **Camera Stream** を確認します |
| **Team Prop** | **Team Prop** を認識します |
| **Color Locator** | **Color Locator** を使用します |
| **Access Codes** | **Access Codes** を入力します |
| **Self Inspect** | **Self Inspect** を実行します |
| **Inspection Reports** | **Inspection Reports** を表示します |

### その他の固有名詞
| 英語（太字で残す） | 使用例 |
|------|------|
| **Awards** | **Awards** に応募します |

---

## 🔤 和訳またはカタカナ表記する用語

以下の一般的な技術用語は、指定された日本語/カタカナ語に統一してください。

### プログラミング関連
| 英語 | 統一訳語 |
|------|---------|
| Debugging | デバッグ |
| Feature | 機能 |
| Variable | 変数 |
| Parameter | パラメーター |
| Framework | フレームワーク |
| Build | ビルド |
| Component | コンポーネント |
| Repository | リポジトリ |
| Tutorial | チュートリアル |
| Documentation | ドキュメント |
| Configuration | 構成 |
| System | システム |
| Resource | リソース |
| Software | ソフトウェア |
| Hardware | ハードウェア |

### FTC競技関連
| 英語 | 統一訳語 |
|------|---------|
| Team | チーム |
| Coach | コーチ |
| Mentor | メンター |
| Competition | 競技 |
| Field | フィールド |
| Match | マッチ |
| Alliance | アライアンス |
| Robot | ロボット |
| Game Manual | 競技マニュアル |
| Season | シーズン |
| Championship | チャンピオンシップ |
| Portfolio | ポートフォリオ |
| Judging | 審査 |
| Inspection | 検査 |
| Event | イベント |
| Rookie Team | 新規チーム |
| Veteran Team | 既存チーム |

### UI/操作関連
| 英語 | 統一訳語 |
|------|---------|
| Button | ボタン |
| Link | リンク |
| Menu | メニュー |
| Click | クリック |
| Select | 選択する |
| Download | ダウンロード |
| Upload | アップロード |
| Install | インストール |
| Dashboard | ダッシュボード |
| Registration | 登録 |

---

## 🚫 翻訳してはいけないもの

### 1. コードブロック内のコード
```java
// このコード部分は翻訳しないでください
public class MyOpMode extends LinearOpMode {
    @Override
    public void runOpMode() {
        // コメントのみ翻訳可能
    }
}
```

### 2. reStructuredText (RST) のディレクティブ
```rst
.. note::
   ← このディレクティブは翻訳しないでください
   
:doc:`リンクテキストのみ翻訳 </path/to/file>`
:ref:`参照テキストのみ翻訳 <label>`
```

### 3. URL とファイルパス
```
https://www.firstinspires.org/
/docs/source/programming_resources/index.rst
```

### 4. ファイル名と拡張子
```
config.xml
MyOpMode.java
README.md
```

---

## ✅ 翻訳例

### 良い例 ✓

**原文:**
```
Create a new OpMode using the Blocks programming environment. 
The OpMode will control the robot during the Autonomous period.
Connect your Control Hub to the Driver Station app.
```

**正しい翻訳:**
```
**Blocks** プログラミング環境を使用して新しい **OpMode** を作成します。
この **OpMode** は **Autonomous** 期間中にロボットを制御します。
**Control Hub** を **Driver Station** アプリに接続してください。
```

### 悪い例 ✗

**誤った翻訳1（太字なし）:**
```
Blocks プログラミング環境を使用して新しい OpMode を作成します。
```
→ **問題:** 技術用語が太字になっていないため、品質チェックで誤検出されます

**誤った翻訳2（用語を和訳）:**
```
**ブロックス** プログラミング環境を使用して新しい**操作モード**を作成します。
```
→ **問題:** 固有名詞を翻訳してしまっています

**誤った翻訳3（コードを翻訳）:**
```java
public class 私のオプモード extends リニアオプモード {
```
→ **問題:** コードを翻訳してはいけません

---

## 📝 翻訳時のチェックリスト

翻訳完了後、以下を確認してください：

- [ ] API名やクラス名（OpMode、Telemetry等）を**太字の英語**で残しているか
- [ ] 製品名（Control Hub、Driver Station等）を**太字の英語**で残しているか
- [ ] アプリ名（Blocks、OnBot Java等）を**太字の英語**で残しているか
- [ ] **FIRST** および **Gracious Professionalism** を**太字の英語**で残しているか
- [ ] 文体が「です・ます」調で統一されているか
- [ ] カタカナ語の長音符号（ー）を省略していないか
- [ ] コードブロック内のコードを翻訳していないか
- [ ] RSTディレクティブ（:doc:、:ref:等）を翻訳していないか
- [ ] URL やファイルパスを翻訳していないか

---

## 🎯 翻訳品質チェックについて

翻訳後、自動品質チェックスクリプトが以下を検出します：

1. **文末に英語が残っている箇所**
   - 例: 「これは説明です for testing purposes.」← 検出される

2. **太字なしで3語以上の英単語が連続している箇所**
   - 例: 「これは how to configure the system です」← 検出される
   - 例: 「これは **how to configure the system** です」← 太字なので検出されない

3. **完全に英語のままの段落**
   - 翻訳漏れとして検出されます

**太字（****）で英語の技術用語を囲むことで、これらが意図的に残された用語であることを明示し、誤検出を防ぎます。**

---

## 💡 翻訳のコツ

### 1. 技術用語は辞書登録
頻出する技術用語（OpMode、Control Hub等）は、翻訳ツールの用語集機能や辞書に登録しておくと効率的です。

### 2. 文脈を考慮
単語単位ではなく、文章全体の意味を理解して翻訳してください。

### 3. 自然な日本語に
直訳調ではなく、日本語として自然で読みやすい表現を心がけてください。

### 4. 一貫性を保つ
同じ原文が繰り返し出てきた場合、同じ訳語を使用してください。

---

## 🔗 詳細情報とトラブルシューティング

### より詳しい情報が必要な場合

- **用語の扱いに迷った場合:** `GLOSSARY.md` の完全版を参照（更新履歴も確認）
- **翻訳方針の背景を知りたい場合:** `TRANSLATION_GUIDE.md` のセクション1～3を参照
- **作業フローやツールについて:** `TRANSLATION_WORKFLOW_TOOLS.md` を参照
- **進捗確認と品質チェック:** `TRANSLATION_PROGRESS.md` で現状を確認

### 用語追加が必要な場合

新しい技術用語を発見した場合：
1. まず `GLOSSARY.md` で既存の用語を検索
2. 見つからない場合は `TRANSLATION_GUIDE.md` のルールに従って判断
3. PRに用語追加の提案を含める

---

## 📝 使用方法

**AI翻訳ツールへの渡し方:**

1. このドキュメント全体をコピー
2. 翻訳対象のRSTファイルの内容を追加
3. 「上記の指示に従って、以下のRSTファイルを日本語に翻訳してください」と指示

**例:**
```
[このドキュメントの内容]

---

以下のRSTファイルを、上記の翻訳指示書に従って日本語に翻訳してください：

[翻訳対象のRSTファイルの内容]
```

---

**このドキュメントを翻訳AIへのプロンプトと共に提示することで、一貫性のある高品質な翻訳を実現できます。**
