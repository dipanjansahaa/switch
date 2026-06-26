class PromptBuilder:

    @staticmethod
    def build_prompt(context_chunks, question):

        context = "\n\n".join(
            chunk["text"] for chunk in context_chunks
        )

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
reply with:

"I couldn't find the answer in the provided documents."

Context:
-------------------------
{context}
-------------------------

Question:
{question}

Answer:
"""

        return prompt