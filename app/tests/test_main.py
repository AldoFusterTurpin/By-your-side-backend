from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}