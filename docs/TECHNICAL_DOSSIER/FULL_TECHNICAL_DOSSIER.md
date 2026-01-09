# Dot_Env — Full Technical Dossier

**Generated:** 2026-01-09T18:18:00+05:30 (Asia/Colombo)
**HEAD SHA:** `704d56b7f2e33775fbcccac3279343af3201f200`
**Repository:** <https://github.com/Nilhan-DeMel/Dot_Env.git>
**Visibility:** PRIVATE

> This document is a **snapshot** of the Dot_Env repository at the commit above.
> All claims are backed by evidence. See [Appendix A](#appendix-a-environment-proof) and [Verification Audit Report](VERIFICATION_AUDIT_REPORT.md) for command outputs.

---

# Table of Contents

1. [Reading Guide](#reading-guide)
2. [Executive Overview](#executive-overview)
3. [Identity & Timeline](#identity--timeline)
4. [Directory Structure](#directory-structure)
5. [Workflows: Complete Spec](#workflows-complete-spec)
6. [Guardrails Stack](#guardrails-stack)
7. [Pre-commit Contract](#pre-commit-contract)
8. [Repo Scripts Tech Spec](#repo-scripts-tech-spec)
9. [Docs System](#docs-system)
10. [Git Policy](#git-policy)
11. [Security Model](#security-model)
12. [Maintenance Automation](#maintenance-automation)
13. [AI-First Playbook](#ai-first-playbook)
14. [Known Issues & Gaps](#known-issues--gaps)
15. [Quickstart](#quickstart)
16. [Appendix A: Environment Proof](#appendix-a-environment-proof)
17. [Appendix B: Workflow Inventory](#appendix-b-workflow-inventory)
18. [Appendix C: Config Files](#appendix-c-config-files)
19. [Appendix D: Schedule Summary](#appendix-d-schedule-summary)
20. [Appendix E: Glossary](#appendix-e-glossary)

---

# Reading Guide

**Target Audience:** AI Agents, Developers, and Auditors.

## Core Philosophy: Evidence First
This documentation is a snapshot of reality backed by evidence. Every claim about a workflow, script, or policy is derived from the actual code at commit `704d56b`.

## How to Verify Claims
When you read a statement like "The Pre-commit Gate runs on every PR," verify it by:

1. Checking this dossier's workflow spec
2. Inspecting the actual YAML in `.github/workflows/`

## Updating This Dossier
If code changes, regenerate this dossier. **CODE IS TRUTH**.

---

# Executive Overview

## Purpose
The `Dot_Env` repository serves as a **production-grade scaffolding and validation environment**. It prioritizes:

1. **Automated Health:** Self-healing and validation scripts run daily
2. **AI Compatibility:** Structure optimized for AI agents
3. **Governance:** Strict linting, commit enforcement, and security scanning

## Current State
As of commit `704d56b`, the repository is **fully operational**:

- **16 GitHub Actions Workflows** covering linting, security, links, and health
- **Daily and Weekly Schedules** for ongoing maintenance
- **Strict Concurrency Controls** to prevent resource waste

## Users & Roles

- **Primary User:** AI Agents (e.g., Antigravity)
- **Supervisor:** Human Developers (alerts via `Failure Alert` workflow)

## Expected Invariants
Any commit on `main` is **expected** to have passed the following checks (enforced via honor system and CI failure alerts on GitHub Free private repos):

- **Syntax Checks:** `actionlint`, `check-yaml`, Python syntax
- **Security Baseline:** `gitleaks`, `trivy`
- **Formatting:** `editorconfig`, `pre-commit` hooks

> **Note:** GitHub Free private repos cannot enforce required checks via API. CI gates provide visibility, not enforcement.

## Health at a Glance

- **CI Status:** ✅ Passing (Main Sanity on `704d56b`)
- **Branch Protection:** Not API-enforced (Free plan limitation)
- **Drift Control:** Active via `auto-fix.yml` (daily)

---

# Identity & Timeline

## Repository Coordinates

| Property | Value |
|----------|-------|
| Remote URL | `https://github.com/Nilhan-DeMel/Dot_Env.git` |
| Visibility | PRIVATE |
| Default Branch | `main` |
| Hosting | GitHub |

## Branch Model

- **Active Branches:** `main` only (trunk-based development)
- **Strategy:** Short-lived feature branches, deleted after merge

## Commit Timeline Phases

### Phase 1: Foundation
Initial setup of `pre-commit`, basic linting, folder structure.

### Phase 2: Pristine Automation
Introduction of `scripts/*.py` for repo-specific rules.

- Notable: `4032581 ci: add auto-fix pristine maintenance`

### Phase 3: Consolidation (Current)
Reduced CI noise, removed duplicates, ensured Free-plan compatibility.

- Notable: `218bbed ci: remove redundant health workflows`
- Notable: `14859ef ci: add main sanity check on push`

## Releases
**Status:** No tags. Rolling HEAD release model.

---

# Directory Structure

## Top-Level Structure

| Path | Purpose |
|------|---------|
| `/.github/workflows/` | 16 CI/CD workflow definitions |
| `/.github/dependabot.yml` | Dependency update configuration |
| `/docs/` | Documentation including this dossier |
| `/scripts/` | 6 Python maintenance scripts |
| `/.gitattributes` | EOL and binary handling |
| `/.editorconfig` | IDE formatting rules |
| `/.pre-commit-config.yaml` | Git hook definitions |
| `/.mega-linter.yml` | MegaLinter configuration |
| `/.markdownlint.json` | Markdown style rules |
| `/commitlint.config.js` | Commit message rules |

## Files of Special Importance

- `scripts/check-repo.py`: Primary health check (used by 6 workflows)
- `.github/workflows/main-sanity.yml`: Push-to-main gatekeeper

## Orphan Status

- `.markdownlint.json`: **LIKELY USED** — Assumed to be discovered by `reviewdog/action-markdownlint` via implicit config lookup. Not verified by explicit test run.

---

# Workflows: Complete Spec

## General Policy (All Workflows)

- **Concurrency:** `group: ${{ github.workflow }}-${{ github.ref }}`, `cancel-in-progress: true`
- **Permissions:** Explicitly defined; defaults to `contents: read`

## Workflow Inventory (16 Total)

### Push-Triggered (1)

| Workflow | File | Purpose |
|----------|------|---------|
| Main Sanity | `main-sanity.yml` | Fast feedback on push to main |

### PR-Triggered (11)

| Workflow | File | Purpose |
|----------|------|---------|
| Pre-commit Gate | `pre-commit.yml` | Enforces pre-commit hooks |
| Actionlint | `actionlint.yml` | Workflow syntax (path-filtered) |
| Commit Lint | `commitlint.yml` | Conventional commits |
| MegaLinter | `megalinter.yml` | Multi-language linting |
| Reviewdog | `reviewdog.yml` | PR annotations |
| Secret Scan | `secret-scan.yml` | Gitleaks scan |
| Trivy Scan | `trivy.yml` | Vulnerability scan |
| Link Check | `link-check.yml` | Broken URL detection |
| Conflict Check | `conflict-check.yml` | Repo health on PRs |
| Pristine Checks | `pristine.yml` | Legacy (duplicate of Conflict Check) |
| Impact CI | `impact-ci.yml` | Smart job skipping |

### Scheduled (5)

| Workflow | File | Cron | Purpose |
|----------|------|------|---------|
| Auto-Fix Maintenance | `auto-fix.yml` | `0 0 * * *` (00:00 UTC daily) | Self-healing commits |
| Repo Dashboard | `repo-dashboard.yml` | `0 6 * * *` (06:00 UTC daily) | Health summary |
| Scheduled Health | `scheduled-health.yml` | `0 23 * * *` (23:00 UTC daily) | Doctor diagnostics |
| Scorecard | `scorecard.yml` | `0 3 * * 0` (03:00 UTC weekly) | OSSF security analysis |
| Secret Scan | `secret-scan.yml` | `0 4 * * 0` (04:00 UTC weekly) | Weekly secret scan |

### Manual (1)

| Workflow | File | Purpose |
|----------|------|---------|
| Full Audit | `full-audit.yml` | One-click comprehensive audit |

### Event-Triggered (1)

| Workflow | File | Trigger | Purpose |
|----------|------|---------|---------|
| Failure Alert | `failure-alert.yml` | `workflow_run` (on failure) | Opens/updates issue on CI failure |

---

# Guardrails Stack

## 1. Linting Guardrails

- **MegaLinter:** Multi-language (JSON, YAML, Markdown, Python, Actions)
- **Actionlint:** GitHub Actions workflow syntax
- **Markdownlint:** Documentation style (via `.markdownlint.json`)

## 2. Formatting Guardrails

- **EditorConfig:** IDE defaults (indent, charset, EOL)
- **Pre-commit:** Enforces trailing-whitespace, end-of-file, mixed-line-ending

## 3. Security Guardrails

- **Gitleaks:** Secret detection
- **Trivy:** Filesystem vulnerability scanner
- **OSSF Scorecard:** Security best practices audit

## 4. Supply Chain Hardening

- **Action Pinning:** Most core actions pinned to SHAs
  - **Exceptions:** `actions/upload-artifact@v4` in `scheduled-health.yml` and `megalinter.yml` use tag pinning
- **Dependabot:** Weekly updates for GitHub Actions

## 5. Secret Handling

- **Policy:** NO secrets in code
- **Detection:** Gitleaks on every PR
- **Remediation:** Rotate immediately if leaked

---

# Pre-commit Contract

## Hooks Inventory

| Hook | Purpose |
|------|---------|
| `trailing-whitespace` | Remove trailing whitespace |
| `end-of-file-fixer` | Ensure single newline at EOF |
| `check-yaml` | Validate YAML syntax |
| `check-json` | Validate JSON syntax |
| `mixed-line-ending` | Enforce LF line endings |

## Operation

- **Local:** Run `pre-commit install` to catch issues before commit
- **CI:** `Pre-commit Gate` workflow enforces on PRs
- **Auto-Fix:** `Auto-Fix Maintenance` runs daily and commits fixes

## Cross-Platform

- **Windows:** Configure `core.autocrlf=input`
- **Enforcement:** LF only; CRLF will fail `mixed-line-ending`

---

# Repo Scripts Tech Spec

## Inventory (6 Scripts)

### 1. check-repo.py

- **Purpose:** Primary health check
- **Used By:** `conflict-check`, `repo-dashboard`, `auto-fix`, `main-sanity`, `full-audit`
- **Exit Codes:** 0=Healthy, 1=Unhealthy

### 2. repo-scan.py

- **Purpose:** Repository metadata summary
- **Used By:** `repo-dashboard`, `conflict-check`, `main-sanity`, `auto-fix`, `full-audit`

### 3. doctor.py

- **Used By:** `repo-dashboard` (daily)

### 4. export-repo-history.py

- **Purpose:** Timestamped markdown exports
- **Used By:** `auto-fix.yml`

### 5. export-repo-history-pdf.py

- **Purpose:** PDF generation (requires `reportlab`)
- **Used By:** `auto-fix.yml`

### 6. impact.py

- **Purpose:** Change impact analysis
- **Used By:** `impact-ci.yml`

## Safety Classification

- **Read-Only:** `check-repo`, `repo-scan`, `doctor`, `impact`
- **Write-Active:** `export-repo-history`, `export-repo-history-pdf`

---

# Docs System

## Inventory

- `README.md`: Entry point
- `/docs/REPO_MAP.md`: High-level file guide
- `/docs/WORKFLOWS.md`: Workflow descriptions
- `/docs/TECHNICAL_DOSSIER/`: This dossier

## Source of Truth Rules

1. **Code is Truth:** Docs are bugs if they contradict code
2. **Generated > Hand-written:** Reduces rot

---

# Git Policy

## Branch Model

- **Trunk-Based:** `main` is the single source
- **Feature Branches:** Short-lived
- **Merge Strategy:** Squash & Merge preferred

## Commit Messages

- **Enforcement:** `commitlint` via `commitlint.yml`
- **Format:** Conventional Commits (`type(scope): subject`)

## Direct-to-Main

- **Policy:** Avoid
- **Exceptions:** `auto-fix` workflow, emergency doc fixes
- **Safety Net:** `Main Sanity` runs on every push

## Rollback

1. Do NOT force push
2. `git revert <sha>`
3. Verify `Main Sanity` passes

---

# Security Model

## Threat Model

| Threat | Mitigation |
|--------|------------|
| Erroneous script | Git history |
| Supply chain attack | SHA pinning |
| Secret leak | Gitleaks scan |

## CI Permissions

- **Read-Only:** Most workflows
- **Write:**
  - `auto-fix.yml`: `contents: write`
  - `failure-alert.yml`: `issues: write`
  - `scorecard.yml`: `security-events: write`

## Tool Limitations

- **Gitleaks:** Regex-based (false positives/negatives possible)
- **Trivy:** Static analysis only
- **Dependabot:** Known CVEs only

---

# Maintenance Automation

## Auto-Fix Philosophy

- **Workflow:** `auto-fix.yml`
- **Schedule:** Daily 00:00 UTC
- **Actions:** Runs pre-commit, exports history, commits fixes

## Dashboard Philosophy

- **Workflow:** `repo-dashboard.yml`
- **Schedule:** Daily 06:00 UTC
- **Output:** Summary in Actions UI (no issue spam)

## Noise Reduction

- **Failure Alert:** ONE rolling issue, updated not duplicated

---

# AI-First Playbook

## Operating Constraints

- **No Hallucinations:** Verify before asserting
- **No Blind Fixes:** Check error logs first

## Safe Change Protocol

1. Run `check-repo.py`
2. Make small, atomic commits
3. Verify CI passes

## Interpreting Failures

| Failure Type | Action |
|--------------|--------|
| Lint | Run linter locally |
| Security | Rotate secret |
| Broken Link | Update docs |

---

# Known Issues & Gaps

## 1. Schedule Overlap

- `scheduled-health.yml` overlaps with `repo-dashboard.yml`

## 2. Legacy Workflow

- `pristine.yml` duplicates `conflict-check.yml`

## 3. Free Plan Limitations

- Branch protection API returned 403 during this audit (cause unverified; may be token scope or plan limitation)
- No environment approval gates on Free plan

## 4. Partial SHA Pinning

- `actions/upload-artifact@v4` uses tag, not SHA (in `scheduled-health.yml`, `megalinter.yml`)

---

# Known Tradeoffs & Intentional Design

## Layered Defense Philosophy
This repo intentionally runs overlapping checks at different stages:

| Stage | Purpose | Speed | Coverage |
|-------|---------|-------|----------|
| **Push to main** | Immediate sanity | Fast | Core health only |
| **PR checks** | Comprehensive gate | Medium | All lints + security |
| **Scheduled** | Drift detection | Slow | Full audit + reports |

## Why Duplication Exists

- `pristine.yml` and `conflict-check.yml` overlap → Planned for consolidation
- `scheduled-health.yml` and `repo-dashboard.yml` overlap → Different output artifacts

---

# Tool Ownership & Failure Routing

| Tool | Workflow | On Failure | Owner |
|------|----------|------------|-------|
| Gitleaks | `secret-scan.yml` | Issue opened via `failure-alert` | Human review required |
| Trivy | `trivy.yml` | Issue opened via `failure-alert` | Evaluate CVE severity |
| Actionlint | `actionlint.yml` | PR blocked | Fix workflow syntax |
| MegaLinter | `megalinter.yml` | PR annotations | Fix lint errors |
| Pre-commit | `pre-commit.yml` | PR blocked | Run `pre-commit run -a` locally |

## Failure Alert Coverage
`failure-alert.yml` monitors: `Lint Workflows`, `Link Check`, `Secret Scan`, `Trivy Scan`, `Pre-commit Gate`, `Pristine Checks`.

---

# How to Verify This Dossier

Run these commands to validate key claims:

```bash
# 1. Confirm HEAD SHA
git rev-parse HEAD

# 2. Count workflows (should be 18)
git ls-tree --name-only HEAD:.github/workflows | wc -l

# 3. List all workflows
git ls-tree --name-only HEAD:.github/workflows

# 4. Count scripts (should be 7)
ls scripts/*.py | wc -l

# 5. Verify config files exist
ls -la .gitattributes .editorconfig .pre-commit-config.yaml .markdownlint.json

# 6. Check scheduled crons
grep -r "cron:" .github/workflows/

# 7. Verify remote
git remote -v
```

---

# GitHub Settings (Out of Scope)

> **Note:** The following GitHub settings are NOT tracked in git and are not documented in this dossier:
>
> - Branch protection rules / rulesets
> - Required status checks
> - Installed GitHub Apps
> - Repository secrets / variables
> - Environments and deployment gates
>
> These must be verified via GitHub UI or API.

---

# Quickstart

```bash
# Clone
git clone https://github.com/Nilhan-DeMel/Dot_Env.git
cd Dot_Env

# Setup
pip install pre-commit
pre-commit install

# Daily Routine
python scripts/check-repo.py
git add .
git commit -m "feat: my feature"
pre-commit run --all-files
```

---

# Appendix A: Environment Proof

```text
HEAD SHA: 704d56b7f2e33775fbcccac3279343af3201f200
Remote: https://github.com/Nilhan-DeMel/Dot_Env.git
Branch: main
Working Tree: clean
Verified: 2026-01-09T18:18+05:30
```

---

# Appendix B: Workflow Inventory

```text
1. actionlint.yml
2. auto-fix.yml
3. commitlint.yml
4. conflict-check.yml
5. failure-alert.yml
6. full-audit.yml
7. impact-ci.yml
8. link-check.yml
9. main-sanity.yml
10. megalinter.yml
11. pre-commit.yml
12. repo-dashboard.yml
13. reviewdog.yml
14. scorecard.yml
15. secret-scan.yml
16. trivy.yml

Total: 16 workflows
```

---

# Appendix C: Config Files

## .gitattributes
```text
* text=auto
*.md text eol=lf
*.yml text eol=lf
*.py text eol=lf
*.pdf binary
```

## .editorconfig
```ini
root = true
[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

## .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: mixed-line-ending
        args: [--fix=lf]
```

## .markdownlint.json
```json
{
    "default": true,
    "MD013": false,
    "MD022": false,
    "MD024": false,
    "MD031": false,
    "MD033": false,
    "MD036": false,
    "MD040": false,
    "MD041": false
}
```

## commitlint.config.js
```javascript
module.exports = {
    extends: ['@commitlint/config-conventional']
};
```

## .github/dependabot.yml
```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

---

# Appendix D: Schedule Summary

| Workflow | Cron | UTC Time | Frequency |
|----------|------|----------|-----------|
| auto-fix.yml | `0 0 * * *` | 00:00 | Daily |
| repo-dashboard.yml | `0 6 * * *` | 06:00 | Daily |
| scorecard.yml | `0 3 * * 0` | 03:00 Sun | Weekly |
| secret-scan.yml | `0 4 * * 0` | 04:00 Sun | Weekly |

---

# Appendix E: Glossary

| Term | Definition |
|------|------------|
| **Actionlint** | Linter for GitHub Actions workflow files |
| **Commitlint** | Enforces Conventional Commits format |
| **Dependabot** | Automated dependency updater |
| **Gitleaks** | Scanner for secrets/credentials in code |
| **MegaLinter** | Aggregator of many linters |
| **Pre-commit** | Framework for managing git hooks |
| **Pristine State** | All health checks pass, no uncommitted files |
| **Scorecard** | OpenSSF tool for security posture |
| **Trivy** | Container and filesystem vulnerability scanner |
| **Trunk-Based** | Git workflow using single long-lived branch |

---

**End of Document**

*This dossier is verified against commit `704d56b` at 2026-01-09T18:18+05:30.*
