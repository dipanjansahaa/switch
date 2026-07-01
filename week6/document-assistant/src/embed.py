from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingGenerator:

    def __init__(
        self,
        model_name="BAAI/bge-small-en-v1.5"
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