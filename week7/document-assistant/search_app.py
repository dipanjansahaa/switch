from src.embed import EmbeddingGenerator
from src.indexer import VectorIndexer
from src.retriever import Retriever
from src.llm import LLM
from src.rag import RAGPipeline
from src.query_expander import QueryExpander
import config


def main():

    print("Loading Vector Store...")

    indexer = VectorIndexer()

    index = indexer.load_index()

    chunks = indexer.load_chunks()

    bm25 = indexer.load_bm25()


    embedder = EmbeddingGenerator()

    retriever = Retriever(
        index=index,
        chunks=chunks,
        embedder=embedder,
        bm25=bm25
    )


    llm = LLM()

    if config.ENABLE_QUERY_EXPANSION:
        query_expander = QueryExpander(llm)
    else:
        query_expander = None


    rag = RAGPipeline(
        retriever,
        llm,
        query_expander
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

            # if source['score'] >= 0.75:
            #     print(
            #         f"- {source['filename']} | Page {source['page']} | Chunk {source['chunk_id']} | Similarity: {source['score']:.4f}"
            #     )

        print("-" * 60)

        print()
        print()

if __name__ == "__main__":
    main()