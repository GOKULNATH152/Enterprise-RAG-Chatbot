from app.rag.embeddings import EmbeddingService

embedding_service = EmbeddingService()

chunks = [
    "Artificial Intelligence is transforming industries.",
    "Computer Vision enables machines to understand images."
]

print("Generating embeddings...")

vectors = embedding_service.create_embeddings(chunks)

print("=" * 50)
print("Embedding Test Successful")
print("=" * 50)
print(f"Chunks        : {len(chunks)}")
print(f"Vectors       : {len(vectors)}")
print(f"Vector Length : {len(vectors[0])}")
print("=" * 50)