def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI is working"}


def test_create_task(client):
    payload = {
        "title": "Write tests",
        "description": "Integration testing"
    }

    response = client.post("/tasks", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["completed"] is False
    assert "id" in data


def test_get_tasks(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_complete_task(client):
    create = client.post("/tasks", json={"title": "Task"})
    task_id = create.json()["id"]

    response = client.patch(f"/tasks/{task_id}/complete")

    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_task(client):
    create = client.post("/tasks", json={"title": "Delete me"})
    task_id = create.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200