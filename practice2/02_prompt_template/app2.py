# prompt
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


def chat(model, temperature, topic, audience, sentences):
    model = ChatOllama(
        model = model,
        temperature = temperature
    )

    prompt = PromptTemplate.from_template(
        "Explain {topic} for a {audience} audience "
        "using at most {sentences} sentences."
    )

    formatted_prompt = prompt.invoke({
        "topic": topic,
        "audience": audience,
        "sentences": sentences
    })

    print(f"Formatted Prompt: {formatted_prompt}")
    print()

    response = model.invoke(formatted_prompt)

    print(f"Response: {response.content}")
    print()

chat(
    model = "llama3.2:3b",
    temperature = 0,
    topic = "Retrieval Augmented Generation",
    audience = "beginner",
    sentences = 4
)
