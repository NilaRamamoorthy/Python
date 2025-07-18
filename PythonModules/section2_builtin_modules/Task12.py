import random

def guessing_game():
    target = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == target:
        print("Correct!")
    else:
        print(f"Wrong! The number was {target}")

if __name__ == "__main__":
    guessing_game()
