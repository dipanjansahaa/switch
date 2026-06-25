from src.ingest import DocumentLoader
from src.chunk import TextChunker
from src.embed import EmbeddingGenerator
import json


loader = DocumentLoader("data/docs")
documents = loader.load_documents()

chunker = TextChunker(
    chunk_size=500,
    overlap=50
)

chunks = chunker.create_chunks(documents)

with open(
    "data/chunks.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        chunks,
        f,
        indent=2,
        ensure_ascii=False
    )

embedder = EmbeddingGenerator()

embeddings = embedder.generate_embeddings(chunks)

print("=" * 60)
print("Embedding Shape")
print("=" * 60)

print(embeddings.shape)

print()

print("=" * 60)
print("First Chunk")
print("=" * 60)

print(chunks[0]["text"][:200])

print()

print("=" * 60)
print("First Embedding")
print("=" * 60)

print(embeddings[0][:10])