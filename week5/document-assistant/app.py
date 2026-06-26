from src.ingest import DocumentLoader
from src.chunk import TextChunker
from src.embed import EmbeddingGenerator
from src.indexer import VectorIndexer
from src.retriever import Retriever
from src.llm import LLM
from src.rag import RAGPipeline
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


# Add LLM and RAG
llm = LLM()

rag = RAGPipeline(
    retriever,
    llm
)

# Ask Question
question = input("Ask a question: ")

response = rag.ask(question)

print("\n")
print("=" * 80)
print("ANSWER")
print("=" * 80)

print(response["answer"])


print("\n")
print("=" * 80)
print("SOURCES")
print("=" * 80)

for source in response["sources"]:

    print(f"\n{source['filename']} | Chunk {source['chunk_id']}")
    print("-" * 50)
    print(source["text"][:250])