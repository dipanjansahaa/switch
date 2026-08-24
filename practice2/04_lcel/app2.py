# lcel updated
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


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
        ),
        # (
        #     "ai",
        #     "Sure. I'll explain it clearly."
        # ),
        # (
        #     "human",
        #     "Now give me a simple example."
        # )
    ])

    chain = prompt | model | StrOutputParser()

    response = chain.invoke({
        "topic": topic,
        "audience": audience
    })

    print(response)


generate_explanation(
    model_name = "llama3.2:3b",
    temperature = 0,
    topic = "LangChain Expression Language",
    # topic = "LangChain",
    audience = "beginner"
)
