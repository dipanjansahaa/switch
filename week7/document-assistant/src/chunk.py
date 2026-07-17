from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
import config

# own chunker
class TextChunker:

    def __init__(
        self,
        chunk_size = config.CHUNK_SIZE,
        overlap = config.CHUNK_OVERLAP
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
                        "filename": document["filename"],
                        "page": document["page"],
                        "chunk_id": idx,
                        "parent_id": document["parent_id"],
                        "parent_content": document["parent_content"],
                        "text": chunk
                    }
                )

        return all_chunks


# inbuild chunker
class RecursiveChunker:

    def __init__(
        self,
        chunk_size = config.CHUNK_SIZE,
        overlap = config.CHUNK_OVERLAP
    ):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size = chunk_size,

            chunk_overlap = overlap,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )


    def create_chunks(self, documents):

        all_chunks = []

        for document in documents:

            chunks = self.splitter.split_text(
                document["content"]
            )

            for idx, chunk in enumerate(chunks):

                all_chunks.append(
                    {
                        "filename": document["filename"],
                        "page": document["page"],
                        "chunk_id": idx,
                        "parent_id": document["parent_id"],
                        "parent_content": document["parent_content"],
                        "text": chunk
                    }
                )

        return all_chunks