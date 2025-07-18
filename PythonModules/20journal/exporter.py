import os
from datetime import datetime

def export_all_entries(output_file="full_journal_export.txt"):
    folder = "journal_entries"
    output_path = os.path.join(folder, output_file)
    with open(output_path, "w") as out_file:
        for fname in sorted(os.listdir(folder)):
            if fname.endswith(".txt"):
                path = os.path.join(folder, fname)
                out_file.write(f"===== {fname} =====\n")
                with open(path) as f:
                    out_file.write(f.read())
                    out_file.write("\n\n")
    print(f"Journal exported to {output_path}")
