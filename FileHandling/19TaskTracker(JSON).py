import json
import os

TASK_FILE = "task_tracker.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    title = input("Enter task title: ")
    status = "Pending"
    tasks = load_tasks()
    tasks.append({"title": title, "status": status})
    save_tasks(tasks)
    print("Task added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} - {task['status']}")

def update_status():
    view_tasks()
    tasks = load_tasks()
    index = int(input("Enter task number to update status: ")) - 1
    if 0 <= index < len(tasks):
        print("Choose new status: 1. Pending 2. In Progress 3. Completed")
        choice = input("Enter choice: ")
        status_map = {"1": "Pending", "2": "In Progress", "3": "Completed"}
        if choice in status_map:
            tasks[index]["status"] = status_map[choice]
            save_tasks(tasks)
            print("Status updated.")
        else:
            print("Invalid choice.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- Task Tracker ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_status()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

main()
