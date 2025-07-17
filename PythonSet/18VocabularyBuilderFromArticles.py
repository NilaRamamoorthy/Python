# Simulated article contents (normally read from files)
article1 = "Python is a powerful programming language for data science and web development."
article2 = "Machine learning and data analysis are key areas in artificial intelligence."

# Split and normalize words (lowercase, strip punctuation)
words_article1 = {word.strip(".,").lower() for word in article1.split()}
words_article2 = {word.strip(".,").lower() for word in article2.split()}

# Combine vocabulary from both articles
article_vocab = words_article1.union(words_article2)
print("Vocabulary from Articles:", article_vocab)

# Known vocabulary of the user
known_words = {"python", "data", "science", "web", "development", "machine"}

# Find new/unfamiliar words
new_words = article_vocab.difference(known_words)
print("New Words to Learn:", new_words)
