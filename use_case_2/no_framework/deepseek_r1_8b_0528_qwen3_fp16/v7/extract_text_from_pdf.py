import PyPDF2


def extract_text_from_pdf(pdf_path, txt_path):
    # Open the PDF file in binary read mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)

        # Initialize an empty string to hold the extracted text
        text = ""

        # Loop through all the pages and extract text from each page
        for page in reader.pages:
            # Extract text from the current page
            page_text = page.extract_text()
            text += page_text + "\n"  # Add a newline between pages

        # Write the extracted text to a text file
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

        print(f"Text extracted successfully and saved to {txt_path}")

# Example usage:
# extract_text_from_pdf('example.pdf', 'output.txt')