# Task Manager CLI (Copilot Demo Repository)

A small, deliberately simple command-line task manager, built to demo **GitHub Copilot in VS Code** across a full dev workflow: requirements → code generation → refactoring → documentation → testing → issue resolution.

## Why this repo exists

This isn't a production app — it's a **teaching sandbox**. It ships with:

| File / Folder | Purpose |
|---|---|
| [`docs/REQUIREMENTS.md`](docs/REQUIREMENTS.md) | Functional & non-functional requirements Copilot can generate code from |
| [`docs/TESTING.md`](docs/TESTING.md) | Testing conventions, coverage targets, naming rules |
| [`src/task_manager.py`](src/task_manager.py) | A working-but-imperfect implementation (intentionally missing features + one bug) |
| [`tests/test_task_manager.py`](tests/test_task_manager.py) | A partial test suite — gaps are left on purpose |
| [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE) | Bug report & feature request templates |
| [`ISSUES.md`](ISSUES.md) | 5 ready-to-paste sample issues (bug, feature, refactor, docs, tests) for demoing Copilot resolving real tickets |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | Repo-wide custom instructions so Copilot follows the requirements/testing docs automatically |

## Quick start

```bash
git clone <your-repo-url>
cd task-manager-demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Suggested demo flow

1. **Code Generation** — Open `docs/REQUIREMENTS.md`, ask Copilot Chat to implement the missing "priority" feature described in REQ-4.
2. **Refactoring** — Point Copilot at `src/task_manager.py`'s `list_tasks()` function (intentionally messy) and ask it to clean it up per the style notes in `copilot-instructions.md`.
3. **Documentation** — Ask Copilot to generate docstrings and a usage section in the README.
4. **Testing** — Open `docs/TESTING.md`, then ask Copilot to fill test gaps flagged in `tests/test_task_manager.py`.
5. **Issues** — Copy an issue from `ISSUES.md` into a real GitHub Issue, assign it to Copilot coding agent (or paste it into Chat) and watch it produce a fix/PR.
6. **Legacy Modernization** — `src/legacy_export.py` uses old-style string formatting; ask Copilot to modernize it.

## Publishing this to your own GitHub repo

```bash
gh repo create task-manager-demo --public --source=. --remote=origin
git add . && git commit -m "Initial demo repo"
git push -u origin main
```
