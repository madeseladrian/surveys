from dataclasses import dataclass
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Any, Dict


@dataclass
class MongoHelper:
    client: MongoClient = MongoClient()

    def connect(self, client: MongoClient) -> None:
        self.client = client

    def get_collection(self, collection: str) -> Collection:
        return self.client['surveys'][collection]

    def map_collection(self, data: Dict) -> Any:
        data['id'] = str(data['_id'])
        data.pop('_id')
        return data

mongohelper = MongoHelper()
