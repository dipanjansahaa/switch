# model.stream()
from langchain_ollama import ChatOllama


def generate_answer(
    model_name,
    temperature,
    question
):
    model = ChatOllama(
        model = model_name,
        temperature = temperature
    )

    # print("Assistant: ", end="", flush=True)

    for chunk in model.stream(question):
        print(chunk.content, end="", flush=True)

    print()

    print(model.stream(question))

    # response = model.invoke(question)

    # print(response.content)


generate_answer(
    model_name = "llama3.2:3b",
    temperature = 0,
    question = "Explain Retrieval Augmented Generation"
)
