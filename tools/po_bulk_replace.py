#!/usr/bin/env python3
"""
Bulk replace a string (or regex) inside `msgstr` entries of .po files.

Usage examples:
  # dry-run: show files/lines that would change
  python tools/po_bulk_replace.py --root . --find "誤訳語" --replace "正しい語" --dry-run

  # actually apply with backup
  python tools/po_bulk_replace.py --root locales/ja --find "誤訳語" --replace "正しい語" --backup

The script only modifies `msgstr` content (including multiline msgstr blocks).
Supports literal replace (default) or regex with `--regex`.
"""
import argparse
import os
import re
import shutil
import sys


def find_po_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith('.po'):
                yield os.path.join(dirpath, fn)


def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()


def write_lines(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def extract_msgstr_block(lines, i):
    # lines: list of lines with newline
    # i: index where lines[i] begins with msgstr
    header = lines[i]
    prefix_match = re.match(r'(\s*msgstr\s*)', header)
    prefix = prefix_match.group(1) if prefix_match else 'msgstr '
    parts = []

    # get quoted part on same line (if any)
    qpos = header.find('"')
    if qpos != -1:
        tail = header[qpos:].rstrip('\n')
        if tail.endswith('"') and len(tail) >= 2:
            parts.append(tail[1:-1].replace('\\"', '"'))
    j = i + 1
    while j < len(lines) and lines[j].lstrip().startswith('"'):
        s = lines[j].strip()
        if len(s) >= 2 and s.endswith('"'):
            parts.append(s[1:-1].replace('\\"', '"'))
        j += 1
    return prefix, parts, j


def build_msgstr_block(prefix, text):
    # text: possibly multiline string
    escaped = lambda s: s.replace('"', '\\"')
    if '\n' in text:
        lines = [prefix + '""\n']
        for ln in text.split('\n'):
            lines.append('"' + escaped(ln) + '"\n')
    else:
        lines = [prefix + '"' + escaped(text) + '"\n']
    return lines


def process_file(path, find, replace, use_regex=False, dry_run=False, backup=False):
    lines = read_lines(path)
    i = 0
    changed = False
    out_lines = []
    report = []
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith('msgstr'):
            prefix, parts, j = extract_msgstr_block(lines, i)
            original = ''.join(parts)
            if use_regex:
                new = re.sub(find, replace, original)
            else:
                new = original.replace(find, replace)
            if new != original:
                changed = True
                report.append((i + 1, original, new))
                out_lines.extend(build_msgstr_block(prefix, new))
            else:
                # preserve original block as-is
                out_lines.append(lines[i])
                for k in range(i + 1, j):
                    out_lines.append(lines[k])
            i = j
        else:
            out_lines.append(line)
            i += 1

    if changed:
        if dry_run:
            return True, report
        if backup:
            shutil.copy2(path, path + '.bak')
        write_lines(path, out_lines)
        return True, report
    return False, []


def main():
    p = argparse.ArgumentParser(description='Bulk replace inside msgstr of .po files')
    p.add_argument('--root', '-r', default='.', help='Root directory to search (default: current dir)')
    p.add_argument('--find', required=True, help='String or regex to find')
    p.add_argument('--replace', required=True, help='Replacement string')
    p.add_argument('--regex', action='store_true', help='Treat find as a regular expression')
    p.add_argument('--dry-run', action='store_true', help='Only show what would change')
    p.add_argument('--backup', action='store_true', help='Create .bak copy before modifying')
    p.add_argument('--encoding', default='utf-8', help='File encoding (default utf-8)')
    args = p.parse_args()

    # change working encoding for read/write helper (we use explicit encoding there)

    total_changed = 0
    for po in find_po_files(args.root):
        try:
            changed, report = process_file(po, args.find, args.replace, use_regex=args.regex, dry_run=args.dry_run, backup=args.backup)
        except Exception as e:
            print(f'Error processing {po}: {e}', file=sys.stderr)
            continue
        if changed:
            total_changed += 1
            print(f'File: {po} — changes: {len(report)}')
            for lineno, old, new in report:
                print(f'  at msgstr starting line {lineno}:')
                print('    - ', old.replace('\n', '\\n'))
                print('    + ', new.replace('\n', '\\n'))

    if total_changed == 0:
        print('No changes detected.')


if __name__ == "__main__":
    main()
