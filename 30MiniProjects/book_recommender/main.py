# main.py

from recommender import search_books_by_author, search_books_by_genre, recommend_by_genre_or_author, get_random_recommendation

print("Books by 'George Orwell':")
print(search_books_by_author("George Orwell"))

print("\nBooks in 'fiction' genre:")
print(search_books_by_genre("fiction"))

print("\nRecommendations based on '1984':")
recs = recommend_by_genre_or_author("1984")
print(recs)

print("\nRandom pick from recommendations:")
print(get_random_recommendation(recs))
