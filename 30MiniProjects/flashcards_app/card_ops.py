import random

flashcards = []  # List of tuples: (word, translation)
categories = set()

def add_flashcard(word, translation, category):
    flashcards.append((word, translation))
    categories.add(category)

def delete_flashcard(word):
    global flashcards
    flashcards = [card for card in flashcards if card[0] != word]

def review_flashcards():
    for word, translation in flashcards:
        print(f"{word} → {translation}")

def quiz(stats):
    random.shuffle(flashcards)
    for word, translation in flashcards:
        answer = input(f"What is the translation of '{word}'? ")
        if answer.lower() == translation.lower():
            print("Correct!")
            stats['correct'] += 1
        else:
            print(f"Incorrect. Correct answer: {translation}")
            stats['incorrect'] += 1
