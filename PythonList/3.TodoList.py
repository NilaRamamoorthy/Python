# To-Do List Manager

# Initial to-do list
todo_list = ["Wake up", "Exercise", "Check emails", "Attend class", "Work on project"]

# Display all tasks with their index using enumerate
print("📋 Today's To-Do List:")
for index, task in enumerate(todo_list, start=1):
    print(f"{index}. {task}")

# Marking a task as complete (remove or pop)
completed_task = todo_list.pop(1)  # Removing the second task: "Exercise"
print(f"\n✅ Completed task: {completed_task}")

# Show top 2 priority tasks using slicing
print("\n🔥 Top 2 Priority Tasks:")
for task in todo_list[:2]:
    print("-", task)

# Display updated to-do list
print("\n🆕 Updated To-Do List:")
for index, task in enumerate(todo_list, start=1):
    print(f"{index}. {task}")
