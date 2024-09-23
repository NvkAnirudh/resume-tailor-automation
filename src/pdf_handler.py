import os
import io
import pdfplumber
from pypdf import PdfReader

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

    # with pdfplumber.open(io.BytesIO(file_buffer)) as pdf:
    #     text = ''
    #     for page in pdf.pages:
    #         text += page.extract_text()
    # return text