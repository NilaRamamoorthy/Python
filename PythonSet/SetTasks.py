# Python Mini Projects Using Sets

# 1. Create a set of favorite fruits and print it.
favorite_fruits = {"apple", "banana", "mango"}
print("Favorite Fruits:", favorite_fruits)

# 2. Convert a list with duplicate values into a unique set.
fruits_list = ["apple", "banana", "apple", "orange"]
unique_fruits = set(fruits_list)
print("Unique Fruits:", unique_fruits)

# 3. Check if a given item exists in a set using the in keyword.
print("banana" in unique_fruits)

# 4. Create a set from a string and print all unique characters.
unique_chars = set("hello world")
print("Unique Characters:", unique_chars)

# 5. Iterate through a set and print each element.
for fruit in favorite_fruits:
    print(fruit)

# 6. Create an empty set and add five movie names using add().
movies = set()
movies.add("Inception")
movies.add("Avatar")
movies.add("Titanic")
movies.add("Interstellar")
movies.add("Gladiator")
print(movies)

# 7. Add multiple subjects to a set using update() from a list.
subjects = {"Math", "Science"}
subjects.update(["English", "History"])
print(subjects)

# 8. Add multiple letters from a string into a set using update().
letters = set()
letters.update("python")
print(letters)

# 9. Remove a specific city from a set using remove().
cities = {"Chennai", "Delhi", "Mumbai"}
cities.remove("Delhi")
print(cities)

# 10. Try to remove an element using discard() and avoid an error if not present.
cities.discard("Kolkata")  # No error even if not present
print(cities)

# 11. Remove a random item from a set using pop() and print it.
removed_item = cities.pop()
print("Removed:", removed_item)

# 12. Clear all elements from a set using clear() and check if it is empty.
cities.clear()
print("Is empty:", len(cities) == 0)

# 13. Find the union of two sets of programming languages.
set1 = {"Python", "Java"}
set2 = {"C++", "Java"}
print("Union:", set1 | set2)

# 14. Find the intersection of two sets of sports.
sports1 = {"Cricket", "Football", "Hockey"}
sports2 = {"Football", "Tennis"}
print("Intersection:", sports1 & sports2)

# 15. Find the difference between set A and set B (A - B).
print("Difference:", sports1 - sports2)

# 16. Find the symmetric difference (items in either set, but not both).
print("Symmetric Difference:", sports1 ^ sports2)

# 17. Perform chained operations like (A | B) - (A & B) on two sets.
print("Chained Operation:", (set1 | set2) - (set1 & set2))

# 18. Check if a set of backend skills is a subset of full-stack skills.
backend = {"Python", "SQL"}
fullstack = {"HTML", "CSS", "Python", "SQL"}
print("Is subset:", backend.issubset(fullstack))

# 19. Verify if a set of developers is a superset of testers.
developers = {"Alice", "Bob", "Charlie"}
testers = {"Alice"}
print("Is superset:", developers.issuperset(testers))

# 20. Determine if two sets of colors are disjoint (no common elements).
colors1 = {"red", "green"}
colors2 = {"blue", "yellow"}
print("Is disjoint:", colors1.isdisjoint(colors2))

# 21. Use multiple sets to test all subset-superset combinations.
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b), b.issuperset(a))

# 22. Demonstrate a real-life case of issubset() using required course completions.
required_courses = {"Python", "Git"}
completed_courses = {"Python", "Git", "SQL"}
print(required_courses.issubset(completed_courses))

# 23. Create a backup of a set using copy() and show that modifying the copy doesn’t affect the original.
original = {"A", "B"}
backup = original.copy()
backup.add("C")
print("Original:", original)
print("Backup:", backup)

# 24. Create a frozenset of vowels and demonstrate immutability.
vowels = frozenset("aeiou")
print("Frozenset:", vowels)

# 25. Try to add an element to a frozenset and catch the error gracefully.
try:
    vowels.add("x")
except AttributeError as e:
    print("Error:", e)

# 26. Use a frozenset as a key in a dictionary for caching purposes.
cache = {frozenset([1, 2]): "Cached Result"}
print("From cache:", cache[frozenset([1, 2])])

# 27. Generate a set of even numbers from 1 to 20 using set comprehension.
evens = {x for x in range(1, 21) if x % 2 == 0}
print("Even Numbers:", evens)

# 28. Generate a set of unique lowercase characters from a sentence using set comprehension.
sentence = "Hello World"
lower_chars = {ch for ch in sentence.lower() if ch.isalpha()}
print("Unique lowercase chars:", lower_chars)

# 29. Create a set of squares for numbers 1 to 10 using set comprehension.
squares = {x**2 for x in range(1, 11)}
print("Squares:", squares)

# 30. Use a set comprehension to filter out vowels from a sentence.
filtered = {ch for ch in "OpenAI creates AI tools" if ch.lower() not in "aeiou" and ch.isalpha()}
print("Filtered Set:", filtered)

# 31. Store a list of registered users and block users, then find the allowed users using set difference.
registered = {"user1", "user2", "user3"}
blocked = {"user2"}
allowed = registered - blocked
print("Allowed users:", allowed)

# 32. Use sets to find students enrolled in both Python and Java courses (intersection).
python_students = {"Alice", "Bob", "Eve"}
java_students = {"Bob", "Charlie"}
print("Both Courses:", python_students & java_students)

# 33. Compare two sets of stock symbols to find new listings (difference).
existing = {"AAPL", "GOOG"}
new = {"AAPL", "TSLA"}
print("New Listings:", new - existing)

# 34. Track users who logged in either yesterday or today (union).
yesterday = {"Alice", "David"}
today = {"Bob", "Alice"}
print("Logged In:", yesterday | today)

# 35. Identify users who changed passwords on only one of the two days (symmetric difference).
print("Changed Password Only Once:", yesterday ^ today)

# 36. Detect duplicate entries in a list of product SKUs using sets.
skus = ["SKU1", "SKU2", "SKU1", "SKU3"]
duplicates = set([sku for sku in skus if skus.count(sku) > 1])
print("Duplicate SKUs:", duplicates)

# 37. Create a set from a CSV file’s column and count unique entries.
csv_column = ["apple", "banana", "apple", "cherry"]
unique_entries = set(csv_column)
print("Unique CSV entries:", unique_entries)

# 38. Build a unique tag manager system for blog posts using sets.
tags = set()
tags.update(["python", "ai", "ml"])
tags.update(["data", "python"])
print("Unique Tags:", tags)

# 39. Check if a given list of security permissions is covered by the default permission set.
required_perms = {"read", "write"}
default_perms = {"read", "write", "execute"}
print("Permissions covered:", required_perms.issubset(default_perms))

# 40. Create two sets from random numbers and apply all operations: union, intersection, etc.
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# 41. Build a contact manager that stores unique email addresses using a set.
emails = set(["a@example.com", "b@example.com", "a@example.com"])
print("Emails:", emails)

# 42. Store completed achievements of players and check who earned all major trophies.
player_achievements = {"trophy1", "trophy2"}
major_trophies = {"trophy1", "trophy2", "trophy3"}
print("All trophies won:", major_trophies.issubset(player_achievements))

# 43. Keep track of unique IPs from a server log using a set.
ips = set()
ips.update(["192.168.0.1", "192.168.0.2", "192.168.0.1"])
print("Unique IPs:", ips)

# 44. Extract unique hashtags from a list of tweets using sets.
tweets = ["#ai", "#ml", "#ai", "#python"]
hashtags = set(tweets)
print("Unique Hashtags:", hashtags)

# 45. Track unique book titles from multiple libraries using update().
library1 = {"Book A", "Book B"}
library2 = {"Book B", "Book C"}
all_books = set()
all_books.update(library1)
all_books.update(library2)
print("All Books:", all_books)

# 46. Validate if all required modules are installed using issubset() on installed_modules.
required = {"flask", "sqlalchemy"}
installed = {"flask", "sqlalchemy", "requests"}
print("All modules installed:", required.issubset(installed))

# 47. Try removing a non-existent item using remove() and handle the exception.
test_set = {"A", "B"}
try:
    test_set.remove("Z")
except KeyError:
    print("Item not found, handled!")

# 48. Explain the difference between remove() and discard() using a test set.
test_set = {"X", "Y"}
test_set.discard("Z")  # No error
try:
    test_set.remove("Z")  # Error
except KeyError as e:
    print("remove() Error:", e)

# 49. Create a set from a list with mixed datatypes and remove all integers using set comprehension.
mixed_list = [1, "hello", 2, "world"]
filtered_set = {item for item in set(mixed_list) if not isinstance(item, int)}
print("Filtered Set:", filtered_set)

# 50. Create a set of characters from a multiline text, excluding punctuation.
text = "Hello! How are you? Let's code."
clean_chars = {ch for ch in text if ch.isalpha()}
print("Character Set:", clean_chars)
