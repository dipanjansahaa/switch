from src.indexer import VectorIndexer
from src.search import SemanticSearcher


def main():

    print("\nLoading index...")

    indexer = VectorIndexer()

    indexer.load_index()

    searcher = SemanticSearcher(
        indexer.index
    )

    print("Search engine ready.")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("Search: ").strip()

        if query.lower() == "exit":
            break

        results = searcher.search(
            query,
            k=5
        )

        print("\nResults:\n")

        for result in results:

            print("=" * 70)

            print(
                f"Score: {result['score']:.4f}"
            )

            print(
                f"File: {result['chunk']['filename']}"
            )

            print(
                f"Chunk ID: {result['chunk']['chunk_id']}"
            )

            print()

            print(
                result["chunk"]["text"][:400]
            )

            print("\n")

    print("Goodbye.")


if __name__ == "__main__":
    main()