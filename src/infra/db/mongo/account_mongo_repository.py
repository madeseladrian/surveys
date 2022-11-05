from dataclasses import dataclass
from pymongo import MongoClient
from pymongo.collection import Collection

from ....data.params import AddAccountRepositoryParams

@dataclass
class AccountMongoRepository:
  client: MongoClient = MongoClient()

  @classmethod
  def get_collection(cls, database: str, collection: str) -> Collection:
    return cls.client[database][collection]

  def add(self, data: AddAccountRepositoryParams) -> bool:
    account_collection = self.get_collection(
      database='accounts',
      collection='customers'
    )
    result = account_collection.insert_one(dict(data))
    return result.inserted_id
