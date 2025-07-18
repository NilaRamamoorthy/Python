import os

def get_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.jpg', '.png', '.gif']:
        return "Images"
    elif ext in ['.mp4', '.mkv', '.mov']:
        return "Videos"
    elif ext in ['.pdf', '.docx', '.txt']:
        return "Documents"
    elif ext in ['.zip', '.rar']:
        return "Archives"
    else:
        return "Others"
