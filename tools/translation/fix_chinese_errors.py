#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国語混入箇所の自動修正スクリプト

detect_chinese_chars.pyで検出された問題箇所を、
Ollamaを使って英語から正しい日本語に再翻訳します。
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional
import polib
import ollama
from tqdm import tqdm
from colorama import Fore, Style, init

# Windows対応: UTF-8出力
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Colorama初期化
init(autoreset=True)

# デフォルト設定
DEFAULT_CONFIG = {
    "model": "qwen2.5:7b-instruct-q5_K_M",
    "temperature": 0.3,
    "max_retries": 3,
    "skip_already_fixed": True,
}


def load_config(config_path: Path) -> Dict:
    """設定ファイルを読み込む"""
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            return {**DEFAULT_CONFIG, **config}
    return DEFAULT_CONFIG


def load_glossary() -> str:
    """用語集を読み込む"""
    glossary_path = Path(__file__).parents[2] / 'guides' / 'GLOSSARY.md'
    if glossary_path.exists():
        with open(glossary_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


def translate_with_ollama(text: str, model: str, temperature: float = 0.3, glossary: str = "") -> Optional[str]:
    """
    Ollamaを使って英語から日本語に翻訳
    
    Args:
        text: 翻訳する英語テキスト
        model: 使用するOllamaモデル名
        temperature: 生成温度（低いほど安定）
        glossary: 用語集（GLOSSARY.md）
    
    Returns:
        翻訳された日本語テキスト、失敗時はNone
    """
    
    glossary_section = ""
    if glossary:
        glossary_section = f"""
TRANSLATION GLOSSARY (MUST FOLLOW):
{glossary}

Strictly follow the glossary for all technical terms and proper nouns.
"""
    
    # 翻訳プロンプト（中国語を避けるように明示）
    prompt = f"""You are a professional English to Japanese translator specializing in technical documentation for FIRST Tech Challenge robotics competition.

CRITICAL TRANSLATION RULES:
1. Translate ONLY into proper Japanese (日本語)
2. NEVER use Simplified Chinese characters (简体字)
3. Use correct Japanese technical terms from the glossary
4. Maintain RST/Sphinx markup exactly as-is
5. Keep proper nouns in English when appropriate
6. Use です・ます tone (polite form)
{glossary_section}
FORBIDDEN CHINESE:
- Chinese expressions: 为了, 对于, 拥有, 姿态, 估计, 镜头, 校准, 通过, 提供, 只有...才, 可以通过, 甚至可以
- Simplified Chinese characters: 为, 拥, 态, 估, 镜, 头, 厅, 览, 购, 谁, 块, 际, 习, 远, 让, 边, 务, 验, 压, 担, 处, 团, 阶, 员, 调, 导, 测, 协, 围, 确, 阳, 养, 层, 双, 医, 审, 护, 坏, 优, 获, 临, 预, 规, 织, 奖, 随, 扩, 杂, 输, 维, 缺, 另, 评, 错, 须, 怀, 产, 业, 们, 发, 经, 应, 对, 时, 进, 实, 现, 动, 过, 问, 题

English text to translate:
{text}

Japanese translation (日本語のみ):"""

    try:
        response = ollama.generate(
            model=model,
            prompt=prompt,
            options={
                'temperature': 0.1,  # より保守的な翻訳（中国語混入を防ぐ）
                'top_p': 0.9,
                'top_k': 40,
            }
        )
        
        translation = response['response'].strip()
        
        # 簡体字チェック
        forbidden_chars = set('为拥态估镜头厅览购谁块际习远让边务验压担处团阶员调导测协围确阳养层双医审护坏优获临预规织奖随扩杂输维缺另评错须怀产业们发经应对时进实现动过问题两这关开间样级义变观认识议标环节农门战较续选传带广术极备组队费况质达资显响专旧尽')
        
        if any(char in translation for char in forbidden_chars):
            print(f"{Fore.YELLOW}⚠ Warning: Translation contains simplified Chinese characters, retrying...{Style.RESET_ALL}")
            return None
            
        return translation
        
    except Exception as e:
        print(f"{Fore.RED}✗ Translation error: {e}{Style.RESET_ALL}")
        return None


def scan_for_chinese_issues(po_files: List[Path]) -> Dict[Path, List[Dict]]:
    """
    POファイルをスキャンして中国語混入箇所を検出
    
    Returns:
        {po_file_path: [issue_dict, ...]} の辞書
    """
    # 簡体字特有の文字
    SIMPLIFIED_CHINESE_CHARS = set([
        '为', '拥', '态', '估', '镜', '头', '厅', '览', '购', '谁', '块', '际', 
        '习', '远', '让', '边', '务', '验', '压', '担', '处', '团', '阶', '员',
        '调', '导', '测', '协', '围', '确', '阳', '养', '层', '双', '医', '审',
        '护', '坏', '优', '获', '临', '预', '规', '织', '奖', '随', '扩', '杂',
        '输', '维', '缺', '另', '评', '错', '须', '怀', '产', '业', '们', '发',
        '经', '应', '对', '时', '进', '实', '现', '动', '过', '问', '题', '两',
        '这', '关', '开', '间', '样', '级', '义', '变', '观', '认', '识', '议',
        '标', '环', '节', '农', '门', '战', '较', '续', '选', '传', '带', '广',
        '术', '极', '备', '组', '队', '费', '况', '质', '达', '资', '显', '响',
        '专', '旧', '尽'
    ])
    
    # 中国語特有のパターン
    CHINESE_PATTERNS = [
        '为了', '对于', '的话', '通过', '拥有', '姿态', '估计', '镜头', '校准',
        '内在参数', '分辨率', '都需要', '可以通过', '甚至可以', '乃至', '亦即',
        '即可', '企图', '左侧', '右侧'
    ]
    
    results = {}
    
    for po_file in tqdm(po_files, desc="Scanning PO files"):
        try:
            po = polib.pofile(str(po_file))
            issues = []
            
            for entry in po:
                if not entry.msgstr:
                    continue
                    
                # 簡体字チェック
                has_simplified = any(char in entry.msgstr for char in SIMPLIFIED_CHINESE_CHARS)
                
                # パターンチェック
                has_pattern = any(pattern in entry.msgstr for pattern in CHINESE_PATTERNS)
                
                if has_simplified or has_pattern:
                    issues.append({
                        'msgid': entry.msgid,
                        'msgstr': entry.msgstr,
                        'linenum': entry.linenum,
                        'msgctxt': entry.msgctxt if hasattr(entry, 'msgctxt') else None,
                    })
            
            if issues:
                results[po_file] = issues
                
        except Exception as e:
            print(f"{Fore.RED}✗ Error scanning {po_file}: {e}{Style.RESET_ALL}")
    
    return results


def fix_chinese_issues(
    issues_dict: Dict[Path, List[Dict]],
    config: Dict,
    progress_file: Optional[Path] = None
) -> Dict:
    """
    検出された中国語混入箇所を修正
    
    Returns:
        統計情報の辞書
    """
    stats = {
        'total_issues': sum(len(issues) for issues in issues_dict.values()),
        'fixed': 0,
        'failed': 0,
        'skipped': 0,
    }
    
    # 進捗ファイルの読み込み
    progress = {}
    if progress_file and progress_file.exists():
        with open(progress_file, 'r', encoding='utf-8') as f:
            progress = json.load(f)
    
    # 用語集の読み込み
    print(f"{Fore.CYAN}Loading glossary...{Style.RESET_ALL}")
    glossary = load_glossary()
    if glossary:
        print(f"{Fore.GREEN}✓ Glossary loaded{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}⚠ Glossary not found, proceeding without it{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}中国語混入箇所の修正を開始{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
    print(f"対象ファイル数: {len(issues_dict)}")
    print(f"問題箇所総数: {stats['total_issues']}")
    print(f"使用モデル: {config['model']}\n")
    
    for po_file, issues in issues_dict.items():
        rel_path = str(po_file.relative_to(po_file.parents[4]))
        print(f"\n{Fore.BLUE}{'─'*60}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}📄 {rel_path}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{'─'*60}{Style.RESET_ALL}")
        
        try:
            po = polib.pofile(str(po_file))
            modified = False
            
            for issue in tqdm(issues, desc=f"Fixing {po_file.name}"):
                # スキップチェック
                issue_key = f"{po_file}:{issue['linenum']}"
                if config.get('skip_already_fixed') and progress.get(issue_key) == 'fixed':
                    stats['skipped'] += 1
                    continue
                
                # エントリを検索
                entry = None
                for e in po:
                    if e.msgid == issue['msgid'] and e.linenum == issue['linenum']:
                        entry = e
                        break
                
                if not entry:
                    print(f"{Fore.YELLOW}⚠ Entry not found at line {issue['linenum']}{Style.RESET_ALL}")
                    stats['failed'] += 1
                    continue
                
                # 翻訳実行（リトライ付き）
                translation = None
                for attempt in range(config['max_retries']):
                    translation = translate_with_ollama(
                        entry.msgid,
                        config['model'],
                        config['temperature']
                    )
                    if translation:
                        break
                    print(f"{Fore.YELLOW}⚠ Retry {attempt + 1}/{config['max_retries']}{Style.RESET_ALL}")
                
                if translation:
                    # 翻訳を適用
                    old_msgstr = entry.msgstr[:50] + "..." if len(entry.msgstr) > 50 else entry.msgstr
                    new_msgstr = translation[:50] + "..." if len(translation) > 50 else translation
                    
                    entry.msgstr = translation
                    modified = True
                    stats['fixed'] += 1
                    
                    # 進捗を保存
                    progress[issue_key] = 'fixed'
                    
                    print(f"{Fore.GREEN}✓ Line {issue['linenum']}: {old_msgstr} → {new_msgstr}{Style.RESET_ALL}")
                else:
                    stats['failed'] += 1
                    progress[issue_key] = 'failed'
                    print(f"{Fore.RED}✗ Line {issue['linenum']}: Translation failed{Style.RESET_ALL}")
            
            # POファイルを保存
            if modified:
                po.save()
                print(f"{Fore.GREEN}💾 Saved: {rel_path}{Style.RESET_ALL}")
            
            # 進捗ファイルを保存
            if progress_file:
                with open(progress_file, 'w', encoding='utf-8') as f:
                    json.dump(progress, f, ensure_ascii=False, indent=2)
                    
        except Exception as e:
            print(f"{Fore.RED}✗ Error processing {po_file}: {e}{Style.RESET_ALL}")
    
    return stats


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='中国語混入箇所を検出して正しい日本語に再翻訳'
    )
    parser.add_argument(
        '--po-dir',
        type=Path,
        default=Path('locales/ja/LC_MESSAGES'),
        help='POファイルのディレクトリ'
    )
    parser.add_argument(
        '--config',
        type=Path,
        default=Path('translate_config.json'),
        help='設定ファイルのパス'
    )
    parser.add_argument(
        '--progress',
        type=Path,
        default=Path('chinese_fix_progress.json'),
        help='進捗ファイルのパス'
    )
    parser.add_argument(
        '--model',
        type=str,
        help='使用するOllamaモデル（設定ファイルより優先）'
    )
    parser.add_argument(
        '--no-skip',
        action='store_true',
        help='修正済みの箇所も再実行'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='実際には変更せず検出のみ'
    )
    
    args = parser.parse_args()
    
    # ワークスペースルート
    workspace_root = Path(__file__).resolve().parents[2]
    os.chdir(workspace_root)
    
    # 設定読み込み
    config = load_config(args.config)
    if args.model:
        config['model'] = args.model
    if args.no_skip:
        config['skip_already_fixed'] = False
    
    # POファイルを収集
    po_dir = workspace_root / args.po_dir
    if not po_dir.exists():
        print(f"{Fore.RED}✗ Directory not found: {po_dir}{Style.RESET_ALL}")
        sys.exit(1)
    
    po_files = list(po_dir.rglob('*.po'))
    print(f"{Fore.CYAN}Found {len(po_files)} PO files{Style.RESET_ALL}\n")
    
    # 中国語混入箇所をスキャン
    print(f"{Fore.CYAN}Scanning for Chinese characters...{Style.RESET_ALL}")
    issues_dict = scan_for_chinese_issues(po_files)
    
    if not issues_dict:
        print(f"\n{Fore.GREEN}✓ No Chinese characters found! All files are clean.{Style.RESET_ALL}")
        sys.exit(0)
    
    print(f"\n{Fore.YELLOW}Found issues in {len(issues_dict)} files{Style.RESET_ALL}")
    total_issues = sum(len(issues) for issues in issues_dict.values())
    print(f"{Fore.YELLOW}Total issues: {total_issues}{Style.RESET_ALL}\n")
    
    if args.dry_run:
        print(f"{Fore.CYAN}Dry run mode - no changes will be made{Style.RESET_ALL}")
        for po_file, issues in issues_dict.items():
            rel_path = str(po_file.relative_to(workspace_root))
            print(f"\n{rel_path}: {len(issues)} issues")
            for issue in issues[:3]:  # 最初の3件のみ表示
                # Windows対応: エンコーディングエラーを回避
                try:
                    msgstr_preview = issue['msgstr'][:60] + "..." if len(issue['msgstr']) > 60 else issue['msgstr']
                    print(f"  Line {issue['linenum']}: {msgstr_preview}")
                except UnicodeEncodeError:
                    print(f"  Line {issue['linenum']}: [contains non-printable characters]")
        sys.exit(0)
    
    # Ollamaの動作確認
    try:
        print(f"{Fore.CYAN}Checking Ollama connection...{Style.RESET_ALL}")
        ollama.list()
        print(f"{Fore.GREEN}✓ Ollama is running{Style.RESET_ALL}\n")
    except Exception as e:
        print(f"{Fore.RED}✗ Ollama error: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Make sure Ollama is running: ollama serve{Style.RESET_ALL}")
        sys.exit(1)
    
    # 修正実行
    stats = fix_chinese_issues(
        issues_dict,
        config,
        args.progress if not args.dry_run else None
    )
    
    # 最終統計
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}修正完了{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
    print(f"総問題箇所: {stats['total_issues']}")
    print(f"{Fore.GREEN}✓ 修正成功: {stats['fixed']}{Style.RESET_ALL}")
    print(f"{Fore.RED}✗ 修正失敗: {stats['failed']}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}⊘ スキップ: {stats['skipped']}{Style.RESET_ALL}")
    
    success_rate = (stats['fixed'] / stats['total_issues'] * 100) if stats['total_issues'] > 0 else 0
    print(f"\n成功率: {success_rate:.1f}%")
    
    if stats['failed'] > 0:
        print(f"\n{Fore.YELLOW}⚠ 一部の翻訳に失敗しました。--no-skip オプションで再試行できます。{Style.RESET_ALL}")


if __name__ == '__main__':
    main()
