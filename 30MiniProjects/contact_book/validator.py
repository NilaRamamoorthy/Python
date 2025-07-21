import re

def validate_phone(phone):
    return re.fullmatch(r"\d{10}", phone) is not None

def validate_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None
