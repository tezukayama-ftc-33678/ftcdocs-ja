#!/usr/bin/env python3
"""
Token Estimator Module

Estimates token usage for text, useful for:
1. Cost estimation (for paid APIs like OpenAI)
2. Pre-flight validation (check if text fits in context window)
3. Planning and reporting

Different models use different tokenizers:
- OpenAI GPT models: ~4 characters per token
- Claude: ~3-4 characters per token
- Ollama: varies, but roughly 3-4 characters per token
- Gemini: ~3 characters per token

Always estimate conservatively (round up) to avoid surprises.
"""

from typing import Dict, Optional


class TokenEstimator:
    """
    Estimates token counts for different model families.
    """
    
    # Model families and their approximate char-to-token ratios
    # (conservative estimates - always round up)
    MODEL_RATIOS = {
        'gpt-4': 4.0,           # OpenAI GPT-4
        'gpt-3.5-turbo': 4.0,   # OpenAI GPT-3.5
        'claude': 3.5,          # Anthropic Claude
        'claude-3': 3.5,
        'gemini': 3.0,          # Google Gemini
        'qwen': 2.5,            # Ollama Qwen
        'llama': 3.0,           # Ollama Llama
        'mistral': 3.0,         # Ollama Mistral
    }
    
    # Pricing per 1K tokens (in USD)
    # Update as pricing changes
    PRICING = {
        'gpt-4-input': 0.03,
        'gpt-4-output': 0.06,
        'gpt-3.5-turbo-input': 0.0005,
        'gpt-3.5-turbo-output': 0.0015,
        'claude-3-opus-input': 0.015,
        'claude-3-opus-output': 0.075,
        'claude-3-sonnet-input': 0.003,
        'claude-3-sonnet-output': 0.015,
        'gemini-pro-input': 0.0,  # Free tier (as of 2024)
        'gemini-pro-output': 0.0,
    }
    
    @staticmethod
    def estimate_tokens(text: str, model: str = 'gpt-4') -> int:
        """
        Estimate token count for text.
        
        Args:
            text: Text to estimate
            model: Model name or family (e.g., 'gpt-4', 'claude', 'qwen')
        
        Returns:
            Estimated token count (rounded up)
        """
        if not text:
            return 0
        
        # Find matching model ratio
        ratio = 4.0  # Default conservative ratio
        
        for model_key, model_ratio in TokenEstimator.MODEL_RATIOS.items():
            if model_key.lower() in model.lower():
                ratio = model_ratio
                break
        
        # Estimate tokens: char count divided by ratio
        # Add 1 to round up (conservative)
        estimated_tokens = len(text) // ratio + 1
        
        return max(1, estimated_tokens)
    
    @staticmethod
    def estimate_cost(tokens: int, model: str = 'gpt-4',
                     input_tokens: Optional[int] = None,
                     output_tokens: Optional[int] = None) -> float:
        """
        Estimate API cost for token usage.
        
        Args:
            tokens: Total tokens (if input_tokens and output_tokens not provided)
            model: Model name
            input_tokens: Tokens in request (optional)
            output_tokens: Tokens in response (optional)
        
        Returns:
            Estimated cost in USD
        """
        if input_tokens is None:
            # Assume 50/50 split between input and output
            input_tokens = tokens // 2
            output_tokens = tokens - input_tokens
        
        cost = 0.0
        
        # Try to find matching pricing
        for pricing_key, price in TokenEstimator.PRICING.items():
            model_lower = model.lower()
            
            if 'input' in pricing_key and pricing_key.replace('-input', '') in model_lower:
                cost += (input_tokens / 1000) * price
            
            if 'output' in pricing_key and pricing_key.replace('-output', '') in model_lower:
                cost += (output_tokens / 1000) * price
        
        return cost
    
    @staticmethod
    def validate_context_window(text: str, model: str = 'gpt-4',
                               context_window: Optional[int] = None) -> bool:
        """
        Check if text fits within model's context window.
        
        Args:
            text: Text to check
            model: Model name
            context_window: Context window size (if not standard)
        
        Returns:
            True if text fits, False if it exceeds context window
        """
        # Standard context windows (in tokens)
        CONTEXT_WINDOWS = {
            'gpt-4': 8192,          # Standard GPT-4
            'gpt-4-turbo': 128000,  # GPT-4 Turbo
            'gpt-3.5-turbo': 4096,
            'claude-3-opus': 200000,
            'claude-3-sonnet': 200000,
            'gemini-pro': 32000,
            'qwen': 4096,           # Typical Ollama
            'llama': 4096,
        }
        
        if context_window is None:
            context_window = 8192  # Default conservative estimate
            
            for key, window in CONTEXT_WINDOWS.items():
                if key.lower() in model.lower():
                    context_window = window
                    break
        
        # Estimate tokens with margin (20% buffer)
        estimated_tokens = TokenEstimator.estimate_tokens(text, model)
        max_tokens = int(context_window * 0.8)  # 80% of window
        
        return estimated_tokens <= max_tokens
    
    @staticmethod
    def get_context_info(model: str) -> Dict[str, any]:
        """
        Get information about model context and costs.
        
        Args:
            model: Model name
        
        Returns:
            Dict with context_window, token_ratio, and estimated_prices
        """
        context_windows = {
            'gpt-4': 8192,
            'gpt-4-turbo': 128000,
            'gpt-3.5-turbo': 4096,
            'claude-3-opus': 200000,
            'claude-3-sonnet': 200000,
            'gemini-pro': 32000,
            'qwen': 4096,
            'llama': 4096,
        }
        
        context_window = 8192
        for key, window in context_windows.items():
            if key.lower() in model.lower():
                context_window = window
                break
        
        ratio = TokenEstimator.MODEL_RATIOS.get(
            model.lower().split('-')[0], 4.0
        )
        
        return {
            'model': model,
            'context_window': context_window,
            'token_ratio': ratio,  # chars per token
            'note': 'Estimate only - actual costs may vary',
        }
