# lcel base
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
        ),
        (
            "human",
            "Explain {topic} to a {audience} audience."
        )
    ])

    chain = prompt | model

    response = chain.invoke({
        "topic": topic,
        "audience": audience
    })

    print(response.content)


generate_explanation(
    model_name = "llama3.2:3b",
    temperature = 0,
    topic = "LangChain Expression Language",
    audience = "beginner"
)
