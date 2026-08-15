# prompt
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


def chat(model, temperature, topic):
    model = ChatOllama(
        model = model,
        temperature = temperature
    )

    prompt = PromptTemplate.from_template(
        "Explain {topic} in simple terms in 3 sentences."
    )

    formatted_prompt = prompt.invoke({
        "topic": topic
    })

    response = model.invoke(formatted_prompt)

    print(response.content)

    print()

chat(
    model = "llama3.2:3b",
    temperature = 0,
    topic = "SAP BW/4HANA"
)

chat(
    model = "llama3.2:3b",
    temperature = 0,
    topic = "Retrieval Augmented Generation"
)
