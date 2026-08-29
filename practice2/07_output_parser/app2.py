# StrOutputParser, LCEL
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def generate_answer(
    model_name,
    temperature,
    question
):
    model = ChatOllama(
        model = model_name,
        temperature = temperature
    )

    prompt = ChatPromptTemplate.from_template(
        "Answer this question in 3 sentences:\n{question}"
    )

    parser = StrOutputParser()

    chain = prompt | model | parser

    response = chain.invoke({
        "question": question
    })

    print(response)
    print(type(response))


generate_answer(
    model_name = "llama3.2:3b",
    temperature = 0,
    question = "What is RAG?"
)
