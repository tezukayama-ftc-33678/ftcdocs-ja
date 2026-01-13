"""
Core Utility Modules

Provides core functionality for PO file translation pipeline:
- RST markup protection and restoration
- PO file I/O operations
- Quality checking (Chinese detection, Japanese validation)
- Token estimation for cost tracking

These modules are backend-agnostic and can be used with any translation implementation.

Architecture:
- rst_protector.py: RST markup extraction and restoration with Japanese spacing
- po_file_handler.py: Safe PO file reading/writing with msgid protection
- quality_checker.py: Translation quality validation
- token_estimator.py: Token counting and cost estimation

Note: Translation implementations are in the separate 'api' module.
"""

from .rst_protector import RSTProtector, split_into_chunks, should_skip_translation
from .po_file_handler import POFileHandler, POBatchHandler
from .quality_checker import QualityChecker
from .token_estimator import TokenEstimator

__all__ = [
    # RST Protection
    "RSTProtector",
    "split_into_chunks",
    "should_skip_translation",
    
    # PO File Handling
    "POFileHandler",
    "POBatchHandler",
    
    # Quality & Estimation
    "QualityChecker",
    "TokenEstimator",
]
