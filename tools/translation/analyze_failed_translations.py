#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
失敗した翻訳箇所を手動で確認・修正するヘルパースクリプト

長文や文脈が必要な箇所は、前後のエントリも含めて翻訳する必要がある
"""

import json
import sys
import polib
from pathlib import Path
from colorama import Fore, Style, init

# Windows対応
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

init(autoreset=True)

def main():
    workspace_root = Path(__file__).resolve().parents[2]
    progress_file = workspace_root / 'chinese_fix_progress.json'
    
    if not progress_file.exists():
        print(f"{Fore.RED}✗ Progress file not found{Style.RESET_ALL}")
        return
    
    with open(progress_file, 'r', encoding='utf-8') as f:
        progress = json.load(f)
    
    # 失敗した箇所を抽出
    failed_items = [(k, v) for k, v in progress.items() if v == 'failed']
    
    print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}失敗した翻訳箇所の分析{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
    print(f"失敗件数: {len(failed_items)}\n")
    
    # ファイルごとにグループ化
    by_file = {}
    for key, status in failed_items:
        file_path, line = key.rsplit(':', 1)
        if file_path not in by_file:
            by_file[file_path] = []
        by_file[file_path].append(int(line))
    
    # 各ファイルの失敗箇所を表示
    for po_file_path, lines in sorted(by_file.items()):
        po_file = Path(po_file_path)
        rel_path = po_file.relative_to(workspace_root)
        
        print(f"\n{Fore.BLUE}{'─'*70}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}File: {rel_path}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{'─'*70}{Style.RESET_ALL}\n")
        
        try:
            po = polib.pofile(str(po_file))
            
            for line in sorted(lines):
                # エントリを検索
                entry = None
                for e in po:
                    if e.linenum == line:
                        entry = e
                        break
                
                if not entry:
                    print(f"{Fore.YELLOW}Line {line}: Entry not found{Style.RESET_ALL}")
                    continue
                
                # エントリの情報を表示
                print(f"{Fore.YELLOW}Line {line}:{Style.RESET_ALL}")
                print(f"  {Fore.GREEN}msgid:{Style.RESET_ALL}")
                msgid_preview = entry.msgid[:100] + "..." if len(entry.msgid) > 100 else entry.msgid
                print(f"    {msgid_preview}")
                
                print(f"  {Fore.RED}msgstr (current - contains Chinese):{Style.RESET_ALL}")
                msgstr_preview = entry.msgstr[:100] + "..." if len(entry.msgstr) > 100 else entry.msgstr
                print(f"    {msgstr_preview}")
                
                # 断片的な文か判定
                is_fragment = (
                    len(entry.msgid.split()) < 5 or  # 5単語未満
                    not entry.msgid.strip().endswith(('.', '!', '?', ':')) or  # 文末記号なし
                    entry.msgid.startswith(('a ', 'an ', 'the ', 'and ', 'or ', 'but '))  # 接続詞始まり
                )
                
                if is_fragment:
                    print(f"  {Fore.MAGENTA}⚠ 断片的な文 - 前後の文脈が必要な可能性{Style.RESET_ALL}")
                
                # 長文か判定
                if len(entry.msgid) > 200:
                    print(f"  {Fore.MAGENTA}⚠ 長文 ({len(entry.msgid)} chars) - 翻訳が難しい可能性{Style.RESET_ALL}")
                
                print()
                
        except Exception as e:
            print(f"{Fore.RED}✗ Error reading {po_file}: {e}{Style.RESET_ALL}")
    
    # 推奨事項
    print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}推奨される対処法{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
    
    print("1. 断片的な文が多い場合:")
    print("   → 手動で前後の文脈を含めて翻訳する")
    print("   → または元のエントリを修正して完全な文にする\n")
    
    print("2. より高品質なモデルを試す:")
    print("   → gemma2:9b-instruct-q4_K_M を使用")
    print(f"   → {Fore.YELLOW}python tools/translation/fix_chinese_errors.py --model gemma2:9b-instruct-q4_K_M --no-skip{Style.RESET_ALL}\n")
    
    print("3. 温度を下げてより保守的な翻訳にする:")
    print("   → translate_config.json で temperature を 0.1 に設定\n")
    
    print("4. 手動で修正:")
    print("   → 上記のファイルを直接編集して中国語を削除\n")


if __name__ == '__main__':
    main()
