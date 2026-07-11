import faiss
import numpy as np
import config
from src.embed import Reranker

class Retriever:

    def __init__(
        self,
        index,
        chunks,
        embedder,
        bm25=None
    ):
        self.index = index
        self.chunks = chunks
        self.embedder = embedder
        self.bm25 = bm25

        if config.RETRIEVAL_TYPE == "reranker":
            self.reranker = Reranker()
        else:
            self.reranker = None


    def retrieve(
        self,
        query: str,
        strategy=config.RETRIEVAL_TYPE,
        k=config.TOP_K,
        threshold=config.SCORE_THRESHOLD
    ):

        if strategy == "similarity":
            return self.similarity_search(
                query, k
            )

        elif strategy == "threshold":
            return self.threshold_search(
                query,
                k,
                threshold
            )

        elif strategy == "hybrid":
            return self.hybrid_search(
                query,
                k
            )

        elif strategy=="reranker":
            return self.rerank_search(
                query,
                k
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


    def hybrid_search(
        self,
        query: str,
        k=config.TOP_K
    ):
        faiss_results = self.similarity_search(
            query,
            k
        )

        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        top_idx = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:k]

        bm25_results = []

        for idx in top_idx:

            bm25_results.append(
                {
                    "score": float(scores[idx]),
                    "filename": self.chunks[idx]["filename"],
                    "page": self.chunks[idx]["page"],
                    "chunk_id": self.chunks[idx]["chunk_id"],
                    "text": self.chunks[idx]["text"]
                }
            )

        merged = {}

        for result in faiss_results + bm25_results:

            key = (
                result["filename"],
                result["chunk_id"]
            )

            merged[key] = result

        return list(merged.values())[:k]


    def rerank_search(
        self,
        query: str,
        k=config.TOP_K
    ):

        results = self.similarity_search(
            query,
            k*2
        )

        results = self.reranker.rerank(
            query,
            results
        )

        return results[:k]