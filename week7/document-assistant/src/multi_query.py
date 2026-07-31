# from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_ollama import ChatOllama
import config


class MultiQuerySearch:

    def __init__(self, vectorstore):

        self.llm = ChatOllama(
            model=config.LLM_MODEL,
            temperature=0
        )

        self.retriever = MultiQueryRetriever.from_llm(
            retriever=vectorstore.as_retriever(
                search_kwargs={"k": 5}
            ),
            llm=self.llm
            # verbose=True
        )

    def retrieve(self, query):

        docs = self.retriever.invoke(query)

        results = []

        for doc in docs:

            results.append(
                {
                    "filename": doc.metadata["filename"],
                    "page": doc.metadata["page"],
                    "chunk_id": doc.metadata["chunk_id"],
                    "text": doc.page_content
                }
            )

        return results