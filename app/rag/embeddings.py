from langchain_ollama import OllamaEmbeddings


class EmbeddingService:
    """
    Creates embeddings using the local Ollama embedding model.
    """

    def __init__(self):
        self.embedding = OllamaEmbeddings(
            model="nomic-embed-text"
        )

    def create_embeddings(self, chunks: list[str]):
        """
        Convert text chunks into embedding vectors.
        """
        return self.embedding.embed_documents(chunks)