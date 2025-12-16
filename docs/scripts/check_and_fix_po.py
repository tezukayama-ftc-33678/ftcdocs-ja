#!/usr/bin/env python3
"""
Sphinx i18n Japanese PO file validator and auto-fixer.

This script:
1. Analyzes Sphinx build warnings (from stderr or log file)
2. Identifies issues in PO files (missing doc references, emphasis mismatches)
3. Suggests and optionally applies fixes to locales/ja/LC_MESSAGES/*.po
"""

import os
import re
import sys
import json
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import tempfile

@dataclass
class POEntry:
    """Represents a single msgid/msgstr pair in a PO file."""
    msgid: str
    msgstr: str
    line_num: int
    context: List[str]  # lines before/after for reference

@dataclass
class Issue:
    """Represents an identified problem."""
    issue_type: str  # 'missing_doc_ref', 'emphasis_mismatch', 'inconsistent_ref'
    po_file: str
    msgid: str
    msgstr: str
    line_num: int
    suggestion: str
    severity: str  # 'error', 'warning', 'info'

class POParser:
    """Parse and extract entries from PO files."""
    
    def __init__(self, po_file_path: str):
        self.po_file_path = po_file_path
        self.entries: List[POEntry] = []
        self.parse()
    
    def parse(self):
        """Parse PO file and extract msgid/msgstr pairs."""
        with open(self.po_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip comments, blank lines, header
            if not line or line.startswith('#'):
                i += 1
                continue
            
            # Detect msgid
            if line.startswith('msgid'):
                msgid = self._extract_string(line) or ""
                msgid_line = i
                
                # Collect continuation lines
                i += 1
                while i < len(lines) and lines[i].strip().startswith('"'):
                    msgid += (self._extract_string(lines[i].strip()) or "")
                    i += 1
                
                # Expect msgstr
                if i < len(lines) and lines[i].strip().startswith('msgstr'):
                    msgstr = self._extract_string(lines[i].strip()) or ""
                    i += 1
                    
                    # Collect continuation lines
                    while i < len(lines) and lines[i].strip().startswith('"'):
                        msgstr += (self._extract_string(lines[i].strip()) or "")
                        i += 1
                    
                    # Skip empty msgid (header)
                    if msgid:
                        self.entries.append(POEntry(
                            msgid=msgid,
                            msgstr=msgstr,
                            line_num=msgid_line,
                            context=[]
                        ))
                else:
                    i += 1
            else:
                i += 1
    
    @staticmethod
    def _extract_string(line: str) -> str:
        """Extract string content from msgid/msgstr line."""
        match = re.match(r'msgid\s+"(.*)"|msgstr\s+"(.*)"', line)
        if match:
            return match.group(1) or match.group(2) or ""
        
        # Handle continuation lines (just quoted strings)
        match = re.match(r'^"(.*)"$', line)
        if match:
            return match.group(1) or ""
        
        return ""

class POValidator:
    """Validate PO entries against msgid/msgstr consistency rules."""
    
    def __init__(self, po_file: str, english_po_file: Optional[str] = None):
        self.po_file = po_file
        self.parser = POParser(po_file)
        self.english_parser = None
        if english_po_file and os.path.exists(english_po_file):
            self.english_parser = POParser(english_po_file)
        self.issues: List[Issue] = []
    
    def check_all(self) -> List[Issue]:
        """Run all checks against PO entries."""
        self.issues = []
        
        for entry in self.parser.entries:
            self._check_emphasis(entry)
            self._check_doc_references(entry)
            self._check_link_consistency(entry)
        
        return self.issues
    
    def _check_emphasis(self, entry: POEntry):
        """Check for balanced emphasis markers (**...** and __...__) in msgstr."""
        # Count ** pairs
        msgid_strong = entry.msgid.count('**')
        msgstr_strong = entry.msgstr.count('**')
        
        if msgid_strong > 0 and msgstr_strong != msgid_strong:
            suggestion = (
                f"Emphasis count mismatch: msgid has {msgid_strong} ** markers, "
                f"msgstr has {msgstr_strong}. Ensure balanced **...**."
            )
            self.issues.append(Issue(
                issue_type='emphasis_mismatch',
                po_file=self.po_file,
                msgid=entry.msgid[:100],
                msgstr=entry.msgstr[:100],
                line_num=entry.line_num,
                suggestion=suggestion,
                severity='warning'
            ))
    
    def _check_doc_references(self, entry: POEntry):
        """Check if :doc: references are preserved in msgstr when present in msgid."""
        msgid_docs = re.findall(r':doc:`[^`]*`', entry.msgid)
        msgstr_docs = re.findall(r':doc:`[^`]*`', entry.msgstr)
        
        if len(msgid_docs) > len(msgstr_docs):
            missing = set(msgid_docs) - set(msgstr_docs)
            suggestion = (
                f"Missing :doc: references in msgstr. "
                f"msgid has {msgid_docs}, msgstr missing: {missing}"
            )
            self.issues.append(Issue(
                issue_type='missing_doc_ref',
                po_file=self.po_file,
                msgid=entry.msgid[:100],
                msgstr=entry.msgstr[:100],
                line_num=entry.line_num,
                suggestion=suggestion,
                severity='error'
            ))
    
    def _check_link_consistency(self, entry: POEntry):
        """Check for other link patterns (http://, https://, etc.)."""
        msgid_links = len(re.findall(r'https?://', entry.msgid))
        msgstr_links = len(re.findall(r'https?://', entry.msgstr))
        
        if msgid_links > msgstr_links:
            suggestion = (
                f"Potential missing external links. "
                f"msgid has {msgid_links} URLs, msgstr has {msgstr_links}."
            )
            self.issues.append(Issue(
                issue_type='inconsistent_ref',
                po_file=self.po_file,
                msgid=entry.msgid[:100],
                msgstr=entry.msgstr[:100],
                line_num=entry.line_num,
                suggestion=suggestion,
                severity='warning'
            ))

class SphinxLogAnalyzer:
    """Analyze Sphinx build stderr/log for warnings."""
    
    WARNING_PATTERN = re.compile(
        r'(?P<file>[^:]+):(?P<line>\d+):\s*(?P<level>WARNING|ERROR):\s*(?P<msg>.*)'
    )
    
    @staticmethod
    def parse_sphinx_output(output: str) -> List[Dict]:
        """Parse Sphinx build output and extract warnings."""
        warnings = []
        for line in output.split('\n'):
            match = SphinxLogAnalyzer.WARNING_PATTERN.search(line)
            if match:
                warnings.append({
                    'file': match.group('file'),
                    'line': int(match.group('line')),
                    'level': match.group('level'),
                    'message': match.group('msg'),
                    'raw': line
                })
        return warnings
    
    @staticmethod
    def filter_po_related(warnings: List[Dict]) -> List[Dict]:
        """Filter warnings related to PO/translation issues."""
        po_warnings = []
        keywords = ['inconsistent', 'term reference', 'strong', 'emphasis', 'inline', 'start-string']
        
        for w in warnings:
            msg = w['message'].lower()
            if any(kw in msg for kw in keywords):
                po_warnings.append(w)
        
        return po_warnings

class POFixer:
    """Apply suggested fixes to PO files."""
    
    @staticmethod
    def fix_emphasis(po_file: str, issues: List[Issue]) -> Tuple[int, List[str]]:
        """Auto-fix emphasis mismatches."""
        fixed = 0
        fixes = []
        
        for issue in issues:
            if issue.issue_type == 'emphasis_mismatch':
                # Simple heuristic: add ** pair if msgid has it but msgstr doesn't
                if issue.msgid.count('**') > issue.msgstr.count('**'):
                    msgid_match = re.search(r'\*\*([^*]*)\*\*', issue.msgid)
                    if msgid_match:
                        text = msgid_match.group(1)
                        new_msgstr = issue.msgstr.replace(text, f'**{text}**', 1)
                        fixes.append(f"Line {issue.line_num}: Add ** around '{text}'")
                        fixed += 1
        
        return fixed, fixes
    
    @staticmethod
    def restore_doc_references(po_file: str, issues: List[Issue]) -> Tuple[int, List[str]]:
        """Auto-restore :doc: references from msgid to msgstr."""
        fixed = 0
        fixes = []
        
        for issue in issues:
            if issue.issue_type == 'missing_doc_ref':
                # Extract missing :doc: from msgid and suggest adding to msgstr
                msgid_docs = re.findall(r':doc:`[^`]*`', issue.msgid)
                msgstr_docs = re.findall(r':doc:`[^`]*`', issue.msgstr)
                
                missing = [d for d in msgid_docs if d not in msgstr_docs]
                if missing:
                    for doc_ref in missing:
                        # Simple insertion at end of msgstr (before punctuation)
                        suggestion = f"Add '{doc_ref}' to msgstr at line {issue.line_num}"
                        fixes.append(suggestion)
                        fixed += 1
        
        return fixed, fixes

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Sphinx i18n PO file validator and auto-fixer for Japanese translation'
    )
    parser.add_argument(
        '--po-dir',
        default='./locales/ja/LC_MESSAGES',
        help='Directory containing PO files (default: locales/ja/LC_MESSAGES)'
    )
    parser.add_argument(
        '--english-dir',
        default='./build/gettext',
        help='Directory containing English POT files (default: build/gettext)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Output file for issues (JSON or text)'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Apply automatic fixes to PO files'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    po_dir = Path(args.po_dir)
    if not po_dir.exists():
        print(f"Error: PO directory not found: {po_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Collect all PO files
    po_files = list(po_dir.rglob('*.po'))
    if not po_files:
        print(f"No PO files found in {po_dir}", file=sys.stderr)
        sys.exit(1)
    
    all_issues: List[Issue] = []
    
    print(f"🔍 Scanning {len(po_files)} PO files...")
    
    for po_file in sorted(po_files):
        validator = POValidator(str(po_file))
        issues = validator.check_all()
        all_issues.extend(issues)
        
        if args.verbose and issues:
            print(f"  {po_file.name}: {len(issues)} issues found")
    
    # Summarize
    print(f"\n📊 Total issues found: {len(all_issues)}")
    
    by_type = {}
    for issue in all_issues:
        by_type.setdefault(issue.issue_type, []).append(issue)
    
    for issue_type, issues in sorted(by_type.items()):
        print(f"  {issue_type}: {len(issues)}")
    
    # Output results
    if args.output:
        if args.output.endswith('.json'):
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(
                    [
                        {
                            'type': i.issue_type,
                            'file': i.po_file,
                            'line': i.line_num,
                            'severity': i.severity,
                            'suggestion': i.suggestion
                        }
                        for i in all_issues
                    ],
                    f,
                    indent=2,
                    ensure_ascii=False
                )
        else:
            with open(args.output, 'w', encoding='utf-8') as f:
                for issue in all_issues:
                    f.write(
                        f"{issue.po_file}:{issue.line_num} [{issue.severity}] {issue.issue_type}\n"
                        f"  {issue.suggestion}\n\n"
                    )
        print(f"✅ Results written to {args.output}")
    
    # Display issues
    if args.verbose or not args.output:
        print("\n📋 Issues:")
        for issue in all_issues[:10]:  # Show first 10
            print(f"  {issue.po_file}:{issue.line_num} [{issue.severity}]")
            print(f"    {issue.suggestion}")
        if len(all_issues) > 10:
            print(f"  ... and {len(all_issues) - 10} more (use --output to see all)")
    
    # Apply fixes if requested
    if args.fix:
        print("\n🔧 Applying fixes...")
        # This would require more sophisticated PO file rewriting
        # For now, just report what would be fixed
        fixed_count = 0
        for issue in all_issues:
            if issue.issue_type == 'emphasis_mismatch':
                fixed_count += 1
        print(f"  Would fix {fixed_count} emphasis mismatches (implementation pending)")

if __name__ == '__main__':
    main()
