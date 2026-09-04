from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="AWS Production API",
    description="FastAPI deployed on AWS ECS via Terraform.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "status": "healthy",
        "message": "AWS Production healtch check",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
