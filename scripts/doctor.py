#!/usr/bin/env python3
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

class Doctor:
    def __init__(self):
        self.report = []
        self.findings = []
        self.repo_root = Path(__file__).resolve().parent.parent

    def run_check(self, name, cmd, allow_fail=False):
        """Run a check command and record result."""
        print(f"Running {name}...", end='', flush=True)
        start = datetime.now()
        try:
            result = subprocess.run(
                cmd,
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=False,
                shell=True if sys.platform == 'win32' else False
            )
            duration = (datetime.now() - start).total_seconds()

            success = result.returncode == 0
            status = "PASS" if success else ("WARN" if allow_fail else "FAIL")
            icon = "✅" if success else ("⚠️" if allow_fail else "❌")

            print(f" {status}")

            self.report.append({
                'name': name,
                'status': status,
                'icon': icon,
                'duration': f"{duration:.2f}s",
                'code': result.returncode,
                'output': result.stdout + result.stderr
            })

            if not success:
                self.extract_findings(name, result.stdout + result.stderr)

            return success
        except Exception as e:
            self.report.append({
                'name': name,
                'status': "ERROR",
                'icon': "💥",
                'duration': "0.00s",
                'code': -1,
                'output': str(e)
            })
            print(" ERROR")
            return False

    def extract_findings(self, name, output):
        """Extract simplified findings from output."""
        lines = output.splitlines()
        count = 0
        for line in lines:
            if count >= 5: break
            if "error" in line.lower() or "fail" in line.lower() or "warn" in line.lower():
                self.findings.append(f"[{name}] {line.strip()}")
                count += 1

    def generate_report(self):
        """Generate markdown report."""
        head_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=self.repo_root).decode().strip()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

        md = f"# 🩺 Doctor Report\n\n"
        md += f"- **Date:** {timestamp}\n"
        md += f"- **HEAD:** `{head_hash}`\n\n"

        md += "## Summary\n\n"
        md += "| Check | Status | Duration | Code |\n"
        md += "|-------|--------|----------|------|\n"

        all_passed = True
        for item in self.report:
            md += f"| {item['name']} | {item['icon']} {item['status']} | {item['duration']} | `{item['code']}` |\n"
            if item['status'] == 'FAIL':
                all_passed = False

        if self.findings:
            md += "\n## 🕵️ Key Findings (Top Issue Samples)\n\n"
            for finding in self.findings:
                md += f"- `{finding}`\n"

        md += "\n## 📝 Detailed Logs\n\n"
        md += "<details><summary>Click to view full logs</summary>\n\n"
        for item in self.report:
            md += f"### {item['name']}\n"
            md += f"```text\n{item['output'][:2000]}\n```\n"
            if len(item['output']) > 2000:
                md += "*...output truncated...*\n"
        md += "\n</details>\n"

        docs_dir = self.repo_root / 'docs'
        docs_dir.mkdir(exist_ok=True)
        (docs_dir / 'DOCTOR_REPORT.md').write_text(md, encoding='utf-8')
        print(f"\nReport written to {docs_dir / 'DOCTOR_REPORT.md'}")

        return all_passed

def main():
    doc = Doctor()

    # 1. Repo Structure
    doc.run_check("Repo Scan", ["python", "scripts/repo-scan.py"])

    # 2. Repo Health
    doc.run_check("Check Repo", ["python", "scripts/check-repo.py"])

    # 3. Hygiene (Pre-commit)
    doc.run_check("Pre-commit Hygiene", ["pre-commit", "run", "-a"], allow_fail=True)

    # 4. Impact Analysis
    doc.run_check("Impact Analysis", ["python", "scripts/impact.py"])

    if not doc.generate_report():
        sys.exit(1)

if __name__ == "__main__":
    main()
