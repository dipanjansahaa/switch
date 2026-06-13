import json
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer


class SemanticSearcher:

    def __init__(
        self,
        index
    ):
        self.index = index

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        with open(
            "data/chunks.json",
            "r",
            encoding="utf-8"
        ) as f:

            self.chunks = json.load(f)

    def search(
        self,
        query,
        k=5
    ):

        # query_vector = self.model.encode(
        #     [query]
        # ).astype("float32")

        query_vector = self.model.encode(
            [query]
        ).astype("float32")

        faiss.normalize_L2(
            query_vector
        )

        # distances, indices = self.index.search(
        #     query_vector,
        #     k
        # )

        # results = []

        # for idx in indices[0]:

        #     results.append(
        #         self.chunks[idx]
        #     )

        distances, indices = self.index.search(
            query_vector,
            k
        )

        results = []

        for score, idx in zip(
            distances[0],
            indices[0]
        ):
            results.append(
                {
                    "score": float(score),
                    "chunk": self.chunks[idx]
                }
            )

        for result in results:

            print(
                f"Score: {result['score']:.4f}"
            )

            print(
                result["chunk"]["filename"]
            )

        return results