from dataclasses import dataclass
import datetime
from pymongo import MongoClient

from ....data.contracts.db.log import LogErrorRepository
from .mongo_helper import get_collection


@dataclass
class LogMongoRepository(LogErrorRepository):
  client: MongoClient = MongoClient()

  def log_error(self, stack: str) -> None:
    error_collection = get_collection(client=self.client, name='errors')
    error_collection.insert_one({
      'log': stack,
      'date': datetime.datetime.now()
    })
