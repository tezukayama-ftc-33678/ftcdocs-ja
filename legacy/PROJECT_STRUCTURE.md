# Project Structure Guide

This document explains the organization of the FTC Japanese translation project after the modularization refactoring.

## Directory Tree

```
ftcdocs-ja/
├── LICENSE                        # Apache 2.0 license
├── LICENSE-JA.md                  # Japanese license text
├── README.md                       # Project overview
│
├── WORKFLOW.md                    # 📖 User-facing workflow guide (UPDATE FOR EACH RELEASE)
├── ARCHITECTURE.md                # 📖 Technical architecture (NEW)
├── LEGACY.md                      # 📖 Legacy code documentation (NEW)
├── REFACTORING_SUMMARY.md         # 📖 Refactoring overview (NEW)
│
├── scripts/                       # Translation scripts
│   ├── core/                      # ✨ NEW: Core modules (main location for new code)
│   │   ├── __init__.py
│   │   ├── rst_protector.py       # RST markup extraction and restoration
│   │   ├── po_file_handler.py     # PO file I/O operations
│   │   ├── translator_base.py     # Abstract translator interface
│   │   ├── local_llm_translator.py# Ollama LLM implementation
│   │   ├── quality_checker.py     # Quality validation (Chinese detection)
│   │   └── token_estimator.py     # Token/cost estimation for APIs
│   │
│   ├── translate_po_smart.py      # ⏳ Main translator (being refactored to use core/)
│   ├── batch_translate_smart.py   # ⏳ Batch translator (being refactored to use core/)
│   ├── normalize_po_files.py      # ⏳ PO normalization (being refactored to use core/)
│   ├── test_simplified_chinese_detection.py  # Quality validation script
│   ├── rst_markup_extractor.py    # ⚠️  DEPRECATED: Use core/rst_protector.py instead
│   └── README.md                  # Script documentation
│
├── data/                          # Configuration and progress tracking
│   ├── translate_config.json      # Translation settings (shared by all scripts)
│   ├── mistranslation_corrections.json  # Mistranslation fixes database
│   ├── simplified_chinese_blocked_entries.json  # Chinese detection reports
│   ├── translation_progress.json  # Batch translation progress tracker
│   └── README.md                  # Data files documentation
│
├── guides/                        # User guides and glossaries
│   ├── GLOSSARY.md                # 📚 Technical glossary (FTC terminology)
│   ├── LOCAL_LLM_SETUP.md         # 📖 Setting up Ollama (local LLM)
│   ├── LICENSE_AND_LOGO_GUIDE.md  # 📖 License and logo usage
│   └── README.md                  # Guides index
│
├── legacy/                        # 📖 Deprecated code and guides (for reference)
│   ├── README.md                  # Legacy documentation overview
│   ├── guides/                    # Old workflow guides
│   │   ├── AUTO_TRANSLATE.md
│   │   ├── BUILD_JA.md
│   │   ├── TRANSLATION_GUIDE.md
│   │   └── ... (13 guides total)
│   │
│   ├── scripts/                   # Old script implementations
│   │   ├── check_translation_progress.py
│   │   ├── translate_partial.py
│   │   └── ... (historical scripts)
│   │
│   └── data/                      # Old data files and outputs
│       ├── po_issues.json
│       └── ...
│
├── locales/                       # Sphinx gettext translations (generated)
│   ├── ja/
│   │   └── LC_MESSAGES/           # Japanese PO files (output of make gettext)
│   │       ├── index.po           # Translation for index.rst
│   │       ├── overview/
│   │       │   ├── overview.po
│   │       │   ├── intro.po
│   │       │   └── ...
│   │       └── ... (100+ PO files)
│
├── docs/                          # Sphinx documentation source
│   ├── source/                    # RST source files
│   │   ├── conf.py                # Sphinx configuration
│   │   ├── index.rst              # Main documentation index
│   │   ├── ... (RST files in English)
│   │
│   ├── build/                     # Built output (generated)
│   │   ├── html-ja/               # Japanese HTML build output
│   │   │   ├── index.html
│   │   │   ├── ... (built HTML)
│   │   │
│   │   ├── gettext/               # Temporary gettext output
│   │   └── ...
│   │
│   ├── Makefile                   # Build commands
│   ├── requirements.txt           # Build dependencies (Python)
│   └── build_result.txt           # Build log
```

---

## Key Locations

### 📖 **Documentation (Read First)**

| Document | Purpose | Audience | When to Read |
|----------|---------|----------|--------------|
| [README.md](./README.md) | Project overview | Everyone | First thing |
| [WORKFLOW.md](./WORKFLOW.md) | Translation workflow | Users, maintainers | Before running scripts |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | Technical design | Contributors, maintainers | Before modifying code |
| [LEGACY.md](./LEGACY.md) | Legacy code explanation | Contributors | When understanding old code |
| [REFACTORING_SUMMARY.md](./REFACTORING_SUMMARY.md) | What changed | Contributors, reviewers | To understand the refactoring |
| [guides/GLOSSARY.md](./guides/GLOSSARY.md) | FTC terminology | Translators | During translation |
| [guides/LOCAL_LLM_SETUP.md](./guides/LOCAL_LLM_SETUP.md) | Ollama setup | Users | First-time setup |

### ✨ **Core Code (New, Actively Developed)**

All new code goes here. Well-structured, focused modules:

```
scripts/core/
├── rst_protector.py        # 330 lines, focused
├── po_file_handler.py      # 270 lines, focused
├── translator_base.py      # 150 lines, abstract interface
├── local_llm_translator.py # 280 lines, implementation
├── quality_checker.py      # 200 lines, validation
└── token_estimator.py      # 180 lines, token counting
```

**To add features:** Extend these modules or create new ones in `core/`.

### ⏳ **Main Scripts (Being Refactored)**

These are the **user-facing entry points**:

```
scripts/
├── translate_po_smart.py       # Translate single PO file
├── batch_translate_smart.py    # Translate multiple PO files
└── normalize_po_files.py       # Fix mistranslations
```

**Status:** Will be refactored to use `core/` modules (backward compatible).

### ⚠️ **Deprecated Code (Reference Only)**

```
scripts/
└── rst_markup_extractor.py     # OLD: Use core/rst_protector.py instead

legacy/
├── guides/                     # Old workflow guides
├── scripts/                    # Old implementation attempts
└── data/                       # Old data files
```

**Don't use for new code.** Reference only.

### 📊 **Data & Configuration**

```
data/
├── translate_config.json                    # Main configuration
├── mistranslation_corrections.json          # Fix database
├── simplified_chinese_blocked_entries.json  # Quality reports
└── translation_progress.json                # Batch progress
```

All scripts share these files. Configuration-driven (modify JSON, not code).

### 📚 **Generated Output (Ignored in Git)**

```
locales/ja/LC_MESSAGES/
├── index.po                # Generated from docs/source/index.rst
├── overview/overview.po    # Generated from docs/source/overview/
└── ... (100+ PO files)

docs/build/
├── gettext/                # Temporary (make gettext output)
├── html-ja/                # Final Japanese HTML docs
└── ...
```

These are **generated files**, not edited directly.

---

## File Lifecycle

### Example: Translating a Document

```
docs/source/overview/intro.rst (English source)
    ↓
make gettext (generates POT file)
    ↓
sphinx-intl update (generates PO file)
    ↓
locales/ja/LC_MESSAGES/overview/intro.po (empty msgstr)
    ↓
python scripts/translate_po_smart.py (fills in msgstr)
    ↓
locales/ja/LC_MESSAGES/overview/intro.po (with Japanese translations)
    ↓
make html-ja (builds Japanese HTML)
    ↓
docs/build/html-ja/ (final Japanese docs)
```

**Where to intervene?** At the `translate_po_smart.py` step.

---

## Module Dependencies

### Dependency Graph

```
translate_po_smart.py
├── core/po_file_handler.py
├── core/rst_protector.py
├── core/local_llm_translator.py
│   ├── core/translator_base.py
│   └── core/quality_checker.py
├── core/quality_checker.py
└── core/token_estimator.py (future)

batch_translate_smart.py
├── core/po_file_handler.py
├── translate_po_smart.py (or refactor to use core/ directly)
└── data/translation_progress.json

normalize_po_files.py
├── core/po_file_handler.py
└── data/mistranslation_corrections.json
```

**All modules are standalone** and can be imported independently:

```python
# Can import individually
from core.rst_protector import RSTProtector
from core.po_file_handler import POFileHandler
from core.quality_checker import QualityChecker
```

---

## File Naming Conventions

### Script Files

| Pattern | Purpose | Example |
|---------|---------|---------|
| `*_smart.py` | Advanced/multi-feature script | `translate_po_smart.py` |
| `*_utils.py` | Utility functions | (none currently) |
| `test_*.py` | Test files | `test_simplified_chinese_detection.py` |

### Core Modules

| Pattern | Purpose | Example |
|---------|---------|---------|
| `*_base.py` | Abstract base classes | `translator_base.py` |
| `*_protector.py` | Protection/extraction logic | `rst_protector.py` |
| `*_handler.py` | File/resource I/O | `po_file_handler.py` |
| `*_checker.py` | Validation/quality checks | `quality_checker.py` |
| `*_estimator.py` | Estimation/calculation | `token_estimator.py` |

### Configuration Files

```
data/
├── *_config.json              # Configuration (human-editable)
├── *_corrections.json         # Database of fixes/mappings
├── *_progress.json            # Tracking/state information
└── *_blocked_entries.json     # Reports/filtered results
```

---

## Adding New Files

### New Script

```python
# scripts/my_new_script.py
"""Module docstring with purpose."""

from core.po_file_handler import POFileHandler
from core.rst_protector import RSTProtector

# Import what you need from core/
```

Place in `scripts/` directly (not `scripts/core/`).

### New Core Module

```python
# scripts/core/my_new_feature.py
"""
Module docstring with detailed explanation.

Purpose, design decisions, and usage examples.
"""

from .translator_base import Translator
# or import from other core modules

class MyNewFeature:
    """Clear docstring."""
    pass
```

Place in `scripts/core/` (not `scripts/` directly).

### New Configuration

```json
// data/my_new_config.json
{
  "setting1": "value",
  "setting2": 42
}
```

Update [data/README.md](./data/README.md) with description.

### New Guide

```markdown
# My New Guide

Put in `guides/` directory.
Reference in [guides/README.md](./guides/README.md).
```

---

## Common Tasks

### Task: "I want to translate a single PO file"

**Location:** `scripts/translate_po_smart.py`

```powershell
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po
```

### Task: "I want to translate all PO files"

**Location:** `scripts/batch_translate_smart.py`

```powershell
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

### Task: "I want to add Chinese language support"

**Location:** Create new file `scripts/core/chinese_translator.py`

```python
from .translator_base import Translator

class ChineseTranslator(Translator):
    def translate(self, text: str, context: str = "") -> str:
        # Implementation
        pass
```

### Task: "I want to understand RST protection"

**Location:** `scripts/core/rst_protector.py` (read the docstrings)

Also read "RST Markup Protection" in [ARCHITECTURE.md](./ARCHITECTURE.md).

### Task: "I want to check translation quality"

**Location:** `scripts/core/quality_checker.py` or `scripts/test_simplified_chinese_detection.py`

```powershell
python scripts/test_simplified_chinese_detection.py
```

### Task: "I want to understand the whole architecture"

**Location:** Read [ARCHITECTURE.md](./ARCHITECTURE.md)

Then read the module docstrings in `scripts/core/`.

---

## Quick Reference

### Important Files by Role

**Project Manager:**
- [README.md](./README.md) — Overview
- [WORKFLOW.md](./WORKFLOW.md) — How to use
- [data/translation_progress.json](./data/translation_progress.json) — Progress tracking

**Translator:**
- [WORKFLOW.md](./WORKFLOW.md) — How to run scripts
- [guides/GLOSSARY.md](./guides/GLOSSARY.md) — Terminology
- [data/translate_config.json](./data/translate_config.json) — Settings

**Developer:**
- [ARCHITECTURE.md](./ARCHITECTURE.md) — Design
- [scripts/core/](./scripts/core/) — Core modules (read docstrings)
- [LEGACY.md](./LEGACY.md) — Legacy code explanation

**Maintainer:**
- [ARCHITECTURE.md](./ARCHITECTURE.md) — Architecture decisions
- [LEGACY.md](./LEGACY.md) — Deprecation path
- [WORKFLOW.md](./WORKFLOW.md) — User-facing workflows
- [scripts/core/](./scripts/core/) — Where to add features

---

## Evolution Timeline

| Phase | Date | Status | Description |
|-------|------|--------|-------------|
| **Phase 0** | Before Jan 2026 | ✅ Done | Monolithic scripts, basic guides |
| **Phase 1** | Jan 2026 | ✅ Done | Create modular core/, document architecture |
| **Phase 2** | In Progress | ⏳ | Refactor main scripts to use core/ |
| **Phase 3** | Future | 📋 | Add comprehensive unit tests |
| **Phase 4** | Future | 📋 | Integration with OpenAI API |
| **Phase 5** | Future | 📋 | Performance optimization |

---

**Last Updated:** January 13, 2026  
**Structure:** Stable (core/ complete, main scripts being refactored)  
**Location Guide Version:** 1.0
