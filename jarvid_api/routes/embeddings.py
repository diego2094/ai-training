from fastapi import APIRouter
from pydantic import BaseModel
import openai

router = APIRouter()

class EmbeddingRequest(BaseModel):
    text: str

@router.post("/generate-embedding")
async def generate_embedding(request: EmbeddingRequest):
    client = openai.OpenAI()
    response = client.embeddings.create(
        input=request.text,
        model="text-embedding-ada-002"
    )
    return {"embedding": response['data'][0]['embedding']}
