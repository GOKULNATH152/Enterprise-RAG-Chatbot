from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.retriever import Retriever
from app.llm.ollama import OllamaLLM


router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)


class Query(BaseModel):
    question:str



retriever = Retriever()
llm = OllamaLLM()



@router.post("/ask")
async def ask_question(data:Query):

    docs = retriever.search(
        data.question
    )


    context = "\n\n".join(
    [doc.page_content for doc in docs]
    )


    prompt=f"""
You are an AI assistant.
Answer only using the given context.

Context:
{context}

Question:
{data.question}

Answer:
"""


    answer = llm.generate(prompt)


    return {
    "question": data.question,
    "answer": answer,
    "sources": [doc.page_content for doc in docs]
}