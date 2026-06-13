from src.ingest import DocumentLoader
from src.chunk2 import TextChunker
import json

loader = DocumentLoader("data/docs")

documents = loader.load_documents()

chunker = TextChunker(max_chars=500)

all_chunks = []

for doc in documents:

    chunks = chunker.chunk_text(
        doc["content"]
    )

    for idx, chunk in enumerate(chunks):

        all_chunks.append(
            {
                "filename": doc["filename"],
                "chunk_id": idx,
                "text": chunk
            }
        )

print(f"\nTotal Chunks: {len(all_chunks)}\n")

print(all_chunks[0])
print(all_chunks[-1])

with open(
    "data/chunks2.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        all_chunks,
        f,
        indent=2,
        ensure_ascii=False
    )