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


def test_get_project_positive():
    project_id = create_project()

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(
        f"{BASE_URL}/{project_id}",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["id"] == project_id
    assert response.json()["title"] == "Temp Project"


def test_get_project_negative():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(
        f"{BASE_URL}/invalid-id",
        headers=headers
    )

    assert response.status_code == 404
