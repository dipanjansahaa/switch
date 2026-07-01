from src.prompt import PromptBuilder


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
        k = 5
    ):

        retrieved_chunks = self.retriever.retrieve(
            question,
            k
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