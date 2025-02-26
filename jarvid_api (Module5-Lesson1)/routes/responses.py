from fastapi import APIRouter
from pydantic import BaseModel
import openai
from prometheus_client import Counter, Summary
import time

router = APIRouter()

class ResponseRequest(BaseModel):
    context: str
    query: str

REQUEST_COUNT_COMPLETIONS = Counter("request_count_completions", "Total number of requests")
REQUEST_LATENCY_COMPLETIONS = Summary("request_latency_seconds_completions", "Latency of API requests")

@router.post("/generate-response")
async def generate_response(request: ResponseRequest):
    REQUEST_COUNT_COMPLETIONS.inc()
    prompt = f"Context: {request.context}\n\nQuestion: {request.query}\n\nAnswer:"
    
    start_time = time.time()
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    
    REQUEST_LATENCY_COMPLETIONS.observe(time.time() - start_time)
    
    return {"response": response.choices[0].message.content.strip()}
