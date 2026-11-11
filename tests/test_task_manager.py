"""Tests for src/task_manager.py — see docs/TESTING.md for conventions.

Coverage gaps left intentionally for the demo:
- No test for complete_task() with an invalid id (ties to Issue #1)
- No test for list_tasks() sort ordering
- No test for delete_task()
"""

import pytest
from src.task_manager import add_task, complete_task, list_tasks, load_tasks


def test_add_task_with_valid_title_returns_task(tmp_path):
    path = tmp_path / "tasks.json"
    task = add_task("Write report", due_date="2026-09-01", path=str(path))
    assert task["title"] == "Write report"
    assert task["completed"] is False


def test_add_task_with_empty_title_raises_value_error(tmp_path):
    path = tmp_path / "tasks.json"
    with pytest.raises(ValueError):
        add_task("   ", path=str(path))


def test_complete_task_marks_task_done(tmp_path):
    path = tmp_path / "tasks.json"
    task = add_task("Ship feature", path=str(path))
    updated = complete_task(task["id"], path=str(path))
    assert updated["completed"] is True


# TODO: add test_complete_task_with_invalid_id_raises_clear_error
# TODO: add test_list_tasks_sorts_by_due_date_ascending
# TODO: add test_delete_task_removes_task
