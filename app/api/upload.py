from pathlib import Path
import shutil
from app.rag.splitter import TextSplitter
from app.rag.vector_store import VectorStore

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.core.config import UPLOAD_FOLDER
from app.rag.loader import PDFLoader

router = APIRouter(
    prefix="/api",
    tags=["Upload"]
)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    destination = Path(UPLOAD_FOLDER) / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    extracted_text = PDFLoader.load_pdf(str(destination))

    # Split into chunks
    chunks = TextSplitter.split_text(extracted_text)

    # Store in ChromaDB
    store = VectorStore()
    store.add_documents(chunks)

    return {
        "message": "PDF uploaded and indexed successfully",
        "filename": file.filename,
        "characters": len(extracted_text),
        "chunks": len(chunks)
    }