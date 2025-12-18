#!/usr/bin/env python3
"""
POファイルのline 9の問題を修正するスクリプト
"""

import sys
from pathlib import Path


def fix_po_header(po_path: Path) -> bool:
    """POファイルのヘッダーを修正"""
    try:
        with open(po_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        for i, line in enumerate(lines):
            # line 9あたりで 'msgstr """' を探す
            if 'msgstr """' in line:
                # これを2行に分割
                indent = len(line) - len(line.lstrip())
                lines[i] = ' ' * indent + 'msgstr ""\n'
                modified = True
                print(f"修正: {po_path}")
                break
        
        if modified:
            with open(po_path, 'w', encoding='utf-8', newline='\n') as f:
                f.writelines(lines)
            return True
        
        return False
    
    except Exception as e:
        print(f"エラー: {po_path}: {e}")
        return False


def main():
    locales_dir = Path('locales/ja/LC_MESSAGES')
    
    if not locales_dir.exists():
        print(f"エラー: {locales_dir} が見つかりません")
        sys.exit(1)
    
    po_files = list(locales_dir.glob('**/*.po'))
    fixed_count = 0
    
    print("POファイルヘッダー修正スクリプト")
    print("="*70)
    
    for po_path in po_files:
        if fix_po_header(po_path):
            fixed_count += 1
    
    print("="*70)
    print(f"修正完了: {fixed_count}/{len(po_files)} ファイル")


if __name__ == '__main__':
    main()
