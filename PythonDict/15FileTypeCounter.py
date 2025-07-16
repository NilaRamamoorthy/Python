# List of filenames
filenames = [
    "report.pdf", "data.csv", "image.png", "notes.txt",
    "presentation.pptx", "image.jpg", "summary.pdf", "readme.txt"
]

# 1. Count file types
file_types = {}

for name in filenames:
    if '.' in name:
        ext = name.split('.')[-1]
        file_types[ext] = file_types.get(ext, 0) + 1

# 2. Display file type count
print("File Extension Count:")
for ext, count in file_types.items():
    print(f".{ext}: {count} file(s)")
