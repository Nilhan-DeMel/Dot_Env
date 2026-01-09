# EditorConfig Reference

> Deep dive into [/.editorconfig](../../.editorconfig)

---

## File Overview

| Property | Value |
|----------|-------|
| **Path** | `/.editorconfig` |
| **Purpose** | Define consistent coding styles across editors |
| **Lines** | 16 |
| **Bytes** | 234 |
| **Affects** | All files in repository |

---

## What It Does

EditorConfig ensures all contributors use consistent formatting:

- Indentation style and size
- Line endings
- Character encoding
- Trailing whitespace handling

**Inputs:** None (configuration file)
**Outputs:** Editor behavior modification
**Side Effects:** Changes editor settings when file is opened

---

## Configuration Breakdown

### Root Declaration (Line 1)

```ini
root = true
```

Tells editors to stop searching for `.editorconfig` files in parent directories.

---

### Default Rules (Lines 3-9)

```ini
[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

| Setting | Value | Meaning |
|---------|-------|---------|
| `indent_style` | `space` | Use spaces, not tabs |
| `indent_size` | `2` | 2 spaces per level |
| `end_of_line` | `lf` | Unix line endings |
| `charset` | `utf-8` | UTF-8 encoding |
| `trim_trailing_whitespace` | `true` | Remove trailing spaces |
| `insert_final_newline` | `true` | Ensure file ends with newline |

---

### Markdown Exception (Lines 11-12)

```ini
[*.md]
trim_trailing_whitespace = false
```

Markdown uses trailing spaces for line breaks, so whitespace trimming is disabled.

---

### Makefile Exception (Lines 14-15)

```ini
[Makefile]
indent_style = tab
```

Makefiles require tabs for indentation (syntax requirement).

---

## Error Handling

**Not applicable.** EditorConfig files are declarative and don't execute code.

If the file contains invalid syntax, editors may:

- Ignore the file entirely
- Ignore only the invalid section
- Show a warning

---

## Dependencies

| Dependency | Required |
|------------|----------|
| EditorConfig plugin | Yes (for editor support) |

**Supported editors:**

- VS Code (via extension)
- JetBrains IDEs (built-in)
- Vim (via plugin)
- Sublime Text (via plugin)

---

## How to Modify Safely

1. Test changes locally first
2. Verify with multiple files
3. Consider impact on existing files
4. Commit and push

**Common modifications:**

- Change `indent_size` for specific file types
- Add rules for new file extensions
- Adjust `end_of_line` for cross-platform work

---

## Related Documentation

- [CONFIGURATION.md](../CONFIGURATION.md) — All config files
- [EditorConfig.org](https://editorconfig.org/) — Official documentation

---

*File last modified: Initial commit (`c3bc5fc`)*
