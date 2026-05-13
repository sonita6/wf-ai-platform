from fastapi import FastAPI

app = FastAPI(
    title="WF AI Platform",
    description="Production-grade ML + GenAI system",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "0.1.0"}

@app.get("/")
def root():
    return {"message": "WF AI Platform is running"}