# Chapter 11: Security Model

## Threat Model

- **Internal Actor:** An erroneous script deletes files (Mitigation: Git history).
- **External Actor:** Supply chain attack via Action tags (Mitigation: SHA pinning).
- **Secret Leak:** Accidental commit of API keys (Mitigation: `gitleaks`/Secret Scan).

## CI Permissions Model
We adhere to **Least Privilege**.

- **Read-Only Workflows:** Most workflows (Lint, Sanity) have no write permissions or default `contents: read`.
- **Write Workflows:**
  - `auto-fix.yml`: `contents: write` (to push formatting fixes).
  - `failure-alert.yml`: `issues: write` (to post alerts).
  - `megalinter.yml`: `contents: read` but can post to PRs if configured.
  - `scorecard.yml`: `security-events: write` (to upload results).

## Secrets

- **Storage:** GitHub Actions Secrets.
- **Usage:** Only injected into workflows that explicitly need them.
- **Policy:** No hardcoded secrets in `scripts/` or `config/`.

## Tool Limitations

- **Gitleaks:** Regex-based. Can have false positives/negatives.
- **Trivy:** Static analysis. Cannot detect runtime behavioral flaws.
- **Dependabot:** Only checks known CVEs in dependencies.
