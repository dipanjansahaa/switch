from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_core.runnables import RunnableLambda


model = ChatOllama(
    model = "llama3.2:3b",
    temperature = 0
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

def fake_retriever(question: str) -> str:
    return (
        "RAG stands for Retrieval-Augmented Generation. "
        "It retrieves relevant information before generating an answer."
    )

retriever = RunnableLambda(fake_retriever)

chain = (
    RunnableParallel(
        context=retriever,
        question=RunnablePassthrough()
    )
    | prompt
    | model
    | StrOutputParser()
)

