# Chapter 15: Quickstart for Contributors

## 1. Clone & Setup
```bash
git clone https://github.com/Nilhan-DeMel/Dot_Env.git
cd Dot_Env
pip install pre-commit
pre-commit install
```

## 2. Daily Routine

- **Check Health:** `python scripts/check-repo.py`
- **Commit Work:**
    ```bash
    git add .
    git commit -m "feat: my new feature"  # Follow conventional commits!
    ```
- **Verify:** `pre-commit run --all-files` (if commit failed).

## 3. Interpreting the Dashboard

- Go to **Actions** tab.
- Look for **"Repo Dashboard"**.
- Green = Healthy.
- Red = Read the logs. Usually a script failure or lint error.

## 4. Adding New Tools
**Rule:** Do not add a new tool without adding a corresponding CI check AND a local pre-commit hook (if applicable).
