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
    raise HTTPException(status_code=404, detail= f"item {id} not found")
    