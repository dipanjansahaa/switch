# model.stream() with lcel
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def generate_answer(
    model_name,
    temperature,
    topic
):
    model = ChatOllama(
        model = model_name,
        temperature = temperature
    )

    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in detail."
    )

    parser = StrOutputParser()

    chain = prompt | model | parser

    for chunk in chain.stream({
        "topic": topic
    }):
        print(chunk, end="", flush=True)

    print()


generate_answer(
    model_name = "llama3.2:3b",
    temperature = 0,
    topic = "Retrieval Augmented Generation"
)
