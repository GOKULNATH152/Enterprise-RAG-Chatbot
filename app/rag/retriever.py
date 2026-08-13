from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.vector_store = VectorStore()

    def search(self, query, k=3):
        return self.vector_store.similarity_search(
            query=query,
            k=k
        )
    
