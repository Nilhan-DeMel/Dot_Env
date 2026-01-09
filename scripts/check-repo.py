#!/usr/bin/env python3
"""
check-repo.py - Repository Health Checker

Validates repository structure, required files, and basic doc link integrity.

Usage:
    python scripts/check-repo.py

Exit codes:
    0 = All checks passed
    1 = One or more checks failed

Requirements:
    Python 3.6+ (stdlib only)
"""

import os
import sys
import re
from pathlib import Path


def get_repo_root():
    """Get repository root directory."""
    return Path(__file__).resolve().parent.parent


def check_required_files(root):
    """Check that required files exist."""
    required = [
        'README.md',
        'LICENSE',
        '.gitignore',
        '.editorconfig',
        '.gitattributes',
        'CONTRIBUTING.md',
        'SECURITY.md',
        'docs/INDEX.md',
        'docs/REPO_MAP.md',
    ]
    
    missing = []
    for f in required:
        if not (root / f).exists():
            missing.append(f)
    
    return missing


def check_doc_links(root):
    """Check that markdown links in docs resolve to existing files."""
    docs_dir = root / 'docs'
    if not docs_dir.exists():
        return ['docs/ directory missing']
    
    broken = []
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    for md_file in docs_dir.rglob('*.md'):
        content = md_file.read_text(encoding='utf-8', errors='ignore')
        for match in link_pattern.finditer(content):
            link_text, link_target = match.groups()
            
            # Skip external links and anchors
            if link_target.startswith(('http://', 'https://', '#', 'mailto:')):
                continue
            
            # Remove anchor from path
            target_path = link_target.split('#')[0]
            if not target_path:
                continue
            
            # Resolve relative to the markdown file's directory
            resolved = (md_file.parent / target_path).resolve()
            
            if not resolved.exists():
                rel_md = md_file.relative_to(root)
                broken.append(f"{rel_md}: {link_target}")
    
    return broken


def check_repo_scan():
    """Check that repo-scan.py runs without error."""
    root = get_repo_root()
    scan_script = root / 'scripts' / 'repo-scan.py'
    
    if not scan_script.exists():
        return ['scripts/repo-scan.py missing']
    
    # Try importing and running
    try:
        import subprocess
        result = subprocess.run(
            [sys.executable, str(scan_script)],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode != 0:
            return [f'repo-scan.py failed: {result.stderr[:100]}']
    except Exception as e:
        return [f'repo-scan.py error: {str(e)[:100]}']
    
    return []


def main():
    """Run all checks and report results."""
    root = get_repo_root()
    all_passed = True
    
    print("=" * 50)
    print("REPOSITORY HEALTH CHECK")
    print("=" * 50)
    print(f"Root: {root}\n")
    
    # Check 1: Required files
    print("[1] Required files...")
    missing = check_required_files(root)
    if missing:
        print(f"    ❌ FAIL: Missing {len(missing)} files:")
        for f in missing:
            print(f"       - {f}")
        all_passed = False
    else:
        print("    ✅ PASS: All required files present")
    
    # Check 2: Doc links
    print("\n[2] Documentation links...")
    broken = check_doc_links(root)
    if broken:
        print(f"    ⚠️  WARN: {len(broken)} broken links:")
        for b in broken[:10]:  # Limit output
            print(f"       - {b}")
        if len(broken) > 10:
            print(f"       ... and {len(broken) - 10} more")
        # Don't fail on broken links, just warn
    else:
        print("    ✅ PASS: All doc links resolve")
    
    # Check 3: repo-scan.py
    print("\n[3] repo-scan.py...")
    errors = check_repo_scan()
    if errors:
        print(f"    ❌ FAIL: {errors[0]}")
        all_passed = False
    else:
        print("    ✅ PASS: repo-scan.py runs successfully")
    
    # Summary
    print("\n" + "=" * 50)
    if all_passed:
        print("RESULT: ✅ All checks passed")
        return 0
    else:
        print("RESULT: ❌ Some checks failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
