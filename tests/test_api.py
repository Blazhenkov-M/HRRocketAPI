import json
from fastapi import HTTPException
from unittest.mock import patch, AsyncMock
import pytest

from app.api.api_v1.services.books import BookService

broken_request = [
    ({
        "author": "Михаил Булгаков",
        "published_year": "сто пятьсот",  # не тот тип данных
        "summary": "Очень интересная книга",
        "title": "Мастер и Маргарита"
    }),
    ({
        "author": "Михаил Булгаков",
        "published_year": 1967,
        "summary": "",  # неверная длина
        "title": "Мастер и Маргарита"
    })
]

broken_id = [
    ("d3346be7-1a35-4b2a-84c7-f1561280e53"),  # не uuid
    (12)  # не uuid
]


def get_response(response_value):
    return json.dumps(response_value)


def test_set_positive(client, request_set_positive_fixture, response_positive_fixture):
    with patch.object(BookService, "set", new_callable=AsyncMock) as mock_process:
        mock_process.return_value = response_positive_fixture

        r = client.post("/v1/books", json=request_set_positive_fixture)
        assert r.status_code == 200


def test_set_internal_server_error(client, request_set_positive_fixture, response_positive_fixture):
    with patch.object(BookService, "set", new_callable=AsyncMock) as mock_process:
        mock_process.return_value = response_positive_fixture
        mock_process.side_effect = HTTPException(status_code=500)

        r = client.post("/v1/books", json=request_set_positive_fixture)
        assert r.status_code == 500


@pytest.mark.parametrize('test_request', broken_request)
def test_set_invalid_request(client, test_request):
    r = client.post("/v1/books", json=test_request)
    assert r.status_code == 422


def test_get_positive(client, boot_id_fixture, response_positive_fixture):
    with patch.object(BookService, "get", new_callable=AsyncMock) as mock_process:
        mock_process.return_value = response_positive_fixture

        r = client.get(f"/v1/books/?book_id={boot_id_fixture}")
        res = r.json()
        assert r.status_code == 200
        assert res == response_positive_fixture


def test_get_internal_server_error(client, boot_id_fixture, response_positive_fixture):
    with patch.object(BookService, "get", new_callable=AsyncMock) as mock_process:
        mock_process.return_value = response_positive_fixture
        mock_process.side_effect = HTTPException(status_code=500)

        r = client.get(f"/v1/books/?book_id={boot_id_fixture}")
        assert r.status_code == 500


@pytest.mark.parametrize('test_request', broken_id)
def test_set_invalid_request(client, test_request):
    r = client.get(f"/v1/books/?book_id={broken_request}")
    assert r.status_code == 422


def test_update_positive(client,
                         boot_id_fixture,
                         request_update_positive_fixture,
                         response_update_positive_fixture):
    with patch.object(BookService, "update", new_callable=AsyncMock) as mock_process:
        mock_process.return_value = response_update_positive_fixture

        r = client.put(f"/v1/books/?book_id={boot_id_fixture}", json=request_update_positive_fixture)
        res = r.json()
        assert r.status_code == 200
        assert res == response_update_positive_fixture


def test_update_internal_server_error(client,
                                      boot_id_fixture,
                                      request_update_positive_fixture,
                                      response_update_positive_fixture):
    with patch.object(BookService, "update", new_callable=AsyncMock) as mock_process:
        mock_process.return_value = response_update_positive_fixture
        mock_process.side_effect = HTTPException(status_code=500)

        r = client.put(f"/v1/books/?book_id={boot_id_fixture}", json=request_update_positive_fixture)
        assert r.status_code == 500


def test_delete_positive(client, boot_id_fixture, response_update_positive_fixture):
    with patch.object(BookService, "delete", new_callable=AsyncMock) as mock_process:
        mock_process.return_value = response_update_positive_fixture

        r = client.delete(f"/v1/books/?book_id={boot_id_fixture}")
        res = r.json()
        assert r.status_code == 200
        assert res == response_update_positive_fixture


def test_delete_internal_server_error(client, boot_id_fixture, response_update_positive_fixture):
    with patch.object(BookService, "delete", new_callable=AsyncMock) as mock_process:
        mock_process.return_value = response_update_positive_fixture
        mock_process.side_effect = HTTPException(status_code=500)

        r = client.delete(f"/v1/books/?book_id={boot_id_fixture}")
        assert r.status_code == 500
