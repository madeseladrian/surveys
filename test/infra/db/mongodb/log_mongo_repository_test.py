from faker import Faker
import mongomock

from src.infra.db.mongodb import LogMongoRepository, mongohelper


class TestLogMongoRepository:
    faker = Faker()
    error = faker.word()
    mongohelper.connect(mongomock.MongoClient())

    def make_sut(self) -> LogMongoRepository:
        return LogMongoRepository()

    def test_1_should_create_an_error_log_on_success(self):
        sut = self.make_sut()
        sut.log_error(self.error)

        collection = mongohelper.client['surveys']['errors']
        count = collection.count_documents({})
        log = collection.find_one({})

        assert count == 1
        assert log['log'] == self.error
