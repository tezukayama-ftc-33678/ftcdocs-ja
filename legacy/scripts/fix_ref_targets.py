#!/usr/bin/env python3
"""Ensure :ref: targets in msgstr match msgid targets.
If counts match, overwrite target (inside <...>) with msgid target while keeping display text from msgstr.
"""
import re
from pathlib import Path
import polib
from tqdm import tqdm

REF_PATTERN = re.compile(r"(:ref:`)([^<`]*)<([^>`]+)>(`)")


def extract_refs(text: str):
    return list(REF_PATTERN.finditer(text))


def fix_entry(entry) -> bool:
    msgid_refs = extract_refs(entry.msgid)
    msgstr_refs = extract_refs(entry.msgstr or "")
    if not msgid_refs or len(msgid_refs) != len(msgstr_refs):
        return False
    new_msgstr = entry.msgstr
    # process from end to keep offsets
    for id_match, str_match in zip(reversed(msgid_refs), reversed(msgstr_refs)):
        target = id_match.group(3).strip()
        # rebuild ref with msgstr display, msgid target
        display = str_match.group(2).strip()
        replacement = f":ref:`{display}<{target}>`"
        start, end = str_match.span()
        new_msgstr = new_msgstr[:start] + replacement + new_msgstr[end:]
    if new_msgstr != entry.msgstr:
        entry.msgstr = new_msgstr
        return True
    return False


def process_file(path: Path):
    po = polib.pofile(str(path))
    modified = False
    for entry in po:
        if entry.msgstr and fix_entry(entry):
            modified = True
    if modified:
        po.save()
    return modified


def main():
    root = Path('locales/ja/LC_MESSAGES')
    files = list(root.rglob('*.po'))
    modified = 0
    for f in tqdm(files, desc='Fixing ref targets'):
        if process_file(f):
            modified += 1
    print(f"Modified files: {modified}/{len(files)}")

if __name__ == '__main__':
    main()
