import re
import time
from functools import wraps

# Decorator to measure execution time
def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper

# Password Strength Checker Class
class PasswordStrengthChecker:
    def __init__(self):
        self.strength_thresholds = {
            "Weak": 1,
            "Medium": 2,
            "Strong": 3
        }

    def evaluate_strength(self, password: str) -> str:
        """Evaluates the strength of the password."""
        if not password:
            raise ValueError("Password cannot be empty.")

        score = 0
        feedback = []

        # Check length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters long.")

        # Check for uppercase letters
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Add at least one uppercase letter.")

        # Check for lowercase letters
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Add at least one lowercase letter.")

        # Check for digits
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Add at least one number.")

        # Check for special characters
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("Include at least one special character.")

        # Determine strength
        for strength, threshold in self.strength_thresholds.items():
            if score >= threshold:
                return f"{strength} Password: {' '.join(feedback)}"

        return f"Weak Password: {' '.join(feedback)}"

    def missing_criteria_generator(self, password: str):
        """Yields missing criteria one by one."""
        criteria = [
            ("uppercase letter", r'[A-Z]'),
            ("lowercase letter", r'[a-z]'),
            ("number", r'\d'),
            ("special character", r'[!@#$%^&*(),.?":{}|<>]')
        ]
        for description, pattern in criteria:
            if not re.search(pattern, password):
                yield f"Add at least one {description}."

    def prompt_for_strong_password(self):
        """Prompts the user until a strong password is provided."""
        while True:
            password = input("Enter your password: ")
            strength = self.evaluate_strength(password)
            print(strength)
            if "Strong" in strength:
                break
            else:
                print("Please improve your password.")
                print("Missing criteria:")
                for missing in self.missing_criteria_generator(password):
                    print(f"- {missing}")

# Example usage
if __name__ == "__main__":
    checker = PasswordStrengthChecker()
    checker.prompt_for_strong_password()
