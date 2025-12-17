#!/usr/bin/env python3
"""
ビルド警告を分析し、該当するPOエントリを特定するスクリプト
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple
import polib


def parse_warning_log(log_path: Path) -> Dict[str, List[Tuple[int, str]]]:
    """
    警告ログを解析して、ファイルごとの警告をまとめる
    
    戻り値: {rst_file_path: [(line_num, warning_message), ...]}
    """
    warnings_by_file = defaultdict(list)
    warning_count = 0
    
    with open(log_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    
    # パターン1: path/to/file.rst:123:<translated>:1: WARNING: message
    # パターン2: WARNING: Start of line didn't match...
    
    for i, line in enumerate(lines):
        # <translated> を含む警告
        match1 = re.match(r'([^:]+\.rst):(\d+):<translated>:\d+:\s*WARNING:\s*(.+)', line)
        if match1:
            rst_file = match1.group(1)
            line_num = int(match1.group(2))
            warning_msg = match1.group(3).strip()
            warnings_by_file[rst_file].append((line_num, warning_msg))
            warning_count += 1
        
        # 通常のWARNING (こちらはfileまたはProblem on lineを持つ)
        if 'WARNING:' in line and '<translated>' not in line:
            # Problem on lineを探す
            if 'Problem on line' in line:
                match2 = re.search(r'Problem on line (\d+):', line)
                if match2:
                    line_num = int(match2.group(1))
                    # この警告はどのファイルのもの?
                    # 前の行を遡って探す
                    warning_count += 1
    
    return dict(warnings_by_file), warning_count


def find_po_file_for_rst(rst_path: str, locales_dir: Path) -> Path:
    """
    RSTファイルに対応するPOファイルを見つける
    """
    # RST path example: H:\ftcdocs-ja\docs\source\apriltag\...\file.rst
    # PO path example: H:\ftcdocs-ja\locales\ja\LC_MESSAGES\apriltag\...\file.po
    
    rst_path_obj = Path(rst_path)
    
    # source/ 以降の相対パスを取得
    try:
        # source ディレクトリを見つける
        parts = rst_path_obj.parts
        if 'source' in parts:
            source_idx = parts.index('source')
            relative_parts = parts[source_idx + 1:]
            
            # .rst を .po に変換
            po_parts = list(relative_parts[:-1]) + [relative_parts[-1].replace('.rst', '.po')]
            
            po_path = locales_dir / Path(*po_parts)
            
            return po_path
    except Exception as e:
        print(f"警告: POファイルパスの変換に失敗: {rst_path} - {e}")
    
    return None


def analyze_warnings():
    """
    警告を分析してレポートを生成
    """
    script_dir = Path(__file__).parent
    log_path = script_dir / 'build_warnings.log'
    locales_dir = script_dir / 'locales' / 'ja' / 'LC_MESSAGES'
    
    if not log_path.exists():
        print(f"エラー: {log_path} が見つかりません")
        sys.exit(1)
    
    print("="*70)
    print("ビルド警告分析")
    print("="*70)
    
    warnings, total_warnings = parse_warning_log(log_path)
    
    print(f"\n警告のあるファイル数: {len(warnings)}")
    print(f"警告総数: {sum(len(w) for w in warnings.values())}")
    
    # 警告タイプ別集計
    warning_types = defaultdict(int)
    for file_warnings in warnings.values():
        for _, msg in file_warnings:
            # 警告タイプを抽出
            if 'Inline strong start-string' in msg:
                warning_types['Inline strong (** 不一致)'] += 1
            elif 'Inline emphasis start-string' in msg:
                warning_types['Inline emphasis (* 不一致)'] += 1
            elif 'Inline literal start-string' in msg:
                warning_types['Inline literal (` 不一致)'] += 1
            else:
                warning_types['その他'] += 1
    
    print("\n警告タイプ別:")
    print("-"*70)
    for wtype, count in sorted(warning_types.items(), key=lambda x: x[1], reverse=True):
        print(f"  {wtype:40} {count:5} 件")
    
    # 最も警告の多いファイルTOP 20
    print("\n警告の多いファイルTOP 20:")
    print("-"*70)
    sorted_files = sorted(warnings.items(), key=lambda x: len(x[1]), reverse=True)[:20]
    
    for rst_file, file_warnings in sorted_files:
        # ファイル名だけを表示
        file_name = Path(rst_file).name
        parent_dir = Path(rst_file).parent.name
        display_name = f"{parent_dir}/{file_name}"
        
        print(f"  {display_name:50} {len(file_warnings):3} 件")
        
        # 対応するPOファイルが存在するか確認
        po_file = find_po_file_for_rst(rst_file, locales_dir)
        if po_file and po_file.exists():
            print(f"    -> PO: {po_file.relative_to(locales_dir)}")
        else:
            print(f"    -> PO: 見つかりません")
    
    # サンプル警告を表示
    print("\n警告サンプル:")
    print("-"*70)
    count = 0
    for rst_file, file_warnings in sorted_files[:5]:
        if count >= 10:
            break
        
        print(f"\nファイル: {Path(rst_file).name}")
        for line_num, msg in file_warnings[:2]:  # 各ファイルから2件
            print(f"  行 {line_num}: {msg[:80]}...")
            count += 1
            if count >= 10:
                break
    
    # POファイルへのマッピング統計
    print("\n\nPOファイルマッピング:")
    print("-"*70)
    mapped_count = 0
    not_found_count = 0
    
    for rst_file in warnings.keys():
        po_file = find_po_file_for_rst(rst_file, locales_dir)
        if po_file and po_file.exists():
            mapped_count += 1
        else:
            not_found_count += 1
    
    print(f"  マッピング成功: {mapped_count} ファイル")
    print(f"  PO未発見:      {not_found_count} ファイル")
    
    print("\n" + "="*70)
    print("分析完了")
    print("="*70)
    
    # 修正推奨事項
    print("\n修正推奨:")
    print("1. fix_build_warnings.py を実行して自動修正を試す")
    print("2. 残った警告はLLMで手動修正")
    print("3. 特に以下のファイルを優先:")
    for rst_file, file_warnings in sorted_files[:5]:
        print(f"   - {Path(rst_file).name} ({len(file_warnings)} 件)")


if __name__ == '__main__':
    analyze_warnings()
