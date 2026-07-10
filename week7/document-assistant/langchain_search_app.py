from src.ingest import DocumentLoader
from src.chunk import TextChunker
from src.langchain_indexer import LangChainIndexer
from src.langchain_retriever import LangChainRetriever
from src.prompt import PromptBuilder
from src.llm import LLM


def main():

    print("Building LangChain Vector Store...")

    loader = DocumentLoader("data/docs")
    documents = loader.load_documents()

    chunker = TextChunker()

    chunks = chunker.create_chunks(documents)

    indexer = LangChainIndexer()

    vectorstore = indexer.create_vectorstore(chunks)

    retriever = LangChainRetriever(vectorstore)

    llm = LLM()

    print("\nLangChain RAG Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break

        docs = retriever.mmr(
            question,
            k=5,
            fetch_k=20,
            lambda_mult=0.5
        )

        context_chunks = []

        for i, doc in enumerate(docs):

            context_chunks.append(
                {
                    "filename": doc.metadata["filename"],
                    "page": doc.metadata["page"],
                    "chunk_id": doc.metadata["chunk_id"],
                    "text": doc.page_content
                }
            )

        prompt = PromptBuilder.build_prompt(
            context_chunks,
            question
        )

        answer = llm.generate(prompt)

        print("\nAssistant: ", end = "")
        print(answer)

        print("\nSources:")

        for doc in docs:

            print(
                f"- {doc.metadata['filename']} | Page {doc.metadata['page']} | Chunk {doc.metadata['chunk_id']}"
            )

        print("-" * 60)
        print()


if __name__ == "__main__":
    main()