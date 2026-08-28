from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field


# class Movie(BaseModel):
#     title: str = Field(description="Name of the movie")
#     genre: str = Field(description="Primary genre of the movie")
#     rating: float = Field(description="Rating from 0 to 10")


class Movie(BaseModel):
    title: str
    genre: str
    rating: float = Field(ge=0, le=10)
    director: str


def extract_movie(
    model_name,
    temperature,
    text
):
    model = ChatOllama(
        model = model_name,
        temperature = temperature
    )

    structured_model = model.with_structured_output(
        Movie
    )

    response = structured_model.invoke(
        text
    )

    print("Type:", type(response))
    print("Response:", response)
    print(response.model_dump())

    # print("\nTitle:", response.title)
    # print("Genre:", response.genre)
    # print("Rating:", response.rating)
    # print(response.director)


extract_movie(
    model_name="llama3.2:3b",
    temperature=0,
    text=(
        "Interstellar is a science fiction movie "
        "directed by Christopher Nolan. "
        "I'd give it a 9 out of 10."
    )
    # text=(
    #     "The Dark Knight, directed by Christopher Nolan, "
    #     "is a superhero crime drama. "
    #     # "It is a great movie. Love it."
    #     "I would rate it 9.5 out of 10."
    # )
    # text = "Interstellar is a great movie."
)
