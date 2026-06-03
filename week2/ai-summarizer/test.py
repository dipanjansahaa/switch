from ollama import chat

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Summarize: Machine Learning is a subset of AI."
        }
    ]
)

print(response.message.content)