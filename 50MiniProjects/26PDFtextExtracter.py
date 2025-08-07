import PyPDF2
import re

def extract_text(pdf_path):
    """Extracts and cleans text from a PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if reader.is_encrypted:
                reader.decrypt("")  # Attempt to decrypt with an empty password
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                page_text = page.extract_text()
                if page_text:
                    text += clean_text(page_text)
            return text
    except PyPDF2.errors.PdfReadError as e:
        print(f"Error reading PDF: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def clean_text(text):
    """Cleans the extracted text by removing unwanted characters."""
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.strip()  # Remove leading and trailing whitespace
    return text

def extract_text_generator(pdf_path):
    """Generator that yields cleaned text from each page of the PDF."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if reader.is_encrypted:
                reader.decrypt("")  # Attempt to decrypt with an empty password
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                page_text = page.extract_text()
                if page_text:
                    yield clean_text(page_text)
    except PyPDF2.errors.PdfReadError as e:
        print(f"Error reading PDF: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    pdf_path = 'sample.pdf'
    
    # Extract and clean text from the entire PDF
    full_text = extract_text(pdf_path)
    if full_text:
        print("Extracted Text:")
        print(full_text)
    
    # Extract and clean text page by page using a generator
    print("\nExtracted Text by Page:")
    for page_text in extract_text_generator(pdf_path):
        print(page_text)
