from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage


def chat(model, temperature, content):
    model = ChatOllama(
        model = model,
        temperature = temperature
    )

    messages = [
        HumanMessage(
            content=content
        )
    ]

    response = model.invoke(messages)

    print(response.content)

    print()
    print(response.response_metadata["model_name"])

    print(response.response_metadata)
    print(response.usage_metadata)

    print()
    total_duration = round(int(response.response_metadata["total_duration"]) / 10 ** 9, 3)
    prompt_eval_duration = round(int(response.response_metadata["prompt_eval_duration"]) / 10 ** 9, 3)
    eval_duration = round(int(response.response_metadata["eval_duration"]) / 10 ** 9, 3)

    prompt_eval_count = response.response_metadata["prompt_eval_count"]
    eval_count = response.response_metadata["eval_count"]

    processing_speed = round(prompt_eval_duration / prompt_eval_count, 3)
    generating_speed = round(eval_duration / eval_count, 3)

    print(f"total duratins: {total_duration} seconds")
    print(f"processing speed: {processing_speed} tokens per second")
    print(f"generating speed: {generating_speed} tokens per second")

    print()

chat(model="llama3.2:3b", temperature=0, content="What is SAP BW/4HANA? Explain in two sentences.")
