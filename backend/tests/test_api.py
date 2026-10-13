
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_chat_returns_reply():
    response = client.post("/chat", json={"message": "hi"})
    assert response.status_code == 200
    assert response.json() == {"reply": "Maya heard: hi"}
       
def test_chat_rejects_missing_message():
    response = client.post("/chat", json={})
    assert response.status_code == 422
