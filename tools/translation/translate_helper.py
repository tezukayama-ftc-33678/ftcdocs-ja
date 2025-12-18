#!/usr/bin/env python3
"""
Translation helper script for batch processing PO files.
Follows COPILOT_TRANSLATION_PROMPT.md and GLOSSARY.md guidelines.
"""

import re
import sys
from pathlib import Path

class POTranslator:
    """Helper class to translate PO file entries."""
    
    def __init__(self, po_file_path):
        self.po_file_path = Path(po_file_path)
        self.content = ""
        self.entries = []
        
    def load(self):
        """Load PO file content."""
        with open(self.po_file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
        return self
    
    def parse_entries(self):
        """Parse msgid/msgstr pairs from PO file."""
        # Match msgid/msgstr pairs including multiline entries
        pattern = r'(#:.*?\n)(msgid\s+"(?:[^"\\]|\\.)*"(?:\n"(?:[^"\\]|\\.)*")*)\n(msgstr\s+"(?:[^"\\]|\\.)*"(?:\n"(?:[^"\\]|\\.)*")*)'
        matches = re.finditer(pattern, self.content, re.MULTILINE | re.DOTALL)
        
        self.entries = []
        for match in matches:
            location = match.group(1).strip()
            msgid = match.group(2).strip()
            msgstr = match.group(3).strip()
            
            # Extract actual text from msgid
            msgid_text_match = re.search(r'msgid\s+"(.*?)"', msgid, re.DOTALL)
            msgstr_text_match = re.search(r'msgstr\s+"(.*?)"', msgstr, re.DOTALL)
            
            if msgid_text_match:
                msgid_text = msgid_text_match.group(1)
                msgstr_text = msgstr_text_match.group(1) if msgstr_text_match else ""
                
                if msgid_text and not msgstr_text:  # Untranslated
                    self.entries.append({
                        'location': location,
                        'msgid_full': msgid,
                        'msgstr_full': msgstr,
                        'msgid_text': msgid_text,
                        'msgstr_text': msgstr_text,
                        'full_match': match.group(0)
                    })
        
        return self
    
    def list_untranslated(self, limit=20):
        """List untranslated entries."""
        print(f"\n{'='*70}")
        print(f"Untranslated entries in {self.po_file_path.name}")
        print(f"{'='*70}\n")
        
        for i, entry in enumerate(self.entries[:limit]):
            print(f"{i+1}. {entry['location']}")
            print(f"   EN: {entry['msgid_text'][:80]}...")
            print()
        
        total = len(self.entries)
        if total > limit:
            print(f"... and {total - limit} more untranslated entries")
        
        print(f"\nTotal untranslated: {total}")
        return self
    
    def apply_translations(self, translations_dict):
        """Apply translations from a dictionary of {msgid_text: japanese_translation}."""
        count = 0
        for entry in self.entries:
            msgid_text = entry['msgid_text']
            if msgid_text in translations_dict:
                japanese = translations_dict[msgid_text]
                old_msgstr = entry['msgstr_full']
                new_msgstr = f'msgstr "{japanese}"'
                
                self.content = self.content.replace(
                    entry['full_match'],
                    entry['full_match'].replace(old_msgstr, new_msgstr)
                )
                count += 1
        
        print(f"Applied {count} translations")
        return self
    
    def save(self):
        """Save modified PO file."""
        with open(self.po_file_path, 'w', encoding='utf-8') as f:
            f.write(self.content)
        print(f"Saved to {self.po_file_path}")
        return self


def main():
    if len(sys.argv) < 2:
        print("Usage: python translate_helper.py <po_file_path>")
        print("Example: python translate_helper.py locales/ja/LC_MESSAGES/apriltag/vision_portal/apriltag_intro/apriltag-intro.po")
        sys.exit(1)
    
    po_file = sys.argv[1]
    
    translator = POTranslator(po_file)
    translator.load().parse_entries().list_untranslated(limit=10)


if __name__ == "__main__":
    main()
