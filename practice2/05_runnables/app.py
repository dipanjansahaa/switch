from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable


def main():
    model = ChatOllama(
        model = "llama3.2:3b",
        temperature = 0
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful technical instructor."
        ),
        (
            "human",
            "Explain {topic} in simple terms."
        )
    ])

    parser = StrOutputParser()

    print("Prompt is Runnable:", isinstance(prompt, Runnable))
    print("Model is Runnable:", isinstance(model, Runnable))
    print("Parser is Runnable:", isinstance(parser, Runnable))


if __name__ == "__main__":
    main()
