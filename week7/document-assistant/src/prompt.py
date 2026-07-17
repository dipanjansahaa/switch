import config

class PromptBuilder:

    @staticmethod
    def build_prompt(context_chunks, question):

        context = ""

        unique_chunks = []

        seen = set()

        for chunk in context_chunks:

            if config.USE_PARENT_CONTEXT:

                parent = (
                    chunk["filename"],
                    chunk["parent_id"]
                )

                if parent in seen:
                    continue

                seen.add(parent)

            unique_chunks.append(chunk)

        for chunk in unique_chunks:

            if config.USE_PARENT_CONTEXT:

                context += (
                    f"Source: {chunk['filename']} "
                    f"(Page {chunk['page']})\n\n"
                    f"{chunk['parent_content']}\n\n"
                    "----------------------------------\n\n"
                )

            else:

                context += (
                    f"Source: {chunk['filename']} "
                    f"(Page {chunk['page']})\n\n"
                    f"{chunk['text']}\n\n"
                    "----------------------------------\n\n"
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