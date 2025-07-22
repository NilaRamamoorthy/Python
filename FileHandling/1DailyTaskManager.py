import os
from datetime import date

FILENAME = f"{date.today()}.txt"

def add_task(task):
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print("Task added.")

def view_tasks():
    if not os.path.exists(FILENAME):
        print("No tasks found for today.")
        return
    with open(FILENAME, "r") as file:
        tasks = file.readlines()
    print("Today's Tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task.strip()}")

def delete_task(task_number):
    if not os.path.exists(FILENAME):
        print("No task file found.")
        return
    with open(FILENAME, "r") as file:
        tasks = file.readlines()
    if task_number <= 0 or task_number > len(tasks):
        print("Invalid task number.")
        return
    del tasks[task_number - 1]
    with open(FILENAME, "w") as file:
        file.writelines(tasks)
    print("Task deleted.")

# Demo usage
add_task("Buy groceries")
add_task("Complete Python project")
view_tasks()
delete_task(1)
view_tasks()
