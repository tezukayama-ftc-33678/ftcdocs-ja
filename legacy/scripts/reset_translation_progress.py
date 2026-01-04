#!/usr/bin/env python3
"""翻訳進捗をリセット"""

import json
from pathlib import Path

# 翻訳進捗ファイルをリセット
progress_file = Path('data/translation_progress.json')

if progress_file.exists():
    with open(progress_file, 'r', encoding='utf-8') as f:
        progress = json.load(f)
    
    print(f"Current progress: {len(progress.get('files', {}))} files tracked")
    
    # 翻訳済みカウントをリセット
    for file_path, file_info in progress.get('files', {}).items():
        file_info['translated'] = 0
        file_info['status'] = 'pending'
    
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
    
    print('Reset translation progress')
else:
    print('Translation progress file not found')

# ブロックエントリレポートを削除
blocked_file = Path('data/simplified_chinese_blocked_entries.json')
if blocked_file.exists():
    blocked_file.unlink()
    print('Cleared blocked entries report')

print('Ready to start fresh translation')
