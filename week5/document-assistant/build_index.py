from src.ingest import DocumentLoader
from src.chunk import TextChunker
from src.embed import EmbeddingGenerator
from src.indexer import VectorIndexer


def main():

    print("Loading documents...")

    loader = DocumentLoader("data/docs")
    documents = loader.load_documents()

    print(f"Loaded {len(documents)} documents")


    print("\nChunking...")

    chunker = TextChunker(
        chunk_size=800,
        overlap=150
    )

    chunks = chunker.create_chunks(documents)

    print(f"Created {len(chunks)} chunks")


    print("\nGenerating embeddings...")

    embedder = EmbeddingGenerator(model_name="BAAI/bge-small-en-v1.5")

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