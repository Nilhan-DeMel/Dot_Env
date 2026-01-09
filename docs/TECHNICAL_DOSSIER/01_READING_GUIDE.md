# How to Use This Dossier

**Target Audience:** AI Agents, Developers, and Auditors.

## Core Philosophy: "Evidence First"
This documentation is NOT a set of vague promises. It is a snapshot of reality, backed by evidence files in the `APPENDICES/` folder. Every claim about a workflow, script, or policy is derived from the actual code at commit `14859ef`.

## How to Verify Claims
When you read a statement like "The Pre-commit Gate runs on every PR," verify it by checking:

1. **Chapter 05 (Workflows):** Read the spec.
2. **Appendix A4 (Workflows Raw):** Read the actual YAML source code.

## Navigation

- Start with **[02. Executive Overview](CHAPTERS/02_EXECUTIVE_OVERVIEW.md)** for a high-level understanding.
- Use **[04. Directory Structure](CHAPTERS/04_DIRECTORY_STRUCTURE.md)** to find specific files.
- Consult **[05. Workflows](CHAPTERS/05_WORKFLOWS_COMPLETE_SPEC.md)** for CI/CD details.

## Updating This Dossier
This dossier was generated largely by automation. To update it:

1. Run the collection scripts (commands listed in appendices).
2. Update the relevant chapter text.
3. Commit with `docs: update technical dossier`.

**Note:** If the code drifts from this documentation, the **CODE IS TRUTH**.
