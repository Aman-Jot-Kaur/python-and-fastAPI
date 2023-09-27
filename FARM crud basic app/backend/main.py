from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)
app = FastAPI()

# ORIGIN OBJECT to allow headers and methods
origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Ping": "pong"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}",response_model=Todo)
async def get_todo_by_id(title:str):
    response=await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"there is no to do item with {title} title")

@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo:Todo):
     response= await create_todo(todo.dict())
     if response:
        return response
     raise HTTPException(400,"something went wrong bad request")

@app.put("/api/todo/{title}",response_model=Todo)
async def modify_todo(title: str, desc: str):
    response= await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"there is no to do item with {title} title")


    
@app.delete("/api/todo/{title}")
async def delete_todo(title:str):
    response= await remove_todo(title)
    if response:
        return "successfully delete the required item"
    raise HTTPException(404, f"there is no to do item with {title} title")

