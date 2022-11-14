import mongomock
import pytest

from src.domain.params import AddAccountParams
from src.infra.db.mongodb import AccountMongoRepository, mongohelper

from ....domain.mocks import mock_add_account_params

class TestAccountMongoRepository:
  # SetUp
  params: AddAccountParams = mock_add_account_params()
  mongohelper.connect(mongomock.MongoClient())

  def make_sut(self) -> AccountMongoRepository:
    return AccountMongoRepository()

  @pytest.fixture
  def clear_db(self) -> None:
    collection = mongohelper.get_collection(
      database='surveys',
      collection='accounts'
    )
    collection.delete_many({})

  def test_1_should_return_an_account_on_success(self, clear_db):
    sut = self.make_sut()

    is_valid = sut.add(dict(self.params))

    assert is_valid

  def test_2_should_return_true_if_email_is_valid(self, clear_db):
    sut = self.make_sut()
    collections = mongohelper.get_collection(
      database='surveys',
      collection='accounts'
    )
    collections.insert_one(self.params)

    exists = sut.check_by_email(self.params['email'])
    assert exists
