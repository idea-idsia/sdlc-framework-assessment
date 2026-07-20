import os
import PyPDF2
import argparse


def extract_text_from_pdf(pdf_path, txt_path):
    """
    Extract text from a PDF file and save it to a text file.

    Args:
        pdf_path (str): Path to the PDF file
        txt_path (str): Path to save the extracted text
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"

            # Write the extracted text to a file
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
            return True
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return False


def process_pdfs_in_directory(directory):
    """
    Process all PDF files in a directory and its subdirectories.

    Args:
        directory (str): Path to the directory to process
    """
    total_processed = 0
    total_skipped = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                txt_path = os.path.splitext(pdf_path)[0] + '.txt'

                # Check if the text file already exists
                if os.path.exists(txt_path):
                    print(f"Skipping {pdf_path} - already processed")
                    total_skipped += 1
                    continue

                print(f"Processing: {pdf_path}")
                success = extract_text_from_text(pdf_path, txt_path)
                if success:
                    total_processed += 1
                else:
                    print(f"Failed to process {pdf_path}")

    return total_processed, total_skipped


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract text from PDF files and save as text files.')
    parser.add_argument('directory', help='Path to the directory containing PDF files')
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: The directory '{args.directory}' does not exist.")
        exit(1)

    print(f"Starting text extraction from PDF files in '{args.directory}'...")
    processed, skipped = process_pdfs_in_directory(args.directory)

    print(f"\nSummary:")
    print(f"Files processed: {processed}")
    print(f"Files skipped (already have text): {skipped}")
    print(f"Total PDF files found: {processed + skipped}")
    print("Extraction completed.")