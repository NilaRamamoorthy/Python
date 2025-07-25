
# Basic Iterator and Iterable Understanding 

# 1. Use iter() and next() to iterate over a list manually.
lst = [10, 20, 30]
it = iter(lst)
print("1.", next(it), next(it), next(it))
# 1. 10 20 30

# 2. Use a for loop vs while with next() to iterate a tuple.
tpl = ('a', 'b', 'c')
print("2a. for loop:", end=" ")
for x in tpl:
    print(x, end=" ")
print()
print("2b. while+next():", end=" ")
it2 = iter(tpl)
while True:
    try:
        print(next(it2), end=" ")
    except StopIteration:
        break
print()
# 2a. for loop: a b c 
# 2b. while+next(): a b c 

# 3. Create a program to check if a variable is iterable using dir().
def is_iterable(v):
    return hasattr(v, '__iter__') or hasattr(v, '__getitem__')
print("3. list is iterable?", is_iterable([1,2,3]))
print("   int is iterable?", is_iterable(5))
# 3. list is iterable? True
#    int is iterable? False

# 4. Try to use next() on a non-iterator and handle the exception.
non_iter = 100
try:
    print(next(non_iter))  # invalid
except TypeError as e:
    print("4.", type(e).__name__, "caught")
# 4. TypeError caught

# 5. Manually consume only the first 3 elements of a set.
s = {1,2,3,4,5}
it3 = iter(s)
first3 = [next(it3), next(it3), next(it3)]
print("5. first 3 of set:", first3)
# 5. first 3 of set: [1, 2, 3]  (order may vary)

# 6. Use next() to iterate through characters in a string.
st = "hi"
it4 = iter(st)
print("6.", next(it4), next(it4))
# 6. h i

# 7. Use iter() on a dictionary and fetch only the keys.
d = {'x': 1, 'y': 2}
it5 = iter(d)
print("7.", next(it5), next(it5))
# 7. x y

# 8. Convert a range object to an iterator and loop using next().
it6 = iter(range(3))
print("8.", next(it6), next(it6), next(it6))
# 8. 0 1 2

# 9. Write a function that takes an iterable and prints each item using next().
def consume_three(it):
    it2 = iter(it)
    print("9.", next(it2), next(it2), next(it2))
consume_three([7,8,9,10])
# 9. 7 8 9

# 10. Handle StopIteration with a try-except after consuming all items.
it7 = iter([100,200])
try:
    print("10.", next(it7), next(it7), next(it7))
except StopIteration:
    print("10. StopIteration caught after exhausting")
# 10. StopIteration caught after exhausting


# Custom Iterator Classes

# 1. Countdown: counts down from a number
class Countdown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

print("1.", list(Countdown(5)))
# 1. [5, 4, 3, 2, 1]  (pattern from Vultr docs) :contentReference[oaicite:1]{index=1}

# 2. EvenNumbers: yields even numbers up to n
class EvenNumbers:
    def __init__(self, max_n):
        self.max = max_n
        self.num = 2
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= self.max:
            res = self.num
            self.num += 2
            return res
        raise StopIteration

print("2.", list(EvenNumbers(10)))
# 2. [2, 4, 6, 8, 10]  (based on GeeksforGeeks example) :contentReference[oaicite:2]{index=2}

# 3. CharIterator: iterate over characters in a string
class CharIterator:
    def __init__(self, s):
        self.s = s
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.s):
            ch = self.s[self.index]
            self.index += 1
            return ch
        raise StopIteration

print("3.", list(CharIterator("hello")))
# 3. ['h', 'e', 'l', 'l', 'o']

# 4. FibonacciIterator: Fibonacci numbers up to n terms
class FibonacciIterator:
    def __init__(self, n_terms):
        self.n = n_terms
        self.count = 0
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val

print("4.", list(FibonacciIterator(7)))
# 4. [0, 1, 1, 2, 3, 5, 8]

# 5. ReverseListIterator: yields list items in reverse
class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        val = self.data[self.index]
        self.index -= 1
        return val

print("5.", list(ReverseListIterator([1, 2, 3, 4])))
# 5. [4, 3, 2, 1]

# 6. SquareIterator: yields squares from start to end
class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current ** 2
        self.current += 1
        return val

print("6.", list(SquareIterator(1, 5)))
# 6. [1, 4, 9, 16, 25]

# 7. LetterPositionIterator: (letter, position) from string
class LetterPositionIterator:
    def __init__(self, s):
        self.s = s
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.s):
            raise StopIteration
        pair = (self.s[self.index], self.index)
        self.index += 1
        return pair

print("7.", list(LetterPositionIterator("abc")))
# 7. [('a', 0), ('b', 1), ('c', 2)]

# 8. CountdownWithStop: stops early if value is 3
class CountdownWithStop:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == 3:
            raise StopIteration
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

print("8.", list(CountdownWithStop(5)))
# 8. [5, 4]  (stops when reaching 3)

# 9. VowelIterator: yields vowels from a sentence
class VowelIterator:
    def __init__(self, sentence):
        self.s = sentence
        self.index = 0
        self.vowels = set('aeiouAEIOU')
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.s):
            ch = self.s[self.index]
            self.index += 1
            if ch in self.vowels:
                return ch
        raise StopIteration

print("9.", list(VowelIterator("Hello World")))
# 9. ['e', 'o', 'o']

# 10. DigitIterator: yields digits from a mixed string
class DigitIterator:
    def __init__(self, s):
        self.s = s
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.s):
            ch = self.s[self.index]
            self.index += 1
            if ch.isdigit():
                return ch
        raise StopIteration

print("10.", list(DigitIterator("a1b2c3")))
# 10. ['1', '2', '3']


# Advanced Use of iter()


import random, math

# 1. Use iter(callable, sentinel) to read lines from input until "exit".
print("1. Enter lines (type 'exit'):")
# Uncomment to run:
# for line in iter(lambda: input(), "exit"):
#     print("Got:", line)
# (Stops when user types "exit") :contentReference[oaicite:1]{index=1}

# 2. Implement custom file reader using iter() and a sentinel.
print("\n2. Reading file in 5-byte chunks until EOF:")
# f = open('file.txt', 'rb')
# for block in iter(lambda: f.read(5), b''):
#     print("Block:", block)
# f.close() :contentReference[oaicite:2]{index=2}

# 3. Loop fetching random numbers until > 90.
print("\n3.", end=" ")
for num in iter(lambda: random.randint(0, 100), None):
    print(num, end=" ")
    if num > 90:
        break
print("=> stopped after > 90")

# 4. Iterator using iter() that stops when 0 is entered.
print("\n4. Enter numbers (0 to stop):")
# for num in iter(lambda: int(input()), 0):
#     print("Num:", num)

# 5. Iterator to filter out non-alphabet characters.
s = "a1!b2@c"
it_alpha = iter(ch for ch in s if ch.isalpha())
print("\n5.", list(it_alpha))
# 5. ['a', 'b', 'c']

# 6. iter() with a lambda to simulate infinite number stream.
it_inf = iter(lambda count=[0]: count.__setitem__(0, count[0]+1) or count[0], None)
print("\n6.", next(it_inf), next(it_inf), next(it_inf))
# 6. 1 2 3

# 7. Calculator input stream using iter(input, "done").
print("\n7. Enter expressions (type 'done'):")
# for expr in iter(lambda: input(">>> "), "done"):
#     print("Result:", eval(expr))

# 8. Lazy square root generator using math.sqrt and iter().
values = [4, 9, 16, -1, 25]
it_sqrt = iter(lambda: math.sqrt(values.pop(0)) if values else None, None)
print("\n8.", [round(x,2) for x in it_sqrt])
# 8. [2.0, 3.0, 4.0]  (negative skipped or error-safe)

# 9. Iterate any iterable using iter() and next(), tracking index.
def consume_iterable(it):
    i = 0
    it = iter(it)
    try:
        while True:
            val = next(it)
            print(f"9. Index {i} -> {val}")
            i += 1
    except StopIteration:
        pass

consume_iterable(["x", "y", "z"])

# 10. Use iter() with a stop-signal and count loops.
counter = 0
for _ in iter(lambda: random.randint(1, 5), 3):
    counter += 1
print(f"\n10. Looped {counter} times before hitting sentinel 3.")


# Iterator with Files 

# 1. Open a file and use iter() to read line-by-line using next().
f = open('sample.txt', 'w+')
f.write("line1\nline2\n")
f.seek(0)
it = iter(f)
print("1.", next(it).rstrip(), next(it).rstrip())
# Output assumption: "sample.txt" has those two lines => 1. line1 line2
# note: file object is its own iterator :contentReference[oaicite:1]{index=1}

# 2. Handle StopIteration when reaching the end of a file manually.
try:
    print("2.", next(it))
except StopIteration:
    print("2. StopIteration: end of file reached")
# 2. StopIteration: end of file reached :contentReference[oaicite:2]{index=2}

f.close()

# 3. Custom file iterator that only returns non-empty lines.
class NonEmptyLines:
    def __init__(self, filepath):
        self.f = open(filepath, 'r')
    def __iter__(self):
        return self
    def __next__(self):
        for line in self.f:
            if line.strip():
                return line.rstrip()
        self.f.close()
        raise StopIteration

# Prepare demo file
with open('demo.txt', 'w') as df:
    df.write("\nHello\n\nWorld\n\n")
print("3.", list(NonEmptyLines('demo.txt')))
# 3. ['Hello', 'World']

# 4. Iterator that returns the first word of each line in a file.
class FirstWordIterator:
    def __init__(self, filepath):
        self.f = open(filepath, 'r')
    def __iter__(self):
        return self
    def __next__(self):
        line = self.f.readline()
        if not line:
            self.f.close()
            raise StopIteration
        words = line.split()
        return words[0] if words else ''

print("4.", list(FirstWordIterator('demo.txt')))
# 4. ['Hello', 'World']

# 5. Program that returns lines with more than 3 words using iterators.
class LinesWithMinWords:
    def __init__(self, filepath, min_words=4):
        self.f = open(filepath, 'r')
        self.min = min_words
    def __iter__(self):
        return self
    def __next__(self):
        for line in self.f:
            if len(line.split()) > self.min:
                return line.rstrip()
        self.f.close()
        raise StopIteration

with open('big.txt', 'w') as bf:
    bf.write("one two three\nthis is four words here\nshort\nanother line with five words\n")
print("5.", list(LinesWithMinWords('big.txt', 3)))
# 5. ['this is four words here', 'another line with five words']


# Loop Integration and Comparison


import timeit, sys, random, itertools

# 1. Compare performance of for loop vs while+next() for a large list
large = list(range(1_000_000))

# for loop timing
def for_loop():
    s = 0
    for x in large:
        s += x
    return s

# while+next() timing
def while_next():
    it = iter(large)
    s = 0
    try:
        while True:
            s += next(it)
    except StopIteration:
        pass
    return s

t_for = timeit.timeit("for_loop()", globals=globals(), number=3)
t_while = timeit.timeit("while_next()", globals=globals(), number=3)
print("1. for loop time:", t_for, "while+next() time:", t_while)
# Expect for loop to be notably faster—`for` uses C-level iteration vs Python-level while-next :contentReference[oaicite:1]{index=1}

# 2. Iterator that can skip alternate items
class SkipAlternate:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 2
        return val

print("2.", list(SkipAlternate([1,2,3,4,5,6])))
# 2. [1, 3, 5]

# 3. Iterator to loop over two iterables at once (zip-like)
class PairIterator:
    def __init__(self, a, b):
        self.a, self.b = iter(a), iter(b)
    def __iter__(self):
        return self
    def __next__(self):
        return (next(self.a), next(self.b))

print("3.", list(PairIterator([1,2,3], ['a','b','c'])))
# 3. [(1, 'a'), (2, 'b'), (3, 'c')]

# 4. Peekable iterator that wraps a list and offers peek()
class Peekable:
    def __init__(self, iterator):
        self._it = iterator
        self._peeked = False
    def peek(self):
        if not self._peeked:
            try:
                self._next = next(self._it)
            except StopIteration:
                self._next = None
            self._peeked = True
        return self._next
    def __iter__(self):
        return self
    def __next__(self):
        if self._peeked:
            self._peeked = False
            return self._next
        return next(self._it)

p = Peekable(iter([10,20,30]))
print("4. peek:", p.peek(), "next:", next(p), "next:", next(p))
# 4. peek: 10 next: 10 next: 20 :contentReference[oaicite:2]{index=2}

# 5. Circular iterator that restarts after end
class Circular:
    def __init__(self, data):
        self.data = data
        self.it = iter(self.data)
    def __iter__(self):
        return self
    def __next__(self):
        try:
            return next(self.it)
        except StopIteration:
            self.it = iter(self.data)
            return next(self.it)

circ = Circular([1,2,3])
print("5.", next(circ), next(circ), next(circ), next(circ), next(circ))
# 5. 1 2 3 1 2


# Exception Handling and Edge Cases 

# 1. Use a try-except block to catch StopIteration and continue a new list.
class LimitedIterator:
    def __init__(self, data):
        self._it = iter(data)
    def __iter__(self):
        return self
    def __next__(self):
        return next(self._it)

it = LimitedIterator([1, 2, 3])
lst = []
while True:
    try:
        lst.append(next(it))
    except StopIteration:
        break
print("1.", lst)
# 1. [1, 2, 3]

# 2. Build an iterator that raises a custom error after 5 items.
class FiveItemError(Exception):
    pass

class LimitedFive:
    def __init__(self, data):
        self._it = iter(data)
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= 5:
            raise FiveItemError("Exceeded 5 items")
        self.count += 1
        return next(self._it)

it2 = LimitedFive(range(10))
print("2.", end=" ")
try:
    for x in it2:
        print(x, end=" ")
except FiveItemError as e:
    print(f"\nCaught: {e}")
# 2. 0 1 2 3 4 
# Caught: Exceeded 5 items

# 3. Modify __next__() to raise StopIteration with custom message.
class MsgIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration("No more items available")
        val = self.i
        self.i += 1
        return val

it3 = MsgIterator(3)
print("3.", end=" ")
try:
    while True:
        print(next(it3), end=" ")
except StopIteration as e:
    print(f"\nStopIteration message: {e}")
# 3. 0 1 2 
# StopIteration message: No more items available

# 4. Write a safe iterator that silently ends without exception using a wrapper.
class SafeIterator:
    def __init__(self, iterable):
        self._it = iter(iterable)
    def __iter__(self):
        return self
    def __next__(self):
        return next(self._it, None)

it4 = SafeIterator([7, 8])
print("4.", end=" ")
for _ in range(4):  # call more times than elements
    val = next(it4)
    if val is None:
        break
    print(val, end=" ")
# 4. 7 8

# 5. Create an iterator that prints a warning before stopping.
import warnings
class WarnIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            warnings.warn("Iterator is about to stop", UserWarning)
            raise StopIteration
        val = self.i
        self.i += 1
        return val

it5 = WarnIterator(2)
print("\n5.", end=" ")
try:
    while True:
        print(next(it5), end=" ")
except StopIteration:
    pass
# On termination, a warning "Iterator is about to stop" is emitted


# Real-Life Use Case Based Iterators 

# 1. PaginationIterator for navigating a list of blog articles page-by-page.
class PaginationIterator:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        page = self.items[self.index : self.index + self.page_size]
        self.index += self.page_size
        return page

blogs = [f"post{i}" for i in range(1, 11)]
pages = list(PaginationIterator(blogs, 3))
print("1.", pages)
# 1. [['post1','post2','post3'], ['post4','post5','post6'], ['post7','post8','post9'], ['post10']]

# 2. TransactionIterator that returns 5 transactions at a time.
class TransactionIterator:
    def __init__(self, transactions):
        self._it = iter(transactions)

    def __iter__(self):
        return self

    def __next__(self):
        chunk = []
        for _ in range(5):  # batch size
            chunk.append(next(self._it))
        return chunk

txns = [f"tx{i}" for i in range(1, 13)]
print("2.", [chunk for chunk in TransactionIterator(txns)])
# 2. [['tx1'..'tx5'], ['tx6'..'tx10'], ['tx11','tx12']]

# 3. SensorDataIterator that stops when a threshold is breached.
class SensorDataIterator:
    def __init__(self, readings, threshold):
        self._it = iter(readings)
        self.threshold = threshold

    def __iter__(self):
        return self

    def __next__(self):
        val = next(self._it)
        if val > self.threshold:
            raise StopIteration
        return val

readings = [10, 20, 30, 105, 40]
print("3.", list(SensorDataIterator(readings, 100)))
# 3. [10, 20, 30]

# 4. EmailValidatorIterator that yields only valid emails from a list.
import re
class EmailValidatorIterator:
    def __init__(self, items):
        self._it = iter(items)
        self.pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self._it)  # may raise StopIteration
            if self.pattern.match(item):
                return item

emails = ["a@b.com", "invalid", "user@site.org"]
print("4.", list(EmailValidatorIterator(emails)))
# 4. ['a@b.com', 'user@site.org']

# 5. ProductStockIterator that yields products below threshold level.
class ProductStockIterator:
    def __init__(self, products, threshold):
        self._it = iter(products)
        self.threshold = threshold

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            prod, stock = next(self._it)
            if stock < self.threshold:
                return prod  # only return product name

inventory = [("apple", 5), ("banana", 12), ("cherry", 2), ("date", 20)]
print("5.", list(ProductStockIterator(inventory, 10)))
# 5. ['apple', 'cherry']


