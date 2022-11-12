from pymongo import MongoClient
from src.main.config.database import get_db, uri

class TestDabase:
  def test_1_should_get_db_return_a_database_with_uri(self):
    assert next(get_db()) == MongoClient(uri)
