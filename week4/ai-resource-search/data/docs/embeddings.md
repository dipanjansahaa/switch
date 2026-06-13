# Vector Embeddings Documentation

This document details how our project handles **vector embeddings** for semantic search, document chunking, and similarity retrieval.

---

## 🛠️ Embedding Pipeline Overview

We transform raw unstructured data into high-dimensional numerical vectors to facilitate fast mathematical similarity searches.

1. **Data Ingestion**: Collect text files, Markdown documentation, or API content.
2. **Text Chunking**: Split text into small, context-aware segments using structural boundaries.
3. **Vector Generation**: Pass text chunks through an embedding model to extract numerical vectors.
4. **Database Storage**: Save the vectors alongside original text metadata inside our vector store.

---

## 🤖 Supported Embedding Models

Depending on your environment (Local vs. Cloud), you can configure one of the following models:

### 1. Cloud-Based: OpenAI
* **Default Model**: `text-embedding-3-small` or `text-embedding-3-large`
* **Dimensions**: 1536 or 3072
* **Best For**: High performance, zero local hardware requirements, and large production scale.

### 2. Local/Open-Source: Hugging Face
* **Default Model**: `sentence-transformers/all-MiniLM-L6-v2`
* **Dimensions**: 384
* **Best For**: Free local development, data privacy, and completely offline execution.

---

## 📐 Chunking Strategy

To maintain maximum semantic accuracy, text must be divided before it is sent to the embedding model:

* **Strategy**: `RecursiveCharacterTextSplitter`
* **Chunk Size**: `500` characters (ideal balance for capturing context phrases).
* **Chunk Overlap**: `50` characters (prevents loss of data at chunk boundaries).

---

## 💻 Code Quickstart (Python)

Ensure you have your environment variables set up in a `.env` file:
```env
OPENAI_API_KEY=your_api_key_here
```

### Installation
```bash
pip install openai sentence-transformers numpy
```

### Generating an Embedding
```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_embedding(text: str, model="text-embedding-3-small"):
    # Clean string input
    text = text.replace("\n", " ")
    
    # Request vector from API
    response = client.embeddings.create(
        input=[text], 
        model=model
    )
    return response.data[0].embedding

# Example run
vector = get_embedding("Vector embeddings power intelligent semantic search.")
print(f"Generated Vector. Total Dimensions: {len(vector)}")
```

---

## 🔍 Similarity Retrieval

We utilize **Cosine Similarity** to compare user queries with our stored embeddings:

$$\text{Cosine Similarity} = \frac{A \cdot B}{\|A\| \|B\|}$$

Results are ranked from `1.0` (identical context) to `-1.0` (opposite context). A score threshold of `0.75+` is typically required to consider a document relevant for RAG synthesis.

---

## 🛡️ Best Practices & Optimization

* **Handle Rate Limits**: Always implement exponential backoff retry logic for cloud APIs to avoid 429 errors.
* **Keep Text Clean**: Remove excessive whitespaces, HTML/Markdown boilerplate, and broken characters prior to chunking.
* **Idempotent Upserts**: Ensure your pipeline tracks document IDs. Only generate new embeddings if the source file's cryptographic hash has changed.
