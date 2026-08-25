# RunnablePassthrough, RunnableLambda, RunnableParallel
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)


def count_words(text: str) -> int:
    return len(text.split())


def create_chain(model_name, temperature):

    model = ChatOllama(
        model = model_name,
        temperature = temperature
    )

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using the following context.

        Context:
        {context}

        Question:
        {question}
        """
    )

    fake_retriever = RunnableLambda(
        lambda question: (
            "RAG stands for Retrieval-Augmented Generation. "
            "It retrieves relevant information before generating an answer. "
            "We use RAG to build LLMs. "
        )
    )

    word_count = RunnableLambda(count_words)

    chain = (
        RunnableParallel(
            context = fake_retriever,
            question = RunnablePassthrough(),
            word_count = word_count
        )
        | prompt
        | model
        | StrOutputParser()
    )

    return chain


def main():
    chain = create_chain(
        model_name = "llama3.2:3b",
        temperature = 0
    )

    response = chain.invoke(
        "What is RAG?"
    )

    print(response)


if __name__ == "__main__":
    main()
