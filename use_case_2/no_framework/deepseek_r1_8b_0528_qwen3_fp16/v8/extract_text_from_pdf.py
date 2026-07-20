import os
import PyPDF2
from pathlib import Path


def extract_text_from_pdf(pdf_path, txt_path):
    """Extract text from a PDF file and save it to a text file."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
            return True
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return False


def process_pdfs_in_directory(directory):
    """Process all PDF files in a directory and its subdirectories."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                # Create a txt file with the same name but .txt extension
                txt_path = os.path.splitext(pdf_path)[0] + '.txt'
                print(f"Extracting text from: {pdf_path}")
                extract_text_from_pdf(pdf_path, txt_path)


if __name__ == "__main__":
    # Get the directory from the user
    directory = input("Enter the path to the directory containing PDF files: ").strip()

    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Error: The specified directory does not exist.")
    else:
        # Process all PDF files in the directory and its subdirectories
        process_pdfs_in_directory(directory)
        print("Text extraction completed for all PDF files.")