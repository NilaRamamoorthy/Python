import time
from datetime import datetime, date
from functools import wraps

# ========== Decorator ==========
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[{func.__name__}] executed in {time.time() - start:.4f} seconds")
        return result
    return wrapper

# ========== OOP: Task Class ==========
class Task:
    def __init__(self, name, deadline, status=False):
        self.name = name
        self.deadline = deadline  # store as tuple (YYYY, MM, DD)
        self.status = status

    def is_overdue(self):
        return date.today() > date(*self.deadline)

    def due_today(self):
        return date.today() == date(*self.deadline)

    def __str__(self):
        due = date(*self.deadline).strftime("%Y-%m-%d")
        status = "✔️ Done" if self.status else "❌ Pending"
        overdue = "⚠️ Overdue!" if not self.status and self.is_overdue() else ""
        return f"{self.name} | Due: {due} | {status} {overdue}"

# ========== Task Manager ==========
class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def __iter__(self):
        return (task for task in self.tasks if not task.status)

    @timeit
    def add_task(self, name, deadline_str):
        try:
            deadline = tuple(map(int, deadline_str.split("-")))
            datetime(*deadline)  # Validate date
            task = Task(name, deadline)
            self.tasks.append(task)
            print("[+] Task added.")
        except ValueError:
            print("[!] Invalid date format. Use YYYY-MM-DD.")

    @timeit
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = True
            print("[✔️] Task marked as complete.")
        else:
            print("[!] Invalid task index.")

    @timeit
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"[🗑️] Task '{removed.name}' deleted.")
        else:
            print("[!] Invalid task index.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n-- To-Do List --")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def save_tasks(self):
        with open(self.filename, "w") as f:
            for task in self.tasks:
                line = f"{task.name}|{','.join(map(str, task.deadline))}|{task.status}\n"
                f.write(line)
        print("[💾] Tasks saved.")

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    name, date_str, status = line.strip().split("|")
                    deadline = tuple(map(int, date_str.split(",")))
                    self.tasks.append(Task(name, deadline, status == "True"))
        except FileNotFoundError:
            open(self.filename, "w").close()

    def generate_due_today(self):
        return (task for task in self.tasks if task.due_today() and not task.status)

# ========== Main Menu ==========
def main():
    tm = TaskManager()

    menu = """
--- To-Do Reminder App ---
1. Add Task
2. Complete Task
3. Delete Task
4. View Tasks
5. View Tasks Due Today
6. Save and Exit
"""

    while True:
        print(menu)
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Task Name: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            tm.add_task(name, deadline)

        elif choice == "2":
            tm.show_tasks()
            idx = int(input("Enter task index to mark complete: "))
            tm.complete_task(idx)

        elif choice == "3":
            tm.show_tasks()
            idx = int(input("Enter task index to delete: "))
            tm.delete_task(idx)

        elif choice == "4":
            tm.show_tasks()

        elif choice == "5":
            print("\n-- Tasks Due Today --")
            for task in tm.generate_due_today():
                print(task)

        elif choice == "6":
            tm.save_tasks()
            print("Exiting. Goodbye!")
            break

        else:
            print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
