# generator.py

import random
import string

def generate_password(length: int = 12) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
