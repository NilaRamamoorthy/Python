from textutils.count import count_words, count_characters
from textutils.sanitize import remove_punctuation

def summary_report(text):
    clean_text = remove_punctuation(text)
    words = count_words(clean_text)
    chars = count_characters(clean_text)
    return {
        "Words": words,
        "Characters (no punctuation)": chars
    }
