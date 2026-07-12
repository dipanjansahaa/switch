class QueryExpander:

    def __init__(self, llm):
        self.llm = llm

    def expand(self, query):

        prompt = f"""
You are a search query optimization assistant.

Rewrite the user's query so it is better suited for semantic retrieval from a vector database.

Rules:
- Preserve the original intent.
- Expand abbreviations if applicable.
- Include important technical terms.
- Do NOT answer the question.
- Return ONLY the rewritten query.

User Query:
{query}

Keep in mind:
- Try to form it as a question.
"""

        expanded_query = self.llm.generate(prompt)

        return expanded_query.strip()