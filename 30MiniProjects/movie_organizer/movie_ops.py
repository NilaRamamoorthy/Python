# movie_ops.py

from typing import List, Dict, Set, Tuple

# List to store movie records
movies: List[Dict] = []

def add_movie(title: str, year: int, genres: Set[str], actors: List[str]):
    movie = {
        "title": title,
        "year": year,
        "genres": {g.lower() for g in genres},
        "actors": [a.lower() for a in actors]
    }
    movies.append(movie)
    print(f"Added movie: {title} ({year})")

def get_movies() -> List[Dict]:
    return movies

def group_by_genre() -> Dict[str, List[Tuple[str, int]]]:
    grouped = {}
    for movie in movies:
        for genre in movie["genres"]:
            grouped.setdefault(genre, []).append((movie["title"], movie["year"]))
    return grouped

def unique_genres() -> Set[str]:
    return {g for m in movies for g in m["genres"]}

def unique_actors() -> Set[str]:
    return {a for m in movies for a in m["actors"]}
