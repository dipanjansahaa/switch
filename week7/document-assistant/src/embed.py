from sentence_transformers import SentenceTransformer
from sentence_transformers import CrossEncoder
import numpy as np
import config


class EmbeddingGenerator:

    def __init__(
        self,
        model_name = config.EMBEDDING_MODEL
    ):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(
        self,
        chunks
    ) -> np.ndarray:
        """
        Generate embeddings for a list of chunk dictionaries.
        """

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        return embeddings


    def embed_query(
        self,
        query: str
    ) -> np.ndarray:
        """
        Generate embedding for a user query.
        """

        embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )

        return embedding


class Reranker:

    def __init__(
        self,
        model_name = config.RERANKER_MODEL

    ):

        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query,
        retrieved_chunks
    ):
        pairs = [
            (query, chunk["text"])
            for chunk in retrieved_chunks
        ]

        scores = self.model.predict(
            pairs
        )

        for score, chunk in zip(
            scores,
            retrieved_chunks
        ):

            chunk["rerank_score"] = float(score)

        retrieved_chunks.sort(
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return retrieved_chunks