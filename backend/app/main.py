# exercise: create backend/app/main.py with two endpoints.

# GET /health returns {"status": "ok"}.
# GET /tasks/example returns a Task built from your schema, for example id 1, “Write router”, “pending”. Import it with from app.schemas import Task.
#  As a hint, adding response_model=Task inside the decorator makes FastAPI check the output against your model.


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/ping")
# def ping():
#     return {"message": "pong"}


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