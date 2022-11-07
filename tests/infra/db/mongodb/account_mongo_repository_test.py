import mongomock
from pymongo import MongoClient
import pytest

from src.domain.params import AddAccountParams
from src.infra.db.mongo import AccountMongoRepository

from ....domain.mocks import mock_add_account_params

class TestAccountMongoRepository:
  # SetUp
  params: AddAccountParams = mock_add_account_params()
  mock_mongo_client: MongoClient = mongomock.MongoClient()

  def make_sut(self) -> AccountMongoRepository:
    account_mongo_repository = AccountMongoRepository()
    account_mongo_repository.client = self.mock_mongo_client
    return account_mongo_repository

  @pytest.fixture
  def insert_one(self):
    sut = self.make_sut()
    sut.get_collection(client=self.mock_mongo_client).insert_one(self.params)

  @pytest.fixture
  def clear_db(self):
    sut = self.make_sut()
    sut.get_collection(client=self.mock_mongo_client).delete_many({})

  def test_1_should_return_an_account_on_success(self, clear_db):
    sut = self.make_sut()
    is_valid = sut.add(dict(self.params))

    assert is_valid

  def test_2_should_return_true_if_email_is_valid(self, clear_db, insert_one):
    sut = self.make_sut()
    add_account_params = self.params
    exists = sut.check_by_email(add_account_params['email'])

    assert exists
