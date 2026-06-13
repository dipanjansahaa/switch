from src.ingest import DocumentLoader
from src.chunk import TextChunker
import json
from src.embed import EmbeddingGenerator
import numpy as np
from src.indexer import VectorIndexer
from src.search import SemanticSearcher


loader = DocumentLoader("data/docs")

documents = loader.load_documents()

chunker = TextChunker(
    chunk_size=500,
    overlap=50
)

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

# print(all_chunks[0])
# print(all_chunks[-1])


with open(
    "data/chunks.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        all_chunks,
        f,
        indent=2,
        ensure_ascii=False
    )

texts = [
    chunk["text"]
    for chunk in all_chunks
]

embedder = EmbeddingGenerator()

embeddings = embedder.generate_embeddings(
    texts
)

# print(embeddings.shape)
# print(embeddings[0][:10])

np.save(
    "data/embeddings.npy",
    embeddings
)

# embeddings = np.load(
#     "data/embeddings.npy"
# )

# print(loaded_embeddings.shape)

indexer = VectorIndexer()

indexer.create_index(
    embeddings
)

indexer.save_index()

print(indexer.index.ntotal)

searcher = SemanticSearcher(
    indexer.index
)

results = searcher.search(
    "How does retrieval augmented generation work?"
)

for result in results:

    print("\n")
    print("=" * 60)

    print(
        f"Score: {result['score']:.4f}"
    )

    print(
        result["chunk"]["filename"]
    )

    print(
        result["chunk"]["text"][:300]
    )