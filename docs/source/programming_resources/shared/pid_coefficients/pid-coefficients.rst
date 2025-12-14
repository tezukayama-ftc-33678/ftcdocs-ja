PID 係数の変更
==========================

**REV Robotics Control Hub** および**REV Robotics Expansion Hub** を使用すると、ユーザーは閉ループモーター制御に使用される PID 係数を変更できます。PID 係数はチャネルとモードに固有です。

次の **op mode** は、拡張または強化された**DcMotor** クラス（「**DcMotorEx**」と呼ばれる）を使用して、「left_drive」という名前のモーターの RUN_USING_ENCODER モードの PID 係数を変更します。**op mode** は、**DcMotorEx** クラスの setPIDCoefficients メソッドを使用して値を変更します。このメソッドは、標準の**DcMotor** クラスでは使用できません。

PID 係数に加えた変更は、**REV Robotics Control Hub** または**REV Robotics Expansion Hub** の電源を入れ直すと保持されないことに注意してください。PID への変更を保持する必要がある場合は、**op mode** を変更して、**Control Hub** または**Android** スマートフォンに状態情報を保存することを検討する必要があります。Android Developer Web サイトには、アプリから**Android** デバイスにデータを保存する方法に関するチュートリアルがあります `こちら <https://developer.android.com/training/data-storage>`__

.. code-block:: java

   package org.firstinspires.ftc.teamcode;

   import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
   import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
   import com.qualcomm.robotcore.hardware.DcMotor;
   import com.qualcomm.robotcore.hardware.DcMotorEx;
   import com.qualcomm.robotcore.hardware.PIDCoefficients;

   /**
    * Created by tom on 9/26/17.
    * これは、DC モーターコントローラーとして REV Robotics Control Hub または
    * REV Robotics Expansion Hub を使用していることを前提としています。
    * この op mode は、DcMotorEx クラスの拡張/強化された PID 関連機能を使用します。
    */

   @Autonomous(name="Concept: Change PID", group = "Concept")
   public class ConceptChangePID extends LinearOpMode {

       // DC モーター
       DcMotorEx motorExLeft;

       public static final double NEW_P = 2.5;
       public static final double NEW_I = 0.1;
       public static final double NEW_D = 0.2;

       public void runOpMode() {
           // DC モーターへの参照を取得
           // Control Hub または Expansion Hub を使用しているため、
           // このモーターを DcMotorEx オブジェクトにキャストします
           motorExLeft = (DcMotorEx)hardwareMap.get(DcMotor.class, "left_drive");

           // 開始コマンドを待ちます
           waitForStart();

           // RUN_USING_ENCODER モードの PID 係数を取得
           PIDCoefficients pidOrig = motorExLeft.getPIDCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

           // DcMotorEx クラスに含まれるメソッドを使用して係数を変更
           PIDCoefficients pidNew = new PIDCoefficients(NEW_P, NEW_I, NEW_D);
           motorExLeft.setPIDCoefficients(DcMotor.RunMode.RUN_USING_ENCODER, pidNew);

           // 係数を再読み取りして変更を確認
           PIDCoefficients pidModified = motorExLeft.getPIDCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

           // ユーザーに情報を表示
           while(opModeIsActive()) {
               telemetry.addData("Runtime", "%.03f", getRuntime());
               telemetry.addData("P,I,D (orig)", "%.04f, %.04f, %.0f",
                       pidOrig.p, pidOrig.i, pidOrig.d);
               telemetry.addData("P,I,D (modified)", "%.04f, %.04f, %.04f",
                       pidModified.p, pidModified.i, pidModified.d);
               telemetry.update();
           }
       }
   }


PID 制御とは？
-----------------------

PID（比例-積分-微分）制御は、制御システムで使用されるフィードバックメカニズムです。モーター制御のコンテキストでは、PID コントローラーは、望ましい速度または位置（セットポイント）と実際の速度または位置の間の誤差を計算し、その誤差を最小化するようにモーター出力を調整します。

**PID 係数の説明：**

- **P（比例）**: 現在の誤差に比例する制御出力を生成します。P 値が大きいほど、セットポイントへの応答が速くなりますが、オーバーシュートや振動が発生する可能性があります。

- **I（積分）**: 時間の経過とともに蓄積された誤差に基づいて制御出力を生成します。これは、定常状態誤差を排除するのに役立ちますが、I 値が大きすぎると、システムの不安定性につながる可能性があります。

- **D（微分）**: 誤差の変化率に基づいて制御出力を生成します。これは、オーバーシュートを減らし、システムの安定性を向上させるのに役立ちますが、D 値が大きすぎると、ノイズ感度が増す可能性があります。


PID 係数の調整
------------------------

PID 係数の調整は、特定のモーターとアプリケーションに最適なパフォーマンスを達成するための反復プロセスです。開始点として：

1. すべての係数をゼロに設定することから始めます。
2. P 係数を増やして、システムが応答するまで確認します。
3. システムが振動または不安定になり始めるまで、P を増やし続けます。
4. P を最後の安定値の約半分に減らします。
5. I 係数を小さな値から増やして、定常状態誤差を排除します。
6. 必要に応じて D 係数を追加して、オーバーシュートを減らし、システムの応答を改善します。

**注意**: PID 調整は複雑なプロセスであり、各ロボットとアプリケーションに固有です。最適な結果を得るには、実験とテストが必要です。


デフォルトの PID 値
---------------------

**REV Robotics Control Hub** および**Expansion Hub** には、ほとんどのアプリケーションでうまく機能する各モーターチャネルのデフォルト PID 値があります。これらのデフォルト値は、**REV Robotics** によって広範なテストを通じて決定されています。

カスタム PID 係数が必要な場合のみ、デフォルト値を変更することをお勧めします。


追加リソース
---------------------

PID 制御の詳細については、次のリソースを参照してください：

- `Wikipedia: PID Controller <https://en.wikipedia.org/wiki/PID_controller>`__
- `Control Engineering: PID Control <https://www.ni.com/en-us/innovations/white-papers/06/pid-theory-explained.html>`__
- `FIRST Tech Challenge フォーラム <https://ftc-community.firstinspires.org/>`__
