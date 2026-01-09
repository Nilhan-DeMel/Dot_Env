# Chapter 07: Pre-commit Contract

## Hooks Inventory
(Verified via `.pre-commit-config.yaml` in Appendix A5)

| Hook | Purpose |
|------|---------|
| `trailing-whitespace` | Removes silent whitespace at end of lines. |
| `end-of-file-fixer` | Ensures strictly one newline at EOF. |
| `check-yaml` | Validates YAML syntax. |
| `check-json` | Validates JSON syntax. |
| `mixed-line-ending` | Enforces LF (Unix) line endings on all files. |

## Contract & Operation

- **Local:** Developers *should* run `pre-commit install` to catch issues before commit.
- **CI Gate:** The `Pre-commit Gate` workflow (`pre-commit.yml`) runs strict checks on every PR.
- **Auto-Fix:** The `Auto-Fix Maintenance` workflow (`auto-fix.yml`) runs pre-commit daily and **commits changes**. This means formatting drift is self-correcting.

## Cross-Platform Policy

- **Line Endings:** We enforce LF.
- **Windows Users:** Must configure git to handle CRLF/LF correctly (`core.autocrlf`). The `mixed-line-ending` hook will fail if Windows CRLF leaks into the repo.

## AI Guidance

- **Interpretation:** A pre-commit failure usually means "Formatting violation".
- **Reaction:**
    1. If local: Run `pre-commit run -a`.
    2. If CI: Check logs, apply fix.
    3. If lazy: Wait for `auto-fix` (daily) or run `auto-fix` manually (if permissions allow).
