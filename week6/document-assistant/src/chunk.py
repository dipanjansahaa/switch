from typing import List
from config import CHUNK_SIZE
from config import CHUNK_OVERLAP


class TextChunker:

    def __init__(
        self,
        chunk_size = CHUNK_SIZE,
        overlap = CHUNK_OVERLAP
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