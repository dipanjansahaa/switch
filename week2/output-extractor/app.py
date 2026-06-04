from ollama import chat
import json

with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

prompt = f"""
Extract the following information from the text.

Fields:
- name
- email
- skills
- experience_years
- company

Return ONLY valid JSON.

Text:
{text}

Return ONLY JSON.
Do not explain.
Do not add markdown.
Do not add comments.
Do not add text before or after JSON.
"""

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

summary = response.message.content

# summary = response["message"]["content"]

# print(summary)

# print(response["message"]["content"])

data = json.loads(summary)

# print(data["name"])
# print(data["skills"])

data = json.loads(response.message.content)

with open(
    "outputs/result.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        data,
        f,
        indent=4,
        ensure_ascii=False
    )

print("Output saved to outputs/result.json")