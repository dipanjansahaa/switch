import faiss
import numpy as np
import config


class Retriever:

    def __init__(
        self,
        index,
        chunks,
        embedder
    ):
        self.index = index
        self.chunks = chunks
        self.embedder = embedder


    def retrieve(
        self,
        query: str,
        strategy=config.RETRIEVAL_TYPE,
        k=config.TOP_K,
        threshold=config.SCORE_THRESHOLD
    ):

        if strategy == "similarity":
            return self.similarity_search(query, k)

        elif strategy == "threshold":
            return self.threshold_search(
                query,
                k,
                threshold
            )

        else:
            raise ValueError(
                f"Unknown strategy: {strategy}"
            )
    

    def similarity_search(
        self,
        query: str,
        k=config.TOP_K
    ):
        """
        Retrieve Top-K chunks using similarity search.
        """

        query_embedding = self.embedder.embed_query(query)

        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            results.append(
                {
                    "score": float(score),
                    "filename": self.chunks[idx]["filename"],
                    "page": self.chunks[idx]["page"],
                    "chunk_id": self.chunks[idx]["chunk_id"],
                    "text": self.chunks[idx]["text"]
                }
            )

        return results
    

    def threshold_search(
        self,
        query: str,
        k=config.TOP_K,
        threshold=config.SCORE_THRESHOLD
    ):
        """
        Retrieve chunks above a similarity threshold.
        """

        query_embedding = self.embedder.embed_query(query)

        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            if score < threshold:
                continue

            results.append(
                {
                    "score": float(score),
                    "filename": self.chunks[idx]["filename"],
                    "page": self.chunks[idx]["page"],
                    "chunk_id": self.chunks[idx]["chunk_id"],
                    "text": self.chunks[idx]["text"]
                }
            )

        return results