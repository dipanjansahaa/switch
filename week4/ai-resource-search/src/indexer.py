import faiss
import numpy as np


class VectorIndexer:

    def __init__(self):
        self.index = None

    def create_index(self, embeddings):

        embeddings = embeddings.astype("float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(
            dimension
        )

        faiss.normalize_L2(
            embeddings
        )

        self.index.add(
            embeddings
        )

        # self.index = faiss.IndexFlatL2(
        #     dimension
        # )

        # self.index.add(embeddings)

        return self.index

    def save_index(
        self,
        path="data/faiss.index"
    ):
        faiss.write_index(
            self.index,
            path
        )

    def load_index(
        self,
        path="data/faiss.index"
    ):
        self.index = faiss.read_index(
            path
        )

        return self.index