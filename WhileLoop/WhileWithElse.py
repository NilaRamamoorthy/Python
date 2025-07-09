# Task 41: Print numbers from 1 to 3. Use else to print "Loop Finished".
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop Finished")

print("-"*40)

# Task 42: Ask the user to enter 3 numbers. Use else to say “All numbers entered successfully”.
count = 0
while count < 3:
    num = input("Enter a number: ")
    if num.strip() == "":
        print("Empty input. Try again.")
        break
    count += 1
else:
    print("All numbers entered successfully")

print("-"*40)

# Task 43: Run a loop to print even numbers till 10. Use break to exit early. Ensure else doesn’t run.
i = 2
while i <= 10:
    print(i)
    if i == 6:
        break
    i += 2
else:
    print("Completed without break")  # This will not run due to break

print("-"*40)

# Task 44: Print numbers from 1 to 5. If loop finishes without break, print “Nice job!”.
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Nice job!")

print("-"*40)

# Task 45: Create a password checker with 3 attempts. If successful, print inside else.
correct_password = "admin123"
attempts = 0
while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password")
    attempts += 1
else:
    print("Access denied after 3 attempts")
print("-"*40)