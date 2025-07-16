# Initial movie data
movies = {
    "Inception": {"ratings": [5, 4, 5], "genre": "Sci-Fi", "avg_rating": 4.67},
    "Titanic": {"ratings": [5, 3, 4], "genre": "Romance", "avg_rating": 4.0},
    "Avatar": {"ratings": [4, 4, 5], "genre": "Sci-Fi", "avg_rating": 4.33}
}

# 1. Add new rating
movies["Titanic"]["ratings"].append(5)

# 2. Recalculate average ratings
for movie in movies:
    ratings = movies[movie]["ratings"]
    avg = sum(ratings) / len(ratings)
    movies[movie]["avg_rating"] = round(avg, 2)

# 3. Sort by average rating
sorted_movies = sorted(movies.items(), key=lambda x: x[1]["avg_rating"], reverse=True)

print("Movies Sorted by Average Rating:")
for title, data in sorted_movies:
    print(f"{title}: {data['avg_rating']}")

# 4. Filter movies by genre
genre_filter = "Sci-Fi"
sci_fi_movies = {title: data for title, data in movies.items() if data["genre"] == genre_filter}

print(f"\nMovies in genre '{genre_filter}':")
for title in sci_fi_movies:
    print(title)
