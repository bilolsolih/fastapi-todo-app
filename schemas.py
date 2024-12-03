from pydantic import BaseModel
from datetime import date

class Task(BaseModel):
    title: str
    description: str
    deadline: date