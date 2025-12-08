# FTC ドキュメント 翻訳用語集

このドキュメントは、FTC ドキュメントの日本語翻訳プロジェクトで使用される統一用語のリストです。
**TRANSLATION_GUIDE.md** に準拠し、翻訳の一貫性を保つために使用します。

---

## 📚 用語カテゴリ

### 1. 和訳しない用語（英語のまま太字で表記）

#### API/クラス名
| 英語 | 表記 | 備考 |
|------|------|------|
| OpMode | **OpMode** | コードに登場する固有名詞 |
| LinearOpMode | **LinearOpMode** | コードに登場する固有名詞 |
| Telemetry | **Telemetry** | コードに登場する固有名詞 |
| HardwareMap | **HardwareMap** | コードに登場する固有名詞 |
| Robot Controller | **Robot Controller** | アプリ名 |
| Driver Station | **Driver Station** | アプリ名 |
| VisionPortal | **VisionPortal** | API名 |

#### 制御モード
| 英語 | 表記 | 備考 |
|------|------|------|
| Autonomous | **Autonomous** | 競技フィールドでの操作モード |
| TeleOp | **TeleOp** | 競技フィールドでの操作モード |

#### ハードウェア製品名
| 英語 | 表記 | 備考 |
|------|------|------|
| REV Robotics Control Hub | **REV Robotics Control Hub** | 製品名 |
| REV Robotics Expansion Hub | **REV Robotics Expansion Hub** | 製品名 |
| DRIVER STATION | **DRIVER STATION** | 製品名 |
| IMU | **IMU** | センサー名（Inertial Measurement Unit） |
| Control Hub | **Control Hub** | 製品名 |
| Driver Hub | **Driver Hub** | 製品名 |

#### ビジョンと画像処理
| 英語 | 表記 | 備考 |
|------|------|------|
| AprilTag | **AprilTag** | 画像認識技術名 |
| OpenCV | **OpenCV** | ライブラリ名 |
| EasyOpenCV | **EasyOpenCV** | ライブラリ名 |

#### プログラミング環境
| 英語 | 表記 | 備考 |
|------|------|------|
| Blocks | **Blocks** | プログラミング環境名 |
| OnBot Java | **OnBot Java** | プログラミング環境名 |
| Android Studio | **Android Studio** | IDE名 |

#### その他の固有名詞
| 英語 | 表記 | 備考 |
|------|------|------|
| FIRST | **FIRST** | 組織名（For Inspiration and Recognition of Science and Technology） |
| FIRST Tech Challenge (FTC) | **FIRST Tech Challenge (FTC)** | プログラム名 |
| Gracious Professionalism | **Gracious Professionalism** | FIRST の理念（登録商標） |

---

### 2. 和訳またはカタカナ表記する用語

#### 一般的な技術用語
| 英語 | 統一訳語/カタカナ語 | 備考 |
|------|------------------|------|
| Debugging | デバッグ | 「デバッギング」ではない |
| Feature | 機能 | 「フィーチャー」ではない |
| Variable | 変数 | 「ヴァリアブル」ではない |
| Parameter | パラメーター | 長音符号を省略しない |
| Framework | フレームワーク | カタカナ語として使用 |
| Build | ビルド | ソフトウェアの構築作業 |
| Component | コンポーネント | 部品、構成要素 |
| Repository | リポジトリ | 「レポジトリ」ではない |
| Tutorial | チュートリアル | |
| Documentation | ドキュメント | |
| Configuration | 構成 | 「コンフィギュレーション」ではない |
| System | システム | |
| Resource | リソース | |
| Software | ソフトウェア | |
| Hardware | ハードウェア | |

#### FTC 固有の用語（和訳するもの）
| 英語 | 統一訳語 | 備考 |
|------|---------|------|
| Team | チーム | |
| Coach | コーチ | |
| Mentor | メンター | |
| Competition | 競技 | |
| Field | フィールド | 競技場 |
| Match | マッチ | 試合 |
| Alliance | アライアンス | |
| Robot | ロボット | |
| Game Manual | 競技マニュアル | |
| Season | シーズン | |
| Championship | チャンピオンシップ | |
| Portfolio | ポートフォリオ | |
| Judging | 審査 | |
| Inspection | 検査 | |
| Awards | 表彰 | |
| Event | イベント | |
| Rookie Team | 新規チーム | |
| Veteran Team | 既存チーム | |

#### UI/操作関連
| 英語 | 統一訳語 | 備考 |
|------|---------|------|
| Button | ボタン | |
| Link | リンク | |
| Menu | メニュー | |
| Click | クリック | |
| Select | 選択する | |
| Download | ダウンロード | |
| Upload | アップロード | |
| Install | インストール | |
| Dashboard | ダッシュボード | |
| Registration | 登録 | |
| FAQ | FAQ / よくある質問 | |
| Question Box | クエスチョンボックス | 競技会場での質問受付場所 |

---

## 📝 翻訳スタイルガイド

### 文体
- **「です・ます」調** で統一
- 読者への呼びかけは「皆さん」や「読者の方」
- 「あなた」や「君」といった呼びかけは避ける

### 技術用語の扱い
1. **コード内のクラス名、API名は英語のまま太字**で表記
2. **製品名は英語のまま太字**で表記
3. 一般的な技術用語は適切に和訳またはカタカナ表記
4. 長音符号（ー）は省略しない（例: パラメーター、コンピューター）

### 句読点
- 読点：「、」
- 句点：「。」
- コロン：「：」（全角）
- セミコロン：「；」（全角）

---

## 🔄 用語追加プロセス

新しい用語を発見した場合：

1. **TRANSLATION_GUIDE.md** を参照し、既存のルールに従う
2. 既存の用語リストにない場合は、このGLOSSARY.mdに追加
3. PR作成時に用語追加を明記する
4. レビュー時に用語の適切性を確認

---

## 📅 更新履歴

| 日付 | バージョン | 更新内容 |
|------|-----------|---------|
| 2025-12-08 | 1.0 | 初版作成 - Phase 1 翻訳に基づく基本用語集 |
| 2025-12-08 | 1.1 | Phase 2 完了 - 新規用語追加（Portfolio, Judging, Awards 等） |

---

## 参考

このドキュメントは **TRANSLATION_GUIDE.md** の具体的な実装例として作成されています。
翻訳作業を行う際は、必ずTRANSLATION_GUIDE.mdと併せて参照してください。
