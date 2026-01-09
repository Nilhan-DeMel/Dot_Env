#!/usr/bin/env python3
import subprocess
import os
from pathlib import Path

def get_repo_info():
    root = Path(__file__).resolve().parent.parent
    os.chdir(root)

    remote = subprocess.check_output(['git', 'remote', '-v']).decode('utf-8')
    branch = subprocess.check_output(['git', 'branch', '--show-current']).decode('utf-8').strip()
    log_graph = subprocess.check_output(['git', 'log', '--graph', '--oneline', '--decorate', '--all', '--date=short', '--pretty=format:%h %ad %s (%an)']).decode('utf-8')
    full_stats = subprocess.check_output(['git', 'log', '--stat']).decode('utf-8')

    head_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()
    timestamp = subprocess.check_output(['git', 'show', '-s', '--format=%ci', 'HEAD']).decode('utf-8').strip()

    output = f"# 📜 Repository History Export\n\n"
    output += f"## ℹ️ Metadata\n"
    output += f"- **Generated:** `{timestamp}`\n"
    output += f"- **Commit:** `{head_hash}`\n"
    output += f"- **Current Branch:** `{branch}`\n"
    output += f"- **Remotes:**\n```text\n{remote}```\n\n"

    output += f"## 📈 Commit Graph\n"
    output += f"```text\n{log_graph}\n```\n\n"

    output += f"## 📄 Detailed Commit History\n"
    output += f"```text\n{full_stats}\n```\n"

    docs_dir = root / 'docs'
    docs_dir.mkdir(exist_ok=True)

    target = docs_dir / 'REPO_HISTORY.md'
    target.write_text(output, encoding='utf-8')
    print(f"Generated {target}")

if __name__ == "__main__":
    get_repo_info()
