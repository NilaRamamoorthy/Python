def diary_entry_tool(entry, save_to_file=False):
    def process_entry(text):
        print("\n--- Diary Entry ---")
        print(text)
        if save_to_file:
            with open("diary.txt", "a") as file:
                file.write(text + "\n\n")
            print("Entry saved to diary.txt")

    process_entry(entry)

    entry_length = len(entry)
    word_count = len(entry.split())

    return entry_length, word_count

# Example Usage
entry_text = input("Write your diary entry: ").strip()
length, words = diary_entry_tool(entry_text, save_to_file=True)

print(f"\nEntry Length: {length} characters")
print(f"Word Count: {words} words")
