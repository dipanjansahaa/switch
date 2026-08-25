# RunnablePassthrough, RunnableLambda, RunnableParallel
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from langchain_core.runnables import RunnableSequence
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableLambda, RunnableParallel


def count_words(text):
    return len(text.split())

def main():
    # model = ChatOllama(
    #     model = "llama3.2:3b",
    #     temperature = 0
    # )

    # prompt = ChatPromptTemplate.from_messages([
    #     (
    #         "system",
    #         "You are a helpful technical instructor."
    #     ),
    #     (
    #         "human",
    #         "Explain {topic} in simple terms."
    #     )
    # ])

    # parser = StrOutputParser()

    # print("Prompt is Runnable:", isinstance(prompt, Runnable))
    # print("Model is Runnable:", isinstance(model, Runnable))
    # print("Parser is Runnable:", isinstance(parser, Runnable))

    # chain_1 = prompt | model | parser

    # chain_2 = RunnableSequence(
    #     prompt,
    #     model,
    #     parser
    # )

    # inputs = {
    #     "topic": "Runnables in LangChain"
    # }

    # print(chain_1.invoke(inputs))
    # print()

    # print(chain_2.invoke(inputs))
    # print()

    inputs = {
        "question": "What is RAG?"
    }

    chain = RunnablePassthrough()

    result = chain.invoke("Hello")

    print(result)

    word_count = RunnableLambda(count_words)

    chain2 = RunnableParallel(
        original = RunnablePassthrough(),
        word_count = word_count
    )

    result = chain2.invoke("What is RAG?")

    print(result)


if __name__ == "__main__":
    main()
