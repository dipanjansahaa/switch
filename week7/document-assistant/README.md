# Week 7 - Advanced RAG Enhancements

## Objective

In Week 7, the goal was to improve the retrieval quality and context provided to the LLM without changing the underlying embedding model or vector database. Instead of simply retrieving the most similar chunks, the RAG pipeline was enhanced with multiple retrieval strategies, query expansion, and parent document retrieval.

---

# Features Implemented

- Multiple Retrieval Strategies
- Similarity Search
- Threshold Search
- Max Marginal Relevance (MMR)
- Query Expansion
- Parent Document Retrieval
- Configurable Retrieval Pipeline

---

# Project Structure

```
week7-rag-document-assistant/

src/
│
├── ingest.py
├── chunk.py
├── embed.py
├── indexer.py
├── retriever.py
├── prompt.py
├── query_expander.py
├── llm.py
└── rag.py

config.py
build_index.py
search_app.py
```

---

# 1. Multiple Retrieval Strategies

Previously, the retriever always performed a simple similarity search.

The retriever was redesigned to support multiple retrieval strategies through a single interface.

```python
retrieve(
    query,
    strategy,
    k,
    threshold
)
```

Currently supported strategies:

- Similarity Search
- Threshold Search
- Max Marginal Relevance (MMR)

The active strategy is controlled from `config.py`.

```python
RETRIEVAL_TYPE = "similarity"

# Options:
# similarity
# threshold
# mmr
```

---

# 2. Similarity Search

The default retrieval strategy.

Pipeline:

```
Query

↓

Embedding

↓

FAISS Similarity Search

↓

Top-K Chunks
```

Returns the K most similar chunks based on cosine similarity.

Advantages:

- Fast
- Simple
- Good baseline

Limitations:

- May return redundant chunks.
- May include low-confidence results.

---

# 3. Threshold Search

Threshold Search improves retrieval by filtering out chunks with low similarity scores.

Example:

Similarity Search:

```
0.93

0.90

0.84

0.46

0.29
```

Threshold Search (0.70):

```
0.93

0.90

0.84
```

Low-confidence chunks are discarded before prompting the LLM.

Benefits:

- Cleaner context
- Less irrelevant information
- Shorter prompts
- More accurate answers

Threshold value is configurable.

```python
SCORE_THRESHOLD = 0.70
```

---

# 4. Max Marginal Relevance (MMR)

MMR reduces redundant context by selecting chunks that are both:

- Relevant to the query
- Different from each other

Instead of retrieving:

```
Definition

Definition

Definition

Definition
```

MMR retrieves:

```
Definition

Pipeline

Advantages

Challenges

Applications
```

Benefits:

- Better context diversity
- Reduced duplication
- Improved answer completeness

---

# 5. Query Expansion

Users often ask very short or ambiguous questions.

Example:

```
RAG
```

Instead of directly retrieving using the original query, the query is rewritten by the LLM.

Example:

Original Query

```
RAG
```

Expanded Query

```
Explain Retrieval-Augmented Generation (RAG), including its purpose,
pipeline, retrieval process and generation stage.
```

Pipeline:

```
User Question

↓

Query Expander

↓

Expanded Query

↓

Retriever

↓

LLM
```

A new module was added:

```
query_expander.py
```

The Query Expander uses the existing LLM to rewrite user queries for better semantic retrieval.

Query expansion can be enabled or disabled from `config.py`.

```python
ENABLE_QUERY_EXPANSION = True
```

Benefits:

- Better semantic retrieval
- Improved recall
- Better handling of abbreviations
- More informative search queries

---

# 6. Parent Document Retrieval

Traditional RAG retrieves only small chunks.

Example:

```
Chunk 18

Embedding creation...

Vector database...
```

Sometimes the retrieved chunk lacks sufficient context.

Parent Document Retrieval solves this by embedding small chunks but supplying the larger parent document to the LLM.

Current implementation uses the PDF page as the parent document.

Each chunk now stores:

```python
{
    "filename": "...",
    "page": 3,
    "chunk_id": 8,
    "parent_id": 3,
    "parent_content": "...entire page...",
    "text": "...small chunk..."
}
```

Pipeline:

```
Document

↓

Page (Parent)

↓

Small Chunks

↓

Embeddings

↓

Retriever

↓

Parent Page

↓

LLM
```

Benefits:

- Richer context
- More complete answers
- Better explanation quality

---

# 7. Parent Context Deduplication

Multiple retrieved chunks often belong to the same parent page.

Without deduplication:

```
Page 4

Page 4

Page 4
```

The prompt wastes context by repeating the same page multiple times.

A deduplication step was added before prompt generation.

Duplicate parent pages are removed using their:

- filename
- parent_id

Only one copy of each parent document is included in the prompt.

Benefits:

- Smaller prompts
- Reduced token usage
- No repeated context

---

# 8. Configurable Prompt Context

Prompt generation now supports two modes.

Child Chunk Mode

```
Chunk

↓

Prompt
```

Parent Context Mode

```
Parent Page

↓

Prompt
```

Controlled from:

```python
USE_PARENT_CONTEXT = True
```

When enabled, the prompt is built using the parent document instead of individual chunks.

---

# Overall Retrieval Pipeline

```
                User Question
                      │
                      ▼
             Query Expansion
                      │
                      ▼
               Expanded Query
                      │
                      ▼
         Retrieval Strategy Selection
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Similarity      Threshold          MMR
      │               │                │
      └───────────────┴────────────────┘
                      │
                      ▼
           Retrieved Child Chunks
                      │
                      ▼
        Parent Document Selection
                      │
                      ▼
        Parent Context Deduplication
                      │
                      ▼
            Prompt Construction
                      │
                      ▼
                  LLM Answer
```

---

# Configuration Options

```python
RETRIEVAL_TYPE = "mmr"

TOP_K = 5

SCORE_THRESHOLD = 0.70

ENABLE_QUERY_EXPANSION = True

USE_PARENT_CONTEXT = True
```

---

# Learning Outcomes

After completing Week 7, the RAG system supports:

- Multiple retrieval strategies
- Configurable retrieval pipeline
- Similarity Search
- Threshold Search
- Max Marginal Relevance (MMR)
- Query Expansion
- Parent Document Retrieval
- Parent context deduplication
- Configurable prompt context

These enhancements significantly improve retrieval quality, reduce redundant information, provide richer context to the LLM, and make the RAG pipeline more modular and closer to production-ready systems.