import os

import PyPDF2

from app import UPLOAD_FOLDER


def pdf_reader(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    with open(filepath, mode='rb') as f:

        reader = PyPDF2.PdfFileReader(f)
        total_pages = reader.getNumPages()
        i = 0

        while i < total_pages:
            page = reader.getPage(i)
            print(page.extractText())
