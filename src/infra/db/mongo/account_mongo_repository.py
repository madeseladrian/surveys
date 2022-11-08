from dataclasses import dataclass
from pymongo import MongoClient
from pymongo.collection import Collection

from ....data.contracts.db import AddAccountRepository, CheckAccountByEmailRepository
from ....data.params import AddAccountRepositoryParams, AddAccountRepositoryResult

@dataclass
class AccountMongoRepository(AddAccountRepository, CheckAccountByEmailRepository):
  client: MongoClient = MongoClient()

  @classmethod
  def get_collection(cls, client: MongoClient) -> Collection:
    return client['surveys']['accounts']

  def add(self, data: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
    account_collection = self.get_collection(client=self.client)
    result = account_collection.insert_one(dict(data))
    return result.inserted_id is not None

  def check_by_email(self, email: str) -> bool:
    account_collection = self.get_collection(client=self.client)
    account = account_collection.find_one({'email': email})
    return account is not None
