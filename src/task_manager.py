"""Task Manager CLI — core logic.

See docs/REQUIREMENTS.md for the full requirements this module implements.
NOTE: REQ-4 (priority) is intentionally NOT implemented here — good Copilot
code-generation demo target.
"""

import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks(path=TASKS_FILE):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_tasks(tasks, path=TASKS_FILE):
    with open(path, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title, due_date=None, path=TASKS_FILE):
    """Add a new task and persist it. Raises ValueError on empty title."""
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty")
    tasks = load_tasks(path)
    new_id = max([t["id"] for t in tasks], default=0) + 1
    task = {
        "id": new_id,
        "title": title.strip(),
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    save_tasks(tasks, path)
    return task


# TODO(REQ-7 / Issue #1): this raises a raw IndexError/StopIteration on bad
# ids instead of a clean, user-facing error. Good refactor target.
def complete_task(task_id, path=TASKS_FILE):
    tasks = load_tasks(path)
    task = next(t for t in tasks if t["id"] == task_id)
    task["completed"] = True
    save_tasks(tasks, path)
    return task


def delete_task(task_id, path=TASKS_FILE):
    tasks = load_tasks(path)
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks, path)


# Intentionally messy — good "Refactoring" demo target (see README step 2).
def list_tasks(path=TASKS_FILE):
    tasks = load_tasks(path)
    result = []
    for t in tasks:
        if t["due_date"] is not None:
            result.append(t)
    for t in tasks:
        if t["due_date"] is None:
            result.append(t)
    result_sorted = sorted(
        result,
        key=lambda x: x["due_date"] if x["due_date"] is not None else "9999-99-99",
    )
    return result_sorted
