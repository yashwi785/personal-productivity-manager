# Personal Productivity Manager

A lightweight, terminal-based task management application written in Python. It lets you track daily goals, set priorities, track deadlines, and monitor completion status through an interactive command-line interface.

---

## Features

- **Add Tasks**: record a task name, due date (`YYYY-MM-DD`), priority (`high`, `medium`, `low`), and status (`pending`, `completed`).
- **View All Tasks**: inspect the full task list with all metadata and task IDs.
- **Remove Tasks**: delete a task by its ID.
- **Mark Complete**: update any task's status to `completed` by its ID.
- **Interactive Menu**: continuous loop until explicitly exited.

---

## Project Structure

```text
personal-productivity-manager/
|
|-- productive.py   # menu loop, validation and task functions
`-- README.md       # project documentation
```

---

## Run it

```bash
python productive.py
```

Python 3.10+ required (the type hints use `dict | None`).

---

## Input validation

- Dates are parsed with `datetime.strptime`, so `2026-13-45` is rejected instead of stored.
- Priority and status are checked against allowed values and re-prompt on a typo.
- An empty task name is rejected.
- Tasks are addressed by ID, so two tasks with the same name no longer collide.
