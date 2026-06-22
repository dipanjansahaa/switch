from src.ingest import DocumentLoader


loader = DocumentLoader("data/docs")

documents = loader.load_documents()


for doc in documents:
    print("=" * 50)
    print(doc["filename"])
    print(doc["content"][:300])