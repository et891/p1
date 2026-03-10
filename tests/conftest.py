# tests/conftest.py
import os
import pytest
import httpx

@pytest.fixture
def client():
    base_url = os.getenv("BASE_URL", "http://api:8000")
    with httpx.Client(base_url=base_url, timeout=5.0) as client:
        yield client