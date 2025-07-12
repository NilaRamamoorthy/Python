# Password Strength Checker

import string

# Function to evaluate password strength
def check_strength(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if len(password) < 8:
        return " Password too short. Minimum 8 characters required."
    elif has_lower and has_upper and has_digit and has_symbol:
        return "Strong Password!"
    else:
        return "Weak Password. Use uppercase, lowercase, digits, and symbols."

# Main program loop
while True:
    pwd = input("Enter a password to check strength (or type 'exit' to quit): ")
    if pwd.lower() == 'exit':
        print("Exiting Password Checker.")
        break
    result = check_strength(pwd)
    print(result)
