# Task 21: Loop from 1 to 10 and break the loop if number is 5
print("Task 21:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)
print()

# Task 22: Loop from 1 to 10 and continue (skip) if the number is 5
print("Task 22:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print()

# Task 23: Use pass in a loop where you want to add code later
print("Task 23:")
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
print()

# Task 24: Ask the user to enter 5 numbers, break if a number is negative
print("Task 24:")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    if num < 0:
        print("Negative number entered. Breaking loop.")
        break
print()

# Task 25: Use continue to skip even numbers and print only odd numbers from 1 to 10
print("Task 25:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print()

# Task 26: Print numbers from 1 to 3, and print “Loop complete!” using else with loop
print("Task 26:")
for i in range(1, 4):
    print(i)
else:
    print("Loop complete!")
print()

# Task 27: Print all elements in a list, but stop the loop if the item is "Stop"
print("Task 27:")
items = ["Apple", "Banana", "Stop", "Grapes"]
for item in items:
    if item == "Stop":
        break
    print(item)
print()

# Task 28: Loop through "VetriTech" and skip the letter "T" using continue
print("Task 28:")
for char in "VetriTech":
    if char == "T" or char == "t":
        continue
    print(char)
print()

# Task 29: Loop through 1 to 10. Use pass when number is divisible by 3
print("Task 29:")
for i in range(1, 11):
    if i % 3 == 0:
        pass  # Skipped processing for now
    print(i)
print()

# Task 30: Demonstrate a for loop that runs else when loop completes without break
print("Task 30:")
for i in range(1, 6):
    print(i)
else:
    print("Loop completed without break.")
