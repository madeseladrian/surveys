from dataclasses import dataclass
from pymongo import MongoClient
from pymongo.collection import Collection


@dataclass
class MongoHelper:
    client: MongoClient = None

    def connect(self, client: MongoClient) -> None:
        self.client = client

    def get_collection(self, database: str, collection: str) -> Collection:
        return self.client[database][collection]

mongohelper = MongoHelper()
