# Mock translation dictionary
eng2tam = {
    "hello": "வணக்கம்",     # vanakkam
    "thank": "நன்றி",      # nandri
    "love": "அன்பு",        # anbu
    "book": "புத்தகம்",     # puthagam
    "science": "அறிவியல்"   # ariviyal
}

def translator(words):
    """
    Lazily translates English words to Tamil.

    Yields: (word, translation)
    Filters out unknown words.
    """
    return ((w, eng2tam[w]) for w in words if w in eng2tam)

# Input list of words
input_words = ["hello", "world", "thank", "foo", "science", "book"]

# Lazy translation generator
lazy_trans = translator(input_words)

# Demonstrate manual iteration
print("Lazy translation output:")
for eng, tam in lazy_trans:
    print(f"{eng} → {tam}")
