from nltk.tokenize import sent_tokenize


class TextChunker:
    def __init__(self, max_chars=500):
        self.max_chars = max_chars

    def chunk_text(self, text):
        sentences = sent_tokenize(text)

        chunks = []
        current_chunk = ""

        for sentence in sentences:

            if len(current_chunk) + len(sentence) + 1 <= self.max_chars:
                current_chunk += " " + sentence

            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())

                current_chunk = sentence

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks