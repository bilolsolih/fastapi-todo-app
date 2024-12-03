from sqlite3 import Connection

from fastapi import FastAPI, Depends

from database import set_up_database, get_db_connection
from schemas import Task

app = FastAPI()


@app.on_event("startup")
def startup():
    set_up_database()


@app.get(path="/tasks/list")
def get_tasks(db: Connection = Depends(get_db_connection)):
    tasks = db.execute("SELECT * FROM tasks;").fetchall()
    return tasks


@app.post(path="/tasks/create")
def create_tasks(task: Task, db: Connection = Depends(get_db_connection)):
    db.execute(
        "INSERT INTO tasks (title, description, deadline) VALUES (?, ?, ?);",
        [task.title, task.description, task.deadline]
    )
    db.commit()
    return task
