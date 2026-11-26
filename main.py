from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
import connect_with_db as db

@asynccontextmanager
async def lifespan(FastAPI):
    db.create_db_and_tables()
    db.count_rows()
    yield
    
app = FastAPI(lifespan=lifespan)

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
    return db.list_tasks()

@app.get("/tasks/{id}")
async def tasks_id(id : int):
    for task in db.list_tasks():
        if task.id == id:
            return task
    raise HTTPException(status_code=404, detail = f"item {id} not found")

@app.post("/tasks", status_code=201)
async def add_task(title:str|None=None, done:bool|None=False):
    if title is None or not title.strip():
         raise HTTPException(status_code=400, detail = "Title cannot be empty" )
    else:
        new_id = max((object.id for object in db.list_tasks()), default=0) + 1
        new_task=db.Tasks(id=new_id,title=title,done=done)
        db.create_tasks(new_task)
    return new_task
              
@app.put("/tasks/{id}")
async def update_task(id:int|None, title:str|None =None, done:bool|None=False ):
    for task in db.list_tasks():
        if task.id == id:
           if task.title is None or not task.title.strip():
               raise HTTPException(status_code=400, detail= "Envalid/Empty Bady") 
           else:
               task.title = title
               if task.done is not None:
                   task.done = done
               return task
    raise HTTPException(status_code=404, detail= f"item {id} not found")      


@app.delete("/task/{id}", status_code=204)
async def delete_task(id: int):
    idlist=[]
    for task in db.list_tasks():
        if task.id == id:
            db.delete_tasks(id)
            idlist.append(id)
    if id not in idlist:        
        raise HTTPException(status_code=404, detail= f"task {id} is not found")

@app.delete("/task", status_code=204)
async def delete_all():
    db.delete_tasks()