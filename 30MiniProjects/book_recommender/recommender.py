# recommender.py

from typing import Set, Tuple
import random
from book_data import books, genre_to_books

def search_books_by_author(author: str) -> Set[Tuple[str, str]]:
    return {(book["title"], book["author"]) for book in books if book["author"].lower() == author.lower()}

def search_books_by_genre(genre: str) -> Set[Tuple[str, str]]:
    return genre_to_books.get(genre.lower(), set())

def recommend_by_genre_or_author(input_title: str) -> Set[Tuple[str, str]]:
    for book in books:
        if book["title"].lower() == input_title.lower():
            similar_books = set()
            # Genre similarity
            for genre in book["genres"]:
                similar_books |= genre_to_books.get(genre, set())
            # Author similarity
            author_books = search_books_by_author(book["author"])
            similar_books |= author_books
            # Remove the original book
            similar_books.discard((book["title"], book["author"]))
            return similar_books
    return set()

def get_random_recommendation(recommendations: Set[Tuple[str, str]]) -> Tuple[str, str]:
    if recommendations:
        return random.choice(list(recommendations))
    return ("No recommendation", "")
