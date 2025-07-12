# Movie Rating Collector

movies = []  # List to store movie info as [name, rating]

# Function to collect movie ratings
def collect_rating():
    while True:
        name = input("\nEnter movie name (or type 'exit' to stop): ").strip().title()
        if name.lower() == 'exit':
            break
        try:
            rating = float(input(f"Enter your rating for '{name}' (0–10): "))
            if 0 <= rating <= 10:
                movies.append([name, rating])
                print(f"Added '{name}' with rating {rating}")
            else:
                print("Rating must be between 0 and 10.")
        except ValueError:
            print("Invalid rating. Enter a number.")

# Function to show top-rated movies
def show_top_movies():
    if not movies:
        print("No movies rated yet.")
        return
    print("\nMovie Ratings:")
    for m in movies:
        print(f"{m[0]} → {m[1]}")

    # Sort movies by rating (descending)
    top = sorted(movies, key=lambda x: x[1], reverse=True)[:3]
    print("\n🏆 Top Rated Movies:")
    for m in top:
        print(f"{m[0]} → {m[1]}")

# Run the app
def movie_rating_app():
    print("Movie Rating Collector")
    collect_rating()
    show_top_movies()

# Start app
movie_rating_app()
