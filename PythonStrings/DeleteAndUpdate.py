# SECTION 3: Deleting and Updating Strings (16–20)

#  Task 16: Create a string and delete it using del, then try to print it (catch the error)
try:
    greeting = "Hello, world!"
    del greeting
    print(greeting)  # This will raise a NameError since greeting is deleted
except NameError:
    print("Task 16: The variable 'greeting' was deleted and no longer exists.")

print("-" * 40)

#  Task 17: Concatenate two strings using + and print the result
first = "Python"
second = "Rocks"
combined = first + " " + second
print("Task 17:", combined)

print("-" * 40)

#  Task 18: Write a program that takes a name and appends "Welcome!" to it
name = input("Task 18 - Enter your name: ").strip()
message = name + ", Welcome!"
print(message)

print("-" * 40)

#  Task 19: Take user input and create a new sentence by combining it with a fixed phrase
hobby = input("Task 19 - Enter your hobby: ").strip()
sentence = "It's great that you enjoy " + hobby + "!"
print(sentence)

print("-" * 40)

# Task 20: Repeat a string 3 times using * operator
word = "Hi! "
repeated = word * 3
print("Task 20:", repeated)
