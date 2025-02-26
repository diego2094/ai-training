from fastapi import APIRouter
from pydantic import BaseModel
import openai
from prometheus_client import Counter, Summary
import time

router = APIRouter()

class EmbeddingRequest(BaseModel):
    text: str
    
REQUEST_COUNT_EMBEDDINGS = Counter("request_count_embedding", "Total number of requests")
REQUEST_LATENCY_EMBEDDINGS = Summary("request_latency_seconds_embedding", "Latency of API requests")

@router.post("/generate-embedding")
async def generate_embedding(request: EmbeddingRequest):
    REQUEST_COUNT_EMBEDDINGS.inc()
    client = openai.OpenAI()
    
    start_time = time.time()
    
    response = client.embeddings.create(
        input=request.text,
        model="text-embedding-ada-002"
    )
    
    REQUEST_LATENCY_EMBEDDINGS.observe(time.time() - start_time)
    
    return {"embedding": response.data[0].embedding}
