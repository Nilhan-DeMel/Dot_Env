# Chapter 14: Known Issues & Gaps

## 1. Confirmed Duplications
(Evidence: Workflows Spec)

- `scheduled-health.yml` overlaps significantly with `repo-dashboard.yml`. Both run daily and check health. Consolidation is planned.

## 2. Orphan Files
(Evidence: `check-repo.py` & Directory Structure)

- `.markdownlint.json`: Configuration exists, but the dedicated `markdownlint.yml` workflow was removed. It is currently used by `reviewdog` but lacks a dedicated "local runner" definition in `package.json` or similar.

## 3. Free Plan Limitations

- **Branch Protection:** Cannot enforce "Required Checks" via API on private/free repos. We rely on "Honor System" + CI Failure Alerts.
- **Environments:** No approval gates for deployment.

## 4. Unpinned Actions
(Evidence: `scorecard` output history)

- Most core actions are pinned to SHA (Good).
- Some third-party actions in `megalinter` or `reviewdog` might resolve dependencies dynamically.
