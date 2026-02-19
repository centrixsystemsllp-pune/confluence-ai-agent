# Main application entry point
from fastapi import FastAPI

app = FastAPI(
    title="Confluence AI Search Agent",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
