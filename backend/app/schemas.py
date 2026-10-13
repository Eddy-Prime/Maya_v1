#  exercise: in backend/app/schemas.py, write a Task model with id, description, and status.
# Make status accept only "pending", "in_progress", or "done". The hint is to look up typing.Literal. 
# Then add a short test script in scratch/ that creates one valid task and one with a bad status, and prints what happens.

#exercise:

# In backend/app/schemas.py, add a ChatRequest model with one field, message: str, and a ChatResponse model with one field, reply: str.
# In main.py, add POST /chat that takes a ChatRequest and returns a ChatResponse. For now the reply can be a fake echo like "Maya heard: <their message>". The real routing comes after this.
# Use response_model=ChatResponse the same way you did for Task.

from typing import Literal
from pydantic import BaseModel

class Task(BaseModel):
    id : int
    description : str
    status : Literal["pending", "in_progress", "done"] = "pending"


class ChatRequest(BaseModel):
    message: str

class ChatResponse (BaseModel):
    reply: str



