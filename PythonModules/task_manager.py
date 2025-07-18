from task_manager.tasks import add_task, update_task, delete_task, list_tasks

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            desc = input("Enter description: ")
            add_task(title, desc)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            status = input("Enter new status (Pending/In Progress/Done): ")
            update_task(task_id, status)
        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
