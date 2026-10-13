#  exercise: in backend/app/schemas.py, write a Task model with id, description, and status.
# Make status accept only "pending", "in_progress", or "done". The hint is to look up typing.Literal. 
# Then add a short test script in scratch/ that creates one valid task and one with a bad status, and prints what happens.


from typing import Literal
from pydantic import BaseModel

class Task(BaseModel):
    id : int
    description : str
    status : Literal["pending", "in_progress", "done"] = "pending"


