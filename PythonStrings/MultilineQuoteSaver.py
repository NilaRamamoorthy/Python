# 7. Multi-line Quote Saver

quote = """
    The greatest glory in living
    lies not in never falling,
    but in rising every time we fall.
    – Nelson Mandela
"""

quote=quote.strip()
count=quote.count("\n")
print(f"Number of lines in the quote: {count+1}")
