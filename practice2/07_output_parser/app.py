# StrOutputParser
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

    response = model.invoke(
        prompt.invoke({
            "question": question
        })
    )

    print("Without parser:")
    print(response)
    print(type(response))

    print("Content:")
    print(response.content)
    print(type(response.content))

    parser = StrOutputParser()

    parsed_response = parser.invoke(response)

    print("\nWith parser:")
    print(parsed_response)
    print(type(parsed_response))


generate_answer(
    model_name = "llama3.2:3b",
    temperature = 0,
    question = "What is RAG?"
)
