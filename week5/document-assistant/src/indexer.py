import faiss
import pickle
import numpy as np


class VectorIndexer:

    def __init__(self):
        self.index = None


    def create_index(
        self,
        embeddings: np.ndarray
    ):

        embeddings = embeddings.astype("float32")

        faiss.normalize_L2(embeddings)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(embeddings)

        return self.index


    def save_index(
        self,
        index_path="data/vector_store/faiss.index"
    ):

        faiss.write_index(
            self.index,
            index_path
        )


    def load_index(
        self,
        index_path="data/vector_store/faiss.index"
    ):

        self.index = faiss.read_index(
            index_path
        )

        return self.index


    def save_chunks(
        self,
        chunks,
        chunk_path="data/vector_store/chunks.pkl"
    ):

        with open(chunk_path, "wb") as file:
            pickle.dump(chunks, file)


    def load_chunks(
        self,
        chunk_path="data/vector_store/chunks.pkl"
    ):

        with open(chunk_path, "rb") as file:
            chunks = pickle.load(file)

        return chunks