"""Personal Productivity Manager - a small command-line task manager."""
from datetime import datetime

PRIORITIES = ("high", "medium", "low")
STATUSES = ("pending", "completed")
DATE_FORMAT = "%Y-%m-%d"

tasks: list[dict] = []
next_id = 1


def get_due_date() -> str:
    while True:
        text = input("Enter due date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(text, DATE_FORMAT)
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, e.g. 2026-11-05.")
            continue
        return text


def get_priority() -> str:
    while True:
        text = input("Enter priority level (high, medium, low): ").strip().lower()
        if text in PRIORITIES:
            return text
        print("Invalid priority. Choose high, medium or low.")


def get_status() -> str:
    while True:
        text = input("Enter status (pending, completed): ").strip().lower()
        if not text:
            return "pending"
        if text in STATUSES:
            return text
        print("Invalid status. Choose pending or completed.")


def add_task() -> None:
    global next_id
    title = input("Enter your task: ").strip()
    if not title:
        print("Task name cannot be empty.")
        return
    tasks.append(
        {
            "id": next_id,
            "task": title,
            "due_date": get_due_date(),
            "priority": get_priority(),
            "status": get_status(),
        }
    )
    next_id += 1
    print("Task added successfully!")


def find_task(task_id: int) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def view_tasks() -> None:
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['task']}")
        print("  Due Date:", task["due_date"])
        print("  Priority:", task["priority"])
        print("  Status:", task["status"])


def choose_task(action: str) -> dict | None:
    """Show the task list and return the task the user selects by ID."""
    if not tasks:
        print(f"No tasks available to {action}.")
        return None
    view_tasks()
    text = input(f"Enter the task number to {action}: ").strip()
    if not text.isdigit():
        print("Please enter a valid task number.")
        return None
    task = find_task(int(text))
    if task is None:
        print("Task not found.")
    return task


def remove_task() -> None:
    task = choose_task("remove")
    if task is None:
        return
    for index, item in enumerate(tasks):
        if item is task:
            tasks.pop(index)  # pop by index; never mutate while iterating
            break
    print("Task removed successfully!")


def mark_task_completed() -> None:
    task = choose_task("mark as completed")
    if task is None:
        return
    task["status"] = "completed"
    print("Task marked as completed!")


def main() -> None:
    print("Welcome to your Personal Productivity Manager!")
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            print("Exiting the Personal Productivity Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
