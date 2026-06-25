from src.ingest import DocumentLoader
from src.chunk import TextChunker


loader = DocumentLoader("data/docs")

documents = loader.load_documents()

print("=" * 60)
print("Documents Loaded")
print("=" * 60)

for document in documents:
    print(document["filename"])

print()


chunker = TextChunker(
    chunk_size=500,
    overlap=50
)

chunks = chunker.create_chunks(documents)


print("=" * 60)
print(f"Total Chunks: {len(chunks)}")
print("=" * 60)


for chunk in chunks[:13]:

    print(f"File      : {chunk['filename']}")
    print(f"Chunk ID  : {chunk['chunk_id']}")
    print(chunk["text"][:150])
    print("-" * 60)