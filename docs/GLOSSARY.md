# 📖 Glossary

> Terms, acronyms, and definitions used in the Dot_Env project.

---

## Terms

### CI/CD

**Continuous Integration / Continuous Deployment**

Automated pipelines that build, test, and deploy code. See [WORKFLOWS.md](WORKFLOWS.md).

---

### Conventional Commits

A specification for commit message format that enables automated changelog generation.

**Format:** `<type>(<scope>): <description>`

**Source:** [CONTRIBUTING.md](../CONTRIBUTING.md#L16)

**Reference:** <https://www.conventionalcommits.org/>

---

### EditorConfig

A file format for defining consistent coding styles across editors and IDEs.

**File:** [.editorconfig](../.editorconfig)

**Reference:** <https://editorconfig.org/>

---

### Environment Variable

A dynamic value stored outside the application code that affects program behavior.

**Examples:** `NODE_ENV`, `API_KEY`, `DATABASE_URL`

---

### Git Hook

A script that runs automatically at specific points in the git workflow.

**Common hooks:** `pre-commit`, `commit-msg`, `pre-push`

---

### GitHub Actions

GitHub's built-in CI/CD platform for automating workflows.

**Location:** `.github/workflows/` (not yet configured)

---

### MIT License

A permissive open-source license that allows commercial use, modification, and distribution.

**File:** [LICENSE](../LICENSE)

---

### Scaffold

A starter template or skeleton for a project, containing boilerplate files but no core functionality.

**Status:** This repository is currently a scaffold.

---

### Semantic Versioning (SemVer)

A versioning scheme using `MAJOR.MINOR.PATCH` format.

- **MAJOR:** Breaking changes
- **MINOR:** New features (backward compatible)
- **PATCH:** Bug fixes

**Reference:** <https://semver.org/>

---

## Acronyms

| Acronym | Full Form | Description |
|---------|-----------|-------------|
| API | Application Programming Interface | Programmatic interface |
| CI | Continuous Integration | Automated testing on commits |
| CD | Continuous Deployment | Automated deployment |
| CLI | Command-Line Interface | Terminal-based interface |
| ENV | Environment | Runtime context |
| LF | Line Feed | Unix line ending (`\n`) |
| MIT | Massachusetts Institute of Technology | License type |
| PR | Pull Request | Code review mechanism |
| SemVer | Semantic Versioning | Version numbering scheme |
| UTF-8 | Unicode Transformation Format 8-bit | Character encoding |

---

## File Extensions

| Extension | Type | Description |
|-----------|------|-------------|
| `.md` | Markdown | Documentation files |
| `.env` | Environment | Environment variable files |
| `.yml` / `.yaml` | YAML | Configuration files |
| `.json` | JSON | Data/configuration files |
| `.js` | JavaScript | JavaScript source |
| `.ts` | TypeScript | TypeScript source |

---

## Project-Specific Terms

| Term | Definition |
|------|------------|
| Dot_Env | This project — environment configuration management |
| repo-scan | Script that regenerates documentation |
| FILE_DOCS | Per-file technical documentation |

---

*Add new terms as the project evolves.*
