from typing import List


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str) -> List[str]:

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(text[start:end])

            start += self.chunk_size - self.overlap

        return chunks


    def create_chunks(self, documents):

        all_chunks = []

        for document in documents:

            chunks = self.chunk_text(document["content"])

            for idx, chunk in enumerate(chunks):

                all_chunks.append(
                    {
                        "chunk_id": idx,
                        "filename": document["filename"],
                        "text": chunk
                    }
                )

        return all_chunks