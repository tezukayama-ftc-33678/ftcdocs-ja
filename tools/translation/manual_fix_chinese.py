#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡単な中国語フレーズを手動パターンで修正

よくある中国語フレーズを日本語に置換
"""

import sys
import io
import polib
from pathlib import Path
from colorama import Fore, Style, init

# Windows対応
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

init(autoreset=True)

# 中国語→日本語の置換パターン
CHINESE_TO_JAPANESE = {
    '对于': '',  # 「～に対して」の意味だが、通常は削除で文意が通る
    '识别': '認識',
    '几乎': 'ほとんど',
    '之间应留有': 'の間には',
    '因为': 'なぜなら',
    '所以': 'したがって',
    '可以通过': 'によって',
    '拥有': '持つ',
    '姿态': '姿勢',
    '估计': '推定',
    '校准': 'キャリブレーション',
    '通过': 'を通じて',
    '提供': '提供する',
    '应': '',
    '留有': '',
    '単页': '単一ページ',
    '且': 'で',
    '包含': '含む',
    '高级信息': '高レベルの情報',
    '将其': 'それを',
    '我们会看到它是如何被': 'それがどのように',
    '对于此句，翻译如下：': '',  # LLMのメタコメントを削除
    '翻译如下': '',
    '可以更好翻译为：': '',
    '双摄像头': 'デュアルウェブカメラ',
    '会成为一个问题': 'が問題になる可能性があります',
    '譯': '',  # 「訳」の簡体字
}

def fix_entry_simple(msgstr: str) -> str:
    """簡単な置換で中国語を修正"""
    fixed = msgstr
    for chinese, japanese in CHINESE_TO_JAPANESE.items():
        if chinese in fixed:
            fixed = fixed.replace(chinese, japanese)
    return fixed

def main():
    workspace_root = Path(__file__).resolve().parents[2]
    
    # failed_analysis.jsonから失敗箇所を読み込む
    import json
    with open(workspace_root / 'failed_analysis.json', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    fixed_count = 0
    still_has_chinese_count = 0
    
    print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}簡単な中国語フレーズを手動パターンで修正{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
    
    for file_info in data['files']:
        po_path = workspace_root / file_info['file']
        if not po_path.exists():
            continue
            
        po = polib.pofile(str(po_path))
        file_modified = False
        
        for failure in file_info['failures']:
            if 'msgstr' not in failure:
                continue
                
            line = failure['line']
            msgstr_old = failure['msgstr']
            
            # エントリを検索
            entry = None
            for e in po:
                if e.linenum == line:
                    entry = e
                    break
            
            if not entry:
                continue
            
            # 簡単な置換を試す
            msgstr_new = fix_entry_simple(entry.msgstr)
            
            if msgstr_new != entry.msgstr:
                print(f"{Fore.YELLOW}Fixing {file_info['file']}:{line}{Style.RESET_ALL}")
                print(f"  Old: {entry.msgstr[:80]}...")
                entry.msgstr = msgstr_new
                print(f"  New: {msgstr_new[:80]}...")
                file_modified = True
                fixed_count += 1
                
                # まだ簡体字が残っているかチェック
                forbidden_chars = set('为拥态估镜头厅览购谁块际习远让边务验压担处团阶员调导测协围确阳养层双医审护坏优获临预规织奖随扩杂输维缺另评错须怀产业们发经应对时进实现动过问题')
                if any(char in msgstr_new for char in forbidden_chars):
                    print(f"  {Fore.RED}⚠ Still contains Chinese characters{Style.RESET_ALL}")
                    still_has_chinese_count += 1
                else:
                    print(f"  {Fore.GREEN}✓ No Chinese characters detected{Style.RESET_ALL}")
                print()
        
        if file_modified:
            po.save()
            print(f"{Fore.GREEN}✓ Saved {file_info['file']}{Style.RESET_ALL}\n")
    
    print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Summary{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"Fixed entries: {fixed_count}")
    print(f"Still contains Chinese: {still_has_chinese_count}")
    print(f"Clean: {fixed_count - still_has_chinese_count}")

if __name__ == '__main__':
    main()
