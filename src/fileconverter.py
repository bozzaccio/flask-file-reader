from typing import Tuple

from pdf2docx import Converter


def convert_pdf2docx(pdf_file: str, docx_file: str, pages: Tuple = None):
    cv = Converter(pdf_file)
    cv.convert(docx_file)  # all pages by default
    cv.close()

    summary = {
        "File": pdf_file, "Pages": "All", "Output File": docx_file
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return summary
