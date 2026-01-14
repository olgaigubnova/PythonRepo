import requests
from config import (
    BASE_URL,
    HEADERS,
    CREATE_PROJECT_PAYLOAD,
    UPDATE_PROJECT_PAYLOAD,
)


def create_project():
    response = requests.post(
        BASE_URL,
        json=CREATE_PROJECT_PAYLOAD,
        headers=HEADERS
    )
    return response.json()["id"]


def test_update_project_positive():
    project_id = create_project()

    response = requests.put(
        f"{BASE_URL}/{project_id}",
        json=UPDATE_PROJECT_PAYLOAD,
        headers=HEADERS
    )

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_update_project_negative():
    response = requests.put(
        f"{BASE_URL}/invalid-id",
        json=UPDATE_PROJECT_PAYLOAD,
        headers=HEADERS
    )

    assert response.status_code == 404
