import sqlalchemy
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

task_objects = [
    { "id" : 1 , "title" : "surat al-kahf" , "done" : False},
    { "id" : 2 , "title" : "clean room" , "done" : False },
    { "id" : 3 , "title" : "eat breakfast" , "done" : True}
]

@app.get("/")
async def root():
    return { "name" : "Task API" , "version" : 1.0 , "endpoints" : ["/tasks"] }

@app.get("/health")
async def health():
    return { "status" : "ok" }

@app.get("/tasks")
async def task():
    return task_objects

@app.get("/tasks/{id}")
async def tasks_id(id : int):
    for task in task_objects:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail = f"item {id} not found")

@app.post("/tasks", status_code=201)
async def add_task(task : TaskCreate):
    if task.title is None or not task.title.strip():
         raise HTTPException(status_code=400, detail = "Bad Request" )
    else:
        new_id = max((object["id"] for object in task_objects), default=0) + 1
        new_task = {"id" : new_id, "title" : task.title, "done" : False}
        task_objects.append(new_task)
    return new_task

# @app.put("/tasks/{id}")
# async def update_task(id: int, title: str, done: bool | None =None):
#     for task in task_objects:
#        if task["id"] == id:
#            if title.strip() == "" or None or not str:
#                raise HTTPException(status_code=400, detail= "Envalid/Empty Body")
#            task["title"] = title
#            if done == True or False:
#                task["done"] = done
#        raise HTTPException(status_code=404, detail= f"item {id} not found")       
               

@app.put("/tasks/{id}")
async def update_task(id: int, title: str, done: bool | None = None):
    for task in task_objects:
        if task["id"] == id:
           if title is None or 
    raise HTTPException(status_code=404, detail= f"item {id} not found")       
 