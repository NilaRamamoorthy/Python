# 11. Feedback Cleaner Tool
feedback="   I love it!!!   "
feedback=feedback.strip()
feedback=feedback.replace("!","")
count=feedback.count(" ")+1
print(f"Feedback Ater cleaning: {feedback}")
print(f"Number of words {count}")