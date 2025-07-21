# search_ops.py

from typing import List, Dict, Set, Tuple
from movie_ops import get_movies

def search_by_actor(actor_name: str) -> List[Tuple[str, int]]:
    actor_name = actor_name.lower()
    return [(m["title"], m["year"]) for m in get_movies() if actor_name in m["actors"]]

def search_by_genre(genre_name: str) -> List[Tuple[str, int]]:
    genre_name = genre_name.lower()
    return [(m["title"], m["year"]) for m in get_movies() if genre_name in m["genres"]]
