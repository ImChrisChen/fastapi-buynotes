from fastapi.testclient import TestClient

from main import app
from src.config.config import settings

client = TestClient(app)


def test_app():
    r = client.get(f'{settings.API_V1_STR}/account_note')
    response = r.json()
    assert type(response) == list
