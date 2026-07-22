# Week 7 - Advanced RAG Enhancements

## Objective

In Week 7, the goal was to improve the retrieval quality and context provided to the LLM without changing the underlying embedding model or vector database. Instead of simply retrieving the most similar chunks, the RAG pipeline was enhanced with multiple retrieval strategies, query expansion, and parent document retrieval.

---

# Features Implemented

- Multiple Retrieval Strategies
- Similarity Search
- Threshold Search
- Max Marginal Relevance (MMR)

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
├── langchain_indexer.py
├── langchain_retriever.py
├── llm.py
└── rag.py

config.py
build_index.py
search_app.py
langchainsearch_app.py
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

# Configuration Options

```python
RETRIEVAL_TYPE = "mmr"

TOP_K = 5

SCORE_THRESHOLD = 0.70
```

---

# Learning Outcomes

After completing Week 7, the RAG system supports:

- Multiple retrieval strategies
- Configurable retrieval pipeline
- Similarity Search
- Threshold Search
- Max Marginal Relevance (MMR)

These enhancements significantly improve retrieval quality, reduce redundant information, provide richer context to the LLM, and make the RAG pipeline more modular and closer to production-ready systems.