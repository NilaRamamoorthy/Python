# main.py

from movie_ops import add_movie, group_by_genre, unique_genres, unique_actors
from search_ops import search_by_actor, search_by_genre

# Add sample movies
add_movie("Inception", 2010, {"Sci-Fi", "Thriller"}, ["Leonardo DiCaprio", "Tom Hardy"])
add_movie("Titanic", 1997, {"Romance", "Drama"}, ["Leonardo DiCaprio", "Kate Winslet"])
add_movie("The Matrix", 1999, {"Sci-Fi", "Action"}, ["Keanu Reeves", "Laurence Fishburne"])

# Search operations
print("\nSearch by Actor 'Leonardo DiCaprio':")
print(search_by_actor("Leonardo DiCaprio"))

print("\nSearch by Genre 'Sci-Fi':")
print(search_by_genre("Sci-Fi"))

# Grouping
print("\nMovies Grouped by Genre:")
for genre, movie_list in group_by_genre().items():
    print(f"{genre.title()}: {movie_list}")

# Unique genres and actors
print("\nUnique Genres:")
print(unique_genres())

print("\nUnique Actors:")
print(unique_actors())
