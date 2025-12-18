#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
POファイル一括翻訳バッチ処理スクリプト
全てのPOファイルを自動翻訳 → 品質チェック → 自動修正 → ビルド検証
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

try:
    from colorama import init, Fore, Style
    from tqdm import tqdm
    init(autoreset=True)
except ImportError:
    print("colorama と tqdm をインストールしてください:")
    print("pip install colorama tqdm")
    sys.exit(1)

# 翻訳スクリプトをインポート
try:
    from translate_po import POTranslator
except ImportError:
    print("translate_po.py が見つかりません")
    sys.exit(1)


class BatchTranslator:
    """バッチ翻訳管理クラス"""
    
    def __init__(self, config_path: str = "translate_config.json"):
        self.config_path = config_path
        self.load_config()
        
        # 進捗管理
        self.progress_file = "translation_progress.json"
        self.load_progress()
        
        # 統計
        self.stats = {
            "files_total": 0,
            "files_completed": 0,
            "files_failed": 0,
            "files_skipped": 0,
            "start_time": None,
            "end_time": None
        }
        
    def load_config(self):
        """設定読み込み"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "checkpoint_interval": 50,
                "quality_check_enabled": True,
                "auto_fix_common_errors": True,
                "skip_translated": True
            }
    
    def load_progress(self):
        """進捗状態の読み込み"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                self.progress = json.load(f)
        else:
            self.progress = {
                "completed_files": [],
                "failed_files": [],
                "current_file": None,
                "last_update": None
            }
    
    def save_progress(self):
        """進捗状態の保存"""
        self.progress["last_update"] = datetime.now().isoformat()
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, indent=2, ensure_ascii=False)
    
    def find_po_files(self, po_dir: str) -> List[Path]:
        """POファイルの検索"""
        po_dir_path = Path(po_dir)
        if not po_dir_path.exists():
            print(f"{Fore.RED}✗ ディレクトリが見つかりません: {po_dir}")
            return []
        
        po_files = list(po_dir_path.rglob("*.po"))
        
        # 優先順位付きソート（重要なファイルを先に）
        priority_files = [
            "index.po",
            "persona_pages",
            "gracious_professionalism",
            "hardware_and_software_configuration"
        ]
        
        def sort_key(path: Path) -> int:
            for i, priority in enumerate(priority_files):
                if priority in str(path):
                    return i
            return len(priority_files)
        
        po_files.sort(key=sort_key)
        
        return po_files
    
    def should_skip_file(self, po_file: Path) -> bool:
        """ファイルをスキップすべきか判定"""
        po_file_str = str(po_file)
        
        # 既に完了済み
        if po_file_str in self.progress["completed_files"]:
            return True
        
        return False
    
    def translate_file(self, po_file: Path) -> bool:
        """ファイルを翻訳"""
        try:
            self.progress["current_file"] = str(po_file)
            self.save_progress()
            
            print(f"\n{Fore.CYAN}{'='*70}")
            print(f"{Fore.CYAN}翻訳: {po_file.name}")
            print(f"{Fore.CYAN}{'='*70}")
            
            # 翻訳実行
            translator = POTranslator(self.config_path)
            success = translator.translate_po_file(str(po_file))
            
            if success:
                self.progress["completed_files"].append(str(po_file))
                self.stats["files_completed"] += 1
                print(f"{Fore.GREEN}✓ 完了: {po_file.name}")
            else:
                self.progress["failed_files"].append(str(po_file))
                self.stats["files_failed"] += 1
                print(f"{Fore.RED}✗ 失敗: {po_file.name}")
            
            self.save_progress()
            return success
            
        except Exception as e:
            print(f"{Fore.RED}✗ エラー: {e}")
            self.progress["failed_files"].append(str(po_file))
            self.stats["files_failed"] += 1
            self.save_progress()
            return False
    
    def run_quality_check(self, po_dir: str) -> Dict:
        """品質チェックの実行"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}品質チェック実行中...")
        print(f"{Fore.CYAN}{'='*70}")
        
        check_script = Path("docs/scripts/check_and_fix_po.py")
        if not check_script.exists():
            print(f"{Fore.YELLOW}⚠ 品質チェックスクリプトが見つかりません")
            return {}
        
        try:
            cmd = [
                sys.executable,
                str(check_script),
                "--po-dir", po_dir,
                "--output", "po_issues.json",
                "--verbose"
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            if result.returncode == 0:
                print(f"{Fore.GREEN}✓ 品質チェック完了")
            else:
                print(f"{Fore.YELLOW}⚠ 品質チェックで問題検出")
            
            # 結果の読み込み
            if os.path.exists("po_issues.json"):
                with open("po_issues.json", 'r', encoding='utf-8') as f:
                    issues = json.load(f)
                return issues
            
        except Exception as e:
            print(f"{Fore.RED}✗ 品質チェックエラー: {e}")
        
        return {}
    
    def print_quality_summary(self, issues):
        """品質チェック結果のサマリー表示 (list/dict両対応)"""
        if not issues:
            print(f"{Fore.GREEN}✓ 問題は検出されませんでした")
            return
        
        print(f"\n{Fore.CYAN}品質チェック結果サマリー:")
        print(f"{Fore.CYAN}{'-'*50}")
        
        # check_and_fix_po.py は list で返す
        if isinstance(issues, list):
            by_type = {}
            for issue in issues:
                if isinstance(issue, dict):
                    issue_type = issue.get("type") or issue.get("issue_type")
                else:
                    issue_type = getattr(issue, "type", None) or getattr(issue, "issue_type", None)
                if not issue_type:
                    continue
                by_type.setdefault(issue_type, 0)
                by_type[issue_type] += 1
            total_issues = sum(by_type.values())
            issue_names = {
                "missing_doc_ref": "doc参照の欠落",
                "emphasis_mismatch": "強調マーカー不一致",
                "external_link_mismatch": "外部リンク不一致",
                "whitespace_issues": "空白の問題",
            }
            for issue_type, count in sorted(by_type.items(), key=lambda kv: kv[0]):
                name = issue_names.get(issue_type, issue_type)
                print(f"{Fore.YELLOW}  {name}: {count} 件")
            print(f"{Fore.CYAN}{'-'*50}")
            print(f"{Fore.YELLOW}合計: {total_issues} 件の問題")
            return
        
        # 旧形式(dict)にも対応
        total_issues = 0
        for issue_type, file_issues in issues.items():
            count = sum(len(entries) for entries in file_issues.values())
            total_issues += count
            
            if count > 0:
                issue_names = {
                    "missing_doc_ref": "doc参照の欠落",
                    "emphasis_mismatch": "強調マーカー不一致",
                    "external_link_mismatch": "外部リンク不一致",
                    "whitespace_issues": "空白の問題"
                }
                name = issue_names.get(issue_type, issue_type)
                print(f"{Fore.YELLOW}  {name}: {count} 件")
        
        print(f"{Fore.CYAN}{'-'*50}")
        print(f"{Fore.YELLOW}合計: {total_issues} 件の問題")

    def compare_build_structures(self):
        """html / html-ja の出力構造差分を簡易チェック"""
        html_dir = Path("docs/build/html")
        html_ja_dir = Path("docs/build/html-ja")
        if not html_dir.exists() or not html_ja_dir.exists():
            print(f"{Fore.YELLOW}⚠ buildディレクトリが不足しているため構造比較をスキップしました")
            return
        
        def list_files(base: Path):
            return {p.relative_to(base) for p in base.rglob("*") if p.is_file()}
        
        en_files = list_files(html_dir)
        ja_files = list_files(html_ja_dir)
        extra_ja = sorted(ja_files - en_files)
        missing_ja = sorted(en_files - ja_files)
        
        report_lines = ["[Extra in html-ja]"] + [str(p) for p in extra_ja]
        report_lines += ["", "[Missing in html-ja]"] + [str(p) for p in missing_ja]
        report_path = Path("build_structure_diff.txt")
        report_path.write_text("\n".join(report_lines), encoding="utf-8")
        
        print(f"{Fore.CYAN}構造比較結果: html-jaにのみ存在 {len(extra_ja)} 件 / htmlのみ {len(missing_ja)} 件")
        print(f"{Fore.CYAN}詳細: {report_path}")
    
    def build_html(self) -> bool:
        """HTMLビルドの実行"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.CYAN}HTMLビルド実行中...")
        print(f"{Fore.CYAN}{'='*70}")
        
        docs_dir = Path("docs")
        if not docs_dir.exists():
            print(f"{Fore.RED}✗ docs ディレクトリが見つかりません")
            return False
        
        try:
            # clean
            subprocess.run(
                ["make", "clean"],
                cwd=str(docs_dir),
                check=True,
                capture_output=True
            )
            
            # html (英語)
            result_html = subprocess.run(
                ["make", "html"],
                cwd=str(docs_dir),
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            # html-ja (日本語)
            result_html_ja = subprocess.run(
                ["make", "html-ja"],
                cwd=str(docs_dir),
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            def count_issues(result: subprocess.CompletedProcess) -> tuple:
                combined = (result.stdout or "") + (result.stderr or "")
                return combined.count("WARNING"), combined.count("ERROR")
            
            warnings_en, errors_en = count_issues(result_html)
            warnings_ja, errors_ja = count_issues(result_html_ja)
            warnings = warnings_en + warnings_ja
            errors = errors_en + errors_ja
            
            print(f"\n{Fore.CYAN}ビルド結果:")
            print(f"  英語:  警告 {warnings_en} / エラー {errors_en}")
            print(f"  日本語:警告 {warnings_ja} / エラー {errors_ja}")
            print(f"  合計: 警告 {warnings} / エラー {errors}")
            
            if errors > 0:
                print(f"{Fore.RED}✗ ビルドエラーあり")
                return False
            elif warnings > 50:
                print(f"{Fore.YELLOW}⚠ 警告が多数あります")
            else:
                print(f"{Fore.GREEN}✓ ビルド成功")
            
            # 出力構造の簡易比較
            self.compare_build_structures()
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}✗ ビルドエラー: {e}")
            return False
    
    def run(self, po_dir: str, skip_build: bool = False):
        """バッチ処理の実行"""
        self.stats["start_time"] = datetime.now()
        
        print(f"{Fore.GREEN}{'='*70}")
        print(f"{Fore.GREEN}PO翻訳バッチ処理開始")
        print(f"{Fore.GREEN}{'='*70}")
        print(f"開始時刻: {self.stats['start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        
        # POファイルの検索
        po_files = self.find_po_files(po_dir)
        self.stats["files_total"] = len(po_files)
        
        if not po_files:
            print(f"{Fore.RED}✗ POファイルが見つかりません")
            return
        
        print(f"\n検出されたPOファイル: {len(po_files)} 個")
        
        # 翻訳処理
        for po_file in tqdm(po_files, desc="全体進捗", unit="file"):
            if self.should_skip_file(po_file):
                print(f"{Fore.BLUE}⊘ スキップ: {po_file.name} (完了済み)")
                self.stats["files_skipped"] += 1
                continue
            
            self.translate_file(po_file)
            
            # 定期的にチェックポイント保存
            if self.stats["files_completed"] % 10 == 0:
                print(f"{Fore.BLUE}💾 チェックポイント保存")
                self.save_progress()
        
        # 品質チェック
        if self.config.get("quality_check_enabled", True):
            issues = self.run_quality_check(po_dir)
            self.print_quality_summary(issues)
        
        # HTMLビルド
        if not skip_build:
            self.build_html()
        
        # 統計表示
        self.stats["end_time"] = datetime.now()
        self.print_final_stats()
    
    def print_final_stats(self):
        """最終統計の表示"""
        duration = self.stats["end_time"] - self.stats["start_time"]
        
        print(f"\n{Fore.GREEN}{'='*70}")
        print(f"{Fore.GREEN}バッチ処理完了")
        print(f"{Fore.GREEN}{'='*70}")
        print(f"処理時間: {duration}")
        print(f"\n統計:")
        print(f"  総ファイル数:     {self.stats['files_total']}")
        print(f"{Fore.GREEN}  完了:             {self.stats['files_completed']}")
        print(f"{Fore.BLUE}  スキップ:         {self.stats['files_skipped']}")
        print(f"{Fore.RED}  失敗:             {self.stats['files_failed']}")
        
        if self.stats["files_total"] > 0:
            success_rate = (self.stats["files_completed"] / 
                          (self.stats["files_total"] - self.stats["files_skipped"]) * 100
                          if self.stats["files_total"] > self.stats["files_skipped"] else 0)
            print(f"\n成功率: {success_rate:.1f}%")


def main():
    """メイン関数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="POファイル一括翻訳バッチ処理"
    )
    parser.add_argument(
        "--po-dir",
        default="locales/ja/LC_MESSAGES",
        help="POファイルディレクトリ（デフォルト: locales/ja/LC_MESSAGES）"
    )
    parser.add_argument(
        "--config",
        default="translate_config.json",
        help="設定ファイル（デフォルト: translate_config.json）"
    )
    parser.add_argument(
        "--skip-build",
        action="store_true",
        help="最終ビルドをスキップ"
    )
    parser.add_argument(
        "--reset-progress",
        action="store_true",
        help="進捗状態をリセット"
    )
    
    args = parser.parse_args()
    
    # 進捗リセット
    if args.reset_progress and os.path.exists("translation_progress.json"):
        os.remove("translation_progress.json")
        print(f"{Fore.GREEN}✓ 進捗状態をリセットしました")
    
    # バッチ処理実行
    batch = BatchTranslator(args.config)
    batch.run(args.po_dir, args.skip_build)


if __name__ == "__main__":
    main()
