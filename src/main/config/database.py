from pydantic import BaseSettings
from pymongo import MongoClient


class Settings(BaseSettings):
  database_hostname: str
  database_port: str
  database_username: str
  database_password: str

  class Config:
    env_file = '.env'

settings = Settings()

uri: str = f'mongodb://\
{settings.database_hostname}:\
{settings.database_port}'

def get_db():
  client: MongoClient = MongoClient(uri)
  try:
    yield client
  finally:
    client.close()
