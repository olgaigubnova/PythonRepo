import requests


class ProjectsAPI:
    BASE_URL = "https://ru.yougile.com/api-v2/projects"

    def __init__(self):
        self.headers = {
            "Authorization": (
                "Bearer "
                "Oc-3hXHM8bIuZ+bF0avHltpHU8kSV+UcZDJbQTonPEifcQvLWM2gY3"
                "ju9viPOSIe"
            ),
            "Content-Type": "application/json"
        }

    def create_project(self, data):
        return requests.post(
            self.BASE_URL,
            json=data,
            headers=self.headers
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.BASE_URL}/{project_id}",
            headers=self.headers
        )

    def update_project(self, project_id, data):
        return requests.put(
            f"{self.BASE_URL}/{project_id}",
            json=data,
            headers=self.headers
        )
