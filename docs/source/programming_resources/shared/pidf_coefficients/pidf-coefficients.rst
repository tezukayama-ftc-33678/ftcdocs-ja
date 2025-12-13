PIDF 係数の変更
===========================

**REV Robotics Control Hub** または **REV Robotics Expansion Hub** を使用すると、ユーザーは閉ループモーター制御に使用される PIDF 係数を変更できます。PIDF 係数は、各チャネル（モーターポート）と各 RunMode に固有です。

次のサンプル **OpMode** は、拡張または強化された **DcMotor** クラス（「**DcMotorEx**」と呼ばれる）を使用して、「left_drive」という名前のモーターの RUN_USING_ENCODER RunMode の PIDF 係数を変更します。**OpMode** は、**DcMotorEx** クラスの setPIDFCoefficients メソッドを使用して値を変更します。このメソッドは、標準の **DcMotor** クラスでは使用できません。

PIDF 係数に加えた変更は、**REV Robotics Control Hub** または **REV Robotics Expansion Hub** の電源を入れ直すと保持されないことに注意してください。変更を保持する必要がある場合は、**OpMode** を変更して、**Control Hub** または **Android** スマートフォンに状態情報を保存することを検討してください。Android Developer Web サイトには、アプリから **Android** デバイスにデータを保存する方法に関するチュートリアルがあります `こちら <https://developer.android.com/training/data-storage>`__

.. code-block:: java

   package org.firstinspires.ftc.teamcode;

   import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
   import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
   import com.qualcomm.robotcore.hardware.DcMotor;
   import com.qualcomm.robotcore.hardware.DcMotorEx;
   import com.qualcomm.robotcore.hardware.PIDFCoefficients;

   /**
    * Created by Tom on 9/26/17. Updated 9/24/2021 for PIDF.
    * これは、DC モーターコントローラーとして REV Robotics Control Hub または
    * REV Robotics Expansion Hub を使用していることを前提としています。
    * この OpMode は、DcMotorEx クラスの拡張/強化された PIDF 関連機能を使用します。
    */

   @Autonomous(name="Concept: Change PIDF", group = "Concept")
   public class ConceptChangePIDF extends LinearOpMode {

       // DC モーター
       DcMotorEx motorExLeft;

       public static final double NEW_P = 2.5;
       public static final double NEW_I = 0.1;
       public static final double NEW_D = 0.2;
       public static final double NEW_F = 0.5;
       // これらの値は説明のみを目的としています。
       // 各モーターの計画された使用法に基づいて設定および調整する必要があります。

       public void runOpMode() {
           // DC モーターへの参照を取得
           // Control Hub または Expansion Hub を使用しているため、
           // このモーターを DcMotorEx オブジェクトにキャストします
           motorExLeft = (DcMotorEx)hardwareMap.get(DcMotor.class, "left_drive");

           // 開始コマンドを待ちます
           waitForStart();

           // RUN_USING_ENCODER RunMode の PIDF 係数を取得
           PIDFCoefficients pidfOrig = motorExLeft.getPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

           // DcMotorEx クラスに含まれるメソッドを使用して係数を変更
           PIDFCoefficients pidfNew = new PIDFCoefficients(NEW_P, NEW_I, NEW_D, NEW_F);
           motorExLeft.setPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER, pidfNew);

           // 係数を再読み取りして変更を確認
           PIDFCoefficients pidfModified = motorExLeft.getPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

           // ユーザーに情報を表示
           while(opModeIsActive()) {
               telemetry.addData("Runtime (sec)", "%.01f", getRuntime());
               telemetry.addData("P,I,D,F (orig)", "%.04f, %.04f, %.04f, %.04f",
                       pidfOrig.p, pidfOrig.i, pidfOrig.d, pidfOrig.f);
               telemetry.addData("P,I,D,F (modified)", "%.04f, %.04f, %.04f, %.04f",
                       pidfModified.p, pidfModified.i, pidfModified.d, pidfModified.f);
               telemetry.update();
           }
       }
   }


PIDF 制御とは？
------------------------

PIDF（比例-積分-微分-フィードフォワード）制御は、PID 制御の拡張版で、フィードフォワード（F）項が追加されています。フィードフォワード項は、システムのダイナミクスの既知の情報に基づいて制御出力を予測的に調整し、応答性と精度を向上させます。

**PIDF 係数の説明：**

- **P（比例）**: 現在の誤差に比例する制御出力を生成します。

- **I（積分）**: 時間の経過とともに蓄積された誤差に基づいて制御出力を生成します。

- **D（微分）**: 誤差の変化率に基づいて制御出力を生成します。

- **F（フィードフォワード）**: システムの既知の特性（重力、摩擦など）を補償するための追加の制御出力を提供します。フィードフォワード項は、望ましい速度または位置を達成するために必要な出力を予測するのに役立ちます。


PIDF 係数の調整
-------------------------

PIDF 係数の調整は、PID 調整と似ていますが、フィードフォワード項が追加されています：

1. PID 係数を調整します（前述の PID セクションを参照）。
2. F 係数を追加して、定常状態のパフォーマンスを向上させます。
3. F 値は通常、望ましい速度を達成するために必要なモーター電力に基づいて計算されます。
4. 実験を通じて F 値を微調整して、最適なパフォーマンスを達成します。

** 注意**: PIDF 調整は高度なトピックであり、モーター制御システムの深い理解が必要です。


PID と PIDF の使い分け
----------------------------

- **PID** は、ほとんどの基本的なモーター制御アプリケーションに適しています。
- **PIDF** は、より高い精度と応答性が必要な高度なアプリケーションに推奨されます。
- フィードフォワード項（F）は、既知のシステムダイナミクス（重力、摩擦など）を補償する場合に特に役立ちます。


デフォルトの PIDF 値
----------------------

**REV Robotics Control Hub** および **Expansion Hub** には、各モーターチャネルのデフォルト PIDF 値があります。これらのデフォルト値は、ほとんどのアプリケーションでうまく機能しますが、特定の要件に基づいて調整できます。


追加リソース
---------------------

PIDF 制御の詳細については、次のリソースを参照してください：

- `Wikipedia: PID Controller <https://en.wikipedia.org/wiki/PID_controller>`__
- `Feed-Forward Control <https://www.ni.com/en-us/innovations/white-papers/06/pid-theory-explained.html>`__
- `FIRST Tech Challenge フォーラム <https://ftc-community.firstinspires.org/>`__
- `REV Robotics ドキュメント <https://docs.revrobotics.com/>`__
