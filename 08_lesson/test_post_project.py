import requests
from config import BASE_URL, HEADERS, CREATE_PROJECT_PAYLOAD


def test_create_project_positive():
    response = requests.post(
        BASE_URL,
        json=CREATE_PROJECT_PAYLOAD,
        headers=HEADERS
    )

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative():
    response = requests.post(
        BASE_URL,
        json={},
        headers=HEADERS
    )

    assert response.status_code == 400
