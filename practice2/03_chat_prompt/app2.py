from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


model = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. You are name is Don Kihote. You are sarcastic."
    ),
    MessagesPlaceholder(variable_name="history"),
    (
        "human",
        "{question}"
    )
])

history = [
    HumanMessage(content="My name is Dipanjan.")
]

while True:
    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        break

    messages = prompt.invoke({
        "history": history,
        "question": question
    })

    response = model.invoke(messages)

    print("Assistant:", response.content)

    # Update conversation history
    history.append(HumanMessage(content=question))
    history.append(AIMessage(content=response.content))

# What is my name?
# What is your name?
# Will you mind if I ask you any question?
