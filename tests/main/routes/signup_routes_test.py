from fastapi.testclient import TestClient
from mongomock import MongoClient
import pytest

from src.infra.db.mongodb import mongohelper
from src.main.config import create_app


class TestSignupRoutes:
    mongohelper.connect(MongoClient())
    app = create_app()
    client = TestClient(app)

    @pytest.fixture
    def clear_db(self) -> None:
        collection = mongohelper.get_collection(collection='accounts')
        collection.delete_many({})

    def test_create_user(self, clear_db):
        response = self.client.post(
            '/api/signup/',
            json={
                "name": "mades",
                "email": "mades@gmail.com",
                "password": "123456",
                "password_confirmation": "123456"
            }
        )

        assert response.status_code == 201
        assert response.json() == {"body": True}
