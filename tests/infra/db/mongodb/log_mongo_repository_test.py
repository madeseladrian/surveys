from faker import Faker
import mongomock

from src.infra.db.mongodb import LogMongoRepository


class TestLogMongoRepository:
  faker = Faker()

  def make_sut(self) -> LogMongoRepository:
    return LogMongoRepository()

  def test_1_should_create_an_error_log_on_success(self):
    error = self.faker.word()
    sut = self.make_sut()
    sut.client = mongomock.MongoClient()
    sut.log_error(error=error)

    count = sut.client.surveys.errors.count_documents({})
    log = sut.client.surveys.errors.find_one({})

    assert count == 1
    assert log['log'] == error
