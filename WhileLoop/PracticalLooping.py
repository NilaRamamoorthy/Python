# Task 46: Ask the user to input 5 student names using while and store them in a list.
students = []
count = 0
while count < 5:
    name = input("Enter student name: ")
    if name:
        students.append(name)
        count += 1
print("\nStudent List:", students)
print("-"*40)

# Task 47: Create a menu-driven loop for a to-do list app (add, view, remove, exit).
todo_list = []
while True:
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task to add: ")
        todo_list.append(task)
    elif choice == "2":
        print("\nCurrent Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
        else:
            print("Task not found.")
    elif choice == "4":
        print("Exiting To-Do List App.")
        break
    else:
        print("Invalid option.")

print("-"*40)

# Task 48: Ask the user to enter age of 5 people. Print how many are adults (age ≥ 18).
adults = 0
count = 0
while count < 5:
    age = int(input(f"Enter age of person {count+1}: "))
    if age >= 18:
        adults += 1
    count += 1
print(f"\nNumber of adults: {adults}")

print("-"*40)

# Task 49: Create a quiz loop: keep asking until the user gets the correct answer.
answer = "python"
while True:
    user_input = input("What programming language are we learning? ").lower()
    if user_input == answer:
        print("Correct!")
        break
    else:
        print("Try again.")

print("-"*40)

# Task 50: Build a basic number guessing game. User keeps guessing until the correct number is entered.
secret_number = 7
while True:
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    else:
        print("Wrong guess. Try again.")
print("-"*40)