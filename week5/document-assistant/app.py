from src.ingest import DocumentLoader
from src.chunk import TextChunker
from src.embed import EmbeddingGenerator
from src.indexer import VectorIndexer
from src.retriever import Retriever
import json


# Load Documents
loader = DocumentLoader("data/docs")
documents = loader.load_documents()

chunker = TextChunker(
    chunk_size=500,
    overlap=50
)


# Chunk Documents
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



# Generate Embeddings
embedder = EmbeddingGenerator()

embeddings = embedder.generate_embeddings(chunks)



# Create FAISS Index
indexer = VectorIndexer()

index = indexer.create_index(embeddings)



indexer.save_index()

indexer.save_chunks(chunks)



# Create Retriever
retriever = Retriever(
    index=index,
    chunks=chunks,
    embedder=embedder
)


# Ask Question
question = input("Ask a question: ")

results = retriever.retrieve(
    question,
    k=3
)


print("\n" + "=" * 70)
print("Retrieved Chunks")
print("=" * 70)

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")
    print(f"Similarity : {result['score']:.4f}")
    print(f"Source     : {result['filename']}")
    print(f"Chunk ID   : {result['chunk_id']}")
    print("-" * 50)
    print(result["text"][:400])