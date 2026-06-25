from src.ingest import DocumentLoader
from src.chunk import TextChunker
from src.embed import EmbeddingGenerator
from src.indexer import VectorIndexer
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


indexer = VectorIndexer()

index = indexer.create_index(embeddings)



indexer.save_index()

indexer.save_chunks(chunks)


print("=" * 60)
print("FAISS index created")
print("=" * 60)

print()

print(f"Vectors stored : {index.ntotal}")

print(f"Chunks stored  : {len(chunks)}")