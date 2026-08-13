from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_FOLDER = BASE_DIR / "data" / "uploads"
CHROMA_DB = BASE_DIR / "data" / "chroma_db"

MODEL_NAME = os.getenv("MODEL_NAME", "llama3.1")

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
CHROMA_DB.mkdir(parents=True, exist_ok=True)