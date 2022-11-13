from pymongo import MongoClient
from pymongo.collection import Collection


def get_collection(client: MongoClient, name: str) -> Collection:
  return client['surveys'][name]
