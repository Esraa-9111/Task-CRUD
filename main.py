import sqlalchemy
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"Name" : "TaskAPI", "Version" : "1.0", "Endpoints" : ["/task"]}