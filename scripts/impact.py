#!/usr/bin/env python3
import sys
import subprocess
import json
from pathlib import Path

def get_changed_files(base_ref, head_ref):
    """Get list of changed files between refs."""
    try:
        cmd = ['git', 'diff', '--name-only', base_ref, head_ref]
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode('utf-8')
        return [f for f in output.split('\n') if f.strip()]
    except subprocess.CalledProcessError:
        return []

def analyze_impact(files):
    """Analyze which components are impacted."""
    impact = {
        'docs': False,
        'workflow': False,
        'python': False,
        'frontend': False,
        'core': False,
        'all': False
    }

    if not files:
        impact['all'] = True
        return impact

    for f in files:
        p = Path(f)
        parts = p.parts
        ext = p.suffix

        if 'docs' in parts or ext == '.md':
            impact['docs'] = True

        if '.github' in parts or ext in ['.yml', '.yaml']:
            impact['workflow'] = True

        if ext == '.py' or 'scripts' in parts:
            impact['python'] = True

        if ext in ['.js', '.html', '.css']:
            impact['frontend'] = True

    # Critical paths that trigger everything
    critical = ['package.json', 'requirements.txt', '.pre-commit-config.yaml']
    if any(f in critical for f in files):
        impact['all'] = True

    return impact

def main():
    if len(sys.argv) < 3:
        # Default fallback
        base = 'origin/main'
        head = 'HEAD'
    else:
        base = sys.argv[1]
        head = sys.argv[2]

    changed = get_changed_files(base, head)
    impact = analyze_impact(changed)

    report = {
        'base': base,
        'head': head,
        'changed_files': len(changed),
        'impact': impact,
        'files': changed
    }

    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
