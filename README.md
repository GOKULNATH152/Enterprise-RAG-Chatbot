# Enterprise RAG Chatbot

An end-to-end Enterprise Retrieval-Augmented Generation (RAG) chatbot built using FastAPI, LangChain, ChromaDB, Ollama, and Llama 3.1.

The application allows users to upload PDF documents and ask natural-language questions. Relevant document chunks are retrieved from the vector database and provided as context to the LLM to generate grounded responses.

---

## 🚀 Project Overview

Enterprise organizations often store large amounts of information in PDFs, manuals, policies, reports, and technical documents.

Finding relevant information manually can be time-consuming.

This project provides an AI-powered document question-answering system that:

1. Accepts PDF documents.
2. Extracts text from the documents.
3. Splits the text into smaller chunks.
4. Generates vector embeddings.
5. Stores embeddings in ChromaDB.
6. Retrieves relevant document chunks for a user question.
7. Sends the retrieved context to Llama 3.1.
8. Generates a context-aware answer.

---

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     FastAPI      │
                    │      API        │
                    └────────┬─────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
     ┌─────────────────┐          ┌─────────────────┐
     │   PDF Upload    │          │  Ask Question   │
     └────────┬────────┘          └────────┬────────┘
              │                            │
              ▼                            │
     ┌─────────────────┐                   │
     │    PDF Loader   │                   │
     └────────┬────────┘                   │
              │                            │
              ▼                            │
     ┌─────────────────┐                   │
     │  Text Splitter  │                   │
     └────────┬────────┘                   │
              │                            │
              ▼                            │
     ┌─────────────────┐                   │
     │    Embeddings   │                   │
     │ nomic-embed-text│                   │
     └────────┬────────┘                   │
              │                            │
              ▼                            │
     ┌─────────────────┐                   │
     │    ChromaDB     │◄──────────────────┘
     │  Vector Store   │
     └────────┬────────┘
              │
              ▼
     ┌─────────────────┐
     │    Retriever    │
     └────────┬────────┘
              │
              ▼
     ┌─────────────────┐
     │    Llama 3.1    │
     │     Ollama      │
     └────────┬────────┘
              │
              ▼
     ┌─────────────────┐
     │  Final Answer   │
     └─────────────────┘
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| FastAPI | Backend REST API |
| LangChain | RAG orchestration |
| ChromaDB | Vector database |
| Ollama | Local LLM runtime |
| Llama 3.1 | Text generation |
| nomic-embed-text | Text embeddings |
| PyPDF | PDF text extraction |
| Uvicorn | ASGI server |

---

## 📂 Project Structure

```text
enterprise-rag-chatbot/
│
├── app/
│   ├── api/
│   │   ├── chat.py
│   │   └── upload.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   │
│   ├── llm/
│   │   └── ollama.py
│   │
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── loader.py
│   │   ├── retriever.py
│   │   ├── splitter.py
│   │   └── vector_store.py
│   │
│   └── main.py
│
├── data/
│   └── chroma_db/
│
├── uploads/
│
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/enterprise-rag-chatbot.git
```

```bash
cd enterprise-rag-chatbot
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Install Ollama

Install Ollama on your local machine.

After installation, download the required models:

```bash
ollama pull llama3.1
```

```bash
ollama pull nomic-embed-text
```

Start Ollama:

```bash
ollama serve
```

The default Ollama API is:

```text
http://localhost:11434
```

---

# ▶️ Run the Application

Start FastAPI:

```bash
python -m uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically provides Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 📄 Upload PDF

Endpoint:

```text
POST /api/upload
```

Upload a PDF document through Swagger UI.

Example successful response:

```json
{
    "message": "PDF uploaded and indexed successfully",
    "filename": "sample.pdf",
    "characters": 19999,
    "chunks": 25
}
```

---

# 💬 Ask a Question

Endpoint:

```text
POST /api/ask
```

Example request:

```json
{
    "question": "What is this document about?"
}
```

Example response:

```json
{
    "question": "What is this document about?",
    "answer": "The document discusses...",
    "sources": [
        "Relevant document content..."
    ]
}
```

---

# 🔄 RAG Pipeline

The application follows the following pipeline:

```text
PDF
 │
 ▼
PDF Loader
 │
 ▼
Text Extraction
 │
 ▼
Text Splitting
 │
 ▼
Embedding Generation
 │
 ▼
ChromaDB
 │
 ▼
Similarity Search
 │
 ▼
Relevant Context
 │
 ▼
Llama 3.1
 │
 ▼
Final Answer
```

---

# 🔍 How Retrieval Works

When a user asks a question:

```text
User Question
      │
      ▼
Embedding Model
      │
      ▼
Vector Representation
      │
      ▼
ChromaDB Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Prompt + Context
      │
      ▼
Llama 3.1
      │
      ▼
Generated Answer
```

---

# 🔐 Large Model Files

The following files are intentionally NOT included in this GitHub repository:

- Llama 3.1 model files
- nomic-embed-text model files
- ChromaDB generated database
- Uploaded PDF documents

These files can be downloaded/generated locally using Ollama and the application setup instructions.

This keeps the repository lightweight and avoids storing multi-gigabyte model files in Git.

---

# 📸 Screenshots

## Swagger API

Add your Swagger screenshot here:

```text
screenshots/01_swagger.png
```

## PDF Upload

Add your upload screenshot here:

```text
screenshots/02_upload_success.png
```

## Question Answering

Add your question-answer screenshot here:

```text
screenshots/03_question_answer.png
```

---

# 🎥 Demo

Add your project demonstration video link here.

Example:

```text
Demo Video:
[Add YouTube / LinkedIn / Portfolio video link]
```

The demo should show:

1. Starting the application
2. Opening Swagger
3. Uploading a PDF
4. Indexing the document
5. Asking questions
6. Receiving AI-generated answers

---

# 🧪 Testing

The application can be tested through FastAPI Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
GET /health
```

Expected response:

```json
{
    "status": "Healthy"
}
```

---

# 🚀 Future Enhancements

- Multi-document support
- Conversation memory
- Source/page citations
- React frontend
- User authentication
- Streaming responses
- RAG evaluation
- Reranking
- Hybrid search
- Docker deployment
- Kubernetes deployment
- CI/CD pipeline
- Monitoring and logging

---

# 💼 Skills Demonstrated

This project demonstrates practical experience with:

- Generative AI
- Large Language Models
- Retrieval-Augmented Generation
- Vector Databases
- Semantic Search
- Embeddings
- Prompt Engineering
- FastAPI
- REST APIs
- LangChain
- ChromaDB
- Ollama
- Python
- AI application architecture

---

# 👨‍💻 Author

## Gokulnath N

Machine Learning & Computer Vision Engineer

Interested in:

- Computer Vision
- Generative AI
- LLMs
- RAG
- MLOps
- AI Engineering

---

# 📄 License

This project is licensed under the MIT License.