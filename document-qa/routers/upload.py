from fastapi import APIRouter, UploadFile, File
import os

from utils.pdf_parser import extract_text_from_pdf
from utils.chunking import chunk_text
from utils.embeddings import get_embeddings
from utils.vector_store import build_index

router = APIRouter()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename or "document")

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)
    build_index(embeddings, chunks)

    return {
        "message": "PDF uploaded and indexed successfully",
        "chunks": len(chunks)
    }