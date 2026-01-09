# Chapter 12: Maintenance Automation

## The "Auto-Fix" Philosophy
Instead of just failing CI, this repo attempts to fix itself where safe.

- **Workflow:** `auto-fix.yml`
- **Schedule:** Daily at **00:00 UTC**.
- **Scope:**
    1. Runs `pre-commit run --all-files` (fixes formatting).
    2. Runs `export-repo-history.py` (archives state).
    3. Commits changes with message `chore: automated pristine maintenance`.
- **Safety:** Stops if `pre-commit` fails in a way that isn't auto-fixable.

## The "Dashboard" Philosophy
Visibility drives health.

- **Workflow:** `repo-dashboard.yml`
- **Schedule:** Daily at **06:00 UTC**.
- **Scope:** Runs all read-only checks (`check-repo`, `repo-scan`).
- **Output:** Generates a Summary in the Actions UI. It does NOT automatically open an issue (to reduce noise).

## Reducing Noise

- **Failure Alert:** Only opens ONE issue ("🚨 Repo Health: FAILING"). It updates the existing issue rather than creating duplicates.
- **Log Retention:** Default GitHub retention (90 days). Artifacts from `scheduled-health.yml` are stored for historic analysis.
