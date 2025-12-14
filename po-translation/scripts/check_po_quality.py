#!/usr/bin/env python3
"""
Quality Checker for .po files

This script checks the quality of translations in .po files.
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Technical terms that should be in bold English
TECHNICAL_TERMS = [
    'OpMode', 'LinearOpMode', 'TeleOp', 'Autonomous',
    'Control Hub', 'Expansion Hub', 'Driver Station', 'Robot Controller',
    'Driver Hub', 'HuskyLens', 'AprilTag', 'VisionPortal',
    'Blocks', 'OnBot Java', 'Android Studio',
    'Telemetry', 'HardwareMap', 'DcMotor', 'Servo',
    'IMU', 'OpenCV', 'EasyOpenCV',
]


class QualityIssue:
    """Represents a quality issue in a translation"""
    
    def __init__(self, issue_type: str, line_num: int, msgid: str, msgstr: str, description: str):
        self.issue_type = issue_type
        self.line_num = line_num
        self.msgid = msgid
        self.msgstr = msgstr
        self.description = description


class POQualityChecker:
    """Quality checker for .po files"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.issues = []
        self.stats = {
            'total_entries': 0,
            'translated': 0,
            'untranslated': 0,
            'fuzzy': 0,
        }
    
    def check(self):
        """Run all quality checks"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        current_msgid = None
        current_msgstr = None
        current_line_num = 0
        is_fuzzy = False
        in_header = True
        
        for i, line in enumerate(lines, 1):
            line = line.rstrip('\n')
            
            # Skip header
            if in_header:
                if line.startswith('msgstr'):
                    in_header = False
                continue
            
            # Check for fuzzy
            if ', fuzzy' in line:
                is_fuzzy = True
            
            # msgid
            if line.startswith('msgid '):
                if current_msgid is not None:
                    self._check_entry(current_line_num, current_msgid, current_msgstr, is_fuzzy)
                
                current_line_num = i
                # Extract msgid (handle multi-line by taking first line only)
                if line.strip().endswith('"'):
                    current_msgid = line[7:-1]
                else:
                    current_msgid = line[7:]
                current_msgstr = None
                is_fuzzy = False
            
            # msgstr
            elif line.startswith('msgstr '):
                # Extract msgstr (handle multi-line by taking first line only)
                if line.strip().endswith('"'):
                    current_msgstr = line[8:-1]
                else:
                    current_msgstr = line[8:]
            
            # Empty line - end of entry
            elif not line.strip():
                if current_msgid is not None:
                    self._check_entry(current_line_num, current_msgid, current_msgstr, is_fuzzy)
                    current_msgid = None
                    current_msgstr = None
        
        # Don't forget last entry
        if current_msgid is not None:
            self._check_entry(current_line_num, current_msgid, current_msgstr, is_fuzzy)
    
    def _check_entry(self, line_num: int, msgid: str, msgstr: str, is_fuzzy: bool):
        """Check a single entry"""
        self.stats['total_entries'] += 1
        
        # Skip empty msgid (header)
        if not msgid:
            return
        
        # Check translation status
        if not msgstr:
            self.stats['untranslated'] += 1
            self.issues.append(QualityIssue(
                'untranslated', line_num, msgid, msgstr,
                'Entry is not translated'
            ))
            return
        
        if is_fuzzy:
            self.stats['fuzzy'] += 1
            self.issues.append(QualityIssue(
                'fuzzy', line_num, msgid, msgstr,
                'Entry has fuzzy flag (needs review)'
            ))
        
        self.stats['translated'] += 1
        
        # Check for technical terms
        self._check_technical_terms(line_num, msgid, msgstr)
        
        # Check for code preservation
        self._check_code_preservation(line_num, msgid, msgstr)
        
        # Check for RST markup
        self._check_rst_markup(line_num, msgid, msgstr)
    
    def _check_technical_terms(self, line_num: int, msgid: str, msgstr: str):
        """Check if technical terms are properly formatted"""
        for term in TECHNICAL_TERMS:
            # Check if term appears in msgid
            if term in msgid:
                # Check if it appears in msgstr without bold
                if term in msgstr and f'**{term}**' not in msgstr:
                    self.issues.append(QualityIssue(
                        'technical_term', line_num, msgid, msgstr,
                        f'Technical term "{term}" should be in bold: **{term}**'
                    ))
    
    def _check_code_preservation(self, line_num: int, msgid: str, msgstr: str):
        """Check if code blocks are preserved"""
        # Find all code in backticks
        code_pattern = r'``([^`]+)``'
        
        msgid_codes = set(re.findall(code_pattern, msgid))
        msgstr_codes = set(re.findall(code_pattern, msgstr))
        
        # Check if all codes are preserved
        missing_codes = msgid_codes - msgstr_codes
        if missing_codes:
            self.issues.append(QualityIssue(
                'code_missing', line_num, msgid, msgstr,
                f'Code blocks missing in translation: {", ".join(missing_codes)}'
            ))
    
    def _check_rst_markup(self, line_num: int, msgid: str, msgstr: str):
        """Check if RST markup is preserved"""
        # Common RST directives
        rst_patterns = [
            r':doc:`[^`]+`',
            r':ref:`[^`]+`',
            r':class:`[^`]+`',
            r':meth:`[^`]+`',
        ]
        
        for pattern in rst_patterns:
            msgid_matches = re.findall(pattern, msgid)
            msgstr_matches = re.findall(pattern, msgstr)
            
            if len(msgid_matches) != len(msgstr_matches):
                self.issues.append(QualityIssue(
                    'rst_markup', line_num, msgid, msgstr,
                    f'RST markup count mismatch: {pattern}'
                ))
    
    def get_report(self) -> str:
        """Generate a quality report"""
        report = []
        report.append(f"# Quality Report: {os.path.basename(self.filepath)}\n")
        
        # Statistics
        report.append("## Statistics\n")
        report.append(f"- Total entries: {self.stats['total_entries']}")
        report.append(f"- Translated: {self.stats['translated']}")
        report.append(f"- Untranslated: {self.stats['untranslated']}")
        report.append(f"- Fuzzy (needs review): {self.stats['fuzzy']}")
        
        if self.stats['total_entries'] > 0:
            completion = (self.stats['translated'] / self.stats['total_entries']) * 100
            report.append(f"- Completion: {completion:.1f}%\n")
        
        # Issues by type
        if self.issues:
            report.append("## Issues\n")
            
            issues_by_type = {}
            for issue in self.issues:
                if issue.issue_type not in issues_by_type:
                    issues_by_type[issue.issue_type] = []
                issues_by_type[issue.issue_type].append(issue)
            
            for issue_type, issues in sorted(issues_by_type.items()):
                report.append(f"\n### {issue_type.replace('_', ' ').title()} ({len(issues)})\n")
                
                for issue in issues[:10]:  # Show first 10
                    report.append(f"**Line {issue.line_num}:**")
                    report.append(f"- Issue: {issue.description}")
                    report.append(f"- msgid: `{issue.msgid[:80]}`")
                    report.append(f"- msgstr: `{issue.msgstr[:80]}`")
                    report.append("")
                
                if len(issues) > 10:
                    report.append(f"... and {len(issues) - 10} more issues of this type\n")
        else:
            report.append("## No Issues Found!\n")
            report.append("✅ All quality checks passed.\n")
        
        return '\n'.join(report)


def check_directory(directory: str, report_file: str = None):
    """Check all .po files in a directory"""
    po_files = list(Path(directory).glob('**/*.po'))
    
    if not po_files:
        print(f"No .po files found in {directory}")
        return
    
    print(f"Found {len(po_files)} .po files\n")
    
    all_stats = {
        'total_entries': 0,
        'translated': 0,
        'untranslated': 0,
        'fuzzy': 0,
    }
    all_issues = []
    
    for po_file in po_files:
        print(f"Checking {po_file}...")
        checker = POQualityChecker(str(po_file))
        checker.check()
        
        # Accumulate stats
        for key in all_stats:
            all_stats[key] += checker.stats[key]
        
        all_issues.extend([(str(po_file), issue) for issue in checker.issues])
        
        # Print file stats
        if checker.stats['total_entries'] > 0:
            completion = (checker.stats['translated'] / checker.stats['total_entries']) * 100
            print(f"  {completion:.1f}% complete, {len(checker.issues)} issues")
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total entries: {all_stats['total_entries']}")
    print(f"Translated: {all_stats['translated']}")
    print(f"Untranslated: {all_stats['untranslated']}")
    print(f"Fuzzy: {all_stats['fuzzy']}")
    
    if all_stats['total_entries'] > 0:
        completion = (all_stats['translated'] / all_stats['total_entries']) * 100
        print(f"Overall completion: {completion:.1f}%")
    
    print(f"Total issues: {len(all_issues)}")
    
    # Generate report
    if report_file:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("# Translation Quality Report\n\n")
            f.write(f"## Overall Statistics\n\n")
            f.write(f"- Total entries: {all_stats['total_entries']}\n")
            f.write(f"- Translated: {all_stats['translated']}\n")
            f.write(f"- Untranslated: {all_stats['untranslated']}\n")
            f.write(f"- Fuzzy: {all_stats['fuzzy']}\n")
            
            if all_stats['total_entries'] > 0:
                completion = (all_stats['translated'] / all_stats['total_entries']) * 100
                f.write(f"- Overall completion: {completion:.1f}%\n\n")
            
            f.write(f"## Issues by File\n\n")
            
            current_file = None
            for filepath, issue in all_issues[:100]:  # First 100 issues
                if filepath != current_file:
                    f.write(f"\n### {os.path.basename(filepath)}\n\n")
                    current_file = filepath
                
                f.write(f"**Line {issue.line_num}:** {issue.description}\n")
            
            if len(all_issues) > 100:
                f.write(f"\n... and {len(all_issues) - 100} more issues\n")
        
        print(f"\nDetailed report saved to: {report_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Quality checker for .po translation files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check a single file
  python check_po_quality.py docs/locale/ja/LC_MESSAGES/index.po
  
  # Check all files in a directory
  python check_po_quality.py docs/locale/ja/LC_MESSAGES/
  
  # Generate a report
  python check_po_quality.py docs/locale/ja/LC_MESSAGES/ --report quality_report.md
        """
    )
    
    parser.add_argument('path', help='Path to .po file or directory')
    parser.add_argument('--report', help='Output report file (markdown)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.path):
        print(f"Error: Path not found: {args.path}")
        sys.exit(1)
    
    if os.path.isfile(args.path):
        # Check single file
        checker = POQualityChecker(args.path)
        checker.check()
        report = checker.get_report()
        
        if args.report:
            with open(args.report, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Report saved to: {args.report}")
        else:
            print(report)
    
    elif os.path.isdir(args.path):
        # Check directory
        check_directory(args.path, args.report)
    
    else:
        print(f"Error: Invalid path: {args.path}")
        sys.exit(1)


if __name__ == '__main__':
    main()
