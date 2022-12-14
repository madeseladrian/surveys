from fastapi.testclient import TestClient
import pytest
from mongomock import MongoClient

from src.infra.db.mongodb import mongohelper
from src.main.config import create_app


class TestLoginRoutes:
    mongohelper.connect(MongoClient())
    app = create_app()
    client = TestClient(app)

    @pytest.fixture
    def clear_db(self) -> None:
        collection = mongohelper.get_collection(collection='accounts')
        collection.delete_many({})

    def test_create_user(self, clear_db):
        response = self.client.post(
            '/signup/',
            json={
                "name": "mades",
                "email": "mades@gmail.com",
                "password": "123456",
                "password_confirmation": "123456"
            }
        )

        assert response.status_code == 200

    def test_create_user_on_fail(self, clear_db):
        response = self.client.post(
            '/signup/',
            json={
                "name": "mades",
                "email": "mades",
                "password": "123456",
                "password_confirmation": "123456"
            }
        )

        assert response.status_code == 400

    def test_login_on_success(self, clear_db):
        self.client.post(
            '/signup/',
            json={
                "name": "mades",
                "email": "mades@gmail.com",
                "password": "123456",
                "password_confirmation": "123456"
            }
        )
        response = self.client.post(
            '/login/',
            data={'username': 'mades@gmail.com', 'password': '123456'}
        )

        assert response.status_code == 200
        assert response.json().get('name')
        assert response.json().get('access_token')
        assert response.json().get('token_type')

    def test_login_on_fail(self, clear_db):
        self.client.post(
            '/signup/',
            json={
                "name": "mades",
                "email": "mades@gmail.com",
                "password": "123456",
                "password_confirmation": "123456"
            }
        )
        response = self.client.post(
            '/login/',
            data={'username': 'mades@gmail.com', 'password': '1234567'}
        )

        assert response.status_code == 401
