# Chapter 09: Docs System

## Current Docs Inventory

- `README.md`: Root entry point.
- `/docs/REPO_MAP.md`: A high-level map of important files.
- `/docs/WORKFLOWS.md`: Detailed workflow descriptions (partially superseded by this Dossier).
- `/docs/TECHNICAL_DOSSIER/`: This generated evidence set.

## Source of Truth Rules

1. **Code is Truth:** If `main.py` does something different than `docs/main.md` says, the code is right and the doc is a bug.
2. **Generated is Better:** We prefer generated docs (like `Appendices/A*.md`) over hand-written ones because they don't rot.

## REPO_MAP Rules

- `REPO_MAP.md` is intended to be a human-curated guide, not a generated tree. It explains *why* a file exists, not just that it exists.
- **Update Policy:** Update when adding a major new component.

## No Stale Docs Policy

- Stale docs are dangerous.
- **Detection:** `doctor.py` checks for broken links (via `link-check` workflow) and potentially checks for docs mentioning deleted files.
- **Correction:** Delete stale docs rather than leaving them.
