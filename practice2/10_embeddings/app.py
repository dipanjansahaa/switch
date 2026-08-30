# embeddings, vector dimensions
from langchain_ollama import OllamaEmbeddings


def generate_embedding(
    model_name,
    text
):
    embeddings = OllamaEmbeddings(
        model = model_name
    )

    vector = embeddings.embed_query(text)

    texts = [
        "I love programming in Python.",
        "Python is my favorite programming language.",
        "I went to Hyderabad yesterday."
    ]

    for text in texts:
        vector = embeddings.embed_query(text)

        print(f"{text}")
        print(f"Dimensions: {len(vector)}")
        print()

    # print("Text:")
    # print(text)

    # # print("\nVector:")
    # # print(vector)

    # print("\nVector dimensions:")
    # print(len(vector))


generate_embedding(
    model_name = "nomic-embed-text",
    text = "I love programming in Python."
    # text = "Hi"
    # text = "Hi."
)

