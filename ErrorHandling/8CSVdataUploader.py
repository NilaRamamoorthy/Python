import csv
import logging
import os

# Setup logger
logging.basicConfig(filename='csv_upload_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Custom Exception
class InvalidCSVFormatError(Exception):
    pass

def validate_row(row):
    """Sample validation: all fields must be non-empty and numeric (except name)."""
    try:
        name, age, marks = row
        if not name.strip() or not age.isdigit() or not marks.replace('.', '', 1).isdigit():
            raise ValueError("Row has invalid data types or empty fields")
    except ValueError as ve:
        raise ve

def upload_csv(file_path):
    if not file_path.endswith('.csv'):
        raise InvalidCSVFormatError("❌ File must be in .csv format")
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            print(f"📄 Header: {header}")
            print("📥 Valid Records:")

            for row in reader:
                try:
                    validate_row(row)
                    print(f"✅ {row}")
                except Exception as e:
                    logging.error(f"Invalid row {row}: {e}")
                    print(f"❌ Invalid row skipped: {row}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        print("❌ File not found.")
    except InvalidCSVFormatError as icfe:
        logging.error(f"{icfe}")
        print(icfe)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("❌ An error occurred while processing the file.")
    finally:
        print("🔚 Upload process finished.")

# Sample usage
file_path = input("Enter path to CSV file: ").strip()
try:
    upload_csv(file_path)
except InvalidCSVFormatError as e:
    print(e)
