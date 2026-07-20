import os
import PyPDF2
import argparse
from datetime import datetime


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file

    Returns:
        str: Extracted text from the PDF
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return None


def save_text_to_file(text, output_path):
    """
    Save text to a file.

    Args:
        text (str): Text to save
        output_path (str): Path to save the text file
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
        return True
    except Exception as e:
        print(f"Error saving file {output_path}: {str(e)}")
        return False


def process_directory(directory):
    """
    Process all PDF files in a directory and its subdirectories.

    Args:
        directory (str): Path to the directory to process
    """
    processed_count = 0
    skipped_count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                txt_path = os.path.splitext(pdf_path)[0] + '.txt'

                # Check if the text file already exists
                if os.path.exists(txt_path):
                    print(f"Skipping {pdf_path} - already processed")
                    skipped_count += 1
                    continue

                print(f"Processing: {pdf_path}")
                text = extract_text_from_pdf(pdf_path)

                if text:
                    success = save_text_to_file(text, txt_path)
                    if success:
                        processed_count += 1
                        # Get the base name without extension for cleaner output
                        base_name = os.path.basename(pdf_path)
                        print(f"✓ Successfully processed {base_name}")
                    else:
                        print(f"✗ Failed to save text for {base_name}")
    print(f