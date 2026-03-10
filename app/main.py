from fastapi import FastAPI, HTTPException
from app.schemas import Task, TaskCreate
from app.storage import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    complete_task,
    delete_task,
)

app = FastAPI(title="Simple Task API")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "FastAPI is working"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[dict[str, str]]:
    return [{"message": "FastAPI is working"},{"message": "FastAPI is working"}]


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task, status_code=201)
def add_task(task_data: TaskCreate) -> Task:
    return create_task(task_data)


@app.patch("/tasks/{task_id}/complete", response_model=Task)
def mark_task_completed(task_id: int) -> Task:
    task = complete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int) -> dict[str, str]:
    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}