from mongomock import MongoClient

def mock_get_db():
  client: MongoClient = MongoClient()
  try:
    yield client
  finally:
    client.close()
