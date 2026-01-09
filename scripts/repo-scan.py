#!/usr/bin/env python3
"""
repo-scan.py - Repository Structure Scanner

Scans the Dot_Env repository and outputs a summary of files and directories.
Can be used to refresh REPO_MAP.md documentation.

Usage:
    python scripts/repo-scan.py [--json] [--markdown]

Requirements:
    Python 3.6+ (stdlib only, no external dependencies)
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime


# Directories to exclude from scanning
EXCLUDE_DIRS = {'.git', 'node_modules', 'dist', 'build', '__pycache__', '.nyc_output', 'coverage'}

# File extensions to categorize
CATEGORIES = {
    'documentation': {'.md', '.txt', '.rst'},
    'configuration': {'.json', '.yaml', '.yml', '.toml', '.ini', '.editorconfig'},
    'source': {'.js', '.ts', '.py', '.go', '.rs', '.java'},
    'data': {'.csv', '.xml'},
}


def get_repo_root():
    """Get the repository root directory."""
    script_dir = Path(__file__).resolve().parent
    return script_dir.parent


def scan_directory(root_path, max_depth=4):
    """Scan directory and return file information."""
    files = []
    directories = []

    for item in sorted(root_path.rglob('*')):
        # Calculate depth
        try:
            relative = item.relative_to(root_path)
            depth = len(relative.parts)
        except ValueError:
            continue

        if depth > max_depth:
            continue

        # Skip excluded directories
        if any(excluded in item.parts for excluded in EXCLUDE_DIRS):
            continue

        rel_path = str(relative).replace('\\', '/')

        if item.is_file():
            try:
                stat = item.stat()
                files.append({
                    'path': rel_path,
                    'name': item.name,
                    'size': stat.st_size,
                    'extension': item.suffix.lower(),
                    'category': categorize_file(item.suffix.lower())
                })
            except (OSError, PermissionError):
                pass
        elif item.is_dir():
            directories.append({
                'path': rel_path,
                'name': item.name
            })

    return files, directories


def categorize_file(extension):
    """Categorize a file by its extension."""
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return 'other'


def detect_tech_stack(files):
    """Detect technology stack from files."""
    stack = []
    file_names = {f['name'] for f in files}

    if 'package.json' in file_names:
        stack.append('Node.js')
    if 'requirements.txt' in file_names or 'pyproject.toml' in file_names:
        stack.append('Python')
    if 'go.mod' in file_names:
        stack.append('Go')
    if 'Cargo.toml' in file_names:
        stack.append('Rust')
    if 'pom.xml' in file_names:
        stack.append('Java (Maven)')
    if 'Dockerfile' in file_names:
        stack.append('Docker')

    return stack if stack else ['None detected']


def generate_summary(files, directories, repo_root):
    """Generate a summary report."""
    return {
        'scan_time': datetime.now().isoformat(),
        'repo_root': str(repo_root),
        'total_files': len(files),
        'total_directories': len(directories),
        'total_size_bytes': sum(f['size'] for f in files),
        'tech_stack': detect_tech_stack(files),
        'files_by_category': count_by_key(files, 'category'),
        'files_by_extension': count_by_key(files, 'extension'),
    }


def count_by_key(items, key):
    """Count items grouped by a key."""
    counts = {}
    for item in items:
        value = item.get(key, 'unknown')
        counts[value] = counts.get(value, 0) + 1
    return counts


def output_json(files, directories, summary):
    """Output results as JSON."""
    result = {
        'summary': summary,
        'directories': directories,
        'files': files
    }
    print(json.dumps(result, indent=2))


def output_markdown(files, directories, summary):
    """Output results as Markdown."""
    print("# Repository Scan Results\n")
    print(f"**Scanned:** {summary['scan_time']}")
    print(f"**Root:** `{summary['repo_root']}`\n")

    print("## Summary\n")
    print(f"- **Files:** {summary['total_files']}")
    print(f"- **Directories:** {summary['total_directories']}")
    print(f"- **Total Size:** {summary['total_size_bytes']:,} bytes")
    print(f"- **Tech Stack:** {', '.join(summary['tech_stack'])}\n")

    print("## Files by Category\n")
    for category, count in sorted(summary['files_by_category'].items()):
        print(f"- {category}: {count}")

    print("\n## File List\n")
    print("| Path | Size | Category |")
    print("|------|------|----------|")
    for f in files:
        print(f"| `{f['path']}` | {f['size']} | {f['category']} |")


def output_text(files, directories, summary):
    """Output results as plain text."""
    print("=" * 60)
    print("REPOSITORY SCAN RESULTS")
    print("=" * 60)
    print(f"\nScanned: {summary['scan_time']}")
    print(f"Root: {summary['repo_root']}")
    print(f"\nTotal Files: {summary['total_files']}")
    print(f"Total Directories: {summary['total_directories']}")
    print(f"Tech Stack: {', '.join(summary['tech_stack'])}")
    print("\n" + "-" * 40)
    print(f"\nListing all {len(files)} files:")
    print("-" * 40)
    for f in files:
        print(f"  {f['path']} ({f['size']} bytes)")


def main():
    """Main entry point."""
    repo_root = get_repo_root()

    # Parse arguments
    output_format = 'text'
    if '--json' in sys.argv:
        output_format = 'json'
    elif '--markdown' in sys.argv:
        output_format = 'markdown'

    # Scan repository
    files, directories = scan_directory(repo_root)
    summary = generate_summary(files, directories, repo_root)

    # Output results
    if '--update' in sys.argv:
        # Generate markdown content
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            output_markdown(files, directories, summary)
        content = f.getvalue()

        # Write to REPO_MAP.md
        docs_dir = repo_root / 'docs'
        docs_dir.mkdir(exist_ok=True)
        (docs_dir / 'REPO_MAP.md').write_text(content, encoding='utf-8')
        print(f"Updated {docs_dir / 'REPO_MAP.md'}")

    elif output_format == 'json':
        output_json(files, directories, summary)
    elif output_format == 'markdown':
        output_markdown(files, directories, summary)
    else:
        output_text(files, directories, summary)

    return 0


if __name__ == '__main__':
    sys.exit(main())
