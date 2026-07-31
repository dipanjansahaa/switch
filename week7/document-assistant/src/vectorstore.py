from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
import config


class VectorStoreBuilder:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name=config.EMBEDDING_MODEL
        )

    def build(self, chunks):

        docs = []

        for chunk in chunks:

            docs.append(
                Document(
                    page_content=chunk["text"],
                    metadata={
                        "filename": chunk["filename"],
                        "page": chunk["page"],
                        "chunk_id": chunk["chunk_id"]
                    }
                )
            )

        vectorstore = FAISS.from_documents(
            docs,
            self.embeddings
        )

        return vectorstore