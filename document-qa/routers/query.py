from fastapi import APIRouter
from pydantic import BaseModel

from utils.embeddings import get_query_embedding
from utils.vector_store import search
from utils.llm import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(request: QueryRequest):
    query_embedding = get_query_embedding(request.question)
    relevant_chunks = search(query_embedding, top_k=5 )

    if not relevant_chunks:
        return {"answer": "No document has been uploaded yet."}

    answer = generate_answer(request.question, relevant_chunks)

    return {
        "question": request.question,
        "retrieved_chunks": relevant_chunks,
        "answer": answer
    }