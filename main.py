from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from src.infra.db.mongodb import mongohelper
from src.main.config import create_app, uri


try:
    mongohelper.connect(MongoClient(uri))
    mongohelper.client.server_info()
    app = create_app()
except ServerSelectionTimeoutError as e:
    print('Server is down')
    print(e)
