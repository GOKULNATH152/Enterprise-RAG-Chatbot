from app.rag.vector_store import VectorStore

store = VectorStore()

chunks = [
    "Artificial Intelligence is transforming industries.",
    "Computer Vision detects and understands images.",
    "Deep Learning uses neural networks."
]

print("Adding documents to ChromaDB...")

store.add_documents(chunks)

print("Searching...\n")

results = store.similarity_search(
    "What is Computer Vision?"
)

print("=" * 60)

for index, doc in enumerate(results, start=1):
    print(f"\nResult {index}")
    print(doc.page_content)

print("\n" + "=" * 60)