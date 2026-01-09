# 🛠️ Setup Guide

> Prerequisites, installation, and local development for Dot_Env.

---

## Current State

> [!IMPORTANT]
> This repository is a **scaffold**. There is no application code to run yet.

This guide documents what exists and provides placeholders for future setup steps.

---

## Prerequisites

### Required

| Tool | Version | Purpose |
|------|---------|---------|
| Git | 2.0+ | Version control |

### Recommended

| Tool | Version | Purpose |
|------|---------|---------|
| Node.js | 18+ | (Future) Runtime |
| npm | 9+ | (Future) Package manager |
| EditorConfig plugin | Any | Honor [.editorconfig](../.editorconfig) |

### Editor Support

For consistent formatting, install EditorConfig for your editor:

- **VS Code:** [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
- **JetBrains IDEs:** Built-in support
- **Vim:** [editorconfig-vim](https://github.com/editorconfig/editorconfig-vim)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Nilhan-DeMel/Dot_Env.git
cd Dot_Env
```

### 2. Verify Clone

```bash
# Check you're on main branch
git branch --show-current
# Output: main

# Check file structure
ls -la
# Should show: README.md, LICENSE, CONTRIBUTING.md, etc.
```

---

## Local Development

### Current Capabilities

Since this is a scaffold, you can currently:

| Action | Command | Status |
|--------|---------|--------|
| View docs | Open `docs/INDEX.md` | ✅ Works |
| Run repo scanner | `python scripts/repo-scan.py` | ✅ Works |
| Contribute | Follow [CONTRIBUTING.md](../CONTRIBUTING.md) | ✅ Works |

### Future Capabilities (Not Yet Implemented)

| Action | Expected Command | Status |
|--------|-----------------|--------|
| Install dependencies | `npm install` | ❌ No package.json |
| Run application | `npm start` | ❌ Not implemented |
| Run tests | `npm test` | ❌ Not implemented |
| Build | `npm run build` | ❌ Not implemented |

---

## Environment Variables

> [!NOTE]
> No environment variables are currently required.

### Future Environment Variables

When the application is implemented, expect variables like:

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DOT_ENV_PATH` | No | `.env` | Path to env file |
| `DOT_ENV_STRICT` | No | `false` | Fail on missing vars |
| `DOT_ENV_LOG_LEVEL` | No | `info` | Logging verbosity |

### .env.example (Missing)

> [!WARNING]
> The README references `.env.example` but this file does not exist.
>
> **Gap identified:** Create `.env.example` when implementing core functionality.

---

## Build & Run

### Currently Available Commands

```bash
# Regenerate repo documentation
python scripts/repo-scan.py

# Check git status
git status
```

### Future Commands (Placeholder)

```bash
# Install dependencies
npm install

# Run in development mode
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

---

## Troubleshooting

### EditorConfig Not Being Applied

1. Ensure your editor has EditorConfig support
2. Check that [.editorconfig](../.editorconfig) is in the repo root
3. Restart your editor after installing the plugin

### Git Clone Fails

```bash
# If SSH fails, try HTTPS
git clone https://github.com/Nilhan-DeMel/Dot_Env.git
```

---

## Next Steps

After setup, see:

- [ARCHITECTURE.md](ARCHITECTURE.md) — Understand the design
- [CONFIGURATION.md](CONFIGURATION.md) — Configuration reference
- [WORKFLOWS.md](WORKFLOWS.md) — Git workflow and CI/CD

---

*Document Status: Partial (scaffold only)*
