from .config import create_app
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from ..infra.db.mongodb import mongohelper
from .config import uri


try:
  mongohelper.connect(MongoClient(uri))
  mongohelper.client.server_info()
  app = create_app()
except ServerSelectionTimeoutError as e:
  print('Server is down')
  print(e)
