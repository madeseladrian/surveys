from fastapi.testclient import TestClient
import pytest
from mongomock import MongoClient

from src.infra.db.mongodb import mongohelper
from src.main.config import create_app


class TestSurveysRoutes:
    mongohelper.connect(MongoClient())
    app = create_app()
    client = TestClient(app)

    @pytest.fixture
    def clear_db(self) -> None:
        collection = mongohelper.get_collection(collection='surveys')
        collection.delete_many({})

    def test_add_survey_on_fail(self, clear_db):
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
