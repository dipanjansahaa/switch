from src.prompt import PromptBuilder
import config


class RAGPipeline:

    def __init__(
        self,
        retriever,
        llm
    ):

        self.retriever = retriever
        self.llm = llm


    def ask(
        self,
        question,
        # k = config.TOP_K
    ):

        retrieved_chunks = self.retriever.retrieve(
            query=question,
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