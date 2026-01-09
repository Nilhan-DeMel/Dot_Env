# Chapter 13: AI-First Development Playbook

## AI Operating Constraints

- **No Hallucinations:** You must inspect the Code (via `view_file` or `run_command`) before asserting facts.
- **No Blind "Fixes":** Do not modify a workflow just because you "think" it's wrong. Verify the error log first.

## Safe Change Protocol

1. **Read Context:** Use `check-repo.py` to assess current health.
2. **Small Diffs:** Prefer atomic commits. Do not refactor the entire repo in one go.
3. **Verify:** After pushing, use `gh run list` (or equivalent) to confirm CI passed.

## Interpreting CI Failures

- **Lint Failure:** You likely violated a rule in `.mega-linter.yml` or `.pre-commit-config.yaml`. *Fix: Run linter locally.*
- **Security Failure:** You committed a secret. *Fix: Rotate secret, rewrite history.*
- **Broken Link:** You deleted a file referenced in docs. *Fix: Update docs.*

## Minimal Safe PR Template
```markdown
## Summary
(One line explanation)

## Changes
- [File]: (Change description)

## Verification
- [ ] Ran check-repo.py
- [ ] Ran pre-commit
```
