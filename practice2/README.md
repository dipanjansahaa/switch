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
        model=model,
        temperature=temperature
    )

    messages = [
        HumanMessage(
            content=content
        )
    ]

    response = model.invoke(messages)

    print(response.content)

    print()

    print(response.response_metadata)
    print(response.usage_metadata)


chat(
    model="llama3.2:3b",
    temperature=0,
    content="What is SAP BW/4HANA? Explain in two sentences."
)
```
