#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PO 構文エラーの自動修正
- エスケープされていないダブルクォートを修正
- msgid/msgstr内の " を \" に置換（既にエスケープされている場合は除く）
"""

import re
from pathlib import Path

def fix_po_quotes(content: str) -> tuple:
    """PO ファイルの msgstr 内のダブルクォートをエスケープ"""
    lines = content.split('\n')
    fixed_lines = []
    fixes = 0
    
    in_msgstr = False
    for line in lines:
        # msgid/msgstr の開始を検出
        if line.startswith('msgid ') or line.startswith('msgstr '):
            in_msgstr = True
            fixed_lines.append(line)
            continue
        
        # 空行で msgid/msgstr ブロック終了
        if not line.strip():
            in_msgstr = False
            fixed_lines.append(line)
            continue
        
        # msgstr ブロック内の継続行
        if in_msgstr and line.startswith('"') and line.endswith('"'):
            # 行内のエスケープされていない " を \" に変更
            # ただし、行頭と行末の " は除外
            inner = line[1:-1]  # 行頭・行末の " を除外
            
            # すでにエスケープされている \" は一時的に置換
            inner = inner.replace(r'\"', '\x00ESCAPED_QUOTE\x00')
            # エスケープされていない " を \" に変更
            inner = inner.replace('"', r'\"')
            # 一時置換を戻す
            inner = inner.replace('\x00ESCAPED_QUOTE\x00', r'\"')
            
            new_line = f'"{inner}"'
            if new_line != line:
                fixes += 1
            fixed_lines.append(new_line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), fixes

def main():
    repo = Path(__file__).parent
    po_dir = repo / 'locales' / 'ja' / 'LC_MESSAGES'
    
    total_fixes = 0
    fixed_files = 0
    
    for po_file in po_dir.rglob('*.po'):
        try:
            content = po_file.read_text(encoding='utf-8')
            fixed_content, fixes = fix_po_quotes(content)
            
            if fixes > 0:
                po_file.write_text(fixed_content, encoding='utf-8')
                fixed_files += 1
                total_fixes += fixes
                print(f'OK {po_file.relative_to(repo)}: {fixes} fixes')
        except Exception as e:
            print(f'ERR {po_file.relative_to(repo)}: {e}')
    
    print(f'\nTotal: {fixed_files} files, {total_fixes} fixes')

if __name__ == '__main__':
    main()
