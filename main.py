from fastapi import FastAPI
from Todo import TodoModel, TodoHelper
from database import mongo_db
from bson import ObjectId


app = FastAPI()

TodoCollection = mongo_db["Todo"]


@app.get("/")
async def IndexView():
    data = await TodoCollection.find().to_list(length=None)

    all_todos = []
    for todo in data:
        all_todos.append(TodoHelper(todo))

    # all_todos = [TodoHelper(todo) for todo in data]

    return all_todos


@app.post("/create")
async def createView(data: TodoModel):
    result = await TodoCollection.insert_one(dict(data))
    print(result)
    return {"msg": data}


@app.delete("/delete/{id}")
async def deleteView(id: str):
    data = await TodoCollection.find_one_and_delete({"_id":ObjectId(id)})
    print(data)
    return {"msg": "successufully deleted"}




@app.put("/delete/{id}")
async def updateView(id: str, data: TodoModel):
    data = await TodoCollection.find_one_and_update({"_id":ObjectId(id)}, {
        "$set": dict(data)
    })
    print(data)
    return {"msg": "successufully updated"}
    