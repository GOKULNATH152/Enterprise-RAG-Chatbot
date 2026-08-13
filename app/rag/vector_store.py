from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.rag.embeddings import EmbeddingService


class VectorStore:
    """
    Handles storing and retrieving document chunks using ChromaDB.
    """

    def __init__(self):
        self.embedding = EmbeddingService().embedding

        self.db = Chroma(
            collection_name="enterprise_rag",
            embedding_function=self.embedding,
            persist_directory="./data/chroma_db",
        )

    def add_documents(self, chunks: list[str]):
        """
        Store text chunks in ChromaDB.
        """

        documents = [
            Document(page_content=chunk)
            for chunk in chunks
        ]

        self.db.add_documents(documents)

    def similarity_search(self, query: str, k: int = 3):
        """
        Retrieve the most relevant chunks.
        """

        return self.db.similarity_search(
            query=query,
            k=k
        )