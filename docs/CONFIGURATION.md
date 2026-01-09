# ⚙️ Configuration Reference

> All configuration files, flags, environment variables, and defaults for Dot_Env.

---

## Configuration Files Inventory

| File | Purpose | Source |
|------|---------|--------|
| [.editorconfig](../.editorconfig) | Editor formatting | Lines 1-16 |
| [.gitignore](../.gitignore) | Git exclusion patterns | Lines 1-34 |

---

## .editorconfig

**Path:** `/.editorconfig`
**Purpose:** Ensures consistent formatting across all contributors' editors.

### Settings

```ini
# Line 1: Apply to all editors
root = true

# Lines 3-9: Default rules for all files
[*]
indent_style = space        # Use spaces, not tabs
indent_size = 2             # 2 spaces per indent level
end_of_line = lf            # Unix-style line endings
charset = utf-8             # UTF-8 encoding
trim_trailing_whitespace = true
insert_final_newline = true # Ensure files end with newline

# Lines 11-12: Markdown exception
[*.md]
trim_trailing_whitespace = false  # Preserve trailing spaces (line breaks)

# Lines 14-15: Makefile exception
[Makefile]
indent_style = tab          # Makefiles require tabs
```

### Traceability

| Setting | File | Line |
|---------|------|------|
| `indent_size = 2` | [.editorconfig](../.editorconfig) | L5 |
| `end_of_line = lf` | [.editorconfig](../.editorconfig) | L6 |
| `charset = utf-8` | [.editorconfig](../.editorconfig) | L7 |

---

## .gitignore

**Path:** `/.gitignore`
**Purpose:** Excludes files from version control.

### Categories

#### Dependencies (Lines 1-3)

```gitignore
node_modules/          # npm packages
package-lock.json      # Lock file (regenerated)
```

#### Environment Files (Lines 5-8)

```gitignore
.env                   # Local environment
.env.local             # Local overrides
.env.*.local           # Environment-specific local
```

#### Build Output (Lines 10-13)

```gitignore
dist/                  # Distribution build
build/                 # Build output
out/                   # Output directory
```

#### Logs (Lines 15-18)

```gitignore
logs/                  # Log directory
*.log                  # Any log file
npm-debug.log*         # npm debug logs
```

#### OS Files (Lines 20-23)

```gitignore
.DS_Store              # macOS
Thumbs.db              # Windows thumbnails
Desktop.ini            # Windows folder settings
```

#### IDE (Lines 25-29)

```gitignore
.idea/                 # JetBrains IDEs
.vscode/               # VS Code
*.swp                  # Vim swap
*.swo                  # Vim swap
```

#### Coverage (Lines 31-33)

```gitignore
coverage/              # Test coverage
.nyc_output/           # NYC coverage tool
```

---

## GitHub Configuration

### Issue Templates

**Location:** `/.github/ISSUE_TEMPLATE/`

#### bug_report.md

- **Auto-label:** `bug`
- **Title prefix:** `[BUG]`

#### feature_request.md

- **Auto-label:** `feature`
- **Title prefix:** `[FEATURE]`

### PR Template

**Location:** `/.github/PULL_REQUEST_TEMPLATE.md`

- Requires description, type of change, checklist
- Links to related issues

---

## Environment Variables

> [!NOTE]
> **No environment variables are currently used.** This section documents expected future variables.

### Expected Variables (Future)

| Variable | Type | Default | Required | Description |
|----------|------|---------|----------|-------------|
| `NODE_ENV` | string | `development` | No | Runtime environment |
| `DOT_ENV_DEBUG` | boolean | `false` | No | Enable debug logging |

---

## Defaults Summary

| Aspect | Default Value | Source |
|--------|---------------|--------|
| Indent style | spaces | [.editorconfig](../.editorconfig#L4) |
| Indent size | 2 | [.editorconfig](../.editorconfig#L5) |
| Line endings | LF | [.editorconfig](../.editorconfig#L6) |
| Charset | UTF-8 | [.editorconfig](../.editorconfig#L7) |
| License | MIT | [LICENSE](../LICENSE#L1) |

---

## Missing Configuration (Gaps)

| Expected | Status | Impact |
|----------|--------|--------|
| `package.json` | ❌ Missing | No npm scripts, dependencies |
| `.env.example` | ❌ Missing | No documented env vars |
| `tsconfig.json` / `jsconfig.json` | ❌ Missing | No TypeScript/JS config |
| `.prettierrc` / `.eslintrc` | ❌ Missing | No linting/formatting |
| `Dockerfile` | ❌ Missing | No containerization |

---

*Document Status: Complete for existing configuration*
