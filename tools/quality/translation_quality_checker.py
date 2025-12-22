#!/usr/bin/env python3
"""
Translation Quality Checker
翻訳品質チェッカー

日本語翻訳の品質を自動的にチェックし、問題を検出するツール

機能:
1. 空のmsgstrエントリーの検出
2. RST構文エラーの検出（インラインマークアップのスペーシング問題等）
3. ローカルLLM (Ollama) を使用した修正案の提案
4. インタラクティブなHTMLレポートの生成

使用方法:
    python translation_quality_checker.py --check    # 検査のみ
    python translation_quality_checker.py --fix      # 検査+自動修正
    python translation_quality_checker.py --report   # 詳細レポート生成
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

try:
    import polib
except ImportError:
    print("Error: polib is required. Install it with: pip install polib")
    sys.exit(1)

# Optional: Ollama for LLM-based fixes
try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False

# プロジェクトパス
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
LOCALES_DIR = PROJECT_ROOT / "locales" / "ja" / "LC_MESSAGES"
OUTPUT_DIR = PROJECT_ROOT / "data" / "quality_reports"

# デフォルト設定
DEFAULT_LLM_MODEL = 'qwen2.5:7b-instruct-q5_K_M'

# Pre-compiled regex patterns for performance
REGEX_BOLD_SPACING = re.compile(r'\*\*\s+\w|\w\s+\*\*')
REGEX_ITALIC_SPACING = re.compile(r'(?<!\*)\*\s+\w|\w\s+\*(?!\*)')
REGEX_CODE_SPACING = re.compile(r'``\s+\w|\w\s+``')


@dataclass
class TranslationIssue:
    """翻訳の問題を表すデータクラス"""
    po_file: str
    entry_id: str
    msgid: str
    msgstr: str
    issue_type: str  # 'empty', 'rst_syntax', 'inline_markup', 'partial'
    severity: str    # 'error', 'warning', 'info'
    description: str
    line_number: int
    suggested_fix: Optional[str] = None
    auto_fixable: bool = False


class TranslationQualityChecker:
    """翻訳品質チェッカー"""
    
    def __init__(self, use_llm: bool = False, verbose: bool = False, llm_model: str = DEFAULT_LLM_MODEL):
        self.use_llm = use_llm and OLLAMA_AVAILABLE
        self.verbose = verbose
        self.llm_model = llm_model
        self.issues: List[TranslationIssue] = []
        self.stats = {
            'total_files': 0,
            'total_entries': 0,
            'empty_entries': 0,
            'syntax_errors': 0,
            'warnings': 0,
            'auto_fixable': 0,
        }
        
        if self.use_llm and not OLLAMA_AVAILABLE:
            self.log("Warning: Ollama not available. LLM features disabled.")
            self.use_llm = False
    
    def log(self, message: str):
        """ログ出力"""
        if self.verbose:
            print(message)
    
    def check_po_file(self, po_path: Path) -> List[TranslationIssue]:
        """POファイルをチェック"""
        self.log(f"Checking: {po_path.relative_to(PROJECT_ROOT)}")
        
        try:
            po = polib.pofile(str(po_path))
        except Exception as e:
            self.log(f"Error loading PO file: {e}")
            return []
        
        file_issues = []
        self.stats['total_files'] += 1
        
        for entry in po:
            if entry.obsolete:
                continue
            
            self.stats['total_entries'] += 1
            
            # 1. 空のmsgstrチェック
            if not entry.msgstr or entry.msgstr.strip() == '':
                if entry.msgid and entry.msgid.strip():
                    issue = TranslationIssue(
                        po_file=str(po_path.relative_to(PROJECT_ROOT)),
                        entry_id=f"{entry.msgid[:50]}...",
                        msgid=entry.msgid,
                        msgstr=entry.msgstr,
                        issue_type='empty',
                        severity='warning',
                        description='msgstrが空です（未翻訳）',
                        line_number=entry.linenum,
                        auto_fixable=False
                    )
                    file_issues.append(issue)
                    self.stats['empty_entries'] += 1
                continue
            
            # 2. RST構文エラーチェック
            syntax_issues = self.check_rst_syntax(entry, po_path)
            file_issues.extend(syntax_issues)
            
            # 3. インラインマークアップのスペーシングチェック
            markup_issues = self.check_inline_markup(entry, po_path)
            file_issues.extend(markup_issues)
        
        return file_issues
    
    def check_rst_syntax(self, entry: polib.POEntry, po_path: Path) -> List[TranslationIssue]:
        """RST構文エラーをチェック"""
        issues = []
        msgstr = entry.msgstr
        
        # アスタリスクのスペーシング問題
        # 誤: ** 太字 **  正: **太字**
        if REGEX_BOLD_SPACING.search(msgstr):
            issue = TranslationIssue(
                po_file=str(po_path.relative_to(PROJECT_ROOT)),
                entry_id=f"{entry.msgid[:50]}...",
                msgid=entry.msgid,
                msgstr=msgstr,
                issue_type='rst_syntax',
                severity='error',
                description='太字マークアップ（**）の前後に不要なスペースがあります',
                line_number=entry.linenum,
                suggested_fix=self._fix_bold_spacing(msgstr),
                auto_fixable=True
            )
            issues.append(issue)
            self.stats['syntax_errors'] += 1
            self.stats['auto_fixable'] += 1
        
        # イタリック体のスペーシング問題
        # 誤: * イタリック *  正: *イタリック*
        if REGEX_ITALIC_SPACING.search(msgstr):
            issue = TranslationIssue(
                po_file=str(po_path.relative_to(PROJECT_ROOT)),
                entry_id=f"{entry.msgid[:50]}...",
                msgid=entry.msgid,
                msgstr=msgstr,
                issue_type='rst_syntax',
                severity='error',
                description='イタリック体マークアップ（*）の前後に不要なスペースがあります',
                line_number=entry.linenum,
                suggested_fix=self._fix_italic_spacing(msgstr),
                auto_fixable=True
            )
            issues.append(issue)
            self.stats['syntax_errors'] += 1
            self.stats['auto_fixable'] += 1
        
        # バッククオートのスペーシング問題
        # 誤: `` コード ``  正: ``コード``
        if REGEX_CODE_SPACING.search(msgstr):
            issue = TranslationIssue(
                po_file=str(po_path.relative_to(PROJECT_ROOT)),
                entry_id=f"{entry.msgid[:50]}...",
                msgid=entry.msgid,
                msgstr=msgstr,
                issue_type='rst_syntax',
                severity='error',
                description='コードマークアップ（``）の前後に不要なスペースがあります',
                line_number=entry.linenum,
                suggested_fix=self._fix_code_spacing(msgstr),
                auto_fixable=True
            )
            issues.append(issue)
            self.stats['syntax_errors'] += 1
            self.stats['auto_fixable'] += 1
        
        # バッククオートの不一致
        backtick_count = msgstr.count('`')
        if backtick_count % 2 != 0:
            issue = TranslationIssue(
                po_file=str(po_path.relative_to(PROJECT_ROOT)),
                entry_id=f"{entry.msgid[:50]}...",
                msgid=entry.msgid,
                msgstr=msgstr,
                issue_type='rst_syntax',
                severity='error',
                description='バッククオート（`）の数が一致しません',
                line_number=entry.linenum,
                auto_fixable=False
            )
            issues.append(issue)
            self.stats['syntax_errors'] += 1
        
        # アスタリスクの不一致（太字・イタリック）
        # 単一の*と**を別々にカウント
        double_asterisk = msgstr.count('**')
        single_asterisk = msgstr.count('*') - (double_asterisk * 2)
        
        if double_asterisk % 2 != 0:
            issue = TranslationIssue(
                po_file=str(po_path.relative_to(PROJECT_ROOT)),
                entry_id=f"{entry.msgid[:50]}...",
                msgid=entry.msgid,
                msgstr=msgstr,
                issue_type='rst_syntax',
                severity='error',
                description='太字マークアップ（**）の数が一致しません',
                line_number=entry.linenum,
                auto_fixable=False
            )
            issues.append(issue)
            self.stats['syntax_errors'] += 1
        
        return issues
    
    def check_inline_markup(self, entry: polib.POEntry, po_path: Path) -> List[TranslationIssue]:
        """インラインマークアップのチェック"""
        issues = []
        msgid = entry.msgid
        msgstr = entry.msgstr
        
        # 英語版にあって日本語版にないマークアップ
        en_bold_count = msgid.count('**') // 2
        ja_bold_count = msgstr.count('**') // 2
        
        if en_bold_count > 0 and ja_bold_count == 0:
            issue = TranslationIssue(
                po_file=str(po_path.relative_to(PROJECT_ROOT)),
                entry_id=f"{entry.msgid[:50]}...",
                msgid=entry.msgid,
                msgstr=msgstr,
                issue_type='inline_markup',
                severity='warning',
                description='英語版にある太字マークアップが日本語版にありません',
                line_number=entry.linenum,
                auto_fixable=False
            )
            issues.append(issue)
            self.stats['warnings'] += 1
        
        # コードマークアップのチェック
        en_code_count = msgid.count('``') // 2
        ja_code_count = msgstr.count('``') // 2
        
        if en_code_count > 0 and ja_code_count == 0:
            issue = TranslationIssue(
                po_file=str(po_path.relative_to(PROJECT_ROOT)),
                entry_id=f"{entry.msgid[:50]}...",
                msgid=entry.msgid,
                msgstr=msgstr,
                issue_type='inline_markup',
                severity='warning',
                description='英語版にあるコードマークアップが日本語版にありません',
                line_number=entry.linenum,
                auto_fixable=False
            )
            issues.append(issue)
            self.stats['warnings'] += 1
        
        return issues
    
    def _fix_bold_spacing(self, text: str) -> str:
        """太字マークアップのスペーシングを修正"""
        # ** の後のスペースを削除
        text = re.sub(r'\*\*\s+', '**', text)
        # ** の前のスペースを削除
        text = re.sub(r'\s+\*\*', '**', text)
        return text
    
    def _fix_italic_spacing(self, text: str) -> str:
        """イタリック体マークアップのスペーシングを修正"""
        # * の後のスペースを削除（ただし ** ではない場合）
        text = re.sub(r'(?<!\*)\*\s+', '*', text)
        # * の前のスペースを削除（ただし ** ではない場合）
        text = re.sub(r'\s+\*(?!\*)', '*', text)
        return text
    
    def _fix_code_spacing(self, text: str) -> str:
        """コードマークアップのスペーシングを修正"""
        # `` の後のスペースを削除
        text = re.sub(r'``\s+', '``', text)
        # `` の前のスペースを削除
        text = re.sub(r'\s+``', '``', text)
        return text
    
    def suggest_fix_with_llm(self, issue: TranslationIssue) -> Optional[str]:
        """LLMを使用して修正案を提案"""
        if not self.use_llm:
            return None
        
        prompt = f"""以下の日本語翻訳にRST構文エラーがあります。正しい構文に修正してください。

問題の種類: {issue.description}

元の英語:
{issue.msgid}

現在の日本語翻訳（エラーあり）:
{issue.msgstr}

修正後の日本語翻訳のみを出力してください。説明は不要です。"""
        
        try:
            response = ollama.chat(
                model=self.llm_model,
                messages=[{'role': 'user', 'content': prompt}]
            )
            return response['message']['content'].strip()
        except Exception as e:
            self.log(f"LLM error: {e}")
            return None
    
    def check_all_files(self) -> List[TranslationIssue]:
        """すべてのPOファイルをチェック"""
        all_issues = []
        
        if not LOCALES_DIR.exists():
            print(f"Error: Locales directory not found: {LOCALES_DIR}")
            return all_issues
        
        po_files = list(LOCALES_DIR.rglob("*.po"))
        self.log(f"Found {len(po_files)} PO files")
        
        for po_file in po_files:
            issues = self.check_po_file(po_file)
            all_issues.extend(issues)
        
        self.issues = all_issues
        return all_issues
    
    def apply_fixes(self, dry_run: bool = False) -> int:
        """自動修正可能な問題を修正"""
        fixed_count = 0
        files_to_update = {}
        
        # 自動修正可能な問題をグループ化
        for issue in self.issues:
            if not issue.auto_fixable or not issue.suggested_fix:
                continue
            
            po_path = PROJECT_ROOT / issue.po_file
            if po_path not in files_to_update:
                files_to_update[po_path] = []
            files_to_update[po_path].append(issue)
        
        # ファイルごとに修正適用
        for po_path, issues in files_to_update.items():
            try:
                po = polib.pofile(str(po_path))
                
                for issue in issues:
                    # エントリーを探して修正 (行番号とmsgidで識別)
                    for entry in po:
                        if (entry.linenum == issue.line_number and 
                            entry.msgid == issue.msgid and 
                            entry.msgstr == issue.msgstr):
                            entry.msgstr = issue.suggested_fix
                            fixed_count += 1
                            self.log(f"Fixed: {po_path.name} line {issue.line_number}")
                            break
                
                if not dry_run:
                    po.save()
                    self.log(f"Saved: {po_path}")
                
            except Exception as e:
                self.log(f"Error fixing {po_path}: {e}")
        
        return fixed_count
    
    def generate_report_json(self, output_path: Optional[Path] = None) -> Path:
        """JSON形式でレポートを生成"""
        if output_path is None:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = OUTPUT_DIR / f"quality_report_{timestamp}.json"
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'stats': self.stats,
            'issues': [asdict(issue) for issue in self.issues]
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return output_path
    
    def generate_report_html(self, output_path: Optional[Path] = None) -> Path:
        """HTML形式でレポートを生成"""
        if output_path is None:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = OUTPUT_DIR / f"quality_report_{timestamp}.html"
        
        # 問題をファイルごとにグループ化
        issues_by_file = {}
        for issue in self.issues:
            if issue.po_file not in issues_by_file:
                issues_by_file[issue.po_file] = []
            issues_by_file[issue.po_file].append(issue)
        
        html = self._generate_html_template(issues_by_file)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return output_path
    
    def _generate_html_template(self, issues_by_file: Dict[str, List[TranslationIssue]]) -> str:
        """HTMLテンプレートを生成"""
        
        severity_colors = {
            'error': '#ff4757',
            'warning': '#ffa502',
            'info': '#3742fa'
        }
        
        issue_type_labels = {
            'empty': '未翻訳',
            'rst_syntax': 'RST構文エラー',
            'inline_markup': 'マークアップ不一致',
            'partial': '部分的翻訳'
        }
        
        html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>翻訳品質レポート - FTC Docs 日本語版</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 28px;
            margin-bottom: 10px;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        .stat-number {{
            font-size: 32px;
            font-weight: 700;
            color: #667eea;
        }}
        
        .stat-label {{
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .file-section {{
            margin-bottom: 30px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            overflow: hidden;
        }}
        
        .file-header {{
            background: #f8f9fa;
            padding: 15px 20px;
            border-bottom: 1px solid #e0e0e0;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .file-header:hover {{
            background: #e9ecef;
        }}
        
        .file-name {{
            font-weight: 600;
            color: #333;
        }}
        
        .issue-count {{
            background: #667eea;
            color: white;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
        }}
        
        .issues-list {{
            display: none;
        }}
        
        .issues-list.expanded {{
            display: block;
        }}
        
        .issue-item {{
            padding: 20px;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .issue-item:last-child {{
            border-bottom: none;
        }}
        
        .issue-header {{
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }}
        
        .severity-badge {{
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            color: white;
        }}
        
        .type-badge {{
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            background: #e0e0e0;
            color: #333;
        }}
        
        .issue-description {{
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
        }}
        
        .issue-content {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
        }}
        
        .issue-text {{
            font-family: 'Courier New', monospace;
            font-size: 14px;
            color: #333;
            margin: 5px 0;
            padding: 10px;
            background: white;
            border-radius: 4px;
            word-wrap: break-word;
        }}
        
        .label {{
            font-weight: 600;
            color: #666;
            margin-top: 10px;
            margin-bottom: 5px;
        }}
        
        .suggested-fix {{
            background: #d4edda;
            border-left: 4px solid #28a745;
        }}
        
        .auto-fixable {{
            display: inline-block;
            background: #28a745;
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
            margin-left: 10px;
        }}
        
        .line-number {{
            font-size: 12px;
            color: #999;
            margin-top: 5px;
        }}
        
        .filter-buttons {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}
        
        .filter-btn {{
            padding: 8px 16px;
            border: 2px solid #667eea;
            background: white;
            color: #667eea;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s;
        }}
        
        .filter-btn:hover {{
            background: #667eea;
            color: white;
        }}
        
        .filter-btn.active {{
            background: #667eea;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 翻訳品質レポート</h1>
            <p>生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{self.stats['total_files']}</div>
                <div class="stat-label">チェック済みファイル</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{self.stats['total_entries']}</div>
                <div class="stat-label">チェック済みエントリー</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(self.issues)}</div>
                <div class="stat-label">検出された問題</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{self.stats['empty_entries']}</div>
                <div class="stat-label">未翻訳</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{self.stats['syntax_errors']}</div>
                <div class="stat-label">構文エラー</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{self.stats['auto_fixable']}</div>
                <div class="stat-label">自動修正可能</div>
            </div>
        </div>
        
        <div class="content">
            <div class="filter-buttons">
                <button class="filter-btn active" onclick="filterIssues('all')">すべて</button>
                <button class="filter-btn" onclick="filterIssues('error')">エラーのみ</button>
                <button class="filter-btn" onclick="filterIssues('warning')">警告のみ</button>
                <button class="filter-btn" onclick="filterIssues('auto-fixable')">自動修正可能のみ</button>
            </div>
"""
        
        # ファイルごとに問題を表示
        for file_path, file_issues in sorted(issues_by_file.items()):
            html += f"""
            <div class="file-section">
                <div class="file-header" onclick="toggleFile(this)">
                    <span class="file-name">{file_path}</span>
                    <span class="issue-count">{len(file_issues)} 件の問題</span>
                </div>
                <div class="issues-list">
"""
            
            for issue in file_issues:
                severity_color = severity_colors.get(issue.severity, '#999')
                type_label = issue_type_labels.get(issue.issue_type, issue.issue_type)
                auto_fixable_badge = '<span class="auto-fixable">自動修正可能</span>' if issue.auto_fixable else ''
                
                html += f"""
                    <div class="issue-item" data-severity="{issue.severity}" data-auto-fixable="{str(issue.auto_fixable).lower()}">
                        <div class="issue-header">
                            <span class="severity-badge" style="background-color: {severity_color};">{issue.severity.upper()}</span>
                            <span class="type-badge">{type_label}</span>
                            {auto_fixable_badge}
                        </div>
                        <div class="issue-description">{issue.description}</div>
                        <div class="line-number">行番号: {issue.line_number}</div>
                        <div class="issue-content">
                            <div class="label">元の英語:</div>
                            <div class="issue-text">{self._escape_html(issue.msgid[:200])}{('...' if len(issue.msgid) > 200 else '')}</div>
                            
                            <div class="label">現在の日本語:</div>
                            <div class="issue-text">{self._escape_html(issue.msgstr[:200]) if issue.msgstr else '(空)'}{('...' if issue.msgstr and len(issue.msgstr) > 200 else '')}</div>
"""
                
                if issue.suggested_fix:
                    html += f"""
                            <div class="label">修正案:</div>
                            <div class="issue-text suggested-fix">{self._escape_html(issue.suggested_fix[:200])}{('...' if len(issue.suggested_fix) > 200 else '')}</div>
"""
                
                html += """
                        </div>
                    </div>
"""
            
            html += """
                </div>
            </div>
"""
        
        html += """
        </div>
    </div>
    
    <script>
        function toggleFile(header) {
            const issuesList = header.nextElementSibling;
            issuesList.classList.toggle('expanded');
        }
        
        function filterIssues(filter) {
            // Update button states
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // Filter issues
            document.querySelectorAll('.issue-item').forEach(item => {
                const severity = item.getAttribute('data-severity');
                const autoFixable = item.getAttribute('data-auto-fixable') === 'true';
                
                let show = false;
                if (filter === 'all') {
                    show = true;
                } else if (filter === 'error' && severity === 'error') {
                    show = true;
                } else if (filter === 'warning' && severity === 'warning') {
                    show = true;
                } else if (filter === 'auto-fixable' && autoFixable) {
                    show = true;
                }
                
                item.style.display = show ? 'block' : 'none';
            });
            
            // Update file section visibility
            document.querySelectorAll('.file-section').forEach(section => {
                const visibleIssues = section.querySelectorAll('.issue-item[style="display: block;"], .issue-item:not([style*="display"])').length;
                section.style.display = visibleIssues > 0 ? 'block' : 'none';
            });
        }
    </script>
</body>
</html>
"""
        
        return html
    
    def _escape_html(self, text: str) -> str:
        """HTMLエスケープ"""
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))
    
    def print_summary(self):
        """サマリーを出力"""
        print("\n" + "="*60)
        print("翻訳品質チェック結果")
        print("="*60)
        print(f"チェック済みファイル: {self.stats['total_files']}")
        print(f"チェック済みエントリー: {self.stats['total_entries']}")
        print(f"検出された問題: {len(self.issues)}")
        print(f"  - 未翻訳: {self.stats['empty_entries']}")
        print(f"  - 構文エラー: {self.stats['syntax_errors']}")
        print(f"  - 警告: {self.stats['warnings']}")
        print(f"自動修正可能: {self.stats['auto_fixable']}")
        print("="*60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Translation Quality Checker - 翻訳品質チェッカー'
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help='チェックのみ実行（修正なし）'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='自動修正可能な問題を修正'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='修正内容を表示するが実際には適用しない'
    )
    parser.add_argument(
        '--report',
        action='store_true',
        help='詳細レポートを生成'
    )
    parser.add_argument(
        '--use-llm',
        action='store_true',
        help='ローカルLLM (Ollama) を使用して修正案を提案'
    )
    parser.add_argument(
        '--llm-model',
        type=str,
        default=DEFAULT_LLM_MODEL,
        help=f'使用するLLMモデル (デフォルト: {DEFAULT_LLM_MODEL})'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='詳細な出力を表示'
    )
    
    args = parser.parse_args()
    
    # デフォルトはチェックモード
    if not (args.check or args.fix or args.report):
        args.check = True
    
    # チェッカーを初期化
    checker = TranslationQualityChecker(
        use_llm=args.use_llm,
        verbose=args.verbose,
        llm_model=args.llm_model
    )
    
    # チェック実行
    print("翻訳品質チェックを開始します...")
    checker.check_all_files()
    checker.print_summary()
    
    # 修正実行
    if args.fix:
        print("\n自動修正を実行します...")
        fixed_count = checker.apply_fixes(dry_run=args.dry_run)
        if args.dry_run:
            print(f"修正可能な問題: {fixed_count} 件")
        else:
            print(f"修正完了: {fixed_count} 件")
    
    # レポート生成
    if args.report or args.fix:
        print("\nレポートを生成します...")
        json_path = checker.generate_report_json()
        print(f"JSONレポート: {json_path}")
        
        html_path = checker.generate_report_html()
        print(f"HTMLレポート: {html_path}")
        print(f"\nブラウザで開く: file://{html_path.absolute()}")
    
    # 終了コード
    sys.exit(0 if len(checker.issues) == 0 else 1)


if __name__ == '__main__':
    main()
