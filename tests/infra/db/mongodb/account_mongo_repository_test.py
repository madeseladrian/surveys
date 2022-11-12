import mongomock

from src.domain.params import AddAccountParams
from src.infra.db.mongo import AccountMongoRepository

from ....domain.mocks import mock_add_account_params

class TestAccountMongoRepository:
  # SetUp
  params: AddAccountParams = mock_add_account_params()

  def make_sut(self) -> AccountMongoRepository:
    return AccountMongoRepository()

  def test_1_should_return_an_account_on_success(self):
    sut = self.make_sut()
    sut.client = mongomock.MongoClient()

    is_valid = sut.add(dict(self.params))

    assert is_valid

  def test_2_should_return_true_if_email_is_valid(self):
    sut = self.make_sut()
    sut.client = mongomock.MongoClient()
    collections = sut.client['surveys']['accounts']
    collections.insert_one(self.params)

    exists = sut.check_by_email(self.params['email'])
    assert exists
