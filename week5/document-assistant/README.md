# Week 5 - Basic RAG (Retrieval-Augmented Generation)

## Overview

This project implements a **Basic Retrieval-Augmented Generation (RAG)** pipeline from scratch to understand how modern LLM-powered applications retrieve external knowledge before generating responses.

Instead of relying on pre-built RAG chains, each component of the pipeline is implemented separately to understand the complete workflow.

---

## Features

- Load PDF, TXT and Markdown documents
- Custom text chunking with configurable chunk size and overlap
- Generate embeddings using Sentence Transformers
- Store embeddings in a FAISS vector database
- Perform semantic similarity search
- Retrieve Top-K relevant chunks
- Build prompts using retrieved context
- Generate answers using an LLM (Ollama)
- Display source documents, chunk IDs, and similarity scores
- Save and reload the FAISS index without recomputing embeddings

---

## Project Structure

```
week5-rag-document-assistant/
│
├── data/
│   ├── docs/
│   └── vector_store/
│       ├── faiss.index
│       └── chunks.pkl
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
├── build_index.py
├── search_app.py
├── requirements.txt
└── README.md
```

---

## RAG Pipeline

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
Embeddings
    │
    ▼
FAISS Vector Store
    │
    ▼
Retriever (Top-K Search)
    │
    ▼
Prompt Builder
    │
    ▼
LLM
    │
    ▼
Generated Answer
```

---

## Components

### Document Loader
Loads PDF, TXT and Markdown documents from the `data/docs` directory.

### Text Chunker
Splits documents into smaller overlapping chunks to improve retrieval quality.

### Embedding Generator
Converts document chunks into dense vector embeddings using a Sentence Transformer model.

### Vector Indexer
Creates and saves a FAISS index for efficient similarity search.

### Retriever
Embeds the user query, searches the FAISS index, and retrieves the Top-K most relevant chunks.

### Prompt Builder
Constructs a prompt by combining retrieved context with the user's question.

### LLM
Generates the final response using the retrieved context.

---

## Technologies Used

- Python
- FAISS
- Sentence Transformers
- Ollama
- NumPy
- PyPDF

---

## Embedding Model

```
BAAI/bge-small-en-v1.5
```

This retrieval-optimized embedding model provided significantly better search quality than the default `all-MiniLM-L6-v2`.

---

## Retrieval Settings

| Parameter | Value |
|-----------|------:|
| Chunk Size | 800 |
| Chunk Overlap | 150 |
| Top-K Retrieval | 5 |

---

## Running the Project

### 1. Build the Vector Store

```bash
python build_index.py
```

This will:

- Load documents
- Create chunks
- Generate embeddings
- Build the FAISS index
- Save the vector store

---

### 2. Start the RAG Assistant

```bash
python search_app.py
```

Ask questions about the uploaded documents.

Example:

```
You: What is RAG?

Assistant:
RAG stands for Retrieval-Augmented Generation.

Sources:
- rag_doc.pdf | Chunk 23 | Similarity: 0.9182
- langchain-rag.pdf | Chunk 0 | Similarity: 0.9045
```

---

## Key Concepts Learned

- Retrieval-Augmented Generation (RAG)
- Document ingestion
- Text chunking
- Chunk overlap
- Embeddings
- Semantic similarity
- Vector databases
- FAISS indexing
- Top-K retrieval
- Prompt construction
- Context injection
- LLM-based answer generation

---

## Future Improvements

- RecursiveCharacterTextSplitter
- Hybrid Search (BM25 + Vector Search)
- Cross-Encoder Reranking
- Metadata Filtering
- Streaming Responses
- Chat Memory
- Web Interface
- Evaluation Metrics

---

## Learning Outcome

This project demonstrates the complete implementation of a basic RAG pipeline without relying on high-level RAG abstractions, providing a clear understanding of how document retrieval and LLM-based generation work together.