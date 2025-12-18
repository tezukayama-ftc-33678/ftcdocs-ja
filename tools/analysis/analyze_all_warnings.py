#!/usr/bin/env python3
"""
ビルド警告を詳細に分析し、分類するスクリプト

このスクリプトは、Sphinxビルドの警告ログを解析し、警告の種類、
頻度、影響範囲を分析してレポートを生成します。
"""

import sys
import re
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple
import argparse


class WarningAnalyzer:
    """ビルド警告の分析クラス"""
    
    def __init__(self, log_path: Path):
        self.log_path = log_path
        self.warnings = []
        self.warning_types = Counter()
        self.file_warnings = defaultdict(list)
        
    def parse_log(self) -> int:
        """ログファイルを解析"""
        try:
            with open(self.log_path, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"エラー: ログファイル読み込み失敗: {e}")
            sys.exit(1)
        
        current_file = None
        
        for line in lines:
            # WARNING を含む行を抽出
            if 'WARNING:' not in line:
                continue
            
            self.warnings.append(line.strip())
            
            # 警告タイプを分類
            warning_type = self._classify_warning(line)
            self.warning_types[warning_type] += 1
            
            # ファイル情報を抽出
            file_match = re.search(r'([^:]+\.po)', line)
            if file_match:
                po_file = Path(file_match.group(1)).name
                self.file_warnings[po_file].append(warning_type)
            else:
                # .rst ファイル
                file_match = re.search(r'([^:]+\.rst)', line)
                if file_match:
                    rst_file = Path(file_match.group(1)).name
                    self.file_warnings[rst_file].append(warning_type)
        
        return len(self.warnings)
    
    def _classify_warning(self, line: str) -> str:
        """警告を分類"""
        if '<<<<<<< HEAD' in line or 'Problem on line' in line and '<<<<<<' in line:
            return 'Git Merge Conflict'
        elif '=======' in line and 'Problem on line' in line:
            return 'Git Merge Conflict'
        elif '>>>>>>>' in line and 'Problem on line' in line:
            return 'Git Merge Conflict'
        elif 'reading error:' in line and 'list index out of range' in line:
            return 'PO Reading Error'
        elif "Start of line didn't match" in line:
            return 'Line Start Mismatch'
        elif 'Inline strong start-string' in line:
            return 'Inline Markup: **'
        elif 'Inline emphasis start-string' in line:
            return 'Inline Markup: *'
        elif 'Inline literal start-string' in line:
            return 'Inline Markup: `'
        elif 'Problem on line' in line:
            return 'PO Syntax Error'
        elif '<translated>' in line:
            return 'Translation Error'
        else:
            return 'Other'
    
    def print_summary(self):
        """サマリーレポートを表示"""
        print("=" * 70)
        print("ビルド警告分析レポート")
        print("=" * 70)
        
        print(f"\n総警告数: {len(self.warnings)}")
        
        print("\n警告タイプ別:")
        print("-" * 70)
        total = len(self.warnings)
        for warning_type, count in self.warning_types.most_common():
            percentage = (count * 100) // total if total > 0 else 0
            print(f"  {warning_type:30} {count:5} 件 ({percentage:3}%)")
        
        print("\n警告の多いファイル TOP 20:")
        print("-" * 70)
        top_files = sorted(
            self.file_warnings.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )[:20]
        
        for filename, warnings in top_files:
            print(f"  {filename:50} {len(warnings):4} 件")
        
        # 各ファイルの警告内訳を表示（上位5件）
        if top_files:
            print("\n上位ファイルの警告内訳:")
            print("-" * 70)
            for filename, warnings in top_files[:5]:
                print(f"\n{filename}:")
                warning_breakdown = Counter(warnings)
                for wtype, count in warning_breakdown.most_common():
                    print(f"  - {wtype}: {count} 件")
    
    def generate_fix_recommendations(self):
        """修正推奨事項を生成"""
        print("\n" + "=" * 70)
        print("修正推奨事項")
        print("=" * 70)
        
        merge_conflicts = self.warning_types.get('Git Merge Conflict', 0)
        po_errors = self.warning_types.get('PO Reading Error', 0)
        inline_markup = (
            self.warning_types.get('Inline Markup: **', 0) +
            self.warning_types.get('Inline Markup: *', 0) +
            self.warning_types.get('Inline Markup: `', 0)
        )
        
        recommendations = []
        
        if merge_conflicts > 0:
            recommendations.append({
                'priority': 1,
                'title': 'Gitマージコンフリクトの修正',
                'count': merge_conflicts,
                'command': 'python scripts/warnings/fix_merge_conflicts.py',
                'description': 'POファイルに残っているGitマージコンフリクトマーカーを削除'
            })
        
        if inline_markup > 0:
            recommendations.append({
                'priority': 2,
                'title': 'Inline Markup不一致の修正',
                'count': inline_markup,
                'command': 'python scripts/warnings/fix_build_warnings.py',
                'description': '**, *, ` などの開始/終了マーカーの不一致を修正'
            })
        
        if po_errors > 0:
            recommendations.append({
                'priority': 1,
                'title': 'PO読み込みエラーの修正',
                'count': po_errors,
                'command': '手動修正が必要',
                'description': 'POファイルの構文エラーを手動で確認・修正'
            })
        
        # 優先度順にソート
        recommendations.sort(key=lambda x: x['priority'])
        
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec['title']} (優先度: {rec['priority']})")
            print(f"   影響する警告: {rec['count']} 件")
            print(f"   実行コマンド: {rec['command']}")
            print(f"   説明: {rec['description']}")
        
        # 期待される効果
        print("\n期待される警告削減効果:")
        print("-" * 70)
        
        total_fixable = merge_conflicts + inline_markup
        remaining = len(self.warnings) - total_fixable
        
        print(f"  現在の警告数:           {len(self.warnings)} 件")
        print(f"  自動修正可能:           {total_fixable} 件")
        print(f"  修正後の予想警告数:     {remaining} 件")
        print(f"  削減率:                 {(total_fixable * 100 // len(self.warnings) if len(self.warnings) > 0 else 0)}%")
    
    def save_detailed_report(self, output_path: Path):
        """詳細レポートをファイルに保存"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# ビルド警告詳細レポート\n\n")
            f.write(f"総警告数: {len(self.warnings)}\n\n")
            
            f.write("## 警告タイプ別統計\n\n")
            for warning_type, count in self.warning_types.most_common():
                percentage = (count * 100) // len(self.warnings) if len(self.warnings) > 0 else 0
                f.write(f"- {warning_type}: {count} 件 ({percentage}%)\n")
            
            f.write("\n## ファイル別警告数\n\n")
            for filename, warnings in sorted(
                self.file_warnings.items(),
                key=lambda x: len(x[1]),
                reverse=True
            ):
                f.write(f"- {filename}: {len(warnings)} 件\n")
            
            f.write("\n## 全警告リスト\n\n")
            for i, warning in enumerate(self.warnings, 1):
                f.write(f"{i}. {warning}\n")


def main():
    parser = argparse.ArgumentParser(
        description='ビルド警告を詳細に分析'
    )
    parser.add_argument(
        'log_file',
        nargs='?',
        type=Path,
        default=Path('/tmp/build_warnings_current.log'),
        help='警告ログファイルのパス'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='詳細レポートの出力先ファイル'
    )
    
    args = parser.parse_args()
    
    if not args.log_file.exists():
        print(f"エラー: {args.log_file} が見つかりません")
        sys.exit(1)
    
    # 分析実行
    analyzer = WarningAnalyzer(args.log_file)
    warning_count = analyzer.parse_log()
    
    # レポート表示
    analyzer.print_summary()
    analyzer.generate_fix_recommendations()
    
    # 詳細レポート保存
    if args.output:
        analyzer.save_detailed_report(args.output)
        print(f"\n詳細レポートを保存: {args.output}")
    
    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
