# Sample Issues

Copy any of these into a real GitHub Issue (using the templates in `.github/ISSUE_TEMPLATE/`) to demo Copilot resolving tickets — via Copilot Chat, inline edits, or the Copilot coding agent.

---

## Issue #1 — [BUG] `complete_task()` crashes on invalid task ID

**Type:** Bug | **Labels:** bug, good-first-copilot-demo

**Describe the bug**
Calling `complete_task()` with an ID that doesn't exist raises an unhandled `StopIteration`, which surfaces as a raw traceback to CLI users.

**Steps to reproduce**
1. `add_task("Test")` → creates task with id `1`
2. `complete_task(999)` → crashes

**Expected behavior**
Should raise a clear `ValueError("Task with id 999 not found")` or similar, per REQ-7 / NFR-2 in `docs/REQUIREMENTS.md`.

**Relevant requirement:** REQ-7

---

## Issue #2 — [FEATURE] Add task priority support

**Type:** Feature | **Labels:** enhancement

**Which requirement:** REQ-4 (currently ❌ Not implemented)

**Describe the feature**
Add an optional `priority` field (`low` / `medium` / `high`, default `medium`) to `add_task()`. `list_tasks()` should display priority and support an optional `filter_by_priority` argument.

**Acceptance criteria**
- [ ] `add_task()` accepts and validates `priority`
- [ ] Invalid priority values raise `ValueError`
- [ ] `list_tasks(filter_by_priority="high")` returns only matching tasks
- [ ] REQUIREMENTS.md status updated to ✅

**Testing notes**
Add happy-path, invalid-value, and filter tests per `docs/TESTING.md`.

---

## Issue #3 — [REFACTOR] Simplify `list_tasks()` sorting logic

**Type:** Refactor | **Labels:** tech-debt

**Description**
`list_tasks()` in `src/task_manager.py` does two separate loops to split tasks with/without due dates before sorting. This can be simplified to a single `sorted()` call with a smarter key function, without changing behavior.

**Acceptance criteria**
- [ ] Existing tests still pass unmodified
- [ ] Function readability improved (single pass, clear key function)

---

## Issue #4 — [DOCS] Missing usage examples in README

**Type:** Documentation | **Labels:** documentation

**Description**
`README.md` has a Quick Start but no example of actual CLI usage/output. Add a "Usage" section with example commands and sample output for add/list/complete/delete.

---

## Issue #5 — [TESTS] Close test coverage gaps in `test_task_manager.py`

**Type:** Testing | **Labels:** tests

**Description**
Three TODOs are left in `tests/test_task_manager.py`:
- `test_complete_task_with_invalid_id_raises_clear_error`
- `test_list_tasks_sorts_by_due_date_ascending`
- `test_delete_task_removes_task`

**Acceptance criteria**
- [ ] All three tests implemented per `docs/TESTING.md` naming convention
- [ ] `pytest --cov=src` shows ≥ 85% coverage
