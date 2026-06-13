from src.ingest import DocumentLoader


loader = DocumentLoader("data/docs")

documents = loader.load_documents()

for doc in documents:
    print("=" * 60)
    print(doc["filename"])
    print("=" * 60)

    print(doc["content"][:500])
    print()