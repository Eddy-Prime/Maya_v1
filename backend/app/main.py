from fastapi import FastAPI
from app.schemas import Task
from app.schemas import ChatResponse
from app.schemas import ChatRequest

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks/example", response_model= Task)
def example_task():
    return Task(id=1, description="Write router", status="pending")

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(reply=f"Maya heard: {request.message}")