from fastapi import APIRouter
from pydantic import BaseModel
import openai

router = APIRouter()

class ResponseRequest(BaseModel):
    context: str
    query: str

@router.post("/generate-response")
async def generate_response(request: ResponseRequest):
    openai.api_key = "your_openai_api_key"
    prompt = f"Context: {request.context}\n\nQuestion: {request.query}\n\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return {"response": response['choices'][0]['text'].strip()}
