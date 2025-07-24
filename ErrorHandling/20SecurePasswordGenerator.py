import random
import string

# Custom exception
class WeakPasswordCriteriaError(Exception):
    pass

# Password generator
def generate_password(length, use_digits=True, use_symbols=True):
    try:
        assert length >= 8, "Password must be at least 8 characters long."

        chars = string.ascii_letters
        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation

        if len(chars) < 10:
            raise WeakPasswordCriteriaError("Password criteria too weak. Enable more options.")

        password = ''.join(random.choice(chars) for _ in range(length))
    except AssertionError as ae:
        print("❌", ae)
    except WeakPasswordCriteriaError as we:
        print("❌", we)
    except Exception as e:
        print("❌ Unexpected error:", e)
    else:
        print(f"✅ Your secure password is: {password}")
    finally:
        print("🔐 Password generation attempt completed.")

# Example usage
try:
    user_length = int(input("Enter password length (minimum 8): "))
    digits_input = input("Include digits? (y/n): ").lower()
    symbols_input = input("Include symbols? (y/n): ").lower()

    use_digits = digits_input == 'y'
    use_symbols = symbols_input == 'y'

    generate_password(user_length, use_digits, use_symbols)
except ValueError:
    print("❌ Length must be an integer.")
