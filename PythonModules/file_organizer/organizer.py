import os
import shutil
from file_organizer.categorizer import get_file_type
from file_organizer.utils import create_folder_if_not_exists

def organize_directory(path):
    if not os.path.exists(path):
        print("Invalid directory path.")
        return

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)

        if os.path.isfile(full_path):
            category = get_file_type(filename)
            category_path = os.path.join(path, category)
            create_folder_if_not_exists(category_path)
            shutil.move(full_path, os.path.join(category_path, filename))
            print(f"Moved {filename} → {category}/")
