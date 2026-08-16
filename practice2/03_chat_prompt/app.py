# Chat Prompt Template
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def generate_explanation(
    model_name,
    temperature,
    topic,
    audience
):
    model = ChatOllama(
        model = model_name,
        temperature = temperature
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an expert technical instructor. "
            "Explain concepts clearly and accurately."
            # "You are a strict interview coach. "
            # "Give concise answers and include two interview tips."
        ),
        (
            "human",
            "Explain {topic} to a {audience} audience."
        ),
        (
            "ai",
            "Sure. I'll explain it clearly."
        ),
        (
            "human",
            "Now give me a simple example."
        )
    ])

    # human/user and ai/assistant are role aliases in LangChain’s message system

    messages = prompt.invoke({
        "topic": topic,
        "audience": audience
    })

    # for message in messages.messages:
    #     print(type(message))
    #     print(message.content)
    #     print()

    # print(f"Formatted Prompt: {messages}")
    # print()

    response = model.invoke(messages)

    print(response.content)

generate_explanation(
    model_name = "llama3.2:3b",
    temperature = 0,
    topic = "LangChain",
    audience = "beginner"
)
