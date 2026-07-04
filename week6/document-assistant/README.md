# Week 6 - Improved RAG (Retrieval-Augmented Generation)

## Overview

A production-style **Retrieval-Augmented Generation (RAG)** application built from scratch using Python, FAISS, Sentence Transformers, and a local LLM (Ollama).

The project demonstrates the complete RAG pipeline—from document ingestion to answer generation—without relying on pre-built LangChain RAG chains. Every core component was implemented separately to understand how modern RAG systems work internally.

---

## Features

- Load PDF, TXT, and Markdown documents
- Custom document ingestion pipeline
- Configurable text chunking with overlap
- Generate embeddings using Sentence Transformers
- Store and search vectors using FAISS
- Semantic similarity search
- Retrieval-Augmented Generation (RAG)
- Local LLM inference using Ollama
- Source attribution with filename, page number, and chunk ID
- Persistent vector database (offline indexing)
- Evaluation framework with category-wise accuracy
- Modular and production-style project structure

---

# Project Architecture

```
                Documents
                     │
                     ▼
            Document Loader
                     │
                     ▼
              Text Chunking
                     │
                     ▼
          Embedding Generation
                     │
                     ▼
             FAISS Vector Store
                     │
                     ▼
             Semantic Retrieval
                     │
                     ▼
             Prompt Construction
                     │
                     ▼
                 Local LLM
                     │
                     ▼
          Generated Answer + Sources
```

---

# Project Structure

```
week5-rag-document-assistant/

│
├── src/
│   ├── ingest.py
│   ├── chunk.py
│   ├── embed.py
│   ├── indexer.py
│   ├── retriever.py
│   ├── prompt.py
│   ├── llm.py
│   └── rag.py
│
├── data/
│   ├── docs/
│   └── vector_store/
│       ├── faiss.index
│       └── chunks.pkl
│
├── evaluation/
│   └── evaluation.json
│
├── build_index.py
├── search_app.py
├── evaluate.py
├── config.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

### Language

- Python

### Embedding Model

- BAAI/bge-small-en-v1.5

### Vector Database

- FAISS

### LLM

- Ollama
- Llama 3.2

### Libraries

- sentence-transformers
- faiss-cpu
- pypdf
- numpy
- ollama

---

# Workflow

## Step 1 — Document Ingestion

Supported document formats:

- PDF
- TXT
- Markdown

Documents are converted into plain text while preserving metadata.

---

## Step 2 — Text Chunking

Large documents are divided into smaller chunks.

Current configuration:

```
Chunk Size      : 800
Chunk Overlap   : 150
```

Each chunk stores:

- filename
- page number
- chunk id
- chunk text

---

## Step 3 — Embedding Generation

Each chunk is converted into a dense vector using

```
BAAI/bge-small-en-v1.5
```

These embeddings capture semantic meaning instead of keyword matching.

---

## Step 4 — Vector Indexing

Embeddings are stored inside a FAISS vector database.

The project uses cosine similarity by:

- L2 Normalization
- IndexFlatIP

The vector database is saved locally.

```
faiss.index
```

Chunk metadata is stored separately.

```
chunks.pkl
```

---

## Step 5 — Semantic Retrieval

When the user asks a question:

1. Generate query embedding
2. Search FAISS
3. Retrieve Top-K similar chunks
4. Return chunk metadata

---

## Step 6 — Prompt Construction

Retrieved chunks are combined into a prompt.

Example:

```
Context:
----------------
Retrieved Chunk 1

Retrieved Chunk 2

Retrieved Chunk 3
----------------

Question:
What is RAG?

Answer:
```

---

## Step 7 — Answer Generation

The prompt is passed to a local LLM using Ollama.

The model generates a final answer using only the retrieved context.

---

## Step 8 — Source Attribution

Every response includes the document source.

Example:

```
Sources

langchain-rag.pdf
Page 6
Chunk 12

rag_doc.pdf
Page 3
Chunk 8
```

---

# Offline Indexing

Instead of generating embeddings every time the application starts,

the project creates the vector database once.

Run

```bash
python build_index.py
```

Outputs

```
faiss.index
chunks.pkl
```

---

# Querying

Run

```bash
python search_app.py
```

Example

```
You:
What is RAG?

Assistant:
RAG stands for Retrieval-Augmented Generation.

Sources

langchain-rag.pdf
Page 4
Chunk 12
```

---

# Evaluation

The project includes a simple evaluation framework.

Evaluation file

```
evaluation/evaluation.json
```

Each question contains

- Question
- Expected Answer
- Keywords
- Category

Example

```json
{
    "question":"What is RAG?",
    "expected":"...",
    "keywords":[
        "Retrieval-Augmented Generation",
        "retrieval",
        "generation"
    ],
    "category":"RAG"
}
```

Run evaluation

```bash
python evaluate.py
```

Outputs

- Generated Answer
- Matched Keywords
- PASS / FAIL
- Overall Accuracy
- Category-wise Accuracy

---

# Configuration

Project parameters are centralized inside

```
config.py
```

Example

```python
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

TOP_K = 5

LLM_MODEL = "llama3.2:3b"
```

---

# Learning Outcomes

This project helped understand:

- Retrieval-Augmented Generation (RAG)
- Document ingestion
- Text chunking
- Embedding generation
- Vector databases
- Semantic search
- FAISS indexing
- Prompt engineering
- LLM inference
- Source attribution
- Offline indexing
- RAG evaluation
- Modular project design

---

# Future Improvements

- RecursiveCharacterTextSplitter
- Hybrid Search (BM25 + Vector Search)
- Reranking
- Parent Document Retriever
- Multi-Query Retrieval
- Context Compression
- LangChain Retrieval Chains
- Ragas Evaluation
- DeepEval
- Streaming Responses
- Web Interface (Streamlit/FastAPI)

---

# Acknowledgements

This project was built as part of a hands-on learning roadmap for Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and modern AI application development. The focus was on implementing each stage of the RAG pipeline manually to gain a deeper understanding of how production RAG systems work.