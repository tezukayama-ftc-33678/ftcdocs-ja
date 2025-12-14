#!/usr/bin/env python3
"""
AI Translation Helper for .po files

This script helps translate .po files using various AI translation APIs.
Supports: DeepL, OpenAI, Anthropic, and local LLMs via Ollama.
"""

import argparse
import os
import sys
import re
from pathlib import Path
from typing import List, Tuple, Optional

# Technical terms that should remain in English (bold)
TECHNICAL_TERMS = [
    'OpMode', 'LinearOpMode', 'TeleOp', 'Autonomous',
    'Control Hub', 'Expansion Hub', 'Driver Station', 'Robot Controller',
    'Driver Hub', 'HuskyLens', 'AprilTag', 'VisionPortal',
    'Blocks', 'OnBot Java', 'Android Studio',
    'Telemetry', 'HardwareMap', 'DcMotor', 'Servo',
    'IMU', 'OpenCV', 'EasyOpenCV',
    'FIRST', 'Gracious Professionalism',
]

# Base prompt for AI translation
BASE_PROMPT = """あなたはFIRST Tech Challenge（FTC）ドキュメントの日本語翻訳者です。

【翻訳ルール】
1. 文体: 「です・ます」調で統一
2. 句読点: 全角の「、」と「。」を使用
3. 長音: カタカナ語の長音（ー）は省略しない（例: コンピューター、パラメーター）
4. 技術用語: 以下の用語は**太字の英語**で残す
   - OpMode, LinearOpMode, TeleOp, Autonomous
   - Control Hub, Driver Station, Robot Controller
   - その他のAPI名、クラス名、製品名
5. コード: バッククォート内の``コード``は翻訳しない
6. RSTマークアップ: :doc:、:ref:などのディレクティブは保持
7. 固有名詞: FIRST、Gracious Professionalismは翻訳しない

以下の英語テキストを日本語に翻訳してください。
技術用語は必ず **太字** で英語のまま残してください。
"""


class POEntry:
    """Represents a single entry in a .po file"""
    
    def __init__(self, msgid: str, msgstr: str, comments: List[str], fuzzy: bool = False):
        self.msgid = msgid
        self.msgstr = msgstr
        self.comments = comments
        self.fuzzy = fuzzy
    
    def needs_translation(self) -> bool:
        """Check if this entry needs translation"""
        return not self.msgstr or self.fuzzy


class POFile:
    """Parser and writer for .po files"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.header = []
        self.entries = []
        self._parse()
    
    def _parse(self):
        """Parse the .po file"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        current_comments = []
        current_msgid = None
        current_msgstr = None
        is_fuzzy = False
        in_header = True
        
        for line in lines:
            line = line.rstrip('\n')
            
            # Header section
            if in_header and line.startswith('msgstr'):
                in_header = False
                continue
            
            if in_header:
                self.header.append(line)
                continue
            
            # Comments
            if line.startswith('#'):
                if ', fuzzy' in line:
                    is_fuzzy = True
                current_comments.append(line)
            
            # msgid
            elif line.startswith('msgid '):
                if current_msgid is not None:
                    # Save previous entry
                    entry = POEntry(current_msgid, current_msgstr or '', current_comments, is_fuzzy)
                    self.entries.append(entry)
                    current_comments = []
                    is_fuzzy = False
                
                current_msgid = line[7:-1]  # Remove 'msgid "' and '"'
                current_msgstr = None
            
            # msgstr
            elif line.startswith('msgstr '):
                current_msgstr = line[8:-1]  # Remove 'msgstr "' and '"'
            
            # Empty line
            elif not line.strip():
                if current_msgid is not None:
                    entry = POEntry(current_msgid, current_msgstr or '', current_comments, is_fuzzy)
                    self.entries.append(entry)
                    current_msgid = None
                    current_msgstr = None
                    current_comments = []
                    is_fuzzy = False
        
        # Don't forget the last entry
        if current_msgid is not None:
            entry = POEntry(current_msgid, current_msgstr or '', current_comments, is_fuzzy)
            self.entries.append(entry)
    
    def get_untranslated_entries(self) -> List[Tuple[int, POEntry]]:
        """Get all entries that need translation"""
        return [(i, entry) for i, entry in enumerate(self.entries) if entry.needs_translation()]
    
    def save(self, filepath: Optional[str] = None):
        """Save the .po file"""
        if filepath is None:
            filepath = self.filepath
        
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write header
            for line in self.header:
                f.write(line + '\n')
            f.write('\n')
            
            # Write entries
            for entry in self.entries:
                # Write comments (excluding fuzzy if translated)
                for comment in entry.comments:
                    if not (', fuzzy' in comment and entry.msgstr):
                        f.write(comment + '\n')
                
                # Write msgid and msgstr
                f.write(f'msgid "{entry.msgid}"\n')
                f.write(f'msgstr "{entry.msgstr}"\n')
                f.write('\n')


def translate_with_api(text: str, api: str, api_key: str, model: str = None) -> str:
    """
    Translate text using the specified API
    
    Note: This is a stub implementation. 
    Users should implement actual API calls based on their needs.
    """
    print(f"[INFO] Translating with {api} API...")
    print(f"[INFO] To use this feature, please implement the API call for {api}")
    print(f"[INFO] Text to translate: {text[:100]}...")
    
    # Placeholder - users should implement actual API calls
    if api == 'deepl':
        print("[TODO] Implement DeepL API call")
        print("       Visit: https://www.deepl.com/pro-api")
    elif api == 'openai':
        print("[TODO] Implement OpenAI API call")
        print("       Visit: https://platform.openai.com/docs/api-reference")
    elif api == 'anthropic':
        print("[TODO] Implement Anthropic API call")
        print("       Visit: https://docs.anthropic.com/")
    elif api == 'ollama':
        print("[TODO] Implement Ollama API call")
        print("       Visit: https://ollama.ai/")
    
    return ""


def main():
    parser = argparse.ArgumentParser(
        description='AI Translation Helper for .po files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Translate a single file (dry-run)
  python ai_translate_po.py docs/locale/ja/LC_MESSAGES/index.po --dry-run
  
  # Translate with DeepL API
  python ai_translate_po.py index.po --api deepl --api-key YOUR_KEY
  
  # Translate only fuzzy entries
  python ai_translate_po.py index.po --fuzzy-only --api openai --api-key YOUR_KEY

Note: This script provides a framework for AI translation.
      You need to implement the actual API calls based on your chosen service.
        """
    )
    
    parser.add_argument('pofile', help='Path to .po file to translate')
    parser.add_argument('--api', choices=['deepl', 'openai', 'anthropic', 'ollama'],
                       help='AI translation API to use')
    parser.add_argument('--api-key', help='API key for the translation service')
    parser.add_argument('--model', help='Model to use (for OpenAI, Anthropic, Ollama)')
    parser.add_argument('--fuzzy-only', action='store_true',
                       help='Only translate fuzzy entries')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be translated without making changes')
    parser.add_argument('--output', help='Output file (default: overwrite input)')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.pofile):
        print(f"Error: File not found: {args.pofile}")
        sys.exit(1)
    
    # Parse .po file
    print(f"Parsing {args.pofile}...")
    po = POFile(args.pofile)
    
    # Get entries that need translation
    untranslated = po.get_untranslated_entries()
    
    if not untranslated:
        print("No entries need translation. All done!")
        return
    
    print(f"Found {len(untranslated)} entries that need translation")
    
    if args.dry_run:
        print("\n=== DRY RUN MODE ===")
        print("The following entries would be translated:\n")
        for i, (idx, entry) in enumerate(untranslated[:5]):  # Show first 5
            print(f"{i+1}. msgid: {entry.msgid[:80]}...")
            print(f"   msgstr: {'(empty)' if not entry.msgstr else entry.msgstr[:80]}")
            print(f"   fuzzy: {entry.fuzzy}")
            print()
        
        if len(untranslated) > 5:
            print(f"... and {len(untranslated) - 5} more entries")
        
        print("\nTo perform actual translation, remove --dry-run and specify --api")
        return
    
    if not args.api:
        print("Error: --api is required for translation (use --dry-run to preview)")
        print("Supported APIs: deepl, openai, anthropic, ollama")
        sys.exit(1)
    
    if args.api in ['deepl', 'openai', 'anthropic'] and not args.api_key:
        print(f"Error: --api-key is required for {args.api}")
        sys.exit(1)
    
    # Translate entries
    print(f"\nTranslating {len(untranslated)} entries...")
    for i, (idx, entry) in enumerate(untranslated):
        print(f"[{i+1}/{len(untranslated)}] Translating: {entry.msgid[:60]}...")
        
        # Translate
        translation = translate_with_api(
            entry.msgid,
            args.api,
            args.api_key,
            args.model
        )
        
        if translation:
            entry.msgstr = translation
            entry.fuzzy = False
    
    # Save result
    output_file = args.output or args.pofile
    print(f"\nSaving to {output_file}...")
    po.save(output_file)
    
    print("Done!")
    print(f"\nNext steps:")
    print(f"1. Review the translations: vim {output_file}")
    print(f"2. Build and test: cd docs && make ja-build")
    print(f"3. Preview: python -m http.server 8000 --directory docs/build/html/ja")


if __name__ == '__main__':
    main()
