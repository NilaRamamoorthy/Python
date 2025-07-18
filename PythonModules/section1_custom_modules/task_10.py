# Task 10 - Two modules calling each other

# helper.py
def get_message():
    return "Message from helper"

# main.py
from task_10_helper import get_message

print(get_message())
