# Chapter 10: Git Policy

## Branch Model

- **Trunk-Based:** We use `main` as the single source of truth.
- **Feature Branches:** Short-lived branches (e.g., `feat/new-script`, `fix/typo`).
- **Merge Strategy:** Squash & Merge is preferred to keep history linear and readable.

## Commit Message Rules

- **Enforcement:** `commitlint` (via `commitlint.yml`) runs on PRs.
- **Format:** Conventional Commits (`type(scope): subject`).
  - Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
- **Why:** Allows automated semantic versioning (future) and readable history.

## Direct-to-Main

- **Policy:** **Avoid** direct pushes to `main`.
- **Exception:**
    1. `auto-fix` workflow (automated maintenance).
    2. Emergency doc fixes by the repo owner.
- **Safety Net:** The `Main Sanity` workflow runs on every push to `main` to catch regressions immediately.

## Rollback Procedure
If a bad commit lands on `main`:

1. **Do NOT Force Push.**
2. **Revert:** Create a new commit that reverts the changes: `git revert <sha>`.
3. **Verify:** Ensure `Main Sanity` passes on the revert commit.
