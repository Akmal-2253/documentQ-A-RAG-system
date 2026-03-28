# DocumentQA — RAG-based PDF Question Answering System

An AI-powered application that lets you upload any PDF and ask questions about its content using Retrieval-Augmented Generation (RAG).

---

## How It Works

```
PDF Upload → Extract Text → Chunk → Embed → Store in FAISS
                                                   ↓
Answer ← LLM Generation ← Top-K Chunks ← Semantic Search ← User Question
```

---

## Features

- Upload any PDF and index it instantly
- Ask natural language questions about the document
- Semantic search using vector embeddings
- LLM-generated accurate, context-aware answers
- REST API built with FastAPI

---

## Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Backend REST API |
| OpenAI Embeddings | Text → Vector conversion |
| FAISS | Vector similarity search |
| PyPDF | PDF text extraction |
| Python | Core language |

---

## Project Structure

```
document-qa/
├── routers/
│   ├── upload.py       # PDF upload & indexing
│   └── query.py        # Question answering
├── utils/
│   ├── pdf_parser.py   # PDF text extraction
│   ├── chunking.py     # Text chunking
│   ├── embeddings.py   # Embedding generation
│   ├── vector_store.py # FAISS index management
│   └── llm.py          # LLM answer generation
├── main.py
├── rag_ui.html
└── requirements.txt
```

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Akmal-2253/documentQA-A-RAG-system.git
cd documentQA-A-RAG-system/document-qa
```

### 2. Create virtual environment
```bash
python -m venv myenv
myenv\Scripts\activate      # Windows
source myenv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the application
```bash
uvicorn main:app --reload
```

---

## API Endpoints

### Upload a PDF
```
POST /upload
Content-Type: multipart/form-data
Body: file = your_document.pdf
```

### Ask a Question
```
POST /ask
Content-Type: application/json
Body: { "question": "What is this document about?" }
```

### Response
```json
{
  "question": "What is this document about?",
  "retrieved_chunks": ["...relevant text..."],
  "answer": "This document is about..."
}
```

---

## Environment Variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key |

---

## Author

**Akmal Sultan**
GitHub: [@Akmal-2253](https://github.com/Akmal-2253)
