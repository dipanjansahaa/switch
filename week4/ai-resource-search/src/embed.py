from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingGenerator:

    def __init__(
        self,
        model_name="all-MiniLM-L6-v2"
    ):
        self.model = SentenceTransformer(
            model_name
        )

    def generate_embeddings(
        self,
        texts
    ):

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        return embeddings