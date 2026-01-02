#!/usr/bin/env python3
from pathlib import Path
import polib

po_dir = Path('locales/ja/LC_MESSAGES')
po_files = sorted(list(po_dir.glob('**/*.po')))

print(f'Total PO files: {len(po_files)}')
print()

fully_translated = []
partially_translated = []
untranslated = []

for po_file in po_files:
    try:
        po = polib.pofile(str(po_file))
    except Exception as e:
        print(f"Error reading {po_file}: {e}")
        continue
    
    entries = [e for e in po if e.msgid]
    translated = [e for e in entries if e.msgstr and e.msgstr.strip() != '']
    
    if len(entries) == 0:
        continue
    
    percentage = (len(translated) * 100) // len(entries) if entries else 0
    
    if len(translated) == len(entries):
        fully_translated.append((po_file.relative_to(po_dir), 100))
    elif len(translated) == 0:
        untranslated.append((po_file.relative_to(po_dir), 0))
    else:
        partially_translated.append((po_file.relative_to(po_dir), percentage))

print(f'✓ Fully translated: {len(fully_translated)}')
print(f'◐ Partially translated: {len(partially_translated)}')
print(f'✗ Untranslated: {len(untranslated)}')
print()

total_entries = sum(len([e for e in polib.pofile(str(f)) if e.msgid]) for f in po_files if po_dir in f.parents or po_dir == f.parent)
total_translated = sum(len([e for e in polib.pofile(str(f)) if e.msgid and e.msgstr and e.msgstr.strip()]) for f in po_files if po_dir in f.parents or po_dir == f.parent)

print(f'Total entries: {total_translated}/{total_entries}')
print()

if untranslated:
    print(f'Untranslated files ({len(untranslated)}):')
    for f, _ in untranslated[:10]:
        print(f'  - {f}')
    if len(untranslated) > 10:
        print(f'  ... and {len(untranslated) - 10} more')

if partially_translated:
    print()
    print(f'Partially translated files ({len(partially_translated)}):')
    for f, pct in partially_translated[:10]:
        print(f'  - {f}: {pct}%')
    if len(partially_translated) > 10:
        print(f'  ... and {len(partially_translated) - 10} more')
