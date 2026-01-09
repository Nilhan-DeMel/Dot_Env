# Chapter 06: “Guardrails” Stack

## 1. Linting Guardrails
These tools ensure code quality and syntax correctness.

- **MegaLinter:** The "Heavy Lifter". Scans all file types (JSON, YAML, Markdown, Python). configured in `.mega-linter.yml`.
- **Actionlint:** Specialized for GitHub Actions workflows. Catches syntax errors that MegaLinter might miss or generic YAML linters ignore.
- **Markdownlint:** Enforces style guides for documentation. Configured via `.markdownlint.json`.

## 2. Formatting Guardrails
These tools ensure consistent style (whitespace, EOL).

- **EditorConfig:** (`.editorconfig`) Sets IDE defaults (indentation, charset).
- **Pre-commit:** (`.pre-commit-config.yaml`) Enforces `trailing-whitespace`, `end-of-file-fixer`, `mixed-line-ending` before code enters the repo.

## 3. Security Guardrails
These tools prevent credentials and vulnerabilities from entering.

- **Gitleaks:** (`secret-scan.yml`) Scans history and working tree for API keys, tokens, and secrets.
- **Trivy:** (`trivy.yml`) Filesystem vulnerability scanner.
- **OSSF Scorecard:** (`scorecard.yml`) Evaluates the repository against security best practices (branch protection, fuzzing, etc.).

## 4. Supply Chain Hardening

- **Action Pinning:** Most core actions are pinned to full commit SHAs (e.g., `uses: actions/checkout@11bd...`) rather than mutable tags. Exceptions: `actions/upload-artifact@v4` in `scheduled-health.yml` and `megalinter.yml` use tag pinning. This prevents supply chain attacks via tag hijacking for pinned actions.
- **Dependency Updates:** Dependabot is configured (`.github/dependabot.yml`) to update Actions and pip dependencies.

## 5. Secret Handling Model

- **Policy:** NO secrets in code.
- **Detection:** Gitleaks runs on PRs.
- **Remediation:** If a secret is committed, it must be rotated immediately and history rewritten (or the commit reverted if caught early).
