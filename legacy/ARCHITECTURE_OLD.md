# Translation Pipeline Architecture

## Overview

This document describes the refactored translation infrastructure for the FTC Japanese documentation project. The architecture emphasizes **clarity over cleverness**, **explicit concerns separation**, and **maintainability**.

### Core Principles

1. **Preserve RST Structure Exactly** — RST syntax, directives, roles, references, inline markup, code blocks, substitutions, and anchors must never be altered.
2. **Swappable Translation Backend** — The translation service (local LLM or future API) must be isolated from RST processing and PO file handling.
3. **Clear Module Responsibilities** — Each module has a single, well-defined purpose.
4. **Explicit RST Protection** — RST protection logic is detailed, documented, and separate from translation logic.
5. **Future API Support** — Design allows for seamless integration of OpenAI/ChatGPT or other APIs without affecting core modules.

---

## Directory Structure

```
ftcdocs-ja/
├── scripts/
│   ├── core/                          # New: Core translation modules
│   │   ├── __init__.py
│   │   ├── rst_protector.py           # RST markup extraction and restoration
│   │   ├── po_file_handler.py         # PO file reading/writing
│   │   ├── translator_base.py         # Abstract translator interface
│   │   ├── local_llm_translator.py    # Local LLM implementation
│   │   ├── token_estimator.py         # Token/cost estimation (future API use)
│   │   └── quality_checker.py         # Chinese detection, validation
│   │
│   ├── translate_po_smart.py          # Main script (single file)
│   ├── batch_translate_smart.py       # Batch script (refactored to use core/)
│   ├── normalize_po_files.py          # Normalization script (uses PO handler)
│   ├── rst_markup_extractor.py        # DEPRECATED: moved to core/rst_protector.py
│   │
│   ├── test_simplified_chinese_detection.py  # Validation script
│   └── README.md
│
├── data/
│   ├── translate_config.json          # Translation settings
│   ├── mistranslation_corrections.json
│   ├── simplified_chinese_blocked_entries.json
│   └── translation_progress.json
│
├── guides/
│   ├── GLOSSARY.md
│   ├── LOCAL_LLM_SETUP.md
│   └── LICENSE_AND_LOGO_GUIDE.md
│
├── legacy/                            # Preserved for reference (see LEGACY.md)
│   ├── guides/
│   ├── scripts/
│   ├── data/
│   └── README.md
│
├── ARCHITECTURE.md                    # This file
├── LEGACY.md                          # Documentation of deprecated code
└── WORKFLOW.md                        # Updated workflow guide
```

---

## Module Architecture

### 1. `core/rst_protector.py` — RST Markup Protection

**Purpose**: Extract, protect, and restore RST markup while handling Japanese spacing requirements.

**Key Responsibilities**:
- Identify and protect RST patterns (roles, directives, URLs, file paths, inline markup, etc.)
- Replace protected content with unique placeholders
- Restore placeholders after translation
- **Crucially**: Insert half-width spaces before/after inline markup when adjacent to Japanese characters

**Why This Matters**:
```
Bad (causes Sphinx errors):
日本語このドキュメント`_へのリンク

Good (correct spacing):
日本語 このドキュメント `_ へのリンク
```

**Usage**:
```python
from core.rst_protector import RSTProtector

protector = RSTProtector()

# Protect markup
text = "See :doc:`docs </path>` for details."
protected_text, placeholders = protector.protect(text)
# protected_text: "See __RST_ROLE_0__ for details."
# placeholders: {"__RST_ROLE_0__": ":doc:`docs </path>`"}

# Restore after translation
translated = "詳細は __RST_ROLE_0__ を参照してください。"
restored = protector.restore(translated, placeholders)
# restored: "詳細は :doc:`docs </path>` を参照してください。"
```

**Protected Patterns** (in priority order):
1. External links: `` `text <url>`_ ``
2. Roles: `:ref:`text``, `:doc:`text``, `:download:`file``, etc.
3. URLs: `http://...`, `https://...`
4. File paths: `file.py`, `images/sample.png`, `manual.pdf`, etc.
5. Inline literals: ``` ``code`` ```
6. Bold/italic: `**bold**`, `*italic*`
7. Internal links: `` `text`_ ``
8. Substitutions: `|name|`

---

### 2. `core/po_file_handler.py` — PO File I/O

**Purpose**: Safely read and write PO files, preserving metadata and structure.

**Key Responsibilities**:
- Load PO files using `polib`
- Filter entries (translated vs untranslated, fuzzy vs resolved)
- Write translations to `msgstr` only
- Preserve metadata, comments, and fuzzy flags
- Support periodic saving during batch operations

**Usage**:
```python
from core.po_file_handler import POFileHandler

handler = POFileHandler()

# Load PO file
po = handler.load(path="locales/ja/LC_MESSAGES/index.po")

# Get entries to translate
entries = handler.get_untranslated_entries(po)

# Update translation
handler.set_translation(entry, "翻訳テキスト")

# Save
handler.save(po, path="locales/ja/LC_MESSAGES/index.po")

# Get progress
translated_count, total_count = handler.get_stats(po)
```

**Safety Guarantees**:
- ✓ Never modifies `msgid`
- ✓ Only writes to `msgstr`
- ✓ Preserves fuzzy flags and comments
- ✓ Validates PO syntax before writing

---

### 3. `core/translator_base.py` — Abstract Translator Interface

**Purpose**: Define a common interface for translation backends.

**Key Responsibilities**:
- Define abstract `Translator` class with standard method signature
- Enforce consistent error handling and retry logic
- Document contract for all translator implementations

**Usage**:
```python
from core.translator_base import Translator, TranslationError

class MyTranslator(Translator):
    def translate(self, text: str, context: str = "") -> str:
        """Translate text. Raise TranslationError on failure."""
        pass
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate token count for text."""
        pass
```

**Future Extensions**:
- `OpenAITranslator` (ChatGPT, GPT-4)
- `AnthropicTranslator` (Claude)
- `GoogleTranslator` (Vertex AI)

---

### 4. `core/local_llm_translator.py` — Local LLM Backend

**Purpose**: Translate using a local Ollama model.

**Key Responsibilities**:
- Initialize Ollama connection
- Generate translation prompts with glossary and context
- Handle retries and fallback models
- Validate output (Chinese detection, length checks)

**Usage**:
```python
from core.local_llm_translator import LocalLLMTranslator

translator = LocalLLMTranslator(
    model="qwen2.5-coder:7b-instruct",
    temperature=0.1,
    max_retries=3,
    glossary={"FTC": "FTC"}  # English terms to preserve
)

try:
    translation = translator.translate(
        text="Protected text with __RST_ROLE_0__",
        context="Previous sentence for context"
    )
except TranslationError as e:
    print(f"Translation failed: {e}")
```

**Configuration** (from `data/translate_config.json`):
```json
{
  "model": "qwen2.5-coder:7b-instruct",
  "fallback_model": "qwen2.5:7b-instruct-q5_K_M",
  "temperature": 0.05,
  "max_retries": 3,
  "chunk_size": 400,
  "context_window": 2048
}
```

---

### 5. `core/quality_checker.py` — Quality Validation

**Purpose**: Detect translation quality issues (Chinese characters, etc.).

**Key Responsibilities**:
- Detect simplified Chinese characters
- Validate Japanese output
- Generate quality reports
- Block low-quality translations

**Usage**:
```python
from core.quality_checker import QualityChecker

checker = QualityChecker()

# Check for Chinese
if checker.has_simplified_chinese("翻訳テキスト"):
    print("Chinese detected!")

# Validate Japanese
if not checker.is_valid_japanese("翻訳テキスト"):
    print("Not valid Japanese!")

# Get report
report = checker.generate_report(entries_checked=100, issues_found=5)
```

---

### 6. `core/token_estimator.py` — Token/Cost Estimation

**Purpose**: Estimate tokens for future API cost calculation.

**Key Responsibilities**:
- Estimate tokens for different model families
- Calculate estimated cost
- Provide pre-translation dry runs

**Usage**:
```python
from core.token_estimator import TokenEstimator

estimator = TokenEstimator()

# Estimate for OpenAI GPT-4
tokens = estimator.estimate_tokens("日本語のテキスト", model="gpt-4")
cost = estimator.estimate_cost(tokens, model="gpt-4")
print(f"Estimated cost: ${cost:.2f}")
```

---

## Script Architecture

### Existing Scripts (Refactored)

#### `translate_po_smart.py`
- **Role**: Single-file translator
- **Changes**: Now imports from `core/` modules
- **Behavior**: Unchanged (backward compatible)

```python
from core.po_file_handler import POFileHandler
from core.rst_protector import RSTProtector
from core.local_llm_translator import LocalLLMTranslator
```

#### `batch_translate_smart.py`
- **Role**: Batch translator with progress tracking
- **Changes**: Refactored to use `core/` modules
- **Behavior**: Unchanged (backward compatible)

#### `normalize_po_files.py`
- **Role**: Mistranslation correction
- **Changes**: Uses `POFileHandler` for safer I/O
- **Behavior**: Unchanged (backward compatible)

---

## Data Flow Diagram

```
POファイル
    ↓
┌─────────────────────────┐
│  POFileHandler.load()   │  ← 安全なPO読み込み
└───────┬─────────────────┘
        ↓
┌─────────────────────────┐
│ Extract msgid (entry)   │  ← 翻訳対象を取得
└───────┬─────────────────┘
        ↓
┌─────────────────────────┐
│ RSTProtector.protect()  │  ← RST構文を保護
└───────┬─────────────────┘
        ↓
┌─────────────────────────┐
│ LocalLLMTranslator      │  ← Ollama翻訳実行
│ .translate()            │
└───────┬─────────────────┘
        ↓
┌─────────────────────────┐
│ QualityChecker.check()  │  ← 品質検証（中国語等）
└───────┬─────────────────┘
        ↓ (valid)
┌─────────────────────────┐
│ RSTProtector.restore()  │  ← RST構文を復元
└───────┬─────────────────┘
        ↓
┌─────────────────────────┐
│ POFileHandler.save()    │  ← msgstrに保存
└───────┬─────────────────┘
        ↓
  POファイル（翻訳済み）
```

---

## Chunking Strategy

Large `msgid` entries are split into chunks before translation to:
1. Fit within LLM context windows
2. Improve translation quality
3. Reduce VRAM pressure

**Chunking Logic** (in `core/text_splitter.py`):
- Split by paragraphs (blank lines)
- If paragraph exceeds `max_length`, split by sentences
- Preserve punctuation and structure
- Maintain context for next chunk

```python
from core.text_splitter import TextSplitter

splitter = TextSplitter(max_length=400)
chunks = splitter.split("Large text...\n\nNext paragraph...")
# Returns: ["chunk1", "chunk2", "chunk3"]
```

---

## Configuration System

All configuration lives in `data/translate_config.json`:

```json
{
  "model": "qwen2.5-coder:7b-instruct",
  "fallback_model": "qwen2.5:7b-instruct-q5_K_M",
  "temperature": 0.05,
  "max_retries": 3,
  "chunk_size": 400,
  "context_window": 2048,
  "skip_translated": true,
  "quality_check_enabled": true
}
```

**Why JSON?**
- Language-agnostic
- Version-controllable
- Easy to modify without code changes
- Supports comments (with custom parser if needed)

---

## Error Handling Strategy

**Three-Level Error Recovery**:

1. **Chunk-Level**: Retry with backoff on network/model errors
2. **File-Level**: Mark failed file, continue to next
3. **Batch-Level**: Save progress, allow resumption

```
Entry fails to translate
    ↓
Retry up to max_retries times (exponential backoff)
    ↓
Try fallback model (if available)
    ↓
If all fail: Record in failed_entries.json, continue
    ↓
Resume later: progress/failed files are tracked
```

---

## Testing Strategy

### Unit Tests (with `pytest`)

```python
# tests/test_rst_protector.py
def test_protect_role():
    protector = RSTProtector()
    text = "See :ref:`label`"
    protected, ph = protector.protect(text)
    assert "__RST_ROLE_0__" in protected
    assert ":ref:`label`" in ph.values()

def test_japanese_spacing():
    protector = RSTProtector()
    protected = "__RST_ROLE_0__"
    restored = protector.restore("日本語 __RST_ROLE_0__", {
        "__RST_ROLE_0__": ":ref:`label`"
    })
    # Should have space before role
    assert "日本語 :ref:`label`" in restored
```

### Integration Tests

```python
# tests/test_full_pipeline.py
def test_single_file_translation():
    # Load → Protect → Translate → Restore → Save
    # Verify: No RST corruption, valid Japanese, all markup preserved
    pass
```

---

## Future API Integration

When adding OpenAI/ChatGPT support:

```python
# New module: core/openai_translator.py
from core.translator_base import Translator

class OpenAITranslator(Translator):
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
    
    def translate(self, text: str, context: str = "") -> str:
        # OpenAI implementation
        pass
    
    def estimate_tokens(self, text: str) -> int:
        # Token counting logic
        pass
```

**No changes needed to**:
- `rst_protector.py` (RST handling is universal)
- `po_file_handler.py` (PO handling is universal)
- Main scripts (`translate_po_smart.py`, etc.)

**Only add**:
- New `core/openai_translator.py` class
- Configuration selection in `translate_config.json`
- Type dispatcher in main script

---

## Glossary Integration

The glossary (`guides/GLOSSARY.md`) is used to:
1. Preserve important English terms (FTC, QR code, etc.)
2. Ensure consistent translations across files
3. Prevent LLM from over-translating technical terms

**Format** (Markdown table):
```markdown
| English | 日本語 | Category |
|---------|--------|----------|
| FTC | FTC | Organization |
| Motor | モータ | Hardware |
```

**Usage in Translator**:
```python
glossary = {
    "FTC": "FTC",
    "Motor": "モータ"
}
translator = LocalLLMTranslator(glossary=glossary)
```

---

## Progress Tracking

The `data/translation_progress.json` file tracks:
- Completed files (relative paths)
- Failed files (with error details)
- Last update timestamp

**Structure**:
```json
{
  "completed": [
    "index.po",
    "overview/overview.po"
  ],
  "failed": [
    {
      "file": "error_prone.po",
      "error": "out of memory",
      "timestamp": "2026-01-13 10:30:00"
    }
  ],
  "last_updated": "2026-01-13 10:35:00"
}
```

**Workflow**:
- Batch translator reads progress on startup
- Skips already-completed files
- Updates progress after each file
- Allows resumption after interruption

---

## Maintenance Guidelines

### Adding a New Translator Backend

1. Create `core/new_service_translator.py`
2. Implement `Translator` abstract base class
3. Implement `translate()` and `estimate_tokens()`
4. Add tests in `tests/`
5. Update `translate_config.json` with configuration
6. Update main scripts to dispatch correctly

### Modifying RST Protection

1. Edit patterns in `core/rst_protector.py`
2. Add unit tests for new pattern
3. Test with real documentation (verify no Sphinx errors)
4. Document the pattern in this ARCHITECTURE.md

### Handling Translation Quality Issues

1. Add check to `core/quality_checker.py`
2. Log blocked entries to JSON
3. Provide guidance for manual fixes
4. Consider updating LLM prompt to prevent recurrence

---

## Legacy Code

See [LEGACY.md](./LEGACY.md) for detailed information about deprecated scripts and migration paths.

**Quick Summary**:
- Old translation scripts in `legacy/scripts/` are kept for reference
- Old guides in `legacy/guides/` document deprecated workflows
- No functionality is removed; use `core/` modules instead
- Migration is backward-compatible with existing PO files

---

## References

- [Sphinx Intl Documentation](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [reStructuredText Markup](https://www.docutils.sourceforge.io/rst.html)
- [gettext PO Format](https://www.gnu.org/software/gettext/manual/gettext.html#PO-Files)
- [FTC Docs Repository](https://github.com/FIRST-Tech-Challenge/ftcdocs)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [polib Python Library](https://polib.readthedocs.io/)

---

## Quick Start

### For Users

1. Follow [WORKFLOW.md](./WORKFLOW.md) — unchanged
2. Run the same scripts: `translate_po_smart.py`, `batch_translate_smart.py`
3. Everything works as before (backward compatible)

### For Contributors

1. Read this ARCHITECTURE.md for module structure
2. Review specific modules in `core/` for implementation details
3. Add new features by extending `core/` modules
4. Avoid modifying main scripts directly; modify `core/` instead

---

## Questions?

- **RST Protection issues?** → See `core/rst_protector.py` with detailed comments
- **Adding a new API?** → See "Future API Integration" section above
- **Deprecated code?** → See [LEGACY.md](./LEGACY.md)
- **Workflow questions?** → See [WORKFLOW.md](./WORKFLOW.md)
