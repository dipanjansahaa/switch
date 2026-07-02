import ollama
import config


class LLM:

    def __init__(
        self,
        model = config.LLM_MODEL
    ):
        self.model = model


    def generate(
        self,
        prompt
    ):

        response = ollama.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response["message"]["content"]