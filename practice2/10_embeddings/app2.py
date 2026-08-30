# similarity
import numpy as np
from langchain_ollama import OllamaEmbeddings


def generate_similarity(
    model_name,
    text_1,
    text_2
):
    embeddings = OllamaEmbeddings(
        model = model_name
    )

    vector_1 = embeddings.embed_query(text_1)
    vector_2 = embeddings.embed_query(text_2)

    similarity = np.dot(vector_1, vector_2) / (
        np.linalg.norm(vector_1) *
        np.linalg.norm(vector_2)
    )

    print(similarity)


generate_similarity(
    model_name = "nomic-embed-text",
    text_1 = "I love programming in Python.",
    text_2 = "Python is my favorite programming language."
)

generate_similarity(
    model_name = "nomic-embed-text",
    text_1 = "I love programming in Python.",
    text_2 = "I went to Hyderabad yesterday."
)

generate_similarity(
    model_name = "nomic-embed-text",
    text_1 = "Python is my favorite programming language.",
    text_2 = "I went to Hyderabad yesterday."
)

generate_similarity(
    model_name = "nomic-embed-text",
    text_1 = "I went to Hyderabad yesterday.",
    text_2 = "Python is my favorite programming language."
)

generate_similarity(
    model_name = "nomic-embed-text",
    text_1 = "Python is my favorite programming language.",
    text_2 = "Python is my favorite programming language."
)

generate_similarity(
    model_name = "nomic-embed-text",
    text_1 = "Python is my favorite programming language.",
    text_2 = "programming .is language my favorite Python"
)

generate_similarity(
    model_name = "nomic-embed-text",
    text_1 = "I went to Hyderabad yesterday.",
    text_2 = "I went to Kolkata yesterday."
)

generate_similarity(
    model_name = "nomic-embed-text",
    text_1 = "I went to Hyderabad yesterday.",
    text_2 = "I went to Kolkata today."
)

generate_similarity(
    model_name = "nomic-embed-text",
    text_1 = "Hi",
    text_2 = "Hi."
)
