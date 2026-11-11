# Requirements — Task Manager CLI

## 1. Overview
A command-line tool that lets a user create, list, complete, and delete tasks stored locally in a JSON file (`tasks.json`).

## 2. Functional Requirements

| ID | Requirement | Status |
|---|---|---|
| REQ-1 | User can add a task with a title and optional due date | ✅ Implemented |
| REQ-2 | User can list all tasks, sorted by due date | ✅ Implemented |
| REQ-3 | User can mark a task as complete by ID | ✅ Implemented |
| REQ-4 | User can assign a priority (`low`, `medium`, `high`) to a task, and list output should show priority and support filtering by it | ❌ Not implemented — good Copilot demo target |
| REQ-5 | User can delete a task by ID | ✅ Implemented |
| REQ-6 | Tasks persist across runs via `tasks.json` in the working directory | ✅ Implemented |
| REQ-7 | Invalid task IDs must raise a clear, user-facing error — not a stack trace | ⚠️ Partially implemented (see Issue #1 in `ISSUES.md`) |

## 3. Non-Functional Requirements

- **NFR-1 (Reliability):** No operation should corrupt `tasks.json`, even if the program is killed mid-write.
- **NFR-2 (Usability):** All CLI errors must be human-readable, no raw Python tracebacks shown to end users.
- **NFR-3 (Performance):** Must handle at least 10,000 tasks without noticeable CLI lag (< 200ms per command).
- **NFR-4 (Portability):** Python 3.10+, no external dependencies beyond the standard library.

## 4. Out of Scope (v1)

- Multi-user support
- Cloud sync
- GUI

## 5. Acceptance Criteria Template

Every new feature PR must include:
- [ ] Updated entry in this requirements table
- [ ] Tests added per `docs/TESTING.md`
- [ ] Docstrings on all new public functions
- [ ] No regression in existing `pytest` suite
