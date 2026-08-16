# 01 — Basic Chat Model

A small LangChain experiment to understand how to use an Ollama chat model with LangChain and inspect model response metadata.

## Concepts Covered

- `ChatOllama`
- `HumanMessage`
- `invoke()`
- `AIMessage`
- Response content
- Model metadata
- Token usage
- Inference duration
- Prompt processing speed
- Token generation speed

## Flow

```text
User Prompt
    ↓
HumanMessage
    ↓
ChatOllama
    ↓
model.invoke()
    ↓
AIMessage
    ├── content
    ├── response_metadata
    └── usage_metadata
```

## Code

```python
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage


def chat(model, temperature, content):
    model = ChatOllama(
        model = model,
        temperature = temperature
    )

    messages = [
        HumanMessage(
            content = content
        )
    ]

    response = model.invoke(messages)

    print(response.content)
    print()

    print(response.response_metadata)
    print(response.usage_metadata)
    print()

chat(
    model = "llama3.2:3b",
    temperature = 0,
    content = "What is SAP BW/4HANA? Explain in two sentences."
)
```


# 02 — PromptTemplate

A small LangChain experiment to understand how to create reusable prompt templates, pass dynamic inputs into them, and use the formatted prompt with an Ollama chat model.

## Concepts Covered

- `PromptTemplate`
- Template variables
- `PromptTemplate.from_template()`
- `prompt.invoke()`
- Dynamic prompt inputs
- Formatted prompts
- `ChatOllama`
- `model.invoke()`
- `AIMessage`
- Separating prompt construction from model execution

## Flow

```text
Topic
Audience
Sentences
    ↓
PromptTemplate
    ↓
prompt.invoke()
    ↓
Formatted Prompt
    ↓
ChatOllama
    ↓
model.invoke()
    ↓
AIMessage
    ↓
Response Content
```

## Code

```python
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

    print(formatted_prompt)
    print()

    response = model.invoke(formatted_prompt)

    print(response.content)
    print()

chat(
    model = "llama3.2:3b",
    temperature = 0,
    topic = "Retrieval Augmented Generation",
    audience = "beginner",
    sentences = 4
)
```


03_chat_prompt
04_lcel
05_runnables
06_structured_output
07_output_parser
08_streaming
09_memory
10_embeddings
11_vector_store
12_retriever
13_simple_rag
14_tools
15_tool_calling
16_agent
