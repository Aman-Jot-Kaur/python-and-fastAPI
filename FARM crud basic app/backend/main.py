from fastapi import FastAPI, HTTPException, Request, status, Response
from fastapi.middleware.cors import CORSMiddleware
from model import Todo, TodoResponse
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


@app.get("/api/todo/{_id}",response_model=TodoResponse)
async def get_todo_by_id(_id: str):
 

        response = await fetch_one_todo(_id)
        print(response)
        if not response:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
            return Response(content="Item not found", status_code=404)
           
          
        if response:
            response["_id"] = str(response["_id"])
            response["status"]=200
            return response
        raise HTTPException(status_code=404, detail="item doesnot exist")
   


@app.post("/api/todo")
async def post_todo(todo: Todo):
    try:
        response = await create_todo(todo.dict())
        if response:
            print("post respone in post_todo")
            print(response)
            return response  # Include the _id in the response

        raise HTTPException(400, "Something went wrong bad request")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.put("/api/todo/{_id}")
async def modify_todo(_id: str, todo: Todo):
    try:
        response = await update_todo(_id, todo)

        if response:
            response["_id"] = str(response["_id"])
            return response

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.delete("/api/todo/{_id}")
async def delete_todo(_id: str):
    try:

        response = await remove_todo(_id)
        if response:
            return response
        raise HTTPException(404, f"There is no to-do item with _id {_id}")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Internal Server Error to delete")
