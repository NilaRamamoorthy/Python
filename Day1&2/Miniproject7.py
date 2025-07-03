movie1 = input("Enter your first favorite movie: ")
movie2 = input("Enter your second favorite movie: ")
movie3 = input("Enter your third favorite movie: ")

favorite_movies = (movie1, movie2, movie3)

print("\nYour favorite movies (as a tuple):", favorite_movies)

print("\nIndividual movies:")
print("Movie 1:", favorite_movies[0])
print("Movie 2:", favorite_movies[1])
print("Movie 3:", favorite_movies[2])

print("\nType of favorite_movies:", type(favorite_movies))
