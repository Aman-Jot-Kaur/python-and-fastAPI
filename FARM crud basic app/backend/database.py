# Import the required modules, including the Todo model if needed
import motor.motor_asyncio
from model import Todo  
import bson 
# MongoDB connection setup
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.TodoList
collection = database.todo

# Define async functions to interact with MongoDB
async def fetch_one_todo(_id):
 try:
    object_id = bson.ObjectId(_id)
        
    document= await collection.find_one({"_id": object_id})
    
    
    return document
 except bson.errors.InvalidId:
        raise HTTPException(status_code=400,detail= f"Invalid _id format")


async def fetch_all_todos():
    todos = []
    async for document in collection.find({}):
        # Convert the ObjectId to a string
       
        document["_id"] = str(document["_id"])
        todos.append(document)
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    inserted_id = str(result.inserted_id)  
    document["_id"] = inserted_id 
    print(document)
    return document





async def update_todo(_id, todo):
    try:
        object_id = bson.ObjectId(_id)
        
        await collection.update_one({"_id": object_id}, {"$set": {"Title": todo.Title, "Description": todo.Description}})
        updated_document = await collection.find_one({"_id": object_id})
        return updated_document
    except bson.errors.InvalidId:
        raise HTTPException(400, f"Invalid _id format")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def remove_todo(_id):
    try:
        
        object_id = bson.ObjectId(_id)
        
        result = await collection.delete_one({"_id": object_id})
        if result.deleted_count > 0:
            deleted_id = str(object_id) 
            response = {"_id": deleted_id}
            return response
        raise HTTPException(404, f"There is no to-do item with _id {_id}")
    except bson.errors.InvalidId:
        raise HTTPException(400, f"Invalid _id format")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
