# Headlines from two different news APIs
api1_headlines = {
    "AI beats humans in chess again",
    "Climate change impacts polar bears",
    "Python is the fastest-growing language"
}

api2_headlines = {
    "Python is the fastest-growing language",
    "Mars rover sends new images",
    "Climate change impacts polar bears"
}

# Find duplicate headlines
duplicates = api1_headlines.intersection(api2_headlines)
print("Duplicate Headlines:", duplicates)

# Get all unique headlines using union
all_unique_headlines = api1_headlines.union(api2_headlines)
print("All Unique Headlines:", all_unique_headlines)

# Membership test
headline = "AI beats humans in chess again"
if headline in all_unique_headlines:
    print(f"'{headline}' is in the news feed.")
else:
    print(f"'{headline}' is not in the news feed.")
