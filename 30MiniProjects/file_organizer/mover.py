import os
import shutil

def move_files_by_type(base_path, files_by_type):
    for ext, files in files_by_type.items():
        folder_name = ext[1:] if ext else "no_extension"
        folder_path = os.path.join(base_path, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for file in files:
            src = os.path.join(base_path, file)
            dest = os.path.join(folder_path, file)
            shutil.move(src, dest)
