# Movie Watchlist App

# Initial watchlist
watchlist = ["Inception", "Interstellar", "Dune", "The Matrix", "The Dark Knight"]

# Display all movies with index
print("Your Watchlist:")
for i, movie in enumerate(watchlist, start=1):
    print(f"{i}. {movie}")

# Add a new movie
watchlist.append("Oppenheimer")
print("\nAfter adding 'Oppenheimer':", watchlist)

# Mark a movie as watched (remove it)
watched = "Dune"
if watched in watchlist:
    watchlist.remove(watched)
    print(f"\nMarked '{watched}' as watched.")
else:
    print(f"\n'{watched}' is not in the list.")

# Show top 5 movies to watch using slicing
print("\nTop 5 Movies To Watch:")
for movie in watchlist[:5]:
    print("-", movie)

# Display final list
print("\nUpdated Watchlist:")
for i, movie in enumerate(watchlist, start=1):
    print(f"{i}. {movie}")
