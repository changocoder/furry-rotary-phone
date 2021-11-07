import pytest
from fastapi.testclient import TestClient
from api.views import app



@pytest.fixture(scope="session")
def api_client():
    client = TestClient(app)
    return client

def test_read_root(api_client):
    response = api_client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}