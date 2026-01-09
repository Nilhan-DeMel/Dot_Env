# ❓ Frequently Asked Questions

> Common questions and answers about Dot_Env.

---

## General

### What is Dot_Env?

Dot_Env is a project for managing environment variables and configuration files across different environments (development, staging, production).

**Status:** Currently a scaffold — core functionality is not yet implemented.

---

### Is this production-ready?

**No.** This repository currently contains only:

- Repository hygiene files (LICENSE, CONTRIBUTING, etc.)
- GitHub templates
- Documentation

No application code exists yet.

---

### What's the license?

**MIT License** — see [LICENSE](../LICENSE).

You can use, modify, and distribute this project freely, including for commercial purposes.

---

## Setup

### Why is there no package.json?

This is a **scaffold repository**. The tech stack hasn't been chosen yet. When core functionality is implemented, a `package.json` (or equivalent) will be added.

---

### The README mentions .env.example but I can't find it?

**Known gap.** The `.env.example` file referenced in the README does not exist yet. It will be created when the application code is implemented.

---

### How do I run the project?

Currently, there's nothing to run. The only executable is the documentation scanner:

```bash
python scripts/repo-scan.py
```

---

## Contributing

### How do I contribute?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a PR

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

---

### What commit message format should I use?

[Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add env parser
fix: handle empty files
docs: update README
chore: update dependencies
```

---

### Where do I report bugs?

Use the [bug report template](../.github/ISSUE_TEMPLATE/bug_report.md) when creating a GitHub issue.

---

## Technical

### What technologies will this use?

Not yet decided. Based on the `.gitignore`, Node.js is anticipated:

```gitignore
node_modules/
*.log
npm-debug.log*
```

---

### Why are there no tests?

This is a scaffold. Tests will be added when core functionality is implemented.

---

### Why is branch protection not enabled?

Branch protection rules require **GitHub Pro** for private repositories. Options:

1. Make the repository public
2. Upgrade to GitHub Pro
3. Use repository rulesets (may also require Pro)

---

## Troubleshooting

### My editor isn't respecting formatting rules

1. Install EditorConfig plugin for your editor
2. Verify [.editorconfig](../.editorconfig) is in the repo root
3. Restart your editor

---

### Git complains about line endings

The `.editorconfig` specifies LF line endings. On Windows:

```bash
git config core.autocrlf input
```

---

### The repo-scan script fails

Ensure you have Python 3.6+ installed:

```bash
python --version
# Should be 3.6 or higher
```

---

## Documentation

### How do I update documentation?

1. Edit the relevant file in `/docs/`
2. Run `python scripts/repo-scan.py` to update REPO_MAP
3. Submit a PR

---

### Can I add new documentation files?

Yes! Add them to `/docs/` and update:

- [INDEX.md](INDEX.md) with a link
- [REPO_MAP.md](REPO_MAP.md) with the file entry

---

## Still Have Questions?

Open an issue using the feature request template, or see:

- [INDEX.md](INDEX.md) — Documentation portal
- [GLOSSARY.md](GLOSSARY.md) — Term definitions

---

*This FAQ will be expanded as the project evolves.*
