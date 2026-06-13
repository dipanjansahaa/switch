from pathlib import Path
from pypdf import PdfReader


class DocumentLoader:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_txt(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def load_md(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def load_pdf(self, file_path):
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    def load_documents(self):
        documents = []

        for file_path in self.data_path.iterdir():

            if file_path.suffix == ".txt":
                text = self.load_txt(file_path)

            elif file_path.suffix == ".md":
                text = self.load_md(file_path)

            elif file_path.suffix == ".pdf":
                text = self.load_pdf(file_path)

            else:
                continue

            documents.append(
                {
                    "filename": file_path.name,
                    "content": text
                }
            )

        return documents