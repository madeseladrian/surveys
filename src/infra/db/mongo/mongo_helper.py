from dataclasses import dataclass
from pymongo import MongoClient
from pymongo.collection import Collection

@dataclass
class MongoHelper:
  client: MongoClient = MongoClient()
  uri: str = ''

  def connect(self, uri: str) -> None:
    self.uri = uri
    self.client = MongoClient(uri)

  def get_collection(self, database: str, collection: str) -> Collection:
    return self.client[database][collection]
