import json
import numpy as np

from src.ingest import DocumentLoader
from src.chunk import TextChunker
from src.embed import EmbeddingGenerator
from src.indexer import VectorIndexer


def main():

    print("\nLoading documents...")

    loader = DocumentLoader("data/docs")
    documents = loader.load_documents()

    print(f"Loaded {len(documents)} documents")

    print("\nChunking documents...")

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

    print(f"Created {len(all_chunks)} chunks")

    print("\nGenerating embeddings...")

    texts = [
        chunk["text"]
        for chunk in all_chunks
    ]

    embedder = EmbeddingGenerator()

    embeddings = embedder.generate_embeddings(
        texts
    )

    np.save(
        "data/embeddings.npy",
        embeddings
    )

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

    print("Saved embeddings.npy")
    print("Saved chunks.json")

    print("\nBuilding FAISS index...")

    indexer = VectorIndexer()

    indexer.create_index(
        embeddings
    )

    indexer.save_index()

    print("Saved faiss.index")

    print("\nIndex build completed.")


if __name__ == "__main__":
    main()