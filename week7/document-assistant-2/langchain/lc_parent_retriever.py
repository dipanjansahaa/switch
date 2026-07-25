from langchain.storage import InMemoryStore
from langchain.retrievers import ParentDocumentRetriever
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from src.ingest import DocumentLoader
import config


def build_parent_retriever(data_path):
    """
    Creates a ParentDocumentRetriever using LangChain.
    """

    loader = DocumentLoader(data_path)
    documents = loader.load_documents()

    docs = []

    for doc in documents:
        docs.append(
            Document(
                page_content=doc["content"],
                metadata={
                    "filename": doc["filename"],
                    "page": doc["page"]
                }
            )
        )

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    parent_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )

    child_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

    vectorstore = FAISS.from_documents(
        [],
        embeddings
    )

    store = InMemoryStore()

    retriever = ParentDocumentRetriever(
        vectorstore=vectorstore,
        docstore=store,
        child_splitter=child_splitter,
        parent_splitter=parent_splitter
    )

    retriever.add_documents(docs)

    return retriever


if __name__ == "__main__":

    retriever = build_parent_retriever(config.DATA_PATH)

    while True:

        query = input("\nAsk a question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        results = retriever.invoke(query)

        print("\nRetrieved Parent Documents\n")

        for i, doc in enumerate(results, start=1):

            print("=" * 80)
            print(f"Document {i}")
            print("=" * 80)

            print(f"File : {doc.metadata.get('filename')}")
            print(f"Page : {doc.metadata.get('page')}")

            print("\nContent:\n")
            print(doc.page_content)

            print("\n")