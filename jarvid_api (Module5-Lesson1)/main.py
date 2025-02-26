from fastapi import FastAPI
from routes.embeddings import router as embedding_router
from routes.retrieval import router as retrieval_router
from routes.responses import router as response_router
from routes.health import router as health
from prometheus_client import start_http_server

app = FastAPI()

start_http_server(9100)

app.include_router(embedding_router, prefix="/api/v1")
app.include_router(retrieval_router, prefix="/api/v1")
app.include_router(response_router, prefix="/api/v1")
app.include_router(health, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the Jarvid API"}
