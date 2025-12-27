import requests

BASE_URL = "https://ru.yougile.com/api-v2/projects"
API_TOKEN = "myToken"


def create_project():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        BASE_URL,
        json={"title": "Temp Project"},
        headers=headers
    )

    assert response.status_code == 201
    return response.json()["id"]


def test_update_project_positive():
    project_id = create_project()

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "deleted": True,
        "title": "Temp Project"
    }

    response = requests.put(
        f"{BASE_URL}/{project_id}",
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_update_project_negative():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.put(
        f"{BASE_URL}/invalid-id",
        json={"title": "Fail"},
        headers=headers
    )

    assert response.status_code == 404
