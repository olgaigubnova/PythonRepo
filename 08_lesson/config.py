# config.py

BASE_URL = "https://ru.yougile.com/api-v2/projects"

API_TOKEN = "PASTE_TOKEN_HERE"  # наставник подставь токен

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

CREATE_PROJECT_PAYLOAD = {
    "title": "Temp Project"
}

UPDATE_PROJECT_PAYLOAD = {
    "title": "Temp Project",
    "deleted": True
}
