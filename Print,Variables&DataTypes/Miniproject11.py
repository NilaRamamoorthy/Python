task1 = input("Enter Task 1: ")
task2 = input("Enter Task 2: ")
task3 = input("Enter Task 3: ")
tasks = [task1, task2, task3]
print("\nYour To-Do List:")
print(tasks)

print("\nTask Details:")
for index in range(len(tasks)):
    print(f"{index}  {tasks[index]}")
