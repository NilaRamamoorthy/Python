import os

def scan_directory(path):
    files_by_type = {}  # dict: extension → list of files
    file_types = set()

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            file_types.add(ext)
            if ext not in files_by_type:
                files_by_type[ext] = []
            files_by_type[ext].append(file)

    return files_by_type, file_types
