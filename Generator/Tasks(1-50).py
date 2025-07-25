# Basics of Generator Functions

# 1. Create a generator function to yield numbers from 1 to 10.
def gen_1_to_10():
    for i in range(1, 11):
        yield i

print("1 to 10:", list(gen_1_to_10()))

# 2. Write a generator to yield even numbers from 1 to n.
def gen_evens(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

print("Evens to 10:", list(gen_evens(10)))

# 3. Build a generator that yields squares of numbers from 1 to n.
def gen_squares(n):
    for i in range(1, n + 1):
        yield i * i

print("Squares to 5:", list(gen_squares(5)))

# 4. Create a generator that yields characters from a given string.
def gen_chars(s):
    for ch in s:
        yield ch

print("Chars in 'hello':", list(gen_chars("hello")))

# 5. Build a generator to yield all vowels from a string.
def gen_vowels(s):
    for ch in s:
        if ch.lower() in 'aeiou':
            yield ch

print("Vowels in 'Beautiful Day':", list(gen_vowels("Beautiful Day")))

# 6. Use next() to manually iterate over a generator that yields the first 5 letters of the alphabet.
def gen_first_five_letters():
    for ch in 'abcde':
        yield ch

print("\nManual next() iteration over first 5 letters:")
gen = gen_first_five_letters()
try:
    while True:
        print(next(gen))
except StopIteration:
    print("StopIteration raised, generator exhausted.")

# 7. Show how a generator stops when StopIteration is raised.
# Demonstrated in task 6 above.

# 8. Create a generator that yields prime numbers up to 100.
def gen_primes_upto_100():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, 101):
        if is_prime(num):
            yield num

print("\nPrimes up to 100:", list(gen_primes_upto_100()))

# 9. Compare a list-returning function vs generator (memory-wise) for 100000 elements.
def make_list(n):
    return [i for i in range(n)]

def make_gen(n):
    for i in range(n):
        yield i

import sys
n = 100000
lst = make_list(n)
gen2 = make_gen(n)

print(f"\nMemory of list({n}): {sys.getsizeof(lst)} bytes")
print(f"Memory of generator({n}): {sys.getsizeof(gen2)} bytes")

# 10. Create a generator that accepts a list and yields only positive numbers.
def gen_positive(lst):
    for item in lst:
        if isinstance(item, (int, float)) and item > 0:
            yield item

mixed = [-2, 0, 3, 7, -9, 1]
print("\nPositive numbers from list:", list(gen_positive(mixed)))


# Intermediate Generator Logic 

 # 1. Generator that yields words one-by-one from a paragraph.
def gen_words(paragraph):
    for word in paragraph.split():
        yield word
print("1.", list(gen_words("This is a sample paragraph.")))
# 1. ['This', 'is', 'a', 'sample', 'paragraph.']

# 2. Generator that yields cumulative sum of a list of numbers.
def gen_cumsum(lst):
    total = 0
    for num in lst:
        total += num
        yield total  # running total per iteration—standard generator pattern :contentReference[oaicite:1]{index=1}
print("2.", list(gen_cumsum([1, 2, 3, 4])))
# 2. [1, 3, 6, 10]

# 3. Re-implement range using a generator with yield in a loop.
def gen_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    i = start
    while i < stop:
        yield i
        i += step
print("3.", list(gen_range(5)))
# 3. [0, 1, 2, 3, 4]

# 4. Generator that accepts a nested list and yields flattened values.
import collections
def gen_flatten(nested):
    for x in nested:
        if isinstance(x, collections.abc.Iterable) and not isinstance(x, (str, bytes)):
            yield from gen_flatten(x)
        else:
            yield x  # recursive flattening via yield from—common pattern :contentReference[oaicite:2]{index=2}
print("4.", list(gen_flatten([1, [2, [3, 4], 5], 6])))
# 4. [1, 2, 3, 4, 5, 6]

# 5. Generator that yields factorials up to n.
def gen_factorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact
print("5.", list(gen_factorials(5)))
# 5. [1, 2, 6, 24, 120]

# 6. Generator that yields powers of 2 up to a limit.
def gen_powers_of_two(limit):
    n = 0
    while True:
        value = 2 ** n
        if value > limit:
            break
        yield value
        n += 1
print("6.", list(gen_powers_of_two(20)))
# 6. [1, 2, 4, 8, 16]

# 7. Generate Fibonacci sequence using a generator.
def gen_fibonacci(n_terms):
    a, b = 0, 1
    for _ in range(n_terms):
        yield a
        a, b = b, a + b
print("7.", list(gen_fibonacci(7)))
# 7. [0, 1, 1, 2, 3, 5, 8]

# 8. Generator filtering only even numbers from a list.
def gen_only_evens(lst):
    for num in lst:
        if num % 2 == 0:
            yield num
print("8.", list(gen_only_evens([1, 2, 3, 4, 5, 6])))
# 8. [2, 4, 6]

# 9. Chain two generators: one gives numbers, second squares them.
def gen_numbers(n):
    for i in range(n):
        yield i
def gen_squared(nums_gen):
    for num in nums_gen:
        yield num * num
print("9.", list(gen_squared(gen_numbers(5))))
# 9. [0, 1, 4, 9, 16]

# 10. Reverse generator for a string.
def gen_reverse_string(s):
    for ch in reversed(s):
        yield ch
print("10.", ''.join(gen_reverse_string("hello")))
# 10. 'olleh'



# Generator Expressions


    # 1. Squares of numbers from 1 to 10
squares = (x**2 for x in range(1, 11))
print("1.", list(squares))  # 1. [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2. All odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = (x for x in numbers if x % 2 != 0)
print("2.", list(odds))  # 2. [1, 3, 5, 7, 9]

# 3. Convert a generator expression into a list
gen = (x**3 for x in range(1, 6))
lst = list(gen)
print("3.", lst)  # 3. [1, 8, 27, 64, 125]

# 4. Words longer than 5 characters in a sentence
sentence = "Generator expressions are concise and efficient"
long_words = (w for w in sentence.split() if len(w) > 5)
print("4.", list(long_words))  # 4. ['Generator', 'expressions', 'concise', 'efficient']

# 5. Uppercase letters from a string
text = "Hello World! Python is Great."
uppers = (c for c in text if c.isupper())
print("5.", list(uppers))  # 5. ['H', 'W', 'P', 'G']

# 6. Compare memory usage: generator vs list comprehension for large range
import sys
gen_large = (x for x in range(10_000_000))
lst_large = [x for x in range(10_000_000)]
print("6. Generator size:", sys.getsizeof(gen_large), "List size:", sys.getsizeof(lst_large))
# e.g. Generator size: ~112 bytes List size: ~80_000_000 bytes (varies)

# 7. Use generator expression with sum()
total = sum(x for x in range(1, 101))
print("7.", total)  # 7. 5050

# 8. Filter floats from a mixed list
mixed = [1, 2.5, 'a', 3.14, 4, 5.0, 'hello']
floats = (x for x in mixed if isinstance(x, float))
print("8.", list(floats))  # 8. [2.5, 3.14, 5.0]

# 9. any() to check if any number is divisible by 3
nums = [1, 2, 4, 5, 7, 8, 9]
has_div3 = any(x % 3 == 0 for x in nums)
print("9.", has_div3)  # 9. True

# 10. max() to get the highest number
more_nums = [10, 3, 25, 7, 42, 18]
highest = max(x for x in more_nums)
print("10.", highest)  # 10. 42


# Advanced Generator Techniques

# 1. Infinite generator yielding multiples of 5
def gen_multiples_of_5():
    i = 1
    while True:
        yield 5 * i
        i += 1

# Demo (print first 5 multiples)
inf5 = gen_multiples_of_5()
print("1.", [next(inf5) for _ in range(5)])  # 1. [5, 10, 15, 20, 25]

# 2. Generator to chunk an iterable into parts of 3
def gen_chunks(iterable, size=3):
    it = iter(iterable)
    while chunk := list(__import__('itertools').islice(it, size)):
        yield chunk

print("2.", list(gen_chunks(range(10), 3)))
# 2. [[0,1,2], [3,4,5], [6,7,8], [9]]

# 3. Generator that accepts list of names and yields sorted names
def gen_sorted_names(names):
    for name in sorted(names):
        yield name

print("3.", list(gen_sorted_names(["Charlie", "Alice", "Bob"])))
# 3. ['Alice', 'Bob', 'Charlie']

# 4. Yield reversed lines from a file (generator)
def gen_reversed_lines(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.rstrip('\n')[::-1]

# (Demo omitted due to missing file)

# 5. Countdown generator yielding from n to 0
def gen_countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("5.", list(gen_countdown(5)))  # 5. [5,4,3,2,1,0]

# 6. Generator that logs yield points
def gen_with_log(n):
    for i in range(n):
        print(f"Yielding i={i}")
        yield i

print("6.", list(gen_with_log(3)))
# Logs: Yielding i=0,1,2, then prints list

# 7. Generator with send(), doubling values sent in :contentReference[oaicite:1]{index=1}
def gen_doubler():
    value = None
    while True:
        received = yield value
        if received is None:
            continue
        value = received * 2

d = gen_doubler()
next(d)                # Prime
print("7.", d.send(5))  # 10
print("7.", d.send(8))  # 16

# 8. Use return in a generator and catch StopIteration.value :contentReference[oaicite:2]{index=2}
def gen_with_return(n):
    for i in range(n):
        yield i
    return "Done!"

g = gen_with_return(3)
try:
    for x in g:
        print("8 yields:", x)
except StopIteration as e:
    print("8 return:", e.value)  # "Done!"

# 9. CSV line reader using generator
def gen_csv_lines(filepath):
    with open(filepath, newline='') as f:
        for line in f:
            yield line.strip().split(',')

# (Demo omitted—needs a CSV file to read)

# 10. Generator that counts how many times yield is called
def gen_yield_counter(n):
    count = 0
    for i in range(n):
        count += 1
        yield i
    print(f"Yield was called {count} times")

print("10:", list(gen_yield_counter(4)))
# Logs: "Yield was called 4 times"


# Real-Life Generator Use Cases

import time
import random

# 1. Log file reader generator: yields one log entry at a time.
def gen_log_reader(filepath):
    # Similar to tail -f; reads new lines as they arrive.
    with open(filepath, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line.rstrip('\n')

# Demo: (Assume 'app.log' exists and is being written to)
# for i, entry in zip(range(3), gen_log_reader('app.log')):
#     print("Log entry:", entry)

# 2. Simulate sensor data stream using a generator that yields values every 1 second.
def gen_sensor_data():
    while True:
        yield round(20 + random.random() * 5, 2)  # e.g. temperature
        time.sleep(1)

# Demo: print first 3 sensor readings
sensor = gen_sensor_data()
print("2. Sensor data:", [next(sensor) for _ in range(3)])

# 3. Paginate API results via a mocked generator
def gen_paginated_api(total_pages=3, per_page=5):
    for page in range(1, total_pages + 1):
        # simulate fetching page data
        yield [f"item_{page}_{i}" for i in range(per_page)]

print("3. Pages:", list(gen_paginated_api()))

# 4. Streaming price monitor (mock real-time stock prices)
def gen_price_monitor(symbols):
    # In real-world, fetch live quotes; here we simulate.
    while True:
        prices = {sym: round(100 + random.uniform(-1, 1), 2) for sym in symbols}
        yield prices
        time.sleep(1)

monitor = gen_price_monitor(['AAPL', 'TSLA'])
print("4. Price snapshot:", next(monitor))

# 5. Form validation simulation: each yield is a field check result.
def gen_form_validator(form_data):
    for field, value in form_data.items():
        valid = bool(value and isinstance(value, str))
        yield (field, valid)

form = {'name': 'Alice', 'email': 'alice@example.com', 'age': ''}
print("5. Field validation:", list(gen_form_validator(form)))


# Generator Comparison and Integration 
import timeit, sys, itertools, re

# 1. Compare list vs generator iterating 10 million numbers
setup = "from __main__ import iter_list, iter_gen"
iter_list = lambda: sum([i for i in range(10_000_000)])
iter_gen = lambda: sum((i for i in range(10_000_000)))
t_list = timeit.timeit("iter_list()", setup=setup, number=1)
t_gen = timeit.timeit("iter_gen()", setup=setup, number=1)
print(f"1. List time: {t_list:.2f}s, Generator time: {t_gen:.2f}s")
# Using memory check:
gen_obj = (i for i in range(10_000_000))
lst_obj = list(range(10_000_000))
print("   Mem generator:", sys.getsizeof(gen_obj),
      "Mem list:", sys.getsizeof(lst_obj))
# Observation: list is faster but uses ~80MB vs generator ~112B :contentReference[oaicite:1]{index=1}

# 2. Integrate a generator with map() to transform each yielded value
def gen_nums(n):
    for i in range(n):
        yield i
mapped = map(lambda x: x * x, gen_nums(5))
print("2.", list(mapped))  # [0,1,4,9,16]

# 3. Generator pipeline: numbers -> even filter -> square
def gen_pipeline(n):
    return (x * x for x in gen_nums(n) if x % 2 == 0)
print("3.", list(gen_pipeline(10)))  # [0,4,16,36,64]

# 4. Use generator in a for loop to simulate reading user input commands
def gen_input(cmds):
    for cmd in cmds:
        yield cmd
# Demo:
commands = ["help", "start", "stop", "exit"]
print("4.")
for c in gen_input(commands):
    print("Received:", c)
    if c == "exit":
        break

# 5. Unit tests for a generator that returns only valid emails
def gen_valid_emails(items):
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    for item in items:
        if pattern.match(item):
            yield item

# Unit tests
def test_gen_valid_emails():
    inputs = ["a@b.com", "nope", "x@y.co", "bad@", "@bad.com"]
    expected = ["a@b.com", "x@y.co"]
    assert list(gen_valid_emails(inputs)) == expected

# Run test
try:
    test_gen_valid_emails()
    print("5. Unit test passed ✅")
except AssertionError:
    print("5. Unit test failed ❌")



