#!/usr/bin/env python3
"""
未翻訳ファイルを一括翻訳するスクリプト
"""
import os
import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).parent / 'scripts'))
from translate_po_smart import SmartPOTranslator

def translate_untranslated_files():
    """untranslated_files.txt に列挙されたファイルを翻訳"""
    
    if not os.path.exists('untranslated_files.txt'):
        print("Error: untranslated_files.txt not found")
        return
    
    with open('untranslated_files.txt', 'r', encoding='utf-8') as f:
        files = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(files)} untranslated files to process")
    print()
    
    translator = SmartPOTranslator('data/translate_config.json')
    
    completed = 0
    failed = []
    
    for i, file_name in enumerate(files, 1):
        po_path = Path('locales/ja/LC_MESSAGES') / file_name
        
        if not po_path.exists():
            print(f"[{i}/{len(files)}] SKIP: {file_name} (file not found)")
            continue
        
        try:
            print(f"[{i}/{len(files)}] Translating: {file_name}...", end=' ', flush=True)
            start = time.time()
            
            translator.translate_po_file(str(po_path))
            elapsed = time.time() - start
            
            print(f"OK [{elapsed:.1f}s]")
            completed += 1
            
        except Exception as e:
            print(f"FAILED: {e}")
            failed.append(file_name)
    
    print()
    print("=" * 60)
    print(f"Completed: {completed}/{len(files)}")
    if failed:
        print(f"Failed: {len(failed)}")
        for f in failed:
            print(f"  - {f}")
    print("=" * 60)

if __name__ == '__main__':
    translate_untranslated_files()
