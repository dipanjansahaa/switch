from pypdf import PdfReader
from ollama import chat
import json

reader = PdfReader("CV.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

# print(text)
# print(type(text))                               # string

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

# print(prompt)
# print(type(prompt))                             # string

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

# print(response)
# print(type(response))                           # not a string

# print(response.message)
# print(type(response.message))                   # not a string

# print(response.message.content)
# print(type(response.message.content))           # stirng

summary = response.message.content
data = json.loads(summary)

print(data)
# print(type(data))                               # dict

# print(data["name"])
# print(type(data["name"]))                       # string

# print(data["skills"])
# print(type(data["skills"]))                     # list

data2 = json.dumps(data, indent=4)

# print(data2)
# print(type(data2))                              # string

with open(
    "data.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        data,
        f,
        indent=4,
        ensure_ascii=False
    )

with open(
    "data.json", 
    "r", 
    encoding="utf-8"
) as f:
    data3 = json.load(f)

print(data3)
print(type(data3))
