import fitz  # type: ignore # PyMuPDF
# Fitz is used it  crack open a PDF file and pull out all the raw text. A PDF is not a simple text file — it's a complex format with pages, fonts, images, and layout data. fitz handles all that complexity for you.

import re

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text() # type: ignore
    
    # Clean up broken newlines and extra whitespace
    text = re.sub(r'\n+', ' ', text)       # replace multiple newlines with space
    text = re.sub(r'\s+', ' ', text)        # collapse multiple spaces
    text = text.strip()
    
    return text

