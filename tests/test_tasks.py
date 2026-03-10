import allure


@allure.feature("Tasks API")
class TestTasks:


    @allure.title("Check API root endpoint")
    @allure.story("Root endpoint availability")
    def test_root(self, client):
        with allure.step("Send GET / request"):
            response = client.get("/")

        with allure.step("Verify response"):
            assert response.status_code == 200
            assert response.json() == {"message": "FastAPI is working"}


    @allure.title("Create task")
    @allure.story("Task creation")
    def test_create_task(self, client):
        payload = {
            "title": "Write tests",
            "description": "Integration testing"
        }

        with allure.step("Send POST /tasks"):
            response = client.post("/tasks", json=payload)

        with allure.step("Validate response"):
            assert response.status_code == 201
            data = response.json()

            assert data["title"] == payload["title"]
            assert data["description"] == payload["description"]
            assert data["completed"] is False
            assert "id" in data


    @allure.title("Get tasks list")
    @allure.story("Retrieve tasks")
    def test_get_tasks(self, client):
        with allure.step("Send GET /tasks"):
            response = client.get("/tasks")

        with allure.step("Validate response"):
            assert response.status_code == 200
            assert isinstance(response.json(), list)


    @allure.title("Complete task")
    @allure.story("Task completion")
    def test_complete_task(self, client):
        with allure.step("Create task"):
            create = client.post("/tasks", json={"title": "Task"})
            task_id = create.json()["id"]

        with allure.step("Send PATCH /tasks/{id}/complete"):
            response = client.patch(f"/tasks/{task_id}/complete")

        with allure.step("Validate completion"):
            assert response.status_code == 200
            assert response.json()["completed"] is True


    @allure.title("Delete task")
    @allure.story("Task deletion")
    def test_delete_task(self, client):
        with allure.step("Create task"):
            create = client.post("/tasks", json={"title": "Delete me"})
            task_id = create.json()["id"]

        with allure.step("Send DELETE /tasks/{id}"):
            response = client.delete(f"/tasks/{task_id}")

        with allure.step("Validate deletion"):
            assert response.status_code == 200