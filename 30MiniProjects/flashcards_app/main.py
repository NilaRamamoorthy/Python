from card_ops import *
from stats import show_stats

stats = {'correct': 0, 'incorrect': 0}

# Add sample flashcards
add_flashcard("Hello", "Hola", "Greetings")
add_flashcard("Thank you", "Gracias", "Gratitude")
add_flashcard("Dog", "Perro", "Animals")

print("Review Flashcards:")
review_flashcards()

print("\nStarting Quiz:")
quiz(stats)

show_stats(stats)

print("\nAvailable Categories:", categories)
