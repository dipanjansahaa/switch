# memory
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


def chat(model_name, temperature):

    model = ChatOllama(
        model = model_name,
        temperature = temperature
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant."
        ),
        MessagesPlaceholder(
            variable_name="history"
        ),
        (
            "human",
            "{question}"
        )
    ])

    history = []

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            break

        messages = prompt.invoke({
            "history": history,
            # "history": [],
            "question": question
        })

        response = model.invoke(messages)

        print("Assistant:", response.content)

        # print("Assistant: ", end="", flush=True)

        # full_response = ""

        # for chunk in model.stream(messages):
        #     print(chunk.content, end="", flush=True)
        #     full_response += chunk.content

        # print()

        # response = full_response

        history.append(
            HumanMessage(content=question)
        )

        history.append(
            AIMessage(content=response.content)
            # AIMessage(content=response)
        )


chat(
    model_name = "llama3.2:3b",
    temperature = 0
)
