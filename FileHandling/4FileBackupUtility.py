import os

def backup_file(source_path):
    if not os.path.exists(source_path):
        print("Source file not found.")
        return

    base, ext = os.path.splitext(source_path)
    backup_path = f"{base}_backup{ext}"

    if os.path.exists(backup_path):
        print("Backup already exists.")
        return

    try:
        with open(source_path, 'r') as src, open(backup_path, 'w') as dest:
            content = src.read()
            dest.write(content)
        print(f"Backup created: {backup_path}")
    except Exception as e:
        print(f"Error during backup: {e}")

# Demo usage
backup_file("sample.txt")
