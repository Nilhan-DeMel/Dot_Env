# Chapter 08: Repo Scripts Tech Spec

## General Architecture
All scripts are located in `/scripts`. They are written in Python (3.12+ compatible) and aim for zero dependencies where possible.

## 1. check-repo.py

- **Purpose:** The primary health status script. It asserts the "Pristine State".
- **Inputs:** None (reads valid file states from internal logic).
- **Outputs:** Console status (Pass/Fail).
- **Used By:** `conflict-check.yml`, `pristine.yml` (legacy), `repo-dashboard.yml`, `auto-fix.yml`, `main-sanity.yml`.
- **Exit Codes:** 0 = Healthy, 1 = Unhealthy.

## 2. repo-scan.py

- **Purpose:** Summarizes repository metadata (file usage, type counts).
- **Inputs:** Repository file tree.
- **Outputs:** Console summary report.
- **Used By:** `repo-dashboard.yml`, `conflict-check.yml`, `main-sanity.yml`, `auto-fix.yml`.

## 3. doctor.py

- **Purpose:** Advanced diagnostics. Checks for deep consistency (docs vs code, orphan files, broken links).
- **Used By:** `scheduled-health.yml` (Daily).

## 4. export-repo-history.py

- **Purpose:** Generating timestamped markdown exports of repository history.
- **Used By:** `auto-fix.yml` (Daily).

## 5. export-repo-history-pdf.py

- **Purpose:** Generates PDF versions of history exports using `reportlab`.
- **Used By:** `auto-fix.yml` (implied by pip install reportlab in that workflow).

## 6. impact.py

- **Purpose:** analyzes changed files to determine which CI jobs should run (smart skipping).
- **Used By:** `impact-ci.yml`.

## 7. export-repo-health.py

- **Purpose:** Snapshots health metrics to a file (JSON/MD).
- **Used By:** `scheduled-health.yml`.

## Safety Notes

- **Read-Only:** `check-repo`, `repo-scan`, `doctor`, `impact`.
- **Write-Active:** `export-*` scripts write artifacts.
