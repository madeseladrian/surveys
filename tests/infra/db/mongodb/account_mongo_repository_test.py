import mongomock
from unittest.mock import patch

from src.domain.params import AddAccountParams
from src.infra.db.mongo import AccountMongoRepository

from ....domain.mocks import mock_add_account_params

class TestAccountMongoRepository:
  # SetUp
  params: AddAccountParams = mock_add_account_params()

  def make_sut(self) -> AccountMongoRepository:
    return AccountMongoRepository()

  @patch('src.infra.db.mongo.AccountMongoRepository.client')
  def test_1_should_return_an_account_on_success(self, mocker):
    mocker.return_value = mongomock.MongoClient()

    sut = self.make_sut()
    addAccountParams = self.params
    isValid = sut.add(dict(addAccountParams))

    assert isValid
