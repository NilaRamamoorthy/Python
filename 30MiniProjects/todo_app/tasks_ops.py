from datetime import datetime

tasks = []

def add_task(title, due_date, priority, tags):
    task = {
        "title": title,
        "due_date": due_date,
        "priority": priority,
        "tags": set(tags),
        "completed": False
    }
    tasks.append(task)
    print("✅ Task added.")

def complete_task(title):
    for task in tasks:
        if task["title"].lower() == title.lower():
            task["completed"] = True
            print("✅ Task marked as completed.")
            return
    print("❌ Task not found.")

def delete_task(title):
    global tasks
    tasks = [task for task in tasks if task["title"].lower() != title.lower()]
    print("🗑️ Task deleted (if it existed).")

def show_tasks(group_by=None):
    if not tasks:
        print("📭 No tasks found.")
        return

    if group_by == "priority":
        groups = {}
        for task in tasks:
            key = task["priority"]
            groups.setdefault(key, []).append(task)
        for prio, group in groups.items():
            print(f"\n🔵 Priority: {prio}")
            for t in group:
                status = "✅" if t["completed"] else "❌"
                print(f" - {t['title']} (Due: {t['due_date']}, Tags: {', '.join(t['tags'])}) {status}")
    else:
        for task in tasks:
            status = "✅" if task["completed"] else "❌"
            print(f"- {task['title']} | Due: {task['due_date']} | Priority: {task['priority']} | Tags: {', '.join(task['tags'])} {status}")

def show_overdue():
    today = datetime.today().date()
    print("\n⚠️ Overdue Tasks:")
    for task in tasks:
        due = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        if due < today and not task["completed"]:
            print(f"- {task['title']} (Due: {task['due_date']}) ❌")
