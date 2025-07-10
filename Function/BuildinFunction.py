from functools import reduce

# Task 36: Use map() and lambda to square every element in a list
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares →", squares)
print("-"*40)

# Task 37: Use filter() to remove all odd numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers →", even_numbers)
print("-"*40)

# Task 38: Use map() to convert a list of strings to uppercase
words = ["python", "lambda", "map", "filter"]
uppercase_words = list(map(lambda w: w.upper(), words))
print("Uppercase Words →", uppercase_words)
print("-"*40)

# Task 39: Use reduce() to calculate the product of a list
product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers →", product)
print("-"*40)

# Task 40: Use filter() to return words longer than 5 characters
long_words = list(filter(lambda w: len(w) > 5, words))
print("Words Longer Than 5 Characters →", long_words)
print("-"*40)