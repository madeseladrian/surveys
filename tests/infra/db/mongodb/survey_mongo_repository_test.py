from faker import Faker
import mongomock
import pytest

from src.domain.params import AddSurveyParams
from src.infra.db.mongodb import mongohelper, SurveyMongoRepository

from ....domain.mocks import mock_add_survey_params


class TestSurveyMongoRepository:
    # SetUp
    faker = Faker()
    params: AddSurveyParams = mock_add_survey_params()
    mongohelper.connect(mongomock.MongoClient())

    def make_sut(self) -> SurveyMongoRepository:
        return SurveyMongoRepository()

    @pytest.fixture
    def clear_db(self) -> None:
        collection = mongohelper.get_collection(collection='surveys')
        collection.delete_many({})

    def test_1_should_return_True_on_success(self, clear_db):
        sut = self.make_sut()
        sut.add(dict(self.params))
        collection = mongohelper.client['surveys']['surveys']
        count = collection.count_documents({})

        assert count == 1
