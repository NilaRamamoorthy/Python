# Basic Decorator Tasks

import time
import functools
from datetime import datetime

# 1. Write a basic decorator that prints “Function started” before execution.
def start_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        return func(*args, **kwargs)
    return wrapper

@start_decorator
def greet():
    print("Hello!")

# 2. Create a decorator that prints the name of the function being called.
def name_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@name_decorator
def say_hello():
    print("Hi there!")

# 3. Create a decorator to count how many times a function is called.
def call_counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} has been called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@call_counter
def repeat():
    print("Repeating...")

# 4. Make a decorator that returns the square of the function's return value.
def square_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2
    return wrapper

@square_output
def give_number():
    return 5

# 5. Build a decorator that converts the return value of a function to uppercase.
def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_message():
    return "good morning"

# 6. Write a decorator that logs the function’s arguments and return value.
def log_args_return(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@log_args_return
def multiply(a, b):
    return a * b

# 7. Write a decorator to add logging before and after any function.
def log_before_after(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_before_after
def process():
    print("Processing task...")

# 8. Create a decorator that adds exception handling to a function.
def safe_run(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper

@safe_run
def divide(x, y):
    return x / y

# 9. Build a decorator to print the execution time of a function.
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished slow task")

# 10. Make a decorator that logs the current datetime before a function runs.
def datetime_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function called at: {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

@datetime_logger
def launch():
    print("Launching process...")

# Sample executions
if __name__ == "__main__":
    print("\nTask 1:")
    greet()

    print("\nTask 2:")
    say_hello()

    print("\nTask 3:")
    repeat()
    repeat()

    print("\nTask 4:")
    print(give_number())

    print("\nTask 5:")
    print(say_message())

    print("\nTask 6:")
    multiply(4, 5)

    print("\nTask 7:")
    process()

    print("\nTask 8:")
    print(divide(10, 2))
    print(divide(5, 0))  # will catch exception

    print("\nTask 9:")
    slow_function()

    print("\nTask 10:")
    launch()


# decorators_with_args_kwargs.py

import functools

# 1. Create a decorator that accepts any number of arguments and logs them.
def log_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_arguments
def greet(name, age=None):
    print(f"Hello {name}!")

# 2. Build a decorator that sums all arguments passed to a function.
def sum_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        total = sum(arg for arg in args if isinstance(arg, (int, float)))
        print(f"Sum of positional arguments: {total}")
        return func(*args, **kwargs)
    return wrapper

@sum_args
def process_numbers(*args):
    print("Processing numbers...")

# 3. Make a decorator that validates the argument types using isinstance().
def validate_types(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Expected {expected}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(str, int)
def register(name, age):
    print(f"Registered {name}, age {age}")

# 4. Write a decorator that ensures a string argument is not empty.
def non_empty_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str) and arg.strip() == "":
                raise ValueError("String argument cannot be empty")
        return func(*args, **kwargs)
    return wrapper

@non_empty_string
def say_something(message):
    print(f"You said: {message}")

# 5. Write a decorator that enforces at least one keyword argument.
def require_keyword(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs:
            raise ValueError("At least one keyword argument required")
        return func(*args, **kwargs)
    return wrapper

@require_keyword
def show_info(*args, **kwargs):
    print(f"Info: {kwargs}")

# 6. Create a decorator that only allows int arguments.
def only_ints(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if not isinstance(arg, int):
                raise TypeError("Only integer arguments allowed")
        return func(*args, **kwargs)
    return wrapper

@only_ints
def add(a, b):
    return a + b

# 7. Build a decorator that reverses a list argument before passing it to the function.
def reverse_list_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if isinstance(arg, list):
                new_args.append(arg[::-1])
            else:
                new_args.append(arg)
        return func(*new_args, **kwargs)
    return wrapper

@reverse_list_input
def print_list(data):
    print("Modified list:", data)

# 8. Write a decorator that converts all string arguments to lowercase.
def lowercase_strings(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [arg.lower() if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {k: v.lower() if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper

@lowercase_strings
def show_message(text):
    print(f"Message: {text}")

# 9. Create a decorator that rounds float return values to 2 decimal places.
def round_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, float):
            return round(result, 2)
        return result
    return wrapper

@round_result
def divide(a, b):
    return a / b

# 10. Build a decorator that blocks function execution if a keyword block=True is passed.
def block_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get("block", False):
            print("Execution blocked.")
            return None
        return func(*args, **kwargs)
    return wrapper

@block_execution
def sensitive_task(data, **kwargs):
    print(f"Performing task with data: {data}")

# Sample calls
if __name__ == "__main__":
    print("\nTask 1:")
    greet("Alice", age=25)

    print("\nTask 2:")
    process_numbers(1, 2, 3, "x", 4.5)

    print("\nTask 3:")
    register("Bob", 30)

    print("\nTask 4:")
    say_something("Hello!")

    print("\nTask 5:")
    show_info(x=10, y=20)

    print("\nTask 6:")
    print(add(10, 5))

    print("\nTask 7:")
    print_list([1, 2, 3, 4])

    print("\nTask 8:")
    show_message("HELLO WoRLD")

    print("\nTask 9:")
    print(divide(10, 3))

    print("\nTask 10:")
    sensitive_task("secret", block=True)
    sensitive_task("secret", block=False)


# decorators_with_parameters.py

import functools
import time

# 1. Create a decorator that repeats function output n times.
def repeat_output(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_output(3)
def greet():
    print("Hello!")

# 2. Build a decorator that logs to a custom file path passed as an argument.
def log_to_file(path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(path, "a") as f:
                f.write(f"Function {func.__name__} called with {args}, {kwargs}\n")
            return result
        return wrapper
    return decorator

@log_to_file("custom_log.txt")
def log_message(msg):
    print(msg)

# 3. Create a decorator that limits how many times a function can be called.
def limit_calls(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if wrapper.calls >= n:
                print("Function call limit reached!")
                return
            wrapper.calls += 1
            return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper
    return decorator

@limit_calls(2)
def say_hi():
    print("Hi!")

# 4. Build a decorator that checks if a user has a specific role (e.g., admin, editor).
def require_role(role_required):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user_role, *args, **kwargs):
            if user_role != role_required:
                print(f"Access denied. Required role: {role_required}")
                return
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(role, user_id):
    print(f"{role} deleted user {user_id}")

# 5. Write a decorator that enforces a minimum argument length.
def min_length(length):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg, *args, **kwargs):
            if len(arg) < length:
                raise ValueError(f"Argument must be at least {length} characters")
            return func(arg, *args, **kwargs)
        return wrapper
    return decorator

@min_length(5)
def set_password(pw):
    print("Password set!")

# 6. Create a decorator that prints a custom prefix before every log.
def log_with_prefix(prefix):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_with_prefix(">>>")
def calculate():
    print("Calculating...")

# 7. Create a decorator that delays execution of the function by n seconds.
def delay(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting {seconds} seconds before execution...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(2)
def delayed_hello():
    print("Hello after delay!")

# 8. Create a decorator that adds a custom header and footer to printed output.
def header_footer(header, footer):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(header)
            result = func(*args, **kwargs)
            print(footer)
            return result
        return wrapper
    return decorator

@header_footer("*** START ***", "*** END ***")
def welcome():
    print("Welcome to the platform!")

# 9. Build a decorator that tracks time taken and prints a warning if it exceeds n seconds.
def time_limit(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            print(f"Execution time: {duration:.2f} seconds")
            if duration > seconds:
                print(f"WARNING: Exceeded time limit of {seconds} seconds!")
            return result
        return wrapper
    return decorator

@time_limit(1)
def fast_task():
    time.sleep(1.5)
    print("Task completed.")

# 10. Write a decorator that applies a given function to the result of the decorated function.
def apply_result(modifier_func):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return modifier_func(result)
        return wrapper
    return decorator

def square(x):
    return x * x

@apply_result(square)
def get_number():
    return 4

# Sample executions
if __name__ == "__main__":
    print("\nTask 1:")
    greet()

    print("\nTask 2:")
    log_message("Logging this message to a file.")

    print("\nTask 3:")
    say_hi()
    say_hi()
    say_hi()  # Should not work

    print("\nTask 4:")
    delete_user("editor", 101)  # Access denied
    delete_user("admin", 102)   # Allowed

    print("\nTask 5:")
    set_password("secure")

    print("\nTask 6:")
    calculate()

    print("\nTask 7:")
    delayed_hello()

    print("\nTask 8:")
    welcome()

    print("\nTask 9:")
    fast_task()

    print("\nTask 10:")
    print("Modified result:", get_number())  # Output should be 16


# multiple_decorators_chaining.py

import functools
import time
import math

# 1. Write two decorators: one to double the result and another to square it. Chain them.
def double_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return wrapper

def square_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

@square_result
@double_result
def base_number():
    return 3  # ((3 * 2) ** 2 = 36)

# 2. Create decorators @authenticate and @authorize, apply both to a function.
def authenticate(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated", False):
            print("User not authenticated.")
            return
        return func(user, *args, **kwargs)
    return wrapper

def authorize(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            print("User not authorized.")
            return
        return func(user, *args, **kwargs)
    return wrapper

@authenticate
@authorize
def delete_account(user):
    print("Account deleted.")

# 3. Create @log_input, @log_output, and use both on a function.
def log_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Input: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

def log_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper

@log_output
@log_input
def add(a, b):
    return a + b

# 4. Chain a decorator that reverses a string with one that uppercases it.
def reverse_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)[::-1]
    return wrapper

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@reverse_string
@uppercase
def greet():
    return "hello"

# 5. Write two decorators: one that formats output in HTML <p> tags and another in <div>.
def html_p(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}</p>"
    return wrapper

def html_div(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<div>{func(*args, **kwargs)}</div>"
    return wrapper

@html_div
@html_p
def message():
    return "This is a message."

# 6. Create a decorator chain for a CLI app: logging, timing, formatting.
def cli_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def cli_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIMER] {func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

def cli_format(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f">>> {result} <<<"
    return wrapper

@cli_log
@cli_timer
@cli_format
def run_cli():
    time.sleep(1)
    return "Command Executed"

# 7. Build a mathematical chain: log the result, then check if it’s even.
def math_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[MATH LOG] Result: {result}")
        return result
    return wrapper

def check_even(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 == 0:
            print("Even result.")
        else:
            print("Odd result.")
        return result
    return wrapper

@check_even
@math_log
def compute():
    return 7 + 1

# 8. Make one decorator validate input, another one transform the result — combine them.
def validate_positive(func):
    @functools.wraps(func)
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be positive.")
        return func(x)
    return wrapper

def double_output(func):
    @functools.wraps(func)
    def wrapper(x):
        return func(x) * 2
    return wrapper

@double_output
@validate_positive
def half(x):
    return x / 2

# 9. Create a pipeline using multiple decorators that simulates processing stages.
def stage_one(func):
    @functools.wraps(func)
    def wrapper(data):
        print("Stage 1: Cleaning")
        return func(data.strip())
    return wrapper

def stage_two(func):
    @functools.wraps(func)
    def wrapper(data):
        print("Stage 2: Transforming")
        return func(data.upper())
    return wrapper

def stage_three(func):
    @functools.wraps(func)
    def wrapper(data):
        print("Stage 3: Finalizing")
        return f"[{func(data)}]"
    return wrapper

@stage_three
@stage_two
@stage_one
def process_text(data):
    return data

# 10. Use functools.wraps to preserve function metadata when chaining.
def print_metadata(func):
    print(f"Function: {func.__name__}")
    print(f"Doc: {func.__doc__}")
    return func

@print_metadata
@functools.wraps
def sample():
    """Sample function documentation"""
    pass

# Sample executions
if __name__ == "__main__":
    print("\nTask 1:")
    print("Result:", base_number())

    print("\nTask 2:")
    user1 = {"authenticated": True, "role": "admin"}
    user2 = {"authenticated": False, "role": "editor"}
    delete_account(user2)
    delete_account(user1)

    print("\nTask 3:")
    add(5, 7)

    print("\nTask 4:")
    print("Chained Output:", greet())

    print("\nTask 5:")
    print("HTML:", message())

    print("\nTask 6:")
    print(run_cli())

    print("\nTask 7:")
    compute()

    print("\nTask 8:")
    print("Validated and Transformed:", half(4))

    print("\nTask 9:")
    print("Final Output:", process_text("   clean me now  "))

    print("\nTask 10:")
    print("Metadata preserved.")

# class_based_decorators.py

import functools

# 1. Implement a class-based decorator that logs before and after execution.
class LoggerDecorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"[LOG] Starting '{self.func.__name__}'")
        result = self.func(*args, **kwargs)
        print(f"[LOG] Finished '{self.func.__name__}'")
        return result

@LoggerDecorator
def say_hello():
    print("Hello!")

# 2. Create a decorator that caches results (like memoization) using a class.
class Memoize:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print("Using cached result.")
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result

@Memoize
def slow_add(a, b):
    print("Computing...")
    return a + b

# 3. Create a decorator class that tracks how many instances are created.
class InstanceCounter:
    count = 0

    def __init__(self, cls):
        self.cls = cls
        functools.update_wrapper(self, cls)

    def __call__(self, *args, **kwargs):
        InstanceCounter.count += 1
        print(f"Creating instance #{InstanceCounter.count} of {self.cls.__name__}")
        return self.cls(*args, **kwargs)

@InstanceCounter
class MyObject:
    def __init__(self, name):
        self.name = name

# 4. Decorate a class method with @classmethod, then wrap with your own logger.
def log_classmethod(func):
    @functools.wraps(func)
    def wrapper(cls, *args, **kwargs):
        print(f"[LOG] Class method '{func.__name__}' called on {cls.__name__}")
        return func(cls, *args, **kwargs)
    return wrapper

class Account:
    @classmethod
    @log_classmethod
    def bank_info(cls):
        return "Bank of Python"

# 5. Combine @property with a custom decorator to log when a property is accessed.
def log_property_access(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Accessing property: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Person:
    def __init__(self, name):
        self._name = name

    @property
    @log_property_access
    def name(self):
        return self._name

# Sample executions
if __name__ == "__main__":
    print("\nTask 1:")
    say_hello()

    print("\nTask 2:")
    print("Result:", slow_add(2, 3))
    print("Cached Result:", slow_add(2, 3))  # uses cache

    print("\nTask 3:")
    obj1 = MyObject("One")
    obj2 = MyObject("Two")

    print("\nTask 4:")
    print(Account.bank_info())

    print("\nTask 5:")
    p = Person("Alice")
    print(p.name)


# advanced_practical_decorators.py

import time
import functools
import random
from datetime import datetime
from collections import deque

# Global log storage for call times
call_logs = []

# 1. API Rate Limiting Decorator (allow only 5 calls per minute)
def rate_limiter(max_calls=5, period=60):
    call_times = deque()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            while call_times and current_time - call_times[0] > period:
                call_times.popleft()
            if len(call_times) < max_calls:
                call_times.append(current_time)
                return func(*args, **kwargs)
            else:
                print("[RATE LIMIT] Too many calls. Try again later.")
        return wrapper
    return decorator

@rate_limiter()
def fetch_data():
    print("Fetching data...")

# 2. Retry Decorator (retry up to 3 times on failure)
def retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"[RETRY] Attempt {attempts} failed: {e}")
                    time.sleep(1)
            print("[RETRY] All attempts failed.")
        return wrapper
    return decorator

@retry()
def unreliable():
    if random.choice([True, False]):
        raise ValueError("Random failure!")
    return "Success!"

# 3. Call Time Logger Decorator
def log_call_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        call_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        call_logs.append((func.__name__, call_time))
        print(f"[LOG] Called {func.__name__} at {call_time}")
        return func(*args, **kwargs)
    return wrapper

@log_call_time
def say_hi():
    print("Hi there!")

# 4. API Token Security Decorator
VALID_TOKEN = "secure123"

def require_token(token_key):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            token = kwargs.pop('token', None)
            if token == token_key:
                return func(*args, **kwargs)
            else:
                raise PermissionError("[SECURITY] Invalid API token.")
        return wrapper
    return decorator

@require_token("secure123")
def secure_action():
    print("Secure action executed!")

# 5. Encrypt/Decrypt Decorator with Custom Key
def encrypt_decrypt(key):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Simple Caesar cipher encryption
            def shift(text, k):
                return ''.join(chr((ord(char) + k) % 256) for char in text)

            result = func(*args, **kwargs)
            encrypted = shift(result, key)
            print(f"[ENCRYPTED] {encrypted}")
            decrypted = shift(encrypted, -key)
            print(f"[DECRYPTED] {decrypted}")
            return decrypted
        return wrapper
    return decorator

@encrypt_decrypt(4)
def secret_message():
    return "Confidential Data"

# Sample executions
if __name__ == "__main__":
    print("\nTask 1: Rate Limiting")
    for _ in range(7):
        fetch_data()
        time.sleep(10)  # spread out calls

    print("\nTask 2: Retry Decorator")
    print("Result:", unreliable())

    print("\nTask 3: Log Call Time")
    say_hi()
    say_hi()
    print("Call Log:", call_logs)

    print("\nTask 4: Token Checker")
    try:
        secure_action(token="secure123")  # Valid
        secure_action(token="wrongtoken")  # Invalid
    except Exception as e:
        print(e)

    print("\nTask 5: Encrypt/Decrypt")
    secret_message()

