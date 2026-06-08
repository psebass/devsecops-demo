from app.main import create_app


def test_hello():
    app = create_app()
    client = app.test_client()
    response = client.get("/hello?name=Pablo")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello Pablo"
