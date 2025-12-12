**Kotlin** プログラミング言語の使用
=====================================


**Kotlin** とは？
---------------


**Kotlin** プログラミング言語は、Java Virtual Machine（JVM）でコンパイルおよび実行される Java プログラミング言語の現代的な代替であり、Android アプリケーションの開発に使用できます。これは、IntelliJ IDE（**Android Studio** の基礎）を開発した同じ会社である JetBrains によって開発されました。

* https://kotlinlang.org/

Java に基づいているため、**Kotlin** は多くの同じ機能と構文を共有しています。ただし、コードを書きやすく、エラーが発生しにくくする多くの新しい機能と構文も追加しています。**Kotlin** の機能には次のものがあります：

* Java との完全な相互運用性。**Kotlin** から Java クラスとライブラリを使用でき、その逆も可能です。
* 型推論。**Kotlin** では、必要に応じて型推論を使用できます。つまり、コンテキストから推論できる場合、変数の型を指定する必要はありません（``var myString = "Hi!"``）。
* セミコロンなし。**Kotlin** では、ステートメントを終了するためにセミコロンは必要ありません。
* データクラス。**Kotlin** には、データを保存するために使用されるクラスを作成するための簡潔な構文があります。
* 拡張関数。**Kotlin** では、元のクラスを変更することなく、既存のクラスに関数を追加できます。
* Null 安全性。**Kotlin** には、null ポインター例外を排除するのに役立つ型システムがあります。
* 演算子のオーバーロード。**Kotlin** では、``+`` や ``*`` などの演算子が独自のクラスでどのように機能するかを定義できます。
* その他多数！

さらに、**Kotlin** でゼロからコーディングする方法を学びたくない場合、**Android Studio** IDE には、コードのセクションまたは Java ファイル全体を **Kotlin** ファイルに変換するツールがあります。これは、特定の Java コードが **Kotlin** でどのように記述されているかを学ぶのに非常に役立ちます。

**Kotlin** は完全に相互運用可能であるため、既存のすべての Java コードを変換することなく、**Kotlin** プロジェクトで使用することもできます。


**FIRST** **Tech Challenge** での **Kotlin** の使用
--------------------------------------


このドキュメントの執筆時点では、**FIRST** **Tech Challenge** でプログラミングオプションとして **Kotlin** を禁止する規則はありませんが、公式にサポートまたは推奨されている言語ではありません。**Kotlin** を使用するチームは、自己責任で使用し、ソフトウェアの問題が発生した場合、イベントでテクニカルヘルプ/サポートが利用できないことを予期する必要があります。


プロジェクトへの **Kotlin** のインストール
---------------------------------


Android プロジェクトで **Kotlin** を使用するには、プロジェクトに **Kotlin** プラグインを追加する必要があります。これは、``buildscript`` セクションのルート ``build.gradle`` ファイルに次の行を追加することによって行われます：

.. code-block:: groovy

    buildscript {
        repositories {
            google()
            mavenCentral()
        }
        dependencies {
            classpath 'com.android.tools.build:gradle:7.4.2'
            classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.0"
        }
    }

次に、``TeamCode`` モジュールの ``build.gradle`` ファイルに次の行を追加します：

.. code-block:: groovy

    apply plugin: 'kotlin-android'

    dependencies {
        implementation "org.jetbrains.kotlin:kotlin-stdlib:1.8.0"
        // 他の依存関係...
    }

これで、プロジェクトで **Kotlin** を使用する準備が整いました！


**Kotlin** **OpMode** の作成
----------------------------


**Kotlin** で **OpMode** を作成するには、``TeamCode`` フォルダーに新しい **Kotlin** ファイルを作成し、Java **OpMode** と同じ方法で作成します。主な違いは、**Kotlin** 構文を使用することです。

Java の例：

.. code-block:: java

    @TeleOp(name="Basic OpMode", group="Linear Opmode")
    public class BasicOpMode extends LinearOpMode {
        @Override
        public void runOpMode() {
            telemetry.addData("Status", "Initialized");
            telemetry.update();
            
            waitForStart();
            
            while (opModeIsActive()) {
                telemetry.addData("Status", "Running");
                telemetry.update();
            }
        }
    }

**Kotlin** の同等のもの：

.. code-block:: kotlin

    @TeleOp(name = "Basic OpMode", group = "Linear Opmode")
    class BasicOpMode : LinearOpMode() {
        override fun runOpMode() {
            telemetry.addData("Status", "Initialized")
            telemetry.update()
            
            waitForStart()
            
            while (opModeIsActive()) {
                telemetry.addData("Status", "Running")
                telemetry.update()
            }
        }
    }

**Kotlin** について詳しく知りたい場合は、公式の **Kotlin** ドキュメント https://kotlinlang.org/docs/home.html を参照してください。
