#Task 26: Print numbers from 1 to 10 and break the loop if number is 6.
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

print("-"*40)

#  Task 27: Ask the user to enter numbers. Break the loop when user enters 0.
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print(f"You entered: {num}")
print("-"*40)

# Task 28: Create a simple password checker. Break the loop if the correct password is entered.
correct_password = "admin123"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access Granted")
        break
    else:
        print("Incorrect password")

print("-"*40)

# Task 29: Print numbers from 1 to 100. Break the loop when a number divisible by 17 is found.
n = 1
while n <= 100:
    if n % 17 == 0:
        print(f"Found number divisible by 17: {n}")
        break
    n += 1

print("-"*40)

# Task 30: Keep asking for user input until they type "exit" (use break to stop).
while True:
    text = input("Type something (or 'exit' to quit): ")
    if text.lower() == "exit":
        break
    print(f"You typed: {text}")

print("-"*40)

# Task 31: Simulate a game loop: “Press q to quit”.
while True:
    key = input("Press a key (q to quit): ")
    if key.lower() == 'q':
        print("Game Ended")
        break

print("-"*40)

# Task 32: Ask the user 10 questions, stop early if any answer is empty using break.
question_num = 1
while question_num <= 10:
    ans = input(f"Answer question {question_num}: ")
    if ans.strip() == "":
        print("Empty answer. Stopping early.")
        break
    question_num += 1
print("-"*40)

#  Task 33: Simulate 3 login attempts. Break the loop if login is successful.
correct_username = "user"
correct_password = "pass"
attempt = 0
while attempt < 3:
    username = input("Username: ")
    password = input("Password: ")
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid credentials")
        attempt += 1

print("-"*40)

# Task 34: Print the multiplication table of 5, but stop if the product exceeds 30.
i = 1
while True:
    product = 5 * i
    if product > 30:
        break
    print(f"5 x {i} = {product}")
    i += 1

print("-"*40)

# Task 35: Count from 1 to 10. If number is 7, break the loop and print “Loop Interrupted”.
i = 1
while i <= 10:
    if i == 7:
        print("Loop Interrupted at 7")
        break
    print(i)
    i += 1
print("-"*40)