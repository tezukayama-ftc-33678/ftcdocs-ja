#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
失敗した翻訳箇所をJSON形式で出力

Windows環境でも文字化けせずに出力できる
"""

import json
import sys
import io
import polib
from pathlib import Path

# Windows対応: stdoutをUTF-8に切り替え
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def main():
    workspace_root = Path(__file__).resolve().parents[2]
    progress_file = workspace_root / 'chinese_fix_progress.json'
    
    if not progress_file.exists():
        print(f"Error: Progress file not found", file=sys.stderr)
        return
    
    with open(progress_file, 'r', encoding='utf-8') as f:
        progress = json.load(f)
    
    # 失敗した箇所を抽出
    failed_items = [(k, v) for k, v in progress.items() if v == 'failed']
    
    # ファイルごとにグループ化して情報収集
    results = {
        'total_failures': len(failed_items),
        'files': []
    }
    
    by_file = {}
    for key, status in failed_items:
        file_path, line = key.rsplit(':', 1)
        if file_path not in by_file:
            by_file[file_path] = []
        by_file[file_path].append(int(line))
    
    # 各ファイルの失敗箇所を分析
    for po_file_path, lines in sorted(by_file.items()):
        po_file = Path(po_file_path)
        rel_path = str(po_file.relative_to(workspace_root))
        
        file_info = {
            'file': rel_path,
            'failures': []
        }
        
        try:
            po = polib.pofile(str(po_file))
            
            for line in sorted(lines):
                # エントリを検索
                entry = None
                for e in po:
                    if e.linenum == line:
                        entry = e
                        break
                
                failure_info = {
                    'line': line
                }
                
                if not entry:
                    failure_info['status'] = 'entry_not_found'
                else:
                    msgid = entry.msgid.strip()
                    msgstr = entry.msgstr.strip()
                    
                    failure_info['msgid'] = msgid
                    failure_info['msgstr'] = msgstr
                    failure_info['msgid_length'] = len(msgid)
                    failure_info['word_count'] = len(msgid.split())
                    
                    # 断片的な文か判定
                    is_fragment = (
                        len(msgid.split()) < 5 or
                        not msgid.endswith(('.', '!', '?', ':')) or
                        msgid.startswith(('a ', 'an ', 'the ', 'and ', 'or ', 'but '))
                    )
                    failure_info['is_fragment'] = is_fragment
                    
                    # 長文か判定
                    failure_info['is_long_text'] = len(msgid) > 200
                    
                file_info['failures'].append(failure_info)
                
        except Exception as e:
            file_info['error'] = str(e)
        
        results['files'].append(file_info)
    
    # JSON出力
    print(json.dumps(results, ensure_ascii=False, indent=2))
    
    # 統計情報を stderr に出力
    fragment_count = sum(
        1 for file_info in results['files']
        for failure in file_info.get('failures', [])
        if failure.get('is_fragment', False)
    )
    long_text_count = sum(
        1 for file_info in results['files']
        for failure in file_info.get('failures', [])
        if failure.get('is_long_text', False)
    )
    
    print(f"\n=== Summary ===", file=sys.stderr)
    print(f"Total failures: {results['total_failures']}", file=sys.stderr)
    print(f"Fragment sentences: {fragment_count} ({fragment_count*100//results['total_failures']}%)", file=sys.stderr)
    print(f"Long texts: {long_text_count} ({long_text_count*100//results['total_failures']}%)", file=sys.stderr)


if __name__ == '__main__':
    main()
