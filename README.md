# personal-productivity-manager
A beginner friendly Python CLI application to manage daily tasks, including adding, removing, viewing, marking task as completed.

# Personal Productivity Manager

A lightweight, terminal-based task management application written in Python. It allows users to track daily goals, set priorities, track deadlines, and monitor task completion status through a simple interactive command-line interface.

---

## Features

- **Add Tasks**: Record a task name, due date (`YYYY-MM-DD`), priority level (`high`, `medium`, `low`), and initial status (`pending`, `completed`).
- **View All Tasks**: Inspect your full task list with all associated metadata.
- **Remove Tasks**: Delete an existing task by specifying its name.
- **Mark Complete**: Update the status of any task directly to `completed`.
- **Interactive Menu**: Continuous loop allowing multiple operations in one session until explicitly exited.

---

## Project Structure

```text
personal-productivity-manager/
│
├── main.py          # Core application script containing the menu loop and functions
└── README.md        # Project documentation
