#!/usr/bin/env python3
from pathlib import Path
import polib

po_dir = Path('locales/ja/LC_MESSAGES')
po_files = sorted(list(po_dir.glob('**/*.po')))

partial = []
for po_file in po_files:
    try:
        po = polib.pofile(str(po_file))
    except:
        continue
    
    entries = [e for e in po if e.msgid]
    translated = [e for e in entries if e.msgstr and e.msgstr.strip() != '']
    
    if len(entries) > 0 and 0 < len(translated) < len(entries):
        partial.append(str(po_file.relative_to(po_dir)))

with open('partial_translated_files.txt', 'w', encoding='utf-8') as f:
    for f_name in partial:
        f.write(f"{f_name}\n")

print(f"Found {len(partial)} partially translated files")
for f in partial:
    print(f"  - {f}")
