from fastapi.testclient import TestClient


def test_basic_get(client: TestClient):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json() == 'Hello, world!'
