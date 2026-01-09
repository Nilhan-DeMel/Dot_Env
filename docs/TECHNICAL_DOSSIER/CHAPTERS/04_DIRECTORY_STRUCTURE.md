# Chapter 04: Directory Structure

## Top-Level Structure
(Verified via Appendix A1)

| Path | Purpose |
|------|---------|
| `/.github/workflows/` | CI/CD definitions (18 active workflows). |
| `/.github/` | Dependabot config and templates. |
| `/docs/` | Documentation (including this Dossier). |
| `/scripts/` | Python maintenance scripts (`check-repo.py`, etc.). |
| `/.gitattributes` | Git handling rules (linguist overrides, EOL). |
| `/.editorconfig` | IDE formatting rules. |
| `/.pre-commit-config.yaml` | Git hook definitions. |
| `/.mega-linter.yml` | MegaLinter configuration. |

## /docs Philosophy
Documentation in this repo follows a **"Code as Truth"** philosophy.

- **Hand-written:** `README.md`, strategy docs.
- **Generated:** This Technical Dossier (Appendices).
- **Update Rule:** If code changes, automation should ideally update docs, or humans must update immediately. "Stale docs are worse than no docs."

## /scripts Philosophy
The `/scripts` directory contains custom Python tooling to bridge the gap between standard linters and repo-specific needs.

- **Allowed:** Python 3.12+ scripts, zero external dependencies where possible (standard lib preferred).
- **Forbidden:** Complex build systems or binary blobs.

## /dist and Artifacts
The repo intentionally produces NO binaries in the root. Verify via `.gitignore` (Appendix A5).

## Unused / Orphan Candidates
(Verified via `check-repo.py` coverage)

- `.markdownlint.json`: Currently present but its dedicated workflow (`markdownlint.yml`) was removed in consolidation. Reviewdog uses it via `action-markdownlint`, so it is **NOT ORPHAN**, but effectively "Shared Config".

## Files of Special Importance

- `scripts/check-repo.py`: The single source of truth for "Repository Health". Used by CI, Hooks, and Dashboard.
- `.github/workflows/main-sanity.yml`: The lightweight gatekeeper for the `main` branch.
