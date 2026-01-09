# Workflows

**Last synced:** 2026-01-09T16:50:00Z | Commit: `135c555`

---

## Quick Map

### Runs on Pull Requests

- Lint Workflows (`actionlint.yml`)
- Commit Lint (`commitlint.yml`)
- Conflict Check (`conflict-check.yml`)
- Impact CI (`impact-ci.yml`)
- Link Check (`link-check.yml`)
- MegaLinter (`megalinter.yml`)
- Pre-commit Gate (`pre-commit.yml`)
- Reviewdog (`reviewdog.yml`)
- Secret Scan (`secret-scan.yml`)
- Trivy Scan (`trivy.yml`)

### Runs on Push to main

- Main Sanity (`main-sanity.yml`)

### Runs on Schedule

- Auto-Fix Maintenance (`auto-fix.yml`) — daily 00:00 UTC
- Repo Dashboard (`repo-dashboard.yml`) — daily 06:00 UTC
- Scorecard (`scorecard.yml`) — weekly Sun 03:00 UTC
- Secret Scan (`secret-scan.yml`) — weekly Sun 04:00 UTC

### Manual-only

- Full Audit (`full-audit.yml`)

### Workflow-run Alerts

- Failure Alert (`failure-alert.yml`) — triggers on monitored workflow failures

---

## Workflow Matrix

| File | Name | Triggers | Writes? | Primary Tools | Outputs |
|------|------|----------|---------|---------------|---------|
| actionlint.yml | Lint Workflows | PR, manual | none | actionlint | — |
| auto-fix.yml | Auto-Fix Maintenance | cron, manual | contents | pre-commit, export scripts | commits fixes |
| commitlint.yml | Commit Lint | PR, manual | none | commitlint | — |
| conflict-check.yml | Conflict Check | PR, manual | none | check-repo.py, repo-scan.py | — |
| failure-alert.yml | Failure Alert | workflow_run | issues | github-script | creates/updates issue |
| full-audit.yml | Full Audit | manual | none | check-repo, pre-commit, actionlint | — |
| impact-ci.yml | Impact CI | PR, manual | none | dorny/paths-filter | — |
| link-check.yml | Link Check | PR, manual | none | lychee | — |
| main-sanity.yml | Main Sanity | push(main) | none | check-repo.py, repo-scan.py | — |
| megalinter.yml | MegaLinter | PR, manual | none | megalinter | uploads artifact |
| pre-commit.yml | Pre-commit Gate | PR, manual | none | pre-commit | — |
| repo-dashboard.yml | Repo Dashboard | cron, manual | none | check-repo, repo-scan, doctor.py | uploads artifact |
| reviewdog.yml | Reviewdog | PR | none | reviewdog/actionlint, reviewdog/markdownlint | PR annotations |
| scorecard.yml | Scorecard | cron, manual | security-events | ossf/scorecard | uploads SARIF |
| secret-scan.yml | Secret Scan | PR, cron, manual | none | gitleaks | — |
| trivy.yml | Trivy Scan | PR, manual | none | trivy | — |

---

## Lint Workflows (actionlint.yml)

- **Triggers:** pull_request, workflow_dispatch
- **Paths filter:** `.github/workflows/**`
- **Concurrency:** yes
- **Permissions:** default (read)
- **Writes:** none
- **Tools:** actionlint
- **Outputs:** none

## Auto-Fix Maintenance (auto-fix.yml)

- **Triggers:** schedule (daily 00:00 UTC), workflow_dispatch
- **Concurrency:** yes
- **Permissions:** contents: write
- **Writes:** contents (commits fixes)
- **Tools:** pre-commit, export-repo-history.py, export-repo-history-pdf.py
- **Outputs:** commits to main

## Commit Lint (commitlint.yml)

- **Triggers:** pull_request, workflow_dispatch
- **Concurrency:** yes
- **Permissions:** default (read)
- **Writes:** none
- **Tools:** commitlint
- **Outputs:** none

## Conflict Check (conflict-check.yml)

- **Triggers:** pull_request, workflow_dispatch
- **Concurrency:** yes
- **Permissions:** default (read)
- **Writes:** none
- **Tools:** check-repo.py, repo-scan.py
- **Outputs:** none

## Failure Alert (failure-alert.yml)

- **Triggers:** workflow_run (on failure of monitored workflows)
- **Concurrency:** yes
- **Permissions:** issues: write, actions: read
- **Writes:** issues (creates/updates rolling issue)
- **Tools:** actions/github-script
- **Outputs:** issue titled "🚨 Repo Health: FAILING"

## Full Audit (full-audit.yml)

- **Triggers:** workflow_dispatch only
- **Concurrency:** yes
- **Permissions:** contents: read
- **Writes:** none
- **Tools:** check-repo.py, repo-scan.py, pre-commit, actionlint
- **Outputs:** none

## Impact CI (impact-ci.yml)

- **Triggers:** pull_request, workflow_dispatch
- **Concurrency:** yes
- **Permissions:** default (read)
- **Writes:** none
- **Tools:** dorny/paths-filter
- **Outputs:** none

## Link Check (link-check.yml)

- **Triggers:** pull_request, workflow_dispatch
- **Concurrency:** yes
- **Permissions:** default (read)
- **Writes:** none
- **Tools:** lychee
- **Outputs:** none

## Main Sanity (main-sanity.yml)

- **Triggers:** push (branches: main)
- **Concurrency:** yes
- **Permissions:** contents: read
- **Writes:** none
- **Tools:** check-repo.py, repo-scan.py
- **Outputs:** none

## MegaLinter (megalinter.yml)

- **Triggers:** pull_request, workflow_dispatch
- **Concurrency:** yes
- **Permissions:** contents: read, issues: write
- **Writes:** none
- **Tools:** oxsecurity/megalinter
- **Outputs:** uploads megalinter-reports artifact

## Pre-commit Gate (pre-commit.yml)

- **Triggers:** pull_request, workflow_dispatch
- **Concurrency:** yes
- **Permissions:** default (read)
- **Writes:** none
- **Tools:** pre-commit
- **Outputs:** none

## Repo Dashboard (repo-dashboard.yml)

- **Triggers:** schedule (daily 06:00 UTC), workflow_dispatch
- **Concurrency:** yes
- **Permissions:** contents: read, actions: read
- **Writes:** none
- **Tools:** check-repo.py, repo-scan.py, doctor.py, actionlint
- **Outputs:** uploads doctor-report artifact, writes GITHUB_STEP_SUMMARY

## Reviewdog (reviewdog.yml)

- **Triggers:** pull_request
- **Concurrency:** yes
- **Permissions:** contents: read
- **Writes:** none
- **Tools:** reviewdog/action-actionlint, reviewdog/action-markdownlint
- **Outputs:** PR annotations

## Scorecard (scorecard.yml)

- **Triggers:** schedule (weekly Sun 03:00 UTC), workflow_dispatch
- **Concurrency:** yes
- **Permissions:** security-events: write, contents: read
- **Writes:** security-events (SARIF upload)
- **Tools:** ossf/scorecard-action
- **Outputs:** uploads SARIF to Security tab

## Secret Scan (secret-scan.yml)

- **Triggers:** pull_request, schedule (weekly Sun 04:00 UTC), workflow_dispatch
- **Concurrency:** yes
- **Permissions:** default (read)
- **Writes:** none
- **Tools:** gitleaks
- **Outputs:** none

## Trivy Scan (trivy.yml)

- **Triggers:** pull_request, workflow_dispatch
- **Concurrency:** yes
- **Permissions:** default (read)
- **Writes:** none
- **Tools:** aquasecurity/trivy-action
- **Outputs:** none

---

## Failure Meaning

- **PR workflows fail:** PR is blocked, checks show red
- **Scheduled workflows fail:** Dashboard shows failure in Actions tab
- **Failure Alert triggers:** Issue "🚨 Repo Health: FAILING" is created or updated
- **Main Sanity fails:** Immediate visibility that main is broken

---

## Non-Goals

- This doc is a map, not a full guide
- For details, see the workflow YAML files directly
- No historical narrative here
- No troubleshooting guides
