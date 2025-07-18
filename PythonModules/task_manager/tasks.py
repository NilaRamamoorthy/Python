from task_manager.storage import load_tasks, save_tasks
from task_manager.utils import generate_task_id

def add_task(title, description):
    tasks = load_tasks()
    task = {
        "id": generate_task_id(tasks),
        "title": title,
        "description": description,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def update_task(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            save_tasks(tasks)
            print("Task updated.")
            return
    print("Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) < len(tasks):
        save_tasks(new_tasks)
        print("Task deleted.")
    else:
        print("Task not found.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nAll Tasks:")
    for task in tasks:
        print(f"ID: {task['id']} | {task['title']} - {task['status']}")
