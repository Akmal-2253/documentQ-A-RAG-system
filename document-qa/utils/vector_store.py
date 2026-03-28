import faiss # type: ignore  # Facebook AI Similarity Search, a library stores all those number-lists (vectors) and lets you search through millions of them extremely fast.(VECTORS DATABASE)
# It stores all the chunk embeddings and required answers.

import numpy as np

# Global variables
index = None
stored_chunks = []

def build_index(embeddings, chunks: list[str]):
    global index, stored_chunks
    
    dimension = embeddings.shape[1]  # 384
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings, dtype='float32')) # type: ignore
    stored_chunks = chunks

def search(query_embedding, top_k: int = 3):
    query = np.array([query_embedding], dtype='float32')
    distances, indices = index.search(query, top_k) # type: ignore
    
    results = [stored_chunks[i] for i in indices[0]]
    return results