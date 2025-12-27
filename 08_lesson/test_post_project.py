import requests

BASE_URL = "https://ru.yougile.com/api-v2/projects"

# НАСТАВНИКУ:
# вставить API-токен YouGile
API_TOKEN = "myToken"


def test_create_project_positive():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "title": "Temp Project"
    }

    response = requests.post(
        BASE_URL,
        json=payload,
        headers=headers
    )

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        BASE_URL,
        json={},
        headers=headers
    )

    assert response.status_code == 400

