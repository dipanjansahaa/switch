from langchain.retrievers.multi_query import MultiQueryRetriever
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
        )

    def retrieve(self, query):

        return self.retriever.invoke(query)