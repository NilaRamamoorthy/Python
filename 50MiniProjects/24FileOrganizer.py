import os
import shutil
from functools import wraps

# Decorator to preview changes without actually moving files
def dry_run(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("[Dry Run Mode] No files will be moved.")
        return func(*args, **kwargs)
    return wrapper

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        # Mapping file extensions to folder names
        self.extension_map = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'documents': ['.pdf', '.doc', '.docx', '.txt'],
            'videos': ['.mp4', '.avi', '.mov'],
            'audio': ['.mp3', '.wav'],
            'archives': ['.zip', '.rar', '.tar', '.gz'],
            'spreadsheets': ['.xlsx', '.csv']
        }

    @dry_run
    def organize(self):
        """Organize files in the directory based on their extensions."""
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                category = self.get_category(file_ext)
                if category:
                    self.move_file(file_path, filename, category)
                else:
                    print(f"Unknown file type: {filename}")

    def get_category(self, file_ext):
        """Return the category for a given file extension."""
        for category, extensions in self.extension_map.items():
            if file_ext in extensions:
                return category
        return None

    def move_file(self, file_path, filename, category):
        """Move the file to the appropriate category folder."""
        category_folder = os.path.join(self.directory, category)
        os.makedirs(category_folder, exist_ok=True)
        destination = os.path.join(category_folder, filename)
        shutil.move(file_path, destination)
        print(f"Moved: {filename} -> {category}/")

    def file_mover(self):
        """Generator to yield files being moved."""
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                category = self.get_category(file_ext)
                if category:
                    yield filename, category

# Example usage
if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    organizer = FileOrganizer(directory)
    organizer.organize()

    print("\nFiles to be moved (dry run):")
    for filename, category in organizer.file_mover():
        print(f"{filename} -> {category}")
