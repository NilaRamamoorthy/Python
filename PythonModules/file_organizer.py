from file_organizer.organizer import organize_directory

def main():
    folder_path = input("Enter the path to organize: ").strip()
    organize_directory(folder_path)

if __name__ == "__main__":
    main()
