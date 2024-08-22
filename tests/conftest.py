import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def request_set_positive_fixture():
    return {
        "author": "А. Дюма",
        "published_year": 1844,
        "summary": "Интересная книга",
        "title": "Три мушкетёра"
    }


@pytest.fixture
def request_update_positive_fixture():
    return {
        "author": "Михаил Булгаков",
        "published_year": 1967,
        "summary": "Очень интересная книга",
        "title": "Мастер и Маргарита"
    }


@pytest.fixture
def boot_id_fixture():
    return "d3346be7-1a35-4b2a-84c7-f1561280e539"


@pytest.fixture
def response_positive_fixture():
    return {
        "title": "Три мушкетёра",
        "author": "А. Дюма",
        "published_year": 1844,
        "summary": "Интересная книга",
        "id": "d3346be7-1a35-4b2a-84c7-f1561280e539"
    }


@pytest.fixture
def response_update_positive_fixture():
    return {
        "author": "Михаил Булгаков",
        "published_year": 1967,
        "summary": "Очень интересная книга",
        "title": "Мастер и Маргарита",
        "id": "d3346be7-1a35-4b2a-84c7-f1561280e539"
    }
