from pydantic import BaseModel

class Todo(BaseModel):
    Title:str
    Description: str