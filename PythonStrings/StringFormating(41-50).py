# SECTION 6: String Formatting (41–50)

# 41 Use f-string to print “My name is John and I am 30 years old.”
name="John"
age=30
print(f"My name is {name} and I am {age} years old.")
print("-"*40)

# 42 Use .format() to insert 2 numbers and print their sum.
num1=5
num2=3
print("Sum of {} and {} is {}".format(num1,num2,num1+num2))

# 43 Use % formatting to display the price of a product: "%s costs ₹%.2f"
product="Shirt"
cost=2899
cost=float(cost)
print("%s costs ₹%.2f"%(product,cost))

# Task 44: Create a function that takes name and marks and prints a result using all 3 formatting methods
def display_result(name, marks):
    # f-string
    print(f"Task 44 (f-string): {name} scored {marks} marks.")
    # .format()
    print("Task 44 (.format): {} scored {} marks.".format(name, marks))
    # % formatting
    print("Task 44 (% formatting): %s scored %d marks." % (name, marks))
display_result("Nila", 95)

print("-" * 40)

# Task 45: Format a list of products and their prices into a formatted table using f-strings
products = [("Milk", 45), ("Bread", 30), ("Eggs", 60), ("Sugar", 40)]

print("Task 45: Product Price Table")
print(f"{'Product':<10} | {'Price (₹)':>10}")
print("-" * 25)
for item, price in products:
    print(f"{item:<10} | {price:>10}")

print("-" * 40)

# Task 46: Ask for user input (name, age) and print using .format()
name = input("Task 46 - Enter your name: ").strip()
age = input("Task 46 - Enter your age: ").strip()
print("Hello, {}! You are {} years old.".format(name, age))


# 47 Print temperature conversion: "Temperature is 35°C or 95°F" using f-string.
celsius=input("Enter temperature in °C: ").strip()
farenheit=(celsius * 9/5) + 32
print(f"Temperature is {celsius}°C or {farenheit}°F")

# 48 Format a sentence where the price changes dynamically: "The discounted price is ₹999"
price = 999
print(f"The discounted price is ₹{price}")

# 49 Write a function that accepts employee details and formats them using f-string.
def format_employee(name, emp_id, department, salary):
    return f"Employee: {name} | ID: {emp_id} | Department: {department} | Salary: ₹{salary:.2f}"

print(format_employee("Anjali", "EMP102", "HR", 55000.75))

# 50 Create a dynamic weather report sentence using all formatting styles.
city = "Mumbai"
temperature = 33.5
humidity = 60

# 1. Using f-string
print(f"Weather in {city}: {temperature}°C, {humidity}% humidity")

# 2. Using .format()
print("Weather in {}: {}°C, {}% humidity".format(city, temperature, humidity))

# 3. Using % formatting
print("Weather in %s: %.1f°C, %d%% humidity" % (city, temperature, humidity))
