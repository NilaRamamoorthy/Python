import random

# Custom exception
class GameOverError(Exception):
    pass

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("🎯 Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100.")

    while attempts < max_attempts:
        try:
            guess = input(f"Attempt {attempts + 1}: Enter your guess: ")
            if not guess.isdigit():
                raise ValueError("Only numbers are allowed.")
            guess = int(guess)
            attempts += 1

            if guess == number_to_guess:
                print("🎉 Correct! You guessed the number!")
                break
            elif guess < number_to_guess:
                print("📉 Too low.")
            else:
                print("📈 Too high.")

            if attempts == max_attempts:
                raise GameOverError("Game Over! You've used all your attempts.")
        
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except GameOverError as ge:
            print(ge)
            break
        finally:
            print(f"Attempts used: {attempts}/{max_attempts}")

number_guessing_game()
