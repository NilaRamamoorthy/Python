from storage import add_entry, edit_entry, delete_entry, summarize_entries, entries
from search import search_by_tag, search_by_date

# Adding diary entries
add_entry("2025-07-15", "Started learning Python modules.", ["python", "learning"])
add_entry("2025-07-16", "Built a diary app.", ["project", "diary"])

# Edit an entry
edit_entry(1, new_text="Built and improved diary app", new_tags=["project", "diary", "update"])

# Delete an entry
delete_entry(0)

# Summary of all entries
summarize_entries()

# Search features
search_by_tag(entries, "diary")
search_by_date(entries, "2025-07-16")
