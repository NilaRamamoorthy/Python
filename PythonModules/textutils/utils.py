def capitalize_text(text):
    return text.capitalize()

def word_count(text):
    return len(text.split())

def find_keywords(text, keywords):
    return [word for word in text.split() if word in keywords]
