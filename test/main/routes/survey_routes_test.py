from fastapi.testclient import TestClient
import pytest
from mongomock import MongoClient

from src.infra.db.mongodb import mongohelper
from src.main.config import create_app
from src.main.middlewares import admin_auth


class TestSurveysRoutes:
    mongohelper.connect(MongoClient())
    app = create_app()
    client = TestClient(app)

    @pytest.fixture
    def clear_db(self) -> None:
        collection = mongohelper.get_collection(collection='surveys')
        collection.delete_many({})

    def override_admin_auth(self) -> str:
        return 'any_token'

    def test_add_survey_not_authenticated(self, clear_db):
        response = self.client.post(
            '/surveys/',
            json={
                "question": "any_question",
                "answers": [
                    {
                        "image": "http://any_url",
                        "answer": "any_answer"
                    }
                ]
            }
        )

        assert response.status_code == 401

    def test_add_survey_on_success(self, clear_db):
        # Simulate a valid token
        self.app.dependency_overrides[admin_auth] = self.override_admin_auth
        response = self.client.post(
            '/surveys/',
            json={
                "question": "any_question",
                "answers": [
                    {
                        "image": "http://any_url",
                        "answer": "any_answer"
                    }
                ]
            }
        )

        assert response.status_code == 204

    def test_add_survey_fails_on_422(self, clear_db):
        response = self.client.post(
            '/surveys/',
            json={
                "answers": [
                    {
                        "image": "http://any_url",
                        "answer": "any_answer"
                    }
                ]
            }
        )

        assert response.status_code == 422
