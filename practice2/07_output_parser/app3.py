# StrOutputParser, JsonOutputParser
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser


def classify_topic(
    model_name,
    temperature,
    topic
):
    model = ChatOllama(
        model = model_name,
        temperature = temperature
    )

    # prompt = ChatPromptTemplate.from_template(
    #     """
    #     Classify the following topic.

    #     Return valid JSON with these keys:
    #     topic
    #     difficulty

    #     Topic: {topic}
    #     """
    # )

    prompt = ChatPromptTemplate.from_template(
        """
        Return ONLY valid JSON.
        Do not include any explanation, markdown, code fences, or extra text.

        The JSON must contain exactly these two keys:
        "topic"
        "difficulty"

        The difficulty can vary in between Begineer, Mid, Pro, Expert.

        if there are multiple topics, do the same thing for all the topics.

        Example:
        {{
            "topic": "Math",
            "difficulty": "Expert"
        }}

        Topic: {topic}
        """
    )

    parser1 = StrOutputParser()

    parser2 = JsonOutputParser()

    chain1 = prompt | model | parser1

    chain2 = prompt | model | parser2

    chain3 = prompt | model

    result1 = chain1.invoke({
        "topic": topic
    })

    print(result1)
    print(type(result1))

    print()

    result2 = chain2.invoke({
        "topic": topic
    })

    print(result2)
    print(type(result2))

    print()

    result3 = chain3.invoke({
        "topic": topic
    })

    print(result3.content)
    print(type(result3.content))


classify_topic(
    model_name = "llama3.2:3b",
    temperature = 0,
    topic = "LangChain, RAG, LLM"
)
