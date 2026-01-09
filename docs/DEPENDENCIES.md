# 📦 Dependencies

> Dependency inventory, rationale, and update policy for Dot_Env.

---

## Current State

> [!IMPORTANT]
> **This repository has no runtime dependencies.** No `package.json`, `requirements.txt`, or similar manifest exists.

---

## Dependency Manifest Status

| File | Exists | Dependencies |
|------|--------|--------------|
| `package.json` | ❌ No | — |
| `package-lock.json` | ❌ No | — |
| `requirements.txt` | ❌ No | — |
| `pyproject.toml` | ❌ No | — |
| `go.mod` | ❌ No | — |
| `Cargo.toml` | ❌ No | — |
| `pom.xml` | ❌ No | — |

---

## Development Tools Used

While no code dependencies exist, the repository relies on:

| Tool | Purpose | Required |
|------|---------|----------|
| Git | Version control | ✅ Yes |
| GitHub CLI (`gh`) | Repo automation | ⚪ Optional |
| Python 3.6+ | Run repo-scan.py | ⚪ Optional |
| EditorConfig | Consistent formatting | ⚪ Optional |

---

## Future Dependencies (Recommendations)

When implementing core functionality, consider:

### Runtime Dependencies

| Package | Purpose | Rationale |
|---------|---------|-----------|
| `dotenv` | Parse .env files | Core functionality |
| `commander` / `yargs` | CLI parsing | Command-line interface |
| `ajv` / `zod` | Schema validation | Validate env vars |

### Development Dependencies

| Package | Purpose | Rationale |
|---------|---------|-----------|
| `typescript` | Type safety | Catch errors at compile time |
| `jest` / `vitest` | Testing | Ensure correctness |
| `eslint` | Linting | Code quality |
| `prettier` | Formatting | Consistent style |
| `husky` | Git hooks | Pre-commit checks |

---

## Update Policy

### Recommended Practices

1. **Pin dependencies** — Use exact versions in package.json
2. **Lock files** — Commit package-lock.json
3. **Regular updates** — Monthly dependency review
4. **Security audits** — Run `npm audit` before releases

### Automation

Enable Dependabot by creating `.github/dependabot.yml`:

```yaml
# RECOMMENDATION - not yet implemented
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    commit-message:
      prefix: "chore(deps):"
```

---

## Dependency Audit Commands

### Node.js

```bash
npm audit                 # Check for vulnerabilities
npm audit fix             # Auto-fix where possible
npm outdated              # List outdated packages
```

### Python

```bash
pip-audit                 # Security audit
pip list --outdated       # List outdated packages
```

---

## Adding a Dependency

### Checklist

Before adding a new dependency:

1. [ ] **Is it necessary?** Can stdlib do this?
2. [ ] **Is it maintained?** Check last commit date, open issues
3. [ ] **Is it popular?** Download counts, GitHub stars
4. [ ] **Is it secure?** Check for known vulnerabilities
5. [ ] **License compatible?** Must be MIT/BSD/Apache-compatible

### Documentation Requirement

When adding a dependency, update this file with:

- Package name and version
- Purpose (why it's needed)
- Rationale (why this package over alternatives)

---

## Removing a Dependency

1. Remove from package.json/requirements.txt
2. Run install to update lock file
3. Search codebase for imports
4. Update this documentation
5. Test thoroughly

---

## Scripts Dependency

The repo-scan script has minimal dependencies:

| Script | Dependencies |
|--------|--------------|
| `scripts/repo-scan.py` | Python stdlib only (`os`, `pathlib`) |

---

*Document Status: Complete (no dependencies to document)*
