from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_agent_ask():
    response = client.post("/api/agent/ask", json={"prompt": "Hello"})
    assert response.status_code == 200
    assert "result" in response.json()