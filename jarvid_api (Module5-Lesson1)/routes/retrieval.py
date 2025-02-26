from fastapi import APIRouter
from pydantic import BaseModel
import faiss
import numpy as np

router = APIRouter()

index = faiss.read_index("vector_index.faiss")

class RetrievalRequest(BaseModel):
    embedding: list
    top_k: int

@router.post("/search-similarity")
async def search_similarity(request: RetrievalRequest):
    query_embedding = np.array(request.embedding, dtype=np.float32).reshape(1, -1)
    distances, indices = index.search(query_embedding, request.top_k)
    return {"distances": distances.tolist(), "indices": indices.tolist()}
