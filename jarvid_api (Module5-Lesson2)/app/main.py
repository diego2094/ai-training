from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Jarvid API"}

@app.get("/health")
def health_check():
    return {"status": "Healthy"}

@app.post("/generate-embedding")
def generate_embedding():
    return {"embedding": [0.1, 0.2, 0.3]}

@app.post("/search-similarity")
def search_similarity():
    return {"results": [{"id": 1, "name": "Alice", "similarity": 0.95}]}
