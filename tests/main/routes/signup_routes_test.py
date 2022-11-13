from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.main.config import create_routes
from src.main.config.database import get_db
from ..mocks import mock_get_db


class TestSignupRoutes:
  app = FastAPI()
  create_routes(app=app)
  app.dependency_overrides[get_db] = mock_get_db
  client = TestClient(app)

  def test_create_user(self):
    response = self.client.post(
      '/signup/',
      json={
        "name": "mades",
        "email": "mades.eladrian5@gmail.com",
        "password": "123456",
        "password_confirmation": "123456"
      }
    )

    assert response.status_code == 201
    assert response.json() == {
      "body": True
    }
