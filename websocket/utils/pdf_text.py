
import pdfplumber

def extract_text_from_pdf(pdf_path):
    full_text = ""
    try:
        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            # Iterate through all the pages
            for page in pdf.pages:
                # Extract text from the page
                text = page.extract_text()
                
                # Append the extracted text to the full text
                if text:
                    full_text += text + "\n"
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return ""
    
    return full_text



