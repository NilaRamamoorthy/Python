import random
import datetime
from functools import wraps

# Decorator to validate user input
def validate_input(func):
    @wraps(func)
    def wrapper(self, guess):
        if not isinstance(guess, str) or len(guess) != 1 or not guess.isalpha():
            raise ValueError("Please guess a single alphabet letter")
        return func(self, guess.lower())
    return wrapper

# Custom exception
class InvalidGuessError(Exception):
    pass

class Hangman:
    def __init__(self, words_file, max_attempts=6):
        self.word = self._load_word(words_file)
        self.attempts_left = max_attempts
        self.guessed_letters = []
        self._wrong_guesses = 0
        self.search_history = []
        self._hint_yielded = False

    def _load_word(self, fname):
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                words = [w.strip().lower() for w in f if w.strip()]
            return random.choice(words)
        except FileNotFoundError:
            raise FileNotFoundError(f"Words file {fname} not found")

    def display_word(self):
        return ' '.join(c if c in self.guessed_letters else '_' for c in self.word)

    @validate_input
    def guess(self, guess):
        if guess in self.guessed_letters:
            raise InvalidGuessError(f"You already guessed '{guess}'")
        self.guessed_letters.append(guess)
        if guess not in self.word:
            self._wrong_guesses += 1
            self.attempts_left -= 1
        # record history
        self.search_history.append((guess, guess in self.word, self.attempts_left))
        return guess in self.word

    def is_won(self):
        return all(c in self.guessed_letters for c in self.word)

    def is_lost(self):
        return self.attempts_left <= 0

    def show_history(self):
        print("History: guess, correct?, attempts left")
        for g, ok, att in self.search_history:
            print(f"{g!r}, {'✓' if ok else '✗'}, {att}")

    # Generator yield a hint after 3 wrong guesses
    def hint_provider(self):
        if self._wrong_guesses >= 3 and not self._hint_yielded:
            self._hint_yielded = True
            # yield one hint: reveal one unrevealed letter
            for c in self.word:
                if c not in self.guessed_letters:
                    yield c
                    break

    def play(self):
        print("Let's play Hangman!")
        while not (self.is_won() or self.is_lost()):
            print(self.display_word(), f"(Attempts left: {self.attempts_left})")
            guess = input("Guess a letter: ")
            try:
                correct = self.guess(guess)
            except ValueError as ve:
                print(ve)
                continue
            except InvalidGuessError as ie:
                print(ie)
                continue
            if correct:
                print("Good guess!")
            else:
                print("Wrong guess.")
            # maybe show hint
            for h in self.hint_provider():
                print(f"Hint: one of the letters is '{h}'")
        if self.is_won():
            print("Congratulations! You won! The word was:", self.word)
        else:
            print("Game over. The word was:", self.word)
        self.show_history()

if __name__ == "__main__":
    game = Hangman("words.txt")
    game.play()
