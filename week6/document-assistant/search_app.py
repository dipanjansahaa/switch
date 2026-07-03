from src.embed import EmbeddingGenerator
from src.indexer import VectorIndexer
from src.retriever import Retriever
from src.llm import LLM
from src.rag import RAGPipeline


def main():

    print("Loading Vector Store...")

    indexer = VectorIndexer()

    index = indexer.load_index()

    chunks = indexer.load_chunks()


    embedder = EmbeddingGenerator()

    retriever = Retriever(
        index=index,
        chunks=chunks,
        embedder=embedder
    )


    llm = LLM()

    rag = RAGPipeline(
        retriever,
        llm
    )


    print("\nRAG Assistant Ready!")
    print("Type 'exit' to quit.\n")


    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break


        response = rag.ask(question)


        print("\nAssistant: ", end = "")
        print(response["answer"])


        print("\nSources:")

        for source in response["sources"]:

            print(
                f"- {source['filename']} | Page {source['page']} | Chunk {source['chunk_id']} | Similarity: {source['score']:.4f}"
            )

        print("-" * 60)

        print()
        print()

if __name__ == "__main__":
    main()