from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)

    full_text = ""

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text:
            full_text += f"\n--- PAGE {page_num} ---\n"
            full_text += text

    return full_text