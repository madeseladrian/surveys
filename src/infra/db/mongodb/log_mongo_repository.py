from dataclasses import dataclass
import datetime
from typing import Any

from ....data.contracts.db.log import LogErrorRepository
from .mongo_helper import mongohelper


@dataclass
class LogMongoRepository(LogErrorRepository):

    def log_error(self, error: Any) -> None:
        error_collection = mongohelper.get_collection(collection='errors')
        error_collection.insert_one({
            'log': str(error),
            'date': datetime.datetime.now()
        })
