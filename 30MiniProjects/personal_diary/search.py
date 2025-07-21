def search_by_tag(entries, tag):
    print(f"\n--- Search Results for tag: {tag} ---")
    found = False
    for entry in entries:
        if tag in entry["tags"]:
            print(f"{entry['date']}: {entry['text']}")
            found = True
    if not found:
        print("No entries found with this tag.")

def search_by_date(entries, date):
    print(f"\n--- Search Results for date: {date} ---")
    found = False
    for entry in entries:
        if entry["date"] == date:
            print(f"{entry['date']}: {entry['text']}")
            found = True
    if not found:
        print("No entries found on this date.")
