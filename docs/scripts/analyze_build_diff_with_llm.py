#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_structure_diff.txt をLLMに渡して、差分の意味合いを要約・リスク判定する
- Ollamaのモデルは translate_config.json の "model" を使用
"""

import json
from pathlib import Path
import sys

try:
    import ollama
except Exception as e:
    print('✗ ollama パッケージが必要です: pip install ollama', file=sys.stderr)
    sys.exit(1)

PROMPT_TEMPLATE = """
あなたはSphinxドキュメントのQAエンジニアです。以下の構造差分をレビューし、要約してください。

【目的】
- html(英語)とhtml-ja(日本語)の出力構造差を確認
- 日本語に不足しているページ、英語にのみ存在するページを指摘
- よくある原因（リンク切れ、翻訳欠落、conf差異など）を推測
- 緊急度を High/Medium/Low で評価
- 対応方針を箇条書きで提案

【差分】
```
{diff}
```

出力は日本語の要約で、箇条書き中心、簡潔にしてください。
"""


def load_model_name() -> str:
    cfg = Path('translate_config.json')
    if cfg.exists():
        data = json.loads(cfg.read_text(encoding='utf-8'))
        return data.get('model', 'qwen2.5:7b-instruct-q5_K_M')
    return 'qwen2.5:7b-instruct-q5_K_M'


def main():
    diff_path = Path('build_structure_diff.txt')
    if not diff_path.exists():
        print('⚠ build_structure_diff.txt が見つかりません。まず比較を実行してください。')
        sys.exit(1)
    diff_text = diff_path.read_text(encoding='utf-8')
    model = load_model_name()

    prompt = PROMPT_TEMPLATE.format(diff=diff_text)

    res = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        options={'temperature': 0.2, 'num_predict': 1024}
    )
    print('=== LLM解析結果 ===')
    print(res['message']['content'])

if __name__ == '__main__':
    main()
