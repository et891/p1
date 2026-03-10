import pytest
import httpx


BASE_URL = "http://localhost:8000"


@pytest.fixture
def client():
    with httpx.Client(base_url=BASE_URL) as client:
        yield client