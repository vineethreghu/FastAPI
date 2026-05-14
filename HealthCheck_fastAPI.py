from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "service": "fastapi-app",
        "timestamp": datetime.now().isoformat()
    }