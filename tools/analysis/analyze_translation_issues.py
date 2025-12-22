#!/usr/bin/env python3
"""
翻訳問題の分析と優先順位付けツール

ビルド警告を分析し、日本語翻訳が反映されない原因を特定します。
- RST構文エラー
- Sphinx警告
- 未翻訳箇所
- 構文ミスで反映されていない翻訳

使い方:
    # ビルドして警告を分析
    cd docs && make clean && make html-ja 2>&1 | tee build.log
    python tools/analysis/analyze_translation_issues.py build.log

    # HTMLレポート生成
    python tools/analysis/analyze_translation_issues.py build.log --html-report report.html
    
    # 優先度順に問題をソート
    python tools/analysis/analyze_translation_issues.py build.log --sort-by priority
"""

import re
import sys
import json
import argparse
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple
import subprocess

# プロジェクトルート
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
DOCS_ROOT = PROJECT_ROOT / "docs"


class TranslationIssueAnalyzer:
    """翻訳問題の分析器"""
    
    def __init__(self, build_log_path: Path):
        self.build_log_path = build_log_path
        self.warnings = []
        self.stats = Counter()
        self.issues_by_file = defaultdict(list)
        self.issues_by_type = defaultdict(list)
        
        # 警告タイプの重大度マッピング
        self.severity_map = {
            # 高優先度（日本語が表示されない原因）
            'undefined label': 'critical',
            'unknown document': 'critical',
            'inconsistent term references': 'high',
            'inconsistent references': 'high',
            
            # 中優先度（表示に影響するが致命的ではない）
            'Inline interpreted text or phrase reference start-string without end-string': 'medium',
            'Inline emphasis start-string without end-string': 'medium',
            'Inline literal start-string without end-string': 'medium',
            'Inline strong start-string without end-string': 'medium',
            
            # 低優先度（表示に大きな影響なし）
            'Block quote ends without a blank line': 'low',
            'Title underline too short': 'low',
            'Mismatch': 'low',
        }
    
    def parse_build_log(self):
        """ビルドログをパース"""
        print(f"[INFO] ビルドログを読み込み中: {self.build_log_path}")
        
        if not self.build_log_path.exists():
            print(f"❌ ビルドログが見つかりません: {self.build_log_path}")
            return
        
        with open(self.build_log_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 警告を抽出
        warning_pattern = r'(.+?):(\d+):\s*WARNING:\s*(.+?)(?:\n|$)'
        matches = re.finditer(warning_pattern, content, re.MULTILINE)
        
        for match in matches:
            file_path = match.group(1)
            line_num = int(match.group(2))
            message = match.group(3).strip()
            
            # 警告タイプを判定
            warning_type = self.classify_warning(message)
            severity = self.get_severity(warning_type)
            
            warning = {
                'file': file_path,
                'line': line_num,
                'message': message,
                'type': warning_type,
                'severity': severity,
            }
            
            self.warnings.append(warning)
            self.stats[warning_type] += 1
            self.issues_by_file[file_path].append(warning)
            self.issues_by_type[warning_type].append(warning)
        
        print(f"[INFO] 警告数: {len(self.warnings)}")
        print()
    
    def classify_warning(self, message: str) -> str:
        """警告メッセージからタイプを分類"""
        # 各タイプをチェック
        if 'undefined label' in message.lower():
            return 'undefined label'
        elif 'unknown document' in message.lower():
            return 'unknown document'
        elif 'inconsistent term references' in message.lower():
            return 'inconsistent term references'
        elif 'inconsistent references' in message.lower():
            return 'inconsistent references'
        elif 'Inline interpreted text' in message:
            return 'Inline interpreted text or phrase reference start-string without end-string'
        elif 'Inline emphasis' in message:
            return 'Inline emphasis start-string without end-string'
        elif 'Inline literal' in message:
            return 'Inline literal start-string without end-string'
        elif 'Inline strong' in message:
            return 'Inline strong start-string without end-string'
        elif 'Block quote ends' in message:
            return 'Block quote ends without a blank line'
        elif 'Title underline' in message:
            return 'Title underline too short'
        elif 'Mismatch' in message:
            return 'Mismatch'
        elif 'term not in glossary' in message:
            return 'term not in glossary'
        elif 'duplicate term' in message:
            return 'duplicate term description'
        elif "isn't included in any toctree" in message:
            return 'document not in toctree'
        else:
            return 'other'
    
    def get_severity(self, warning_type: str) -> str:
        """警告タイプから重大度を取得"""
        return self.severity_map.get(warning_type, 'low')
    
    def analyze_japanese_label_issues(self):
        """日本語ラベル参照の問題を分析"""
        japanese_label_issues = []
        
        for warning in self.warnings:
            if warning['type'] == 'undefined label':
                # メッセージから日本語が含まれるか確認
                message = warning['message']
                has_japanese = any('\u3040' <= c <= '\u309F' or
                                 '\u30A0' <= c <= '\u30FF' or
                                 '\u4E00' <= c <= '\u9FFF'
                                 for c in message)
                
                if has_japanese:
                    japanese_label_issues.append(warning)
        
        return japanese_label_issues
    
    def analyze_japanese_doc_path_issues(self):
        """日本語ドキュメントパスの問題を分析"""
        japanese_doc_issues = []
        
        for warning in self.warnings:
            if warning['type'] == 'unknown document':
                message = warning['message']
                has_japanese = any('\u3040' <= c <= '\u309F' or
                                 '\u30A0' <= c <= '\u30FF' or
                                 '\u4E00' <= c <= '\u9FFF'
                                 for c in message)
                
                if has_japanese:
                    japanese_doc_issues.append(warning)
        
        return japanese_doc_issues
    
    def generate_priority_report(self):
        """優先順位付きレポートを生成"""
        print("=" * 80)
        print("📊 翻訳問題分析レポート")
        print("=" * 80)
        print()
        
        # 統計情報
        print("【統計】")
        print(f"  総警告数: {len(self.warnings)}")
        print(f"  影響を受けるファイル数: {len(self.issues_by_file)}")
        print()
        
        # 重大度別
        severity_counts = Counter()
        for warning in self.warnings:
            severity_counts[warning['severity']] += 1
        
        print("【重大度別】")
        for severity in ['critical', 'high', 'medium', 'low']:
            count = severity_counts[severity]
            if count > 0:
                icon = {'critical': '🔴', 'high': '🟠', 'medium': '🟡', 'low': '⚪'}[severity]
                print(f"  {icon} {severity.upper()}: {count}件")
        print()
        
        # 警告タイプ別（上位10件）
        print("【警告タイプ別（上位10件）】")
        for warning_type, count in self.stats.most_common(10):
            severity = self.get_severity(warning_type)
            icon = {'critical': '🔴', 'high': '🟠', 'medium': '🟡', 'low': '⚪'}[severity]
            print(f"  {icon} {warning_type}: {count}件")
        print()
        
        # 日本語ラベルの問題
        ja_label_issues = self.analyze_japanese_label_issues()
        if ja_label_issues:
            print(f"【🔴 最重要】日本語ラベル参照の問題: {len(ja_label_issues)}件")
            print("  これらは翻訳が反映されない直接的な原因です。")
            print("  ラベル名を英語のまま保持し、表示テキストのみ翻訳する必要があります。")
            print()
            for issue in ja_label_issues[:5]:
                print(f"  - {Path(issue['file']).name}:{issue['line']}")
                print(f"    {issue['message'][:80]}...")
            if len(ja_label_issues) > 5:
                print(f"  ... 他{len(ja_label_issues) - 5}件")
            print()
        
        # 日本語ドキュメントパスの問題
        ja_doc_issues = self.analyze_japanese_doc_path_issues()
        if ja_doc_issues:
            print(f"【🔴 最重要】日本語ドキュメントパスの問題: {len(ja_doc_issues)}件")
            print("  ドキュメント参照パスを英語のまま保持する必要があります。")
            print()
            for issue in ja_doc_issues[:5]:
                print(f"  - {Path(issue['file']).name}:{issue['line']}")
                print(f"    {issue['message'][:80]}...")
            if len(ja_doc_issues) > 5:
                print(f"  ... 他{len(ja_doc_issues) - 5}件")
            print()
        
        # ファイル別の問題（上位10件）
        print("【影響を受けるファイル（問題が多い順、上位10件）】")
        sorted_files = sorted(self.issues_by_file.items(), 
                            key=lambda x: len(x[1]), reverse=True)
        
        for file_path, issues in sorted_files[:10]:
            file_name = Path(file_path).name
            critical_count = sum(1 for i in issues if i['severity'] == 'critical')
            high_count = sum(1 for i in issues if i['severity'] == 'high')
            
            severity_str = ""
            if critical_count > 0:
                severity_str += f"🔴{critical_count} "
            if high_count > 0:
                severity_str += f"🟠{high_count}"
            
            print(f"  {file_name}: {len(issues)}件 {severity_str}")
        print()
    
    def generate_html_report(self, output_path: Path):
        """HTML形式の詳細レポートを生成"""
        # 重大度別カウント
        severity_counts = Counter()
        for warning in self.warnings:
            severity_counts[warning['severity']] += 1
        
        # 日本語関連の問題
        ja_label_issues = self.analyze_japanese_label_issues()
        ja_doc_issues = self.analyze_japanese_doc_path_issues()
        
        html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>翻訳問題分析レポート</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #2c3e50;
            margin-top: 30px;
            border-bottom: 2px solid #bdc3c7;
            padding-bottom: 5px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stat-card h3 {{
            margin: 0 0 10px 0;
            color: #7f8c8d;
            font-size: 14px;
        }}
        .stat-card .value {{
            font-size: 28px;
            font-weight: bold;
        }}
        .critical {{ color: #e74c3c; }}
        .high {{ color: #e67e22; }}
        .medium {{ color: #f39c12; }}
        .low {{ color: #95a5a6; }}
        
        .issue-card {{
            background: white;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .issue-card.critical {{ border-left: 4px solid #e74c3c; }}
        .issue-card.high {{ border-left: 4px solid #e67e22; }}
        .issue-card.medium {{ border-left: 4px solid #f39c12; }}
        .issue-card.low {{ border-left: 4px solid #95a5a6; }}
        
        .issue-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}
        .issue-file {{
            font-weight: bold;
            color: #2c3e50;
        }}
        .issue-line {{
            background: #ecf0f1;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
        }}
        .issue-message {{
            font-family: monospace;
            background: #f8f9fa;
            padding: 10px;
            border-radius: 4px;
            margin-top: 10px;
            font-size: 13px;
            line-height: 1.4;
        }}
        .badge {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: bold;
            text-transform: uppercase;
        }}
        .badge.critical {{ background: #e74c3c; color: white; }}
        .badge.high {{ background: #e67e22; color: white; }}
        .badge.medium {{ background: #f39c12; color: white; }}
        .badge.low {{ background: #95a5a6; color: white; }}
        
        .warning-type-list {{
            list-style: none;
            padding: 0;
        }}
        .warning-type-list li {{
            padding: 8px;
            margin: 5px 0;
            background: white;
            border-radius: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .count {{
            background: #3498db;
            color: white;
            padding: 2px 10px;
            border-radius: 12px;
            font-weight: bold;
        }}
        
        .alert {{
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }}
        .alert.critical {{
            background: #fadbd8;
            border-left: 4px solid #e74c3c;
        }}
        .alert h3 {{
            margin: 0 0 10px 0;
            color: #c0392b;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ecf0f1;
        }}
        th {{
            background: #34495e;
            color: white;
            font-weight: bold;
        }}
        tr:hover {{
            background: #f8f9fa;
        }}
    </style>
</head>
<body>
    <h1>📊 翻訳問題分析レポート</h1>
    <p>ビルドログ: <code>{self.build_log_path.name}</code></p>
    
    <div class="stats">
        <div class="stat-card">
            <h3>総警告数</h3>
            <div class="value">{len(self.warnings)}</div>
        </div>
        <div class="stat-card">
            <h3>影響ファイル数</h3>
            <div class="value">{len(self.issues_by_file)}</div>
        </div>
        <div class="stat-card">
            <h3>Critical</h3>
            <div class="value critical">{severity_counts['critical']}</div>
        </div>
        <div class="stat-card">
            <h3>High</h3>
            <div class="value high">{severity_counts['high']}</div>
        </div>
        <div class="stat-card">
            <h3>Medium</h3>
            <div class="value medium">{severity_counts['medium']}</div>
        </div>
        <div class="stat-card">
            <h3>Low</h3>
            <div class="value low">{severity_counts['low']}</div>
        </div>
    </div>
"""
        
        # 日本語関連の問題を表示
        if ja_label_issues or ja_doc_issues:
            html_content += """
    <h2>🔴 最重要: 日本語関連の問題</h2>
    <div class="alert critical">
        <h3>⚠️ これらは翻訳が反映されない直接的な原因です</h3>
        <p>ラベル名やドキュメントパスを英語のまま保持し、表示テキストのみ翻訳する必要があります。</p>
    </div>
"""
            
            if ja_label_issues:
                html_content += f"""
    <h3>日本語ラベル参照の問題 ({len(ja_label_issues)}件)</h3>
"""
                for issue in ja_label_issues[:20]:
                    file_name = Path(issue['file']).name
                    html_content += f"""
    <div class="issue-card critical">
        <div class="issue-header">
            <span class="issue-file">{file_name}</span>
            <span class="issue-line">行 {issue['line']}</span>
        </div>
        <div class="issue-message">{issue['message']}</div>
    </div>
"""
            
            if ja_doc_issues:
                html_content += f"""
    <h3>日本語ドキュメントパスの問題 ({len(ja_doc_issues)}件)</h3>
"""
                for issue in ja_doc_issues[:20]:
                    file_name = Path(issue['file']).name
                    html_content += f"""
    <div class="issue-card critical">
        <div class="issue-header">
            <span class="issue-file">{file_name}</span>
            <span class="issue-line">行 {issue['line']}</span>
        </div>
        <div class="issue-message">{issue['message']}</div>
    </div>
"""
        
        # 警告タイプ別統計
        html_content += """
    <h2>警告タイプ別統計</h2>
    <ul class="warning-type-list">
"""
        for warning_type, count in self.stats.most_common():
            severity = self.get_severity(warning_type)
            html_content += f"""
        <li>
            <span><span class="badge {severity}">{severity}</span> {warning_type}</span>
            <span class="count">{count}</span>
        </li>
"""
        html_content += """
    </ul>
    
    <h2>影響を受けるファイル（問題が多い順）</h2>
    <table>
        <thead>
            <tr>
                <th>ファイル</th>
                <th>警告数</th>
                <th>Critical</th>
                <th>High</th>
                <th>Medium</th>
                <th>Low</th>
            </tr>
        </thead>
        <tbody>
"""
        
        sorted_files = sorted(self.issues_by_file.items(), 
                            key=lambda x: len(x[1]), reverse=True)
        
        for file_path, issues in sorted_files[:30]:
            file_name = Path(file_path).name
            counts_by_severity = Counter(i['severity'] for i in issues)
            
            html_content += f"""
            <tr>
                <td><strong>{file_name}</strong></td>
                <td>{len(issues)}</td>
                <td class="critical">{counts_by_severity['critical']}</td>
                <td class="high">{counts_by_severity['high']}</td>
                <td class="medium">{counts_by_severity['medium']}</td>
                <td class="low">{counts_by_severity['low']}</td>
            </tr>
"""
        
        html_content += """
        </tbody>
    </table>
</body>
</html>
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTMLレポート生成完了: {output_path}")
    
    def export_json(self, output_path: Path):
        """JSON形式でエクスポート"""
        data = {
            'total_warnings': len(self.warnings),
            'files_affected': len(self.issues_by_file),
            'warnings': self.warnings,
            'stats': dict(self.stats),
            'japanese_label_issues': self.analyze_japanese_label_issues(),
            'japanese_doc_issues': self.analyze_japanese_doc_path_issues(),
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ JSONエクスポート完了: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='ビルド警告を分析して翻訳問題を特定'
    )
    parser.add_argument('build_log', type=str,
                       help='ビルドログファイルのパス')
    parser.add_argument('--html-report', type=str,
                       help='HTML形式のレポートを出力')
    parser.add_argument('--json', type=str,
                       help='JSON形式でエクスポート')
    parser.add_argument('--sort-by', choices=['priority', 'file', 'type'],
                       default='priority',
                       help='ソート順（デフォルト: priority）')
    
    args = parser.parse_args()
    
    build_log_path = Path(args.build_log)
    
    analyzer = TranslationIssueAnalyzer(build_log_path)
    analyzer.parse_build_log()
    analyzer.generate_priority_report()
    
    if args.html_report:
        analyzer.generate_html_report(Path(args.html_report))
    
    if args.json:
        analyzer.export_json(Path(args.json))


if __name__ == '__main__':
    main()
