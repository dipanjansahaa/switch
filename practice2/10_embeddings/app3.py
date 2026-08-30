# document embeddings, query embeddings
from langchain_ollama import OllamaEmbeddings


def create_embeddings(
    model_name,
    documents,
    query
):
    embeddings = OllamaEmbeddings(
        model = model_name
    )

    document_vectors = embeddings.embed_documents(
        documents
    )

    query_vector = embeddings.embed_query(
        query
    )

    print("Documents:")
    for document, vector in zip(
        documents,
        document_vectors
    ):
        print(f"\n{document}")
        print(f"Vector dimensions: {len(vector)}")

    print("\nQuery:")
    print(query)

    print("\nQuery vector dimensions:")
    print(len(query_vector))


create_embeddings(
    model_name = "nomic-embed-text",
    documents = [
        "LangChain is a framework for building LLM applications.",
        "RAG retrieves relevant information before generation.",
        "Python is commonly used for machine learning."
    ],
    query = "How does retrieval augmented generation work?"
)
