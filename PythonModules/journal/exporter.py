# journal/exporter.py

import os

JOURNAL_DIR = "journal_entries"

def export_to_file(output_filename="all_journal_entries.txt"):
    with open(output_filename, "w") as outfile:
        for filename in sorted(os.listdir(JOURNAL_DIR)):
            outfile.write(f"=== {filename} ===\n")
            with open(os.path.join(JOURNAL_DIR, filename), "r") as infile:
                outfile.write(infile.read() + "\n")
    print(f"\n✅ All entries exported to {output_filename}")
