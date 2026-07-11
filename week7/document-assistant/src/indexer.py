import faiss
import pickle
import numpy as np
import config
from rank_bm25 import BM25Okapi

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
        index_path = config.INDEX_PATH
    ):

        faiss.write_index(
            self.index,
            index_path
        )


    def load_index(
        self,
        index_path = config.INDEX_PATH
    ):

        self.index = faiss.read_index(
            index_path
        )

        return self.index


    def save_chunks(
        self,
        chunks,
        chunk_path = config.CHUNK_PATH
    ):

        with open(chunk_path, "wb") as file:
            pickle.dump(chunks, file)


    def load_chunks(
        self,
        chunk_path = config.CHUNK_PATH
    ):

        with open(chunk_path, "rb") as file:
            chunks = pickle.load(file)

        return chunks


    def create_bm25(self, chunks):

        tokenized_corpus = [
            chunk["text"].lower().split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(tokenized_corpus)

        return self.bm25


    def save_bm25(
        self,
        path="data/vector_store/bm25.pkl"
    ):

        with open(path, "wb") as f:
            pickle.dump(self.bm25, f)


    def load_bm25(
        self,
        path="data/vector_store/bm25.pkl"
    ):

        with open(path, "rb") as f:

            self.bm25 = pickle.load(f)

        return self.bm25