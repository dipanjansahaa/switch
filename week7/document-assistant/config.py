# Embedding Model
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# Reranker Model
RERANKER_MODEL = "BAAI/bge-reranker-base"

# LLM
LLM_MODEL = "llama3.2:3b"

# Chunking
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# Retrieval Strategy
# RETRIEVAL_TYPE = "similarity"
# RETRIEVAL_TYPE = "threshold"
# RETRIEVAL_TYPE = "hybrid"
RETRIEVAL_TYPE = "reranker"

# Options:
# "similarity"
# "threshold"
# "hybrid"
# "reranker"
# "mmr"

TOP_K = 5

SCORE_THRESHOLD = 0.70

# Paths
DATA_PATH = "data/docs"

VECTOR_STORE_PATH = "data/vector_store"

CHUNK_JSON_PATH = f"{VECTOR_STORE_PATH}/chunks.json"

INDEX_PATH = f"{VECTOR_STORE_PATH}/faiss.index"

CHUNK_PATH = f"{VECTOR_STORE_PATH}/chunks.pkl"