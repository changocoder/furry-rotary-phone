import pytest
from fastapi.testclient import TestClient
from api.views import app

client = TestClient(app)


@pytest.fixture(scope="session")
def api_client():
    return client


def test_read_root(api_client):
    response = api_client.get("/root")
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}

def test_items(api_client):
    response = api_client.get("/items/1?q=sarasa")
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 1,
        "q": "sarasa",
    }
