# ---------- POST ----------
def test_create_project_positive(projects_api):
    response = projects_api.create_project({"title": "New Project"})
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative(projects_api):
    response = projects_api.create_project({})
    assert response.status_code == 400
    assert "error" in response.json()


# ---------- GET ----------

def test_get_project_positive(projects_api, created_project):
    response = projects_api.get_project(created_project)
    assert response.status_code == 200
    assert response.json()["id"] == created_project


def test_get_project_negative(projects_api):
    response = projects_api.get_project(999999999)
    assert response.status_code == 404
    assert "error" in response.json()


# ---------- PUT ----------

def test_update_project_positive(projects_api, created_project):
    response = projects_api.update_project(
        created_project,
        {"title": "Updated Project"}
    )
    assert response.status_code == 200


def test_update_project_negative(projects_api):
    response = projects_api.update_project(
        999999999,
        {"title": "Fail"}
    )
    assert response.status_code == 404
    assert "error" in response.json()
