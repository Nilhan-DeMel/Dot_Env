#!/usr/bin/env python3
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path

def get_workflow_runs(repo, limit=20):
    """Fetch workflow runs from GitHub API."""
    try:
        cmd = [
            'gh', 'api',
            f'repos/{repo}/actions/runs',
            '-f', f'per_page={limit}',
            '--jq', '.workflow_runs[] | {name: .name, conclusion: .conclusion, url: .html_url, created_at: .created_at}'
        ]
        result = subprocess.check_output(cmd).decode('utf-8')
        runs = []
        for line in result.strip().split('\n'):
            if line:
                runs.append(json.loads(line))
        return runs
    except Exception as e:
        print(f"Error fetching runs: {e}")
        return []

def generate_dashboard(repo_root):
    """Generate PRISTINE_STATUS.md"""
    head_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()
    remote = subprocess.check_output(['git', 'remote', 'get-url', 'origin']).decode('utf-8').strip()
    repo_name = remote.split('github.com/')[-1].replace('.git', '').strip()

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

    output = f"# 🛡️ Pristine Status Dashboard\n\n"
    output += f"> **Last Updated:** {timestamp}\n\n"

    output += f"## 📍 Repository State\n"
    output += f"- **HEAD:** `{head_hash}`\n"
    output += f"- **Tracked Files:** "
    try:
        count = subprocess.check_output(['git', 'ls-files'], stderr=subprocess.DEVNULL).decode('utf-8').count('\n') + 1
        output += f"{count}\n"
    except:
        output += "unknown\n"

    output += "\n## 🤖 Workflow Health\n\n"

    runs = get_workflow_runs(repo_name)

    # Group by workflow name, take latest
    latest_runs = {}
    for run in runs:
        name = run['name']
        if name not in latest_runs:
            latest_runs[name] = run

    output += "| Workflow | Status | Run | Time |\n"
    output += "|----------|--------|-----|------|\n"

    for name, run in sorted(latest_runs.items()):
        status_icon = "✅" if run['conclusion'] == 'success' else "❌" if run['conclusion'] == 'failure' else "⚠️"
        date = run['created_at'].split('T')[0]
        output += f"| **{name}** | {status_icon} {run['conclusion']} | [View Log]({run['url']}) | {date} |\n"

    output += "\n---\n"
    output += "*Generated automatically by `scripts/export-repo-health.py`*\n"

    docs_dir = Path(repo_root) / 'docs'
    docs_dir.mkdir(exist_ok=True)
    target = docs_dir / 'PRISTINE_STATUS.md'
    target.write_text(output, encoding='utf-8')
    print(f"Generated {target}")

if __name__ == "__main__":
    generate_dashboard(Path.cwd())
