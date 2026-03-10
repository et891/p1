from app.schemas import Task, TaskCreate

tasks: list[Task] = []
task_id_counter = 1


def get_all_tasks() -> list[Task]:
    return tasks


def get_task_by_id(task_id: int) -> Task | None:
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def create_task(task_data: TaskCreate) -> Task:
    global task_id_counter

    new_task = Task(
        id=task_id_counter,
        title=task_data.title,
        description=task_data.description,
        completed=False,
    )
    tasks.append(new_task)
    task_id_counter += 1
    return new_task


def complete_task(task_id: int) -> Task | None:
    task = get_task_by_id(task_id)
    if task:
        task.completed = True
    return task


def delete_task(task_id: int) -> bool:
    global tasks
    task = get_task_by_id(task_id)
    if not task:
        return False

    tasks = [item for item in tasks if item.id != task_id]
    return True