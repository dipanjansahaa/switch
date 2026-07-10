from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


class LangChainIndexer:

    def __init__(
        self,
        model_name="BAAI/bge-small-en-v1.5"
    ):

        self.embedding = HuggingFaceEmbeddings(
            model_name=model_name
        )

        self.vectorstore = None


    def create_vectorstore(
        self,
        chunks
    ):

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        metadatas = [

            {
                "filename": chunk["filename"],
                "page": chunk["page"],
                "chunk_id": chunk["chunk_id"]
            }

            for chunk in chunks

        ]

        self.vectorstore = FAISS.from_texts(

            texts=texts,

            embedding=self.embedding,

            metadatas=metadatas

        )

        return self.vectorstore