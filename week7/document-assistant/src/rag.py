from src.prompt import PromptBuilder
import config


class RAGPipeline:

    def __init__(
        self,
        retriever,
        llm,
        query_expander=None
    ):

        self.retriever = retriever
        self.llm = llm
        self.query_expander = query_expander


    def ask(
        self,
        question,
        # k = config.TOP_K
    ):

        if self.query_expander:
            expanded_query = self.query_expander.expand(question)
        else:
            expanded_query = question

        print("Expanded Query:", expanded_query)

        retrieved_chunks = self.retriever.retrieve(
            query=expanded_query,
            strategy=config.RETRIEVAL_TYPE,
            k=config.TOP_K,
            threshold=config.SCORE_THRESHOLD
        )

        prompt = PromptBuilder.build_prompt(
            retrieved_chunks,
            question
        )

        answer = self.llm.generate(
            prompt
        )

        return {

            "answer": answer,

            "sources": retrieved_chunks

        }