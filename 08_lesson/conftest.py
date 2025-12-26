import pytest
from projects_api import ProjectsAPI


@pytest.fixture
def projects_api():
    return ProjectsAPI()


@pytest.fixture
def created_project(projects_api):
    response = projects_api.create_project({"title": "Temp Project"})
    assert response.status_code == 201
    return response.json()["id"]
