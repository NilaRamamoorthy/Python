# Mini File Organizer (Mock Version)

# Function to organize files by extension
def organize_files():
    print(" Mini File Organizer")

    files_input = input("Enter file names separated by comma (e.g., photo.jpg, notes.txt):\n").strip()
    files = [file.strip() for file in files_input.split(",")]

    organized = {}  # Dictionary to hold files by extension

    for file in files:
        if '.' in file:
            ext = file.split('.')[-1]
            if ext not in organized:
                organized[ext] = [file]
            else:
                organized[ext].append(file)
        else:
            if 'no_extension' not in organized:
                organized['no_extension'] = [file]
            else:
                organized['no_extension'].append(file)

    print("\n Organized Files by Extension:")
    for ext, file_list in organized.items():
        print(f".{ext} → {file_list}")

# Run the mock organizer
organize_files()
