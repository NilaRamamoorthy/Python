import csv

def csv_row_reader(filepath):
    """
    Generator that reads a CSV file row-by-row:
    - Opens file lazily
    - Uses csv.reader for proper parsing
    - Skips header row via next()
    - Strips leading/trailing whitespace from each field
    - Stops immediately if any field in a row == "END"
    """
    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        # Skip header line
        try:
            next(reader)
        except StopIteration:
            return  # empty file
        
        for row in reader:
            # Clean fields lazily
            cleaned = [field.strip() for field in row]
            # If "END" appears in this row, terminate iteration
            if "END" in cleaned:
                return
            yield cleaned
# Create example CSV file
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'Status'])
    writer.writerow(['Alice', '30', 'Active'])
    writer.writerow(['Bob', 'END', 'Inactive'])
    writer.writerow(['Charlie', '25', 'Active'])

print("CSV rows until 'END' encountered:")
for row in csv_row_reader('data.csv'):
    print(row)
