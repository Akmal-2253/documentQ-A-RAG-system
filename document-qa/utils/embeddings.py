from sentence_transformers import SentenceTransformer # type: ignore
#This converts each chunk into numerical vectors.
#That numeric representation helps us compare meanings.

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text_chunks: list[str]):
    return model.encode(text_chunks)

def get_query_embedding(query: str):
    return model.encode(query)