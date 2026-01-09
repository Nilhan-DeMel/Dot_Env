# Chapter 05: Workflows: Complete Spec

## General Policy applied to ALL Workflows

- **Concurrency:** `group: ${{ github.workflow }}-${{ github.ref }}`, `cancel-in-progress: true`.
- **Permissions:** Explicitly defined or typically `contents: read`. `auto-fix` has `contents: write`.

---

## 1. Main Sanity

- **File:** `main-sanity.yml`
- **Trigger:** `push` (branches: main)
- **Purpose:** Fast feedback for commits to main.
- **Steps:** `checkout`, `setup-python`, `check-repo.py`, `repo-scan.py`.
- **Failure:** Main is broken. Immediate fix required.

## 2. Pre-commit Gate

- **File:** `pre-commit.yml`
- **Trigger:** `pull_request`, `workflow_dispatch`
- **Purpose:** Enforces `.pre-commit-config.yaml` checks on PRs.
- **Steps:** `pre-commit run --all-files`.
- **Note:** Runs on free GitHub Actions runners (not pre-commit.ci).

## 3. Full Audit

- **File:** `full-audit.yml`
- **Trigger:** `workflow_dispatch`
- **Purpose:** Manual trigger to run ALL heavy checks (Security, Lints, Health) at once.
- **Steps:** `check-repo`, `repo-scan`, `pre-commit`, `actionlint`.

## 4. Workflows for Linting & Quality

- **Actionlint:** (`actionlint.yml`) Checks workflow syntax. Path-filtered (`.github/workflows/**`).
- **Commit Lint:** (`commitlint.yml`) Enforces Conventional Commits.
- **MegaLinter:** (`megalinter.yml`) Comprehensive multi-language linting.
- **Reviewdog:** (`reviewdog.yml`) Adds PR annotations for markdown/actionlint failures.

## 5. Workflows for Security

- **Secret Scan:** (`secret-scan.yml`) Runs `gitleaks`. Weekly schedule & PRs.
- **Trivy Scan:** (`trivy.yml`) Vulnerability scanner for fs.
- **Scorecard:** (`scorecard.yml`) OSSF Scorecard analysis. Weekly schedule.

## 6. Workflows for Maintenance

- **Auto-Fix Maintenance:** (`auto-fix.yml`) Daily 00:00 UTC. Runs scripts and **commits changes** (e.g. formatting).
- **Repo Dashboard:** (`repo-dashboard.yml`) Daily 06:00 UTC. Generates health summary.
- **Scheduled Health:** (`scheduled-health.yml`) Daily 23:00 UTC. Redundant overlap with Dashboard/Auto-Fix (candidate for future pruning).

## 7. Workflows for Alerting

- **Failure Alert:** (`failure-alert.yml`)
  - **Trigger:** `workflow_run` (completed) on critical workflows.
  - **Condition:** If `conclusion == failure`.
  - **Action:** Opens/Updates a specific GitHub Issue ("🚨 Repo Health: FAILING").

## 8. Miscellaneous

- **Conflict Check:** (`conflict-check.yml`) Runs `repo-scan`/`check-repo` on PRs.
- **Pristine Checks:** (`pristine.yml`) Duplicate of Conflict Check (slated for removal).
- **Link Check:** (`link-check.yml`) Checks broken URLs in markdown.
- **Impact CI:** (`impact-ci.yml`) Calculates change impact (paths-filter) to skip jobs.
