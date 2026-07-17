import os

def test_model_exists():
    assert os.path.exists("models/best_model.pkl")
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_monitoring_folder():
    assert os.path.exists("monitoring")        