#!/usr/bin/env python3
from pathlib import Path
import polib

po_dir = Path('locales/ja/LC_MESSAGES')
po_files = sorted(list(po_dir.glob('**/*.po')))

untranslated = []
for po_file in po_files:
    try:
        po = polib.pofile(str(po_file))
    except:
        continue
    
    entries = [e for e in po if e.msgid]
    translated = [e for e in entries if e.msgstr and e.msgstr.strip() != '']
    
    if len(entries) > 0 and len(translated) == 0:
        untranslated.append(str(po_file.relative_to(po_dir)))

with open('untranslated_files.txt', 'w', encoding='utf-8') as f:
    for f_name in untranslated:
        f.write(f"{f_name}\n")

print(f"Found {len(untranslated)} untranslated files")
for f in untranslated[:10]:
    print(f"  - {f}")
if len(untranslated) > 10:
    print(f"  ... and {len(untranslated) - 10} more")
