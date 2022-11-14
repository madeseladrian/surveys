from dataclasses import dataclass

from ....data.contracts.db.account import AddAccountRepository, CheckAccountByEmailRepository
from ....data.params import AddAccountRepositoryParams, AddAccountRepositoryResult
from .mongo_helper import mongohelper

@dataclass
class AccountMongoRepository(AddAccountRepository, CheckAccountByEmailRepository):

  def add(self, data: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
    account_collection = mongohelper.get_collection(
      database='surveys',
      collection='accounts'
    )
    result = account_collection.insert_one(dict(data))
    return result.inserted_id is not None

  def check_by_email(self, email: str) -> bool:
    account_collection = mongohelper.get_collection(
      database='surveys',
      collection='accounts'
    )
    account = account_collection.find_one({'email': email})
    return account is not None
