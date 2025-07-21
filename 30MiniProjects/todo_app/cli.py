from task_ops import add_task, complete_task, delete_task, show_tasks, show_overdue

def main():
    print("📝 Welcome to Task Tracker")

    while True:
        print("\n1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Show All Tasks")
        print("5. Show Tasks Grouped by Priority")
        print("6. Show Overdue Tasks")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task Title: ")
            due = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (High/Medium/Low): ")
            tags = input("Tags (comma-separated): ").split(",")
            add_task(title, due, priority, [tag.strip() for tag in tags])
        elif choice == '2':
            title = input("Task Title to Complete: ")
            complete_task(title)
        elif choice == '3':
            title = input("Task Title to Delete: ")
            delete_task(title)
        elif choice == '4':
            show_tasks()
        elif choice == '5':
            show_tasks(group_by="priority")
        elif choice == '6':
            show_overdue()
        elif choice == '7':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
