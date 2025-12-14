#!/usr/bin/env python3
"""
Migration script to convert existing Japanese RST translations to .po format.

This script helps migrate from direct RST translation to gettext-based (.po) translation.
It extracts Japanese translations from RST files and prepares them for .po files.

Usage:
    python docs/scripts/migrate_translations_to_po.py [options]

Options:
    --source-dir DIR     Directory with Japanese RST files (default: docs/source)
    --english-repo URL   URL or path to upstream English repository
    --dry-run            Show what would be done without making changes
    --help               Show this help message
"""

import os
import sys
import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple
import subprocess
import tempfile
import shutil

class TranslationMigrator:
    def __init__(self, source_dir: str, english_repo: str = None, dry_run: bool = False):
        self.source_dir = Path(source_dir)
        self.english_repo = english_repo
        self.dry_run = dry_run
        self.translation_map: Dict[str, List[Tuple[str, str]]] = {}
        
    def detect_japanese_content(self, text: str) -> bool:
        """Check if text contains Japanese characters."""
        japanese_pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]')
        return bool(japanese_pattern.search(text))
    
    def extract_translations_from_rst(self, rst_file: Path) -> List[Tuple[str, str, int]]:
        """
        Extract translated content from a Japanese RST file.
        Returns list of (english_guess, japanese_text, line_number).
        """
        translations = []
        
        try:
            with open(rst_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            current_block = []
            block_start_line = 0
            
            for i, line in enumerate(lines, 1):
                # Skip code blocks, directives, and comments
                if line.strip().startswith('.. ') or line.startswith('   '):
                    continue
                    
                if self.detect_japanese_content(line):
                    if not current_block:
                        block_start_line = i
                    current_block.append(line.rstrip())
                else:
                    if current_block:
                        japanese_text = '\n'.join(current_block)
                        translations.append(('', japanese_text, block_start_line))
                        current_block = []
            
            # Don't forget the last block
            if current_block:
                japanese_text = '\n'.join(current_block)
                translations.append(('', japanese_text, block_start_line))
                
        except Exception as e:
            print(f"Error reading {rst_file}: {e}", file=sys.stderr)
            
        return translations
    
    def scan_japanese_files(self) -> Dict[str, int]:
        """
        Scan all RST files and count Japanese content.
        Returns dict of {file_path: japanese_line_count}.
        """
        japanese_files = {}
        
        for rst_file in self.source_dir.rglob('*.rst'):
            translations = self.extract_translations_from_rst(rst_file)
            if translations:
                relative_path = rst_file.relative_to(self.source_dir)
                japanese_files[str(relative_path)] = len(translations)
                
        return japanese_files
    
    def create_backup(self):
        """Create a backup of the current source directory."""
        backup_dir = Path('docs_source_backup')
        
        if backup_dir.exists():
            print(f"⚠️  Backup directory already exists: {backup_dir}")
            response = input("Overwrite? [y/N]: ")
            if response.lower() != 'y':
                print("Backup cancelled.")
                return False
            shutil.rmtree(backup_dir)
        
        print(f"📦 Creating backup: {backup_dir}")
        # Backup only the source directory, not the parent
        shutil.copytree(self.source_dir, backup_dir)
        print(f"✅ Backup created successfully")
        return True
    
    def generate_translation_report(self) -> str:
        """Generate a report of files with Japanese content."""
        japanese_files = self.scan_japanese_files()
        
        if not japanese_files:
            return "No Japanese content found in RST files."
        
        report = ["# Translation Migration Report\n"]
        report.append(f"## Summary\n")
        report.append(f"- Total files with Japanese content: {len(japanese_files)}")
        report.append(f"- Total translation blocks: {sum(japanese_files.values())}\n")
        report.append(f"## Files to migrate\n")
        
        for file_path, count in sorted(japanese_files.items()):
            report.append(f"- {file_path}: {count} blocks")
        
        return '\n'.join(report)
    
    def run_sphinx_gettext(self):
        """Run sphinx-build to generate .pot files."""
        print("\n📝 Generating .pot files from English RST...")
        
        build_dir = Path('docs/build/gettext')
        
        cmd = [
            'sphinx-build',
            '-b', 'gettext',
            'docs/source',
            str(build_dir)
        ]
        
        if self.dry_run:
            print(f"[DRY RUN] Would run: {' '.join(cmd)}")
            return True
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print("✅ .pot files generated successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to generate .pot files: {e}", file=sys.stderr)
            print(e.stderr, file=sys.stderr)
            return False
    
    def run_sphinx_intl_update(self):
        """Run sphinx-intl to create/update .po files."""
        print("\n🌐 Creating Japanese .po files...")
        
        cmd = [
            'sphinx-intl',
            'update',
            '-p', 'docs/build/gettext',
            '-l', 'ja'
        ]
        
        if self.dry_run:
            print(f"[DRY RUN] Would run: {' '.join(cmd)}")
            return True
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print("✅ .po files created successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to create .po files: {e}", file=sys.stderr)
            print(e.stderr, file=sys.stderr)
            return False
    
    def save_translation_mapping(self):
        """Save extracted translations to a reference file."""
        output_file = Path('TRANSLATION_MAPPING.md')
        
        print(f"\n💾 Saving translation mapping to {output_file}...")
        
        japanese_files = self.scan_japanese_files()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Translation Mapping Reference\n\n")
            f.write("This file contains extracted Japanese translations from RST files.\n")
            f.write("Use this as a reference when filling in .po files.\n\n")
            
            for file_path in sorted(japanese_files.keys()):
                rst_file = self.source_dir / file_path
                translations = self.extract_translations_from_rst(rst_file)
                
                f.write(f"\n## {file_path}\n\n")
                
                for i, (_, japanese_text, line_num) in enumerate(translations, 1):
                    f.write(f"### Block {i} (line {line_num})\n\n")
                    f.write("```\n")
                    f.write(japanese_text)
                    f.write("\n```\n\n")
        
        print(f"✅ Translation mapping saved")
    
    def run_migration(self):
        """Execute the full migration process."""
        print("=" * 70)
        print("  FTC Docs Japanese Translation Migration to .po Format")
        print("=" * 70)
        
        # Step 1: Scan and report
        print("\n📊 Step 1: Scanning for Japanese content...")
        report = self.generate_translation_report()
        print(report)
        
        # Save report
        with open('MIGRATION_REPORT.md', 'w', encoding='utf-8') as f:
            f.write(report)
        print("\n✅ Report saved to MIGRATION_REPORT.md")
        
        # Step 2: Skip backup (using git for version control)
        # Note: Backup functionality is available via create_backup() method if needed
        print("\n📦 Step 2: Skipping backup (using git for version control)")
        
        # Step 3: Generate .pot files
        print("\n📝 Step 3: Generating .pot files...")
        if not self.run_sphinx_gettext():
            return False
        
        # Step 4: Create .po files
        print("\n🌐 Step 4: Creating .po files...")
        if not self.run_sphinx_intl_update():
            return False
        
        # Step 5: Save translation mapping for reference
        print("\n💾 Step 5: Saving translation mapping...")
        self.save_translation_mapping()
        
        print("\n" + "=" * 70)
        print("✅ Migration preparation complete!")
        print("=" * 70)
        
        print("\n📋 Next Steps:")
        print("1. Review MIGRATION_REPORT.md to see what was found")
        print("2. Review TRANSLATION_MAPPING.md for extracted translations")
        print("3. Manually transfer translations from TRANSLATION_MAPPING.md to .po files")
        print("4. Use a .po editor (Poedit, VS Code extensions) for easier editing")
        print("5. Build with: make -e SPHINXOPTS=\"-D language='ja'\" html")
        print("6. Restore English RST files from upstream repository")
        print("\n📚 See MIGRATION_TO_PO_GUIDE.md for detailed instructions")
        
        return True

def main():
    parser = argparse.ArgumentParser(
        description='Migrate FTC Docs translations from RST to .po format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        '--source-dir',
        default='docs/source',
        help='Directory with Japanese RST files (default: docs/source)'
    )
    
    parser.add_argument(
        '--english-repo',
        help='URL or path to upstream English repository'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    
    args = parser.parse_args()
    
    migrator = TranslationMigrator(
        source_dir=args.source_dir,
        english_repo=args.english_repo,
        dry_run=args.dry_run
    )
    
    try:
        success = migrator.run_migration()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
