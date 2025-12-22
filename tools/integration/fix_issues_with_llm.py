#!/usr/bin/env python3
"""
翻訳問題をローカルLLMで自動修正するワークフロー統合ツール

analyze_translation_issues.pyの出力を使用して、検出された問題を
ローカルLLM（Ollama）で自動的に修正します。

使い方:
    # ステップ1: ビルドと分析
    cd docs && make clean && make html-ja 2>&1 | tee build.log
    cd .. && python tools/analysis/analyze_translation_issues.py docs/build.log --json issues.json
    
    # ステップ2: LLMで自動修正（CRITICALのみ、少量で試す）
    python tools/integration/fix_issues_with_llm.py issues.json --limit 10 --dry-run
    python tools/integration/fix_issues_with_llm.py issues.json --limit 10
    
    # ステップ3: ビルドして確認
    cd docs && make clean && make html-ja
"""

import json
import sys
import argparse
import re
from pathlib import Path
from typing import Dict, List

# プロジェクトルート
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
LOCALES_DIR = PROJECT_ROOT / "locales" / "ja" / "LC_MESSAGES"

# 定数
DEFAULT_MODEL = 'qwen2.5:7b-instruct-q5_K_M'
LLM_TEMPERATURE = 0.1  # 低めに設定して一貫性を保つ
LINE_MATCH_TOLERANCE = 5  # エントリマッチングの行番号許容範囲

# 日本語文字の範囲
JAPANESE_RANGES = [
    (0x3040, 0x309F),  # ひらがな
    (0x30A0, 0x30FF),  # カタカナ
    (0x4E00, 0x9FFF),  # 漢字
]


def has_japanese(text: str) -> bool:
    """テキストに日本語が含まれているかチェック"""
    return any(
        any(start <= ord(c) <= end for start, end in JAPANESE_RANGES)
        for c in text
    )


class LLMFixIntegrator:
    """翻訳問題のLLM自動修正統合ツール"""
    
    def __init__(self, issues_json_path: Path, dry_run: bool = False):
        self.issues_json_path = issues_json_path
        self.dry_run = dry_run
        self.issues_data = None
        self.fixes_applied = 0
        self.fixes_failed = 0
        
    def load_issues(self):
        """issues.jsonを読み込み"""
        if not self.issues_json_path.exists():
            print(f"❌ ファイルが見つかりません: {self.issues_json_path}")
            sys.exit(1)
        
        with open(self.issues_json_path, 'r', encoding='utf-8') as f:
            self.issues_data = json.load(f)
        
        print(f"[INFO] 問題データを読み込みました")
        print(f"  総警告数: {self.issues_data.get('total_warnings', 0)}")
        print()
    
    def get_po_file_from_rst(self, rst_path: str) -> Path:
        """RSTファイルパスから対応するPOファイルを推定"""
        # RSTパスからrelativeパスを取得
        rst_path = rst_path.replace('<translated>:1', '').replace('<translated>', '')
        
        # source/以降のパスを抽出
        if '/source/' in rst_path:
            rel_path = rst_path.split('/source/')[1]
        elif 'source/' in rst_path:
            rel_path = rst_path.split('source/')[1]
        else:
            # ファイル名のみの場合
            rel_path = Path(rst_path).name
        
        # .rst -> .po
        if '.rst' in rel_path:
            po_rel_path = rel_path.replace('.rst', '.po').split(':')[0]
        else:
            po_rel_path = rel_path.split(':')[0] + '.po'
        
        po_path = LOCALES_DIR / po_rel_path
        
        return po_path
    
    def fix_critical_issues_with_llm(self, limit: int = None):
        """CRITICAL問題をLLMで修正"""
        print("=" * 70)
        print("🤖 ローカルLLMによる自動修正を開始")
        print("=" * 70)
        print()
        
        # 日本語ラベル/パス問題を抽出
        ja_label_issues = self.issues_data.get('japanese_label_issues', [])
        ja_doc_issues = self.issues_data.get('japanese_doc_issues', [])
        
        critical_issues = ja_label_issues + ja_doc_issues
        
        if limit:
            critical_issues = critical_issues[:limit]
        
        print(f"[INFO] 修正対象: {len(critical_issues)}件のCRITICAL問題")
        print()
        
        if self.dry_run:
            print("[DRY RUN] 実際の修正はスキップします")
            print()
            print("修正対象:")
            for i, issue in enumerate(critical_issues[:10], 1):
                file_path = issue['file']
                po_file = self.get_po_file_from_rst(file_path)
                print(f"  {i}. {po_file.name}:{issue['line']}")
                print(f"     タイプ: {issue.get('type', 'unknown')}")
                print(f"     {issue['message'][:60]}...")
            if len(critical_issues) > 10:
                print(f"  ... 他{len(critical_issues) - 10}件")
            print()
            print("実際に修正するには --dry-run を外して実行してください")
            return
        
        # LLMによる修正を実行
        self._apply_llm_fixes(critical_issues)
    
    def fix_high_issues_with_llm(self, limit: int = None):
        """HIGH問題をLLMで修正"""
        print("=" * 70)
        print("🤖 HIGH優先度問題の自動修正")
        print("=" * 70)
        print()
        
        high_issues = [w for w in self.issues_data.get('warnings', []) 
                      if w['severity'] == 'high']
        
        if limit:
            high_issues = high_issues[:limit]
        
        print(f"[INFO] 修正対象: {len(high_issues)}件のHIGH問題")
        print()
        
        if self.dry_run:
            print("[DRY RUN] 実際の修正はスキップします")
            return
        
        self._apply_llm_fixes(high_issues)
    
    def _apply_llm_fixes(self, issues: List[Dict]):
        """LLMを使用して実際に修正を適用"""
        try:
            import ollama
        except ImportError:
            print("❌ ollamaモジュールがインストールされていません")
            print("   pip install ollama")
            sys.exit(1)
        
        # モデルの確認
        try:
            models = ollama.list()
            model_names = [m['name'] for m in models.get('models', [])]
            print(f"[INFO] 利用可能なモデル: {', '.join(model_names[:3])}")
            
            # 推奨モデルがあるかチェック
            if not any(DEFAULT_MODEL in name for name in model_names):
                print(f"⚠️  推奨モデル {DEFAULT_MODEL} が見つかりません")
                print(f"   ollama pull {DEFAULT_MODEL}")
                
        except Exception as e:
            print(f"❌ Ollamaに接続できません: {e}")
            print("   ollama serveが起動していることを確認してください")
            sys.exit(1)
        
        try:
            import polib
        except ImportError:
            print("❌ polibがインストールされていません")
            print("   pip install polib")
            sys.exit(1)
        
        print()
        print("修正を開始します...")
        print()
        
        for i, issue in enumerate(issues, 1):
            rst_file = issue['file']
            po_file = self.get_po_file_from_rst(rst_file)
            
            print(f"[{i}/{len(issues)}] {po_file.name}:{issue['line']}")
            
            if not po_file.exists():
                print(f"  ⚠️  POファイルが見つかりません: {po_file}")
                self.fixes_failed += 1
                continue
            
            # 該当箇所を修正
            success = self._fix_single_issue_with_llm(po_file, issue)
            
            if success:
                print(f"  ✅ 修正完了")
                self.fixes_applied += 1
            else:
                print(f"  ❌ 修正失敗")
                self.fixes_failed += 1
            
            print()
    
    def _fix_single_issue_with_llm(self, po_file: Path, issue: Dict) -> bool:
        """単一の問題をLLMで修正"""
        import polib
        import ollama
        
        try:
            # POファイルを読み込み
            po = polib.pofile(str(po_file))
            
            # 該当行周辺のエントリを探す
            target_entry = None
            line_num = issue['line']
            
            for entry in po:
                # 行番号が近いエントリを探す
                if abs(entry.linenum - line_num) <= LINE_MATCH_TOLERANCE:
                    # メッセージに日本語が含まれているかチェック
                    if has_japanese(entry.msgstr) and self._entry_has_issue_pattern(entry, issue):
                        target_entry = entry
                        break
            
            if not target_entry:
                print(f"  ⚠️  該当エントリが見つかりません（行 {line_num}）")
                return False
            
            # LLMで修正案を生成
            fixed_msgstr = self._generate_fix_with_llm(
                target_entry.msgid,
                target_entry.msgstr,
                issue
            )
            
            if not fixed_msgstr or fixed_msgstr == target_entry.msgstr:
                print(f"  ⚠️  修正案が生成できませんでした")
                return False
            
            # 修正を適用
            print(f"  📝 修正前: {target_entry.msgstr[:50]}...")
            print(f"  📝 修正後: {fixed_msgstr[:50]}...")
            target_entry.msgstr = fixed_msgstr
            po.save()
            
            return True
            
        except Exception as e:
            print(f"  ❌ エラー: {e}")
            return False
    
    def _entry_has_issue_pattern(self, entry, issue: Dict) -> bool:
        """エントリが問題のパターンを含むかチェック"""
        msgstr = entry.msgstr
        issue_message = issue.get('message', '')
        
        # 日本語ラベル参照の問題
        if 'undefined label' in issue_message:
            # :ref:`...日本語...` のパターンを探す
            if re.search(r':ref:`[^`]*[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]', msgstr):
                return True
        
        # 日本語ドキュメントパスの問題
        if 'unknown document' in issue_message:
            # :doc:`...日本語...` のパターンを探す
            if re.search(r':doc:`[^`]*[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]', msgstr):
                return True
        
        # その他の日本語を含むエントリも候補として扱う
        return has_japanese(msgstr)
    
    def _generate_fix_with_llm(self, msgid: str, msgstr: str, issue: Dict) -> str:
        """LLMを使用して修正案を生成"""
        import ollama
        
        # 問題タイプに応じたプロンプトを生成
        issue_message = issue.get('message', '')
        
        if 'undefined label' in issue_message:
            prompt = self._create_label_fix_prompt(msgid, msgstr)
        elif 'unknown document' in issue_message:
            prompt = self._create_doc_path_fix_prompt(msgid, msgstr)
        else:
            prompt = self._create_generic_fix_prompt(msgid, msgstr, issue)
        
        try:
            response = ollama.chat(
                model=DEFAULT_MODEL,
                messages=[
                    {
                        'role': 'system',
                        'content': 'あなたはSphinxドキュメントのPO翻訳修正の専門家です。RST構文を正確に保持しながら日本語翻訳を修正します。'
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                options={
                    'temperature': LLM_TEMPERATURE,
                }
            )
            
            fixed_msgstr = response['message']['content'].strip()
            
            # 余分な引用符や説明を除去
            fixed_msgstr = self._clean_llm_output(fixed_msgstr)
            
            return fixed_msgstr
            
        except Exception as e:
            print(f"  ❌ LLM呼び出しエラー: {e}")
            return ""
    
    def _clean_llm_output(self, output: str) -> str:
        """LLMの出力から余分な部分を除去"""
        # 引用符を除去
        if output.startswith('"') and output.endswith('"'):
            output = output[1:-1]
        if output.startswith('msgstr "') and output.endswith('"'):
            output = output[8:-1]
        if output.startswith('msgstr: "') and output.endswith('"'):
            output = output[9:-1]
        
        # 説明文を除去（msgstrのみ抽出）
        lines = output.split('\n')
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith('#') and not line.startswith('修正'):
                output = '\n'.join(lines[i:])
                break
        
        return output.strip()
    
    def _create_label_fix_prompt(self, msgid: str, msgstr: str) -> str:
        """日本語ラベル参照問題の修正プロンプト"""
        return f"""以下のSphinx POファイルのエントリを修正してください。

【問題】
:ref:`...` 内のラベル名（<path:label>の部分）が日本語に翻訳されているため、参照が壊れています。

【修正ルール】
1. :ref:`表示テキスト <path:label>` の形式で、<path:label>部分は必ず英語のまま保持
2. 表示テキスト部分のみを日本語に翻訳
3. 他のRST構文（**, *, `など）も正確に保持

【元のmsgid】
{msgid}

【現在のmsgstr（問題あり）】
{msgstr}

【指示】
修正後のmsgstrのみを出力してください。説明や引用符は不要です。"""
    
    def _create_doc_path_fix_prompt(self, msgid: str, msgstr: str) -> str:
        """日本語ドキュメントパス問題の修正プロンプト"""
        return f"""以下のSphinx POファイルのエントリを修正してください。

【問題】
:doc:`...` 内のパスが日本語に翻訳されているため、リンクが壊れています。

【修正ルール】
1. :doc:`表示テキスト <path/to/doc>` の形式で、<path/to/doc>部分は必ず英語のまま保持
2. 表示テキスト部分のみを日本語に翻訳
3. 他のRST構文（**, *, `など）も正確に保持

【元のmsgid】
{msgid}

【現在のmsgstr（問題あり）】
{msgstr}

【指示】
修正後のmsgstrのみを出力してください。説明や引用符は不要です。"""
    
    def _create_generic_fix_prompt(self, msgid: str, msgstr: str, issue: Dict) -> str:
        """一般的な修正プロンプト"""
        return f"""以下のSphinx POファイルのエントリを修正してください。

【問題】
{issue.get('message', '翻訳に問題があります')[:100]}

【修正ルール】
1. RST構文（:ref:, :doc:, **, *, `など）を正確に保持
2. リンクやパスは英語のまま保持
3. 表示テキストのみを適切に日本語化

【元のmsgid】
{msgid}

【現在のmsgstr】
{msgstr}

【指示】
修正後のmsgstrのみを出力してください。説明や引用符は不要です。"""
    
    def print_summary(self):
        """修正結果のサマリーを表示"""
        print("=" * 70)
        print("📊 修正結果サマリー")
        print("=" * 70)
        print(f"修正成功: {self.fixes_applied}件")
        print(f"修正失敗: {self.fixes_failed}件")
        print()
        
        if self.fixes_applied > 0:
            print("✅ 次のステップ:")
            print("  1. ビルドして警告数を確認")
            print("     cd docs && make clean && make html-ja 2>&1 | grep 'build succeeded'")
            print()
            print("  2. HTMLで表示を確認")
            print("     cd docs/build/html-ja && python -m http.server 8000")
            print()
            print("  3. 警告が減っていれば、コミット")
            print("     git add locales/ja/LC_MESSAGES/*.po")
            print("     git commit -m 'Fix CRITICAL translation issues with LLM'")
        elif self.fixes_failed > 0:
            print("⚠️  修正に失敗しました。以下を確認してください:")
            print("  - Ollamaが起動しているか: ollama list")
            print("  - モデルがインストールされているか")
            print("    ollama pull qwen2.5:7b-instruct-q5_K_M")


def main():
    parser = argparse.ArgumentParser(
        description='翻訳問題をローカルLLMで自動修正',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # ドライラン（実際の修正はしない）
  python tools/integration/fix_issues_with_llm.py issues.json --limit 10 --dry-run
  
  # CRITICAL問題を10件修正
  python tools/integration/fix_issues_with_llm.py issues.json --limit 10
  
  # すべてのCRITICAL問題を修正
  python tools/integration/fix_issues_with_llm.py issues.json
  
  # HIGH優先度も含める
  python tools/integration/fix_issues_with_llm.py issues.json --severity critical high --limit 20
        """
    )
    parser.add_argument('issues_json', type=str,
                       help='analyze_translation_issues.pyが出力したJSONファイル')
    parser.add_argument('--severity', choices=['critical', 'high'],
                       nargs='+', default=['critical'],
                       help='修正する問題の重大度（デフォルト: critical）')
    parser.add_argument('--limit', type=int,
                       help='修正する問題の最大数（推奨: 10-20件ずつ）')
    parser.add_argument('--dry-run', action='store_true',
                       help='実際の修正を行わず、対象のみ表示')
    
    args = parser.parse_args()
    
    if not args.dry_run and not args.limit:
        print("⚠️  警告: --limitを指定せずに実行すると、すべての問題を一度に修正します。")
        print("   初回は --limit 10 --dry-run で確認することを推奨します。")
        response = input("続行しますか？ (y/N): ")
        if response.lower() != 'y':
            print("中止しました。")
            return
    
    integrator = LLMFixIntegrator(Path(args.issues_json), dry_run=args.dry_run)
    integrator.load_issues()
    
    # 重大度に応じて修正
    if 'critical' in args.severity:
        integrator.fix_critical_issues_with_llm(limit=args.limit)
    
    if 'high' in args.severity:
        integrator.fix_high_issues_with_llm(limit=args.limit)
    
    integrator.print_summary()


if __name__ == '__main__':
    main()
