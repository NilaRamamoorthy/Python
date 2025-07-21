entries = []

def add_entry(date, text, tags):
    entry = {
        "date": date,
        "text": text,
        "tags": set(tags)
    }
    entries.append(entry)
    print(f"Entry added on {date}.")

def edit_entry(index, new_text=None, new_tags=None):
    if 0 <= index < len(entries):
        if new_text:
            entries[index]["text"] = new_text
        if new_tags:
            entries[index]["tags"] = set(new_tags)
        print(f"Entry {index} updated.")
    else:
        print("Invalid index.")

def delete_entry(index):
    if 0 <= index < len(entries):
        removed = entries.pop(index)
        print(f"Deleted entry from {removed['date']}.")
    else:
        print("Invalid index.")

def summarize_entries():
    print("\n--- Diary Summary ---")
    for idx, entry in enumerate(entries):
        print(f"{idx}. {entry['date']} - Tags: {', '.join(entry['tags'])}")
