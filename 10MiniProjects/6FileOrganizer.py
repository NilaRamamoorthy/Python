import os
import shutil
import hashlib
import time

def organize_files_by_extension(folder):
    print(f"Organizing files in {folder} by extension...")
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            ext = filename.split('.')[-1].lower()
            dest_folder = os.path.join(folder, ext)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(dest_folder, filename))
    print("Organization complete.")

def file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while buf:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def remove_duplicates(folder):
    print("Removing duplicate files...")
    hashes = {}
    duplicates = []
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            h = file_hash(path)
            if h in hashes:
                duplicates.append(path)
            else:
                hashes[h] = path

    for dup in duplicates:
        os.remove(dup)
        print(f"Removed duplicate: {dup}")

    print(f"Removed {len(duplicates)} duplicate files.")

def bulk_rename(folder, pattern):
    print(f"Renaming files in {folder} with pattern '{pattern}'...")
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for i, file in enumerate(files, 1):
        ext = file.split('.')[-1]
        new_name = pattern.replace('{num}', str(i)) + '.' + ext
        os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
        print(f"Renamed {file} -> {new_name}")
    print("Renaming complete.")

def find_largest_files(folder, n=5):
    print(f"Finding {n} largest files in {folder}...")
    files = []
    for root, _, fs in os.walk(folder):
        for file in fs:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            files.append((size, path))
    files.sort(reverse=True)
    for size, path in files[:n]:
        print(f"{path} - {size / (1024 * 1024):.2f} MB")

def schedule_organization(folder, interval_sec=60):
    print(f"Scheduling organization every {interval_sec} seconds. Ctrl+C to stop.")
    try:
        while True:
            organize_files_by_extension(folder)
            remove_duplicates(folder)
            time.sleep(interval_sec)
    except KeyboardInterrupt:
        print("Stopped scheduled organization.")

def main():
    folder = input("Enter folder path to organize: ")

    while True:
        print("\nMenu:")
        print("1. Organize files by extension")
        print("2. Remove duplicate files")
        print("3. Bulk rename files")
        print("4. Find largest files")
        print("5. Schedule automatic organization")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            organize_files_by_extension(folder)

        elif choice == '2':
            remove_duplicates(folder)

        elif choice == '3':
            pattern = input("Enter rename pattern (use {num} for numbering, e.g. file_{num}): ")
            bulk_rename(folder, pattern)

        elif choice == '4':
            n = int(input("How many largest files to show? "))
            find_largest_files(folder, n)

        elif choice == '5':
            interval = int(input("Enter interval in seconds: "))
            schedule_organization(folder, interval)

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
