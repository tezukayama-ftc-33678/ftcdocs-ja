# Legacy Code Documentation

This document explains the deprecated code in the `legacy/` folder and how to migrate to the new modular architecture.

## Overview

The `legacy/` folder contains **old scripts and guides that are preserved for reference and gradual migration**. They are kept as-is for:

1. **Historical reference** — Shows how the project evolved
2. **Gradual migration** — Allows existing workflows to continue while new code uses `core/` modules
3. **Backward compatibility** — Old documentation still relevant to long-time users
4. **Learning resource** — Shows "before" and "after" patterns

**Nothing is removed.** Old scripts still work. They just use the old monolithic approach instead of modular architecture.

---

## What Changed?

### Before (Legacy, Monolithic)

```
scripts/
├── translate_po_smart.py      ← Everything mixed together
│   ├── RST markup logic        (from rst_markup_extractor.py)
│   ├── Translation logic       (Ollama call)
│   ├── Quality checks          (Chinese detection)
│   ├── PO file handling        (polib operations)
│   └── Token/cost estimation   (implicit, not separated)
│
├── batch_translate_smart.py    ← Depends on translate_po_smart.py
├── normalize_po_files.py       ← Standalone script
└── rst_markup_extractor.py     ← Utility module
```

**Problems with this approach:**
- Adding OpenAI support requires editing `translate_po_smart.py`
- Chinese detection logic coupled with translation logic
- PO file operations scattered throughout
- Hard to test individual components
- Difficult for new contributors to understand flow

### After (New Architecture, Modular)

```
scripts/
├── core/                           ← New: Separated concerns
│   ├── __init__.py
│   ├── rst_protector.py            ← RST markup (moved from rst_markup_extractor.py)
│   ├── po_file_handler.py          ← PO file operations
│   ├── translator_base.py          ← Abstract translator interface
│   ├── local_llm_translator.py     ← Ollama implementation
│   ├── quality_checker.py          ← Chinese detection, validation
│   └── token_estimator.py          ← Token counting for APIs
│
├── translate_po_smart.py           ← Refactored (uses core/)
├── batch_translate_smart.py        ← Refactored (uses core/)
├── normalize_po_files.py           ← Refactored (uses core/)
│
└── rst_markup_extractor.py         ← DEPRECATED (use core/rst_protector.py)
```

**Benefits:**
- Add new translator backends without changing main scripts
- Test components independently
- Clear separation of concerns
- Easy for contributors to understand each module
- Configuration driven (swappable models, APIs)

---

## Legacy Code Inventory

### In `legacy/scripts/`

These are old implementation attempts before the current modular system:

| File | Purpose | Status | Migration Path |
|------|---------|--------|-----------------|
| `legacy/scripts/` | (historical folder) | ARCHIVED | Reference only |

All scripts have been consolidated into the current `scripts/` folder with modular architecture.

### In `legacy/guides/`

| Guide | Purpose | Status | What to Use Instead |
|-------|---------|--------|---------------------|
| `AUTO_TRANSLATE.md` | Old auto-translation workflow | OUTDATED | See [WORKFLOW.md](../../WORKFLOW.md) |
| `AUTO_TRANSLATE_QUICKSTART.md` | Quick start (old approach) | OUTDATED | See [WORKFLOW.md](../../WORKFLOW.md) |
| `BUILD_JA.md` | Building Japanese docs | PARTIALLY OUTDATED | See [WORKFLOW.md](../../WORKFLOW.md) § "翻訳の確認とビルド" |
| `ERROR_FIX_GUIDE.md` | Fixing common errors | STILL USEFUL | See [ARCHITECTURE.md](../../ARCHITECTURE.md) § "Error Handling" |
| `EXECUTE_GUIDE.md` | Execution guide | OUTDATED | See [WORKFLOW.md](../../WORKFLOW.md) |
| `FIX_CHINESE_ERRORS.md` | Fixing Chinese detection issues | STILL USEFUL | See [ARCHITECTURE.md](../../ARCHITECTURE.md) § "Quality Validation" |
| `PO_SYNTAX_FIX_GUIDE.md` | Fixing PO syntax | STILL USEFUL | Same approach, now in `normalize_po_files.py` |
| `QUICK_FIX_GUIDE.md` | Quick fixes | PARTIALLY OUTDATED | Reference only |
| `SMART_TRANSLATE_GUIDE.md` | Smart translation explained | STILL USEFUL | See [ARCHITECTURE.md](../../ARCHITECTURE.md) |
| `TRANSLATION_APPROACH.md` | Overall translation philosophy | STILL USEFUL | See [ARCHITECTURE.md](../../ARCHITECTURE.md) |
| `TRANSLATION_GUIDE.md` | Original translation guide | OUTDATED | See [WORKFLOW.md](../../WORKFLOW.md) |
| `TRANSLATION_REFLECTION_FIX.md` | Translation quality improvements | STILL USEFUL | See [ARCHITECTURE.md](../../ARCHITECTURE.md) |

---

## Migration Guide

### For End Users (Running Translation Scripts)

**Good news:** No changes needed! The main scripts work exactly the same:

```powershell
# These commands still work exactly as before
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
python scripts/normalize_po_files.py --all
```

All changes are internal. Behavior is identical.

### For Contributors (Adding Features)

**Old Approach** (monolithic, not recommended):
```python
# Before: Everything in one file
from translate_po_smart import SmartPOTranslator

translator = SmartPOTranslator()
# Now you have translation, markup protection, quality checks all mixed
```

**New Approach** (modular, recommended):
```python
# After: Import specific modules
from core.po_file_handler import POFileHandler
from core.local_llm_translator import LocalLLMTranslator
from core.rst_protector import RSTProtector
from core.quality_checker import QualityChecker

# Each component has a single responsibility
po_handler = POFileHandler()
translator = LocalLLMTranslator()
protector = RSTProtector()
checker = QualityChecker()
```

### For Adding New Translator Backends

**Migration: Adding OpenAI Support**

#### Step 1: Create new translator (old approach — DON'T do this)

```python
# OLD: Modify translate_po_smart.py directly
if args.use_openai:
    # Add 200 lines of OpenAI code to translate_po_smart.py
    # ... messy mixing of concerns
```

#### Step 2: Create new translator (new approach — DO this)

```python
# NEW: Create core/openai_translator.py
from core.translator_base import Translator

class OpenAITranslator(Translator):
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
    
    def translate(self, text: str, context: str = "") -> str:
        # Clean implementation
        response = self.client.chat.completions.create(...)
        return response.choices[0].message.content
    
    def estimate_tokens(self, text: str) -> int:
        # Token counting
        return len(text) // 4

# Update translate_po_smart.py to dispatch:
if config['backend'] == 'openai':
    translator = OpenAITranslator(api_key=config['api_key'])
else:
    translator = LocalLLMTranslator(model=config['model'])
```

**Benefits:**
- `core/openai_translator.py` is isolated
- No changes needed to `rst_protector.py`, `po_file_handler.py`, etc.
- Easy to test independently
- Multiple backends can coexist

---

## Key Files Reference

### Still Used (Active Code)

| Path | Purpose | In Development? |
|------|---------|-----------------|
| [scripts/core/](../scripts/core/) | Core modules | ✅ Yes, actively used |
| [scripts/translate_po_smart.py](../scripts/translate_po_smart.py) | Single-file translator | ✅ Yes, refactored to use core/ |
| [scripts/batch_translate_smart.py](../scripts/batch_translate_smart.py) | Batch translator | ✅ Yes, refactored to use core/ |
| [scripts/normalize_po_files.py](../scripts/normalize_po_files.py) | PO normalization | ✅ Yes, refactored to use core/ |
| [data/translate_config.json](../data/translate_config.json) | Translation config | ✅ Yes, actively used |
| [WORKFLOW.md](../WORKFLOW.md) | User-facing guide | ✅ Yes, updated |
| [ARCHITECTURE.md](../ARCHITECTURE.md) | Technical architecture | ✅ Yes, new comprehensive guide |

### Legacy (Reference Only)

| Path | Purpose | Status | When to Use |
|------|---------|--------|------------|
| [legacy/guides/](../legacy/guides/) | Old workflow guides | 📖 Reference only | Understand project history |
| [legacy/scripts/](../legacy/scripts/) | Abandoned scripts | 📖 Reference only | Understand old approaches |
| [scripts/rst_markup_extractor.py](../scripts/rst_markup_extractor.py) | Old RST protection | ⚠️ DEPRECATED | Use `core/rst_protector.py` instead |

---

## What's Different in RST Protection?

This is the most critical refactoring. The RST protection logic moved from `rst_markup_extractor.py` to `core/rst_protector.py` with improvements:

### Old Code (rst_markup_extractor.py)

```python
class RSTMarkupProtector:
    def protect(self, text: str) -> Tuple[str, Dict[str, str]]:
        # ... protection logic mixed with restoration logic

    def restore(self, text: str, placeholders: Dict[str, str]) -> str:
        # ... restoration with Japanese spacing handling
```

### New Code (core/rst_protector.py)

```python
class RSTProtector:
    def protect(self, text: str) -> Tuple[str, Dict[str, str]]:
        # ✅ Clear separation
        # ✅ Better documentation of why Japanese spacing matters
        # ✅ Improved pattern ordering (more specific → less specific)
        # ✅ Type hints for clarity

    def restore(self, text: str, placeholders: Dict[str, str]) -> str:
        # ✅ Explicit Japanese character detection
        # ✅ Clear comments explaining spacing rules
        # ✅ Better structured for maintenance
```

**Functional differences:** None. Same output, better documented.

---

## Deprecation Timeline

**Phase 1: Current (Coexistence)**
- Both old and new code work
- `scripts/rst_markup_extractor.py` still imported by old scripts
- Warnings logged when using deprecated modules

**Phase 2: Future (Transition)**
- Main scripts refactored to use `core/` modules
- Old code kept for reference
- Documentation updated to recommend `core/` modules

**Phase 3: Future (Legacy Only)**
- `scripts/rst_markup_extractor.py` marked as import-only (no longer imported by main scripts)
- `legacy/` folder expanded with migration guides

---

## Troubleshooting: Which Code Should I Use?

### Scenario 1: "I want to translate a single PO file"

**Use:** `scripts/translate_po_smart.py`

```powershell
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po
```

This script now uses `core/` modules internally. **No changes to how you call it.**

### Scenario 2: "I want to add Chinese language support"

**Don't use:** `legacy/guides/FIX_CHINESE_ERRORS.md`

**Use:** [ARCHITECTURE.md](../../ARCHITECTURE.md) § "Adding a New Translator Backend"

Create a new translator:
```python
# core/chinese_translator.py
from core.translator_base import Translator

class ChineseTranslator(Translator):
    def translate(self, text: str, context: str = "") -> str:
        # Chinese translation logic
        pass
```

### Scenario 3: "I want to understand the overall architecture"

**Don't use:** `legacy/guides/TRANSLATION_APPROACH.md`

**Use:** [ARCHITECTURE.md](../../ARCHITECTURE.md)

### Scenario 4: "The RST protection is broken"

**Don't edit:** `scripts/rst_markup_extractor.py`

**Edit:** `scripts/core/rst_protector.py`

Both have the same logic, but `core/` version has better documentation and structure.

---

## FAQ

### Q: Can I still use the old scripts?

**A:** Yes, absolutely. They work unchanged. But they now use the new modular infrastructure internally (if you modify them).

### Q: Should I migrate my own code to use core/ modules?

**A:** If you're:
- Writing new code → **Yes, use core/ modules**
- Maintaining existing scripts → **Keep as-is unless you need new features**
- Contributing to the project → **Refactor to use core/ modules**

### Q: What if I encounter bugs in the legacy code?

**A:** 
- If it's a bug in `core/` modules → fix it there
- If it's only in old scripts → the core/ version likely fixed it
- Report on GitHub with your version (old or new)

### Q: Is rst_markup_extractor.py still used?

**A:** It's imported by the old `translate_po_smart.py` version in your checkout. The new modular version uses `core/rst_protector.py` instead. Both work identically.

### Q: How do I know which version I'm running?

```python
# Check imports at the top of translate_po_smart.py
# OLD: from rst_markup_extractor import RSTMarkupProtector
# NEW: from core.rst_protector import RSTProtector
```

### Q: Can I use both old and new scripts simultaneously?

**A:** Yes. They share the same PO files and don't conflict. However:
- Both will read/write to the same translation files
- Progress tracking (`data/translation_progress.json`) is shared
- Don't run batch operations simultaneously (file locking)

### Q: What about the config file? Did it change?

**A:** No. `data/translate_config.json` is the same. Both old and new scripts read it.

---

## Maintenance Checklist

For maintainers updating the project:

- [ ] When adding new translator backend:
  - [ ] Create `core/new_translator.py` (not modify existing code)
  - [ ] Implement `Translator` abstract class
  - [ ] Add configuration to `data/translate_config.json`
  - [ ] Update [ARCHITECTURE.md](../../ARCHITECTURE.md)
  - [ ] Update [WORKFLOW.md](../../WORKFLOW.md) if user-facing
  - [ ] Add tests

- [ ] When fixing RST protection:
  - [ ] Fix `core/rst_protector.py` (primary)
  - [ ] Update `scripts/rst_markup_extractor.py` if still used
  - [ ] Add test case to verify fix

- [ ] When updating guides:
  - [ ] Update active guides in root (`WORKFLOW.md`, `ARCHITECTURE.md`)
  - [ ] Keep legacy guides as-is for reference
  - [ ] Add migration notes if moving guides

- [ ] When deprecating code:
  - [ ] Keep old code in `legacy/`
  - [ ] Document why it's deprecated
  - [ ] Provide migration path
  - [ ] Update this file

---

## References

- [WORKFLOW.md](../../WORKFLOW.md) — User-facing workflow guide
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — Technical architecture details
- [scripts/core/](../scripts/core/) — New modular code
- `legacy/` — Old code for reference

---

**Version:** January 13, 2026  
**Status:** Active (refactoring in progress)  
**Next Review:** When all main scripts fully refactored to use core/ modules
