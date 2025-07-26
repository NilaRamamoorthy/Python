import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\n--- To-Do Tasks ---")
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task['completed'] else "✘"
        print(f"{idx}. [{status}] {task['title']} (Priority: {task['priority']}, Due: {task['due_date']})")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter priority (Low, Medium, High): ").capitalize()
    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")  # Validate date
    except ValueError:
        print("Invalid date format. Task not added.")
        return

    tasks.append({
        'title': title,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    })
    print("Task added successfully.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['completed'] = True
            print("Task marked as complete.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

# Sort tasks
def sort_tasks(tasks):
    print("\nSort by:\n1. Priority\n2. Due Date")
    choice = input("Enter your choice: ")
    if choice == '1':
        priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
        tasks.sort(key=lambda x: priority_order.get(x['priority'], 4))
        print("Tasks sorted by priority.")
    elif choice == '2':
        tasks.sort(key=lambda x: x['due_date'])
        print("Tasks sorted by due date.")
    else:
        print("Invalid choice.")

# Search for a task
def search_tasks(tasks):
    query = input("Enter keyword to search: ").lower()
    results = [task for task in tasks if query in task['title'].lower()]
    if results:
        print("\nSearch results:")
        view_tasks(results)
    else:
        print("No tasks found with that keyword.")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Sort Tasks")
        print("6. Search Tasks")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_complete(tasks)
        elif choice == '5':
            sort_tasks(tasks)
        elif choice == '6':
            search_tasks(tasks)
        elif choice == '7':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
