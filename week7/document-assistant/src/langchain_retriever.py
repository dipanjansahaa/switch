class LangChainRetriever:

    def __init__(
        self,
        vectorstore
    ):

        self.vectorstore = vectorstore


    def similarity(
        self,
        query,
        k=5
    ):

        return self.vectorstore.similarity_search(
            query,
            k=k
        )


    def mmr(
        self,
        query,
        k=5,
        fetch_k=20,
        lambda_mult=0.5
    ):

        return self.vectorstore.max_marginal_relevance_search(

            query,

            k=k,

            fetch_k=fetch_k,

            lambda_mult=lambda_mult

        )