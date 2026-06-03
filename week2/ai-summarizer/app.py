from dotenv import load_dotenv
# from openai import OpenAI
from ollama import chat
import os

load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

# print(api_key[:10])

# client = OpenAI(api_key=api_key)

text = input("Enter text: ")

# print(text)

length = input("Choose length (short/medium/long): ")

style = input("Choose style (bullet/paragraph): ")

prompt = f"""
Summarize the following text.

Requirements:
- Length: {length}
- Style: {style}

If style is bullet:
Use bullet points only.

If style is paragraph:
Use a paragraph only.

Do not add information that is not present in the text.

Text:
{text}
"""

# print(prompt)

# response = client.responses.create(
#     model="gpt-4.1-mini",
#     input=prompt
# )

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

print(summary)