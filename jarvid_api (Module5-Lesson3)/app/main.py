from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, AWS Lambda"}

@app.get("/health")
def health_check():
    return {"status": "Healthy"}
