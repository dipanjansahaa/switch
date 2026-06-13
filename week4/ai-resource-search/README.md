# AI Resource Search Engine

A simple semantic search engine built using embeddings and FAISS.

## Overview

This project allows users to search through documents using semantic similarity instead of traditional keyword matching.

The system:

1. Loads documents
2. Splits them into chunks
3. Generates embeddings
4. Stores embeddings in a FAISS index
5. Retrieves the most relevant chunks for a query

---

## Project Structure

```text
ai-resource-search/

├── data/
│   ├── docs/
│   ├── chunks.json
│   ├── embeddings.npy
│   └── faiss.index
│
├── src/
│   ├── ingest.py
│   ├── chunk.py
│   ├── embed.py
│   ├── indexer.py
│   └── search.py
│
├── app.py
├── build_index.py
├── search_app.py
├── requirements.txt
└── README.md
```

---

## How It Works

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
FAISS Index
    ↓
Semantic Search
```

When a user enters a query:

```text
Query
    ↓
Embedding
    ↓
FAISS Search
    ↓
Top-K Relevant Chunks
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Build the Index

Run:

```bash
python build_index.py
```

This will:

- Load documents
- Create chunks
- Generate embeddings
- Build a FAISS index

Generated files:

- `chunks.json`
- `embeddings.npy`
- `faiss.index`

---

## Search

Run:

```bash
python search_app.py
```

Example:

```text
Search: what is retrieval augmented generation
```

The application will return the most relevant document chunks.

---

## Technologies Used

- Python
- Sentence Transformers
- FAISS
- NumPy
- NLTK
- PyPDF

---

## Current Scope

This project focuses only on:

- Chunking
- Embeddings
- Vector Search
- Semantic Retrieval

No LLM is used yet.

The retrieval component will later be used as the foundation for a RAG system.