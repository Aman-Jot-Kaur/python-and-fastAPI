# Import the required modules, including the Todo model if needed
import motor.motor_asyncio
from model import Todo  # Adjust the import if necessary

# MongoDB connection setup
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.TodoList
collection = database.todo

# Define async functions to interact with MongoDB
async def fetch_one_todo(title):
    document = await collection.find_one({"Title": title})
    return document

async def fetch_all_todos():
    todos = []
    async for document in collection.find({}):
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc):
    await collection.update_one({"Title": title}, {"$set": {"Description": desc}})
    document = await collection.find_one({"Title": title})
    return document

async def remove_todo(title):
    result = await collection.delete_one({"Title": title})
    return result.deleted_count > 0  # Return True if a document was deleted
