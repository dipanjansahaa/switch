# Embedding Model
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# LLM
LLM_MODEL = "llama3.2:3b"

# Chunking
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# Retrieval
TOP_K = 5

# Paths
DATA_PATH = "data/docs"

VECTOR_STORE_PATH = "data/vector_store"

CHUNK_JSON_PATH = f"{VECTOR_STORE_PATH}/chunks.json"

INDEX_PATH = f"{VECTOR_STORE_PATH}/faiss.index"

CHUNK_PATH = f"{VECTOR_STORE_PATH}/chunks.pkl"