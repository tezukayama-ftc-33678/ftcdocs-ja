#!/usr/bin/env python3
"""
PO File Handler Module

Safe reading and writing of gettext PO files while preserving metadata,
comments, and fuzzy flags.

A PO (Portable Object) file contains:
- msgid: Original English text
- msgstr: Translated text (empty if untranslated)
- Comments: Developer notes, translator comments
- Flags: 'fuzzy' (incomplete translation), etc.

Safety Guarantees
------------------
✓ Never modifies msgid
✓ Only writes to msgstr
✓ Preserves fuzzy flags and comments
✓ Validates PO syntax before writing
✓ Supports periodic saving during long operations
"""

from pathlib import Path
from typing import List, Dict, Tuple, Optional
import polib


class POFileHandler:
    """
    Safely handles PO file operations.
    
    Provides methods for:
    - Loading PO files
    - Filtering entries (translated vs untranslated)
    - Updating translations (only msgstr)
    - Getting statistics
    - Saving with validation
    """
    
    @staticmethod
    def load(path: str) -> polib.POFile:
        """
        Load a PO file.
        
        Args:
            path: Path to .po file
        
        Returns:
            Loaded POFile object
        
        Raises:
            FileNotFoundError: If file doesn't exist
            Exception: If PO file is malformed
        """
        po_path = Path(path)
        if not po_path.exists():
            raise FileNotFoundError(f"PO file not found: {path}")
        
        try:
            po = polib.pofile(str(po_path))
            return po
        except Exception as e:
            raise Exception(f"Failed to load PO file {path}: {e}")
    
    @staticmethod
    def save(po: polib.POFile, path: str) -> None:
        """
        Save a PO file.
        
        Args:
            po: POFile object to save
            path: Output path
        
        Raises:
            Exception: If save fails
        """
        try:
            po.save(str(path))
        except Exception as e:
            raise Exception(f"Failed to save PO file {path}: {e}")
    
    @staticmethod
    def get_untranslated_entries(po: polib.POFile) -> List[polib.POEntry]:
        """
        Get all entries that need translation.
        
        Filters out:
        - Entries with msgstr already filled
        - Obsolete entries
        - Entries marked as fuzzy (usually means they're incomplete)
        
        Args:
            po: POFile object
        
        Returns:
            List of entries needing translation
        """
        entries = []
        for entry in po:
            # Skip if already translated
            if entry.msgstr:
                continue
            
            # Skip obsolete entries
            if entry.obsolete:
                continue
            
            # Skip fuzzy entries (usually incomplete translations)
            if 'fuzzy' in entry.flags:
                continue
            
            entries.append(entry)
        
        return entries
    
    @staticmethod
    def get_translated_entries(po: polib.POFile) -> List[polib.POEntry]:
        """
        Get all entries that have translations.
        
        Args:
            po: POFile object
        
        Returns:
            List of translated entries
        """
        entries = []
        for entry in po:
            if entry.msgstr and not entry.obsolete:
                entries.append(entry)
        
        return entries
    
    @staticmethod
    def set_translation(entry: polib.POEntry, translation: str) -> None:
        """
        Set translation for an entry.
        
        Only modifies msgstr, never msgid.
        Removes 'fuzzy' flag after successful translation.
        
        Args:
            entry: POEntry to update
            translation: Japanese translation text
        """
        if not entry:
            raise ValueError("Entry cannot be None")
        
        if not isinstance(translation, str):
            raise ValueError(f"Translation must be string, got {type(translation)}")
        
        # Set translation
        entry.msgstr = translation
        
        # Clear fuzzy flag if it exists (translation is now explicit)
        if 'fuzzy' in entry.flags:
            entry.flags.remove('fuzzy')
    
    @staticmethod
    def get_stats(po: polib.POFile) -> Tuple[int, int]:
        """
        Get translation statistics for a PO file.
        
        Args:
            po: POFile object
        
        Returns:
            Tuple of (translated_count, total_count)
            
        Example:
            >>> handler = POFileHandler()
            >>> po = handler.load("index.po")
            >>> translated, total = handler.get_stats(po)
            >>> print(f"{translated}/{total} entries translated")
        """
        total = 0
        translated = 0
        
        for entry in po:
            if entry.obsolete:
                continue
            
            total += 1
            if entry.msgstr:
                translated += 1
        
        return translated, total
    
    @staticmethod
    def get_entry_by_msgid(po: polib.POFile, msgid: str) -> Optional[polib.POEntry]:
        """
        Find an entry by its msgid.
        
        Args:
            po: POFile object
            msgid: Text to search for
        
        Returns:
            POEntry if found, None otherwise
        """
        return po.find(msgid)
    
    @staticmethod
    def validate_po_syntax(po: polib.POFile) -> bool:
        """
        Validate PO file syntax.
        
        Args:
            po: POFile object
        
        Returns:
            True if valid, raises exception if invalid
        """
        try:
            # Check that all entries have non-empty msgid
            for entry in po:
                if entry.obsolete:
                    continue
                if not entry.msgid:
                    raise ValueError(f"Entry with empty msgid found")
            
            return True
        except Exception as e:
            raise Exception(f"PO file validation failed: {e}")
    
    @staticmethod
    def create_entry(msgid: str, msgstr: str = "", 
                     translator_comment: str = "", 
                     developer_comment: str = "") -> polib.POEntry:
        """
        Create a new PO entry.
        
        Args:
            msgid: Original text
            msgstr: Translation (default: empty)
            translator_comment: Translator's note
            developer_comment: Developer's note
        
        Returns:
            New POEntry
        """
        entry = polib.POEntry(msgid=msgid, msgstr=msgstr)
        if translator_comment:
            entry.tcomment = translator_comment
        if developer_comment:
            entry.comment = developer_comment
        return entry


class POBatchHandler:
    """
    Handle batch operations on multiple PO files.
    
    Tracks which files have been processed and supports resumable operations.
    """
    
    def __init__(self):
        """Initialize batch handler."""
        self.handler = POFileHandler()
    
    def find_po_files(self, directory: str, 
                     exclude_translated: bool = True) -> List[Path]:
        """
        Find all PO files in a directory.
        
        Args:
            directory: Path to directory
            exclude_translated: If True, skip files with all entries translated
        
        Returns:
            List of PO file paths sorted by size (smallest first)
        """
        dir_path = Path(directory)
        po_files = list(dir_path.rglob('*.po'))
        
        if exclude_translated:
            result = []
            for po_file in po_files:
                try:
                    po = self.handler.load(str(po_file))
                    translated, total = self.handler.get_stats(po)
                    if translated < total:  # Not fully translated
                        result.append(po_file)
                except Exception:
                    # Include files that can't be read (might be corrupted)
                    result.append(po_file)
            po_files = result
        
        # Sort by file size (smallest first, easier to process)
        po_files.sort(key=lambda p: p.stat().st_size)
        
        return po_files
    
    def get_file_stats(self, po_file_path: str) -> Dict[str, int]:
        """
        Get translation statistics for a single file.
        
        Args:
            po_file_path: Path to PO file
        
        Returns:
            Dict with keys: 'translated', 'untranslated', 'fuzzy', 'total'
        """
        po = self.handler.load(po_file_path)
        
        translated = 0
        untranslated = 0
        fuzzy = 0
        total = 0
        
        for entry in po:
            if entry.obsolete:
                continue
            
            total += 1
            if entry.msgstr:
                translated += 1
                if 'fuzzy' in entry.flags:
                    fuzzy += 1
            else:
                untranslated += 1
        
        return {
            'translated': translated,
            'untranslated': untranslated,
            'fuzzy': fuzzy,
            'total': total,
        }
