# from fastapi import FastAPI
# from fastapi.responses import JSONResponse

# app = FastAPI(
#     title="Enterprise RAG Chatbot",
#     description="Production Ready RAG Chatbot using FastAPI + LangChain + Ollama",
#     version="1.0.0"
# )


# @app.get("/")
# def home():
#     return {
#         "message": "Welcome to Enterprise RAG Chatbot",
#         "status": "Running"
#     }


# @app.get("/health")
# def health():
#     return JSONResponse(
#         content={
#             "status": "Healthy",
#             "application": "Enterprise RAG Chatbot"
#         }
#     )
# from fastapi import FastAPI
# from app.core.logger import logger

# app = FastAPI(
#     title="Enterprise RAG Chatbot",
#     version="1.0.0",
#     description="Enterprise AI Assistant using FastAPI + LangChain + Ollama"
# )


# @app.on_event("startup")
# async def startup():
#     logger.info("Enterprise RAG Chatbot Started")


# @app.get("/")
# def home():
#     return {
#         "application": "Enterprise RAG Chatbot",
#         "version": "1.0.0",
#         "status": "Running"
#     }


# @app.get("/health")
# def health():
#     return {
#         "status": "Healthy"
#     }
from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.core.logger import logger

app = FastAPI(
    title="Enterprise RAG Chatbot",
    version="1.0.0",
    description="Enterprise AI Assistant using FastAPI + Ollama"
)


@app.on_event("startup")
async def startup():
    logger.info("Application Started")


app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "application": "Enterprise RAG Chatbot",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }