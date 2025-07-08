from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_real_news():
    response = client.post("/predict", json={"text": "NASA just launched a new satellite."})
    assert response.status_code == 200
    assert response.json()["prediction"] in ["REAL", "FAKE"]

def test_predict_fake_news():
    response = client.post("/predict", json={"text": "Aliens landed in Paris and shook hands with the President."})
    assert response.status_code == 200
    assert response.json()["prediction"] in ["REAL", "FAKE"]
