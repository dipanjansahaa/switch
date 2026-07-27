from langchain.lc_parent_retriever import build_parent_retriever
import config

retriever = build_parent_retriever(config.DATA_PATH)

while True:

    query = input("\nQuestion: ")

    if query.lower() == "exit":
        break

    docs = retriever.invoke(query)

    print(f"\nRetrieved {len(docs)} parent document(s)\n")

    for i, doc in enumerate(docs, 1):

        print("=" * 80)
        print(f"Parent Document {i}")
        print("=" * 80)

        print("Metadata:")
        print(doc.metadata)

        print("\nContent Preview:\n")
        print(doc.page_content[:1000])
        print("\n")