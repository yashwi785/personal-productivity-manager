#PERSONAL PRODUCTIVITY MANAGER
tasks = []

print("Welcome to your Personal Productivity Manager!")


def add_task():
    task = input("Enter your task: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority level (e.g., high, medium, low): ")
    status = input("Enter status (e.g., pending, completed): ")
    tasks.append({
        "task": task,
        "due_date": due_date,
        "priority": priority,
        "status": status,
    })
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print("Task:", task["task"])
            print("Due Date:", task["due_date"])
            print("Priority:", task["priority"])
            print("Status:", task["status"])


def remove_task():
    check_task = input("Enter the task you want to remove: ")
    if len(tasks) == 0:
        print("No tasks available to remove.")
    else:
        found = False
        for task in tasks:
            if task["task"] == check_task:
                tasks.remove(task)
                print("Task removed successfully!")
                found = True
                break
        if not found:
            print("Task not found.")


def mark_task_completed():
    check_task = input("Enter the task you want to mark as completed: ")
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        found = False
        for task in tasks:
            if task["task"] == check_task:
                task["status"] = "completed"
                print("Task marked as completed!")
                found = True
                break
        if not found:
            print("Task not found.")


while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        remove_task()

    elif choice == '4':
        mark_task_completed()

    elif choice == '5':
        print("Exiting the Personal Productivity Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")