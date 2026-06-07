from ollama import chat
import json
import sys
from pypdf import PdfReader

filename = sys.argv[1]

reader = PdfReader(filename)

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

prompt = f"""
Extract the following information from the text.

Output must strictly follow:

Fields:
- "name": string,
- "email": string,
- "skills": array,
- "experience_years": integer,
- "current_company": string,
- "projects": array,
- "certificates": array

Return ONLY valid JSON.

Text:
{text}

Return ONLY JSON.
Do not explain.
Do not add markdown.
Do not add comments.
Do not add text before or after JSON.

If information is missing,
use null.
"""

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    format="json"
)

summary = response.message.content

data = json.loads(summary)

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

# print("Output saved to outputs/result.json")

response2 = chat(
    model="qwen2.5-coder:7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    format="json"
)

summary2 = response2.message.content

data2 = json.loads(summary2)

with open(
    "outputs/result2.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        data2,
        f,
        indent=4,
        ensure_ascii=False
    )

print("Output saved to outputs/result.json")