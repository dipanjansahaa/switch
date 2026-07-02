import json
from src.ingest import DocumentLoader
from src.chunk import TextChunker
from src.chunk import RecursiveChunker
from src.embed import EmbeddingGenerator
from src.indexer import VectorIndexer
import config

def main():

    print("Loading documents...")

    loader = DocumentLoader(config.DATA_PATH)
    documents = loader.load_documents()

    print(f"Loaded {len(documents)} documents")


    print("\nChunking...")

    # chunker = TextChunker(
    #     chunk_size = CHUNK_SIZE,
    #     overlap = CHUNK_OVERLAP
    # )

    chunker = RecursiveChunker(
        chunk_size = config.CHUNK_SIZE,
        overlap = config.CHUNK_OVERLAP
    )

    chunks = chunker.create_chunks(documents)

    with open(
        config.CHUNK_JSON_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            chunks,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(f"Created {len(chunks)} chunks")


    print("\nGenerating embeddings...")

    embedder = EmbeddingGenerator(model_name = config.EMBEDDING_MODEL)

    embeddings = embedder.generate_embeddings(chunks)


    print("\nBuilding FAISS index...")

    indexer = VectorIndexer()

    indexer.create_index(embeddings)

    indexer.save_index()

    indexer.save_chunks(chunks)


    print("\nDone!")

    print("FAISS Index Saved")

    print("Chunks Saved")


if __name__ == "__main__":
    main()