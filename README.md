# Dot Env

> A repository-governance and documentation automation lab built around repeatable health checks, security workflows, and evidence-rich maintenance.

Dot Env began as an environment-configuration concept. The implemented work is currently the engineering system around that concept: standard-library repository scanners, health and impact checks, history exporters, a structured documentation portal, contribution/security policy, and a broad GitHub Actions control plane.

> [!IMPORTANT]
> The planned environment-variable manager is not implemented. This repository demonstrates developer-experience and repository-governance automation, not a production secret manager.

## Implemented capabilities

- Cross-platform, dependency-light Python diagnostics for repository structure and documentation health.
- Repository scanning with text, JSON, and Markdown output modes.
- Change-impact and history-export tooling for human and agent handoffs.
- Security, policy, contribution, workflow, and architecture documentation.
- CI workflows for secret scanning, supply-chain checks, linting, link validation, review automation, and repository health.
- A technical dossier that separates implemented controls from conceptual architecture.

## Quick verification

```bash
python scripts/check-repo.py
python scripts/repo-scan.py --json
python scripts/impact.py
```

The tools use the Python standard library and are designed to run from the repository root.

## Documentation map

| Start here | Purpose |
| --- | --- |
| [Engineering overview](ENGINEERING_OVERVIEW.md) | What is real, why it matters, and current boundaries |
| [Documentation portal](docs/INDEX.md) | Full navigation hub |
| [Architecture](docs/ARCHITECTURE.md) | Implemented governance layers and conceptual product design |
| [Workflows](docs/WORKFLOWS.md) | CI and automation inventory |
| [Security](SECURITY.md) | Vulnerability reporting and handling |
| [Technical dossier](docs/TECHNICAL_DOSSIER/00_MASTER_INDEX.md) | Audit-oriented repository evidence |

## Security model

Dot Env never needs real `.env` values to demonstrate its current functionality. Secret material should remain outside Git, and future product work must preserve dry-run behavior, value redaction, and fail-closed validation.

## License

[MIT](LICENSE)
