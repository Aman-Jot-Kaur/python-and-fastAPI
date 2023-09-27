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
origins = ['*']


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
    try:
        response = await fetch_all_todos()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@app.get("/api/todo/{title}",response_model=Todo)
async def get_todo_by_id(title:str):
    try:
        response=await fetch_one_todo(title)
        if response:
                    return response
        raise HTTPException(404, f"there is no to do item with {title} title")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
 try:
     response= await create_todo(todo.dict())
     if response:
        return response
     raise HTTPException(400,"something went wrong bad request")
 except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.put("/api/todo/{title}",response_model=Todo)
async def modify_todo(title: str, desc: str):
 try:
     response= await update_todo(title, desc)
     if response:
         return response
     raise HTTPException(404, f"there is no to do item with {title} title")
 except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")



    
@app.delete("/api/todo/{title}")
async def delete_todo(title:str):
 try:
    response= await remove_todo(title)
    if response:
        return "successfully delete the required item"
    raise HTTPException(404, f"there is no to do item with {title} title")
 except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

