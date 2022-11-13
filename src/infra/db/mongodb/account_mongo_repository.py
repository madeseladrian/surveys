from dataclasses import dataclass
from pymongo import MongoClient

from ....data.contracts.db.account import AddAccountRepository, CheckAccountByEmailRepository
from ....data.params import AddAccountRepositoryParams, AddAccountRepositoryResult
from .mongo_helper import get_collection

@dataclass
class AccountMongoRepository(AddAccountRepository, CheckAccountByEmailRepository):
  client: MongoClient = MongoClient()

  def add(self, data: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
    account_collection = get_collection(client=self.client, name='accounts')
    result = account_collection.insert_one(dict(data))
    return result.inserted_id is not None

  def check_by_email(self, email: str) -> bool:
    account_collection = get_collection(client=self.client, name='accounts')
    account = account_collection.find_one({'email': email})
    return account is not None
