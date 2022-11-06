from dataclasses import dataclass
from pymongo import MongoClient
from pymongo.collection import Collection

from ....data.params import AddAccountRepositoryParams
from ....data.contracts.db import AddAccountRepository

@dataclass
class AccountMongoRepository(AddAccountRepository):
  client: MongoClient = MongoClient()

  @classmethod
  def get_collection(cls, client: MongoClient) -> Collection:
    return client['surveys']['accounts']

  def add(self, data: AddAccountRepositoryParams) -> bool:
    account_collection = self.get_collection(client=self.client)
    result = account_collection.insert_one(dict(data))
    return result.inserted_id

  def check_by_email(self, email: str) -> bool:
    account_collection = self.get_collection(client=self.client)
    account = account_collection.find_one({'email': email})
    return account is not None
