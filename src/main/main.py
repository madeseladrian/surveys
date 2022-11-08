from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from .config import create_app

app = FastAPI(
  title='Surveys',
  version='1.0.0'
)

client: MongoClient = MongoClient("mongodb://localhost:27017/")

try:
  client.server_info()
  create_app(app=app)
except ServerSelectionTimeoutError as err:
  print(err)
