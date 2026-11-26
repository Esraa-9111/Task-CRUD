import os
from sqlmodel import SQLModel, Field, create_engine,Session,select
from dotenv import load_dotenv


load_dotenv()

sqlite_url = "sqlite:///tasks.db"
db_url=os.getenv('DATABASE_URL')
engine = create_engine(db_url, echo=True)

class Tasks(SQLModel, table=True):
    id: int | None = Field(default=0, primary_key=True)
    title: str |None = None
    done: bool |None = False

def create_db_and_tables():  
    SQLModel.metadata.create_all(engine) 

def create_tasks(task: Tasks|None =None):
    with Session(engine) as session:
        if not task:
            tasks= [Tasks(id=1, title="unidentified task 1" ),
                    Tasks(id=2, title="unidentified task 2" ),
                    Tasks(id=3, title="unidentified task 3" )]
            session.add_all(tasks)
            session.commit() 
        else:
            taskx= Tasks(id=task.id, title=task.title, done=task.done)
            session.add(taskx)
            session.commit()
            result_task = session.get(Tasks, taskx.id)
            return result_task
        
def count_rows():
    with Session(engine) as session:
        statement= select(Tasks)
        results = session.exec(statement).all()
        
        if len(results) == 0:
            create_tasks()

def list_tasks(id : int | None = None):
    with Session(engine) as session:
        if id is not None:
            statement= select(Tasks).where(Tasks.id == id)
            result = session.exec(statement)
            return (result.one())
        if id is None:
            objects = session.exec(select(Tasks))
            return (objects.all())

def update_tasks(task:Tasks):
    with Session(engine) as session:
        statement= select(Tasks).where(Tasks.id == task.id)
        result = session.exec(statement)
        updated_task=result.one()
        if task.title is not None:
            updated_task.title = task.title
        if task.done is not None:
            updated_task.done = task.done
            
        session.add(updated_task)
        session.commit()
        session.refresh(updated_task)
        return updated_task
        


def delete_tasks(id: int | None = None):
    with Session(engine) as session:
        if id is None:
            tasks = session.exec(select(Tasks)).all()
            session.delete_all(tasks)
            session.commit()
        else:
            statement = select(Tasks).where(Tasks.id == id)
            result = session.exec(statement)
            task = result.one()
            session.delete(task)
            session.commit()