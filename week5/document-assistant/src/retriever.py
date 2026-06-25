import faiss
import numpy as np


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
        k: int = 3
    ):
        """
        Retrieve the Top-K most relevant chunks.
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
                    "chunk_id": self.chunks[idx]["chunk_id"],
                    "text": self.chunks[idx]["text"]
                }
            )

        return results