import json
from src.embed import EmbeddingGenerator
from src.indexer import VectorIndexer
from src.retriever import Retriever
from src.llm import LLM
from src.rag import RAGPipeline
from config import *


def build_rag():

    indexer = VectorIndexer()

    index = indexer.load_index(INDEX_PATH)

    chunks = indexer.load_chunks(CHUNK_PATH)

    embedder = EmbeddingGenerator(EMBEDDING_MODEL)

    retriever = Retriever(
        index=index,
        chunks=chunks,
        embedder=embedder
    )

    llm = LLM(LLM_MODEL)

    rag = RAGPipeline(
        retriever,
        llm
    )

    return rag

def load_questions():

    with open(
        "evaluation/evaluation.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

def evaluate():

    rag = build_rag()

    questions = load_questions()

    print("=" * 80)
    print("RAG Evaluation")
    print("=" * 80)

    passed = 0
    category_stats = {}

    for idx, item in enumerate(questions, start=1):

        question = item["question"]

        expected = item["expected"]

        response = rag.ask(question)

        generated = response["answer"]

        print(f"\nQuestion {idx}")

        print("-" * 80)

        print("Question :")

        print(question)

        print()

        print("Expected :")

        print(expected)

        print()

        print("Generated :")

        # generated_lower = generated.lower()

        # expected_lower = expected.lower()

        # correct = expected_lower in generated_lower

        keywords = item["keywords"]

        generated_lower = generated.lower()

        matched_keywords = []

        for keyword in keywords:

            if keyword.lower() in generated_lower:
                matched_keywords.append(keyword)

        correct = len(matched_keywords) >= max(1, len(keywords) // 2)

        print(generated)

        print()

        # print(
        #     f"Result : {'PASS' if correct else 'FAIL'}"
        # )

        print("Matched Keywords :")

        print(matched_keywords)

        print()

        print(
            f"Result : {'PASS' if correct else 'FAIL'}"
        )

        print()

        print("=" * 80)

        if correct:
            passed += 1

        category = item["category"]

        if category not in category_stats:

            category_stats[category] = {
                "pass": 0,
                "total": 0
            }

        category_stats[category]["total"] += 1

        if correct:

            category_stats[category]["pass"] += 1

    accuracy = (passed / len(questions)) * 100

    print("\n")
    print("=" * 80)
    print("CATEGORY REPORT")
    print("=" * 80)

    for category, stats in category_stats.items():

        accuracy = (
            stats["pass"] /
            stats["total"]
        ) * 100

        print(
            f"{category:<20}"
            f"{stats['pass']}/{stats['total']} "
            f"({accuracy:.2f}%)"
        )


if __name__ == "__main__":
    evaluate()